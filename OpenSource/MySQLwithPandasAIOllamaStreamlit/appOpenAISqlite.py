from pandasai.llm.openai import OpenAI
import streamlit as st
from pandasai.connectors import MySQLConnector
from pandasai import SmartDataframe
from pandasai.agent import Agent
from pandasai.connectors import SqliteConnector
from pandasai.ee.connectors.relations import ForeignKey, PrimaryKey

# MySQL Bağlantısı
sqlite_db_path = "./my_demo.db"  # SQLite veritabanı dosya yolunu buraya ekleyin

dept_connector = SqliteConnector(
    config={
    "database" : "my_demo.db",
    "table" : "dept"
},
    connector_relations=[
        PrimaryKey("deptno"),
        ForeignKey(
            field="empno", 
            foreign_table="emp", foreign_table_field="deptno"
        ),
    ],
)

emp_connector = SqliteConnector(
    config={
    "database" : "my_demo.db",
    "table" : "emp"
},
connector_relations=[PrimaryKey("empno")],
    
)


# OpenAI Modeli ile LLM
llm = OpenAI(api_token="")  
config_ = {"llm": llm, "direct_sql": True}

# SmartDataframe Tanımlama
agent = Agent([emp_connector, dept_connector], config=config_, memory_size=10)

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
            response=agent.chat(prompt)
            print("Prompt: ", prompt)
            print("response: ",response)
            if os.path.exists(chart_path):
                st.image(response, caption="Generated Chart", use_column_width=True)
            else:
                st.write(response)
