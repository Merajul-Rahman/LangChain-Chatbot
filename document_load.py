#step1: Install LangChain  
#! pip install langchain
#step2: Load the required libraries.
import os

import openai

import sys
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

#set openai api_key set OPENAI_API_KEY="key" in cmd
openai.api_key  = os.environ['OPENAI_API_KEY']

from langchain_community.document_loaders import PyPDFLoader



#step3: load pdf type files
loader = PyPDFLoader("E:\OneDrive - Masco Group\Shipon\Github\LangChain-Chatbot\CV_MD_MERAJUL_RAHMAN_CSE_RUET.pdf")
pages = loader.load()

page =pages[0]

print(page.page_content[:500])

print(len(pages))


# Load from a website page.
from langchain_community.document_loaders import WebBaseLoader

# Pass the session to WebBaseLoader
website_loader = WebBaseLoader(
    "https://sports.mascoknit.com/details.php?match_id=127"
)

# Now use the session to load the data
web_data = website_loader.load()

print(web_data[:500])

