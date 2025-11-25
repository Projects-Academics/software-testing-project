def test_images_tv_episode(client):
    response = client.get("/tv/1399/season/1/episode/1/images")

    assert response.status_code == 200

    data = response.json()
    assert "stills" in data
    assert isinstance(data["stills"], list)
