#!/usr/bin/env python3
"""
Test cases for access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
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


class TestMemoize(unittest.TestCase):
    """Test cases for memoize decorator."""

    def test_memoize(self) -> None:
        """Test memoize decorator for caching a method result.
        """

        class TestClass:
            """Class to test memoize decorator."""

            def a_method(self) -> int:
                """Simple method to be memoized."""
                return 42

            @memoize
            def a_property(self) -> int:
                """Property that uses memoized method."""
                return self.a_method()

        # Initialize the test class
        test_instance = TestClass()

        # Patch 'a_method' to verify its call behavior
        with patch.object(
                test_instance,
                'a_method',
                return_value=42
                ) as mocked_method:
            # First call to a_property should call a_method
            self.assertEqual(test_instance.a_property, 42)
            mocked_method.assert_called_once()

            # 2nd call to a_property should use cached result
            self.assertEqual(test_instance.a_property, 42)
            mocked_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
