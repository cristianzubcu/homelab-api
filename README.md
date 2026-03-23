# homelab-api

Flask dashboard for managing self-hosted media server stack. 

## Main Features (What I use the most)

- **Health check** — live up/down status for all services
- **VPN status** — confirm WireGuard/Mullvad is connected
- **Library scan** — trigger Jellyfin to scan for new media

## Setup

```bash
git clone https://github.com/cristianzubcu/homelab-api
cd homelab-api

cp .env.example .env
# Fill in your secrets in here (API keys, etc.)
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


## Development

```bash
pip install flask requests
cp .env.example .env  # fill in required values
python app.py
```

Run tests:
```bash
pip install pytest
pytest tests/ -v
```
