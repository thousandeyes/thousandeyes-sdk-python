# TestTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the test template. | [optional] 
**name** | **str** | The name of the test template. | [optional] 
**description** | **str** | Text that describes the test template. | [optional] 
**icon** | **str** | Icon for the test template; will be displayed in the UI. | [optional] 
**is_built_in** | **bool** | Indicates whether the test template is a built-in template. Note that built-in test templates are read-only. | [optional] 
**certification_level** | **str** |  | [optional] 
**date_created** | **str** | The date and time the test template was created. | [optional] 
**user_inputs** | [**Dict[str, UserInput]**](UserInput.md) |  | [optional] 
**labels** | **object** | A map of &lt;labelKey, labelConfiguration&gt;. | [optional] 
**tests** | **object** | A map of &lt;testKey, testConfiguration&gt;. | [optional] 
**alert_rules** | **object** | A map of &lt;alertRuleKey, alertRuleConfiguration&gt;. | [optional] 
**dashboards** | **object** | A map of &lt;dashboardKey, dashboardConfiguration&gt;. | [optional] 
**deployment_strategy** | [**Dict[str, DeploymentStrategy]**](DeploymentStrategy.md) | A map of &lt;assetKey, deploymentStrategy&gt;. | [optional] 
**links** | [**Dict[str, Link]**](Link.md) |  | [optional] 

## Example

```python
from test_templates_api.models.test_template import TestTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of TestTemplate from a JSON string
test_template_instance = TestTemplate.from_json(json)
# print the JSON string representation of the object
print TestTemplate.to_json()

# convert the object into a dict
test_template_dict = test_template_instance.to_dict()
# create an instance of TestTemplate from a dict
test_template_form_dict = test_template.from_dict(test_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


