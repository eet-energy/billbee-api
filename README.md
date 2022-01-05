# Getting Started with Billbee API

## Getting Started

### Introduction

Documentation of the Billbee REST API to connect a Billbee account to external aplications.

#### Endpoint

The Billbee API endpoint base url is https://app.billbee.io/api/v1

#### Activation

You have to enable the API in the settings of your Billbee account. In addition you need a Billbee API Key identifying the application you develop. To get an API key, send a mail to support@billbee.io and send us a short note about what you are building.

#### Authorization & security

Because you can access private data with the Billbee API, every request has to be sent over https and must

* Contain a valid API Key identifying the application/developer. It has to be sent as the HTTP header X-Billbee-Api-Key
* Contain a valid user login with billbee username and api password in form of a basic auth HTTP header

#### Throttling

Each endpoint has a throttle of max 2 requests per second per combination of API Key and Billbee user.

When you exceed these 2 calls, the API will return a HTTP 429 status code

### Install the Package

The package is compatible with Python versions `2 >=2.7.9` and `3 >=3.4`.

Download the wheel file an using the following pip command
```python
pip install billbee_api-1.1.0-py3-none-any.whl
```

#### package note

This is a fork from 
https://pypi.python.org/pypi/billbee-1
which you can install from PyPi using the following pip command.
```python
pip install billbee-api
```
But this package does not support API_KEYs 

### Initialize the API Client

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `basic_auth_user_name` | `string` | The username to use with basic authentication |
| `basic_auth_password` | `string` | The password to use with basic authentication |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 3** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 0** |

The API client can be initialized as follows:

```python
from billbeeapi.billbeeapi_client import BillbeeapiClient
from billbeeapi.configuration import Environment

client = BillbeeapiClient(
    basic_auth_user_name='BasicAuthUserName',
    basic_auth_password='BasicAuthPassword',
    api_key='ApiKey'
    environment = ,)
```

### Authorization

This API uses `Basic Authentication` and the API-KEY in the HTTP header `X-Billbee-Api-Key`

## Client Class Documentation

### Billbee API Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

### Controllers

| Name | Description |
|  --- | --- |
| products | Gets ProductsController |
| provisioning | Gets ProvisioningController |
| cloud_storage | Gets CloudStorageController |
| customers | Gets CustomersController |
| customer_addresses | Gets CustomerAddressesController |
| enum_api | Gets EnumApiController |
| events | Gets EventsController |
| orders | Gets OrdersController |
| shipments | Gets ShipmentsController |
| webhooks | Gets WebhooksController |

## API Reference

### List of APIs

