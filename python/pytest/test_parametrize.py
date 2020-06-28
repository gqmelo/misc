from types import SimpleNamespace
import pytest

@pytest.fixture(params=[pytest.param({}, id="default")])
def server(request):
    config = {
        "database": "127.0.0.1",
        "enable_cache": False,
    }
    additional_config = request.param
    config.update(additional_config)
    return SimpleNamespace(**config)

def test_default_server(server):
    assert server.enable_cache is False

@pytest.mark.parametrize(
    "server", [pytest.param({"enable_cache": True}, id="cache_enabled")], indirect=True
)
def test_server_with_cache(server):
    assert server.enable_cache is True
