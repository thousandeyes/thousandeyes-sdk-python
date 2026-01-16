# thousandeyes-sdk-core

This package provides core functionality for interacting with the ThousandEyes API and should be installed before using any of the published SDKs.

`PaginationIterable` is unbounded, so wrap it with `itertools.islice` to cap the number of items and avoid making unintended, potentially expensive API calls. 
Pick a slice size that matches your UI or batch size so you only fetch what you plan to process:

```python
from thousandeyes_sdk.core import Configuration, ApiClient, PaginationIterable
from thousandeyes_sdk.dashboards import DashboardsApi
from itertools import islice

configuration = Configuration(
    host = "https://api.thousandeyes.com/v7",
    access_token = "an_access_token",
)


def get_dashboard_widget_data():
    with ApiClient(configuration) as client:
        dashboards_api = DashboardsApi(client)
        for item in list(islice(PaginationIterable(
            dashboards_api.get_dashboard_widget_data,
            lambda response: response.data.tests,
            dashboard_id="a_dashboard_id",
            widget_id="a_widget_id",
        ), 20)):
            print(item.test_id)
```
