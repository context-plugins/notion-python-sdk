# Blocks

Blocks are the fundamental units of content in Notion. Every page is composed of blocks, which can be paragraphs, headings, images, tables, lists, and many other types. Blocks can have children, forming a tree structure. Use these endpoints to retrieve, update, delete blocks and manage block children.

Find out more here: [https://developers.notion.com/reference/block](https://developers.notion.com/reference/block)

```python
blocks_api = client.blocks
```

## Class Name

`BlocksApi`

## Methods

* [Retrieve Block](../../doc/controllers/blocks.md#retrieve-block)
* [Update Block](../../doc/controllers/blocks.md#update-block)
* [Delete Block](../../doc/controllers/blocks.md#delete-block)
* [Retrieve Block Children](../../doc/controllers/blocks.md#retrieve-block-children)
* [Append Block Children](../../doc/controllers/blocks.md#append-block-children)


# Retrieve Block

Retrieves a Block object using the ID specified in the path. If the block is a page, the page properties will be returned. The block's children are not included; use the retrieve block children endpoint to get them.

Find out more here: [https://developers.notion.com/reference/retrieve-a-block](https://developers.notion.com/reference/retrieve-a-block)

```python
def retrieve_block(self,
                  notion_version,
                  block_id)
```

## Authentication

This endpoint requires [bearerAuth](../../doc/auth/oauth-2-bearer-token.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Required | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests. |
| `block_id` | `uuid\|str` | Template, Required | The ID of the block to retrieve. |

## Response Type

**200**: Block successfully retrieved.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Block`](../../doc/models/block.md).

## Example Usage

```python
notion_version = '2022-06-28'

block_id = '00000abc-0000-0000-0000-000000000000'

result = blocks_api.retrieve_block(
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


# Update Block

Updates the content of a block. The fields that can be updated depend on the block type. Blocks can also be archived by setting the archived field to true.

Find out more here: [https://developers.notion.com/reference/update-a-block](https://developers.notion.com/reference/update-a-block)

```python
def update_block(self,
                notion_version,
                block_id,
                body)
```

## Authentication

This endpoint requires [bearerAuth](../../doc/auth/oauth-2-bearer-token.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Required | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests. |
| `block_id` | `uuid\|str` | Template, Required | The ID of the block to update. |
| `body` | [`BlocksRequest`](../../doc/models/blocks-request.md) | Body, Required | - |

## Response Type

**200**: Block successfully updated.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Block`](../../doc/models/block.md).

## Example Usage

```python
notion_version = '2022-06-28'

block_id = '00000abc-0000-0000-0000-000000000000'

body = BlocksRequest()

result = blocks_api.update_block(
    notion_version,
    block_id,
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


# Delete Block

Sets a Block object, including page blocks, to archived: true using the ID specified in the path. This is equivalent to trashing the block in the Notion UI. To restore an archived block, use the update block endpoint to set archived to false.

Find out more here: [https://developers.notion.com/reference/delete-a-block](https://developers.notion.com/reference/delete-a-block)

```python
def delete_block(self,
                notion_version,
                block_id)
```

## Authentication

This endpoint requires [bearerAuth](../../doc/auth/oauth-2-bearer-token.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Required | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests. |
| `block_id` | `uuid\|str` | Template, Required | The ID of the block to delete (archive). |

## Response Type

**200**: Block successfully deleted (archived).

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Block`](../../doc/models/block.md).

## Example Usage

```python
notion_version = '2022-06-28'

block_id = '00000abc-0000-0000-0000-000000000000'

result = blocks_api.delete_block(
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


# Retrieve Block Children

Returns a paginated array of child block objects contained in the block using the ID specified. This is used to read page content by passing a page ID as the block_id. Responses include a maximum of 100 blocks per request and are returned in the order they appear in the parent block.

Find out more here: [https://developers.notion.com/reference/get-block-children](https://developers.notion.com/reference/get-block-children)

```python
def retrieve_block_children(self,
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
| `block_id` | `uuid\|str` | Template, Required | The ID of the block whose children to retrieve. This can be a page ID to retrieve page content. |
| `start_cursor` | `str` | Query, Optional | Pagination cursor to continue fetching results. |
| `page_size` | `int` | Query, Optional | Maximum number of blocks to return (max 100).<br><br>**Constraints**: `<= 100` |

## Response Type

**200**: Block children successfully retrieved.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaginatedList`](../../doc/models/paginated-list.md).

## Example Usage

```python
notion_version = '2022-06-28'

block_id = '00000abc-0000-0000-0000-000000000000'

result = blocks_api.retrieve_block_children(
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


# Append Block Children

Creates and appends new children blocks to the parent block specified by block_id. Returns the updated parent block. Blocks can be appended to pages, or to other blocks that support children. The maximum number of blocks that can be appended in a single request is 100.

Find out more here: [https://developers.notion.com/reference/patch-block-children](https://developers.notion.com/reference/patch-block-children)

```python
def append_block_children(self,
                         notion_version,
                         block_id,
                         body)
```

## Authentication

This endpoint requires [bearerAuth](../../doc/auth/oauth-2-bearer-token.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Required | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests. |
| `block_id` | `uuid\|str` | Template, Required | The ID of the block to append children to. This can be a page ID to add content to a page. |
| `body` | [`BlocksChildrenRequest`](../../doc/models/blocks-children-request.md) | Body, Required | - |

## Response Type

**200**: Block children successfully appended.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaginatedList`](../../doc/models/paginated-list.md).

## Example Usage

```python
notion_version = '2022-06-28'

block_id = '00000abc-0000-0000-0000-000000000000'

body = BlocksChildrenRequest(
    children=[
        Block(
            object=Object1.BLOCK,
            id='000003b4-0000-0000-0000-000000000000',
            mtype=Type1.TO_DO,
            created_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            last_edited_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            has_children=False
        )
    ]
)

result = blocks_api.append_block_children(
    notion_version,
    block_id,
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

