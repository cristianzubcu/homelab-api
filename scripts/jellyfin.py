import os
import requests


class Jellyfin:
    def __init__(self):
        self.url = os.environ["JELLYFIN_URL"].rstrip("/")
        self.api_key = os.environ["JELLYFIN_API_KEY"]
        self.headers = {
            "X-Emby-Authorization": (
                f'MediaBrowser Token="{self.api_key}", Client="homelab-api",'
                ' Device="server", DeviceId="homelab-api", Version="1.0"'
            )
        }

    def scan_libraries(self):
        try:
            resp = requests.post(
                f"{self.url}/Library/Refresh",
                headers=self.headers,
                timeout=10,
            )
            resp.raise_for_status()
            return {"status": "scan triggered"}
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_libraries(self):
        try:
            resp = requests.get(
                f"{self.url}/Library/VirtualFolders",
                headers=self.headers,
                timeout=10,
            )
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_recent(self, limit=10):
        try:
            resp = requests.get(
                f"{self.url}/Items/Latest",
                headers=self.headers,
                params={"Limit": limit, "Fields": "Overview,ProductionYear"},
                timeout=10,
            )
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            return {"error": str(e)}
