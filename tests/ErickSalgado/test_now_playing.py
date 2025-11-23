import requests

url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MWUzYWZlYzI3MWYxMjE3NzdiNjg1ZWUwNjMwYmRkNiIsIm5iZiI6MTc2MzYwMDMwNy4yNTgsInN1YiI6IjY5MWU2N2IzZGY0NTI0ZjgwZmMyY2JlYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oSN4WXIYsxv7t345_2_GXaSbCHInOa9Ub8vYiWU8nRA"
}

def test_can_get_now_playing_movies():
    response = requests.get(url, headers=headers)
    assert response.status_code == 200

def test_can_get_first_now_playing_movie_details():
    url = "https://api.themoviedb.org/3/movie/534649?language=en-US"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200

def test_can_post_now_playing_movies():
    url = "https://api.themoviedb.org/3/movie/534649/rating"
    payload = {
        "value": 8.0
    }
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 201

def test_can_delete_now_playing_movie_rating():
    url = "https://api.themoviedb.org/3/movie/534649/rating"
    response = requests.delete(url, headers=headers)
    assert response.status_code == 200