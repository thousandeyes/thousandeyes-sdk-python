# TestTemplateCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**templates** | [**List[TestTemplate]**](TestTemplate.md) |  | [optional] 
**links** | [**TestTemplateCollectionLinks**](TestTemplateCollectionLinks.md) |  | [optional] 

## Example

```python
from test_templates_api.models.test_template_collection import TestTemplateCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TestTemplateCollection from a JSON string
test_template_collection_instance = TestTemplateCollection.from_json(json)
# print the JSON string representation of the object
print TestTemplateCollection.to_json()

# convert the object into a dict
test_template_collection_dict = test_template_collection_instance.to_dict()
# create an instance of TestTemplateCollection from a dict
test_template_collection_form_dict = test_template_collection.from_dict(test_template_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


