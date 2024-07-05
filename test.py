import thousandeyes_sdk.core
import thousandeyes_sdk.usage
from thousandeyes_sdk.core.exceptions import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = thousandeyes_sdk.core.Configuration(
    access_token='8b919a53-6977-4d19-92a7-3615a20836b2',
    host='https://api.stg.thousandeyes.com'
)


# Enter a context with an instance of the API client
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.usage.UsageApi(api_client)

    try:
        # Create or update accout group quotas
        api_response = api_instance.get_usage(aid="85486")
        print("The response of UsageApi->assign_organizations_account_groups_quotas:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QuotasApi->assign_organizations_account_groups_quotas: %s\n" % e)
