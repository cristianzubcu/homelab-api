import shutil


def get_disk_usage(path="/data"):
    try:
        usage = shutil.disk_usage(path)
        return {
            "total": _human_size(usage.total),
            "used": _human_size(usage.used),
            "free": _human_size(usage.free),
            "percent_used": round(usage.used / usage.total * 100, 1),
        }
    except OSError as e:
        return {"error": str(e)}


def _human_size(n):
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} PB"
