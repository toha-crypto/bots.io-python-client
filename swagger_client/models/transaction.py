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

class Transaction(object):
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
        'transaction_id': 'str',
        'timestamp': 'int',
        'status': 'str',
        'exchange_rate': 'float',
        'payment_method': 'str',
        'address': 'str',
        'type': 'str',
        'kind': 'str',
        'amount_ticker': 'str',
        'amount': 'float',
        'source_ticker': 'str',
        'source_amount': 'float',
        'target_ticker': 'str',
        'target_amount': 'float',
        'fee_ticker': 'str',
        'fee_amount': 'float',
        'vat_ticker': 'str',
        'vat_amount': 'float',
        'performance_fee_ticker': 'str',
        'performance_fee_amount': 'float',
        'profit_ticker': 'str',
        'profit_amount': 'float'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'timestamp': 'timestamp',
        'status': 'status',
        'exchange_rate': 'exchangeRate',
        'payment_method': 'paymentMethod',
        'address': 'address',
        'type': 'type',
        'kind': 'kind',
        'amount_ticker': 'amount_ticker',
        'amount': 'amount',
        'source_ticker': 'source_ticker',
        'source_amount': 'source_amount',
        'target_ticker': 'target_ticker',
        'target_amount': 'target_amount',
        'fee_ticker': 'fee_ticker',
        'fee_amount': 'fee_amount',
        'vat_ticker': 'vat_ticker',
        'vat_amount': 'vat_amount',
        'performance_fee_ticker': 'performance_fee_ticker',
        'performance_fee_amount': 'performance_fee_amount',
        'profit_ticker': 'profit_ticker',
        'profit_amount': 'profit_amount'
    }

    def __init__(self, transaction_id=None, timestamp=None, status=None, exchange_rate=None, payment_method=None, address=None, type=None, kind=None, amount_ticker=None, amount=None, source_ticker=None, source_amount=None, target_ticker=None, target_amount=None, fee_ticker=None, fee_amount=None, vat_ticker=None, vat_amount=None, performance_fee_ticker=None, performance_fee_amount=None, profit_ticker=None, profit_amount=None):  # noqa: E501
        """Transaction - a model defined in Swagger"""  # noqa: E501
        self._transaction_id = None
        self._timestamp = None
        self._status = None
        self._exchange_rate = None
        self._payment_method = None
        self._address = None
        self._type = None
        self._kind = None
        self._amount_ticker = None
        self._amount = None
        self._source_ticker = None
        self._source_amount = None
        self._target_ticker = None
        self._target_amount = None
        self._fee_ticker = None
        self._fee_amount = None
        self._vat_ticker = None
        self._vat_amount = None
        self._performance_fee_ticker = None
        self._performance_fee_amount = None
        self._profit_ticker = None
        self._profit_amount = None
        self.discriminator = None
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if timestamp is not None:
            self.timestamp = timestamp
        if status is not None:
            self.status = status
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if payment_method is not None:
            self.payment_method = payment_method
        if address is not None:
            self.address = address
        if type is not None:
            self.type = type
        if kind is not None:
            self.kind = kind
        self.amount_ticker = amount_ticker
        if amount is not None:
            self.amount = amount
        self.source_ticker = source_ticker
        if source_amount is not None:
            self.source_amount = source_amount
        self.target_ticker = target_ticker
        if target_amount is not None:
            self.target_amount = target_amount
        self.fee_ticker = fee_ticker
        if fee_amount is not None:
            self.fee_amount = fee_amount
        self.vat_ticker = vat_ticker
        if vat_amount is not None:
            self.vat_amount = vat_amount
        self.performance_fee_ticker = performance_fee_ticker
        if performance_fee_amount is not None:
            self.performance_fee_amount = performance_fee_amount
        self.profit_ticker = profit_ticker
        if profit_amount is not None:
            self.profit_amount = profit_amount

    @property
    def transaction_id(self):
        """Gets the transaction_id of this Transaction.  # noqa: E501


        :return: The transaction_id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this Transaction.


        :param transaction_id: The transaction_id of this Transaction.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def timestamp(self):
        """Gets the timestamp of this Transaction.  # noqa: E501


        :return: The timestamp of this Transaction.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Transaction.


        :param timestamp: The timestamp of this Transaction.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def status(self):
        """Gets the status of this Transaction.  # noqa: E501


        :return: The status of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Transaction.


        :param status: The status of this Transaction.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this Transaction.  # noqa: E501


        :return: The exchange_rate of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this Transaction.


        :param exchange_rate: The exchange_rate of this Transaction.  # noqa: E501
        :type: float
        """

        self._exchange_rate = exchange_rate

    @property
    def payment_method(self):
        """Gets the payment_method of this Transaction.  # noqa: E501


        :return: The payment_method of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this Transaction.


        :param payment_method: The payment_method of this Transaction.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def address(self):
        """Gets the address of this Transaction.  # noqa: E501


        :return: The address of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Transaction.


        :param address: The address of this Transaction.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def type(self):
        """Gets the type of this Transaction.  # noqa: E501


        :return: The type of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Transaction.


        :param type: The type of this Transaction.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def kind(self):
        """Gets the kind of this Transaction.  # noqa: E501


        :return: The kind of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Transaction.


        :param kind: The kind of this Transaction.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def amount_ticker(self):
        """Gets the amount_ticker of this Transaction.  # noqa: E501


        :return: The amount_ticker of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._amount_ticker

    @amount_ticker.setter
    def amount_ticker(self, amount_ticker):
        """Sets the amount_ticker of this Transaction.


        :param amount_ticker: The amount_ticker of this Transaction.  # noqa: E501
        :type: str
        """
        if amount_ticker is None:
            raise ValueError("Invalid value for `amount_ticker`, must not be `None`")  # noqa: E501

        self._amount_ticker = amount_ticker

    @property
    def amount(self):
        """Gets the amount of this Transaction.  # noqa: E501


        :return: The amount of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Transaction.


        :param amount: The amount of this Transaction.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def source_ticker(self):
        """Gets the source_ticker of this Transaction.  # noqa: E501


        :return: The source_ticker of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._source_ticker

    @source_ticker.setter
    def source_ticker(self, source_ticker):
        """Sets the source_ticker of this Transaction.


        :param source_ticker: The source_ticker of this Transaction.  # noqa: E501
        :type: str
        """
        if source_ticker is None:
            raise ValueError("Invalid value for `source_ticker`, must not be `None`")  # noqa: E501

        self._source_ticker = source_ticker

    @property
    def source_amount(self):
        """Gets the source_amount of this Transaction.  # noqa: E501


        :return: The source_amount of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._source_amount

    @source_amount.setter
    def source_amount(self, source_amount):
        """Sets the source_amount of this Transaction.


        :param source_amount: The source_amount of this Transaction.  # noqa: E501
        :type: float
        """

        self._source_amount = source_amount

    @property
    def target_ticker(self):
        """Gets the target_ticker of this Transaction.  # noqa: E501


        :return: The target_ticker of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._target_ticker

    @target_ticker.setter
    def target_ticker(self, target_ticker):
        """Sets the target_ticker of this Transaction.


        :param target_ticker: The target_ticker of this Transaction.  # noqa: E501
        :type: str
        """
        if target_ticker is None:
            raise ValueError("Invalid value for `target_ticker`, must not be `None`")  # noqa: E501

        self._target_ticker = target_ticker

    @property
    def target_amount(self):
        """Gets the target_amount of this Transaction.  # noqa: E501


        :return: The target_amount of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._target_amount

    @target_amount.setter
    def target_amount(self, target_amount):
        """Sets the target_amount of this Transaction.


        :param target_amount: The target_amount of this Transaction.  # noqa: E501
        :type: float
        """

        self._target_amount = target_amount

    @property
    def fee_ticker(self):
        """Gets the fee_ticker of this Transaction.  # noqa: E501


        :return: The fee_ticker of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._fee_ticker

    @fee_ticker.setter
    def fee_ticker(self, fee_ticker):
        """Sets the fee_ticker of this Transaction.


        :param fee_ticker: The fee_ticker of this Transaction.  # noqa: E501
        :type: str
        """
        if fee_ticker is None:
            raise ValueError("Invalid value for `fee_ticker`, must not be `None`")  # noqa: E501

        self._fee_ticker = fee_ticker

    @property
    def fee_amount(self):
        """Gets the fee_amount of this Transaction.  # noqa: E501


        :return: The fee_amount of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._fee_amount

    @fee_amount.setter
    def fee_amount(self, fee_amount):
        """Sets the fee_amount of this Transaction.


        :param fee_amount: The fee_amount of this Transaction.  # noqa: E501
        :type: float
        """

        self._fee_amount = fee_amount

    @property
    def vat_ticker(self):
        """Gets the vat_ticker of this Transaction.  # noqa: E501


        :return: The vat_ticker of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._vat_ticker

    @vat_ticker.setter
    def vat_ticker(self, vat_ticker):
        """Sets the vat_ticker of this Transaction.


        :param vat_ticker: The vat_ticker of this Transaction.  # noqa: E501
        :type: str
        """
        if vat_ticker is None:
            raise ValueError("Invalid value for `vat_ticker`, must not be `None`")  # noqa: E501

        self._vat_ticker = vat_ticker

    @property
    def vat_amount(self):
        """Gets the vat_amount of this Transaction.  # noqa: E501


        :return: The vat_amount of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._vat_amount

    @vat_amount.setter
    def vat_amount(self, vat_amount):
        """Sets the vat_amount of this Transaction.


        :param vat_amount: The vat_amount of this Transaction.  # noqa: E501
        :type: float
        """

        self._vat_amount = vat_amount

    @property
    def performance_fee_ticker(self):
        """Gets the performance_fee_ticker of this Transaction.  # noqa: E501


        :return: The performance_fee_ticker of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._performance_fee_ticker

    @performance_fee_ticker.setter
    def performance_fee_ticker(self, performance_fee_ticker):
        """Sets the performance_fee_ticker of this Transaction.


        :param performance_fee_ticker: The performance_fee_ticker of this Transaction.  # noqa: E501
        :type: str
        """
        if performance_fee_ticker is None:
            raise ValueError("Invalid value for `performance_fee_ticker`, must not be `None`")  # noqa: E501

        self._performance_fee_ticker = performance_fee_ticker

    @property
    def performance_fee_amount(self):
        """Gets the performance_fee_amount of this Transaction.  # noqa: E501


        :return: The performance_fee_amount of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._performance_fee_amount

    @performance_fee_amount.setter
    def performance_fee_amount(self, performance_fee_amount):
        """Sets the performance_fee_amount of this Transaction.


        :param performance_fee_amount: The performance_fee_amount of this Transaction.  # noqa: E501
        :type: float
        """

        self._performance_fee_amount = performance_fee_amount

    @property
    def profit_ticker(self):
        """Gets the profit_ticker of this Transaction.  # noqa: E501


        :return: The profit_ticker of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._profit_ticker

    @profit_ticker.setter
    def profit_ticker(self, profit_ticker):
        """Sets the profit_ticker of this Transaction.


        :param profit_ticker: The profit_ticker of this Transaction.  # noqa: E501
        :type: str
        """
        if profit_ticker is None:
            raise ValueError("Invalid value for `profit_ticker`, must not be `None`")  # noqa: E501

        self._profit_ticker = profit_ticker

    @property
    def profit_amount(self):
        """Gets the profit_amount of this Transaction.  # noqa: E501


        :return: The profit_amount of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._profit_amount

    @profit_amount.setter
    def profit_amount(self, profit_amount):
        """Sets the profit_amount of this Transaction.


        :param profit_amount: The profit_amount of this Transaction.  # noqa: E501
        :type: float
        """

        self._profit_amount = profit_amount

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
        if issubclass(Transaction, dict):
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
        if not isinstance(other, Transaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
