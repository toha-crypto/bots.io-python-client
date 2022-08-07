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

class Ticker(object):
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
        'currency': 'str',
        'price': 'float',
        'change24h': 'float',
        'change7d': 'float',
        'change1m': 'float',
        'change3m': 'float',
        'change6m': 'float',
        'change12m': 'float',
        'change_all': 'float',
        'aum': 'float'
    }

    attribute_map = {
        'ticker': 'ticker',
        'currency': 'currency',
        'price': 'price',
        'change24h': 'change24h',
        'change7d': 'change7d',
        'change1m': 'change1m',
        'change3m': 'change3m',
        'change6m': 'change6m',
        'change12m': 'change12m',
        'change_all': 'changeAll',
        'aum': 'aum'
    }

    def __init__(self, ticker=None, currency=None, price=None, change24h=None, change7d=None, change1m=None, change3m=None, change6m=None, change12m=None, change_all=None, aum=None):  # noqa: E501
        """Ticker - a model defined in Swagger"""  # noqa: E501
        self._ticker = None
        self._currency = None
        self._price = None
        self._change24h = None
        self._change7d = None
        self._change1m = None
        self._change3m = None
        self._change6m = None
        self._change12m = None
        self._change_all = None
        self._aum = None
        self.discriminator = None
        if ticker is not None:
            self.ticker = ticker
        if currency is not None:
            self.currency = currency
        if price is not None:
            self.price = price
        if change24h is not None:
            self.change24h = change24h
        if change7d is not None:
            self.change7d = change7d
        if change1m is not None:
            self.change1m = change1m
        if change3m is not None:
            self.change3m = change3m
        if change6m is not None:
            self.change6m = change6m
        if change12m is not None:
            self.change12m = change12m
        if change_all is not None:
            self.change_all = change_all
        if aum is not None:
            self.aum = aum

    @property
    def ticker(self):
        """Gets the ticker of this Ticker.  # noqa: E501


        :return: The ticker of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this Ticker.


        :param ticker: The ticker of this Ticker.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def currency(self):
        """Gets the currency of this Ticker.  # noqa: E501


        :return: The currency of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Ticker.


        :param currency: The currency of this Ticker.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def price(self):
        """Gets the price of this Ticker.  # noqa: E501


        :return: The price of this Ticker.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Ticker.


        :param price: The price of this Ticker.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def change24h(self):
        """Gets the change24h of this Ticker.  # noqa: E501


        :return: The change24h of this Ticker.  # noqa: E501
        :rtype: float
        """
        return self._change24h

    @change24h.setter
    def change24h(self, change24h):
        """Sets the change24h of this Ticker.


        :param change24h: The change24h of this Ticker.  # noqa: E501
        :type: float
        """

        self._change24h = change24h

    @property
    def change7d(self):
        """Gets the change7d of this Ticker.  # noqa: E501


        :return: The change7d of this Ticker.  # noqa: E501
        :rtype: float
        """
        return self._change7d

    @change7d.setter
    def change7d(self, change7d):
        """Sets the change7d of this Ticker.


        :param change7d: The change7d of this Ticker.  # noqa: E501
        :type: float
        """

        self._change7d = change7d

    @property
    def change1m(self):
        """Gets the change1m of this Ticker.  # noqa: E501


        :return: The change1m of this Ticker.  # noqa: E501
        :rtype: float
        """
        return self._change1m

    @change1m.setter
    def change1m(self, change1m):
        """Sets the change1m of this Ticker.


        :param change1m: The change1m of this Ticker.  # noqa: E501
        :type: float
        """

        self._change1m = change1m

    @property
    def change3m(self):
        """Gets the change3m of this Ticker.  # noqa: E501


        :return: The change3m of this Ticker.  # noqa: E501
        :rtype: float
        """
        return self._change3m

    @change3m.setter
    def change3m(self, change3m):
        """Sets the change3m of this Ticker.


        :param change3m: The change3m of this Ticker.  # noqa: E501
        :type: float
        """

        self._change3m = change3m

    @property
    def change6m(self):
        """Gets the change6m of this Ticker.  # noqa: E501


        :return: The change6m of this Ticker.  # noqa: E501
        :rtype: float
        """
        return self._change6m

    @change6m.setter
    def change6m(self, change6m):
        """Sets the change6m of this Ticker.


        :param change6m: The change6m of this Ticker.  # noqa: E501
        :type: float
        """

        self._change6m = change6m

    @property
    def change12m(self):
        """Gets the change12m of this Ticker.  # noqa: E501


        :return: The change12m of this Ticker.  # noqa: E501
        :rtype: float
        """
        return self._change12m

    @change12m.setter
    def change12m(self, change12m):
        """Sets the change12m of this Ticker.


        :param change12m: The change12m of this Ticker.  # noqa: E501
        :type: float
        """

        self._change12m = change12m

    @property
    def change_all(self):
        """Gets the change_all of this Ticker.  # noqa: E501


        :return: The change_all of this Ticker.  # noqa: E501
        :rtype: float
        """
        return self._change_all

    @change_all.setter
    def change_all(self, change_all):
        """Sets the change_all of this Ticker.


        :param change_all: The change_all of this Ticker.  # noqa: E501
        :type: float
        """

        self._change_all = change_all

    @property
    def aum(self):
        """Gets the aum of this Ticker.  # noqa: E501


        :return: The aum of this Ticker.  # noqa: E501
        :rtype: float
        """
        return self._aum

    @aum.setter
    def aum(self, aum):
        """Sets the aum of this Ticker.


        :param aum: The aum of this Ticker.  # noqa: E501
        :type: float
        """

        self._aum = aum

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
        if issubclass(Ticker, dict):
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
        if not isinstance(other, Ticker):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
