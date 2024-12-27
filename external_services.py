import requests

def fetch_cep_info(cep: str):
    """
    Função para buscar informações do CEP usando a API ViaCEP.
    """
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}