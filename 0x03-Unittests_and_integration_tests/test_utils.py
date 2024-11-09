#!/usr/bin/env python3
"""
Test cases for access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Dict, Tuple


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


if __name__ == '__main__':
    unittest.main()
