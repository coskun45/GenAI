from pandasai.llm.openai import OpenAI
import streamlit as st
from pandasai.connectors import MySQLConnector
from pandasai import SmartDataframe

# MySQL Bağlantısı
my_connector = MySQLConnector(
    config={
        "host": "localhost",
        "port": 3306,
        "database": "demo",
        "username": "root",
        "password": "Ec.294086",
        "table": "versicherung",
    }
)

# OpenAI Modeli ile LLM
model = OpenAI(api_token="")  # OpenAI API anahtarınızı buraya ekleyin

# SmartDataframe Tanımlama
df_connector = SmartDataframe(my_connector, config={"llm": model})

# Streamlit Başlık
st.title("Talk to your Database")

# Kullanıcıdan girdi almak
prompt = st.text_input("Enter your prompt:")

# Butona basıldığında modeli çalıştırmak
if st.button("Generate"):
    import os

    chart_path = "C:/Users/ecoskun/Desktop/githubUpload/GenAI/OpenSource/MySQLwithPandasAIOllamaStreamlit/exports/charts/temp_chart.png"

# Dosyanın mevcut olup olmadığını kontrol et
    if os.path.exists(chart_path):
        os.remove(chart_path)  # Dosyayı sil
        print(f"{chart_path} başarıyla silindi.")
    else:
        print(f"{chart_path} mevcut değil.")

    if prompt:
        with st.spinner("Generating response..."):
            response=df_connector.chat(prompt)
            print("Prompt: ", prompt)
            print("response: ",response)
            if os.path.exists(chart_path):
                st.image(response, caption="Generated Chart", use_column_width=True)
            else:
                st.write(response)
