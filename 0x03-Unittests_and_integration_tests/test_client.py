#!/usr/bin/env python3
"""
Unittests for GithubOrgClient
"""
import unittest
from unittest.mock import patch, PropertyMock
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

    @patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        )
    def test_public_repos_url(self, mock_org):
        """
        test that GithubOrgClient._public_repos_url returns
        the expected URL
        """
        mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
                }

        # Instantiate the client
        client = GithubOrgClient("google")

        # call the _public_repos_url property
        result = client._public_repos_url
        expected_url = "https://api.github.com/orgs/google/repos"

        self.assertEqual(result, expected_url)


if __name__ == '__main__':
    unittest.main()
