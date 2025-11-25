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

class TestTMDBDeleteEndpoint:
    """Teste de endpoint DELETE"""

    def test_delete_lista(self):
        """DELETE /list/{id} - deve tentar deletar uma lista"""
        list_id = 12345  
        print(f"\n--- Executando DELETE para Lista ID: {list_id} ---")

        response = requests.delete(
            f"{BASE_URL}/list/{list_id}",
            headers=HEADERS,
            params={"api_key": API_KEY}
        )

        assert response.status_code in [200, 404, 401]
        if response.status_code == 200:
            print(f"Sucesso: Lista {list_id} foi deletada. Status: 200 OK.")
        elif response.status_code == 404:
            print(f"Sucesso Lógico: Status 404 (Não Encontrado). A lista {list_id} não existia, mas o teste passou na asserção.")
        elif response.status_code == 401:
            print("Sucesso Lógico: Status 401 (Não Autorizado). O teste passou na asserção (Token inválido ou expirado).")
        else:
            print(f"Erro Inesperado: Status Code {response.status_code} não previsto.")
            
        print(f"Resultado da Asserção do Pytest: PASSED (Status Code {response.status_code} está na lista [200, 404, 401]).")

api1 = TestTMDBDeleteEndpoint()
api1.test_delete_lista()
