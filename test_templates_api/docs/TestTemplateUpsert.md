# TestTemplateUpsert

The test template to create or update.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the test template. | 
**description** | **str** | Text that describes the test template. | [optional] 
**icon** | **str** | Icon for the test template; will be displayed in the UI. | [optional] 
**is_built_in** | **bool** | Indicates whether the test template is a built-in template. Note that built-in test templates are read-only. | [optional] 
**user_inputs** | [**Dict[str, UserInput]**](UserInput.md) |  | [optional] 
**labels** | **object** | A map of &lt;labelKey, labelConfiguration&gt;. | [optional] 
**tests** | **object** | A map of &lt;testKey, testConfiguration&gt;. | [optional] 
**alert_rules** | **object** | A map of &lt;alertRuleKey, alertRuleConfiguration&gt;. | [optional] 
**dashboards** | **object** | A map of &lt;dashboardKey, dashboardConfiguration&gt;. | [optional] 
**deployment_strategy** | [**Dict[str, DeploymentStrategy]**](DeploymentStrategy.md) | A map of &lt;assetKey, deploymentStrategy&gt;. | [optional] 

## Example

```python
from test_templates_api.models.test_template_upsert import TestTemplateUpsert

# TODO update the JSON string below
json = "{}"
# create an instance of TestTemplateUpsert from a JSON string
test_template_upsert_instance = TestTemplateUpsert.from_json(json)
# print the JSON string representation of the object
print TestTemplateUpsert.to_json()

# convert the object into a dict
test_template_upsert_dict = test_template_upsert_instance.to_dict()
# create an instance of TestTemplateUpsert from a dict
test_template_upsert_form_dict = test_template_upsert.from_dict(test_template_upsert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


