# DeployTestTemplateUserInputValues


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **int** |  | [optional] 
**target** | **str** |  | [optional] 
**agents** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 

## Example

```python
from test_templates_api.models.deploy_test_template_user_input_values import DeployTestTemplateUserInputValues

# TODO update the JSON string below
json = "{}"
# create an instance of DeployTestTemplateUserInputValues from a JSON string
deploy_test_template_user_input_values_instance = DeployTestTemplateUserInputValues.from_json(json)
# print the JSON string representation of the object
print DeployTestTemplateUserInputValues.to_json()

# convert the object into a dict
deploy_test_template_user_input_values_dict = deploy_test_template_user_input_values_instance.to_dict()
# create an instance of DeployTestTemplateUserInputValues from a dict
deploy_test_template_user_input_values_form_dict = deploy_test_template_user_input_values.from_dict(deploy_test_template_user_input_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


