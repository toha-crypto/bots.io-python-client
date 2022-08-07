# swagger_client.AssetApi

All URIs are relative to *https://api.iconomi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_details**](AssetApi.md#asset_details) | **GET** /v1/assets/{ticker} | Asset details
[**asset_history**](AssetApi.md#asset_history) | **GET** /v1/assets/{ticker}/pricehistory | Historical information
[**asset_list**](AssetApi.md#asset_list) | **GET** /v1/assets | List of Assets
[**asset_statistics**](AssetApi.md#asset_statistics) | **GET** /v1/assets/{ticker}/statistics | Statistics
[**asset_ticker**](AssetApi.md#asset_ticker) | **GET** /v1/assets/{ticker}/price | Current ticker

# **asset_details**
> AssetInfo asset_details(ticker)

Asset details

Returns information about one specific Asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
ticker = 'ticker_example' # str | 

try:
    # Asset details
    api_response = api_instance.asset_details(ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->asset_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

[**AssetInfo**](AssetInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_history**
> Chart asset_history(ticker, currency=currency, _from=_from, to=to, granulation=granulation)

Historical information

The price history returns data points for the given period. Different granulation of data can be returned based on the length of the period provided from daily to 5 minute (one  price point per period).  From and to are optional parameters (both are either supplied or neither is supplied). If from/to are not supplied a default of last month is returned with hourly granulation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **currency** | **str**|  | [optional] [default to USD]
 **_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **granulation** | **str**|  | [optional] 

### Return type

[**Chart**](Chart.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_list**
> list[Asset] asset_list()

List of Assets

Returns a list of all assets on platform.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()

try:
    # List of Assets
    api_response = api_instance.asset_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->asset_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Asset]**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_statistics**
> Statistics asset_statistics(ticker, currency=currency)

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
api_instance = swagger_client.AssetApi()
ticker = 'ticker_example' # str | 
currency = 'USD' # str |  (optional) (default to USD)

try:
    # Statistics
    api_response = api_instance.asset_statistics(ticker, currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->asset_statistics: %s\n" % e)
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

# **asset_ticker**
> Ticker asset_ticker(ticker, currency=currency)

Current ticker

Returns the current ticker of the Asset. The price is refreshed every minute.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
ticker = 'ticker_example' # str | 
currency = 'USD' # str |  (optional) (default to USD)

try:
    # Current ticker
    api_response = api_instance.asset_ticker(ticker, currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->asset_ticker: %s\n" % e)
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

