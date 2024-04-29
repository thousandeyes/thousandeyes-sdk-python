# coding: utf-8

"""
    OAuth2 API

    This endpoint allows clients to trade their client credentials for an Access Token that can be used on subsequent calls to our API. Example of usage:    `   curl -X POST -H \"Content-Type: application/x-www-form-urlencoded\" -d 'client_id=someId&scope=someScope&client_secret=someSecret&grant_type=client_credentials' 'https://api.thousandeyes.com/v7/oauth2/token'   `

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "oauth2"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="OAuth2 API",
    author="ThousandEyes API Team",
    author_email="api-team@thousandeyes.com",
    url="https://github.com/thousandeyes/thousandeyes-sdk-python/oauth2",
    keywords=["OpenAPI", "OpenAPI-Generator", "ThousandEyes", "OAuth2 API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    This endpoint allows clients to trade their client credentials for an Access Token that can be used on subsequent calls to our API. Example of usage:    &#x60;   curl -X POST -H \&quot;Content-Type: application/x-www-form-urlencoded\&quot; -d &#39;client_id&#x3D;someId&amp;scope&#x3D;someScope&amp;client_secret&#x3D;someSecret&amp;grant_type&#x3D;client_credentials&#39; &#39;https://api.thousandeyes.com/v7/oauth2/token&#39;   &#x60;
    """,  # noqa: E501
    package_data={"oauth2": ["py.typed"]},
)