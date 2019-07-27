# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def some_config(some_config):
    print("PLUGIN B - 2")
    some_config.update({"url3": "https://example3.com"})
    return some_config
