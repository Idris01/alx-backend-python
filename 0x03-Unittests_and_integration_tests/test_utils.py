#!/usr/bin/env python3
"""This module define test for the assess_nested_map of thr utils module
"""
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """Define Tests for access_nested_map
    """

    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested, path, output):
        """Test that function works as expected"""
        self.assertEqual(access_nested_map(nested, path), output)

    @parameterized.expand([
            ({}, ("a",), "a"),
            ({"a": 1}, ("a", "b"), "b")])
    def test_access_nested_map_exception(self, nested, path, error_msg):
        """Test that KeyError is thrown"""
        with self.assertRaisesRegex(KeyError, error_msg):
            access_nested_map(nested, path)
