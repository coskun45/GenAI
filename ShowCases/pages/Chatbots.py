import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from helperClass import llms
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

# Dil modeli seçenekleri
MODEL_OPTIONS = {
    "OpenAI GPT-3.5": "openai",
    "Gemini 1.5 Pro": "gemini",
    "LLaMA 3.1-405M": "llama"
}
selected_model = st.sidebar.selectbox("Choose a model:", list(MODEL_OPTIONS.keys()))

# Eğer seçilen model daha önceki seçimden farklıysa, mesajları sıfırla
if "last_selected_model" in st.session_state:
    if st.session_state["last_selected_model"] != selected_model:
        st.session_state["messages"] = [{"role": "assistant", "content": f"You are chatting with {selected_model}. How can I assist you?"}]

# Seçilen modeli kaydet
st.session_state["last_selected_model"] = selected_model

# Model'e göre API setup
if selected_model == "OpenAI GPT-3.5":
    client = llms.get_openAI()

elif selected_model == "Gemini 1.5 Pro":
    client = llms.google_gemini()

elif selected_model == "LLaMA 3.1-405M":
    client = llms.llama3_405B()

st.title(f"💬 Chatbot - {selected_model}")
st.caption(f"🚀 A chatbot powered by {selected_model}")

# Mesajları session state ile saklıyoruz
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": f"You are chatting with {selected_model}. How can I assist you?"}]

# Önceki mesajları ekrana yazdır
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Kullanıcıdan input al
if question := st.chat_input("Send a message..."):
    st.session_state.messages.append({"role": "user", "content": question})
    st.chat_message("user").write(question)

    prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an intelligent assistant that provides accurate and concise answers to questions.",
        ),
        ("human", "Please answer the following question: {question}"),
    ]
    )

    # Format metodunu kullanarak prompt'u oluşturma
    formatted_prompt = prompt.format_prompt(question=question)  # format_prompt metodunu kullanın

    # LLM ile yanıt alma
    response = client(formatted_prompt.messages)  # LLM'e mesajları geçme
    msg=response.content
    
    # API'den gelen yanıtı göster ve kaydet
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
