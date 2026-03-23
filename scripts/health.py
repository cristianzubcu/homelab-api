import requests

SERVICES = {
    "jellyfin":    "http://host.docker.internal:8096",
    "radarr":      "http://host.docker.internal:7878",
    "sonarr":      "http://host.docker.internal:8989",
    "prowlarr":    "http://host.docker.internal:9696",
    "qbittorrent": "http://host.docker.internal:8080",
    "bazarr":      "http://host.docker.internal:6767",
    "grafana":     "http://host.docker.internal:3001",
    "prometheus":  "http://host.docker.internal:9090",
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
