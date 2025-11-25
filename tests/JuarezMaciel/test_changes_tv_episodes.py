def test_changes_tv_episode(client):
    # exemplo: episode_id = 63056 (Got S01E01)
    response = client.get("/tv/episode/63056/changes")

    assert response.status_code == 200

    data = response.json()
    assert "changes" in data
    assert isinstance(data["changes"], list)
