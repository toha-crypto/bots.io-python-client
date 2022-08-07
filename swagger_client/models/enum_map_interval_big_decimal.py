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

class EnumMapIntervalBigDecimal(object):
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
        'day': 'float',
        'week': 'float',
        'month': 'float',
        'three_month': 'float',
        'six_month': 'float',
        'ytd': 'float',
        'year': 'float',
        'all_time': 'float'
    }

    attribute_map = {
        'day': 'DAY',
        'week': 'WEEK',
        'month': 'MONTH',
        'three_month': 'THREE_MONTH',
        'six_month': 'SIX_MONTH',
        'ytd': 'YTD',
        'year': 'YEAR',
        'all_time': 'ALL_TIME'
    }

    def __init__(self, day=None, week=None, month=None, three_month=None, six_month=None, ytd=None, year=None, all_time=None):  # noqa: E501
        """EnumMapIntervalBigDecimal - a model defined in Swagger"""  # noqa: E501
        self._day = None
        self._week = None
        self._month = None
        self._three_month = None
        self._six_month = None
        self._ytd = None
        self._year = None
        self._all_time = None
        self.discriminator = None
        if day is not None:
            self.day = day
        if week is not None:
            self.week = week
        if month is not None:
            self.month = month
        if three_month is not None:
            self.three_month = three_month
        if six_month is not None:
            self.six_month = six_month
        if ytd is not None:
            self.ytd = ytd
        if year is not None:
            self.year = year
        if all_time is not None:
            self.all_time = all_time

    @property
    def day(self):
        """Gets the day of this EnumMapIntervalBigDecimal.  # noqa: E501


        :return: The day of this EnumMapIntervalBigDecimal.  # noqa: E501
        :rtype: float
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this EnumMapIntervalBigDecimal.


        :param day: The day of this EnumMapIntervalBigDecimal.  # noqa: E501
        :type: float
        """

        self._day = day

    @property
    def week(self):
        """Gets the week of this EnumMapIntervalBigDecimal.  # noqa: E501


        :return: The week of this EnumMapIntervalBigDecimal.  # noqa: E501
        :rtype: float
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this EnumMapIntervalBigDecimal.


        :param week: The week of this EnumMapIntervalBigDecimal.  # noqa: E501
        :type: float
        """

        self._week = week

    @property
    def month(self):
        """Gets the month of this EnumMapIntervalBigDecimal.  # noqa: E501


        :return: The month of this EnumMapIntervalBigDecimal.  # noqa: E501
        :rtype: float
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this EnumMapIntervalBigDecimal.


        :param month: The month of this EnumMapIntervalBigDecimal.  # noqa: E501
        :type: float
        """

        self._month = month

    @property
    def three_month(self):
        """Gets the three_month of this EnumMapIntervalBigDecimal.  # noqa: E501


        :return: The three_month of this EnumMapIntervalBigDecimal.  # noqa: E501
        :rtype: float
        """
        return self._three_month

    @three_month.setter
    def three_month(self, three_month):
        """Sets the three_month of this EnumMapIntervalBigDecimal.


        :param three_month: The three_month of this EnumMapIntervalBigDecimal.  # noqa: E501
        :type: float
        """

        self._three_month = three_month

    @property
    def six_month(self):
        """Gets the six_month of this EnumMapIntervalBigDecimal.  # noqa: E501


        :return: The six_month of this EnumMapIntervalBigDecimal.  # noqa: E501
        :rtype: float
        """
        return self._six_month

    @six_month.setter
    def six_month(self, six_month):
        """Sets the six_month of this EnumMapIntervalBigDecimal.


        :param six_month: The six_month of this EnumMapIntervalBigDecimal.  # noqa: E501
        :type: float
        """

        self._six_month = six_month

    @property
    def ytd(self):
        """Gets the ytd of this EnumMapIntervalBigDecimal.  # noqa: E501


        :return: The ytd of this EnumMapIntervalBigDecimal.  # noqa: E501
        :rtype: float
        """
        return self._ytd

    @ytd.setter
    def ytd(self, ytd):
        """Sets the ytd of this EnumMapIntervalBigDecimal.


        :param ytd: The ytd of this EnumMapIntervalBigDecimal.  # noqa: E501
        :type: float
        """

        self._ytd = ytd

    @property
    def year(self):
        """Gets the year of this EnumMapIntervalBigDecimal.  # noqa: E501


        :return: The year of this EnumMapIntervalBigDecimal.  # noqa: E501
        :rtype: float
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this EnumMapIntervalBigDecimal.


        :param year: The year of this EnumMapIntervalBigDecimal.  # noqa: E501
        :type: float
        """

        self._year = year

    @property
    def all_time(self):
        """Gets the all_time of this EnumMapIntervalBigDecimal.  # noqa: E501


        :return: The all_time of this EnumMapIntervalBigDecimal.  # noqa: E501
        :rtype: float
        """
        return self._all_time

    @all_time.setter
    def all_time(self, all_time):
        """Sets the all_time of this EnumMapIntervalBigDecimal.


        :param all_time: The all_time of this EnumMapIntervalBigDecimal.  # noqa: E501
        :type: float
        """

        self._all_time = all_time

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
        if issubclass(EnumMapIntervalBigDecimal, dict):
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
        if not isinstance(other, EnumMapIntervalBigDecimal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
