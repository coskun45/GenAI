import torch
from transformers import ( AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline, )
from langchain import HuggingFacePipeline
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain.retrievers import BM25Retriever, EnsembleRetriever

model_name = "HuggingFaceH4/zephyr-7b-beta"


def data_load_split():
    
    loader = PyPDFLoader("./ragNLP.pdf")
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=30)
    chunks = splitter.split_documents(docs)
    return chunks

def embedding(chunks):
    
    HUGGING_FACE="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"
    embeddings = HuggingFaceInferenceAPIEmbeddings(api_key=HUGGING_FACE,model_name="BAAI/bge-base-en-v1.5")
    from langchain.vectorstores import Chroma
    vectorstore = Chroma.from_documents(chunks,embeddings)
    vectorstore_retriever = vectorstore.as_retriever(search_kwargs={"k":3})
    
    keyword_retriever = BM25Retriever.from_documents(chunks)
    keyword_retriever.k = 3
    retriever = EnsembleRetriever(retrievers=[vectorstore_retriever,keyword_retriever],weights=[0.3,0.7])
    return retriever

def load_quantized_model(model_name: str="HuggingFaceH4/zephyr-7b-beta"):
    
    """
    model_name: Name or path of the model to be loaded.
    return: Loaded quantized model.
    """
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
        quantization_config=bnb_config,
    )
    return model

def initialize_tokenizer(model_name: str):
    """
    model_name: Name or path of the model for tokenizer initialization.
    return: Initialized tokenizer.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name, return_token_type_ids=False)
    tokenizer.bos_token_id = 1  # Set beginning of sentence token id
    return tokenizer

model = load_quantized_model()
tokenizer = initialize_tokenizer(model_name)

pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    use_cache=True,
    device_map="auto",
    max_length=2048,
    do_sample=True,
    top_k=5,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    pad_token_id=tokenizer.pad_token_id,
)