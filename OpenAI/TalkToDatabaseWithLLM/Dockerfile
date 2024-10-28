# Base image olarak Python 3.12.5 kullanılıyor
FROM python:3.12.5

# Çalışma dizinini ayarla
WORKDIR /app

# requirements.txt dosyasını çalışma dizinine kopyala
COPY requirements.txt .

# Gereksinimleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Tüm proje dosyalarını çalışma dizinine kopyala
COPY . .

# Streamlit uygulamasını dışarıya aç
EXPOSE 8501

# Streamlit'i başlat
CMD ["streamlit", "run", "app.py"]
