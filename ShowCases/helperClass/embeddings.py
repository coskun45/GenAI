import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from langchain_openai import AzureOpenAIEmbeddings
import credentials


def get_openAI_embedding_model():
    embedding_model = AzureOpenAIEmbeddings(
        model="text-embedding-ada-002",
        azure_endpoint =credentials.AZURE_OPENAI_ENDPOINT,
        api_key=credentials.OPENAI_API_KEY)
    return embedding_model