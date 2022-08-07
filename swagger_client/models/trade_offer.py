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

class TradeOffer(object):
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
        'offer_id': 'str',
        'source_ticker': 'str',
        'target_ticker': 'str',
        'source_amount': 'float',
        'target_amount': 'float',
        'exchange_rate': 'float',
        'fee_amount': 'float',
        'fee_ticker': 'str',
        'selling_assets': 'bool',
        'valid_to': 'int',
        'server_time': 'int',
        'error': 'str',
        'used': 'bool'
    }

    attribute_map = {
        'offer_id': 'offerId',
        'source_ticker': 'sourceTicker',
        'target_ticker': 'targetTicker',
        'source_amount': 'sourceAmount',
        'target_amount': 'targetAmount',
        'exchange_rate': 'exchangeRate',
        'fee_amount': 'feeAmount',
        'fee_ticker': 'feeTicker',
        'selling_assets': 'sellingAssets',
        'valid_to': 'validTo',
        'server_time': 'serverTime',
        'error': 'error',
        'used': 'used'
    }

    def __init__(self, offer_id=None, source_ticker=None, target_ticker=None, source_amount=None, target_amount=None, exchange_rate=None, fee_amount=None, fee_ticker=None, selling_assets=None, valid_to=None, server_time=None, error=None, used=None):  # noqa: E501
        """TradeOffer - a model defined in Swagger"""  # noqa: E501
        self._offer_id = None
        self._source_ticker = None
        self._target_ticker = None
        self._source_amount = None
        self._target_amount = None
        self._exchange_rate = None
        self._fee_amount = None
        self._fee_ticker = None
        self._selling_assets = None
        self._valid_to = None
        self._server_time = None
        self._error = None
        self._used = None
        self.discriminator = None
        if offer_id is not None:
            self.offer_id = offer_id
        if source_ticker is not None:
            self.source_ticker = source_ticker
        if target_ticker is not None:
            self.target_ticker = target_ticker
        if source_amount is not None:
            self.source_amount = source_amount
        if target_amount is not None:
            self.target_amount = target_amount
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if fee_amount is not None:
            self.fee_amount = fee_amount
        if fee_ticker is not None:
            self.fee_ticker = fee_ticker
        if selling_assets is not None:
            self.selling_assets = selling_assets
        if valid_to is not None:
            self.valid_to = valid_to
        if server_time is not None:
            self.server_time = server_time
        if error is not None:
            self.error = error
        if used is not None:
            self.used = used

    @property
    def offer_id(self):
        """Gets the offer_id of this TradeOffer.  # noqa: E501


        :return: The offer_id of this TradeOffer.  # noqa: E501
        :rtype: str
        """
        return self._offer_id

    @offer_id.setter
    def offer_id(self, offer_id):
        """Sets the offer_id of this TradeOffer.


        :param offer_id: The offer_id of this TradeOffer.  # noqa: E501
        :type: str
        """

        self._offer_id = offer_id

    @property
    def source_ticker(self):
        """Gets the source_ticker of this TradeOffer.  # noqa: E501


        :return: The source_ticker of this TradeOffer.  # noqa: E501
        :rtype: str
        """
        return self._source_ticker

    @source_ticker.setter
    def source_ticker(self, source_ticker):
        """Sets the source_ticker of this TradeOffer.


        :param source_ticker: The source_ticker of this TradeOffer.  # noqa: E501
        :type: str
        """

        self._source_ticker = source_ticker

    @property
    def target_ticker(self):
        """Gets the target_ticker of this TradeOffer.  # noqa: E501


        :return: The target_ticker of this TradeOffer.  # noqa: E501
        :rtype: str
        """
        return self._target_ticker

    @target_ticker.setter
    def target_ticker(self, target_ticker):
        """Sets the target_ticker of this TradeOffer.


        :param target_ticker: The target_ticker of this TradeOffer.  # noqa: E501
        :type: str
        """

        self._target_ticker = target_ticker

    @property
    def source_amount(self):
        """Gets the source_amount of this TradeOffer.  # noqa: E501


        :return: The source_amount of this TradeOffer.  # noqa: E501
        :rtype: float
        """
        return self._source_amount

    @source_amount.setter
    def source_amount(self, source_amount):
        """Sets the source_amount of this TradeOffer.


        :param source_amount: The source_amount of this TradeOffer.  # noqa: E501
        :type: float
        """

        self._source_amount = source_amount

    @property
    def target_amount(self):
        """Gets the target_amount of this TradeOffer.  # noqa: E501


        :return: The target_amount of this TradeOffer.  # noqa: E501
        :rtype: float
        """
        return self._target_amount

    @target_amount.setter
    def target_amount(self, target_amount):
        """Sets the target_amount of this TradeOffer.


        :param target_amount: The target_amount of this TradeOffer.  # noqa: E501
        :type: float
        """

        self._target_amount = target_amount

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this TradeOffer.  # noqa: E501


        :return: The exchange_rate of this TradeOffer.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this TradeOffer.


        :param exchange_rate: The exchange_rate of this TradeOffer.  # noqa: E501
        :type: float
        """

        self._exchange_rate = exchange_rate

    @property
    def fee_amount(self):
        """Gets the fee_amount of this TradeOffer.  # noqa: E501


        :return: The fee_amount of this TradeOffer.  # noqa: E501
        :rtype: float
        """
        return self._fee_amount

    @fee_amount.setter
    def fee_amount(self, fee_amount):
        """Sets the fee_amount of this TradeOffer.


        :param fee_amount: The fee_amount of this TradeOffer.  # noqa: E501
        :type: float
        """

        self._fee_amount = fee_amount

    @property
    def fee_ticker(self):
        """Gets the fee_ticker of this TradeOffer.  # noqa: E501


        :return: The fee_ticker of this TradeOffer.  # noqa: E501
        :rtype: str
        """
        return self._fee_ticker

    @fee_ticker.setter
    def fee_ticker(self, fee_ticker):
        """Sets the fee_ticker of this TradeOffer.


        :param fee_ticker: The fee_ticker of this TradeOffer.  # noqa: E501
        :type: str
        """

        self._fee_ticker = fee_ticker

    @property
    def selling_assets(self):
        """Gets the selling_assets of this TradeOffer.  # noqa: E501


        :return: The selling_assets of this TradeOffer.  # noqa: E501
        :rtype: bool
        """
        return self._selling_assets

    @selling_assets.setter
    def selling_assets(self, selling_assets):
        """Sets the selling_assets of this TradeOffer.


        :param selling_assets: The selling_assets of this TradeOffer.  # noqa: E501
        :type: bool
        """

        self._selling_assets = selling_assets

    @property
    def valid_to(self):
        """Gets the valid_to of this TradeOffer.  # noqa: E501


        :return: The valid_to of this TradeOffer.  # noqa: E501
        :rtype: int
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        """Sets the valid_to of this TradeOffer.


        :param valid_to: The valid_to of this TradeOffer.  # noqa: E501
        :type: int
        """

        self._valid_to = valid_to

    @property
    def server_time(self):
        """Gets the server_time of this TradeOffer.  # noqa: E501


        :return: The server_time of this TradeOffer.  # noqa: E501
        :rtype: int
        """
        return self._server_time

    @server_time.setter
    def server_time(self, server_time):
        """Sets the server_time of this TradeOffer.


        :param server_time: The server_time of this TradeOffer.  # noqa: E501
        :type: int
        """

        self._server_time = server_time

    @property
    def error(self):
        """Gets the error of this TradeOffer.  # noqa: E501


        :return: The error of this TradeOffer.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this TradeOffer.


        :param error: The error of this TradeOffer.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def used(self):
        """Gets the used of this TradeOffer.  # noqa: E501


        :return: The used of this TradeOffer.  # noqa: E501
        :rtype: bool
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this TradeOffer.


        :param used: The used of this TradeOffer.  # noqa: E501
        :type: bool
        """

        self._used = used

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
        if issubclass(TradeOffer, dict):
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
        if not isinstance(other, TradeOffer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
