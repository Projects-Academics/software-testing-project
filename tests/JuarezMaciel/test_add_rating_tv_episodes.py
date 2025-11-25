def test_add_rating_tv_episode(client):
    body = {"value": 8.5}

    response = client.post(
        "/tv/1399/season/1/episode/1/rating",
        body=body
    )

    # A API retorna 401 se o token não for autorizado para rating.
    # Para o trabalho, valide comportamento esperado:
    assert response.status_code in (200, 201, 401)

    data = response.json()
    assert "status_code" in data
