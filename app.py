from flask import Flask, jsonify, render_template, request

from scripts.health import check_all
from scripts.jellyfin import Jellyfin
from scripts.qbittorrent import QBittorrent
from scripts.radarr import Radarr
from scripts.sonarr import Sonarr
from scripts.storage import get_disk_usage
from scripts.vpn import check_vpn

app = Flask(__name__)


# ── Dashboard ─────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


# ── Health ────────────────────────────────────────────────────────────────────

@app.route("/api/health")
def health():
    return jsonify(check_all())


# ── Jellyfin ──────────────────────────────────────────────────────────────────

@app.route("/api/jellyfin/scan", methods=["POST"])
def jellyfin_scan():
    return jsonify(Jellyfin().scan_libraries())


@app.route("/api/jellyfin/recent")
def jellyfin_recent():
    return jsonify(Jellyfin().get_recent())


# ── Downloads ────────────────────────────────────────────────────────────────

@app.route("/api/downloads")
def downloads():
    return jsonify(QBittorrent().get_active())


@app.route("/api/downloads/speed")
def downloads_speed():
    return jsonify(QBittorrent().get_speed())


@app.route("/api/downloads/cleanup", methods=["POST"])
def downloads_cleanup():
    return jsonify(QBittorrent().remove_completed())


# ── Storage ───────────────────────────────────────────────────────────────────

@app.route("/api/storage")
def storage():
    return jsonify(get_disk_usage())


# ── VPN ───────────────────────────────────────────────────────────────────────

@app.route("/api/vpn")
def vpn():
    return jsonify(check_vpn())


# ── Search ────────────────────────────────────────────────────────────────────

@app.route("/api/radarr/search")
def radarr_search():
    term = request.args.get("q", "").strip()
    if not term:
        return jsonify({"error": "q parameter is required"}), 400
    return jsonify(Radarr().search_movie(term))


@app.route("/api/sonarr/search")
def sonarr_search():
    term = request.args.get("q", "").strip()
    if not term:
        return jsonify({"error": "q parameter is required"}), 400
    return jsonify(Sonarr().search_series(term))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
