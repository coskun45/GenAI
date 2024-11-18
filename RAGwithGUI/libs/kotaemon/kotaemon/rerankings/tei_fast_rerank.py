from __future__ import annotations

from typing import Optional

import requests

from kotaemon.base import Document, Param

from .base import BaseReranking

session = requests.session()


class TeiFastReranking(BaseReranking):
    """Text Embeddings Inference (TEI) Reranking model
    (https://huggingface.co/docs/text-embeddings-inference/en/index)
    """

    endpoint_url: str = Param(
        None, help="TEI Reranking service api base URL", required=True
    )
    model_name: Optional[str] = Param(
        None,
        help=(
            "ID of the model to use. You can go to [Supported Models]"
            "(https://github.com/huggingface"
            "/text-embeddings-inference?tab=readme-ov-file"
            "#supported-models) to see the supported models"
        ),
    )
    is_truncated: Optional[bool] = Param(True, help="Whether to truncate the inputs")

    def client(self, query, texts):
        response = session.post(
            url=self.endpoint_url,
            json={
                "query": query,
                "texts": texts,
                "is_truncated": self.is_truncated,  # default is True
            },
        ).json()
        return response

    def run(self, documents: list[Document], query: str) -> list[Document]:
        """Use the deployed TEI rerankings service to re-order documents
        with their relevance score"""
        if not self.endpoint_url:
            print("TEI API reranking URL not found. Skipping rerankings.")
            return documents

        compressed_docs: list[Document] = []

        if not documents:  # to avoid empty api call
            return compressed_docs

        if isinstance(documents[0], str):
            documents = self.prepare_input(documents)

        batch_size = 6
        num_batch = max(len(documents) // batch_size, 1)
        for i in range(num_batch):
            if i == num_batch - 1:
                mini_batch = documents[batch_size * i :]
            else:
                mini_batch = documents[batch_size * i : batch_size * (i + 1)]

            _docs = [d.content for d in mini_batch]
            rerank_resp = self.client(query, _docs)
            for r in rerank_resp:
                doc = mini_batch[r["index"]]
                doc.metadata["reranking_score"] = r["score"]
                compressed_docs.append(doc)

        compressed_docs = sorted(
            compressed_docs, key=lambda x: x.metadata["reranking_score"], reverse=True
        )
        return compressed_docs
