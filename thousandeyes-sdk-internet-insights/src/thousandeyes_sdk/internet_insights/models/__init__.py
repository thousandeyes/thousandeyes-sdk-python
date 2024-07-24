# coding: utf-8

# flake8: noqa
"""
    Internet Insights API

    We are happy to announce the release of the Internet Insights API set. This limited release includes endpoints that:  * Make our catalog provider and Internet outage data accessible to API users. * Provide access to advanced filtering, which is part of our next-generation API efforts to allow API users to fine-tune queries across all of our APIs in a consistent manner.  Internet Insights provide visibility into core Internet infrastructure, including ISPs, DNS providers, IaaS, CDNs , and SaaS providers. It tracks the macro-level impact of Internet events on individual users and enterprise networks connecting at the edge of the Internet. These events include Outages, Routing hijacks and leaks, DDoS attacks, And political interference, among others.  Future releases of the Internet Insights API set will further unlock access to core Internet Insights functionality, unlocking potential integrations to enrich customer process flows.  For more information about Internet Insights, see the [Internet Insights](https://docs.thousandeyes.com/product-documentation/internet-insights). 

    The version of the OpenAPI document: 7.0.10
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from thousandeyes_sdk.internet_insights.models.api_affected_agent import ApiAffectedAgent
from thousandeyes_sdk.internet_insights.models.api_affected_test import ApiAffectedTest
from thousandeyes_sdk.internet_insights.models.api_application_outage_affected_location import ApiApplicationOutageAffectedLocation
from thousandeyes_sdk.internet_insights.models.api_application_outage_affected_server import ApiApplicationOutageAffectedServer
from thousandeyes_sdk.internet_insights.models.api_application_outage_details import ApiApplicationOutageDetails
from thousandeyes_sdk.internet_insights.models.api_asn import ApiAsn
from thousandeyes_sdk.internet_insights.models.api_catalog_provider import ApiCatalogProvider
from thousandeyes_sdk.internet_insights.models.api_catalog_provider_details import ApiCatalogProviderDetails
from thousandeyes_sdk.internet_insights.models.api_catalog_provider_filter import ApiCatalogProviderFilter
from thousandeyes_sdk.internet_insights.models.api_catalog_provider_response import ApiCatalogProviderResponse
from thousandeyes_sdk.internet_insights.models.api_network_outage_affected_location import ApiNetworkOutageAffectedLocation
from thousandeyes_sdk.internet_insights.models.api_network_outage_details import ApiNetworkOutageDetails
from thousandeyes_sdk.internet_insights.models.api_outage import ApiOutage
from thousandeyes_sdk.internet_insights.models.api_outage_filter import ApiOutageFilter
from thousandeyes_sdk.internet_insights.models.api_outages_response import ApiOutagesResponse
from thousandeyes_sdk.internet_insights.models.error import Error
from thousandeyes_sdk.internet_insights.models.link import Link
from thousandeyes_sdk.internet_insights.models.outage_scope import OutageScope
from thousandeyes_sdk.internet_insights.models.provider_location import ProviderLocation
from thousandeyes_sdk.internet_insights.models.self_links import SelfLinks
from thousandeyes_sdk.internet_insights.models.unauthorized_error import UnauthorizedError
from thousandeyes_sdk.internet_insights.models.validation_error import ValidationError
from thousandeyes_sdk.internet_insights.models.validation_error_item import ValidationErrorItem
