import os
import openai
from dotenv import load_dotenv, find_dotenv

# Step 1: Load environment variables
_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

# Step 2: Load required libraries
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import OpenAIWhisperParser
from langchain_community.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader

# Step 3: Define the YouTube URL and save directory
url = "https://www.youtube.com/watch?v=SM66GDRyIVY"
save_dir = "Docs/Youtube/"
os.makedirs(save_dir, exist_ok=True)  # Ensure the directory exists

# Step 4: Set yt_dlp options
yt_dlp_opts = {
    'nocheckcertificate': True,
    'format': 'bestaudio/best',
    'outtmpl': save_dir + '%(id)s.%(ext)s',
}

# Step 5: Initialize the loader
loader = GenericLoader(
    YoutubeAudioLoader([url], save_dir),
    OpenAIWhisperParser()
)

# Step 6: Load the documents
try:
    docs = loader.load()
    print(f"Number of documents loaded: {len(docs)}")
except Exception as e:
    print(f"Error: {e}")
