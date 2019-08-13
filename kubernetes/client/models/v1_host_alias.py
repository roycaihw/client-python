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


class V1HostAlias(object):
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
        'hostnames': 'list[str]',
        'ip': 'str'
    }

    attribute_map = {
        'hostnames': 'hostnames',
        'ip': 'ip'
    }

    def __init__(self, hostnames=None, ip=None):
        """
        V1HostAlias - a model defined in Swagger
        """

        self._hostnames = None
        self._ip = None
        self.discriminator = None

        if hostnames is not None:
          self.hostnames = hostnames
        if ip is not None:
          self.ip = ip

    @property
    def hostnames(self):
        """
        Gets the hostnames of this V1HostAlias.
        Hostnames for the above IP address.

        :return: The hostnames of this V1HostAlias.
        :rtype: list[str]
        """
        return self._hostnames

    @hostnames.setter
    def hostnames(self, hostnames):
        """
        Sets the hostnames of this V1HostAlias.
        Hostnames for the above IP address.

        :param hostnames: The hostnames of this V1HostAlias.
        :type: list[str]
        """

        self._hostnames = hostnames

    @property
    def ip(self):
        """
        Gets the ip of this V1HostAlias.
        IP address of the host file entry.

        :return: The ip of this V1HostAlias.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this V1HostAlias.
        IP address of the host file entry.

        :param ip: The ip of this V1HostAlias.
        :type: str
        """

        self._ip = ip

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
        if not isinstance(other, V1HostAlias):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
