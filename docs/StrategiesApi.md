# swagger_client.StrategiesApi

All URIs are relative to *https://api.iconomi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**charts**](StrategiesApi.md#charts) | **GET** /v1/strategies/{ticker}/pricehistory | Historical information
[**daa_balance**](StrategiesApi.md#daa_balance) | **GET** /v1/strategies/{ticker}/balance | Balance
[**daa_price**](StrategiesApi.md#daa_price) | **GET** /v1/strategies/{ticker}/price | Current ticker
[**fitting_info**](StrategiesApi.md#fitting_info) | **GET** /v1/strategies/{ticker}/structure/info | Structure info
[**get_statistics**](StrategiesApi.md#get_statistics) | **GET** /v1/strategies/{ticker}/statistics | Statistics
[**info**](StrategiesApi.md#info) | **GET** /v1/strategies/{ticker} | Strategy details
[**posts**](StrategiesApi.md#posts) | **GET** /v1/strategies/{ticker}/posts | Strategy posts
[**strategy_list**](StrategiesApi.md#strategy_list) | **GET** /v1/strategies | List of Strategies
[**structure**](StrategiesApi.md#structure) | **GET** /v1/strategies/{ticker}/structure | Structure
[**submit_structure**](StrategiesApi.md#submit_structure) | **POST** /v1/strategies/{ticker}/structure | Structure

# **charts**
> Chart charts(ticker, currency=currency, _from=_from, to=to, granulation=granulation)

Historical information

The price history returns data points for the given period. Different granulation of data can be returned based on the length of the period provided from daily to 5 minute (one  price point per period).  From and to are optional parameters (both are either suplied or neither is supplied). If from/to are not supplied a default of last month is returned with hourly granulation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
ticker = 'ticker_example' # str | 
currency = 'USD' # str |  (optional) (default to USD)
_from = 789 # int |  (optional)
to = 789 # int |  (optional)
granulation = 'granulation_example' # str | Granulation for price points. See granulation enumeration section for more details. (optional)

try:
    # Historical information
    api_response = api_instance.charts(ticker, currency=currency, _from=_from, to=to, granulation=granulation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->charts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **currency** | **str**|  | [optional] [default to USD]
 **_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **granulation** | **str**| Granulation for price points. See granulation enumeration section for more details. | [optional] 

### Return type

[**Chart**](Chart.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **daa_balance**
> StrategyBalance daa_balance(ticker)

Balance

Endpoint requires manager authentication with institutional role. Returns live balances underlying assets of strategy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
ticker = 'ticker_example' # str | 

try:
    # Balance
    api_response = api_instance.daa_balance(ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->daa_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

[**StrategyBalance**](StrategyBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **daa_price**
> Ticker daa_price(ticker, currency=currency)

Current ticker

Returns the current ticker of the Strategy. The price is refreshed every minute.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
ticker = 'ticker_example' # str | 
currency = 'USD' # str |  (optional) (default to USD)

try:
    # Current ticker
    api_response = api_instance.daa_price(ticker, currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->daa_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **currency** | **str**|  | [optional] [default to USD]

### Return type

[**Ticker**](Ticker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fitting_info**
> FittingInfo fitting_info(ticker)

Structure info

Returns the current structure info of a strategy. It contains data about new structure progress after submitting new structure.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
ticker = 'ticker_example' # str | 

try:
    # Structure info
    api_response = api_instance.fitting_info(ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->fitting_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

[**FittingInfo**](FittingInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics**
> Statistics get_statistics(ticker, currency=currency)

Statistics

Returns statistics of the strategy; returns, max drawdown and volatility for strategy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
ticker = 'ticker_example' # str | 
currency = 'USD' # str |  (optional) (default to USD)

try:
    # Statistics
    api_response = api_instance.get_statistics(ticker, currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->get_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **currency** | **str**|  | [optional] [default to USD]

### Return type

[**Statistics**](Statistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info**
> Strategy info(ticker)

Strategy details

Returns information about one specific strategy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
ticker = 'ticker_example' # str | Ticker of structure

try:
    # Strategy details
    api_response = api_instance.info(ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Ticker of structure | 

### Return type

[**Strategy**](Strategy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **posts**
> Posts posts(ticker, page_size=page_size, page_number=page_number)

Strategy posts

Returns a list of posts.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
ticker = 'ticker_example' # str | 
page_size = 20 # int |  (optional) (default to 20)
page_number = 0 # int |  (optional) (default to 0)

try:
    # Strategy posts
    api_response = api_instance.posts(ticker, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->posts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **page_size** | **int**|  | [optional] [default to 20]
 **page_number** | **int**|  | [optional] [default to 0]

### Return type

[**Posts**](Posts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **strategy_list**
> list[Strategy] strategy_list(page_size=page_size, page_number=page_number)

List of Strategies

Returns a list of all public Strategies.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
page_size = 1000 # int |  (optional) (default to 1000)
page_number = 0 # int |  (optional) (default to 0)

try:
    # List of Strategies
    api_response = api_instance.strategy_list(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->strategy_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**|  | [optional] [default to 1000]
 **page_number** | **int**|  | [optional] [default to 0]

### Return type

[**list[Strategy]**](Strategy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **structure**
> Structure structure(ticker, currency=currency)

Structure

Returns the current structure of a strategy. The same result entity is returned  for both PASSIVE and ACTIVE type DAAs, but for ACTIVE DAAs rebalancedWeight  and targetWeight are always set to 0.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
ticker = 'ticker_example' # str | 
currency = 'USD' # str |  (optional) (default to USD)

try:
    # Structure
    api_response = api_instance.structure(ticker, currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->structure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **currency** | **str**|  | [optional] [default to USD]

### Return type

[**Structure**](Structure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_structure**
> Structure submit_structure(ticker, body=body)

Structure

Endpoint requires authentication. Creates and submits a new structure for a given strategy.   Response is the same object as GET to /v1/strategies/{ticker}/structure.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['ICN-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ICN-API-KEY'] = 'Bearer'
# Configure API key authorization: ApiSign
configuration = swagger_client.Configuration()
configuration.api_key['ICN-SIGN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ICN-SIGN'] = 'Bearer'
# Configure API key authorization: ApiTimestamp
configuration = swagger_client.Configuration()
configuration.api_key['ICN-TIMESTAMP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ICN-TIMESTAMP'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StrategiesApi(swagger_client.ApiClient(configuration))
ticker = 'ticker_example' # str | 
body = swagger_client.StructureSubmit() # StructureSubmit |  (optional)

try:
    # Structure
    api_response = api_instance.submit_structure(ticker, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->submit_structure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **body** | [**StructureSubmit**](StructureSubmit.md)|  | [optional] 

### Return type

[**Structure**](Structure.md)

### Authorization

[ApiKey](../README.md#ApiKey), [ApiSign](../README.md#ApiSign), [ApiTimestamp](../README.md#ApiTimestamp)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

