import os
import requests


class QBittorrent:
    def __init__(self):
        self.url = os.environ["QBIT_URL"].rstrip("/")
        self.user = os.environ["QBIT_USER"]
        self.password = os.environ["QBIT_PASS"]
        self.session = requests.Session()
        self._logged_in = False

    def login(self):
        try:
            resp = self.session.post(
                f"{self.url}/api/v2/auth/login",
                data={"username": self.user, "password": self.password},
                timeout=10,
            )
            resp.raise_for_status()
            self._logged_in = resp.text.strip() == "Ok."
            return self._logged_in
        except requests.RequestException as e:
            return {"error": str(e)}

    def _ensure_logged_in(self):
        if not self._logged_in:
            self.login()

    def get_active(self):
        self._ensure_logged_in()
        try:
            resp = self.session.get(
                f"{self.url}/api/v2/torrents/info",
                params={"filter": "active"},
                timeout=10,
            )
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_all(self):
        self._ensure_logged_in()
        try:
            resp = self.session.get(
                f"{self.url}/api/v2/torrents/info",
                timeout=10,
            )
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def remove_completed(self):
        self._ensure_logged_in()
        try:
            torrents = self.get_all()
            if isinstance(torrents, dict) and "error" in torrents:
                return torrents
            completed = [t["hash"] for t in torrents if t.get("state") == "uploading"
                         or t.get("progress", 0) == 1.0]
            if not completed:
                return {"removed": 0}
            hashes = "|".join(completed)
            self.session.post(
                f"{self.url}/api/v2/torrents/delete",
                data={"hashes": hashes, "deleteFiles": "false"},
                timeout=10,
            )
            return {"removed": len(completed)}
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_speed(self):
        self._ensure_logged_in()
        try:
            resp = self.session.get(
                f"{self.url}/api/v2/transfer/info",
                timeout=10,
            )
            resp.raise_for_status()
            data = resp.json()
            return {
                "dl_speed": data.get("dl_info_speed", 0),
                "up_speed": data.get("up_info_speed", 0),
                "dl_speed_human": _human_speed(data.get("dl_info_speed", 0)),
                "up_speed_human": _human_speed(data.get("up_info_speed", 0)),
            }
        except requests.RequestException as e:
            return {"error": str(e)}


def _human_speed(bps):
    for unit in ("B/s", "KB/s", "MB/s", "GB/s"):
        if bps < 1024:
            return f"{bps:.1f} {unit}"
        bps /= 1024
    return f"{bps:.1f} TB/s"
