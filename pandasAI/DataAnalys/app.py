import streamlit as st 
from langchain_community.llms import Ollama
import pandas as pd
from pandasai import SmartDataframe

llm=Ollama(model="mistral:latest")

st.title("Data Analysis with PandasAI")

uploader_file = st.file_uploader("Upluad a CSV file", type= ["CSV"])

if uploader_file is not None:
    data=pd.read_csv(uploader_file)
    st.write(data.head())
    df = SmartDataframe(data, config={"llm":llm})
    promt= st.text_area("Enter your prompt:")

    if st.button("Generate"):
        if promt:
            with st.spinner("Generative response..."):
                st.write(df.chat(promt))
        else:
            st.warning("Please enter a prompt!")

