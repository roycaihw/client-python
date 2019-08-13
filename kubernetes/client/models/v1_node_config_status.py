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


class V1NodeConfigStatus(object):
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
        'active': 'V1NodeConfigSource',
        'assigned': 'V1NodeConfigSource',
        'error': 'str',
        'last_known_good': 'V1NodeConfigSource'
    }

    attribute_map = {
        'active': 'active',
        'assigned': 'assigned',
        'error': 'error',
        'last_known_good': 'lastKnownGood'
    }

    def __init__(self, active=None, assigned=None, error=None, last_known_good=None):
        """
        V1NodeConfigStatus - a model defined in Swagger
        """

        self._active = None
        self._assigned = None
        self._error = None
        self._last_known_good = None
        self.discriminator = None

        if active is not None:
          self.active = active
        if assigned is not None:
          self.assigned = assigned
        if error is not None:
          self.error = error
        if last_known_good is not None:
          self.last_known_good = last_known_good

    @property
    def active(self):
        """
        Gets the active of this V1NodeConfigStatus.
        Active reports the checkpointed config the node is actively using. Active will represent either the current version of the Assigned config, or the current LastKnownGood config, depending on whether attempting to use the Assigned config results in an error.

        :return: The active of this V1NodeConfigStatus.
        :rtype: V1NodeConfigSource
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this V1NodeConfigStatus.
        Active reports the checkpointed config the node is actively using. Active will represent either the current version of the Assigned config, or the current LastKnownGood config, depending on whether attempting to use the Assigned config results in an error.

        :param active: The active of this V1NodeConfigStatus.
        :type: V1NodeConfigSource
        """

        self._active = active

    @property
    def assigned(self):
        """
        Gets the assigned of this V1NodeConfigStatus.
        Assigned reports the checkpointed config the node will try to use. When Node.Spec.ConfigSource is updated, the node checkpoints the associated config payload to local disk, along with a record indicating intended config. The node refers to this record to choose its config checkpoint, and reports this record in Assigned. Assigned only updates in the status after the record has been checkpointed to disk. When the Kubelet is restarted, it tries to make the Assigned config the Active config by loading and validating the checkpointed payload identified by Assigned.

        :return: The assigned of this V1NodeConfigStatus.
        :rtype: V1NodeConfigSource
        """
        return self._assigned

    @assigned.setter
    def assigned(self, assigned):
        """
        Sets the assigned of this V1NodeConfigStatus.
        Assigned reports the checkpointed config the node will try to use. When Node.Spec.ConfigSource is updated, the node checkpoints the associated config payload to local disk, along with a record indicating intended config. The node refers to this record to choose its config checkpoint, and reports this record in Assigned. Assigned only updates in the status after the record has been checkpointed to disk. When the Kubelet is restarted, it tries to make the Assigned config the Active config by loading and validating the checkpointed payload identified by Assigned.

        :param assigned: The assigned of this V1NodeConfigStatus.
        :type: V1NodeConfigSource
        """

        self._assigned = assigned

    @property
    def error(self):
        """
        Gets the error of this V1NodeConfigStatus.
        Error describes any problems reconciling the Spec.ConfigSource to the Active config. Errors may occur, for example, attempting to checkpoint Spec.ConfigSource to the local Assigned record, attempting to checkpoint the payload associated with Spec.ConfigSource, attempting to load or validate the Assigned config, etc. Errors may occur at different points while syncing config. Earlier errors (e.g. download or checkpointing errors) will not result in a rollback to LastKnownGood, and may resolve across Kubelet retries. Later errors (e.g. loading or validating a checkpointed config) will result in a rollback to LastKnownGood. In the latter case, it is usually possible to resolve the error by fixing the config assigned in Spec.ConfigSource. You can find additional information for debugging by searching the error message in the Kubelet log. Error is a human-readable description of the error state; machines can check whether or not Error is empty, but should not rely on the stability of the Error text across Kubelet versions.

        :return: The error of this V1NodeConfigStatus.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this V1NodeConfigStatus.
        Error describes any problems reconciling the Spec.ConfigSource to the Active config. Errors may occur, for example, attempting to checkpoint Spec.ConfigSource to the local Assigned record, attempting to checkpoint the payload associated with Spec.ConfigSource, attempting to load or validate the Assigned config, etc. Errors may occur at different points while syncing config. Earlier errors (e.g. download or checkpointing errors) will not result in a rollback to LastKnownGood, and may resolve across Kubelet retries. Later errors (e.g. loading or validating a checkpointed config) will result in a rollback to LastKnownGood. In the latter case, it is usually possible to resolve the error by fixing the config assigned in Spec.ConfigSource. You can find additional information for debugging by searching the error message in the Kubelet log. Error is a human-readable description of the error state; machines can check whether or not Error is empty, but should not rely on the stability of the Error text across Kubelet versions.

        :param error: The error of this V1NodeConfigStatus.
        :type: str
        """

        self._error = error

    @property
    def last_known_good(self):
        """
        Gets the last_known_good of this V1NodeConfigStatus.
        LastKnownGood reports the checkpointed config the node will fall back to when it encounters an error attempting to use the Assigned config. The Assigned config becomes the LastKnownGood config when the node determines that the Assigned config is stable and correct. This is currently implemented as a 10-minute soak period starting when the local record of Assigned config is updated. If the Assigned config is Active at the end of this period, it becomes the LastKnownGood. Note that if Spec.ConfigSource is reset to nil (use local defaults), the LastKnownGood is also immediately reset to nil, because the local default config is always assumed good. You should not make assumptions about the node's method of determining config stability and correctness, as this may change or become configurable in the future.

        :return: The last_known_good of this V1NodeConfigStatus.
        :rtype: V1NodeConfigSource
        """
        return self._last_known_good

    @last_known_good.setter
    def last_known_good(self, last_known_good):
        """
        Sets the last_known_good of this V1NodeConfigStatus.
        LastKnownGood reports the checkpointed config the node will fall back to when it encounters an error attempting to use the Assigned config. The Assigned config becomes the LastKnownGood config when the node determines that the Assigned config is stable and correct. This is currently implemented as a 10-minute soak period starting when the local record of Assigned config is updated. If the Assigned config is Active at the end of this period, it becomes the LastKnownGood. Note that if Spec.ConfigSource is reset to nil (use local defaults), the LastKnownGood is also immediately reset to nil, because the local default config is always assumed good. You should not make assumptions about the node's method of determining config stability and correctness, as this may change or become configurable in the future.

        :param last_known_good: The last_known_good of this V1NodeConfigStatus.
        :type: V1NodeConfigSource
        """

        self._last_known_good = last_known_good

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
        if not isinstance(other, V1NodeConfigStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
