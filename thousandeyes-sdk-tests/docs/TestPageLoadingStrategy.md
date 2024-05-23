# TestPageLoadingStrategy

* `normal`: The test waits until the entire page is fully loaded, including the downloading and parsing of HTML content as well as all associated resources, before advancing to the next action in the transaction test script.  * `eager`: The test waits for the DOMContentLoaded event, indicating that HTML content is downloaded and parsed, and the document reaches the \"interactive\" readiness state, before proceeding to the next action in the test script. * `none`: The test only waits for the download of HTML content. Once the HTML is downloaded, the test continues to the next action in the transaction test script without waiting for additional resources. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


