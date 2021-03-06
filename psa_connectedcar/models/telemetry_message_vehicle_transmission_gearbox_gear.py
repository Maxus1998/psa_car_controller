# coding: utf-8

"""
    Groupe PSA Connected Car - WEB API B2C

    *PSA B2C Connected Car API*  # Introduction This is the description of the *Groupe PSA Connected Car V2 API*. The speccification is  is based on **OpenAPI Specification version 3** and can be displayed via [ReDoc](https://github.com/Rebilly/ReDoc)a or [Swagger](http://swagger.io).   This API allows applications to fetch data from the connected Vehicles data platform. # Authentication PSA Connected Car APIs uses the [OAuth 2.0](https://tools.ietf.org/html/rfc6749) protocol for authentication and Authorization. any application require a valid [Access Token](https://tools.ietf.org/html/rfc6749#section-1.4) to access to user data. # Errors   Error codes returned by all REST APIs comply with the standard. Nevertheless, PSA Services (callers) need to have more complete data structures (even when the answer is not Http-OK) to better detail the type of error by providing application code, message and a debugging code(for investigation purposes). The http code of the response is managed by the protocol itself (in the header).      **Errors are  returned as a generic error response:**    * ```xError``` object model.       # noqa: E501

    OpenAPI spec version: 4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TelemetryMessageVehicleTransmissionGearboxGear(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'recommended': 'str'
    }

    attribute_map = {
        'recommended': 'recommended'
    }

    def __init__(self, recommended=None):  # noqa: E501
        """TelemetryMessageVehicleTransmissionGearboxGear - a model defined in Swagger"""  # noqa: E501

        self._recommended = None
        self.discriminator = None

        if recommended is not None:
            self.recommended = recommended

    @property
    def recommended(self):
        """Gets the recommended of this TelemetryMessageVehicleTransmissionGearboxGear.  # noqa: E501


        :return: The recommended of this TelemetryMessageVehicleTransmissionGearboxGear.  # noqa: E501
        :rtype: str
        """
        return self._recommended

    @recommended.setter
    def recommended(self, recommended):
        """Sets the recommended of this TelemetryMessageVehicleTransmissionGearboxGear.


        :param recommended: The recommended of this TelemetryMessageVehicleTransmissionGearboxGear.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Up", "Down", "UpDown"]  # noqa: E501
        if recommended not in allowed_values:
            raise ValueError(
                "Invalid value for `recommended` ({0}), must be one of {1}"  # noqa: E501
                .format(recommended, allowed_values)
            )

        self._recommended = recommended

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(TelemetryMessageVehicleTransmissionGearboxGear, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TelemetryMessageVehicleTransmissionGearboxGear):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
