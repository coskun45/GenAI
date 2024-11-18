import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from helperClass import llms, embeddings


llm = llms.get_azure_openAI()
res=llm.invoke("hallo")
print(res.content)

embedding_model = embeddings.get_openAI_embedding_model()

print(embedding_model.embed_query("hallo"))
