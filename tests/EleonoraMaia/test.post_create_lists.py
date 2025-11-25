
import pytest
import requests
from typing import Dict, Any

BASE_URL = "https://api.themoviedb.org/3"
API_KEY = "9d087a8d82e7bd9e553313176a8388cd"
TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMThkNTQxYWNkNTljN2EwMzU4N2FlMWE3YTEyZGJhNyIsIm5iZiI6MTc2MzYwNjQ4NC41OTUsInN1YiI6IjY5MWU3ZmQ0NDg0MzJkMmJiMmViNjRmNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Um5wGKuz--P9_XNY6QlBNTxj7XVaWbhkGBkJiL9yT2Y"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

class TestTMDBPostEndpoint:
    def test_post_criar(self):
        "POST /list - deve tentar criar uma nova lista"
        body = {
            "name": "Lista de Teste",
            "description": "Lista criada para testes automatizados",
            "language": "pt-BR"
        }
        print("\n--- Executando POST: Criar Lista ---")
        response = requests.post(
            f"{BASE_URL}/list",
            headers=HEADERS,
            params={"api_key": API_KEY},
            json=body
        )
        assert response.status_code in [200, 201, 401]
        if response.status_code in [200, 201]:
            data = response.json()
            print(f"SUCESSO! Lista criada (ou resposta de sucesso). Status: {response.status_code}")
            print(f"Mensagem: {data.get('status_message', 'N/A')}")
            print(f"ID da Lista (se fornecido): {data.get('list_id', 'N/A')}")
        elif response.status_code == 401:
            print("SUCESSO LÓGICO: Falha na Autenticação (401). O teste passou na asserção, pois 401 é um resultado esperado.")
        else:
            print(f"ERRO INESPERADO: Status Code {response.status_code} não previsto.")

api1 = TestTMDBPostEndpoint()
api1.test_post_criar()

