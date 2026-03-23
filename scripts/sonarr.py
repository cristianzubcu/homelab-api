import os
import requests


class Sonarr:
    def __init__(self):
        self.url = os.environ["SONARR_URL"].rstrip("/")
        self.headers = {"X-Api-Key": os.environ["SONARR_API_KEY"]}

    def get_series(self):
        try:
            resp = requests.get(
                f"{self.url}/api/v3/series",
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

    def search_series(self, term):
        try:
            resp = requests.get(
                f"{self.url}/api/v3/series/lookup",
                headers=self.headers,
                params={"term": term},
                timeout=10,
            )
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def add_series(self, series_data):
        try:
            resp = requests.post(
                f"{self.url}/api/v3/series",
                headers=self.headers,
                json=series_data,
                timeout=10,
            )
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            return {"error": str(e)}
