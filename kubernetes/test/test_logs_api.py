# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.15.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes.client
from kubernetes.client.api.logs_api import LogsApi  # noqa: E501
from kubernetes.client.rest import ApiException


class TestLogsApi(unittest.TestCase):
    """LogsApi unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.logs_api.LogsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_log_file_handler(self):
        """Test case for log_file_handler

        """
        pass

    def test_log_file_list_handler(self):
        """Test case for log_file_list_handler

        """
        pass


if __name__ == '__main__':
    unittest.main()
