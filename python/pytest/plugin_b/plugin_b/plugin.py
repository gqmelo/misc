# -*- coding: utf-8 -*-
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )

@pytest.fixture
def some_config(some_config):
    print("PLUGIN B")
    some_config.update({"url2": "https://example2.com"})
    return some_config
