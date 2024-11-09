#!/usr/bin/env python3
"""
Unittests for GithubOrgClient
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for GithubOrgClient.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        test that GithubOrgClient.org returns the correct value.
        """
        client = GithubOrgClient(org_name)

        # call the org method
        client.org()

        # Assert get_json was called oce with the expected URL
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
        )


if __name__ == '__main__':
    unittest.main()
