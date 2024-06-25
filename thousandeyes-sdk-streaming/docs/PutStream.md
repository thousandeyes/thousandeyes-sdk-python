# PutStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_headers** | **Dict[str, str]** | Custom headers. **Note**: When using the &#x60;splunk-hec&#x60; &#x60;type&#x60;, the &#x60;customHeaders&#x60; must contain just one element with the key &#x60;token&#x60; and the value of the *Splunk HEC Token*. | [optional] 
**tag_match** | [**List[TagMatch]**](TagMatch.md) | A collection of tags that determine what tests are included in the data stream. These tag values are also included as attributes in the data stream metrics. | [optional] 
**test_match** | [**List[TestMatch]**](TestMatch.md) | A collection of tests to be included in the data stream. | [optional] 
**enabled** | **bool** | Flag to enable or disable the stream integration. | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.put_stream import PutStream

# TODO update the JSON string below
json = "{}"
# create an instance of PutStream from a JSON string
put_stream_instance = PutStream.from_json(json)
# print the JSON string representation of the object
print(PutStream.to_json())

# convert the object into a dict
put_stream_dict = put_stream_instance.to_dict()
# create an instance of PutStream from a dict
put_stream_from_dict = PutStream.from_dict(put_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


