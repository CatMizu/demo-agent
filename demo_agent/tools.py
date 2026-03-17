from langchain.tools import tool
from tavily import TavilyClient
import os


@tool
def internet_search(query: str) -> str:
    """Search the internet for up-to-date information using Tavily.

    Use this tool to find current data, statistics, reports, and news articles.
    Returns relevant search results with URLs and content snippets.
    """
    client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
    response = client.search(query, max_results=5)
    results = []
    for r in response["results"]:
        results.append(f"**{r['title']}**\n{r['url']}\n{r['content']}\n")
    return "\n---\n".join(results) if results else "No results found."
