# Page


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_num** | **int** | Page index | [optional] [readonly] 
**page_name** | **str** | Meta title value for page visited | [optional] [readonly] 
**component_count** | **int** | Number of components on target page | [optional] [readonly] 
**error_count** | **int** | Number of errors encountered during page load | [optional] [readonly] 
**duration** | **float** | Time spent on page in milliseconds | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.page import Page

# TODO update the JSON string below
json = "{}"
# create an instance of Page from a JSON string
page_instance = Page.from_json(json)
# print the JSON string representation of the object
print(Page.to_json())

# convert the object into a dict
page_dict = page_instance.to_dict()
# create an instance of Page from a dict
page_from_dict = Page.from_dict(page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


