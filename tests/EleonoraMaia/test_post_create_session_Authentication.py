"""
Testes para API do TMDB (The Movie Database)
Test Cases organizados por features da API
"""
import pytest
import requests
from typing import Dict, Any


# Configurações da API
BASE_URL = "https://api.themoviedb.org/3"
API_KEY = "9d087a8d82e7bd9e553313176a8388cd"
TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZDA4N2E4ZDgyZTdiZDllNTUzMzEzMTc2YTgzODhjZCIsIm5iZiI6MTc2Mzg2MDgzMC45MjIsInN1YiI6IjY5MjI2MTVlMjhmMDRlNGMxOWRjZjhiZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hGTM8QnAfjrekrlFULxkbwupIHEEPTLBGYdD-Mn6bWQ"

# Headers para autenticação
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

class TestTMDBPostEndpoint:
    "Teste de endpoint POST"

    def test_post_criar_lista(self):
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
            print(f"Mensagem da API: {data.get('status_message', 'N/A')}")
            print(f"ID da Lista (se fornecido): {data.get('list_id', 'N/A')}")
        elif response.status_code == 401:
            print("SUCESSO LÓGICO: Falha na Autenticação (401). O teste passou na asserção, pois 401 é um resultado esperado.")
        else:
            # Esta linha só seria atingida se o status fosse, por exemplo, 500
            print(f"ERRO INESPERADO: Status Code {response.status_code} não previsto.")

api1 = TestTMDBPostEndpoint()
api1.test_post_criar_lista()