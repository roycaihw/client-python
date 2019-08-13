# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.14.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1GlusterfsPersistentVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'endpoints': 'str',
        'endpoints_namespace': 'str',
        'path': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'endpoints': 'endpoints',
        'endpoints_namespace': 'endpointsNamespace',
        'path': 'path',
        'read_only': 'readOnly'
    }

    def __init__(self, endpoints=None, endpoints_namespace=None, path=None, read_only=None):
        """
        V1GlusterfsPersistentVolumeSource - a model defined in Swagger
        """

        self._endpoints = None
        self._endpoints_namespace = None
        self._path = None
        self._read_only = None
        self.discriminator = None

        self.endpoints = endpoints
        if endpoints_namespace is not None:
          self.endpoints_namespace = endpoints_namespace
        self.path = path
        if read_only is not None:
          self.read_only = read_only

    @property
    def endpoints(self):
        """
        Gets the endpoints of this V1GlusterfsPersistentVolumeSource.
        EndpointsName is the endpoint name that details Glusterfs topology. More info: https://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

        :return: The endpoints of this V1GlusterfsPersistentVolumeSource.
        :rtype: str
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """
        Sets the endpoints of this V1GlusterfsPersistentVolumeSource.
        EndpointsName is the endpoint name that details Glusterfs topology. More info: https://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

        :param endpoints: The endpoints of this V1GlusterfsPersistentVolumeSource.
        :type: str
        """
        if endpoints is None:
            raise ValueError("Invalid value for `endpoints`, must not be `None`")

        self._endpoints = endpoints

    @property
    def endpoints_namespace(self):
        """
        Gets the endpoints_namespace of this V1GlusterfsPersistentVolumeSource.
        EndpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: https://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

        :return: The endpoints_namespace of this V1GlusterfsPersistentVolumeSource.
        :rtype: str
        """
        return self._endpoints_namespace

    @endpoints_namespace.setter
    def endpoints_namespace(self, endpoints_namespace):
        """
        Sets the endpoints_namespace of this V1GlusterfsPersistentVolumeSource.
        EndpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: https://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

        :param endpoints_namespace: The endpoints_namespace of this V1GlusterfsPersistentVolumeSource.
        :type: str
        """

        self._endpoints_namespace = endpoints_namespace

    @property
    def path(self):
        """
        Gets the path of this V1GlusterfsPersistentVolumeSource.
        Path is the Glusterfs volume path. More info: https://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

        :return: The path of this V1GlusterfsPersistentVolumeSource.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1GlusterfsPersistentVolumeSource.
        Path is the Glusterfs volume path. More info: https://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

        :param path: The path of this V1GlusterfsPersistentVolumeSource.
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")

        self._path = path

    @property
    def read_only(self):
        """
        Gets the read_only of this V1GlusterfsPersistentVolumeSource.
        ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

        :return: The read_only of this V1GlusterfsPersistentVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1GlusterfsPersistentVolumeSource.
        ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

        :param read_only: The read_only of this V1GlusterfsPersistentVolumeSource.
        :type: bool
        """

        self._read_only = read_only

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1GlusterfsPersistentVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
