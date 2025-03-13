import os
import logging
from dotenv import load_dotenv
from agents import set_default_openai_key

def load_api_keys():
    # Load environment variables and setup API keys
    load_dotenv()
    
    # setup openai api key
    