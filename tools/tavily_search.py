"""
Custom search tool using Tavily API to find information about founders.
"""
    
import os
import asyncio
from typing import Optional
from dotenv import load_dotenv
import logging

from agents import function_tool, RunContextWrapper

# Configure logging
logger = logging.getLogger("tavily_search")

# Load environment variables
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

try:
    from tavily import TavilyClient
    
    tavily_client = TavilyClient(api_key=TAVILY_API_KEY)
    TAVILY_AVALIABLE = True

except ImportError as e:
    TAVILY_AVALIABLE = False
    logger.warning("tavily module not found. Please install it using pip install tavily-python to use this search tool.")

except Exception as e:
    TAVILY_AVALIABLE = False
    logger.error(f"Error initializing Tavily client: {e}")


async def search_tavily(query: str, max_results: int = 5) -> str:
    """
    Internal function to search Tavily for information about founders.
    """
    from tavily import TavilyClient
    # intiialize Tavily client
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if not tavily_api_key:
        raise "Error: Tavily API key not found. Please set the TAVILY_API_KEY environment variable."
    
    tavily_client = TavilyClient(api_key=tavily_api_key)
    
    try: 
        # call the tavily api using the client
        response = tavily_client.search(
            api_key=tavily_api_key,
            search_depth= "basic",
            max_results=max_results
        )
        
        if not response or "results" not in response:
            return f"No results found for query: {query}"
        
        #format the results
        result_text = f"Web Search results for '{query}':\n\n"
        
        for i, result in enumerate(response["results"]):
            result_text += f"{i + 1}. {result.get('title', 'No Title')}\n\n"
            result_text += f"   URL: {result.get('url', 'No URL')}\n\n"
            result_text += f"   {result.get('content', 'No content available')}\n\n"
            
        return result_text
    
    except Exception as e:
        return f"Error during Tavily search: {str(e)}"
    
@function_tool
async def tavily_search(ctx: RunContextWrapper, query: str, max_results: Optional[int] = None) -> str:
    """
    Search the web for information using Tavily search engine.

    Args:
        query: The search query to find information on the web
        max_results: Number of results to return (between 1 and 10)
        search_depth: Depth of search, either "basic" for faster results or "comprehensive" for more thorough search

    Returns:
        Information found on the web related to the query
    """
    # Set the tool name in context
    ctx.context.set_last_tool("tavily_search")
    
    # Apply defaults inside the function
    if max_results is None:
        max_results = 5
        
    return await search_tavily(query, max_results=max_results)