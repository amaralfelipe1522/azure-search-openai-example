from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv

load_dotenv()


search_endpoint = "https://searchbs.search.windows.net"
index_name = "azureblob-index"
api_key = os.getenv("AZURE_SEARCH_API_KEY")

search_client = SearchClient(
    endpoint=search_endpoint,
    index_name=index_name,
    credential=AzureKeyCredential(api_key)
)

def search_index(query):
    try:
        search_results = search_client.search(search_text=query)
        results_array = [result['content'] for result in search_results]
        return results_array
    except Exception as e:
        print(f"Erro ao buscar no Azure Search: {e}")
        return []
