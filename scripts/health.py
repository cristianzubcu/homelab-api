import os
import requests

SERVICES = {
    "jellyfin":    os.environ.get("JELLYFIN_URL",   "http://host.docker.internal:8096"),
    "radarr":      os.environ.get("RADARR_URL",     "http://host.docker.internal:7878"),
    "sonarr":      os.environ.get("SONARR_URL",     "http://host.docker.internal:8989"),
    "qbittorrent": os.environ.get("QBIT_URL",       "http://host.docker.internal:8080"),
    "prowlarr":    os.environ.get("PROWLARR_URL",   "http://host.docker.internal:9696"),
    "bazarr":      os.environ.get("BAZARR_URL",     "http://host.docker.internal:6767"),
    "grafana":     os.environ.get("GRAFANA_URL",    "http://host.docker.internal:3001"),
    "prometheus":  os.environ.get("PROMETHEUS_URL", "http://host.docker.internal:9090"),
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
