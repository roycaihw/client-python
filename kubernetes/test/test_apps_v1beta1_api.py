# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.14.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.apps_v1beta1_api import AppsV1beta1Api


class TestAppsV1beta1Api(unittest.TestCase):
    """ AppsV1beta1Api unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.apps_v1beta1_api.AppsV1beta1Api()

    def tearDown(self):
        pass

    def test_create_namespaced_controller_revision(self):
        """
        Test case for create_namespaced_controller_revision

        
        """
        pass

    def test_create_namespaced_deployment(self):
        """
        Test case for create_namespaced_deployment

        
        """
        pass

    def test_create_namespaced_deployment_rollback(self):
        """
        Test case for create_namespaced_deployment_rollback

        
        """
        pass

    def test_create_namespaced_stateful_set(self):
        """
        Test case for create_namespaced_stateful_set

        
        """
        pass

    def test_delete_collection_namespaced_controller_revision(self):
        """
        Test case for delete_collection_namespaced_controller_revision

        
        """
        pass

    def test_delete_collection_namespaced_deployment(self):
        """
        Test case for delete_collection_namespaced_deployment

        
        """
        pass

    def test_delete_collection_namespaced_stateful_set(self):
        """
        Test case for delete_collection_namespaced_stateful_set

        
        """
        pass

    def test_delete_namespaced_controller_revision(self):
        """
        Test case for delete_namespaced_controller_revision

        
        """
        pass

    def test_delete_namespaced_deployment(self):
        """
        Test case for delete_namespaced_deployment

        
        """
        pass

    def test_delete_namespaced_stateful_set(self):
        """
        Test case for delete_namespaced_stateful_set

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass

    def test_list_controller_revision_for_all_namespaces(self):
        """
        Test case for list_controller_revision_for_all_namespaces

        
        """
        pass

    def test_list_deployment_for_all_namespaces(self):
        """
        Test case for list_deployment_for_all_namespaces

        
        """
        pass

    def test_list_namespaced_controller_revision(self):
        """
        Test case for list_namespaced_controller_revision

        
        """
        pass

    def test_list_namespaced_deployment(self):
        """
        Test case for list_namespaced_deployment

        
        """
        pass

    def test_list_namespaced_stateful_set(self):
        """
        Test case for list_namespaced_stateful_set

        
        """
        pass

    def test_list_stateful_set_for_all_namespaces(self):
        """
        Test case for list_stateful_set_for_all_namespaces

        
        """
        pass

    def test_patch_namespaced_controller_revision(self):
        """
        Test case for patch_namespaced_controller_revision

        
        """
        pass

    def test_patch_namespaced_deployment(self):
        """
        Test case for patch_namespaced_deployment

        
        """
        pass

    def test_patch_namespaced_deployment_scale(self):
        """
        Test case for patch_namespaced_deployment_scale

        
        """
        pass

    def test_patch_namespaced_deployment_status(self):
        """
        Test case for patch_namespaced_deployment_status

        
        """
        pass

    def test_patch_namespaced_stateful_set(self):
        """
        Test case for patch_namespaced_stateful_set

        
        """
        pass

    def test_patch_namespaced_stateful_set_scale(self):
        """
        Test case for patch_namespaced_stateful_set_scale

        
        """
        pass

    def test_patch_namespaced_stateful_set_status(self):
        """
        Test case for patch_namespaced_stateful_set_status

        
        """
        pass

    def test_read_namespaced_controller_revision(self):
        """
        Test case for read_namespaced_controller_revision

        
        """
        pass

    def test_read_namespaced_deployment(self):
        """
        Test case for read_namespaced_deployment

        
        """
        pass

    def test_read_namespaced_deployment_scale(self):
        """
        Test case for read_namespaced_deployment_scale

        
        """
        pass

    def test_read_namespaced_deployment_status(self):
        """
        Test case for read_namespaced_deployment_status

        
        """
        pass

    def test_read_namespaced_stateful_set(self):
        """
        Test case for read_namespaced_stateful_set

        
        """
        pass

    def test_read_namespaced_stateful_set_scale(self):
        """
        Test case for read_namespaced_stateful_set_scale

        
        """
        pass

    def test_read_namespaced_stateful_set_status(self):
        """
        Test case for read_namespaced_stateful_set_status

        
        """
        pass

    def test_replace_namespaced_controller_revision(self):
        """
        Test case for replace_namespaced_controller_revision

        
        """
        pass

    def test_replace_namespaced_deployment(self):
        """
        Test case for replace_namespaced_deployment

        
        """
        pass

    def test_replace_namespaced_deployment_scale(self):
        """
        Test case for replace_namespaced_deployment_scale

        
        """
        pass

    def test_replace_namespaced_deployment_status(self):
        """
        Test case for replace_namespaced_deployment_status

        
        """
        pass

    def test_replace_namespaced_stateful_set(self):
        """
        Test case for replace_namespaced_stateful_set

        
        """
        pass

    def test_replace_namespaced_stateful_set_scale(self):
        """
        Test case for replace_namespaced_stateful_set_scale

        
        """
        pass

    def test_replace_namespaced_stateful_set_status(self):
        """
        Test case for replace_namespaced_stateful_set_status

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
