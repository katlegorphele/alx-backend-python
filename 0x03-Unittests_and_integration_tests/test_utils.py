#!/usr/bin/env python3

"""
Test unit for utils.py
"""

import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Dict, Union, Any, List, Tuple, Callable
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Tests nested map function"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
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


class TestGetJson(unittest.TestCase):
    """
    Test get_json function
    """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """
        Test that utils.get_json returns the expected result.
        """

        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test memoize function
    """

    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock_meth:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mock_meth.assert_called_once()


if __name__ == "__main__":
    unittest.main()
