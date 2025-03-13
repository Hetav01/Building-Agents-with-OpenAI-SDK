import os
import logging
from dotenv import load_dotenv
from agents import set_default_openai_key

def load_api_keys():
    # Load environment variables and setup API keys
    load_dotenv()
    
    # setup openai api key
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OpenAI API key not found in environment variables.")
    
    set_default_openai_key(openai_api_key)
    
    # Check for tavily api key
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if not tavily_api_key:
        raise ValueError("Tavily API key not found in environment variables.")
    
    return {"openai_api_key": openai_api_key, "tavily_api_key": tavily_api_key}

# Format search results helper
def format_document_length(text):
    """Add document length indicator to help assess completeness"""
    doc_length = len(text.split())

    if doc_length < 50:
        return "(very brief)"
    elif doc_length > 200:
        return "(detailed)"
    return ""


def setup_logs():
    # Setup logging for the application
    # Set to WARNING level to suppress INFO logs
    logging.basicConfig(
        level = logging.WARNING,
        format= "%(asctime)s - %(levelname)s - %(message)s",
    )
    
    return logging.getLogger("founder_agent")