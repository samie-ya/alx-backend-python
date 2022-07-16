#!/usr/bin/env python3
"""This script will create unittests"""
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from unittest import TestCase
from utils import access_nested_map


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
