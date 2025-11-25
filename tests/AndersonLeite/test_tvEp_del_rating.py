import pytest
import requests

url = "https://api.themoviedb.org/3/tv/1/season/1/episode/1/rating"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json;charset=utf-8",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MWRlOTE4ZDU3YzYyOWZmMjc1MjE1OWFhNmE3NjQ0NyIsIm5iZiI6MTc2MzkxOTY3Ni43MzUwMDAxLCJzdWIiOiI2OTIzNDczYzNjYTJhNzM3Yzc5NThiMTciLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.zUAONZ2_EJsN2Zb2uz5kllFpHFa8ekd8vCBUCXP_6LM"
}

def test_del_rating_sucesso():
    """Testar se o DELETE request foi bem sucedido"""
    response = requests.delete(url, headers=headers)
    
    assert response.status_code == 200
    assert "success" in response.text
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

def test_del_rating_sem_autorizacao():
    """Testar se o DELETE request falha sem autorização"""
    headers_invalidos = {"accept": "application/json"}
    response = requests.delete(url, headers=headers_invalidos)
    
    assert response.status_code == 401
    print(f"Status Code: {response.status_code}")