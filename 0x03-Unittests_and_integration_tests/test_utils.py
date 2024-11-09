#!/usr/bin/env python3
"""
Test cases for access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Any, Dict, Tuple
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict[str, Any],
            path: Tuple[str, ...],
            expected: Any
    ) -> None:
        """Test access_nested_map function with various inputs."""
        self.assertEqual(
            access_nested_map(nested_map, path),
            expected
        )

    @parameterized.expand([
        ({}, ("a",)),            # Empty map, path = ("a",)
        ({"a": 1}, ("a", "b")),  # Missing key "b" inside "a"
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict[str, Any],
            path: Tuple[str, ...]
    ) -> None:
        """Test that a KeyError is raised for invalid paths
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Exception message contains the key
        self.assertIn(path[-1], str(context.exception))


class TestGetJson(unittest.TestCase):
    """Test cases for get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, test_url: str, test_payload: Dict)\
            -> None:
        """
        Test get_json function returns expected result.
        """
        # Patch `requests.get` to return a mock response
        with patch('utils.requests.get') as mocked_get:
            # Set up the mock to return a response object
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mocked_get.return_value = mock_response

            # Call the function and assert results
            result = get_json(test_url)
            mocked_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
