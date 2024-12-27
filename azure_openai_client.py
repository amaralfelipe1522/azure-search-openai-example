import openai
import os
from dotenv import load_dotenv
from external_services import fetch_cep_info

load_dotenv()

openai.api_type = "azure"
openai.api_base = "https://openaibs.openai.azure.com"
openai.api_version = "2024-05-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

# GPT 3.5 Turbo:
#     api_version = "2023-03-15-preview"
#     deployment_id="gpt-35-turbo"

# GPT 4o:
#     api_version = "2024-05-01-preview"
#     deployment_id="gpt-4o"

def get_azure_openai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            deployment_id="gpt-4o",
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ],
            functions=functions,
            max_tokens=150
        )

        if "function_call" in response["choices"][0]["message"]:
            function_call = response["choices"][0]["message"]["function_call"]
            arguments = eval(function_call["arguments"])
            if function_call["name"] == "fetch_cep_info":
                cep_data = fetch_cep_info(arguments["cep"])
                return ("Informações do CEP:", cep_data)
        else:
            return response['choices'][0]['message']['content'].strip()
        
    except Exception as e:
        print(f"Erro ao chamar OpenAI: {e}")
        return ''

functions = [
    {
        "name": "fetch_cep_info",
        "description": "Busca informações sobre o CEP fornecido.",
        "parameters": {
            "type": "object",
            "properties": {
                "cep": {
                    "type": "string",
                    "description": "O CEP no formato 00000000."
                }
            },
            "required": ["cep"],
        },
    }
]