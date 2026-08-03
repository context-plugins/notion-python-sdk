# Users

Users represent people or bots in a Notion workspace. Person users are human members of the workspace, while bot users represent API integrations. Use these endpoints to list users, retrieve specific users, or get information about the current bot integration.

Find out more here: [https://developers.notion.com/reference/user](https://developers.notion.com/reference/user)

```python
users_api = client.users
```

## Class Name

`UsersApi`

## Methods

* [List Users](../../doc/controllers/users.md#list-users)
* [Retrieve User](../../doc/controllers/users.md#retrieve-user)
* [Retrieve Bot User](../../doc/controllers/users.md#retrieve-bot-user)


# List Users

Returns a paginated list of Users for the workspace. Guest users are not included. The response may include person users and bot users. Results are paginated with a maximum of 100 users per request.

Find out more here: [https://developers.notion.com/reference/get-users](https://developers.notion.com/reference/get-users)

```python
def list_users(self,
              notion_version,
              start_cursor=None,
              page_size=None)
```

## Authentication

This endpoint requires [bearerAuth](../../doc/auth/oauth-2-bearer-token.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Required | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests. |
| `start_cursor` | `str` | Query, Optional | Pagination cursor to continue fetching results. |
| `page_size` | `int` | Query, Optional | Maximum number of users to return (max 100).<br><br>**Constraints**: `<= 100` |

## Response Type

**200**: Users successfully retrieved.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaginatedList`](../../doc/models/paginated-list.md).

## Example Usage

```python
notion_version = '2022-06-28'

result = users_api.list_users(notion_version)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | The bearer token is missing, invalid, or the integration lacks access. | [`ErrorException`](../../doc/models/error-exception.md) |
| 429 | The request has been rate limited. Notion enforces rate limits of 3 requests per second for integrations. Retry after the specified delay. | [`ErrorException`](../../doc/models/error-exception.md) |


# Retrieve User

Retrieves a User object using the ID specified in the path. Returns user details including name, avatar, and type (person or bot).

Find out more here: [https://developers.notion.com/reference/get-user](https://developers.notion.com/reference/get-user)

```python
def retrieve_user(self,
                 notion_version,
                 user_id)
```

## Authentication

This endpoint requires [bearerAuth](../../doc/auth/oauth-2-bearer-token.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Required | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests. |
| `user_id` | `uuid\|str` | Template, Required | The ID of the user to retrieve. |

## Response Type

**200**: User successfully retrieved.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`User`](../../doc/models/user.md).

## Example Usage

```python
notion_version = '2022-06-28'

user_id = '00001e80-0000-0000-0000-000000000000'

result = users_api.retrieve_user(
    notion_version,
    user_id
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


# Retrieve Bot User

Retrieves the bot User associated with the current API token. Returns information about the integration including its name, owner, and the workspace it belongs to.

Find out more here: [https://developers.notion.com/reference/get-self](https://developers.notion.com/reference/get-self)

```python
def retrieve_bot_user(self,
                     notion_version)
```

## Authentication

This endpoint requires [bearerAuth](../../doc/auth/oauth-2-bearer-token.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Required | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests. |

## Response Type

**200**: Bot user successfully retrieved.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`User`](../../doc/models/user.md).

## Example Usage

```python
notion_version = '2022-06-28'

result = users_api.retrieve_bot_user(notion_version)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | The bearer token is missing, invalid, or the integration lacks access. | [`ErrorException`](../../doc/models/error-exception.md) |
| 429 | The request has been rate limited. Notion enforces rate limits of 3 requests per second for integrations. Retry after the specified delay. | [`ErrorException`](../../doc/models/error-exception.md) |

