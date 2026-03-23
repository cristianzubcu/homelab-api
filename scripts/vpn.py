import subprocess


def check_vpn():
    try:
        result = subprocess.run(
            [
                "docker", "exec", "wireguard",
                "curl", "-s", "https://am.i.mullvad.net/connected",
            ],
            capture_output=True,
            text=True,
            timeout=15,
        )
        output = result.stdout.strip()
        return {
            "connected": "You are connected" in output,
            "message": output or result.stderr.strip() or "No response",
        }
    except subprocess.TimeoutExpired:
        return {"connected": False, "message": "Timed out"}
    except FileNotFoundError:
        return {"connected": False, "message": "docker not found in PATH"}
    except Exception as e:
        return {"connected": False, "message": str(e)}
