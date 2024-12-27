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
    while True:
        query = input("Digite sua pergunta (ou 'sair' para encerrar): ").strip()
        if query.lower() == "sair":
            print("Encerrando o programa. Até mais!")
            break
        response = answer_question_from_search(query)
        print(f"Resposta: {response}")
