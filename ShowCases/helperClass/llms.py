import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_together import ChatTogether
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()



GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY')
OPENAI_KEY = os.getenv('OPENAI_KEY')

# def get_azure_openAI():
#     azure_llm = AzureChatOpenAI(
#             deployment_name=AZURE_MODEL_NAME,
#             temperature=0,
#             max_tokens=None,
#             api_version=AZURE_API_VERSION,
#             azure_endpoint =AZURE_OPENAI_ENDPOINT,
#             api_key=AZURE_OPENAI_API_KEY,

#         )
#     return azure_llm

def get_openAI():
    openAI_llm = ChatOpenAI(
            temperature=0,
            api_key=OPENAI_KEY,

        )
    return openAI_llm

def google_gemini():
    client = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            api_key=GOOGLE_API_KEY,
        )
    return client

def llama3_405B():
    TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY')
    client = ChatTogether(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=TOGETHER_API_KEY,
    )
    return client
