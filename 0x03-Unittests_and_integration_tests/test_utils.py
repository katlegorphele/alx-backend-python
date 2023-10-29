#!/usr/bin/env python3

"""
Test unit for utils.py
"""

import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Dict, Union, Any, List, Tuple, Callable


class TestAccessNestedMap(unittest.TestCase):
    """Tests nested map function"""

    passing_test_cases = [
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ]

    @parameterized.expand(passing_test_cases)
    def test_access_nested_map(
        self, nested_map: Dict, path: Tuple, expected: Any
    ) -> None:
        """Tests access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    keyErr_test_cases = [
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ]

    @parameterized.expand(keyErr_test_cases)
    def test_access_nested_map_exception(
        self, nested_map: Dict, path: Tuple, expected: Any
    ) -> None:
        """Tests access_nested_map exception"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
