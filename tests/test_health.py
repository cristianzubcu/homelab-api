from unittest.mock import MagicMock, patch

from scripts.health import check_all, SERVICES


def _mock_response(status_code):
    r = MagicMock()
    r.status_code = status_code
    return r


@patch("scripts.health.requests.get")
def test_check_all_all_up(mock_get):
    mock_get.return_value = _mock_response(200)
    result = check_all()

    assert isinstance(result, dict)
    assert set(result.keys()) == set(SERVICES.keys())
    assert all(v == "up" for v in result.values())


@patch("scripts.health.requests.get")
def test_check_all_all_down(mock_get):
    mock_get.side_effect = Exception("Connection refused")
    result = check_all()

    assert all(v == "down" for v in result.values())


@patch("scripts.health.requests.get")
def test_check_all_partial(mock_get):
    def side_effect(url, timeout):
        if "jellyfin" in url:
            return _mock_response(200)
        raise Exception("unreachable")

    mock_get.side_effect = side_effect
    result = check_all()

    assert result["jellyfin"] == "up"
    assert result["radarr"] == "down"


@patch("scripts.health.requests.get")
def test_check_all_server_error(mock_get):
    mock_get.return_value = _mock_response(503)
    result = check_all()

    assert all(v == "down" for v in result.values())


def test_check_all_returns_all_services():
    with patch("scripts.health.requests.get", side_effect=Exception):
        result = check_all()
    assert set(result.keys()) == set(SERVICES.keys())
