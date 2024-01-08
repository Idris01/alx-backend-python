#!/usr/bin/env python3
"""This module tests classes in the client module
"""

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """Define tests for org
    """
    @parameterized.expand([
        ("google",), ("abc",)])
    @patch('client.get_json')
    def test_org(self, url, org_get_json):
        """test the org method
        """
        my_class = GithubOrgClient(url)
        result = my_class.org()
        org_get_json.assert_called_once_with(my_class.ORG_URL.format(org=url))
