import os
import requests
from dotenv import load_dotenv

from agents import function_tool, RunContextWrapper

# Import from models instead of defining here
from models import RetrievalResponse
from agent_context import AgentContext
from utils import format_document_length

load_dotenv()

retrieval_endpoint = os.getenv("VECTORIZE_ENDPOINT")
if retrieval_endpoint is None:
    raise ValueError("VECTORIZE_ENDPOINT environment variable is not set")

headers = {
    "Content-Type": "application/json",
    "Authorization": os.getenv("VECTORIZE_TOKEN"),
}
 
# function to retrieve documents from the vector store
def retrieve_documents(question: str, num_results: int = 10, rerank: bool = False) -> RetrievalResponse:
    """
    Retrieve documents from Vectorize

    Args:
        question: The search query
        num_results: Number of results to return (default: 10)
        rerank: Whether to use Vectorize's built-in reranking (default: False)

    Returns:
        Retrieval response with documents
    """
    print(f"Searching for documents related to: {question}")

    # Prepare data payload
    retrieval_data = {
        "question": question,
        "numResults": num_results,
        "rerank": rerank,
    }
    
    # Ensure endpoint is not None
    if retrieval_endpoint is None:
        raise ValueError("Retrieval endpoint cannot be None")
    
    # Make the API request
    response = requests.post(retrieval_endpoint, headers=headers, json=retrieval_data)
    response.raise_for_status()  # Raise an error for bad responses
    result_json = response.json()
    
    return RetrievalResponse(**result_json)  # Parse the JSON response into a RetrievalResponse object

# Create a function tool for document retrieval
@function_tool
async def search_founder_articles(ctx: RunContextWrapper, query: str, num_results: int, use_reranking: bool) -> str:
    """
    Search for founder-related articles matching the query.

    Args:
        query: The search query about founders
        num_results: Number of results to return
        use_reranking: Whether to use reranking for better results

    Returns:
        Information from relevant founder articles with quality assessment
    """
    try:
        # Set the tool name in context
        ctx.context.set_last_tool("founder_articles")

        # Track this search in our context
        ctx.context.add_search(query)

        # Call the retrieval function
        result = retrieve_documents(
            question=query, num_results=num_results, rerank=use_reranking
        )

        # Store documents in context
        if result.documents:
            ctx.context.add_documents(result.documents)
            
        # if we found documents, return them with quality information
        if result.documents:
            response = f"Here's what I found about '{query}':\n\n"
            
            # Add overall document information
            response += f"DOCUMENT INFORMATION:\n"
            response += f"- Document count: {len(result.documents)}\n"
            response += "- Content assessment: You must evaluate if these documents actually answer the question completely and accurately.\n"
            response += "- Consider if the information appears current and from reliable sources.\n\n"

            for i, doc in enumerate(result.documents):
                # Add document length to help agent assess information completeness
                completeness_indicator = format_document_length(doc.text)

                response += (
                    f"Document {i + 1} {completeness_indicator}:\n{doc.text}\n\n"
                )
            
            return response
        else:
            return "I could not find any relevant articles for your query. Please try a different search term."
    
    except Exception as e:
        return f"Error during search: {str(e)}. Please try again with a different query or check the API endpoint."