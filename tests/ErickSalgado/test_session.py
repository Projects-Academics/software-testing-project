import requests

url = "https://api.themoviedb.org/3/authentication/guest_session/new"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MWUzYWZlYzI3MWYxMjE3NzdiNjg1ZWUwNjMwYmRkNiIsIm5iZiI6MTc2MzYwMDMwNy4yNTgsInN1YiI6IjY5MWU2N2IzZGY0NTI0ZjgwZmMyY2JlYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oSN4WXIYsxv7t345_2_GXaSbCHInOa9Ub8vYiWU8nRA"
}

def test_can_create_guest_session():
    response = requests.get(url, headers=headers)
    assert response.status_code == 200

def test_guest_session_id_not_null():
    response = requests.get(url, headers=headers)
    data = response.json()
    assert "guest_session_id" in data
    assert data["guest_session_id"] is not None

def test_can_post_with_guest_session():
    guest_session_response = requests.get(url, headers=headers)
    guest_session_data = guest_session_response.json()
    guest_session_id = guest_session_data["guest_session_id"]
    post_url = f"https://api.themoviedb.org/3/movie/550/rating?guest_session_id={guest_session_id}"
    payload = {
        "value": 8.0
    }
    post_response = requests.post(post_url, headers=headers, json=payload)
    assert post_response.status_code == 201

def test_can_delete_with_guest_session():
    guest_session_response = requests.get(url, headers=headers)
    guest_session_data =guest_session_response.json()
    guest_session_id = guest_session_data["guest_session_id"]
    delete_url = f"https://api.themoviedb.org/3/movie/550/rating?guest_session_id={guest_session_id}"
    delete_url_response = requests.delete(delete_url, headers=headers)
    assert delete_url_response.status_code == 200