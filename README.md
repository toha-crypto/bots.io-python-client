# swagger-client
# Introduction Welcome to the ICONOMI Platform API. There are two ways to integrate with the ICONOMI platform, the REST API and a stream-oriented API using Websockets.  ## Versioning  This API maintains backward compatibility. Breaking changes to the API are managed by providing new endpoints. Old versions will remain available for two months after a new version is released and can then be removed at any time. All information about releases is published on this website. Non-breaking changes are released in the same major-version API.  ## Types  All request bodies should have content type application/json and be valid JSON.  <br/>  ### Timestamps  Unless otherwise specified, all timestamps will be returned in ISO 8601 with microseconds.  <br/> Example:  ``` 2019-08-01T01:02:03.000004Z ```  <br/>  ### Numbers  Integers are unquoted.  <br/> Example:  ``` \"x\": 194767 ```  Decimals are returned as strings with a period as a decimal separator and no thousands separator.  <br/> Example:  ``` \"price\": \"3.3847\" ```  <br/>  ### IDs  All IDs are UUIDs.  <br/> Example:  ```  6EFB3D83-830A-42F8-84CD-2C307FE62AD8 ```  <br/>  ### Enumerations  There are several enumerations on the platform that are used across the platform.  #### Strategy types There are different types of strategies supported on the platform which use different behaviour for  investment:  * **PASSIVE** - Strategies that have structures based set on percentages and are rebalances less often  * **ACTIVE** - Strategies that follow a more active strategy not using an index  #### Granulations  Depending on the time period selected different granulation of data is possible as a result.  For each of the granulations there will be one data point available:  * **TWO_MINUTE** - only available for institutional strategies. * **FIVE_MINUTE** * **HOURLY** * **THREE_HOURLY** * **EIGHT_HOURLY** * **DAILY**  ## Rate limiting  The public API (both the REST API and the Websocket API) allows for 60 requests per minute. This rate is subject to change.  ## Authentication  To access authenticated endpoints you need an account on the ICONOMI platform. After you have an account you need to setup your api keys (you can find the option under Settings).  ### Creating a request  All REST requests must contain the following headers:  * **ICN-API-KEY** - The api key as a string. * **ICN-SIGN** - The base64-encoded signature (see Signing a Message). * **ICN-TIMESTAMP** - A timestamp for your request in epoch milliseconds.  <br/>   ### Signing a Message  You generate the **ICN-SIGN** header by creating a **sha512 HMAC** using the base64-decoded secret key on the prehash string timestamp + method + requestPath + body (where + represents string concatenation) and base64-encode the output, where: * the timestamp value is the same as the **ICN-TIMESTAMP** header. * the body is the request body string or omitted if there is no request body (typically for GET requests).  * method must always be in upper case * the request path starts with /v1/ and doesn't include query parameters   Pseudocode example: ```  base64_encode(HMAC_SHA512(secret_key, timestamp + upper_case(method) + requestPath + body)) ```  Java code example: ``` String apiSecret = \"...\"; String toSign = timestamp + method.toUpperCase() + requestPath + body; SecretKeySpec signingKey = new SecretKeySpec(apiSecret.getBytes(), \"HmacSHA512\"); Mac mac = Mac.getInstance(signingKey.getAlgorithm()); mac.init(signingKey); String digest = Base64.getEncoder().encodeToString(mac.doFinal(toSign.getBytes())); ```  Example of a POST with a body: ``` secret = '51ffd0604d4ba42790b42860fc1e98ac6a4b60e32e078b801d899c6eb04bc29e' timestamp = '1643118174153' method = 'post' requestPath = '/v1/order' body = '{\"amount\":100,\"source_ticker\":\"EUR\",\"target_ticker\":\"BTC\",\"fitting_speed_type\":\"FAST\"}'  string to encode = '1643118174153POST/v1/order{\"amount\":100,\"source_ticker\":\"EUR\",\"target_ticker\":\"BTC\",\"fitting_speed_type\":\"FAST\"}'  base64 encoded signature = 'tD9pi/UhcVp8BeQyahBDRQnkIm0avWmE1JMZlCEveZ66whMZ0YsHWfzFz6G14FhRunPR/rFbbFZuRkOLXEIoEA==' ``` Example of GET with query parameters: ``` secret = '51ffd0604d4ba42790b42860fc1e98ac6a4b60e32e078b801d899c6eb04bc29e' timestamp = '1643178751655' method = 'get' requestPath = '/v1/user/activity?type=FEES_AND_EARNINGS&pageSize=4&pageNumber=0' body = <empty>  string to encode = '1643178751655GET/v1/user/activity'  base64 encoded signature = 'efIB1zs7yunvzvCUL1SPWh5IAjU2b+g51vSPdGSX69KjJIVbtJQKIc2yVTaZlQIoReu6hx39r4w9dTDJhRdgdA==' ```   <br/>  ### Postman  You can also try with <a href=\"https://www.postman.com/downloads/\" target=\"_blank\" rel=\"nofollow\">postman client</a>. After you import <a href=\"https://www.postman.com/collections/2d5e387a761a6da9f022\" target=\"_blank\" rel=\"nofollow\">collection</a> into client, you have to create new environment under \"Manage environments\" and add two variables:  <br>  * **ICN-API-KEY** - The api key from your account on ICONOMI platform * **ICN-SECRET** - The secret key from your account on ICONOMI platform  <br/>  Before you execute any of those endpoints, environment must be selected.  ### Websocket Authentication  It is possible to authenticate yourself when subscribing to the websocket feed.  When opening connection to websocket, add additional headers, as if you were signing a request. To get the necessary parameters, you would go through the same process as you do to make authenticated calls to the API.  ## Sample libraries You can find sample libraries for communicating with our API at our <a href=\"https://github.com/iconomi-ag\" target=\"_blank\" rel=\"nofollow\">github page.</a>  ## Bug reports For any bug reports in the documentation or the API, feel free to report them to our <a href=\"https://github.com/iconomi-ag/iconomi-api\" target=\"_blank\" rel=\"nofollow\">github page.</a>

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.3
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi(swagger_client.ApiClient(configuration))
ticker = 'ticker_example' # str | 

