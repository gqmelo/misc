# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def some_config():
    print("PLUGIN A")
    return {"url": "https://example.com"}
