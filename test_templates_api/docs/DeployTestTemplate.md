# DeployTestTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_input_values** | [**DeployTestTemplateUserInputValues**](DeployTestTemplateUserInputValues.md) |  | [optional] 
**name** | **str** |  | [optional] 
**tests** | [**DeployTestTemplateTests**](DeployTestTemplateTests.md) |  | [optional] 

## Example

```python
from test_templates_api.models.deploy_test_template import DeployTestTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of DeployTestTemplate from a JSON string
deploy_test_template_instance = DeployTestTemplate.from_json(json)
# print the JSON string representation of the object
print DeployTestTemplate.to_json()

# convert the object into a dict
deploy_test_template_dict = deploy_test_template_instance.to_dict()
# create an instance of DeployTestTemplate from a dict
deploy_test_template_form_dict = deploy_test_template.from_dict(deploy_test_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


