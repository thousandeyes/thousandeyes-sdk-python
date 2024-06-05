# AccountGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_group_name** | **str** | The name of the account group | 
**agents** | **List[str]** | To grant access to enterprise agents, specify the agent list. Note that this is not an additive list - the full list must be specified if changing access to agents. | [optional] 

## Example

```python
from thousandeyes_sdk.administrative.models.account_group_request import AccountGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGroupRequest from a JSON string
account_group_request_instance = AccountGroupRequest.from_json(json)
# print the JSON string representation of the object
print(AccountGroupRequest.to_json())

# convert the object into a dict
account_group_request_dict = account_group_request_instance.to_dict()
# create an instance of AccountGroupRequest from a dict
account_group_request_from_dict = AccountGroupRequest.from_dict(account_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


