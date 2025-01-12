#step1: Install LangChain  
#! pip install langchain
#step2: Load the required libraries.
import os

import openai

import sys
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

from langchain.document_loaders import PyPDFLoader

#step3: load pdf type files
loader = PyPDFLoader("E:\OneDrive - Masco Group\Shipon\Github\LangChain-Chatbot\CV_MD_MERAJUL_RAHMAN_CSE_RUET.pdf")
pages = loader.load()