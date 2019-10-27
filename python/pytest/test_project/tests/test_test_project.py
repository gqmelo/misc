#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `test_project` package."""

import pytest


from test_project import test_project

# @pytest.fixture
# def some_config(some_config):
#     some_config.update({"url3": "https://example2.com"})
#     return some_config

import structlog
log = structlog.get_logger()

def test_content(some_config):
    print("\u001b[32mlkajsdkj\u001b[0m")
    log.msg("\u001b[1m\u001b[31mTesting colors\u001b[0m", a=1, b=2)
    log.msg("\u001b[32mTesting colors\u001b[0m", a=1, b=2)
    log.msg("\u001b[33mTesting colors\u001b[0m", a=1, b=2)
    log.msg("\u001b[34mTesting colors\u001b[0m", a=1, b=2)
    log.msg("\u001b[35mTesting colors\u001b[0m", a=1, b=2)
    log.msg("\u001b[36mTesting colors\u001b[0m", a=1, b=2)
    log.msg("\u001b[37mTesting colors\u001b[0m", a=1, b=2)
    print("\u001b[32mlkajsdkj\u001b[0m")
    assert some_config == {"url": "https://example.com", "url2": "https://example2.com"}
