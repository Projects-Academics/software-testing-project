import pytest
import requests

url = "https://api.themoviedb.org/3/tv/1/season/1/episode/1/rating"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json;charset=utf-8",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MWRlOTE4ZDU3YzYyOWZmMjc1MjE1OWFhNmE3NjQ0NyIsIm5iZiI6MTc2MzkxOTY3Ni43MzUwMDAxLCJzdWIiOiI2OTIzNDczYzNjYTJhNzM3Yzc5NThiMTciLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.zUAONZ2_EJsN2Zb2uz5kllFpHFa8ekd8vCBUCXP_6LM"
}

def test_post_rating_sucesso():
    """Testar se o POST request foi bem sucedido"""
    payload = '{"value":8.5}'
    response = requests.post(url, data=payload, headers=headers)
    
    assert response.status_code == 201
    assert "success" in response.text
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

def test_post_rating_falha():
    """Testar se o POST request falha com valor inválido"""
    payload = '{"value":15.0}'  # Valor inválido, deve ser entre 0.5 e 10.0
    response = requests.post(url, data=payload, headers=headers)
    
    assert response.status_code == 400
    assert "success" in response.text
    print(f"Status Code: {response.status_code}")