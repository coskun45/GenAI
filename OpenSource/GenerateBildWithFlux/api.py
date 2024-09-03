import requests
import os
from dotenv import load_dotenv

# .env dosyasını yüklemek için bu komutu kullan
load_dotenv()

# Yüklenen bir çevresel değişkene erişmek için
key= os.getenv("HUGGING_FACE")

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
headers = {"Authorization": f"Bearer {key}"}
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": "Astronaut riding a horse",
})
print(image_bytes)
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))
try:
    image = Image.open(io.BytesIO(image_bytes))
    image.show()  # Eğer resim açılamazsa bu satır çalışmayacaktır
except Image.UnidentifiedImageError:
    print("The provided bytes could not be identified as an image.")