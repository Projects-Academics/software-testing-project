import requests

class TMDbClient:
    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self, token):
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json;charset=utf-8"
        }

    def get(self, endpoint, params=None):
        return requests.get(f"{self.BASE_URL}{endpoint}", headers=self.headers, params=params)

    def post(self, endpoint, body=None):
        return requests.post(f"{self.BASE_URL}{endpoint}", headers=self.headers, json=body)

    def delete(self, endpoint):
        return requests.delete(f"{self.BASE_URL}{endpoint}", headers=self.headers)
