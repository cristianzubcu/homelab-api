import os
import requests


class Radarr:
    def __init__(self):
        self.url = os.environ["RADARR_URL"].rstrip("/")
        self.headers = {"X-Api-Key": os.environ["RADARR_API_KEY"]}

    def get_movies(self):
        try:
            resp = requests.get(
                f"{self.url}/api/v3/movie",
                headers=self.headers,
                timeout=10,
            )
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_queue(self):
        try:
            resp = requests.get(
                f"{self.url}/api/v3/queue",
                headers=self.headers,
                timeout=10,
            )
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def search_movie(self, term):
        try:
            resp = requests.get(
                f"{self.url}/api/v3/movie/lookup",
                headers=self.headers,
                params={"term": term},
                timeout=10,
            )
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def add_movie(self, movie_data):
        try:
            resp = requests.post(
                f"{self.url}/api/v3/movie",
                headers=self.headers,
                json=movie_data,
                timeout=10,
            )
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            return {"error": str(e)}
