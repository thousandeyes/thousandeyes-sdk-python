# SslCert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_until_expiry** | **int** | Days until certificate expires, rounded down. 0 is shown if there are less than 24 hours remaining. Calculated when the test was executed. | [optional] 
**is_fetch_date_in_valid_cert_date_range** | **bool** | True when certificate fetch date is within the valid certificate date range, false otherwise | [optional] 
**has_valid_signing_cert** | **bool** | This field is implicitly true; it is output only when false. false indicates this certificate was missing a valid signing certificate in the chain. | [optional] 
**issuer_name** | **str** | Certificate issuer | [optional] 
**valid_before** | **datetime** | Certificate is not valid after this date | [optional] 
**valid_after** | **datetime** | Certificate is not valid before this date | [optional] 
**subject_alternative_names** | **List[str]** | Alternative name(s) of the certificate subject, extracted from the Subject Alternative Name (SAN) X.509 certificate extension, for example example.com, www2.example.com | [optional] 
**subject_name** | **str** | certificate’s subject name - a value of the common name (CN) RDN from the certificate’s Subject attribute, for example www.example.com | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.ssl_cert import SslCert

# TODO update the JSON string below
json = "{}"
# create an instance of SslCert from a JSON string
ssl_cert_instance = SslCert.from_json(json)
# print the JSON string representation of the object
print(SslCert.to_json())

# convert the object into a dict
ssl_cert_dict = ssl_cert_instance.to_dict()
# create an instance of SslCert from a dict
ssl_cert_from_dict = SslCert.from_dict(ssl_cert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


