from langchain_community.llms import Ollama
import streamlit as st
llm=Ollama(model="llama3:latest")

st.title("Chabot using Llama3")

prompt=st.text_area("Enter your prompt: ")

if st.button("Generate"):
    if prompt:
        with st.spinner("generating response..."):
            st.write(llm.stream(prompt, stop=['<|eot_id|>']))