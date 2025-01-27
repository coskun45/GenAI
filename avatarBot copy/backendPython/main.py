import os
import json
import subprocess
import base64
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
from openai import OpenAI
import time
import requests
from pydub import AudioSegment
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 
#CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI and ElevenLabs API keys
openai.api_key = os.getenv("OPENAI_API_KEY")
eleven_labs_api_key = os.getenv("ELEVEN_LABS_API_KEY")
voice_id = "Xb7hH8MSUJpSbSDYk0k2"#"kgG7dCoKCfLehAPWkJOE"  # Provided voice ID for ElevenLabs


# Helper functions
def exec_command(command):
    """Execute a shell command."""
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        raise Exception(f"Command failed: {e}")

def lip_sync_message(message_id):
    """Perform lip-sync using FFmpeg and Rhubarb."""
    current_time = int(round(time.time() * 1000))
    print(f"Starting conversion for message {message_id}")
    
    # Convert MP3 to WAV
    exec_command(f'C:/ffmpeg/bin/ffmpeg.exe -y -i audios/message_{message_id}.mp3 audios/message_{message_id}.wav')
    print(f"Conversion done in {int(round(time.time() * 1000)) - current_time}ms")
    
    # Generate lip-sync JSON with Rhubarb
    exec_command(f'C:/rhurbab/rhubarb.exe -f json -o audios/message_{message_id}.json audios/message_{message_id}.wav -r phonetic')
    print(f"Lip sync done in {int(round(time.time() * 1000)) - current_time}ms")

def read_json_transcript(file):
    """Read JSON transcript from file."""
    with open(file, 'r') as f:
        return json.load(f)

def audio_file_to_base64(file_path):
    """Convert an audio file to Base64."""
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

# def text_to_speech(text, message_id):
#     """Call ElevenLabs API to generate speech."""
#     url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
#     headers = {
#         "xi-api-key": eleven_labs_api_key,
#         "Content-Type": "application/json"
#     }
#     data = {
#         "text": text,
#         "language_code": "de",
#         "voice_settings": {
#             "stability": 0.5,
#             "similarity_boost": 0.7
#         }
#     }
    
#     response = requests.post(url, json=data, headers=headers)
#     if response.status_code == 200:
#         with open(f"audios/message_{message_id}.mp3", "wb") as f:
#             f.write(response.content)
#     else:
#         raise Exception(f"Failed to generate speech: {response.status_code} {response.text}")
    
def text_to_speech(text,message_id):
    client = OpenAI()
    speech_response = client.audio.speech.create(
                model="tts-1",
                voice="nova",
                input=text
            )
    speech_response.write_to_file(f"audios/message_{message_id}.mp3")

@app.route("/", methods=["GET"])
def home():
    return "Hello World!"

@app.route("/voices", methods=["GET"])
def get_voices():
    url = "https://api.elevenlabs.io/v1/voices"
    headers = {"xi-api-key": eleven_labs_api_key}
    response = requests.get(url, headers=headers)
    return jsonify(response.json())

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get('message')
    print(type(user_message))
    print(user_message)
    if not user_message:
        print("if")
        return jsonify({
            "messages": [
                {
                    "text": "Hey dear... How was your day?",
                    "audio": audio_file_to_base64("audios/intro_0.wav"),
                    "lipsync": read_json_transcript("audios/intro_0.json"),
                    "facialExpression": "smile",
                    "animation": "Talking_1"
                },
                {
                    "text": "I missed you so much... Please don't go for so long!",
                    "audio": audio_file_to_base64("audios/intro_1.wav"),
                    "lipsync": read_json_transcript("audios/intro_1.json"),
                    "facialExpression": "sad",
                    "animation": "Crying"
                }
            ]
        })

    if not eleven_labs_api_key or openai.api_key == "-":
        return jsonify({
            "messages": [
                {
                    "text": "Please my dear, don't forget to add your API keys!",
                    "audio": audio_file_to_base64("audios/api_0.wav"),
                    "lipsync": read_json_transcript("audios/api_0.json"),
                    "facialExpression": "angry",
                    "animation": "Angry"
                },
                {
                    "text": "You don't want to ruin Wawa Sensei with a crazy ChatGPT and ElevenLabs bill, right?",
                    "audio": audio_file_to_base64("audios/api_1.wav"),
                    "lipsync": read_json_transcript("audios/api_1.json"),
                    "facialExpression": "smile",
                    "animation": "Laughing"
                }
            ]
        })
    
    # OpenAI API call for generating messages
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """
                You are a virtual insurance assistant. 
                You will always reply with a JSON array of messages.
                Answer in German.
                Each message has a text, facialExpression, and animation property. Possible animations: 'Angry', 'Crying', 'Idle', 'Laughing', 'Rumba', 'Talking_0', 'Talking_1', 'Talking_2', 'Terrified'
            """},
            {"role": "user", "content": user_message}
        ]
    )
    
    messages = json.loads(completion.choices[0].message.content)
    print("messages length: ", len(messages))
    response=[]
    for i, message in enumerate(messages):
        # Generate audio file
        
        print("mesaj",message['text'])
        text_to_speech(message['text'], i)
        
        # Generate lip-sync JSON
        lip_sync_message(i)
        
        
        mes= {
                    "text": message['text'],
                    "audio": audio_file_to_base64(f"audios/message_{i}.wav"),
                    "lipsync": read_json_transcript(f"audios/message_{i}.json"),
                    "facialExpression": message['facialExpression'],
                    "animation": message['animation']
            }
        if(mes['facialExpression']==None):
            mes['facialExpression']= "smile"
        if(mes['animation']==None):
            mes['animation']= "Laughing"
        response.append(mes)
    return jsonify({"messages": response})

if __name__ == "__main__":
    app.run(port=3000)
