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


class V1VolumeAttachmentStatus(object):
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
        'attach_error': 'V1VolumeError',
        'attached': 'bool',
        'attachment_metadata': 'dict(str, str)',
        'detach_error': 'V1VolumeError'
    }

    attribute_map = {
        'attach_error': 'attachError',
        'attached': 'attached',
        'attachment_metadata': 'attachmentMetadata',
        'detach_error': 'detachError'
    }

    def __init__(self, attach_error=None, attached=None, attachment_metadata=None, detach_error=None):
        """
        V1VolumeAttachmentStatus - a model defined in Swagger
        """

        self._attach_error = None
        self._attached = None
        self._attachment_metadata = None
        self._detach_error = None
        self.discriminator = None

        if attach_error is not None:
          self.attach_error = attach_error
        self.attached = attached
        if attachment_metadata is not None:
          self.attachment_metadata = attachment_metadata
        if detach_error is not None:
          self.detach_error = detach_error

    @property
    def attach_error(self):
        """
        Gets the attach_error of this V1VolumeAttachmentStatus.
        The last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.

        :return: The attach_error of this V1VolumeAttachmentStatus.
        :rtype: V1VolumeError
        """
        return self._attach_error

    @attach_error.setter
    def attach_error(self, attach_error):
        """
        Sets the attach_error of this V1VolumeAttachmentStatus.
        The last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.

        :param attach_error: The attach_error of this V1VolumeAttachmentStatus.
        :type: V1VolumeError
        """

        self._attach_error = attach_error

    @property
    def attached(self):
        """
        Gets the attached of this V1VolumeAttachmentStatus.
        Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.

        :return: The attached of this V1VolumeAttachmentStatus.
        :rtype: bool
        """
        return self._attached

    @attached.setter
    def attached(self, attached):
        """
        Sets the attached of this V1VolumeAttachmentStatus.
        Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.

        :param attached: The attached of this V1VolumeAttachmentStatus.
        :type: bool
        """
        if attached is None:
            raise ValueError("Invalid value for `attached`, must not be `None`")

        self._attached = attached

    @property
    def attachment_metadata(self):
        """
        Gets the attachment_metadata of this V1VolumeAttachmentStatus.
        Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.

        :return: The attachment_metadata of this V1VolumeAttachmentStatus.
        :rtype: dict(str, str)
        """
        return self._attachment_metadata

    @attachment_metadata.setter
    def attachment_metadata(self, attachment_metadata):
        """
        Sets the attachment_metadata of this V1VolumeAttachmentStatus.
        Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.

        :param attachment_metadata: The attachment_metadata of this V1VolumeAttachmentStatus.
        :type: dict(str, str)
        """

        self._attachment_metadata = attachment_metadata

    @property
    def detach_error(self):
        """
        Gets the detach_error of this V1VolumeAttachmentStatus.
        The last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher.

        :return: The detach_error of this V1VolumeAttachmentStatus.
        :rtype: V1VolumeError
        """
        return self._detach_error

    @detach_error.setter
    def detach_error(self, detach_error):
        """
        Sets the detach_error of this V1VolumeAttachmentStatus.
        The last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher.

        :param detach_error: The detach_error of this V1VolumeAttachmentStatus.
        :type: V1VolumeError
        """

        self._detach_error = detach_error

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
        if not isinstance(other, V1VolumeAttachmentStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
