# Comments

Comments allow integrations to read and create comments on pages and blocks within Notion. Comments support rich text content and are associated with discussion threads.

Find out more here: [https://developers.notion.com/reference/comment-object](https://developers.notion.com/reference/comment-object)

```python
comments_api = client.comments
```

## Class Name

`CommentsApi`

## Methods

* [List Comments](../../doc/controllers/comments.md#list-comments)
* [Create Comment](../../doc/controllers/comments.md#create-comment)


# List Comments

Retrieves a list of unresolved comments from a page or block. Requires the integration to have read comment capabilities.

Find out more here: [https://developers.notion.com/reference/list-comments](https://developers.notion.com/reference/list-comments)

```python
def list_comments(self,
                 notion_version,
                 block_id,
                 start_cursor=None,
                 page_size=None)
```

## Authentication

This endpoint requires [bearerAuth](../../doc/auth/oauth-2-bearer-token.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Required | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests. |
| `block_id` | `uuid\|str` | Query, Required | The ID of the block or page to retrieve comments for. |
| `start_cursor` | `str` | Query, Optional | Pagination cursor to continue fetching results. |
| `page_size` | `int` | Query, Optional | Maximum number of comments to return (max 100).<br><br>**Constraints**: `<= 100` |

## Response Type

**200**: Comments successfully retrieved.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaginatedList`](../../doc/models/paginated-list.md).

## Example Usage

```python
notion_version = '2022-06-28'

block_id = '00000abc-0000-0000-0000-000000000000'

result = comments_api.list_comments(
    notion_version,
    block_id
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


# Create Comment

Creates a comment on a page or in an existing discussion thread. The integration must have comment capabilities to use this endpoint.

Find out more here: [https://developers.notion.com/reference/create-a-comment](https://developers.notion.com/reference/create-a-comment)

```python
def create_comment(self,
                  notion_version,
                  body)
```

## Authentication

This endpoint requires [bearerAuth](../../doc/auth/oauth-2-bearer-token.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Required | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests. |
| `body` | [`CommentsRequest`](../../doc/models/comments-request.md) | Body, Required | - |

## Response Type

**200**: Comment successfully created.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Comment`](../../doc/models/comment.md).

## Example Usage

```python
notion_version = '2022-06-28'

body = CommentsRequest(
    rich_text=[
        RichText(
            mtype=Type2.EQUATION,
            plain_text='plain_text4'
        )
    ]
)

result = comments_api.create_comment(
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