try:
    # Asset details
    api_response = api_instance.asset_details(ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->asset_details: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AssetApi(swagger_client.ApiClient(configuration))
ticker = 'ticker_example' # str | 
currency = 'USD' # str |  (optional) (default to USD)
_from = 789 # int |  (optional)
to = 789 # int |  (optional)
granulation = 'granulation_example' # str |  (optional)

try:
    # Historical information
    api_response = api_instance.asset_history(ticker, currency=currency, _from=_from, to=to, granulation=granulation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->asset_history: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AssetApi(swagger_client.ApiClient(configuration))

try:
    # List of Assets
    api_response = api_instance.asset_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->asset_list: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AssetApi(swagger_client.ApiClient(configuration))
ticker = 'ticker_example' # str | 
currency = 'USD' # str |  (optional) (default to USD)

try:
    # Statistics
    api_response = api_instance.asset_statistics(ticker, currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->asset_statistics: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AssetApi(swagger_client.ApiClient(configuration))
ticker = 'ticker_example' # str | 
currency = 'USD' # str |  (optional) (default to USD)

try:
    # Current ticker
    api_response = api_instance.asset_ticker(ticker, currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->asset_ticker: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.iconomi.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AssetApi* | [**asset_details**](docs/AssetApi.md#asset_details) | **GET** /v1/assets/{ticker} | Asset details
*AssetApi* | [**asset_history**](docs/AssetApi.md#asset_history) | **GET** /v1/assets/{ticker}/pricehistory | Historical information
*AssetApi* | [**asset_list**](docs/AssetApi.md#asset_list) | **GET** /v1/assets | List of Assets
*AssetApi* | [**asset_statistics**](docs/AssetApi.md#asset_statistics) | **GET** /v1/assets/{ticker}/statistics | Statistics
*AssetApi* | [**asset_ticker**](docs/AssetApi.md#asset_ticker) | **GET** /v1/assets/{ticker}/price | Current ticker
*StrategiesApi* | [**charts**](docs/StrategiesApi.md#charts) | **GET** /v1/strategies/{ticker}/pricehistory | Historical information
*StrategiesApi* | [**daa_balance**](docs/StrategiesApi.md#daa_balance) | **GET** /v1/strategies/{ticker}/balance | Balance
*StrategiesApi* | [**daa_price**](docs/StrategiesApi.md#daa_price) | **GET** /v1/strategies/{ticker}/price | Current ticker
*StrategiesApi* | [**fitting_info**](docs/StrategiesApi.md#fitting_info) | **GET** /v1/strategies/{ticker}/structure/info | Structure info
*StrategiesApi* | [**get_statistics**](docs/StrategiesApi.md#get_statistics) | **GET** /v1/strategies/{ticker}/statistics | Statistics
*StrategiesApi* | [**info**](docs/StrategiesApi.md#info) | **GET** /v1/strategies/{ticker} | Strategy details
*StrategiesApi* | [**posts**](docs/StrategiesApi.md#posts) | **GET** /v1/strategies/{ticker}/posts | Strategy posts
*StrategiesApi* | [**strategy_list**](docs/StrategiesApi.md#strategy_list) | **GET** /v1/strategies | List of Strategies
*StrategiesApi* | [**structure**](docs/StrategiesApi.md#structure) | **GET** /v1/strategies/{ticker}/structure | Structure
*StrategiesApi* | [**submit_structure**](docs/StrategiesApi.md#submit_structure) | **POST** /v1/strategies/{ticker}/structure | Structure
*TradingApi* | [**cancel_order**](docs/TradingApi.md#cancel_order) | **DELETE** /v1/order/{orderId} | Delete
*TradingApi* | [**confirm_offer**](docs/TradingApi.md#confirm_offer) | **POST** /v1/order/offer/{offerId}/confirm | Confirm trade offer
*TradingApi* | [**get_all_orders**](docs/TradingApi.md#get_all_orders) | **GET** /v1/order/orders | List of orders
*TradingApi* | [**order_offer**](docs/TradingApi.md#order_offer) | **POST** /v1/order/offer | Trade offer
*TradingApi* | [**order_trade**](docs/TradingApi.md#order_trade) | **POST** /v1/order | Place order
*TradingApi* | [**status**](docs/TradingApi.md#status) | **GET** /v1/order/{orderId} | Logical order
*UserApi* | [**get_activities**](docs/UserApi.md#get_activities) | **GET** /v1/user/activity | Activity
*UserApi* | [**get_deposit_address**](docs/UserApi.md#get_deposit_address) | **GET** /v1/user/deposit/{currency} | Deposit
*UserApi* | [**get_user_balance**](docs/UserApi.md#get_user_balance) | **GET** /v1/user/balance | User Balance
*UserApi* | [**portfolio_history**](docs/UserApi.md#portfolio_history) | **POST** /v1/user/portfoliohistory | Portfolio value history
*UserApi* | [**transaction_info**](docs/UserApi.md#transaction_info) | **GET** /v1/user/transaction/{transactionId} | Transaction
*UserApi* | [**withdraw**](docs/UserApi.md#withdraw) | **POST** /v1/user/withdraw | Withdraw

## Documentation For Models

 - [Activity](docs/Activity.md)
 - [Asset](docs/Asset.md)
 - [AssetInfo](docs/AssetInfo.md)
 - [Balance](docs/Balance.md)
 - [BalanceEntry](docs/BalanceEntry.md)
 - [Chart](docs/Chart.md)
 - [ChartPoint](docs/ChartPoint.md)
 - [Deposit](docs/Deposit.md)
 - [EnumMapIntervalBigDecimal](docs/EnumMapIntervalBigDecimal.md)
 - [FittingInfo](docs/FittingInfo.md)
 - [Order](docs/Order.md)
 - [OrderInfo](docs/OrderInfo.md)
 - [OrderOffer](docs/OrderOffer.md)
 - [PortfolioHistory](docs/PortfolioHistory.md)
 - [Post](docs/Post.md)
 - [Posts](docs/Posts.md)
 - [Statistics](docs/Statistics.md)
 - [StatisticsReturns](docs/StatisticsReturns.md)
 - [Strategy](docs/Strategy.md)
 - [StrategyBalance](docs/StrategyBalance.md)
 - [StrategyBalanceElement](docs/StrategyBalanceElement.md)
 - [Structure](docs/Structure.md)
 - [StructureElement](docs/StructureElement.md)
 - [StructureSubmit](docs/StructureSubmit.md)
 - [SubmitStructureElement](docs/SubmitStructureElement.md)
 - [Ticker](docs/Ticker.md)
 - [TradeConfirm](docs/TradeConfirm.md)
 - [TradeOffer](docs/TradeOffer.md)
 - [Transaction](docs/Transaction.md)
 - [Withdraw](docs/Withdraw.md)

## Documentation For Authorization


## ApiKey

- **Type**: API key
- **API key parameter name**: ICN-API-KEY
- **Location**: HTTP header

## ApiSign

- **Type**: API key
- **API key parameter name**: ICN-SIGN
- **Location**: HTTP header

## ApiTimestamp

- **Type**: API key
- **API key parameter name**: ICN-TIMESTAMP
- **Location**: HTTP header


## Author


