import requests

SERVICES = {
    "jellyfin":    "http://jellyfin:8096",
    "radarr":      "http://radarr:7878",
    "sonarr":      "http://sonarr:8989",
    "prowlarr":    "http://prowlarr:9696",
    "qbittorrent": "http://wireguard:8080",
    "bazarr":      "http://bazarr:6767",
    "grafana":     "http://grafana:3001",
    "prometheus":  "http://prometheus:9090",
}


def check_all():
    results = {}
    for name, url in SERVICES.items():
        try:
            resp = requests.get(url, timeout=3)
            results[name] = "up" if resp.status_code < 500 else "down"
        except requests.RequestException:
            results[name] = "down"
    return results
