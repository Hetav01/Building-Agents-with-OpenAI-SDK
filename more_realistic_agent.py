import asyncio
from agents import Agent, Runner

from prompts import FOUNDER_AGENT_INSTRUCTIONS
from dotenv import load_dotenv
from agents import set_default_openai_key
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
set_default_openai_key(openai_api_key)

