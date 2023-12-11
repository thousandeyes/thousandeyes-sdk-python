# PutStream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_headers** | **Dict[str, str]** | Custom headers | [optional] 
**tag_match** | [**List[PutStreamTagMatchInner]**](PutStreamTagMatchInner.md) | A collection of tags that determine what tests are included in the data stream. These tag values are also included as attributes in the data stream metrics. | [optional] 
**enabled** | **bool** | Flag to enable or disable the stream integration. | [optional] 

## Example

```python
from streaming_api.models.put_stream import PutStream

# TODO update the JSON string below
json = "{}"
# create an instance of PutStream from a JSON string
put_stream_instance = PutStream.from_json(json)
# print the JSON string representation of the object
print PutStream.to_json()

# convert the object into a dict
put_stream_dict = put_stream_instance.to_dict()
# create an instance of PutStream from a dict
put_stream_form_dict = put_stream.from_dict(put_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


