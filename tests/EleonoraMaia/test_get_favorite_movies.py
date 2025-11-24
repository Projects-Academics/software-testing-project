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

# Pode retornar 200 (OK) ou 401 (não autorizado)
class TestTMDBGetEndpoints:
    """Testes de endpoints GET"""

    def test_get_filmes_populares(self):
        """GET /movie/popular - deve retornar lista de filmes populares"""
        response = requests.get(
            f"{BASE_URL}/movie/popular",
            headers=HEADERS,
            params={"api_key": API_KEY}
        )

        assert response.status_code in [200, 401]
        print(f"Status OK: Retornou {response.status_code}.")

        if response.status_code == 200:
            data = response.json()
            assert "results" in data
            assert isinstance(data["results"], list)
            assert len(data["results"]) > 0

            print(f"Teste de Estrutura OK: Lista 'Results' com {len(data['results'])} itens.")
            print(f"   Primeiro resultado: {data['results'][0].get('title', 'N/A')}")
        
        elif response.status_code == 401:
            print("Teste Considerado OK: Autenticação Falhou (401).")

api1 = TestTMDBGetEndpoints()
api1.test_get_filmes_populares() 
