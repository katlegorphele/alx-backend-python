#!/usr/bin/env python3
'''
Test units for github org client
'''
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from utils import get_json, memoize
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    '''
    TestGithubOrgClient class
    '''
    
    @parameterized.expand([
        ("google"),
        ("abc")
    ])

    @patch('client.get_json')
    def test_org(self, org_name:str, mock_get_json: Mock):
        '''
        Test that GithubOrgClient.org returns the correct value
        '''
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

    
    def test_public_repos_url(self):
        '''
        Test that the result of _public_repos_url is the expected one
        based on the mocked payload
        '''
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            test_class = GithubOrgClient("test")
            mock_org.return_value = {"repos_url": "test_url"}
            self.assertEqual(test_class._public_repos_url, "test_url")


    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Mock):
        '''
        Test that the list of repos is what you expect from the chosen payload
        '''
        payload = [{"name": "Google"}, {"name": "abc"}]
        mock_get_json.return_value = payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "test_url"
            test_class = GithubOrgClient("test")
            self.assertEqual(test_class.public_repos(), ["Google", "abc"])
            mock_get_json.assert_called_once_with("test_url")

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])

    def test_has_license(self, repo: dict, license_key: str, expected: bool):
        '''
        Test that the result of has_license is the expected one based on the
        mocked payload
        '''
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class.has_license(repo, license_key), expected)

test_cases = [
    {"org_payload": TEST_PAYLOAD[0][0],
     "repos_payload": TEST_PAYLOAD[0][1],
     "expected_repos": TEST_PAYLOAD[0][2],
     "apache2_repos": TEST_PAYLOAD[0][3]}]


@parameterized_class(test_cases)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test integration GithubOrgClient class """

    @classmethod
    def setUpClass(cls) -> None:
        """ Set up class """
        req_payload = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload,
        }

        def get_payload(url: str) -> Mock:
            """ get payload
            """
            if url in req_payload.keys():
                # get the corresponding payload for the url
                return Mock(**{"json.return_value": req_payload[url]})
            return Mock(**{"json.return_value": []})

        cls.get_patcher = patch('requests.get', side_effect=get_payload)

        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """ Test GithubOrgClient.public_repos """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        # self.get_patcher.stop()

    def test_public_repos_with_license(self) -> None:
        """ Test GithubOrgClient.public_repos with license """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(
            license="apache-2.0"), self.apache2_repos)
        # self.get_patcher.stop()

    @classmethod
    def tearDownClass(cls) -> None:
        """ Tear down class """
        cls.get_patcher.stop()

if __name__ == '__main__':
    unittest.main()