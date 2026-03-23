import docker


def check_vpn():
    try:
        client = docker.from_env()
        container = client.containers.get("wireguard")
        result = container.exec_run("curl -s https://am.i.mullvad.net/connected")
        output = result.output.decode().strip()
        return {
            "connected": "You are connected" in output,
            "message": output or "No response",
        }
    except docker.errors.NotFound:
        return {"connected": False, "message": "wireguard container not found"}
    except docker.errors.DockerException as e:
        return {"connected": False, "message": str(e)}
