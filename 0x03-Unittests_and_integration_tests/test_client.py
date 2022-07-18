#!/usr/bin/env python3
"""This script will create unittests"""
from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict
from unittest import TestCase, mock


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

    def test_public_repos_url(self):
        """This function will test _public_repos_url"""
        with mock.patch('client.GithubOrgClient.org') as org:
            org.return_value = {"repos_url": "https://api.github\
                                .com/orgs/google/repos"}
            GithubOrgClient._public_repos_url

    @parameterized.expand([
        ("1", {"license": {"key": "my_license"}}, "my_license", True),
        ("2", {"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, name: str, repo: Dict[str, Dict],
                         res: str, Bool: bool):
        """This function will test has_license"""
        self.assertEqual(GithubOrgClient.has_license(repo, res), Bool)


if __name__ == "__main__":
    unittest.main()
