# coding: utf-8

"""
    Iconomi API!

    # Introduction Welcome to the ICONOMI Platform API. There are two ways to integrate with the ICONOMI platform, the REST API and a stream-oriented API using Websockets.  ## Versioning  This API maintains backward compatibility. Breaking changes to the API are managed by providing new endpoints. Old versions will remain available for two months after a new version is released and can then be removed at any time. All information about releases is published on this website. Non-breaking changes are released in the same major-version API.  ## Types  All request bodies should have content type application/json and be valid JSON.  <br/>  ### Timestamps  Unless otherwise specified, all timestamps will be returned in ISO 8601 with microseconds.  <br/> Example:  ``` 2019-08-01T01:02:03.000004Z ```  <br/>  ### Numbers  Integers are unquoted.  <br/> Example:  ``` \"x\": 194767 ```  Decimals are returned as strings with a period as a decimal separator and no thousands separator.  <br/> Example:  ``` \"price\": \"3.3847\" ```  <br/>  ### IDs  All IDs are UUIDs.  <br/> Example:  ```  6EFB3D83-830A-42F8-84CD-2C307FE62AD8 ```  <br/>  ### Enumerations  There are several enumerations on the platform that are used across the platform.  #### Strategy types There are different types of strategies supported on the platform which use different behaviour for  investment:  * **PASSIVE** - Strategies that have structures based set on percentages and are rebalances less often  * **ACTIVE** - Strategies that follow a more active strategy not using an index  #### Granulations  Depending on the time period selected different granulation of data is possible as a result.  For each of the granulations there will be one data point available:  * **TWO_MINUTE** - only available for institutional strategies. * **FIVE_MINUTE** * **HOURLY** * **THREE_HOURLY** * **EIGHT_HOURLY** * **DAILY**  ## Rate limiting  The public API (both the REST API and the Websocket API) allows for 60 requests per minute. This rate is subject to change.  ## Authentication  To access authenticated endpoints you need an account on the ICONOMI platform. After you have an account you need to setup your api keys (you can find the option under Settings).  ### Creating a request  All REST requests must contain the following headers:  * **ICN-API-KEY** - The api key as a string. * **ICN-SIGN** - The base64-encoded signature (see Signing a Message). * **ICN-TIMESTAMP** - A timestamp for your request in epoch milliseconds.  <br/>   ### Signing a Message  You generate the **ICN-SIGN** header by creating a **sha512 HMAC** using the base64-decoded secret key on the prehash string timestamp + method + requestPath + body (where + represents string concatenation) and base64-encode the output, where: * the timestamp value is the same as the **ICN-TIMESTAMP** header. * the body is the request body string or omitted if there is no request body (typically for GET requests).  * method must always be in upper case * the request path starts with /v1/ and doesn't include query parameters   Pseudocode example: ```  base64_encode(HMAC_SHA512(secret_key, timestamp + upper_case(method) + requestPath + body)) ```  Java code example: ``` String apiSecret = \"...\"; String toSign = timestamp + method.toUpperCase() + requestPath + body; SecretKeySpec signingKey = new SecretKeySpec(apiSecret.getBytes(), \"HmacSHA512\"); Mac mac = Mac.getInstance(signingKey.getAlgorithm()); mac.init(signingKey); String digest = Base64.getEncoder().encodeToString(mac.doFinal(toSign.getBytes())); ```  Example of a POST with a body: ``` secret = '51ffd0604d4ba42790b42860fc1e98ac6a4b60e32e078b801d899c6eb04bc29e' timestamp = '1643118174153' method = 'post' requestPath = '/v1/order' body = '{\"amount\":100,\"source_ticker\":\"EUR\",\"target_ticker\":\"BTC\",\"fitting_speed_type\":\"FAST\"}'  string to encode = '1643118174153POST/v1/order{\"amount\":100,\"source_ticker\":\"EUR\",\"target_ticker\":\"BTC\",\"fitting_speed_type\":\"FAST\"}'  base64 encoded signature = 'tD9pi/UhcVp8BeQyahBDRQnkIm0avWmE1JMZlCEveZ66whMZ0YsHWfzFz6G14FhRunPR/rFbbFZuRkOLXEIoEA==' ``` Example of GET with query parameters: ``` secret = '51ffd0604d4ba42790b42860fc1e98ac6a4b60e32e078b801d899c6eb04bc29e' timestamp = '1643178751655' method = 'get' requestPath = '/v1/user/activity?type=FEES_AND_EARNINGS&pageSize=4&pageNumber=0' body = <empty>  string to encode = '1643178751655GET/v1/user/activity'  base64 encoded signature = 'efIB1zs7yunvzvCUL1SPWh5IAjU2b+g51vSPdGSX69KjJIVbtJQKIc2yVTaZlQIoReu6hx39r4w9dTDJhRdgdA==' ```   <br/>  ### Postman  You can also try with <a href=\"https://www.postman.com/downloads/\" target=\"_blank\" rel=\"nofollow\">postman client</a>. After you import <a href=\"https://www.postman.com/collections/2d5e387a761a6da9f022\" target=\"_blank\" rel=\"nofollow\">collection</a> into client, you have to create new environment under \"Manage environments\" and add two variables:  <br>  * **ICN-API-KEY** - The api key from your account on ICONOMI platform * **ICN-SECRET** - The secret key from your account on ICONOMI platform  <br/>  Before you execute any of those endpoints, environment must be selected.  ### Websocket Authentication  It is possible to authenticate yourself when subscribing to the websocket feed.  When opening connection to websocket, add additional headers, as if you were signing a request. To get the necessary parameters, you would go through the same process as you do to make authenticated calls to the API.  ## Sample libraries You can find sample libraries for communicating with our API at our <a href=\"https://github.com/iconomi-ag\" target=\"_blank\" rel=\"nofollow\">github page.</a>  ## Bug reports For any bug reports in the documentation or the API, feel free to report them to our <a href=\"https://github.com/iconomi-ag/iconomi-api\" target=\"_blank\" rel=\"nofollow\">github page.</a>  # noqa: E501

    OpenAPI spec version: 1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AssetApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def asset_details(self, ticker, **kwargs):  # noqa: E501
        """Asset details  # noqa: E501

        Returns information about one specific Asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_details(ticker, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ticker: (required)
        :return: AssetInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.asset_details_with_http_info(ticker, **kwargs)  # noqa: E501
        else:
            (data) = self.asset_details_with_http_info(ticker, **kwargs)  # noqa: E501
            return data

    def asset_details_with_http_info(self, ticker, **kwargs):  # noqa: E501
        """Asset details  # noqa: E501

        Returns information about one specific Asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_details_with_http_info(ticker, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ticker: (required)
        :return: AssetInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ticker']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method asset_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ticker' is set
        if ('ticker' not in params or
                params['ticker'] is None):
            raise ValueError("Missing the required parameter `ticker` when calling `asset_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ticker' in params:
            path_params['ticker'] = params['ticker']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/assets/{ticker}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssetInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def asset_history(self, ticker, **kwargs):  # noqa: E501
        """Historical information  # noqa: E501

        The price history returns data points for the given period. Different granulation of data can be returned based on the length of the period provided from daily to 5 minute (one  price point per period).  From and to are optional parameters (both are either supplied or neither is supplied). If from/to are not supplied a default of last month is returned with hourly granulation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_history(ticker, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ticker: (required)
        :param str currency:
        :param int _from:
        :param int to:
        :param str granulation:
        :return: Chart
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.asset_history_with_http_info(ticker, **kwargs)  # noqa: E501
        else:
            (data) = self.asset_history_with_http_info(ticker, **kwargs)  # noqa: E501
            return data

    def asset_history_with_http_info(self, ticker, **kwargs):  # noqa: E501
        """Historical information  # noqa: E501

        The price history returns data points for the given period. Different granulation of data can be returned based on the length of the period provided from daily to 5 minute (one  price point per period).  From and to are optional parameters (both are either supplied or neither is supplied). If from/to are not supplied a default of last month is returned with hourly granulation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_history_with_http_info(ticker, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ticker: (required)
        :param str currency:
        :param int _from:
        :param int to:
        :param str granulation:
        :return: Chart
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ticker', 'currency', '_from', 'to', 'granulation']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method asset_history" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ticker' is set
        if ('ticker' not in params or
                params['ticker'] is None):
            raise ValueError("Missing the required parameter `ticker` when calling `asset_history`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ticker' in params:
            path_params['ticker'] = params['ticker']  # noqa: E501

        query_params = []
        if 'currency' in params:
            query_params.append(('currency', params['currency']))  # noqa: E501
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501
        if 'granulation' in params:
            query_params.append(('granulation', params['granulation']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/assets/{ticker}/pricehistory', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Chart',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def asset_list(self, **kwargs):  # noqa: E501
        """List of Assets  # noqa: E501

        Returns a list of all assets on platform.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Asset]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.asset_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.asset_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def asset_list_with_http_info(self, **kwargs):  # noqa: E501
        """List of Assets  # noqa: E501

        Returns a list of all assets on platform.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Asset]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method asset_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/assets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Asset]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def asset_statistics(self, ticker, **kwargs):  # noqa: E501
        """Statistics  # noqa: E501

        Returns statistics of the strategy; returns, max drawdown and volatility for strategy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_statistics(ticker, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ticker: (required)
        :param str currency:
        :return: Statistics
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.asset_statistics_with_http_info(ticker, **kwargs)  # noqa: E501
        else:
            (data) = self.asset_statistics_with_http_info(ticker, **kwargs)  # noqa: E501
            return data

    def asset_statistics_with_http_info(self, ticker, **kwargs):  # noqa: E501
        """Statistics  # noqa: E501

        Returns statistics of the strategy; returns, max drawdown and volatility for strategy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_statistics_with_http_info(ticker, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ticker: (required)
        :param str currency:
        :return: Statistics
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ticker', 'currency']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method asset_statistics" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ticker' is set
        if ('ticker' not in params or
                params['ticker'] is None):
            raise ValueError("Missing the required parameter `ticker` when calling `asset_statistics`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ticker' in params:
            path_params['ticker'] = params['ticker']  # noqa: E501

        query_params = []
        if 'currency' in params:
            query_params.append(('currency', params['currency']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/assets/{ticker}/statistics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Statistics',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def asset_ticker(self, ticker, **kwargs):  # noqa: E501
        """Current ticker  # noqa: E501

        Returns the current ticker of the Asset. The price is refreshed every minute.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_ticker(ticker, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ticker: (required)
        :param str currency:
        :return: Ticker
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.asset_ticker_with_http_info(ticker, **kwargs)  # noqa: E501
        else:
            (data) = self.asset_ticker_with_http_info(ticker, **kwargs)  # noqa: E501
            return data

    def asset_ticker_with_http_info(self, ticker, **kwargs):  # noqa: E501
        """Current ticker  # noqa: E501

        Returns the current ticker of the Asset. The price is refreshed every minute.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_ticker_with_http_info(ticker, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ticker: (required)
        :param str currency:
        :return: Ticker
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ticker', 'currency']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method asset_ticker" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ticker' is set
        if ('ticker' not in params or
                params['ticker'] is None):
            raise ValueError("Missing the required parameter `ticker` when calling `asset_ticker`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ticker' in params:
            path_params['ticker'] = params['ticker']  # noqa: E501

        query_params = []
        if 'currency' in params:
            query_params.append(('currency', params['currency']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/assets/{ticker}/price', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Ticker',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
