# coding: utf-8

"""
    Iconomi API!

    # Introduction Welcome to the ICONOMI Platform API. There are two ways to integrate with the ICONOMI platform, the REST API and a stream-oriented API using Websockets.  ## Versioning  This API maintains backward compatibility. Breaking changes to the API are managed by providing new endpoints. Old versions will remain available for two months after a new version is released and can then be removed at any time. All information about releases is published on this website. Non-breaking changes are released in the same major-version API.  ## Types  All request bodies should have content type application/json and be valid JSON.  <br/>  ### Timestamps  Unless otherwise specified, all timestamps will be returned in ISO 8601 with microseconds.  <br/> Example:  ``` 2019-08-01T01:02:03.000004Z ```  <br/>  ### Numbers  Integers are unquoted.  <br/> Example:  ``` \"x\": 194767 ```  Decimals are returned as strings with a period as a decimal separator and no thousands separator.  <br/> Example:  ``` \"price\": \"3.3847\" ```  <br/>  ### IDs  All IDs are UUIDs.  <br/> Example:  ```  6EFB3D83-830A-42F8-84CD-2C307FE62AD8 ```  <br/>  ### Enumerations  There are several enumerations on the platform that are used across the platform.  #### Strategy types There are different types of strategies supported on the platform which use different behaviour for  investment:  * **PASSIVE** - Strategies that have structures based set on percentages and are rebalances less often  * **ACTIVE** - Strategies that follow a more active strategy not using an index  #### Granulations  Depending on the time period selected different granulation of data is possible as a result.  For each of the granulations there will be one data point available:  * **TWO_MINUTE** - only available for institutional strategies. * **FIVE_MINUTE** * **HOURLY** * **THREE_HOURLY** * **EIGHT_HOURLY** * **DAILY**  ## Rate limiting  The public API (both the REST API and the Websocket API) allows for 60 requests per minute. This rate is subject to change.  ## Authentication  To access authenticated endpoints you need an account on the ICONOMI platform. After you have an account you need to setup your api keys (you can find the option under Settings).  ### Creating a request  All REST requests must contain the following headers:  * **ICN-API-KEY** - The api key as a string. * **ICN-SIGN** - The base64-encoded signature (see Signing a Message). * **ICN-TIMESTAMP** - A timestamp for your request in epoch milliseconds.  <br/>   ### Signing a Message  You generate the **ICN-SIGN** header by creating a **sha512 HMAC** using the base64-decoded secret key on the prehash string timestamp + method + requestPath + body (where + represents string concatenation) and base64-encode the output, where: * the timestamp value is the same as the **ICN-TIMESTAMP** header. * the body is the request body string or omitted if there is no request body (typically for GET requests).  * method must always be in upper case * the request path starts with /v1/ and doesn't include query parameters   Pseudocode example: ```  base64_encode(HMAC_SHA512(secret_key, timestamp + upper_case(method) + requestPath + body)) ```  Java code example: ``` String apiSecret = \"...\"; String toSign = timestamp + method.toUpperCase() + requestPath + body; SecretKeySpec signingKey = new SecretKeySpec(apiSecret.getBytes(), \"HmacSHA512\"); Mac mac = Mac.getInstance(signingKey.getAlgorithm()); mac.init(signingKey); String digest = Base64.getEncoder().encodeToString(mac.doFinal(toSign.getBytes())); ```  Example of a POST with a body: ``` secret = '51ffd0604d4ba42790b42860fc1e98ac6a4b60e32e078b801d899c6eb04bc29e' timestamp = '1643118174153' method = 'post' requestPath = '/v1/order' body = '{\"amount\":100,\"source_ticker\":\"EUR\",\"target_ticker\":\"BTC\",\"fitting_speed_type\":\"FAST\"}'  string to encode = '1643118174153POST/v1/order{\"amount\":100,\"source_ticker\":\"EUR\",\"target_ticker\":\"BTC\",\"fitting_speed_type\":\"FAST\"}'  base64 encoded signature = 'tD9pi/UhcVp8BeQyahBDRQnkIm0avWmE1JMZlCEveZ66whMZ0YsHWfzFz6G14FhRunPR/rFbbFZuRkOLXEIoEA==' ``` Example of GET with query parameters: ``` secret = '51ffd0604d4ba42790b42860fc1e98ac6a4b60e32e078b801d899c6eb04bc29e' timestamp = '1643178751655' method = 'get' requestPath = '/v1/user/activity?type=FEES_AND_EARNINGS&pageSize=4&pageNumber=0' body = <empty>  string to encode = '1643178751655GET/v1/user/activity'  base64 encoded signature = 'efIB1zs7yunvzvCUL1SPWh5IAjU2b+g51vSPdGSX69KjJIVbtJQKIc2yVTaZlQIoReu6hx39r4w9dTDJhRdgdA==' ```   <br/>  ### Postman  You can also try with <a href=\"https://www.postman.com/downloads/\" target=\"_blank\" rel=\"nofollow\">postman client</a>. After you import <a href=\"https://www.postman.com/collections/2d5e387a761a6da9f022\" target=\"_blank\" rel=\"nofollow\">collection</a> into client, you have to create new environment under \"Manage environments\" and add two variables:  <br>  * **ICN-API-KEY** - The api key from your account on ICONOMI platform * **ICN-SECRET** - The secret key from your account on ICONOMI platform  <br/>  Before you execute any of those endpoints, environment must be selected.  ### Websocket Authentication  It is possible to authenticate yourself when subscribing to the websocket feed.  When opening connection to websocket, add additional headers, as if you were signing a request. To get the necessary parameters, you would go through the same process as you do to make authenticated calls to the API.  ## Sample libraries You can find sample libraries for communicating with our API at our <a href=\"https://github.com/iconomi-ag\" target=\"_blank\" rel=\"nofollow\">github page.</a>  ## Bug reports For any bug reports in the documentation or the API, feel free to report them to our <a href=\"https://github.com/iconomi-ag/iconomi-api\" target=\"_blank\" rel=\"nofollow\">github page.</a>  # noqa: E501

    OpenAPI spec version: 1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Structure(object):
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
        'ticker': 'str',
        'values': 'list[StructureElement]',
        'number_of_assets': 'int',
        'last_rebalanced': 'int',
        'monthly_rebalanced_count': 'int'
    }

    attribute_map = {
        'ticker': 'ticker',
        'values': 'values',
        'number_of_assets': 'numberOfAssets',
        'last_rebalanced': 'lastRebalanced',
        'monthly_rebalanced_count': 'monthlyRebalancedCount'
    }

    def __init__(self, ticker=None, values=None, number_of_assets=None, last_rebalanced=None, monthly_rebalanced_count=None):  # noqa: E501
        """Structure - a model defined in Swagger"""  # noqa: E501
        self._ticker = None
        self._values = None
        self._number_of_assets = None
        self._last_rebalanced = None
        self._monthly_rebalanced_count = None
        self.discriminator = None
        if ticker is not None:
            self.ticker = ticker
        if values is not None:
            self.values = values
        if number_of_assets is not None:
            self.number_of_assets = number_of_assets
        if last_rebalanced is not None:
            self.last_rebalanced = last_rebalanced
        if monthly_rebalanced_count is not None:
            self.monthly_rebalanced_count = monthly_rebalanced_count

    @property
    def ticker(self):
        """Gets the ticker of this Structure.  # noqa: E501


        :return: The ticker of this Structure.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this Structure.


        :param ticker: The ticker of this Structure.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def values(self):
        """Gets the values of this Structure.  # noqa: E501


        :return: The values of this Structure.  # noqa: E501
        :rtype: list[StructureElement]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this Structure.


        :param values: The values of this Structure.  # noqa: E501
        :type: list[StructureElement]
        """

        self._values = values

    @property
    def number_of_assets(self):
        """Gets the number_of_assets of this Structure.  # noqa: E501


        :return: The number_of_assets of this Structure.  # noqa: E501
        :rtype: int
        """
        return self._number_of_assets

    @number_of_assets.setter
    def number_of_assets(self, number_of_assets):
        """Sets the number_of_assets of this Structure.


        :param number_of_assets: The number_of_assets of this Structure.  # noqa: E501
        :type: int
        """

        self._number_of_assets = number_of_assets

    @property
    def last_rebalanced(self):
        """Gets the last_rebalanced of this Structure.  # noqa: E501


        :return: The last_rebalanced of this Structure.  # noqa: E501
        :rtype: int
        """
        return self._last_rebalanced

    @last_rebalanced.setter
    def last_rebalanced(self, last_rebalanced):
        """Sets the last_rebalanced of this Structure.


        :param last_rebalanced: The last_rebalanced of this Structure.  # noqa: E501
        :type: int
        """

        self._last_rebalanced = last_rebalanced

    @property
    def monthly_rebalanced_count(self):
        """Gets the monthly_rebalanced_count of this Structure.  # noqa: E501


        :return: The monthly_rebalanced_count of this Structure.  # noqa: E501
        :rtype: int
        """
        return self._monthly_rebalanced_count

    @monthly_rebalanced_count.setter
    def monthly_rebalanced_count(self, monthly_rebalanced_count):
        """Sets the monthly_rebalanced_count of this Structure.


        :param monthly_rebalanced_count: The monthly_rebalanced_count of this Structure.  # noqa: E501
        :type: int
        """

        self._monthly_rebalanced_count = monthly_rebalanced_count

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
        if issubclass(Structure, dict):
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
        if not isinstance(other, Structure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
