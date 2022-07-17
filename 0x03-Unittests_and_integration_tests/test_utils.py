#!/usr/bin/env python3
"""This script will create unittests"""
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict
from unittest import TestCase, mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """This class will test access_nested_map"""
    @parameterized.expand([
        ("first", {"a": 1}, ("a",), 1),
        ("second", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("third", {"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, number: str, nested: Mapping,
                               path: Sequence, res: Any):
        """This function will test the given parameterized iterable"""
        self.assertEqual(access_nested_map(nested, path), res)

    @parameterized.expand([
        ("first", {}, ("a",)),
        ("second", {"a", 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, number: str, nested: Mapping,
                                         path: Sequence):
        """This function will test raising errors"""
        self.assertRaises(KeyError, access_nested_map, nested, path)


class TestGetJson(TestCase):
    """This class will test get_json"""
    @parameterized.expand([
        ("url1", "http://example.com", {"payload": True}),
        ("url2", "http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, name: str, url: str, res: Dict):
        """This function will create a mock for a request"""
        with mock.patch('utils.requests') as request:
            request.json.return_value = res
            get_json(url)


class TestMemoize(TestCase):
    """This class will test memoization"""
    def test_memoize(self):
        """This function will create a mock for a method"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        new_class = TestClass()
        with mock.patch.object(new_class, 'a_method') as method:
            new_class.a_property
            new_class.a_property
            method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
