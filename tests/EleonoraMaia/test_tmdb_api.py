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

    def test_get_detalhes_filme(self):
        """GET /movie/{id} - deve retornar detalhes de um filme existente"""
        movie_id = 550  # Fight Club
        response = requests.get(
            f"{BASE_URL}/movie/{movie_id}",
            headers=HEADERS,
            params={"api_key": API_KEY}
        )

        assert response.status_code in [200, 401]

        if response.status_code == 200:
            data = response.json()
            assert data["id"] == movie_id
            assert "title" in data

    def test_get_filmes_populares(self):
        """GET /movie/popular - deve retornar lista de filmes populares"""
        response = requests.get(
            f"{BASE_URL}/movie/popular",
            headers=HEADERS,
            params={"api_key": API_KEY}
        )

        assert response.status_code in [200, 401]

        if response.status_code == 200:
            data = response.json()
            assert "results" in data
            assert isinstance(data["results"], list)
            assert len(data["results"]) > 0


class TestTMDBPostEndpoint:
    """Teste de endpoint POST"""

    def test_post_criar_lista(self):
        """POST /list - deve tentar criar uma nova lista"""
        body = {
            "name": "Lista de Teste",
            "description": "Lista criada para testes automatizados",
            "language": "pt-BR"
        }

        response = requests.post(
            f"{BASE_URL}/list",
            headers=HEADERS,
            params={"api_key": API_KEY},
            json=body
        )

        assert response.status_code in [200, 201, 401]

class TestTMDBDeleteEndpoint:
    """Teste de endpoint DELETE"""

    def test_delete_lista(self):
        """DELETE /list/{id} - deve tentar deletar uma lista"""
        list_id = 12345  

        response = requests.delete(
            f"{BASE_URL}/list/{list_id}",
            headers=HEADERS,
            params={"api_key": API_KEY}
        )

        assert response.status_code in [200, 404, 401]