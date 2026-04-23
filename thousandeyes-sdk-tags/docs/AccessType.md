# AccessType

 The access level of the tag. The access level determines the label's visibility in the UI and the permissions required to modify it. Accepted values are:   * `all`: The tag is visible and editable by any user in the account group with the standard **View tags** or **Edit tags** permission. Default for all user-created tags.  * `partner`: The tag is owned by a specific integration partner. Only that partner can read or modify it. It's hidden from all regular account users and excluded from their GET responses.  * `system`: Reserved for ThousandEyes internal use only. This value may appear in GET responses on internally managed tags but cannot be set by users or integration partners.  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


