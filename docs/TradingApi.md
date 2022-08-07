# swagger_client.TradingApi

All URIs are relative to *https://api.iconomi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](TradingApi.md#cancel_order) | **DELETE** /v1/order/{orderId} | Delete
[**confirm_offer**](TradingApi.md#confirm_offer) | **POST** /v1/order/offer/{offerId}/confirm | Confirm trade offer
[**get_all_orders**](TradingApi.md#get_all_orders) | **GET** /v1/order/orders | List of orders
[**order_offer**](TradingApi.md#order_offer) | **POST** /v1/order/offer | Trade offer
[**order_trade**](TradingApi.md#order_trade) | **POST** /v1/order | Place order
[**status**](TradingApi.md#status) | **GET** /v1/order/{orderId} | Logical order

# **cancel_order**
> OrderInfo cancel_order(order_id)

Delete

Remove user's logical order.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradingApi()
order_id = 'order_id_example' # str | 

try:
    # Delete
    api_response = api_instance.cancel_order(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradingApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 

### Return type

[**OrderInfo**](OrderInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_offer**
> TradeConfirm confirm_offer(offer_id)

Confirm trade offer

This endpoint confirms generated trade offer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradingApi()
offer_id = 'offer_id_example' # str | 

try:
    # Confirm trade offer
    api_response = api_instance.confirm_offer(offer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradingApi->confirm_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**|  | 

### Return type

[**TradeConfirm**](TradeConfirm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_orders**
> list[OrderInfo] get_all_orders(status=status, page_size=page_size, page_number=page_number)

List of orders

Returns a list of all user's logical orders.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradingApi()
status = 'status_example' # str |  (optional)
page_size = 20 # int |  (optional) (default to 20)
page_number = 0 # int |  (optional) (default to 0)

try:
    # List of orders
    api_response = api_instance.get_all_orders(status=status, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradingApi->get_all_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] [default to 20]
 **page_number** | **int**|  | [optional] [default to 0]

### Return type

[**list[OrderInfo]**](OrderInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_offer**
> TradeOffer order_offer(body=body)

Trade offer

Generating trade offer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradingApi()
body = swagger_client.OrderOffer() # OrderOffer |  (optional)

try:
    # Trade offer
    api_response = api_instance.order_offer(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradingApi->order_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderOffer**](OrderOffer.md)|  | [optional] 

### Return type

[**TradeOffer**](TradeOffer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_trade**
> OrderInfo order_trade(body=body)

Place order

Placing user's logical order.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradingApi()
body = swagger_client.Order() # Order |  (optional)

try:
    # Place order
    api_response = api_instance.order_trade(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradingApi->order_trade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Order**](Order.md)|  | [optional] 

### Return type

[**OrderInfo**](OrderInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> OrderInfo status(order_id)

Logical order

Returns a user's logical order.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradingApi()
order_id = 'order_id_example' # str | 

try:
    # Logical order
    api_response = api_instance.status(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradingApi->status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 

### Return type

[**OrderInfo**](OrderInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

