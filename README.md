# homelab-api

Mobile-friendly Flask dashboard for managing a self-hosted media server stack. Wraps Jellyfin, Radarr, Sonarr, qBittorrent, and monitoring services behind a clean web UI.

## Features

- **Health check** — live up/down status for all services
- **VPN status** — confirm WireGuard/Mullvad is connected
- **Storage** — disk usage of the media volume
- **Library scan** — trigger Jellyfin to scan for new media
- **Recent additions** — last 10 items added to Jellyfin
- **Active torrents** — live list with progress bars and speeds
- **Cleanup** — remove completed torrents from qBittorrent
- **Search** — look up movies (Radarr) or TV shows (Sonarr)

## Setup

```bash
git clone https://github.com/cristianzubcu/homelab-api
cd homelab-api

cp .env.example .env
# Fill in your API keys and service URLs
nano .env

docker compose up -d
```

Open `http://your-server:5000`

## Environment variables

| Variable | Description |
|---|---|
| `JELLYFIN_URL` | Jellyfin base URL |
| `JELLYFIN_API_KEY` | Jellyfin API key (Dashboard → API Keys) |
| `QBIT_URL` | qBittorrent WebUI URL |
| `QBIT_USER` | qBittorrent username |
| `QBIT_PASS` | qBittorrent password |
| `RADARR_URL` | Radarr base URL |
| `RADARR_API_KEY` | Radarr API key (Settings → General) |
| `SONARR_URL` | Sonarr base URL |
| `SONARR_API_KEY` | Sonarr API key (Settings → General) |

## API endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | Dashboard UI |
| GET | `/api/health` | All service up/down status |
| GET | `/api/vpn` | VPN connection status |
| GET | `/api/storage` | Disk usage |
| POST | `/api/jellyfin/scan` | Trigger library scan |
| GET | `/api/jellyfin/recent` | Recently added media |
| GET | `/api/downloads` | Active torrents |
| GET | `/api/downloads/speed` | Current transfer speed |
| POST | `/api/downloads/cleanup` | Remove completed torrents |
| GET | `/api/radarr/search?q=term` | Search movies |
| GET | `/api/sonarr/search?q=term` | Search TV shows |

## Screenshots

<!-- Add screenshots here -->

## Development

```bash
pip install flask requests
cp .env.example .env  # fill in values
python app.py
```

Run tests:
```bash
pip install pytest
pytest tests/ -v
```
