# Databases

Databases are collections of Notion pages organized with a shared schema of properties. Each database defines columns (properties) that all its pages share. Databases support filtering, sorting, and querying. Use these endpoints to create, retrieve, update, and query databases.

Find out more here: [https://developers.notion.com/reference/database](https://developers.notion.com/reference/database)

```python
databases_api = client.databases
```

## Class Name

`DatabasesApi`

## Methods

* [Create Database](../../doc/controllers/databases.md#create-database)
* [Retrieve Database](../../doc/controllers/databases.md#retrieve-database)
* [Update Database](../../doc/controllers/databases.md#update-database)
* [Query Database](../../doc/controllers/databases.md#query-database)


# Create Database

Creates a database as a subpage of the specified parent page, with the specified properties schema. A database can be created with a title, properties defining the schema, and an optional description. The parent must be a page that the integration has access to.

Find out more here: [https://developers.notion.com/reference/create-a-database](https://developers.notion.com/reference/create-a-database)

```python
def create_database(self,
                   notion_version,
                   body)
```

## Authentication

This endpoint requires [bearerAuth](../../doc/auth/oauth-2-bearer-token.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Required | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests. |
| `body` | [`DatabasesRequest`](../../doc/models/databases-request.md) | Body, Required | - |

## Response Type

**200**: Database successfully created.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Database`](../../doc/models/database.md).

## Example Usage

```python
notion_version = '2022-06-28'

body = DatabasesRequest(
    parent=Parent(
        mtype=Type.BLOCK_ID
    ),
    properties={
        'key0': PropertySchema(),
        'key1': PropertySchema(),
        'key2': PropertySchema()
    }
)

result = databases_api.create_database(
    notion_version,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request was invalid or malformed. | [`ErrorException`](../../doc/models/error-exception.md) |
| 401 | The bearer token is missing, invalid, or the integration lacks access. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The requested resource does not exist or the integration lacks access to it. | [`ErrorException`](../../doc/models/error-exception.md) |
| 429 | The request has been rate limited. Notion enforces rate limits of 3 requests per second for integrations. Retry after the specified delay. | [`ErrorException`](../../doc/models/error-exception.md) |


# Retrieve Database

Retrieves a Database object using the ID specified in the path. Returns the database properties schema and metadata.

Find out more here: [https://developers.notion.com/reference/retrieve-a-database](https://developers.notion.com/reference/retrieve-a-database)

```python
def retrieve_database(self,
                     notion_version,
                     database_id)
```

## Authentication

This endpoint requires [bearerAuth](../../doc/auth/oauth-2-bearer-token.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Required | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests. |
| `database_id` | `uuid\|str` | Template, Required | The ID of the database to retrieve. |

## Response Type

**200**: Database successfully retrieved.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Database`](../../doc/models/database.md).

## Example Usage

```python
notion_version = '2022-06-28'

database_id = '0000206e-0000-0000-0000-000000000000'

result = databases_api.retrieve_database(
    notion_version,
    database_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | The bearer token is missing, invalid, or the integration lacks access. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The requested resource does not exist or the integration lacks access to it. | [`ErrorException`](../../doc/models/error-exception.md) |
| 429 | The request has been rate limited. Notion enforces rate limits of 3 requests per second for integrations. Retry after the specified delay. | [`ErrorException`](../../doc/models/error-exception.md) |


# Update Database

Updates an existing database's title, description, or properties schema. Only the fields specified in the request body will be updated. To remove a property from the schema, set its value to null.

Find out more here: [https://developers.notion.com/reference/update-a-database](https://developers.notion.com/reference/update-a-database)

```python
def update_database(self,
                   notion_version,
                   database_id,
                   body)
```

## Authentication

This endpoint requires [bearerAuth](../../doc/auth/oauth-2-bearer-token.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Required | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests. |
| `database_id` | `uuid\|str` | Template, Required | The ID of the database to update. |
| `body` | [`DatabasesRequest1`](../../doc/models/databases-request-1.md) | Body, Required | - |

## Response Type

**200**: Database successfully updated.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Database`](../../doc/models/database.md).

## Example Usage

```python
notion_version = '2022-06-28'

database_id = '0000206e-0000-0000-0000-000000000000'

body = DatabasesRequest1()

result = databases_api.update_database(
    notion_version,
    database_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request was invalid or malformed. | [`ErrorException`](../../doc/models/error-exception.md) |
| 401 | The bearer token is missing, invalid, or the integration lacks access. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The requested resource does not exist or the integration lacks access to it. | [`ErrorException`](../../doc/models/error-exception.md) |
| 429 | The request has been rate limited. Notion enforces rate limits of 3 requests per second for integrations. Retry after the specified delay. | [`ErrorException`](../../doc/models/error-exception.md) |


# Query Database

Gets a list of Pages and/or Databases contained in the database, filtered and ordered according to the filter and sort conditions specified in the request body. Responses are paginated and limited to 100 results per request.

Find out more here: [https://developers.notion.com/reference/post-database-query](https://developers.notion.com/reference/post-database-query)

```python
def query_database(self,
                  notion_version,
                  database_id,
                  filter_properties=None,
                  body=None)
```

## Authentication

This endpoint requires [bearerAuth](../../doc/auth/oauth-2-bearer-token.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Required | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests. |
| `database_id` | `uuid\|str` | Template, Required | The ID of the database to query. |
| `filter_properties` | `List[str]` | Query, Optional | A list of property IDs to include in the response. Only the specified properties will be returned for each page. |
| `body` | [`DatabasesQueryRequest`](../../doc/models/databases-query-request.md) | Body, Optional | - |

## Response Type

**200**: Database query results.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaginatedList`](../../doc/models/paginated-list.md).

## Example Usage

```python
notion_version = '2022-06-28'

database_id = '0000206e-0000-0000-0000-000000000000'

body = DatabasesQueryRequest(
    page_size=100
)

result = databases_api.query_database(
    notion_version,
    database_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request was invalid or malformed. | [`ErrorException`](../../doc/models/error-exception.md) |
| 401 | The bearer token is missing, invalid, or the integration lacks access. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The requested resource does not exist or the integration lacks access to it. | [`ErrorException`](../../doc/models/error-exception.md) |
| 429 | The request has been rate limited. Notion enforces rate limits of 3 requests per second for integrations. Retry after the specified delay. | [`ErrorException`](../../doc/models/error-exception.md) |

