def test_delete_rating_tv_series(client):
    response = client.delete("/tv/1399/rating")

    # Respostas possíveis conforme a permissão
    assert response.status_code in (200, 204, 401)

    if response.status_code != 204:
        data = response.json()
        assert "status_code" in data
