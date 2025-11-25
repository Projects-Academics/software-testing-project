def test_details_tv_episode(client):
    response = client.get("/tv/1399/season/1/episode/1")  # Exemplo: Game of Thrones S01E01
    assert response.status_code == 200

    data = response.json()
    assert "name" in data
    assert data["episode_number"] == 1
    assert data["season_number"] == 1
