#!/usr/bin/env python3
"""This script will create unittests"""
from client import GithubOrgClient
from parameterized import parameterized
from unittest import TestCase, mock
from utils import get_json


class TestGithubOrgClient(TestCase):
    """This class will test the GithubOrgClient class"""
    @parameterized.expand([
        ("org1", "google"),
        ("org2", "abc")
        ])
    @mock.patch('utils.get_json')
    def test_org(self, holder: str, org: str, mock_json):
        """This function will test org function"""
        orgs = GithubOrgClient(org)
        orgs.org


if __name__ == "__main__":
    unittest.main()
