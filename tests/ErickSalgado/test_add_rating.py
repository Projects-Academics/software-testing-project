import requests

url = "https://api.themoviedb.org/3/tv/series_id/rating"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json;charset=utf-8",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MWUzYWZlYzI3MWYxMjE3NzdiNjg1ZWUwNjMwYmRkNiIsIm5iZiI6MTc2MzYwMDMwNy4yNTgsInN1YiI6IjY5MWU2N2IzZGY0NTI0ZjgwZmMyY2JlYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oSN4WXIYsxv7t345_2_GXaSbCHInOa9Ub8vYiWU8nRA"
}

def test_can_get_tv_show_details():
    url = "https://api.themoviedb.org/3/tv/1399?language=en-US"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200

def test_can_add_tv_show_rating():
    url = "https://api.themoviedb.org/3/tv/1399/rating"
    payload = {
        "value": 9.0
    }
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 201

def test_can_delete_tv_show_rating():
    url = "https://api.themoviedb.org/3/tv/1399/rating"
    response = requests.delete(url, headers=headers)
    assert response.status_code == 200