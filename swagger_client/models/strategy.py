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

class Strategy(object):
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
        'name': 'str',
        'manager': 'str',
        'management_type': 'str',
        'management_fee': 'float',
        'performance_fee': 'float',
        'performance_fee_collection_period': 'str',
        'entry_fee': 'float',
        'exit_fee': 'float',
        'followers': 'int'
    }

    attribute_map = {
        'ticker': 'ticker',
        'name': 'name',
        'manager': 'manager',
        'management_type': 'managementType',
        'management_fee': 'managementFee',
        'performance_fee': 'performanceFee',
        'performance_fee_collection_period': 'performanceFeeCollectionPeriod',
        'entry_fee': 'entryFee',
        'exit_fee': 'exitFee',
        'followers': 'followers'
    }

    def __init__(self, ticker=None, name=None, manager=None, management_type=None, management_fee=None, performance_fee=None, performance_fee_collection_period=None, entry_fee=None, exit_fee=None, followers=None):  # noqa: E501
        """Strategy - a model defined in Swagger"""  # noqa: E501
        self._ticker = None
        self._name = None
        self._manager = None
        self._management_type = None
        self._management_fee = None
        self._performance_fee = None
        self._performance_fee_collection_period = None
        self._entry_fee = None
        self._exit_fee = None
        self._followers = None
        self.discriminator = None
        if ticker is not None:
            self.ticker = ticker
        if name is not None:
            self.name = name
        if manager is not None:
            self.manager = manager
        if management_type is not None:
            self.management_type = management_type
        if management_fee is not None:
            self.management_fee = management_fee
        if performance_fee is not None:
            self.performance_fee = performance_fee
        if performance_fee_collection_period is not None:
            self.performance_fee_collection_period = performance_fee_collection_period
        if entry_fee is not None:
            self.entry_fee = entry_fee
        if exit_fee is not None:
            self.exit_fee = exit_fee
        if followers is not None:
            self.followers = followers

    @property
    def ticker(self):
        """Gets the ticker of this Strategy.  # noqa: E501


        :return: The ticker of this Strategy.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this Strategy.


        :param ticker: The ticker of this Strategy.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def name(self):
        """Gets the name of this Strategy.  # noqa: E501


        :return: The name of this Strategy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Strategy.


        :param name: The name of this Strategy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def manager(self):
        """Gets the manager of this Strategy.  # noqa: E501


        :return: The manager of this Strategy.  # noqa: E501
        :rtype: str
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """Sets the manager of this Strategy.


        :param manager: The manager of this Strategy.  # noqa: E501
        :type: str
        """

        self._manager = manager

    @property
    def management_type(self):
        """Gets the management_type of this Strategy.  # noqa: E501


        :return: The management_type of this Strategy.  # noqa: E501
        :rtype: str
        """
        return self._management_type

    @management_type.setter
    def management_type(self, management_type):
        """Sets the management_type of this Strategy.


        :param management_type: The management_type of this Strategy.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "PASSIVE"]  # noqa: E501
        if management_type not in allowed_values:
            raise ValueError(
                "Invalid value for `management_type` ({0}), must be one of {1}"  # noqa: E501
                .format(management_type, allowed_values)
            )

        self._management_type = management_type

    @property
    def management_fee(self):
        """Gets the management_fee of this Strategy.  # noqa: E501


        :return: The management_fee of this Strategy.  # noqa: E501
        :rtype: float
        """
        return self._management_fee

    @management_fee.setter
    def management_fee(self, management_fee):
        """Sets the management_fee of this Strategy.


        :param management_fee: The management_fee of this Strategy.  # noqa: E501
        :type: float
        """

        self._management_fee = management_fee

    @property
    def performance_fee(self):
        """Gets the performance_fee of this Strategy.  # noqa: E501


        :return: The performance_fee of this Strategy.  # noqa: E501
        :rtype: float
        """
        return self._performance_fee

    @performance_fee.setter
    def performance_fee(self, performance_fee):
        """Sets the performance_fee of this Strategy.


        :param performance_fee: The performance_fee of this Strategy.  # noqa: E501
        :type: float
        """

        self._performance_fee = performance_fee

    @property
    def performance_fee_collection_period(self):
        """Gets the performance_fee_collection_period of this Strategy.  # noqa: E501


        :return: The performance_fee_collection_period of this Strategy.  # noqa: E501
        :rtype: str
        """
        return self._performance_fee_collection_period

    @performance_fee_collection_period.setter
    def performance_fee_collection_period(self, performance_fee_collection_period):
        """Sets the performance_fee_collection_period of this Strategy.


        :param performance_fee_collection_period: The performance_fee_collection_period of this Strategy.  # noqa: E501
        :type: str
        """

        self._performance_fee_collection_period = performance_fee_collection_period

    @property
    def entry_fee(self):
        """Gets the entry_fee of this Strategy.  # noqa: E501


        :return: The entry_fee of this Strategy.  # noqa: E501
        :rtype: float
        """
        return self._entry_fee

    @entry_fee.setter
    def entry_fee(self, entry_fee):
        """Sets the entry_fee of this Strategy.


        :param entry_fee: The entry_fee of this Strategy.  # noqa: E501
        :type: float
        """

        self._entry_fee = entry_fee

    @property
    def exit_fee(self):
        """Gets the exit_fee of this Strategy.  # noqa: E501


        :return: The exit_fee of this Strategy.  # noqa: E501
        :rtype: float
        """
        return self._exit_fee

    @exit_fee.setter
    def exit_fee(self, exit_fee):
        """Sets the exit_fee of this Strategy.


        :param exit_fee: The exit_fee of this Strategy.  # noqa: E501
        :type: float
        """

        self._exit_fee = exit_fee

    @property
    def followers(self):
        """Gets the followers of this Strategy.  # noqa: E501


        :return: The followers of this Strategy.  # noqa: E501
        :rtype: int
        """
        return self._followers

    @followers.setter
    def followers(self, followers):
        """Sets the followers of this Strategy.


        :param followers: The followers of this Strategy.  # noqa: E501
        :type: int
        """

        self._followers = followers

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
        if issubclass(Strategy, dict):
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
        if not isinstance(other, Strategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
