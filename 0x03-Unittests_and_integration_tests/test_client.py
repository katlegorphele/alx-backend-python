#!/usr/bin/env python3
'''
Test units for github org client
'''

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError
from utils import get_json, access_nested_map, memoize
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
    List,
    Tuple,
    Type,
    Union,
)


class TestGithubOrgClient(unittest.TestCase):
    '''
    GithubOrgClient class unit tests
    '''

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])

    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        '''
        Test that GithubOrgClient.org returns the correct value
        '''
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')


if __name__ == '__main__':
    unittest.main()