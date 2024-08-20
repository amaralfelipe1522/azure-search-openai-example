from search_client import search_index
from azure_openai_client import get_azure_openai_response
from dotenv import load_dotenv

load_dotenv()

def answer_question_from_search(query):
    search_results = search_index(query)
    context = " ".join(search_results)
    prompt = f"Com base no seguinte contexto: {context}, responda a pergunta: {query}"
    return get_azure_openai_response(prompt)

if __name__ == "__main__":
    response = answer_question_from_search("Qual o nome da seguradora?")
    print(response)
