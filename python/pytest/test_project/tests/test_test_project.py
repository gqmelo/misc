#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `test_project` package."""

import pytest


from test_project import test_project

# @pytest.fixture
# def some_config(some_config):
#     some_config.update({"url3": "https://example2.com"})
#     return some_config


def test_content(some_config):
    assert some_config == {"url": "https://example.com", "url2": "https://example2.com"}
