#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_clean_architecture_python_tutorial
----------------------------------

Tests for `clean_architecture_python_tutorial` module.
"""

import pytest


from clean_architecture_python_tutorial import clean_architecture_python_tutorial


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