* [Products](#products)
* [Provisioning](#provisioning)
* [Cloud Storage](#cloud-storage)
* [Customers](#customers)
* [Customer Addresses](#customer-addresses)
* [Enum Api](#enum-api)
* [Events](#events)
* [Orders](#orders)
* [Shipments](#shipments)
* [Webhooks](#webhooks)

### Products

#### Overview

##### Get instance

An instance of the `ProductsController` class can be accessed from the API Client.

```
products_controller = client.products
```

#### Article Update Stock

The article is specified by sku. You have to send the absolute value for the current stock

```python
def article_update_stock(self,
                        model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel`](#billbee-interfaces-billbee-api-model-update-stock-api-model) | Body, Required | - |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-update-stock-response-data)

##### Example Usage

```python
model = BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel()

result = products_controller.article_update_stock(model)
```

#### Article Get Reserved Amount

Queries the reserved amount for a single article by id or by sku

```python
def article_get_reserved_amount(self,
                               id,
                               lookup_by=None,
                               stock_id=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Query, Required | The id or the sku of the article to query |
| `lookup_by` | `string` | Query, Optional | Either the value id or the value sku to specify the meaning of the id parameter |
| `stock_id` | `long\|int` | Query, Optional | Optional the stock id if the multi stock feature is enabled |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelGetReservedAmountResponseData`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-get-reserved-amount-response-data)

##### Example Usage

```python
id = 'id0'

result = products_controller.article_get_reserved_amount(id)
```

#### Article Update Stock Multiple

Update the stock qty for multiple articles at once

```python
def article_update_stock_multiple(self,
                                 models)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `models` | [`List of BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel`](#billbee-interfaces-billbee-api-model-update-stock-api-model) | Body, Required | - |

##### Response Type

[`List of RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-update-stock-response-data)

##### Example Usage

```python
models = []

models.append(BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel())

models.append(BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel())


result = products_controller.article_update_stock_multiple(models)
```

#### Article Update Stock Code

Update the stock code of an article

```python
def article_update_stock_code(self,
                             model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`BillbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel`](#billbee-interfaces-billbee-api-model-update-stock-code-api-model) | Body, Required | - |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockCodeResponseData`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-update-stock-code-response-data)

##### Example Usage

```python
model = BillbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel()

result = products_controller.article_update_stock_code(model)
```

#### Article Get Article

Queries a single article by id or by sku

```python
def article_get_article(self,
                       id,
                       lookup_by=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | The id or the sku of the article to query |
| `lookup_by` | `string` | Query, Optional | Either the value id, ean or the value sku to specify the meaning of the id parameter |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-article-api-model)

##### Example Usage

```python
id = 'id0'

result = products_controller.article_get_article(id)
```

#### Article Delete Article

Deletes a product

```python
def article_delete_article(self,
                          id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The id of the Product |

##### Response Type

`object`

##### Example Usage

```python
id = 112

result = products_controller.article_delete_article(id)
```

#### Article Patch Article

Updates one or more fields of a product

```python
def article_patch_article(self,
                         id,
                         model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The id of the Product |
| `model` | `object` | Body, Required | - |

##### Response Type

`object`

##### Example Usage

```python
id = 112
model = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = products_controller.article_patch_article(id, model)
```

#### Article Get List

Get a list of all products

```python
def article_get_list(self,
                    page=None,
                    page_size=None,
                    min_created_at=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | The current page to request starting with 1 |
| `page_size` | `int` | Query, Optional | The pagesize for the result list. Values between 1 and 250 are allowed |
| `min_created_at` | `datetime` | Query, Optional | Optional the oldest create date of the articles to be returned |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiModel`](#rechnungsdruck-web-app-controllers-api-api-paged-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-article-api-model)

##### Example Usage

```python
result = products_controller.article_get_list()
```

#### Article Create Article

Creates a new product

```python
def article_create_article(self,
                          model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`BillbeeInterfacesBillbeeAPIModelArticleApiModel`](#billbee-interfaces-billbee-api-model-article-api-model) | Body, Required | - |

##### Response Type

`object`

##### Example Usage

```python
model = BillbeeInterfacesBillbeeAPIModelArticleApiModel()
model.vat_index = 104
model.price = 72.12
model.vat_1_rate = 42.06
model.vat_2_rate = 167.28
model.mtype = 2
model.is_digital = False
model.is_customizable = False

result = products_controller.article_create_article(model)
```

#### Article Get Custom Fields

Queries a list of all custom fields

```python
def article_get_custom_fields(self,
                             page=None,
                             page_size=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | - |
| `page_size` | `int` | Query, Optional | - |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel`](#rechnungsdruck-web-app-controllers-api-api-paged-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-article-api-custom-field-definition-model)

##### Example Usage

```python
result = products_controller.article_get_custom_fields()
```

#### Article Get Custom Field

Queries a single custom field

```python
def article_get_custom_field(self,
                            id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The id of the custom field to query |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-article-api-custom-field-definition-model)

##### Example Usage

```python
id = 112

result = products_controller.article_get_custom_field(id)
```

#### Article Get Patchable Fields

Returns a list of fields which can be updated with the patch call

```python
def article_get_patchable_fields(self)
```

##### Response Type

`object`

##### Example Usage

```python
result = products_controller.article_get_patchable_fields()
```

#### Article Get Category

GEts a list of all defined categories

```python
def article_get_category(self)
```

##### Response Type

`object`

##### Example Usage

```python
result = products_controller.article_get_category()
```

#### Article Get Images

Returns a list of all images of the product

```python
def article_get_images(self,
                      product_id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `long\|int` | Template, Required | The Id of the product |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-article-image-relation-api-model)

##### Example Usage

```python
product_id = 98

result = products_controller.article_get_images(product_id)
```

#### Article Put Images

Add multiple images to a product or replace the product images by the given images

```python
def article_put_images(self,
                      product_id,
                      models,
                      replace=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `long\|int` | Template, Required | The id of the product |
| `models` | [`List of BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel`](#billbee-interfaces-billbee-api-model-article-image-relation-api-model) | Body, Required | An array of ArticleApiImageModel |
| `replace` | `bool` | Query, Optional | If you pass true, the images will be replaced by the passed images. Otherwise the passed images will be appended to the product. |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-article-image-relation-api-model)

##### Example Usage

```python
product_id = 98
models = []

models.append(BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel())

models.append(BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel())


result = products_controller.article_put_images(product_id, models)
```

#### Article Get Image From Product

Returns a single image by id

```python
def article_get_image_from_product(self,
                                  product_id,
                                  image_id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `long\|int` | Template, Required | The Id of the product |
| `image_id` | `long\|int` | Template, Required | The Id of the image |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-article-image-relation-api-model)

##### Example Usage

```python
product_id = 98
image_id = 126

result = products_controller.article_get_image_from_product(product_id, image_id)
```

#### Article Put Image

Add or update an existing image of a product

```python
def article_put_image(self,
                     product_id,
                     image_id,
                     model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `long\|int` | Template, Required | The product id |
| `image_id` | `long\|int` | Template, Required | The image id. If you pass 0, the image will be added |
| `model` | [`BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel`](#billbee-interfaces-billbee-api-model-article-image-relation-api-model) | Body, Required | The ArticleApiImageModel |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-article-image-relation-api-model)

##### Example Usage

```python
product_id = 98
image_id = 126
model = BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel()

result = products_controller.article_put_image(product_id, image_id, model)
```

#### Article Delete Image From Product

Deletes a single image from a product

```python
def article_delete_image_from_product(self,
                                     product_id,
                                     image_id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `long\|int` | Template, Required | The product id |
| `image_id` | `long\|int` | Template, Required | The image id |

##### Response Type

`object`

##### Example Usage

```python
product_id = 98
image_id = 126

result = products_controller.article_delete_image_from_product(product_id, image_id)
```

#### Article Get Image

Returns a single image by id

```python
def article_get_image(self,
                     image_id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `image_id` | `long\|int` | Template, Required | The Id of the image |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-article-image-relation-api-model)

##### Example Usage

```python
image_id = 126

result = products_controller.article_get_image(image_id)
```

#### Article Delete Image

Deletes a single image by id

```python
def article_delete_image(self,
                        image_id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `image_id` | `long\|int` | Template, Required | The image id |

##### Response Type

`object`

##### Example Usage

```python
image_id = 126

result = products_controller.article_delete_image(image_id)
```

#### Article Delete Images

Delete multiple images by id

```python
def article_delete_images(self,
                         image_ids)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `image_ids` | `List of long\|int` | Body, Required | - |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelDeletedImagesModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-deleted-images-model)

##### Example Usage

```python
image_ids = [87, 88, 89]

result = products_controller.article_delete_images(image_ids)
```

#### Search Search

Search for products, customers and orders.
Type can be "order", "product" and / or "customer"
Term can contains lucene query syntax

```python
def search_search(self,
                 model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`RechnungsdruckWebAppControllersApiSearchControllerSearchModel`](#rechnungsdruck-web-app-controllers-api-search-controller-search-model) | Body, Required | - |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel`](#rechnungsdruck-web-app-controllers-api-api-result-rechnungsdruck-web-app-controllers-api-search-controller-search-results-model)

##### Example Usage

```python
model = RechnungsdruckWebAppControllersApiSearchControllerSearchModel()

result = products_controller.search_search(model)
```

### Provisioning

#### Overview

##### Get instance

An instance of the `ProvisioningController` class can be accessed from the API Client.

```
provisioning_controller = client.provisioning
```

#### Automatic Provisioning Create Account

Creates a new Billbee user account with the data passed

```python
def automatic_provisioning_create_account(self,
                                         model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer`](#rechnungsdruck-web-app-controllers-api-automatic-provisioning-controller-create-account-container) | Body, Required | - |

##### Response Type

`object`

##### Example Usage

```python
model = RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer()
model.e_mail = 'EMail2'

result = provisioning_controller.automatic_provisioning_create_account(model)
```

#### Automatic Provisioning Terms Info

Returns infos about Billbee terms and conditions

```python
def automatic_provisioning_terms_info(self)
```

##### Response Type

`object`

##### Example Usage

```python
result = provisioning_controller.automatic_provisioning_terms_info()
```

### Cloud Storage

#### Overview

##### Get instance

An instance of the `CloudStorageController` class can be accessed from the API Client.

```
cloud_storage_controller = client.cloud_storage
```

#### Cloud Storage Api Get List

Gets a list of all connected cloud storage devices

```python
def cloud_storage_api_get_list(self)
```

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCloudStorageApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-cloud-storage-api-model)

##### Example Usage

```python
result = cloud_storage_controller.cloud_storage_api_get_list()
```

### Customers

#### Overview

##### Get instance

An instance of the `CustomersController` class can be accessed from the API Client.

```
customers_controller = client.customers
```

#### Customer Get All

Get a list of all customers

```python
def customer_get_all(self,
                    page=None,
                    page_size=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | The current page to request starting with 1 |
| `page_size` | `int` | Query, Optional | The pagesize for the result list. Values between 1 and 250 are allowed |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel`](#rechnungsdruck-web-app-controllers-api-api-paged-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-customer-api-model)

##### Example Usage

```python
result = customers_controller.customer_get_all()
```

#### Customer Create

Creates a new customer

```python
def customer_create(self,
                   model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel`](#billbee-interfaces-billbee-api-model-create-customer-api-model) | Body, Required | - |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-customer-api-model)

##### Example Usage

```python
model = BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel()

result = customers_controller.customer_create(model)
```

#### Customer Get One

Queries a single customer by id

```python
def customer_get_one(self,
                    id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The id of the customer to query |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-customer-api-model)

##### Example Usage

```python
id = 112

result = customers_controller.customer_get_one(id)
```

#### Customer Update

Updates a customer by id

```python
def customer_update(self,
                   model,
                   id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`BillbeeInterfacesBillbeeAPIModelCustomerApiModel`](#billbee-interfaces-billbee-api-model-customer-api-model) | Body, Required | - |
| `id` | `long\|int` | Template, Required | The id of the customer |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-customer-api-model)

##### Example Usage

```python
model = BillbeeInterfacesBillbeeAPIModelCustomerApiModel()
id = 112

result = customers_controller.customer_update(model, id)
```

#### Customer Get Customer Orders

Queries a list of orders from a customer

```python
def customer_get_customer_orders(self,
                                id,
                                page=None,
                                page_size=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The id of the customer |
| `page` | `int` | Query, Optional | The current page to request starting with 1 |
| `page_size` | `int` | Query, Optional | The pagesize for the result list. Values between 1 and 250 are allowed |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListRechnungsdruckWebAppControllersApiOrder`](#rechnungsdruck-web-app-controllers-api-api-paged-result-system-collections-generic-list-rechnungsdruck-web-app-controllers-api-order)

##### Example Usage

```python
id = 112

result = customers_controller.customer_get_customer_orders(id)
```

#### Customer Get Customer Addresses

Queries a list of addresses from a customer

```python
def customer_get_customer_addresses(self,
                                   id,
                                   page=None,
                                   page_size=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The id of the customer |
| `page` | `int` | Query, Optional | The current page to request starting with 1 |
| `page_size` | `int` | Query, Optional | The pagesize for the result list. Values between 1 and 250 are allowed |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#rechnungsdruck-web-app-controllers-api-api-paged-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-customer-address-api-model)

##### Example Usage

```python
id = 112

result = customers_controller.customer_get_customer_addresses(id)
```

#### Customer Add Customer Address

Id and  CustomerId will be ignored in model. If Id is set, the addition will be stopped.

```python
def customer_add_customer_address(self,
                                 id,
                                 model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | CustomerId to attach the new address to. |
| `model` | [`BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#billbee-interfaces-billbee-api-model-customer-address-api-model) | Body, Required | Model containing the address, that should be attached. |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-customer-address-api-model)

##### Example Usage

```python
id = 112
model = BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel()

result = customers_controller.customer_add_customer_address(id, model)
```

#### Customer Get Customer Address

Queries a single address from a customer

```python
def customer_get_customer_address(self,
                                 id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The id of the address |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-customer-address-api-model)

##### Example Usage

```python
id = 112

result = customers_controller.customer_get_customer_address(id)
```

#### Customer Update Address

Id and CustomerId cannot be changed. Fields you do not send will become empty.

```python
def customer_update_address(self,
                           model,
                           id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#billbee-interfaces-billbee-api-model-customer-address-api-model) | Body, Required | The updated address. Please query an address via (todo) to see all fields. Note that Id and CustomerId cannot be changed. |
| `id` | `long\|int` | Template, Required | The id of the address |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-customer-address-api-model)

##### Example Usage

```python
model = BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel()
id = 112

result = customers_controller.customer_update_address(model, id)
```

#### Customer Patch Address

Id and CustomerId cannot be changed

```python
def customer_patch_address(self,
                          id,
                          model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The id of the address |
| `model` | `object` | Body, Required | The address fields to be changed. Please query an address via (todo) to see all fields. Note that Id and CustomerId cannot be changed. |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-customer-address-api-model)

##### Example Usage

```python
id = 112
model = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = customers_controller.customer_patch_address(id, model)
```

### Customer Addresses

#### Overview

##### Get instance

An instance of the `CustomerAddressesController` class can be accessed from the API Client.

```
customer_addresses_controller = client.customer_addresses
```

#### Customer Addresses Get All

Get a list of all customer addresses

```python
def customer_addresses_get_all(self,
                              page=None,
                              page_size=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | The current page to request starting with 1 (default is 1) |
| `page_size` | `int` | Query, Optional | The page size for the result list. Values between 1 and 250 are allowed. (default is 50) |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#rechnungsdruck-web-app-controllers-api-api-paged-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-customer-address-api-model)

##### Example Usage

```python
result = customer_addresses_controller.customer_addresses_get_all()
```

#### Customer Addresses Create

Creates a new customer address

```python
def customer_addresses_create(self,
                             model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#billbee-interfaces-billbee-api-model-customer-address-api-model) | Body, Required | - |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-customer-address-api-model)

##### Example Usage

```python
model = BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel()

result = customer_addresses_controller.customer_addresses_create(model)
```

#### Customer Addresses Get One

Queries a single customer address by id

```python
def customer_addresses_get_one(self,
                              id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The id of the address to query |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-customer-address-api-model)

##### Example Usage

```python
id = 112

result = customer_addresses_controller.customer_addresses_get_one(id)
```

#### Customer Addresses Update

Updates a customer address by id

```python
def customer_addresses_update(self,
                             model,
                             id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#billbee-interfaces-billbee-api-model-customer-address-api-model) | Body, Required | - |
| `id` | `long\|int` | Template, Required | The id of the address |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-customer-address-api-model)

##### Example Usage

```python
model = BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel()
id = 112

result = customer_addresses_controller.customer_addresses_update(model, id)
```

### Enum Api

#### Overview

##### Get instance

An instance of the `EnumApiController` class can be accessed from the API Client.

```
enum_api_controller = client.enum_api
```

#### Enum Api Get Payment Types

Returns a list with all defined paymenttypes

```python
def enum_api_get_payment_types(self)
```

##### Response Type

`object`

##### Example Usage

```python
result = enum_api_controller.enum_api_get_payment_types()
```

#### Enum Api Get Shipping Carriers

Returns a list with all defined shippingcarriers

```python
def enum_api_get_shipping_carriers(self)
```

##### Response Type

`object`

##### Example Usage

```python
result = enum_api_controller.enum_api_get_shipping_carriers()
```

#### Enum Api Get Order States

Returns a list with all defined orderstates

```python
def enum_api_get_order_states(self)
```

##### Response Type

`object`

##### Example Usage

```python
result = enum_api_controller.enum_api_get_order_states()
```

### Events

#### Overview

##### Get instance

An instance of the `EventsController` class can be accessed from the API Client.

```
events_controller = client.events
```

#### Event Api Get List

Get a list of all events optionally filtered by date. This request is extra throttled to 2 calls per page per hour.

```python
def event_api_get_list(self,
                      min_date=None,
                      max_date=None,
                      page=None,
                      page_size=None,
                      type_id=None,
                      order_id=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `min_date` | `datetime` | Query, Optional | Specifies the oldest date to include in the response |
| `max_date` | `datetime` | Query, Optional | Specifies the newest date to include in the response |
| `page` | `int` | Query, Optional | Specifies the page to request |
| `page_size` | `int` | Query, Optional | Specifies the pagesize. Defaults to 50, max value is 250 |
| `type_id` | `List of int` | Query, Optional | Filter for specific event types |
| `order_id` | `int` | Query, Optional | Filter for specific order id |

##### Response Type

`object`

##### Example Usage

```python
result = events_controller.event_api_get_list()
```

### Orders

#### Overview

##### Get instance

An instance of the `OrdersController` class can be accessed from the API Client.

```
orders_controller = client.orders
```

#### Layout Api Get List

```python
def layout_api_get_list(self)
```

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelsLayoutTemplate`](#rechnungsdruck-web-app-controllers-api-api-result-system-collections-generic-list-billbee-interfaces-billbee-api-models-layout-template)

##### Example Usage

```python
result = orders_controller.layout_api_get_list()
```

#### Order Api Get List

Get a list of all orders optionally filtered by date

```python
def order_api_get_list(self,
                      min_order_date=None,
                      max_order_date=None,
                      page=None,
                      page_size=None,
                      shop_id=None,
                      order_state_id=None,
                      tag=None,
                      minimum_bill_bee_order_id=None,
                      modified_at_min=None,
                      modified_at_max=None,
                      article_title_source=None,
                      exclude_tags=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `min_order_date` | `datetime` | Query, Optional | Specifies the oldest order date to include in the response |
| `max_order_date` | `datetime` | Query, Optional | Specifies the newest order date to include in the response |
| `page` | `int` | Query, Optional | Specifies the page to request |
| `page_size` | `int` | Query, Optional | Specifies the pagesize. Defaults to 50, max value is 250 |
| `shop_id` | `List of long\|int` | Query, Optional | Specifies a list of shop ids for which invoices should be included |
| `order_state_id` | `List of int` | Query, Optional | Specifies a list of state ids to include in the response |
| `tag` | `List of string` | Query, Optional | Specifies a list of tags the order must have attached to be included in the response |
| `minimum_bill_bee_order_id` | `long\|int` | Query, Optional | If given, all delivered orders have an Id greater than or equal to the given minimumOrderId |
| `modified_at_min` | `datetime` | Query, Optional | If given, the last modification has to be newer than the given date |
| `modified_at_max` | `datetime` | Query, Optional | If given, the last modification has to be older or equal than the given date. |
| `article_title_source` | [`ArticleTitleSourceEnum`](#article-title-source) | Query, Optional | The source field for the article title. 0 = Order Position (default), 1 = Article Title, 2 = Article Invoice Text |
| `exclude_tags` | `bool` | Query, Optional | If true the list of tags passed to the call are used to filter orders to not include these tags |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelOrder`](#rechnungsdruck-web-app-controllers-api-api-paged-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-order)

##### Example Usage

```python
result = orders_controller.order_api_get_list()
```

#### Order Api Post New Order

To create an order POST an JSON object to the orders endpoint with the shown properties.
Not all properties are required.

```python
def order_api_post_new_order(self,
                            order_data,
                            shop_id=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_data` | [`BillbeeInterfacesBillbeeAPIModelOrder`](#billbee-interfaces-billbee-api-model-order) | Body, Required | - |
| `shop_id` | `long\|int` | Query, Optional | - |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-order)

##### Example Usage

```python
order_data = BillbeeInterfacesBillbeeAPIModelOrder()

result = orders_controller.order_api_post_new_order(order_data)
```

##### Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid data was received in the request | `APIException` |
| 500 | An internal exception occured. Order was not created | `APIException` |

#### Order Api Tags Update

Updates/Sets the tags attached to an order

```python
def order_api_tags_update(self,
                         tag_data,
                         id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tag_data` | [`RechnungsdruckWebAppControllersApiOrderTagCreate`](#rechnungsdruck-web-app-controllers-api-order-tag-create) | Body, Required | Tags to attach |
| `id` | `long\|int` | Template, Required | The internal id of the order |

##### Response Type

`object`

##### Example Usage

```python
tag_data = RechnungsdruckWebAppControllersApiOrderTagCreate()
id = 112

result = orders_controller.order_api_tags_update(tag_data, id)
```

#### Order Api Tags Create

When a tag is already attached, it is ignored. Tags are not case sensitive.

```python
def order_api_tags_create(self,
                         tag_data,
                         id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tag_data` | [`RechnungsdruckWebAppControllersApiOrderTagCreate`](#rechnungsdruck-web-app-controllers-api-order-tag-create) | Body, Required | Tags to attach |
| `id` | `long\|int` | Template, Required | The internal id of the order |

##### Response Type

`object`

##### Example Usage

```python
tag_data = RechnungsdruckWebAppControllersApiOrderTagCreate()
id = 112

result = orders_controller.order_api_tags_create(tag_data, id)
```

#### Order Api Get

Get a single order by its internal billbee id. This request is throttled to 6 calls per order in one minute

```python
def order_api_get(self,
                 id,
                 article_title_source=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The internal billbee id of the order |
| `article_title_source` | [`ArticleTitleSourceEnum`](#article-title-source) | Query, Optional | The source field for the article title. 0 = Order Position (default), 1 = Article Title, 2 = Article Invoice Text |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-order)

##### Example Usage

```python
id = 112

result = orders_controller.order_api_get(id)
```

#### Order Api Patch Order

Updates one or more fields of an order

```python
def order_api_patch_order(self,
                         id,
                         model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | - |
| `model` | `object` | Body, Required | - |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-order)

##### Example Usage

```python
id = 112
model = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = orders_controller.order_api_patch_order(id, model)
```

#### Order Api Get by Ext Ref

Get a single order by its external order number

```python
def order_api_get_by_ext_ref(self,
                            ext_ref)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ext_ref` | `string` | Template, Required | The extern order number of the order |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder`](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-order)

##### Example Usage

```python
ext_ref = 'extRef8'

result = orders_controller.order_api_get_by_ext_ref(ext_ref)
```

#### Order Api Update State

### REMARKS

Use this call to change the state of an order to i.e. paid or sent.

The state is transfered to the external shop/marketplace if configured.
This is the list of known states:

- 1: ordered
- 2: confirmed
- 3: paid
- 4: shipped
- 5: reclamation
- 6: deleted
- 7: closed
- 8: canceled
- 9: archived
- 10: not used
- 11: demand note 1
- 12: demand note 2
- 13: packed
- 14: offered
- 15: payment reminder
- 16: fulfilling

```python
def order_api_update_state(self,
                          id,
                          model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The internal id of the order |
| `model` | [`RechnungsdruckWebAppControllersApiOrderStateUpdate`](#rechnungsdruck-web-app-controllers-api-order-state-update) | Body, Required | The data used to change the state |

##### Response Type

`object`

##### Example Usage

```python
id = 112
model = RechnungsdruckWebAppControllersApiOrderStateUpdate()

result = orders_controller.order_api_update_state(id, model)
```

#### Order Api Add Shipment

Add a shipment to a given order

```python
def order_api_add_shipment(self,
                          id,
                          model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The internal billbee id of the order |
| `model` | [`RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel`](#rechnungsdruck-web-app-controllers-api-api-add-shipment-to-order-model) | Body, Required | The shipment data to create the shipment |

##### Response Type

`object`

##### Example Usage

```python
id = 112
model = RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel()

result = orders_controller.order_api_add_shipment(id, model)
```

#### Order Api Get Invoice List

Get a list of all invoices optionally filtered by date. This request ist throttled to 1 per 1 minute for same page and minInvoiceDate

```python
def order_api_get_invoice_list(self,
                              min_invoice_date=None,
                              max_invoice_date=None,
                              page=None,
                              page_size=None,
                              shop_id=None,
                              order_state_id=None,
                              tag=None,
                              min_pay_date=None,
                              max_pay_date=None,
                              include_positions=None,
                              exclude_tags=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `min_invoice_date` | `datetime` | Query, Optional | Specifies the oldest invoice date to include |
| `max_invoice_date` | `datetime` | Query, Optional | Specifies the newest invoice date to include |
| `page` | `int` | Query, Optional | Specifies the page to request |
| `page_size` | `int` | Query, Optional | Specifies the pagesize. Defaults to 50, max value is 250 |
| `shop_id` | `List of long\|int` | Query, Optional | Specifies a list of shop ids for which invoices should be included |
| `order_state_id` | `List of int` | Query, Optional | Specifies a list of state ids to include in the response |
| `tag` | `List of string` | Query, Optional | - |
| `min_pay_date` | `datetime` | Query, Optional | - |
| `max_pay_date` | `datetime` | Query, Optional | - |
| `include_positions` | `bool` | Query, Optional | - |
| `exclude_tags` | `bool` | Query, Optional | If true the list of tags passed to the call are used to filter orders to not include these tags |

##### Response Type

`object`

##### Example Usage

```python
result = orders_controller.order_api_get_invoice_list()
```

#### Order Api Find

Find a single order by its external id (order number)

```python
def order_api_find(self,
                  id,
                  partner)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | The order id from the external system |
| `partner` | `string` | Template, Required | Optional the name of the shop/marketplace the order was imported from |

##### Response Type

`object`

##### Example Usage

```python
id = 'id0'
partner = 'partner0'

result = orders_controller.order_api_find(id, partner)
```

#### Order Api Create Delivery Note

Create an delivery note for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.

```python
def order_api_create_delivery_note(self,
                                  id,
                                  include_pdf=None,
                                  send_to_cloud_id=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The internal billbee id of the order |
| `include_pdf` | `bool` | Query, Optional | If true, the PDF is included in the response as base64 encoded string |
| `send_to_cloud_id` | `long\|int` | Query, Optional | Optionally specify the id of a billbee connected cloud device to send the pdf to |

##### Response Type

`object`

##### Example Usage

```python
id = 112

result = orders_controller.order_api_create_delivery_note(id)
```

#### Order Api Create Invoice

Create an invoice for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.

```python
def order_api_create_invoice(self,
                            id,
                            include_invoice_pdf=None,
                            template_id=None,
                            send_to_cloud_id=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The internal billbee id of the order |
| `include_invoice_pdf` | `bool` | Query, Optional | If true, the PDF is included in the response as base64 encoded string |
| `template_id` | `long\|int` | Query, Optional | You can pass the id of an invoice template to overwrite the assigned template for invoice creation |
| `send_to_cloud_id` | `long\|int` | Query, Optional | You can pass the id of a connected cloud printer/storage to send the invoice to it |

##### Response Type

`object`

##### Example Usage

```python
id = 112

result = orders_controller.order_api_create_invoice(id)
```

#### Order Api Get Patchable Fields

Returns a list of fields which can be updated with the orders/{id} patch call

```python
def order_api_get_patchable_fields(self)
```

##### Response Type

`object`

##### Example Usage

```python
result = orders_controller.order_api_get_patchable_fields()
```

#### Order Api Send Message

Sends a message to the buyer

```python
def order_api_send_message(self,
                          id,
                          model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The id of the order |
| `model` | [`RechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel`](#rechnungsdruck-web-app-controllers-api-order-api-controller-send-message-model) | Body, Required | The message model |

##### Response Type

`object`

##### Example Usage

```python
id = 112
model = RechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel()

result = orders_controller.order_api_send_message(id, model)
```

#### Order Api Trigger Event

Triggers a rule event

```python
def order_api_trigger_event(self,
                           id,
                           model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The id of the order |
| `model` | [`RechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer`](#rechnungsdruck-web-app-controllers-api-order-api-controller-trigger-event-container) | Body, Required | - |

##### Response Type

`object`

##### Example Usage

```python
id = 112
model = RechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer()

result = orders_controller.order_api_trigger_event(id, model)
```

#### Order Api Parse Placeholders

Parses a text and replaces all placeholders

```python
def order_api_parse_placeholders(self,
                                id,
                                container)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | The id of the order |
| `container` | [`RechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer`](#rechnungsdruck-web-app-controllers-api-order-api-controller-parse-text-container) | Body, Required | - |

##### Response Type

`object`

##### Example Usage

```python
id = 112
container = RechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer()

result = orders_controller.order_api_parse_placeholders(id, container)
```

### Shipments

#### Overview

##### Get instance

An instance of the `ShipmentsController` class can be accessed from the API Client.

```
shipments_controller = client.shipments
```

#### Shipment Post Shipment

Creates a new shipment with the selected Shippingprovider

```python
def shipment_post_shipment(self,
                          model)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel`](#billbee-interfaces-billbee-api-model-create-shipment-api-model) | Body, Required | Data to specify shipment parameters |

##### Response Type

`object`

##### Example Usage

```python
model = BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel()

result = shipments_controller.shipment_post_shipment(model)
```

#### Shipment Get Shippingproviders

Query all defined shipping providers

```python
def shipment_get_shippingproviders(self)
```

##### Response Type

`object`

##### Example Usage

```python
result = shipments_controller.shipment_get_shippingproviders()
```

#### Shipment Ship With Label

Creates a shipment for an order in billbee

```python
def shipment_ship_with_label(self,
                            shipment_information)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `shipment_information` | [`RechnungsdruckWebAppControllersApiShipmentWithLabel`](#rechnungsdruck-web-app-controllers-api-shipment-with-label) | Body, Required | Details on the order and the shipping methods, that should be used. |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiShipmentWithLabelResult`](#rechnungsdruck-web-app-controllers-api-api-result-rechnungsdruck-web-app-controllers-api-shipment-with-label-result)

##### Example Usage

```python
shipment_information = RechnungsdruckWebAppControllersApiShipmentWithLabel()

result = shipments_controller.shipment_ship_with_label(shipment_information)
```

#### Shipment Get Shipping Carrier

Queries the currently available shipping carriers.

```python
def shipment_get_shipping_carrier(self)
```

##### Response Type

`object`

##### Example Usage

```python
result = shipments_controller.shipment_get_shipping_carrier()
```

#### Shipment Get Ping

```python
def shipment_get_ping(self)
```

##### Response Type

`object`

##### Example Usage

```python
result = shipments_controller.shipment_get_ping()
```

#### Shipment Get List

Get a list of all shipments optionally filtered by date. All parameters are optional.

```python
def shipment_get_list(self,
                     page=None,
                     page_size=None,
                     created_at_min=None,
                     created_at_max=None,
                     order_id=None,
                     minimum_shipment_id=None,
                     shipping_provider_id=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Specifies the page to request. |
| `page_size` | `int` | Query, Optional | Specifies the pagesize. Defaults to 50, max value is 250 |
| `created_at_min` | `datetime` | Query, Optional | Specifies the oldest shipment date to include in the response |
| `created_at_max` | `datetime` | Query, Optional | Specifies the newest shipment date to include in the response |
| `order_id` | `long\|int` | Query, Optional | Get shipments for this order only. |
| `minimum_shipment_id` | `long\|int` | Query, Optional | Get Shipments with a shipment greater or equal than this id. New shipments have a greater id than older shipments. |
| `shipping_provider_id` | `long\|int` | Query, Optional | Get Shippings for the specified shipping provider only. <seealso cref="M:Rechnungsdruck.WebApp.Controllers.Api.ShipmentController.GetShippingproviders" /> |

##### Response Type

[`RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelShipment`](#rechnungsdruck-web-app-controllers-api-api-paged-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-shipment)

##### Example Usage

```python
result = shipments_controller.shipment_get_list()
```

### Webhooks

#### Overview

##### Get instance

An instance of the `WebhooksController` class can be accessed from the API Client.

```
webhooks_controller = client.webhooks
```

#### Web Hook Management Get

Gets all registered WebHooks for a given user.

```python
def web_hook_management_get(self)
```

##### Response Type

[`List of MicrosoftAspNetWebHooksWebHook`](#microsoft-asp-net-web-hooks-web-hook)

##### Example Usage

```python
result = webhooks_controller.web_hook_management_get()
```

#### Web Hook Management Post

Registers a new WebHook for a given user.

```python
def web_hook_management_post(self,
                            web_hook)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `web_hook` | [`MicrosoftAspNetWebHooksWebHook`](#microsoft-asp-net-web-hooks-web-hook) | Body, Required | The webhook to create. Attach ?noecho to the uri to prevent echo test. |

##### Response Type

[`MicrosoftAspNetWebHooksWebHook`](#microsoft-asp-net-web-hooks-web-hook)

##### Example Usage

```python
web_hook = MicrosoftAspNetWebHooksWebHook()
web_hook.web_hook_uri = 'WebHookUri2'

result = webhooks_controller.web_hook_management_post(web_hook)
```

#### Web Hook Management Delete All

Deletes all existing WebHook registrations.

```python
def web_hook_management_delete_all(self)
```

##### Response Type

`object`

##### Example Usage

```python
result = webhooks_controller.web_hook_management_delete_all()
```

#### Web Hook Management Lookup

Looks up a registered WebHook with the given {id} for a given user.

```python
def web_hook_management_lookup(self,
                              id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | - |

##### Response Type

[`MicrosoftAspNetWebHooksWebHook`](#microsoft-asp-net-web-hooks-web-hook)

##### Example Usage

```python
id = 'id0'

result = webhooks_controller.web_hook_management_lookup(id)
```

#### Web Hook Management Put

Updates an existing WebHook registration.

```python
def web_hook_management_put(self,
                           id,
                           web_hook)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | The WebHook ID. |
| `web_hook` | [`MicrosoftAspNetWebHooksWebHook`](#microsoft-asp-net-web-hooks-web-hook) | Body, Required | The new webhook to use. |

##### Response Type

`object`

##### Example Usage

```python
id = 'id0'
web_hook = MicrosoftAspNetWebHooksWebHook()
web_hook.web_hook_uri = 'WebHookUri2'

result = webhooks_controller.web_hook_management_put(id, web_hook)
```

#### Web Hook Management Delete

Deletes an existing WebHook registration.

```python
def web_hook_management_delete(self,
                              id)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | The WebHook ID. |

##### Response Type

`object`

##### Example Usage

```python
id = 'id0'

result = webhooks_controller.web_hook_management_delete(id)
```

#### Web Hook Management Get Filters

Returns a list of all known filters you can use to register webhooks

```python
def web_hook_management_get_filters(self)
```

##### Response Type

`object`

##### Example Usage

```python
result = webhooks_controller.web_hook_management_get_filters()
```

## Model Reference

### Structures

* [Billbee Interfaces Billbee API Model Update Stock Api Model](#billbee-interfaces-billbee-api-model-update-stock-api-model)
* [Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Update Stock Response Data](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-update-stock-response-data)
* [Billbee Interfaces Billbee API Model Update Stock Response Data](#billbee-interfaces-billbee-api-model-update-stock-response-data)
* [Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Get Reserved Amount Response Data](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-get-reserved-amount-response-data)
* [Billbee Interfaces Billbee API Model Get Reserved Amount Response Data](#billbee-interfaces-billbee-api-model-get-reserved-amount-response-data)
* [Billbee Interfaces Billbee API Model Update Stock Code Api Model](#billbee-interfaces-billbee-api-model-update-stock-code-api-model)
* [Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Update Stock Code Response Data](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-update-stock-code-response-data)
* [Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Article Api Model](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-article-api-model)
* [Billbee Interfaces Billbee API Model Article Api Model](#billbee-interfaces-billbee-api-model-article-api-model)
* [Billbee Interfaces Order Multi Language String](#billbee-interfaces-order-multi-language-string)
* [Billbee Interfaces Billbee API Model Article Image Relation Api Model](#billbee-interfaces-billbee-api-model-article-image-relation-api-model)
* [Billbee Interfaces Billbee API Model Article Source Api Model](#billbee-interfaces-billbee-api-model-article-source-api-model)
* [Billbee Interfaces Billbee API Model Stock Article Api Model](#billbee-interfaces-billbee-api-model-stock-article-api-model)
* [Billbee Interfaces Billbee API Model Article Category Api Model](#billbee-interfaces-billbee-api-model-article-category-api-model)
* [Billbee Interfaces Billbee API Model Bom Sub Article Api Model](#billbee-interfaces-billbee-api-model-bom-sub-article-api-model)
* [Billbee Interfaces Billbee API Model Article Api Custom Field Value Model](#billbee-interfaces-billbee-api-model-article-api-custom-field-value-model)
* [Billbee Interfaces Billbee API Model Article Api Custom Field Definition Model](#billbee-interfaces-billbee-api-model-article-api-custom-field-definition-model)
* [Rechnungsdruck Web App Controllers Api Api Paged Result System Collections Generic List Billbee Interfaces Billbee API Model Article Api Model](#rechnungsdruck-web-app-controllers-api-api-paged-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-article-api-model)
* [Rechnungsdruck Web App Controllers Api Api Paged Result Paging Information System Collections Generic List Billbee Interfaces Billbee API Model Article Api Model](#rechnungsdruck-web-app-controllers-api-api-paged-result-paging-information-system-collections-generic-list-billbee-interfaces-billbee-api-model-article-api-model)
* [Rechnungsdruck Web App Controllers Api Api Paged Result System Collections Generic List Billbee Interfaces Billbee API Model Article Api Custom Field Definition Model](#rechnungsdruck-web-app-controllers-api-api-paged-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-article-api-custom-field-definition-model)
* [Rechnungsdruck Web App Controllers Api Api Paged Result Paging Information System Collections Generic List Billbee Interfaces Billbee API Model Article Api Custom Field Definition Model](#rechnungsdruck-web-app-controllers-api-api-paged-result-paging-information-system-collections-generic-list-billbee-interfaces-billbee-api-model-article-api-custom-field-definition-model)
* [Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Article Api Custom Field Definition Model](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-article-api-custom-field-definition-model)
* [Rechnungsdruck Web App Controllers Api Api Result System Collections Generic List Billbee Interfaces Billbee API Model Article Image Relation Api Model](#rechnungsdruck-web-app-controllers-api-api-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-article-image-relation-api-model)
* [Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Article Image Relation Api Model](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-article-image-relation-api-model)
* [Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Deleted Images Model](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-deleted-images-model)
* [Billbee Interfaces Billbee API Model Deleted Images Model](#billbee-interfaces-billbee-api-model-deleted-images-model)
* [Rechnungsdruck Web App Controllers Api Automatic Provisioning Controller Create Account Container](#rechnungsdruck-web-app-controllers-api-automatic-provisioning-controller-create-account-container)
* [Rechnungsdruck Web App Controllers Api Automatic Provisioning Controller Create Account Container User Address](#rechnungsdruck-web-app-controllers-api-automatic-provisioning-controller-create-account-container-user-address)
* [Rechnungsdruck Web App Controllers Api Api Result System Collections Generic List Billbee Interfaces Billbee API Model Cloud Storage Api Model](#rechnungsdruck-web-app-controllers-api-api-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-cloud-storage-api-model)
* [Billbee Interfaces Billbee API Model Cloud Storage Api Model](#billbee-interfaces-billbee-api-model-cloud-storage-api-model)
* [Rechnungsdruck Web App Controllers Api Api Paged Result System Collections Generic List Billbee Interfaces Billbee API Model Customer Api Model](#rechnungsdruck-web-app-controllers-api-api-paged-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-customer-api-model)
* [Rechnungsdruck Web App Controllers Api Api Paged Result Paging Information System Collections Generic List Billbee Interfaces Billbee API Model Customer Api Model](#rechnungsdruck-web-app-controllers-api-api-paged-result-paging-information-system-collections-generic-list-billbee-interfaces-billbee-api-model-customer-api-model)
* [Billbee Interfaces Billbee API Model Customer Api Model](#billbee-interfaces-billbee-api-model-customer-api-model)
* [Billbee Interfaces Billbee API Model Create Customer Api Model](#billbee-interfaces-billbee-api-model-create-customer-api-model)
* [Billbee Interfaces Billbee API Model Customer Address Api Model](#billbee-interfaces-billbee-api-model-customer-address-api-model)
* [Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Customer Api Model](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-customer-api-model)
* [Rechnungsdruck Web App Controllers Api Api Paged Result System Collections Generic List Rechnungsdruck Web App Controllers Api Order](#rechnungsdruck-web-app-controllers-api-api-paged-result-system-collections-generic-list-rechnungsdruck-web-app-controllers-api-order)
* [Rechnungsdruck Web App Controllers Api Api Paged Result Paging Information System Collections Generic List Rechnungsdruck Web App Controllers Api Order](#rechnungsdruck-web-app-controllers-api-api-paged-result-paging-information-system-collections-generic-list-rechnungsdruck-web-app-controllers-api-order)
* [Rechnungsdruck Web App Controllers Api Order](#rechnungsdruck-web-app-controllers-api-order)
* [Rechnungsdruck Web App Controllers Api Api Paged Result System Collections Generic List Billbee Interfaces Billbee API Model Customer Address Api Model](#rechnungsdruck-web-app-controllers-api-api-paged-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-customer-address-api-model)
* [Rechnungsdruck Web App Controllers Api Api Paged Result Paging Information System Collections Generic List Billbee Interfaces Billbee API Model Customer Address Api Model](#rechnungsdruck-web-app-controllers-api-api-paged-result-paging-information-system-collections-generic-list-billbee-interfaces-billbee-api-model-customer-address-api-model)
* [Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Customer Address Api Model](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-customer-address-api-model)
* [Rechnungsdruck Web App Controllers Api Api Result System Collections Generic List Billbee Interfaces Billbee API Models Layout Template](#rechnungsdruck-web-app-controllers-api-api-result-system-collections-generic-list-billbee-interfaces-billbee-api-models-layout-template)
* [Billbee Interfaces Billbee API Models Layout Template](#billbee-interfaces-billbee-api-models-layout-template)
* [Billbee Interfaces Billbee API Model Order](#billbee-interfaces-billbee-api-model-order)
* [Billbee Interfaces Billbee API Model Shipment](#billbee-interfaces-billbee-api-model-shipment)
* [Billbee Interfaces Billbee API Model Comment Api Model](#billbee-interfaces-billbee-api-model-comment-api-model)
* [Billbee Interfaces Billbee API Model Order Address Api Model](#billbee-interfaces-billbee-api-model-order-address-api-model)
* [Billbee Interfaces Billbee API Model Order Item](#billbee-interfaces-billbee-api-model-order-item)
* [Billbee Interfaces Billbee API Model Order User](#billbee-interfaces-billbee-api-model-order-user)
* [Billbee Interfaces Shipping Product Service](#billbee-interfaces-shipping-product-service)
* [Billbee Interfaces Order History Entry](#billbee-interfaces-order-history-entry)
* [Billbee Interfaces Billbee API Models Order Payment](#billbee-interfaces-billbee-api-models-order-payment)
* [Billbee Interfaces Billbee API Model Sold Product](#billbee-interfaces-billbee-api-model-sold-product)
* [Billbee Interfaces Billbee API Model Order Item Attribute](#billbee-interfaces-billbee-api-model-order-item-attribute)
* [System Collections Generic Key Value Pair System String System Collections Generic List System Collections Generic Key Value Pair System Int 32 System String](#system-collections-generic-key-value-pair-system-string-system-collections-generic-list-system-collections-generic-key-value-pair-system-int-32-system-string)
* [Billbee Interfaces Billbee API Model Product Image](#billbee-interfaces-billbee-api-model-product-image)
* [System Collections Generic Key Value Pair System Int 32 System String](#system-collections-generic-key-value-pair-system-int-32-system-string)
* [Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Order](#rechnungsdruck-web-app-controllers-api-api-result-billbee-interfaces-billbee-api-model-order)
* [Rechnungsdruck Web App Controllers Api Api Paged Result System Collections Generic List Billbee Interfaces Billbee API Model Order](#rechnungsdruck-web-app-controllers-api-api-paged-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-order)
* [Rechnungsdruck Web App Controllers Api Api Paged Result Paging Information System Collections Generic List Billbee Interfaces Billbee API Model Order](#rechnungsdruck-web-app-controllers-api-api-paged-result-paging-information-system-collections-generic-list-billbee-interfaces-billbee-api-model-order)
* [Rechnungsdruck Web App Controllers Api Order Tag Create](#rechnungsdruck-web-app-controllers-api-order-tag-create)
* [Rechnungsdruck Web App Controllers Api Order State Update](#rechnungsdruck-web-app-controllers-api-order-state-update)
* [Rechnungsdruck Web App Controllers Api Api Add Shipment to Order Model](#rechnungsdruck-web-app-controllers-api-api-add-shipment-to-order-model)
* [Rechnungsdruck Web App Controllers Api Order Api Controller Send Message Model](#rechnungsdruck-web-app-controllers-api-order-api-controller-send-message-model)
* [Rechnungsdruck Web App Controllers Api Order Api Controller Trigger Event Container](#rechnungsdruck-web-app-controllers-api-order-api-controller-trigger-event-container)
* [Rechnungsdruck Web App Controllers Api Order Api Controller Parse Text Container](#rechnungsdruck-web-app-controllers-api-order-api-controller-parse-text-container)
* [Rechnungsdruck Web App Controllers Api Search Controller Search Model](#rechnungsdruck-web-app-controllers-api-search-controller-search-model)
* [Rechnungsdruck Web App Controllers Api Api Result Rechnungsdruck Web App Controllers Api Search Controller Search Results Model](#rechnungsdruck-web-app-controllers-api-api-result-rechnungsdruck-web-app-controllers-api-search-controller-search-results-model)
* [Rechnungsdruck Web App Controllers Api Search Controller Search Results Model](#rechnungsdruck-web-app-controllers-api-search-controller-search-results-model)
* [Rechnungsdruck Web App Controllers Api Search Controller Product Result](#rechnungsdruck-web-app-controllers-api-search-controller-product-result)
* [Rechnungsdruck Web App Controllers Api Search Controller Order Result](#rechnungsdruck-web-app-controllers-api-search-controller-order-result)
* [Rechnungsdruck Web App Controllers Api Search Controller Customer Result](#rechnungsdruck-web-app-controllers-api-search-controller-customer-result)
* [Billbee Interfaces Billbee API Model Create Shipment Api Model](#billbee-interfaces-billbee-api-model-create-shipment-api-model)
* [Billbee Interfaces Billbee API Model Shipment Address Api Model](#billbee-interfaces-billbee-api-model-shipment-address-api-model)
* [Billbee Interfaces Shipping Shipment Data Dimensions](#billbee-interfaces-shipping-shipment-data-dimensions)
* [Rechnungsdruck Web App Controllers Api Shipment With Label](#rechnungsdruck-web-app-controllers-api-shipment-with-label)
* [Rechnungsdruck Web App Controllers Api Api Result Rechnungsdruck Web App Controllers Api Shipment With Label Result](#rechnungsdruck-web-app-controllers-api-api-result-rechnungsdruck-web-app-controllers-api-shipment-with-label-result)
* [Rechnungsdruck Web App Controllers Api Shipment With Label Result](#rechnungsdruck-web-app-controllers-api-shipment-with-label-result)
* [Rechnungsdruck Web App Controllers Api Api Paged Result System Collections Generic List Billbee Interfaces Billbee API Model Shipment](#rechnungsdruck-web-app-controllers-api-api-paged-result-system-collections-generic-list-billbee-interfaces-billbee-api-model-shipment)
* [Rechnungsdruck Web App Controllers Api Api Paged Result Paging Information System Collections Generic List Billbee Interfaces Billbee API Model Shipment](#rechnungsdruck-web-app-controllers-api-api-paged-result-paging-information-system-collections-generic-list-billbee-interfaces-billbee-api-model-shipment)
* [Microsoft Asp Net Web Hooks Web Hook](#microsoft-asp-net-web-hooks-web-hook)

#### Billbee Interfaces Billbee API Model Update Stock Api Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billbee_id` | `long\|int` | Optional | Optional the ID of the Billbee product to update |
| `sku` | `string` | Optional | The SKU of the product to update |
| `stock_id` | `long\|int` | Optional | Optional the stock id if the feature multi stock is activated |
| `reason` | `string` | Optional | Optional a reason text for the stock update |
| `old_quantity` | `float` | Optional | This parameter is currently ignored |
| `new_quantity` | `float` | Optional | The new absolute stock quantity for the product you want to set |
| `delta_quantity` | `float` | Optional | This parameter is currently ignored |
| `force_send_stock_to_shops` | `bool` | Optional | If true, every sent stockchange is stored and transmitted to the connected shop, even if the value has not changed |
| `autosubtract_reserved_amount` | `bool` | Optional | Automatically reduce the NewQuantity by the currently not fulfilled amount |

##### Example (as JSON)

```json
{
  "BillbeeId": null,
  "Sku": null,
  "StockId": null,
  "Reason": null,
  "OldQuantity": null,
  "NewQuantity": null,
  "DeltaQuantity": null,
  "ForceSendStockToShops": null,
  "AutosubtractReservedAmount": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Update Stock Response Data

##### Class Name

`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`BillbeeInterfacesBillbeeAPIModelUpdateStockResponseData`](#billbee-interfaces-billbee-api-model-update-stock-response-data) | Optional | - |

##### Example (as JSON)

```json
{
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Billbee Interfaces Billbee API Model Update Stock Response Data

##### Class Name

`BillbeeInterfacesBillbeeAPIModelUpdateStockResponseData`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sku` | `string` | Optional | The SKU of the article to update the current stock |
| `current_stock` | `float` | Optional | The new value for current stock after the update |
| `unfulfilled_amount` | `float` | Optional | The value of the unfulfilled amount (reserved) of the article |
| `message` | `string` | Optional | A human readable message that explains the result of the operation |

##### Example (as JSON)

```json
{
  "SKU": null,
  "CurrentStock": null,
  "UnfulfilledAmount": null,
  "Message": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Get Reserved Amount Response Data

##### Class Name

`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelGetReservedAmountResponseData`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`BillbeeInterfacesBillbeeAPIModelGetReservedAmountResponseData`](#billbee-interfaces-billbee-api-model-get-reserved-amount-response-data) | Optional | - |

##### Example (as JSON)

```json
{
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Billbee Interfaces Billbee API Model Get Reserved Amount Response Data

##### Class Name

`BillbeeInterfacesBillbeeAPIModelGetReservedAmountResponseData`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reserved_amount` | `float` | Optional | The reserve (not fulfilled) qty of the article |

##### Example (as JSON)

```json
{
  "ReservedAmount": null
}
```

#### Billbee Interfaces Billbee API Model Update Stock Code Api Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billbee_id` | `long\|int` | Optional | - |
| `sku` | `string` | Optional | - |
| `stock_id` | `long\|int` | Optional | - |
| `stock_code` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "BillbeeId": null,
  "Sku": null,
  "StockId": null,
  "StockCode": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Update Stock Code Response Data

##### Class Name

`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockCodeResponseData`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | `object` | Optional | - |

##### Example (as JSON)

```json
{
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Article Api Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`BillbeeInterfacesBillbeeAPIModelArticleApiModel`](#billbee-interfaces-billbee-api-model-article-api-model) | Optional | - |

##### Example (as JSON)

```json
{
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Billbee Interfaces Billbee API Model Article Api Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelArticleApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice_text` | [`List of BillbeeInterfacesOrderMultiLanguageString`](#billbee-interfaces-order-multi-language-string) | Optional | - |
| `manufacturer` | `string` | Optional | - |
| `id` | `long\|int` | Optional | - |
| `title` | [`List of BillbeeInterfacesOrderMultiLanguageString`](#billbee-interfaces-order-multi-language-string) | Optional | - |
| `description` | [`List of BillbeeInterfacesOrderMultiLanguageString`](#billbee-interfaces-order-multi-language-string) | Optional | - |
| `short_description` | [`List of BillbeeInterfacesOrderMultiLanguageString`](#billbee-interfaces-order-multi-language-string) | Optional | - |
| `basic_attributes` | [`List of BillbeeInterfacesOrderMultiLanguageString`](#billbee-interfaces-order-multi-language-string) | Optional | - |
| `images` | [`List of BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel`](#billbee-interfaces-billbee-api-model-article-image-relation-api-model) | Optional | - |
| `vat_index` | `int` | Required | - |
| `price` | `float` | Required | - |
| `cost_price` | `float` | Optional | - |
| `vat_1_rate` | `float` | Required | - |
| `vat_2_rate` | `float` | Required | - |
| `stock_desired` | `float` | Optional | - |
| `stock_current` | `float` | Optional | - |
| `stock_warning` | `float` | Optional | - |
| `sku` | `string` | Optional | - |
| `ean` | `string` | Optional | - |
| `materials` | [`List of BillbeeInterfacesOrderMultiLanguageString`](#billbee-interfaces-order-multi-language-string) | Optional | - |
| `tags` | [`List of BillbeeInterfacesOrderMultiLanguageString`](#billbee-interfaces-order-multi-language-string) | Optional | - |
| `sources` | [`List of BillbeeInterfacesBillbeeAPIModelArticleSourceApiModel`](#billbee-interfaces-billbee-api-model-article-source-api-model) | Optional | - |
| `weight` | `int` | Optional | - |
| `weight_net` | `int` | Optional | - |
| `low_stock` | `bool` | Optional | - |
| `stock_code` | `string` | Optional | - |
| `stock_reduce_items_per_sale` | `float` | Optional | - |
| `stocks` | [`List of BillbeeInterfacesBillbeeAPIModelStockArticleApiModel`](#billbee-interfaces-billbee-api-model-stock-article-api-model) | Optional | - |
| `category_1` | [`BillbeeInterfacesBillbeeAPIModelArticleCategoryApiModel`](#billbee-interfaces-billbee-api-model-article-category-api-model) | Optional | - |
| `category_2` | [`BillbeeInterfacesBillbeeAPIModelArticleCategoryApiModel`](#billbee-interfaces-billbee-api-model-article-category-api-model) | Optional | - |
| `category_3` | [`BillbeeInterfacesBillbeeAPIModelArticleCategoryApiModel`](#billbee-interfaces-billbee-api-model-article-category-api-model) | Optional | - |
| `mtype` | `int` | Required | - |
| `unit` | `int` | Optional | - |
| `units_per_item` | `float` | Optional | - |
| `sold_amount` | `float` | Optional | - |
| `sold_sum_gross` | `float` | Optional | - |
| `sold_sum_net` | `float` | Optional | - |
| `sold_sum_net_last_30_days` | `float` | Optional | - |
| `sold_sum_gross_last_30_days` | `float` | Optional | - |
| `sold_amount_last_30_days` | `float` | Optional | - |
| `shipping_product_id` | `int` | Optional | - |
| `is_digital` | `bool` | Required | - |
| `is_customizable` | `bool` | Required | - |
| `delivery_time` | `int` | Optional | - |
| `recipient` | `int` | Optional | - |
| `occasion` | `int` | Optional | - |
| `country_of_origin` | `string` | Optional | - |
| `export_description` | `string` | Optional | - |
| `taric_number` | `string` | Optional | - |
| `condition` | `int` | Optional | - |
| `width_cm` | `float` | Optional | - |
| `length_cm` | `float` | Optional | - |
| `height_cm` | `float` | Optional | - |
| `bill_of_material` | [`List of BillbeeInterfacesBillbeeAPIModelBomSubArticleApiModel`](#billbee-interfaces-billbee-api-model-bom-sub-article-api-model) | Optional | - |
| `custom_fields` | [`List of BillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldValueModel`](#billbee-interfaces-billbee-api-model-article-api-custom-field-value-model) | Optional | - |

##### Example (as JSON)

```json
{
  "InvoiceText": null,
  "Manufacturer": null,
  "Id": null,
  "Title": null,
  "Description": null,
  "ShortDescription": null,
  "BasicAttributes": null,
  "Images": null,
  "VatIndex": 40,
  "Price": 6.2,
  "CostPrice": null,
  "Vat1Rate": 232.14,
  "Vat2Rate": 233.2,
  "StockDesired": null,
  "StockCurrent": null,
  "StockWarning": null,
  "SKU": null,
  "EAN": null,
  "Materials": null,
  "Tags": null,
  "Sources": null,
  "Weight": null,
  "WeightNet": null,
  "LowStock": null,
  "StockCode": null,
  "StockReduceItemsPerSale": null,
  "Stocks": null,
  "Category1": null,
  "Category2": null,
  "Category3": null,
  "Type": 190,
  "Unit": null,
  "UnitsPerItem": null,
  "SoldAmount": null,
  "SoldSumGross": null,
  "SoldSumNet": null,
  "SoldSumNetLast30Days": null,
  "SoldSumGrossLast30Days": null,
  "SoldAmountLast30Days": null,
  "ShippingProductId": null,
  "IsDigital": false,
  "IsCustomizable": false,
  "DeliveryTime": null,
  "Recipient": null,
  "Occasion": null,
  "CountryOfOrigin": null,
  "ExportDescription": null,
  "TaricNumber": null,
  "Condition": null,
  "WidthCm": null,
  "LengthCm": null,
  "HeightCm": null,
  "BillOfMaterial": null,
  "CustomFields": null
}
```

#### Billbee Interfaces Order Multi Language String

##### Class Name

`BillbeeInterfacesOrderMultiLanguageString`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `string` | Optional | - |
| `language_code` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "Text": null,
  "LanguageCode": null
}
```

#### Billbee Interfaces Billbee API Model Article Image Relation Api Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `string` | Optional | - |
| `id` | `long\|int` | Optional | - |
| `thumb_path_ext` | `string` | Optional | - |
| `thumb_url` | `string` | Optional | - |
| `position` | `int` | Optional | - |
| `is_default` | `bool` | Optional | - |
| `article_id` | `long\|int` | Optional | - |

##### Example (as JSON)

```json
{
  "Url": null,
  "Id": null,
  "ThumbPathExt": null,
  "ThumbUrl": null,
  "Position": null,
  "IsDefault": null,
  "ArticleId": null
}
```

#### Billbee Interfaces Billbee API Model Article Source Api Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelArticleSourceApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `source` | `string` | Required | - |
| `source_id` | `string` | Required | - |
| `api_account_name` | `string` | Optional | - |
| `api_account_id` | `long\|int` | Optional | - |
| `export_factor` | `float` | Optional | - |
| `stock_sync_inactive` | `bool` | Optional | - |
| `stock_sync_min` | `float` | Optional | - |
| `stock_sync_max` | `float` | Optional | - |
| `units_per_item` | `float` | Optional | - |
| `custom` | `object` | Optional | - |

##### Example (as JSON)

```json
{
  "Id": null,
  "Source": "Source0",
  "SourceId": "SourceId2",
  "ApiAccountName": null,
  "ApiAccountId": null,
  "ExportFactor": null,
  "StockSyncInactive": null,
  "StockSyncMin": null,
  "StockSyncMax": null,
  "UnitsPerItem": null,
  "Custom": null
}
```

#### Billbee Interfaces Billbee API Model Stock Article Api Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelStockArticleApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | - |
| `stock_id` | `int` | Optional | - |
| `stock_current` | `float` | Optional | - |
| `stock_warning` | `float` | Optional | - |
| `stock_code` | `string` | Optional | - |
| `unfulfilled_amount` | `float` | Optional | - |
| `stock_desired` | `float` | Optional | - |

##### Example (as JSON)

```json
{
  "Name": null,
  "StockId": null,
  "StockCurrent": null,
  "StockWarning": null,
  "StockCode": null,
  "UnfulfilledAmount": null,
  "StockDesired": null
}
```

#### Billbee Interfaces Billbee API Model Article Category Api Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelArticleCategoryApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | - |
| `id` | `long\|int` | Optional | - |

##### Example (as JSON)

```json
{
  "Name": null,
  "Id": null
}
```

#### Billbee Interfaces Billbee API Model Bom Sub Article Api Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelBomSubArticleApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `float` | Optional | - |
| `article_id` | `long\|int` | Optional | - |
| `sku` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "Amount": null,
  "ArticleId": null,
  "SKU": null
}
```

#### Billbee Interfaces Billbee API Model Article Api Custom Field Value Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldValueModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | - |
| `definition_id` | `long\|int` | Optional | - |
| `definition` | [`BillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel`](#billbee-interfaces-billbee-api-model-article-api-custom-field-definition-model) | Optional | - |
| `article_id` | `long\|int` | Optional | - |
| `value` | `object` | Optional | - |

##### Example (as JSON)

```json
{
  "Id": null,
  "DefinitionId": null,
  "Definition": null,
  "ArticleId": null,
  "Value": null
}
```

#### Billbee Interfaces Billbee API Model Article Api Custom Field Definition Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | - |
| `name` | `string` | Optional | - |
| `configuration` | `object` | Optional | - |
| `mtype` | [`TypeEnum`](#type) | Optional | - |
| `is_nullable` | `bool` | Optional | - |

##### Example (as JSON)

```json
{
  "Id": null,
  "Name": null,
  "Configuration": null,
  "Type": null,
  "IsNullable": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Paged Result System Collections Generic List Billbee Interfaces Billbee API Model Article Api Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `paging` | [`RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiModel`](#rechnungsdruck-web-app-controllers-api-api-paged-result-paging-information-system-collections-generic-list-billbee-interfaces-billbee-api-model-article-api-model) | Optional | - |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`List of BillbeeInterfacesBillbeeAPIModelArticleApiModel`](#billbee-interfaces-billbee-api-model-article-api-model) | Optional | - |

##### Example (as JSON)

```json
{
  "Paging": null,
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Paged Result Paging Information System Collections Generic List Billbee Interfaces Billbee API Model Article Api Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Optional | - |
| `total_pages` | `int` | Optional | - |
| `total_rows` | `int` | Optional | - |
| `page_size` | `int` | Optional | - |

##### Example (as JSON)

```json
{
  "Page": null,
  "TotalPages": null,
  "TotalRows": null,
  "PageSize": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Paged Result System Collections Generic List Billbee Interfaces Billbee API Model Article Api Custom Field Definition Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `paging` | [`RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel`](#rechnungsdruck-web-app-controllers-api-api-paged-result-paging-information-system-collections-generic-list-billbee-interfaces-billbee-api-model-article-api-custom-field-definition-model) | Optional | - |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`List of BillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel`](#billbee-interfaces-billbee-api-model-article-api-custom-field-definition-model) | Optional | - |

##### Example (as JSON)

```json
{
  "Paging": null,
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Paged Result Paging Information System Collections Generic List Billbee Interfaces Billbee API Model Article Api Custom Field Definition Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Optional | - |
| `total_pages` | `int` | Optional | - |
| `total_rows` | `int` | Optional | - |
| `page_size` | `int` | Optional | - |

##### Example (as JSON)

```json
{
  "Page": null,
  "TotalPages": null,
  "TotalRows": null,
  "PageSize": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Article Api Custom Field Definition Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`BillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel`](#billbee-interfaces-billbee-api-model-article-api-custom-field-definition-model) | Optional | - |

##### Example (as JSON)

```json
{
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Result System Collections Generic List Billbee Interfaces Billbee API Model Article Image Relation Api Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`List of BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel`](#billbee-interfaces-billbee-api-model-article-image-relation-api-model) | Optional | - |

##### Example (as JSON)

```json
{
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Article Image Relation Api Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel`](#billbee-interfaces-billbee-api-model-article-image-relation-api-model) | Optional | - |

##### Example (as JSON)

```json
{
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Deleted Images Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelDeletedImagesModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`BillbeeInterfacesBillbeeAPIModelDeletedImagesModel`](#billbee-interfaces-billbee-api-model-deleted-images-model) | Optional | - |

##### Example (as JSON)

```json
{
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Billbee Interfaces Billbee API Model Deleted Images Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelDeletedImagesModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `deleted` | `List of long\|int` | Optional | - |
| `not_found` | `List of long\|int` | Optional | - |

##### Example (as JSON)

```json
{
  "Deleted": null,
  "NotFound": null
}
```

#### Rechnungsdruck Web App Controllers Api Automatic Provisioning Controller Create Account Container

Data used to create a new Billbee user account

##### Class Name

`RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `e_mail` | `string` | Required | The Email address of the user to create |
| `password` | `string` | Optional | - |
| `accept_terms` | `bool` | Optional | Set to true, if the user has accepted the Billbee terms &amp; conditions |
| `address` | [`RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainerUserAddress`](#rechnungsdruck-web-app-controllers-api-automatic-provisioning-controller-create-account-container-user-address) | Optional | Represents the invoice address of a Billbee user |
| `newsletter` | `bool` | Optional | Gets or sets if the user is interested in the Billbee newsletter |
| `affiliate_coupon_code` | `string` | Optional | Specifies an billbee affiliate code to attach to the user |
| `vat_1_rate` | `float` | Optional | Optionally specify the vat1 (normal) rate of the user |
| `vat_2_rate` | `float` | Optional | Optionally specify the vat2 (reduced) rate of the user |
| `default_vat_mode` | [`DefaultVatModeEnum`](#default-vat-mode) | Optional | Optionally specify the default vat mode of the user |
| `default_currrency` | `string` | Optional | Optionally specify the default currency of the user |
| `default_vat_index` | `int` | Optional | Optionally specify the default vat index of the user |

##### Example (as JSON)

```json
{
  "EMail": "EMail0",
  "Password": null,
  "AcceptTerms": null,
  "Address": null,
  "Newsletter": null,
  "AffiliateCouponCode": null,
  "Vat1Rate": null,
  "Vat2Rate": null,
  "DefaultVatMode": null,
  "DefaultCurrrency": null,
  "DefaultVatIndex": null
}
```

#### Rechnungsdruck Web App Controllers Api Automatic Provisioning Controller Create Account Container User Address

Represents the invoice address of a Billbee user

##### Class Name

`RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainerUserAddress`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company` | `string` | Optional | - |
| `name` | `string` | Optional | - |
| `address_1` | `string` | Optional | - |
| `address_2` | `string` | Optional | - |
| `zip` | `string` | Optional | - |
| `city` | `string` | Optional | - |
| `country` | `string` | Optional | The ISO2 country code of the users country |
| `vat_id` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "Company": null,
  "Name": null,
  "Address1": null,
  "Address2": null,
  "Zip": null,
  "City": null,
  "Country": null,
  "VatId": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Result System Collections Generic List Billbee Interfaces Billbee API Model Cloud Storage Api Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCloudStorageApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`List of BillbeeInterfacesBillbeeAPIModelCloudStorageApiModel`](#billbee-interfaces-billbee-api-model-cloud-storage-api-model) | Optional | - |

##### Example (as JSON)

```json
{
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Billbee Interfaces Billbee API Model Cloud Storage Api Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelCloudStorageApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | - |
| `name` | `string` | Optional | - |
| `mtype` | `string` | Optional | - |
| `used_as_printer` | `bool` | Optional | - |

##### Example (as JSON)

```json
{
  "Id": null,
  "Name": null,
  "Type": null,
  "UsedAsPrinter": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Paged Result System Collections Generic List Billbee Interfaces Billbee API Model Customer Api Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `paging` | [`RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel`](#rechnungsdruck-web-app-controllers-api-api-paged-result-paging-information-system-collections-generic-list-billbee-interfaces-billbee-api-model-customer-api-model) | Optional | - |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`List of BillbeeInterfacesBillbeeAPIModelCustomerApiModel`](#billbee-interfaces-billbee-api-model-customer-api-model) | Optional | - |

##### Example (as JSON)

```json
{
  "Paging": null,
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Paged Result Paging Information System Collections Generic List Billbee Interfaces Billbee API Model Customer Api Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Optional | - |
| `total_pages` | `int` | Optional | - |
| `total_rows` | `int` | Optional | - |
| `page_size` | `int` | Optional | - |

##### Example (as JSON)

```json
{
  "Page": null,
  "TotalPages": null,
  "TotalRows": null,
  "PageSize": null
}
```

#### Billbee Interfaces Billbee API Model Customer Api Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelCustomerApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | The Billbee Id of the customer |
| `name` | `string` | Optional | - |
| `email` | `string` | Optional | - |
| `tel_1` | `string` | Optional | - |
| `tel_2` | `string` | Optional | - |
| `number` | `int` | Optional | - |
| `price_group_id` | `long\|int` | Optional | - |
| `language_id` | `int` | Optional | - |
| `vat_id` | `string` | Optional | - |
| `mtype` | `int` | Optional | Customer Type |

##### Example (as JSON)

```json
{
  "Id": null,
  "Name": null,
  "Email": null,
  "Tel1": null,
  "Tel2": null,
  "Number": null,
  "PriceGroupId": null,
  "LanguageId": null,
  "VatId": null,
  "Type": null
}
```

#### Billbee Interfaces Billbee API Model Create Customer Api Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#billbee-interfaces-billbee-api-model-customer-address-api-model) | Optional | Container for passing address data |
| `id` | `long\|int` | Optional | The Billbee Id of the customer |
| `name` | `string` | Optional | - |
| `email` | `string` | Optional | - |
| `tel_1` | `string` | Optional | - |
| `tel_2` | `string` | Optional | - |
| `number` | `int` | Optional | - |
| `price_group_id` | `long\|int` | Optional | - |
| `language_id` | `int` | Optional | - |
| `vat_id` | `string` | Optional | - |
| `mtype` | `int` | Optional | Customer Type |

##### Example (as JSON)

```json
{
  "Address": null,
  "Id": null,
  "Name": null,
  "Email": null,
  "Tel1": null,
  "Tel2": null,
  "Number": null,
  "PriceGroupId": null,
  "LanguageId": null,
  "VatId": null,
  "Type": null
}
```

#### Billbee Interfaces Billbee API Model Customer Address Api Model

Container for passing address data

##### Class Name

`BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | The internal Billbee ID of the address record. Can be null if a new address is created |
| `address_type` | [`AddressTypeEnum`](#address-type) | Optional | The type of the address |
| `customer_id` | `long\|int` | Optional | The internal Billbee id of the customer the address belongs to |
| `company` | `string` | Optional | The name of the company |
| `first_name` | `string` | Optional | - |
| `last_name` | `string` | Optional | - |
| `name_2` | `string` | Optional | Optionally an additional name field |
| `street` | `string` | Optional | - |
| `housenumber` | `string` | Optional | - |
| `zip` | `string` | Optional | - |
| `city` | `string` | Optional | - |
| `state` | `string` | Optional | - |
| `country_code` | `string` | Optional | The ISO2 code of the country |
| `email` | `string` | Optional | - |
| `tel_1` | `string` | Optional | - |
| `tel_2` | `string` | Optional | - |
| `fax` | `string` | Optional | - |
| `address_addition` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "Id": null,
  "AddressType": null,
  "CustomerId": null,
  "Company": null,
  "FirstName": null,
  "LastName": null,
  "Name2": null,
  "Street": null,
  "Housenumber": null,
  "Zip": null,
  "City": null,
  "State": null,
  "CountryCode": null,
  "Email": null,
  "Tel1": null,
  "Tel2": null,
  "Fax": null,
  "AddressAddition": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Customer Api Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`BillbeeInterfacesBillbeeAPIModelCustomerApiModel`](#billbee-interfaces-billbee-api-model-customer-api-model) | Optional | - |

##### Example (as JSON)

```json
{
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Paged Result System Collections Generic List Rechnungsdruck Web App Controllers Api Order

##### Class Name

`RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListRechnungsdruckWebAppControllersApiOrder`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `paging` | [`RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListRechnungsdruckWebAppControllersApiOrder`](#rechnungsdruck-web-app-controllers-api-api-paged-result-paging-information-system-collections-generic-list-rechnungsdruck-web-app-controllers-api-order) | Optional | - |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`List of RechnungsdruckWebAppControllersApiOrder`](#rechnungsdruck-web-app-controllers-api-order) | Optional | - |

##### Example (as JSON)

```json
{
  "Paging": null,
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Paged Result Paging Information System Collections Generic List Rechnungsdruck Web App Controllers Api Order

##### Class Name

`RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListRechnungsdruckWebAppControllersApiOrder`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Optional | - |
| `total_pages` | `int` | Optional | - |
| `total_rows` | `int` | Optional | - |
| `page_size` | `int` | Optional | - |

##### Example (as JSON)

```json
{
  "Page": null,
  "TotalPages": null,
  "TotalRows": null,
  "PageSize": null
}
```

#### Rechnungsdruck Web App Controllers Api Order

##### Class Name

`RechnungsdruckWebAppControllersApiOrder`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `external_id` | `string` | Optional | - |
| `invoice_number` | `string` | Optional | - |
| `invoice_created_at` | `datetime` | Optional | - |
| `invoice_date` | `datetime` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `paid_at` | `datetime` | Optional | - |
| `shipped_at` | `datetime` | Optional | - |
| `has_invoice` | `bool` | Optional | - |
| `order_state_id` | `int` | Optional | - |
| `order_state_text` | `string` | Optional | - |
| `total_gross` | `float` | Optional | - |
| `shop_name` | `string` | Optional | - |
| `can_create_auto_invoice` | `bool` | Optional | - |

##### Example (as JSON)

```json
{
  "Id": null,
  "ExternalId": null,
  "InvoiceNumber": null,
  "InvoiceCreatedAt": null,
  "InvoiceDate": null,
  "CreatedAt": null,
  "PaidAt": null,
  "ShippedAt": null,
  "HasInvoice": null,
  "OrderStateId": null,
  "OrderStateText": null,
  "TotalGross": null,
  "ShopName": null,
  "CanCreateAutoInvoice": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Paged Result System Collections Generic List Billbee Interfaces Billbee API Model Customer Address Api Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `paging` | [`RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#rechnungsdruck-web-app-controllers-api-api-paged-result-paging-information-system-collections-generic-list-billbee-interfaces-billbee-api-model-customer-address-api-model) | Optional | - |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`List of BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#billbee-interfaces-billbee-api-model-customer-address-api-model) | Optional | - |

##### Example (as JSON)

```json
{
  "Paging": null,
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Paged Result Paging Information System Collections Generic List Billbee Interfaces Billbee API Model Customer Address Api Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Optional | - |
| `total_pages` | `int` | Optional | - |
| `total_rows` | `int` | Optional | - |
| `page_size` | `int` | Optional | - |

##### Example (as JSON)

```json
{
  "Page": null,
  "TotalPages": null,
  "TotalRows": null,
  "PageSize": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Customer Address Api Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel`](#billbee-interfaces-billbee-api-model-customer-address-api-model) | Optional | Container for passing address data |

##### Example (as JSON)

```json
{
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Result System Collections Generic List Billbee Interfaces Billbee API Models Layout Template

##### Class Name

`RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelsLayoutTemplate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`List of BillbeeInterfacesBillbeeAPIModelsLayoutTemplate`](#billbee-interfaces-billbee-api-models-layout-template) | Optional | - |

##### Example (as JSON)

```json
{
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Billbee Interfaces Billbee API Models Layout Template

##### Class Name

`BillbeeInterfacesBillbeeAPIModelsLayoutTemplate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | - |
| `name` | `string` | Optional | - |
| `mtype` | [`Type1Enum`](#type-1) | Optional | - |

##### Example (as JSON)

```json
{
  "Id": null,
  "Name": null,
  "Type": null
}
```

#### Billbee Interfaces Billbee API Model Order

A class that represents the Billbee data model of a single order

##### Class Name

`BillbeeInterfacesBillbeeAPIModelOrder`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `rebate_difference` | `float` | Optional | - |
| `shipping_ids` | [`List of BillbeeInterfacesBillbeeAPIModelShipment`](#billbee-interfaces-billbee-api-model-shipment) | Optional | The shipments of the order |
| `accept_loss_of_return_right` | `bool` | Optional | Customer accepts loss due to withdrawal |
| `id` | `string` | Optional | Id of the order in the external system (marketplace) |
| `order_number` | `string` | Optional | Order number of the order in the external system (marketplace) |
| `state` | [`StateEnum`](#state) | Optional | The current state of the order |
| `vat_mode` | [`VatModeEnum`](#vat-mode) | Optional | The vat mode of the order |
| `created_at` | `datetime` | Optional | The date on which the order was created |
| `shipped_at` | `datetime` | Optional | The date on which the order was shipped |
| `confirmed_at` | `datetime` | Optional | The date on which the order was confirmed |
| `payed_at` | `datetime` | Optional | The date on which the order was paid |
| `seller_comment` | `string` | Optional | An internal seller comment |
| `comments` | [`List of BillbeeInterfacesBillbeeAPIModelCommentApiModel`](#billbee-interfaces-billbee-api-model-comment-api-model) | Optional | All messages / comments of the order |
| `invoice_number_prefix` | `string` | Optional | The prefix of the invoice number |
| `invoice_number_postfix` | `string` | Optional | The postfix of the invoice number |
| `invoice_number` | `int` | Optional | The invoice number |
| `invoice_date` | `datetime` | Optional | The date on which the invoice was created |
| `invoice_address` | [`BillbeeInterfacesBillbeeAPIModelOrderAddressApiModel`](#billbee-interfaces-billbee-api-model-order-address-api-model) | Optional | - |
| `shipping_address` | [`BillbeeInterfacesBillbeeAPIModelOrderAddressApiModel`](#billbee-interfaces-billbee-api-model-order-address-api-model) | Optional | - |
| `payment_method` | [`PaymentMethodEnum`](#payment-method) | Optional | The payment method |
| `shipping_cost` | `float` | Optional | The shipping cost |
| `total_cost` | `float` | Optional | The total cost excluding shipping cost |
| `adjustment_cost` | `float` | Optional | - |
| `adjustment_reason` | `string` | Optional | - |
| `order_items` | [`List of BillbeeInterfacesBillbeeAPIModelOrderItem`](#billbee-interfaces-billbee-api-model-order-item) | Optional | The list of items purchased like shirt, pant, toys etc |
| `currency` | `string` | Optional | The three letter currency code. |
| `seller` | [`BillbeeInterfacesBillbeeAPIModelOrderUser`](#billbee-interfaces-billbee-api-model-order-user) | Optional | - |
| `buyer` | [`BillbeeInterfacesBillbeeAPIModelOrderUser`](#billbee-interfaces-billbee-api-model-order-user) | Optional | - |
| `updated_at` | `datetime` | Optional | The date on which the order was last updated |
| `tax_rate_1` | `float` | Optional | The regular tax rate |
| `tax_rate_2` | `float` | Optional | The reduced tax rate |
| `bill_bee_order_id` | `long\|int` | Optional | The Order.Id from the Billbee database |
| `bill_bee_parent_order_id` | `long\|int` | Optional | The Id of the parent order in the Billbee database |
| `vat_id` | `string` | Optional | The customers vat id |
| `tags` | `List of string` | Optional | The Tags of the order |
| `ship_weight_kg` | `float` | Optional | The total weight of the shipment(s) |
| `language_code` | `string` | Optional | The two-letter language code of the customer |
| `paid_amount` | `float` | Optional | - |
| `shipping_profile_id` | `string` | Optional | Internal Id for the shipping profile for that order |
| `shipping_provider_id` | `long\|int` | Optional | Internal Id for the used shipping provider |
| `shipping_provider_product_id` | `long\|int` | Optional | Internal Id for the used shipping product |
| `shipping_provider_name` | `string` | Optional | The Name for of used shipping provider |
| `shipping_provider_product_name` | `string` | Optional | The Name of the used shipping product |
| `shipping_profile_name` | `string` | Optional | Display Name of Shipping profile, if available |
| `payment_instruction` | `string` | Optional | A textfield optionaly filled with a payment instruction text for printout on the invoice (z.B. Ebay Kauf auf Rechnung) |
| `is_cancelation_for` | `string` | Optional | An optional Order Id (externalid) for an order if this is a cancel order (shopify only at the moment) |
| `payment_transaction_id` | `string` | Optional | The id of the payment transaction. For example the transaction id of PayPal payment. Should not be used any more. Please use 'Payments' instead. |
| `distribution_center` | `string` | Optional | An optional code for the distribution center delivering this order |
| `delivery_source_country_code` | `string` | Optional | An optional Country ISO2 Code of the country where order is shipped from (FBA) |
| `custom_invoice_note` | `string` | Optional | An optional multiline text which is printed on the invoice |
| `customer_number` | `string` | Optional | The customer number (not to be confused with the id of the customer) |
| `payment_reference` | `string` | Optional | A payment reference. Should not be used any more. Please use 'Payments' instead. |
| `shipping_services` | [`List of BillbeeInterfacesShippingProductService`](#billbee-interfaces-shipping-product-service) | Optional | Additional services for the shipment |
| `customer` | [`BillbeeInterfacesBillbeeAPIModelCustomerApiModel`](#billbee-interfaces-billbee-api-model-customer-api-model) | Optional | - |
| `history` | [`List of BillbeeInterfacesOrderHistoryEntry`](#billbee-interfaces-order-history-entry) | Optional | - |
| `payments` | [`List of BillbeeInterfacesBillbeeAPIModelsOrderPayment`](#billbee-interfaces-billbee-api-models-order-payment) | Optional | - |
| `last_modified_at` | `datetime` | Optional | Date of the last update, the order got |

##### Example (as JSON)

```json
{
  "RebateDifference": null,
  "ShippingIds": null,
  "AcceptLossOfReturnRight": null,
  "Id": null,
  "OrderNumber": null,
  "State": null,
  "VatMode": null,
  "CreatedAt": null,
  "ShippedAt": null,
  "ConfirmedAt": null,
  "PayedAt": null,
  "SellerComment": null,
  "Comments": null,
  "InvoiceNumberPrefix": null,
  "InvoiceNumberPostfix": null,
  "InvoiceNumber": null,
  "InvoiceDate": null,
  "InvoiceAddress": null,
  "ShippingAddress": null,
  "PaymentMethod": null,
  "ShippingCost": null,
  "TotalCost": null,
  "AdjustmentCost": null,
  "AdjustmentReason": null,
  "OrderItems": null,
  "Currency": null,
  "Seller": null,
  "Buyer": null,
  "UpdatedAt": null,
  "TaxRate1": null,
  "TaxRate2": null,
  "BillBeeOrderId": null,
  "BillBeeParentOrderId": null,
  "VatId": null,
  "Tags": null,
  "ShipWeightKg": null,
  "LanguageCode": null,
  "PaidAmount": null,
  "ShippingProfileId": null,
  "ShippingProviderId": null,
  "ShippingProviderProductId": null,
  "ShippingProviderName": null,
  "ShippingProviderProductName": null,
  "ShippingProfileName": null,
  "PaymentInstruction": null,
  "IsCancelationFor": null,
  "PaymentTransactionId": null,
  "DistributionCenter": null,
  "DeliverySourceCountryCode": null,
  "CustomInvoiceNote": null,
  "CustomerNumber": null,
  "PaymentReference": null,
  "ShippingServices": null,
  "Customer": null,
  "History": null,
  "Payments": null,
  "LastModifiedAt": null
}
```

#### Billbee Interfaces Billbee API Model Shipment

Represents a single shipment.

##### Class Name

`BillbeeInterfacesBillbeeAPIModelShipment`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billbee_id` | `long\|int` | Optional | The billbee internal id of the shipment |
| `shipping_id` | `string` | Optional | The id of this shipment |
| `shipper` | `string` | Optional | The name of the shipping provider |
| `created` | `datetime` | Optional | The creation date |
| `tracking_url` | `string` | Optional | The url to track this shipment |
| `shipping_provider_id` | `long\|int` | Optional | The id of the used shipping provider |
| `shipping_provider_product_id` | `long\|int` | Optional | The id of the used shipping provider product |
| `shipping_carrier` | `int` | Optional | The carrier used to ship the parcel with |

##### Example (as JSON)

```json
{
  "BillbeeId": null,
  "ShippingId": null,
  "Shipper": null,
  "Created": null,
  "TrackingUrl": null,
  "ShippingProviderId": null,
  "ShippingProviderProductId": null,
  "ShippingCarrier": null
}
```

#### Billbee Interfaces Billbee API Model Comment Api Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelCommentApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | - |
| `from_customer` | `bool` | Optional | - |
| `text` | `string` | Optional | - |
| `name` | `string` | Optional | - |
| `created` | `datetime` | Optional | - |

##### Example (as JSON)

```json
{
  "Id": null,
  "FromCustomer": null,
  "Text": null,
  "Name": null,
  "Created": null
}
```

#### Billbee Interfaces Billbee API Model Order Address Api Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelOrderAddressApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billbee_id` | `long\|int` | Optional | - |
| `first_name` | `string` | Optional | - |
| `last_name` | `string` | Optional | - |
| `company` | `string` | Optional | - |
| `name_addition` | `string` | Optional | - |
| `street` | `string` | Optional | - |
| `house_number` | `string` | Optional | - |
| `zip` | `string` | Optional | - |
| `city` | `string` | Optional | - |
| `country_iso_2` | `string` | Optional | - |
| `country` | `string` | Optional | - |
| `line_2` | `string` | Optional | - |
| `email` | `string` | Optional | - |
| `state` | `string` | Optional | - |
| `phone` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "BillbeeId": null,
  "FirstName": null,
  "LastName": null,
  "Company": null,
  "NameAddition": null,
  "Street": null,
  "HouseNumber": null,
  "Zip": null,
  "City": null,
  "CountryISO2": null,
  "Country": null,
  "Line2": null,
  "Email": null,
  "State": null,
  "Phone": null
}
```

#### Billbee Interfaces Billbee API Model Order Item

##### Class Name

`BillbeeInterfacesBillbeeAPIModelOrderItem`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billbee_id` | `long\|int` | Optional | The billbee id of this item |
| `transaction_id` | `string` | Optional | Id of the individual transaction. Only required by Ebay to detect aggregated orders |
| `product` | [`BillbeeInterfacesBillbeeAPIModelSoldProduct`](#billbee-interfaces-billbee-api-model-sold-product) | Optional | - |
| `quantity` | `float` | Optional | The sold quantity |
| `total_price` | `float` | Optional | The total price (unit price * quantity) |
| `tax_amount` | `float` | Optional | The tax amount in the total price |
| `tax_index` | `int` | Optional | The tax index. |
| `discount` | `float` | Optional | Sets the discount in percent |
| `attributes` | [`List of BillbeeInterfacesBillbeeAPIModelOrderItemAttribute`](#billbee-interfaces-billbee-api-model-order-item-attribute) | Optional | A list of product attributes for this position |
| `get_price_from_article_if_any` | `bool` | Optional | If true, the price will be overwritten by the known article price in billbee if available |
| `is_coupon` | `bool` | Optional | Determines if it is a coupon, which is interpreted as tax-free payment |
| `shipping_profile_id` | `string` | Optional | Determines if it is a coupon, which is interpreted as tax-free payment |
| `dont_adjust_stock` | `bool` | Optional | If true, the import of this order won't adjust the stock level at billbee. |
| `unrebated_total_price` | `float` | Optional | Is just used for the billbee api |
| `serial_number` | `string` | Optional | Contains the used serial number |

##### Example (as JSON)

```json
{
  "BillbeeId": null,
  "TransactionId": null,
  "Product": null,
  "Quantity": null,
  "TotalPrice": null,
  "TaxAmount": null,
  "TaxIndex": null,
  "Discount": null,
  "Attributes": null,
  "GetPriceFromArticleIfAny": null,
  "IsCoupon": null,
  "ShippingProfileId": null,
  "DontAdjustStock": null,
  "UnrebatedTotalPrice": null,
  "SerialNumber": null
}
```

#### Billbee Interfaces Billbee API Model Order User

##### Class Name

`BillbeeInterfacesBillbeeAPIModelOrderUser`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `platform` | `string` | Optional | The name of the platform from which this customer originated |
| `billbee_shop_name` | `string` | Optional | The name of shop connection in Billbee |
| `billbee_shop_id` | `long\|int` | Optional | The Billbee internal id of the shop connection |
| `id` | `string` | Optional | The Billbee internal id of this customer |
| `nick` | `string` | Optional | The nick name (if available) from the original system |
| `first_name` | `string` | Optional | The first name of this customer |
| `last_name` | `string` | Optional | The last name of this customer |
| `full_name` | `string` | Optional | The full name ("firstname lastname") of this customer |
| `email` | `string` | Optional | The email address of this customer |

##### Example (as JSON)

```json
{
  "Platform": null,
  "BillbeeShopName": null,
  "BillbeeShopId": null,
  "Id": null,
  "Nick": null,
  "FirstName": null,
  "LastName": null,
  "FullName": null,
  "Email": null
}
```

#### Billbee Interfaces Shipping Product Service

##### Class Name

`BillbeeInterfacesShippingProductService`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_name` | `string` | Optional | - |
| `display_value` | `string` | Optional | - |
| `requires_user_input` | `bool` | Optional | - |
| `service_name` | `string` | Optional | - |
| `type_name` | `string` | Optional | - |
| `possible_value_lists` | [`List of SystemCollectionsGenericKeyValuePairSystemStringSystemCollectionsGenericListSystemCollectionsGenericKeyValuePairSystemInt32SystemString`](#system-collections-generic-key-value-pair-system-string-system-collections-generic-list-system-collections-generic-key-value-pair-system-int-32-system-string) | Optional | - |
| `can_be_configured` | `bool` | Optional | - |

##### Example (as JSON)

```json
{
  "DisplayName": null,
  "DisplayValue": null,
  "RequiresUserInput": null,
  "ServiceName": null,
  "typeName": null,
  "PossibleValueLists": null,
  "CanBeConfigured": null
}
```

#### Billbee Interfaces Order History Entry

##### Class Name

`BillbeeInterfacesOrderHistoryEntry`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created` | `datetime` | Optional | - |
| `event_type_name` | `string` | Optional | - |
| `text` | `string` | Optional | - |
| `employee_name` | `string` | Optional | - |
| `type_id` | `int` | Optional | - |

##### Example (as JSON)

```json
{
  "Created": null,
  "EventTypeName": null,
  "Text": null,
  "EmployeeName": null,
  "TypeId": null
}
```

#### Billbee Interfaces Billbee API Models Order Payment

##### Class Name

`BillbeeInterfacesBillbeeAPIModelsOrderPayment`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billbee_id` | `long\|int` | Optional | - |
| `transaction_id` | `string` | Optional | - |
| `pay_date` | `datetime` | Optional | - |
| `payment_type` | `int` | Optional | - |
| `source_technology` | `string` | Optional | - |
| `source_text` | `string` | Optional | - |
| `pay_value` | `float` | Optional | - |
| `purpose` | `string` | Optional | - |
| `name` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "BillbeeId": null,
  "TransactionId": null,
  "PayDate": null,
  "PaymentType": null,
  "SourceTechnology": null,
  "SourceText": null,
  "PayValue": null,
  "Purpose": null,
  "Name": null
}
```

#### Billbee Interfaces Billbee API Model Sold Product

##### Class Name

`BillbeeInterfacesBillbeeAPIModelSoldProduct`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `old_id` | `string` | Optional | This is for migration scenarios when the internal id of a product changes<br>I.E. Etsy when switching to the new inventory management, the ids for variants will change. |
| `id` | `string` | Optional | The id of this product in the external system |
| `title` | `string` | Optional | The name of this product |
| `weight` | `int` | Optional | Weight of one item in gram |
| `sku` | `string` | Optional | The SKU of this product |
| `sku_or_id` | `string` | Optional | The SKU of this product or the id if the SKU is empty |
| `is_digital` | `bool` | Optional | True if the product is a digital good (download etc.), false if not |
| `images` | [`List of BillbeeInterfacesBillbeeAPIModelProductImage`](#billbee-interfaces-billbee-api-model-product-image) | Optional | The images of this product |
| `ean` | `string` | Optional | The EAN / GTIN of this product |
| `platform_data` | `string` | Optional | Optional platform specific Data as serialized JSON Object for the product |
| `taric_code` | `string` | Optional | The TARIC code |
| `country_of_origin` | `string` | Optional | The country where this article was made |
| `billbee_id` | `long\|int` | Optional | The Billbee internal id of the linked product |

##### Example (as JSON)

```json
{
  "OldId": null,
  "Id": null,
  "Title": null,
  "Weight": null,
  "SKU": null,
  "SkuOrId": null,
  "IsDigital": null,
  "Images": null,
  "EAN": null,
  "PlatformData": null,
  "TARICCode": null,
  "CountryOfOrigin": null,
  "BillbeeId": null
}
```

#### Billbee Interfaces Billbee API Model Order Item Attribute

##### Class Name

`BillbeeInterfacesBillbeeAPIModelOrderItemAttribute`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The internal id of this attribute |
| `name` | `string` | Optional | The attribute name. E.g. color |
| `value` | `string` | Optional | The attribute value. E.g. red |
| `price` | `float` | Optional | - |

##### Example (as JSON)

```json
{
  "Id": null,
  "Name": null,
  "Value": null,
  "Price": null
}
```

#### System Collections Generic Key Value Pair System String System Collections Generic List System Collections Generic Key Value Pair System Int 32 System String

##### Class Name

`SystemCollectionsGenericKeyValuePairSystemStringSystemCollectionsGenericListSystemCollectionsGenericKeyValuePairSystemInt32SystemString`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `string` | Optional | - |
| `value` | [`List of SystemCollectionsGenericKeyValuePairSystemInt32SystemString`](#system-collections-generic-key-value-pair-system-int-32-system-string) | Optional | - |

##### Example (as JSON)

```json
{
  "key": null,
  "value": null
}
```

#### Billbee Interfaces Billbee API Model Product Image

##### Class Name

`BillbeeInterfacesBillbeeAPIModelProductImage`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `string` | Optional | The url to the image |
| `is_default_image` | `bool` | Optional | True if the image is / should be the default image |
| `position` | `int` | Optional | The order of this image |
| `external_id` | `string` | Optional | The id of this image from the original system |

##### Example (as JSON)

```json
{
  "Url": null,
  "IsDefaultImage": null,
  "Position": null,
  "ExternalId": null
}
```

#### System Collections Generic Key Value Pair System Int 32 System String

##### Class Name

`SystemCollectionsGenericKeyValuePairSystemInt32SystemString`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `int` | Optional | - |
| `value` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "key": null,
  "value": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Result Billbee Interfaces Billbee API Model Order

##### Class Name

`RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`BillbeeInterfacesBillbeeAPIModelOrder`](#billbee-interfaces-billbee-api-model-order) | Optional | A class that represents the Billbee data model of a single order |

##### Example (as JSON)

```json
{
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Paged Result System Collections Generic List Billbee Interfaces Billbee API Model Order

##### Class Name

`RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelOrder`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `paging` | [`RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelOrder`](#rechnungsdruck-web-app-controllers-api-api-paged-result-paging-information-system-collections-generic-list-billbee-interfaces-billbee-api-model-order) | Optional | - |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`List of BillbeeInterfacesBillbeeAPIModelOrder`](#billbee-interfaces-billbee-api-model-order) | Optional | - |

##### Example (as JSON)

```json
{
  "Paging": null,
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Paged Result Paging Information System Collections Generic List Billbee Interfaces Billbee API Model Order

##### Class Name

`RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelOrder`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Optional | - |
| `total_pages` | `int` | Optional | - |
| `total_rows` | `int` | Optional | - |
| `page_size` | `int` | Optional | - |

##### Example (as JSON)

```json
{
  "Page": null,
  "TotalPages": null,
  "TotalRows": null,
  "PageSize": null
}
```

#### Rechnungsdruck Web App Controllers Api Order Tag Create

##### Class Name

`RechnungsdruckWebAppControllersApiOrderTagCreate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tags` | `List of string` | Optional | - |

##### Example (as JSON)

```json
{
  "Tags": null
}
```

#### Rechnungsdruck Web App Controllers Api Order State Update

Specifies the parameters used to set the new state of an order

##### Class Name

`RechnungsdruckWebAppControllersApiOrderStateUpdate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `new_state_id` | [`NewStateIdEnum`](#new-state-id) | Optional | The new state to set |

##### Example (as JSON)

```json
{
  "NewStateId": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Add Shipment to Order Model

Data of the shipment to be created

##### Class Name

`RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `shipping_id` | `string` | Optional | The id of the shipment (Sendungsnummer/trackingid) |
| `order_id` | `string` | Optional | Optional a differing order number of the shipment if available |
| `comment` | `string` | Optional | Optional a text stored with the shipment |
| `shipping_provider_id` | `long\|int` | Optional | Optional the id of a shipping provider existing in the billbee account that should be assigned to the shipment |
| `shipping_provider_product_id` | `long\|int` | Optional | Optional the id of a shipping provider product that should be assigend to the shipment |
| `carrier_id` | `int` | Optional | Optional the id of a shipping carrier that should be assigend to the shipment<br>Will override the carrier from the shipment product.<br>Please use the integer value from this Enumeration:<br>{Billbee.Interfaces.Shipping.Enums.ShippingCarrier} |

##### Example (as JSON)

```json
{
  "ShippingId": null,
  "OrderId": null,
  "Comment": null,
  "ShippingProviderId": null,
  "ShippingProviderProductId": null,
  "CarrierId": null
}
```

#### Rechnungsdruck Web App Controllers Api Order Api Controller Send Message Model

##### Class Name

`RechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `send_mode` | [`SendModeEnum`](#send-mode) | Optional | - |
| `subject` | [`List of BillbeeInterfacesOrderMultiLanguageString`](#billbee-interfaces-order-multi-language-string) | Optional | - |
| `body` | [`List of BillbeeInterfacesOrderMultiLanguageString`](#billbee-interfaces-order-multi-language-string) | Optional | - |
| `alternative_mail` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "SendMode": null,
  "Subject": null,
  "Body": null,
  "AlternativeMail": null
}
```

#### Rechnungsdruck Web App Controllers Api Order Api Controller Trigger Event Container

##### Class Name

`RechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Name of the event |
| `delay_in_minutes` | `int` | Optional | The delay in minutes until the rule is executed |

##### Example (as JSON)

```json
{
  "Name": null,
  "DelayInMinutes": null
}
```

#### Rechnungsdruck Web App Controllers Api Order Api Controller Parse Text Container

##### Class Name

`RechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text_to_parse` | `string` | Optional | The text to parse and replace the placeholders in. |
| `is_html` | `bool` | Optional | If true, the string will be handled as html. |
| `language` | `string` | Optional | The ISO 639-1 code of the target language. Using default if not set. |
| `trim` | `bool` | Optional | If true, then the placeholder values are trimmed after usage. |

##### Example (as JSON)

```json
{
  "TextToParse": null,
  "IsHtml": null,
  "Language": null,
  "Trim": null
}
```

#### Rechnungsdruck Web App Controllers Api Search Controller Search Model

##### Class Name

`RechnungsdruckWebAppControllersApiSearchControllerSearchModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `List of string` | Optional | - |
| `term` | `string` | Optional | - |
| `search_mode` | [`SearchModeEnum`](#search-mode) | Optional | - |

##### Example (as JSON)

```json
{
  "Type": null,
  "Term": null,
  "SearchMode": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Result Rechnungsdruck Web App Controllers Api Search Controller Search Results Model

##### Class Name

`RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`RechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel`](#rechnungsdruck-web-app-controllers-api-search-controller-search-results-model) | Optional | - |

##### Example (as JSON)

```json
{
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Rechnungsdruck Web App Controllers Api Search Controller Search Results Model

##### Class Name

`RechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `products` | [`List of RechnungsdruckWebAppControllersApiSearchControllerProductResult`](#rechnungsdruck-web-app-controllers-api-search-controller-product-result) | Optional | - |
| `orders` | [`List of RechnungsdruckWebAppControllersApiSearchControllerOrderResult`](#rechnungsdruck-web-app-controllers-api-search-controller-order-result) | Optional | - |
| `customers` | [`List of RechnungsdruckWebAppControllersApiSearchControllerCustomerResult`](#rechnungsdruck-web-app-controllers-api-search-controller-customer-result) | Optional | - |

##### Example (as JSON)

```json
{
  "Products": null,
  "Orders": null,
  "Customers": null
}
```

#### Rechnungsdruck Web App Controllers Api Search Controller Product Result

##### Class Name

`RechnungsdruckWebAppControllersApiSearchControllerProductResult`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | - |
| `short_text` | `string` | Optional | - |
| `sku` | `string` | Optional | - |
| `tags` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "Id": null,
  "ShortText": null,
  "SKU": null,
  "Tags": null
}
```

#### Rechnungsdruck Web App Controllers Api Search Controller Order Result

##### Class Name

`RechnungsdruckWebAppControllersApiSearchControllerOrderResult`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | - |
| `external_reference` | `string` | Optional | - |
| `buyer_name` | `string` | Optional | - |
| `invoice_number` | `string` | Optional | - |
| `customer_name` | `string` | Optional | - |
| `article_texts` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "Id": null,
  "ExternalReference": null,
  "BuyerName": null,
  "InvoiceNumber": null,
  "CustomerName": null,
  "ArticleTexts": null
}
```

#### Rechnungsdruck Web App Controllers Api Search Controller Customer Result

##### Class Name

`RechnungsdruckWebAppControllersApiSearchControllerCustomerResult`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | - |
| `name` | `string` | Optional | - |
| `addresses` | `string` | Optional | - |
| `number` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "Id": null,
  "Name": null,
  "Addresses": null,
  "Number": null
}
```

#### Billbee Interfaces Billbee API Model Create Shipment Api Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `provider_name` | `string` | Optional | The name of the provider as specified in the billbee account |
| `product_code` | `string` | Optional | The productcode to be used when creating the shipment. Values depends on the carrier used |
| `printer_name` | `string` | Optional | The name of a connected Cloudprinter to sent the label to |
| `printer_id_for_export_docs` | `long\|int` | Optional | The id of a connected Cloudprinter to sent the export docs to |
| `services` | [`List of BillbeeInterfacesShippingProductService`](#billbee-interfaces-shipping-product-service) | Optional | A list of services to be used when creating the shipment |
| `receiver_address` | [`BillbeeInterfacesBillbeeAPIModelShipmentAddressApiModel`](#billbee-interfaces-billbee-api-model-shipment-address-api-model) | Optional | - |
| `client_reference` | `string` | Optional | Optional specify a text to be included on the label. Not possible with all carriers |
| `customer_number` | `string` | Optional | Not used anymore |
| `weight_in_gram` | `float` | Optional | Optional specify the weight in gram of the shipment |
| `order_sum` | `float` | Optional | The value of the shipments content |
| `order_currency_code` | `string` | Optional | The Currency if the ordersum |
| `content` | `string` | Optional | Optional specify a text describing the content of the shipment. Used for export shipments |
| `ship_date` | `datetime` | Optional | Optional overwrite the shipdate to be transferred to the carrier |
| `shipping_carrier` | [`ShippingCarrierEnum`](#shipping-carrier) | Optional | - |
| `dimension` | [`BillbeeInterfacesShippingShipmentDataDimensions`](#billbee-interfaces-shipping-shipment-data-dimensions) | Optional | - |

##### Example (as JSON)

```json
{
  "ProviderName": null,
  "ProductCode": null,
  "PrinterName": null,
  "PrinterIdForExportDocs": null,
  "Services": null,
  "ReceiverAddress": null,
  "ClientReference": null,
  "CustomerNumber": null,
  "WeightInGram": null,
  "OrderSum": null,
  "OrderCurrencyCode": null,
  "Content": null,
  "ShipDate": null,
  "shippingCarrier": null,
  "Dimension": null
}
```

#### Billbee Interfaces Billbee API Model Shipment Address Api Model

##### Class Name

`BillbeeInterfacesBillbeeAPIModelShipmentAddressApiModel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company` | `string` | Optional | - |
| `first_name` | `string` | Optional | - |
| `last_name` | `string` | Optional | - |
| `name_2` | `string` | Optional | - |
| `street` | `string` | Optional | - |
| `housenumber` | `string` | Optional | - |
| `zip` | `string` | Optional | - |
| `city` | `string` | Optional | - |
| `country_code` | `string` | Optional | - |
| `country_code_iso_3` | `string` | Optional | - |
| `email` | `string` | Optional | - |
| `telephone` | `string` | Optional | - |
| `address_addition` | `string` | Optional | - |
| `is_export_country` | `bool` | Optional | - |
| `state` | `string` | Optional | - |
| `full_name` | `string` | Optional | - |
| `full_street` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "Company": null,
  "FirstName": null,
  "LastName": null,
  "Name2": null,
  "Street": null,
  "Housenumber": null,
  "Zip": null,
  "City": null,
  "CountryCode": null,
  "CountryCodeISO3": null,
  "Email": null,
  "Telephone": null,
  "AddressAddition": null,
  "IsExportCountry": null,
  "State": null,
  "FullName": null,
  "FullStreet": null
}
```

#### Billbee Interfaces Shipping Shipment Data Dimensions

##### Class Name

`BillbeeInterfacesShippingShipmentDataDimensions`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `length` | `float` | Optional | - |
| `width` | `float` | Optional | - |
| `height` | `float` | Optional | - |

##### Example (as JSON)

```json
{
  "length": null,
  "width": null,
  "height": null
}
```

#### Rechnungsdruck Web App Controllers Api Shipment With Label

##### Class Name

`RechnungsdruckWebAppControllersApiShipmentWithLabel`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `long\|int` | Optional | The Billbee internal id of the order to ship |
| `provider_id` | `long\|int` | Optional | The id of the provider. You can query all providers with the shippingproviders endpoint |
| `product_id` | `long\|int` | Optional | the id of the shipping provider product to be used |
| `change_state_to_send` | `bool` | Optional | Optional parameter to automatically change the orderstate to sent after creating the shipment |
| `printer_name` | `string` | Optional | Optional the name of a connected cloudprinter to send the label to |
| `weight_in_gram` | `int` | Optional | Optional the shipments weight in gram to override the calculated weight |
| `ship_date` | `datetime` | Optional | Optional specify the shipdate to be transmitted to the carrier |
| `client_reference` | `string` | Optional | Optional specify a reference text to be included on the label. Works not with all carriers |
| `dimension` | [`BillbeeInterfacesShippingShipmentDataDimensions`](#billbee-interfaces-shipping-shipment-data-dimensions) | Optional | - |

##### Example (as JSON)

```json
{
  "OrderId": null,
  "ProviderId": null,
  "ProductId": null,
  "ChangeStateToSend": null,
  "PrinterName": null,
  "WeightInGram": null,
  "ShipDate": null,
  "ClientReference": null,
  "Dimension": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Result Rechnungsdruck Web App Controllers Api Shipment With Label Result

##### Class Name

`RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiShipmentWithLabelResult`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`RechnungsdruckWebAppControllersApiShipmentWithLabelResult`](#rechnungsdruck-web-app-controllers-api-shipment-with-label-result) | Optional | - |

##### Example (as JSON)

```json
{
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Rechnungsdruck Web App Controllers Api Shipment With Label Result

##### Class Name

`RechnungsdruckWebAppControllersApiShipmentWithLabelResult`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `long\|int` | Optional | - |
| `order_reference` | `string` | Optional | - |
| `shipping_id` | `string` | Optional | - |
| `tracking_url` | `string` | Optional | - |
| `label_data_pdf` | `string` | Optional | - |
| `export_docs_pdf` | `string` | Optional | - |
| `carrier` | `string` | Optional | - |
| `shipping_date` | `datetime` | Optional | - |

##### Example (as JSON)

```json
{
  "OrderId": null,
  "OrderReference": null,
  "ShippingId": null,
  "TrackingUrl": null,
  "LabelDataPdf": null,
  "ExportDocsPdf": null,
  "Carrier": null,
  "ShippingDate": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Paged Result System Collections Generic List Billbee Interfaces Billbee API Model Shipment

##### Class Name

`RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelShipment`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `paging` | [`RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelShipment`](#rechnungsdruck-web-app-controllers-api-api-paged-result-paging-information-system-collections-generic-list-billbee-interfaces-billbee-api-model-shipment) | Optional | - |
| `error_message` | `string` | Optional | - |
| `error_code` | [`ErrorCodeEnum`](#error-code) | Optional | - |
| `data` | [`List of BillbeeInterfacesBillbeeAPIModelShipment`](#billbee-interfaces-billbee-api-model-shipment) | Optional | - |

##### Example (as JSON)

```json
{
  "Paging": null,
  "ErrorMessage": null,
  "ErrorCode": null,
  "Data": null
}
```

#### Rechnungsdruck Web App Controllers Api Api Paged Result Paging Information System Collections Generic List Billbee Interfaces Billbee API Model Shipment

##### Class Name

`RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelShipment`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Optional | - |
| `total_pages` | `int` | Optional | - |
| `total_rows` | `int` | Optional | - |
| `page_size` | `int` | Optional | - |

##### Example (as JSON)

```json
{
  "Page": null,
  "TotalPages": null,
  "TotalRows": null,
  "PageSize": null
}
```

#### Microsoft Asp Net Web Hooks Web Hook

##### Class Name

`MicrosoftAspNetWebHooksWebHook`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `web_hook_uri` | `string` | Required | - |
| `secret` | `string` | Optional | - |
| `description` | `string` | Optional | - |
| `is_paused` | `bool` | Optional | - |
| `filters` | `List of string` | Optional | - |
| `headers` | `dict` | Optional | - |
| `properties` | `dict` | Optional | - |

##### Example (as JSON)

```json
{
  "Id": null,
  "WebHookUri": "WebHookUri0",
  "Secret": null,
  "Description": null,
  "IsPaused": null,
  "Filters": null,
  "Headers": null,
  "Properties": null
}
```

### Enumerations

* [Address Type](#address-type)
* [Article Title Source](#article-title-source)
* [Default Vat Mode](#default-vat-mode)
* [Error Code](#error-code)
* [New State Id](#new-state-id)
* [Payment Method](#payment-method)
* [Search Mode](#search-mode)
* [Send Mode](#send-mode)
* [Shipping Carrier](#shipping-carrier)
* [State](#state)
* [Type](#type)
* [Type 1](#type-1)
* [Vat Mode](#vat-mode)

#### Address Type

The type of the address

##### Class Name

`AddressTypeEnum`

##### Fields

| Name |
|  --- |
| `ENUM_1` |
| `ENUM_2` |

#### Article Title Source

##### Class Name

`ArticleTitleSourceEnum`

##### Fields

| Name |
|  --- |
| `ENUM_0` |
| `ENUM_1` |
| `ENUM_2` |
| `ENUM_3` |

#### Default Vat Mode

Optionally specify the default vat mode of the user

##### Class Name

`DefaultVatModeEnum`

##### Fields

| Name |
|  --- |
| `ENUM_0` |
| `ENUM_1` |
| `ENUM_2` |
| `ENUM_3` |
| `ENUM_4` |
| `ENUM_5` |

#### Error Code

##### Class Name

`ErrorCodeEnum`

##### Fields

| Name |
|  --- |
| `ENUM_0` |
| `ENUM_1` |
| `ENUM_2` |
| `ENUM_3` |
| `ENUM_4` |
| `ENUM_5` |
| `ENUM_6` |
| `ENUM_7` |
| `ENUM_8` |
| `ENUM_9` |
| `ENUM_10` |
| `ENUM_11` |
| `ENUM_12` |
| `ENUM_13` |
| `ENUM_14` |
| `ENUM_15` |
| `ENUM_16` |
| `ENUM_17` |
| `ENUM_18` |
| `ENUM_19` |
| `ENUM_20` |
| `ENUM_21` |
| `ENUM_22` |
| `ENUM_23` |
| `ENUM_24` |
| `ENUM_25` |
| `ENUM_26` |
| `ENUM_27` |

#### New State Id

The new state to set

##### Class Name

`NewStateIdEnum`

##### Fields

| Name |
|  --- |
| `ENUM_1` |
| `ENUM_2` |
| `ENUM_3` |
| `ENUM_4` |
| `ENUM_5` |
| `ENUM_6` |
| `ENUM_7` |
| `ENUM_8` |
| `ENUM_9` |
| `ENUM_10` |
| `ENUM_11` |
| `ENUM_12` |
| `ENUM_13` |
| `ENUM_14` |
| `ENUM_15` |
| `ENUM_16` |

#### Payment Method

The payment method

##### Class Name

`PaymentMethodEnum`

##### Fields

| Name |
|  --- |
| `ENUM_1` |
| `ENUM_2` |
| `ENUM_3` |
| `ENUM_4` |
| `ENUM_6` |
| `ENUM_19` |
| `ENUM_20` |
| `ENUM_21` |
| `ENUM_22` |
| `ENUM_23` |
| `ENUM_24` |
| `ENUM_25` |
| `ENUM_26` |
| `ENUM_27` |
| `ENUM_28` |
| `ENUM_29` |
| `ENUM_30` |
| `ENUM_31` |
| `ENUM_32` |
| `ENUM_33` |
| `ENUM_34` |
| `ENUM_35` |
| `ENUM_36` |
| `ENUM_37` |
| `ENUM_38` |
| `ENUM_39` |
| `ENUM_40` |
| `ENUM_41` |
| `ENUM_42` |
| `ENUM_43` |
| `ENUM_44` |
| `ENUM_45` |
| `ENUM_46` |
| `ENUM_47` |
| `ENUM_48` |
| `ENUM_49` |
| `ENUM_50` |
| `ENUM_51` |
| `ENUM_52` |
| `ENUM_53` |
| `ENUM_54` |
| `ENUM_55` |
| `ENUM_56` |
| `ENUM_57` |
| `ENUM_58` |
| `ENUM_59` |
| `ENUM_60` |
| `ENUM_61` |
| `ENUM_62` |
| `ENUM_63` |
| `ENUM_64` |
| `ENUM_65` |
| `ENUM_66` |
| `ENUM_67` |
| `ENUM_68` |
| `ENUM_69` |
| `ENUM_70` |
| `ENUM_71` |
| `ENUM_72` |
| `ENUM_73` |
| `ENUM_74` |
| `ENUM_75` |
| `ENUM_76` |
| `ENUM_77` |
| `ENUM_78` |
| `ENUM_79` |
| `ENUM_80` |
| `ENUM_81` |
| `ENUM_82` |
| `ENUM_83` |
| `ENUM_84` |
| `ENUM_85` |
| `ENUM_86` |
| `ENUM_87` |
| `ENUM_88` |
| `ENUM_89` |
| `ENUM_90` |
| `ENUM_91` |
| `ENUM_92` |
| `ENUM_93` |
| `ENUM_94` |
| `ENUM_95` |
| `ENUM_96` |
| `ENUM_97` |
| `ENUM_98` |
| `ENUM_99` |
| `ENUM_100` |
| `ENUM_101` |
| `ENUM_102` |
| `ENUM_103` |
| `ENUM_104` |
| `ENUM_105` |
| `ENUM_106` |
| `ENUM_107` |
| `ENUM_108` |
| `ENUM_109` |
| `ENUM_110` |
| `ENUM_111` |
| `ENUM_112` |

#### Search Mode

##### Class Name

`SearchModeEnum`

##### Fields

| Name |
|  --- |
| `ENUM_0` |
| `ENUM_1` |
| `ENUM_2` |
| `ENUM_3` |
| `ENUM_4` |

#### Send Mode

##### Class Name

`SendModeEnum`

##### Fields

| Name |
|  --- |
| `ENUM_0` |
| `ENUM_1` |
| `ENUM_2` |
| `ENUM_3` |
| `ENUM_4` |

#### Shipping Carrier

##### Class Name

`ShippingCarrierEnum`

##### Fields

| Name |
|  --- |
| `ENUM_0` |
| `ENUM_1` |
| `ENUM_2` |
| `ENUM_3` |
| `ENUM_4` |
| `ENUM_5` |
| `ENUM_6` |
| `ENUM_7` |
| `ENUM_8` |
| `ENUM_9` |
| `ENUM_10` |
| `ENUM_11` |
| `ENUM_12` |
| `ENUM_13` |
| `ENUM_14` |
| `ENUM_15` |
| `ENUM_16` |
| `ENUM_17` |

#### State

The current state of the order

##### Class Name

`StateEnum`

##### Fields

| Name |
|  --- |
| `ENUM_1` |
| `ENUM_2` |
| `ENUM_3` |
| `ENUM_4` |
| `ENUM_5` |
| `ENUM_6` |
| `ENUM_7` |
| `ENUM_8` |
| `ENUM_9` |
| `ENUM_10` |
| `ENUM_11` |
| `ENUM_12` |
| `ENUM_13` |
| `ENUM_14` |
| `ENUM_15` |
| `ENUM_16` |

#### Type

##### Class Name

`TypeEnum`

##### Fields

| Name |
|  --- |
| `ENUM_0` |
| `ENUM_1` |
| `ENUM_2` |
| `ENUM_3` |

#### Type 1

##### Class Name

`Type1Enum`

##### Fields

| Name |
|  --- |
| `ENUM_0` |
| `ENUM_1` |
| `ENUM_2` |
| `ENUM_3` |
| `ENUM_4` |
| `ENUM_5` |

#### Vat Mode

The vat mode of the order

##### Class Name

`VatModeEnum`

##### Fields

| Name |
|  --- |
| `ENUM_0` |
| `ENUM_1` |
| `ENUM_2` |
| `ENUM_3` |
| `ENUM_4` |
| `ENUM_5` |

## Utility Classes Documentation

### ApiHelper

A utility class for processing API Calls. Also contains classes for supporting standard datetime formats.

#### Methods

| Name | Description |
|  --- | --- |
| json_deserialize | Deserializes a JSON string to a Python dictionary. |

#### Classes

| Name | Description |
|  --- | --- |
| HttpDateTime | A wrapper for datetime to support HTTP date format. |
| UnixDateTime | A wrapper for datetime to support Unix date format. |
| RFC3339DateTime | A wrapper for datetime to support RFC3339 format. |

## Common Code Documentation

### HttpResponse

Http response received.

#### Parameters

| Name | Type | Description |
|  --- | --- | --- |
| status_code | int | The status code returned by the server. |
| reason_phrase | str | The reason phrase returned by the server. |
| headers | dict | Response headers. |
| text | str | Response body. |
| request | HttpRequest | The request that resulted in this response. |

### HttpRequest

Represents a single Http Request.

#### Parameters

| Name | Type | Tag | Description |
|  --- | --- | --- | --- |
| http_method | HttpMethodEnum |  | The HTTP method of the request. |
| query_url | str |  | The endpoint URL for the API request. |
| headers | dict | optional | Request headers. |
| query_parameters | dict | optional | Query parameters to add in the URL. |
| parameters | dict &#124; str | optional | Request body, either as a serialized string or else a list of parameters to form encode. |
| files | dict | optional | Files to be sent with the request. |

