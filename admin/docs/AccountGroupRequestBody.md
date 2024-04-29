# AccountGroupRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_group_name** | **str** | The name of the account group | 
**agents** | **List[str]** | To grant access to enterprise agents, specify the agent list. Note that this is not an additive list - the full list must be specified if changing access to agents. | [optional] 

## Example

```python
from admin.models.account_group_request_body import AccountGroupRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGroupRequestBody from a JSON string
account_group_request_body_instance = AccountGroupRequestBody.from_json(json)
# print the JSON string representation of the object
print(AccountGroupRequestBody.to_json())

# convert the object into a dict
account_group_request_body_dict = account_group_request_body_instance.to_dict()
# create an instance of AccountGroupRequestBody from a dict
account_group_request_body_from_dict = AccountGroupRequestBody.from_dict(account_group_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


