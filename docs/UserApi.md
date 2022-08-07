# swagger_client.UserApi

All URIs are relative to *https://api.iconomi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_activities**](UserApi.md#get_activities) | **GET** /v1/user/activity | Activity
[**get_deposit_address**](UserApi.md#get_deposit_address) | **GET** /v1/user/deposit/{currency} | Deposit
[**get_user_balance**](UserApi.md#get_user_balance) | **GET** /v1/user/balance | User Balance
[**portfolio_history**](UserApi.md#portfolio_history) | **POST** /v1/user/portfoliohistory | Portfolio value history
[**transaction_info**](UserApi.md#transaction_info) | **GET** /v1/user/transaction/{transactionId} | Transaction
[**withdraw**](UserApi.md#withdraw) | **POST** /v1/user/withdraw | Withdraw

# **get_activities**
> Activity get_activities(type=type, page_size=page_size, page_number=page_number)

Activity

Endpoint returns user's activity (buy, sell, deposit, withdraw).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
type = 'MY_ACTIVITIES' # str |  (optional) (default to MY_ACTIVITIES)
page_size = 25 # int |  (optional) (default to 25)
page_number = 0 # int |  (optional) (default to 0)

try:
    # Activity
    api_response = api_instance.get_activities(type=type, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] [default to MY_ACTIVITIES]
 **page_size** | **int**|  | [optional] [default to 25]
 **page_number** | **int**|  | [optional] [default to 0]

### Return type

[**Activity**](Activity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deposit_address**
> Deposit get_deposit_address(currency)

Deposit

Endpoint returns user's crypto address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
currency = 'currency_example' # str | 

try:
    # Deposit
    api_response = api_instance.get_deposit_address(currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_deposit_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**|  | 

### Return type

[**Deposit**](Deposit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_balance**
> Balance get_user_balance(currency=currency)

User Balance

Endpoint requires authentication. Returns the balance based on the authentication of the user.   There is an optional query parameter currency that changes the resulting fiat value calculation to chosen currency. Possibly values are EUR or USD.  ##### Request  Empty body.  ##### Response  | Parameter  | Description   | Sample  | |---|---|---| | **currency** <br> *String*        |   Currency in which the values are returned | USD  | | **daaList** <br> *BalanceEntry*     | Array of portfolios balances   |   | | **assetList** <br> *BalanceEntry*     | Array of cryptocurrency balances  |   |  BalanceEntry is of the following structure:  | Parameter  | Description   | Sample  | | ---|---|---| | **name** <br> _String_ | Name of asset | Blockchain index  | | **ticker** <br> _String_  | Ticker of asset  | BLX  | | **balance** <br> _String_  | Balance of the asset  | 1337  | | **value** <br> _String_  | Value in USD or EUR (depending on the optional currency in query string)  | 4700  |

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
currency = 'USD' # str |  (optional) (default to USD)

try:
    # User Balance
    api_response = api_instance.get_user_balance(currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**|  | [optional] [default to USD]

### Return type

[**Balance**](Balance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_history**
> PortfolioHistory portfolio_history(currency=currency, period=period)

Portfolio value history

Get the history of the value of the users portfolio.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
currency = 'USD' # str |  (optional) (default to USD)
period = 'ONE_WEEK' # str |  (optional) (default to ONE_WEEK)

try:
    # Portfolio value history
    api_response = api_instance.portfolio_history(currency=currency, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->portfolio_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**|  | [optional] [default to USD]
 **period** | **str**|  | [optional] [default to ONE_WEEK]

### Return type

[**PortfolioHistory**](PortfolioHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_info**
> Transaction transaction_info(transaction_id)

Transaction

Endpoint returns details about user's transaction.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
transaction_id = 'transaction_id_example' # str | 

try:
    # Transaction
    api_response = api_instance.transaction_info(transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->transaction_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw**
> Transaction withdraw(body=body)

Withdraw

Endpoint allows to make withdraw asset from user's account to recipient's address. Recipient's address must be whitelisted at ICONOMI platform.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
body = swagger_client.Withdraw() # Withdraw |  (optional)

try:
    # Withdraw
    api_response = api_instance.withdraw(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->withdraw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Withdraw**](Withdraw.md)|  | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

