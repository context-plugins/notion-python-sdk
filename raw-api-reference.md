# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [NotionApiClient](notion_api/client.py)

<details>
<summary><code>def append_block_children(block_id: UUID, body: BlocksChildrenRequest | BlocksChildrenRequestDict, *, notion_version: str = "2022-06-28", request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaginatedList, AppendBlockChildrenErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates and appends new children blocks to the parent block specified by block_id. Returns the updated parent block. Blocks can be appended to pages, or to other blocks that support children. The maximum number of blocks that can be appended in a single request is 100.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.append_block_children(block_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaginatedList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AppendBlockChildrenErrorBody
```

**Async**

```python
result = await async_client.with_raw_response.append_block_children(block_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaginatedList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AppendBlockChildrenErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>block_id</code> | <code>UUID</code> | The ID of the block to append children to. This can be a page ID to add content to a page. |
| <code>body</code> | <code>[BlocksChildrenRequest](notion_api/models/blocks_children_request.py) \| [BlocksChildrenRequestDict](notion_api/models/blocks_children_request.py)</code> | The request body. |
| <code>notion_version</code> | <code>str</code> | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests.<br>**Default**: <code>"2022-06-28"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](notion_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](notion_api/core/results.py)&#91;[PaginatedList](notion_api/models/paginated_list.py), [AppendBlockChildrenErrorBody](notion_api/errors/append_block_children_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaginatedList](notion_api/models/paginated_list.py)</code> -- Block children successfully appended.

**On `Failure`**: `error` is <code>[AppendBlockChildrenErrorBody](notion_api/errors/append_block_children_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 404, 429 | <code>[Error](notion_api/models/error.py)</code> |
| anything unmapped | <code>[RawError](notion_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_block(block_id: UUID, *, notion_version: str = "2022-06-28", request_options: RequestOptionsOrDict | None = None) -> ApiResult[Block, DeleteBlockErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sets a Block object, including page blocks, to archived: true using the ID specified in the path. This is equivalent to trashing the block in the Notion UI. To restore an archived block, use the update block endpoint to set archived to false.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.delete_block(block_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Block
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteBlockErrorBody
```

**Async**

```python
result = await async_client.with_raw_response.delete_block(block_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Block
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteBlockErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>block_id</code> | <code>UUID</code> | The ID of the block to delete (archive). |
| <code>notion_version</code> | <code>str</code> | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests.<br>**Default**: <code>"2022-06-28"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](notion_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](notion_api/core/results.py)&#91;[Block](notion_api/models/block.py), [DeleteBlockErrorBody](notion_api/errors/delete_block_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Block](notion_api/models/block.py)</code> -- Block successfully deleted (archived).

**On `Failure`**: `error` is <code>[DeleteBlockErrorBody](notion_api/errors/delete_block_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 404, 429 | <code>[Error](notion_api/models/error.py)</code> |
| anything unmapped | <code>[RawError](notion_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_block(block_id: UUID, *, notion_version: str = "2022-06-28", request_options: RequestOptionsOrDict | None = None) -> ApiResult[Block, RetrieveBlockErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a Block object using the ID specified in the path. If the block is a page, the page properties will be returned. The block's children are not included; use the retrieve block children endpoint to get them.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.retrieve_block(block_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Block
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RetrieveBlockErrorBody
```

**Async**

```python
result = await async_client.with_raw_response.retrieve_block(block_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Block
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RetrieveBlockErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>block_id</code> | <code>UUID</code> | The ID of the block to retrieve. |
| <code>notion_version</code> | <code>str</code> | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests.<br>**Default**: <code>"2022-06-28"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](notion_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](notion_api/core/results.py)&#91;[Block](notion_api/models/block.py), [RetrieveBlockErrorBody](notion_api/errors/retrieve_block_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Block](notion_api/models/block.py)</code> -- Block successfully retrieved.

**On `Failure`**: `error` is <code>[RetrieveBlockErrorBody](notion_api/errors/retrieve_block_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 404, 429 | <code>[Error](notion_api/models/error.py)</code> |
| anything unmapped | <code>[RawError](notion_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_block_children(block_id: UUID, *, start_cursor: str | None = None, page_size: int | None = None, notion_version: str = "2022-06-28", request_options: RequestOptionsOrDict | None = None) -> ApiResult[PaginatedList, RetrieveBlockChildrenErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a paginated array of child block objects contained in the block using the ID specified. This is used to read page content by passing a page ID as the block_id. Responses include a maximum of 100 blocks per request and are returned in the order they appear in the parent block.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.retrieve_block_children(block_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaginatedList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RetrieveBlockChildrenErrorBody
```

**Async**

```python
result = await async_client.with_raw_response.retrieve_block_children(block_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PaginatedList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RetrieveBlockChildrenErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>block_id</code> | <code>UUID</code> | The ID of the block whose children to retrieve. This can be a page ID to retrieve page content. |
| <code>start_cursor</code> | <code>str \| None</code> | Pagination cursor to continue fetching results.<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>int \| None</code> | Maximum number of blocks to return (max 100).<br>**Default**: <code>None</code> |
| <code>notion_version</code> | <code>str</code> | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests.<br>**Default**: <code>"2022-06-28"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](notion_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](notion_api/core/results.py)&#91;[PaginatedList](notion_api/models/paginated_list.py), [RetrieveBlockChildrenErrorBody](notion_api/errors/retrieve_block_children_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[PaginatedList](notion_api/models/paginated_list.py)</code> -- Block children successfully retrieved.

**On `Failure`**: `error` is <code>[RetrieveBlockChildrenErrorBody](notion_api/errors/retrieve_block_children_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 404, 429 | <code>[Error](notion_api/models/error.py)</code> |
| anything unmapped | <code>[RawError](notion_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_block(block_id: UUID, body: BlocksRequest | BlocksRequestDict, *, notion_version: str = "2022-06-28", request_options: RequestOptionsOrDict | None = None) -> ApiResult[Block, UpdateBlockErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the content of a block. The fields that can be updated depend on the block type. Blocks can also be archived by setting the archived field to true.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.update_block(block_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Block
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateBlockErrorBody
```

**Async**

```python
result = await async_client.with_raw_response.update_block(block_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Block
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateBlockErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>block_id</code> | <code>UUID</code> | The ID of the block to update. |
| <code>body</code> | <code>[BlocksRequest](notion_api/models/blocks_request.py) \| [BlocksRequestDict](notion_api/models/blocks_request.py)</code> | The request body. |
| <code>notion_version</code> | <code>str</code> | The version of the Notion API to use. The current version is 2022-06-28. This header is required for all API requests.<br>**Default**: <code>"2022-06-28"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](notion_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](notion_api/core/results.py)&#91;[Block](notion_api/models/block.py), [UpdateBlockErrorBody](notion_api/errors/update_block_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Block](notion_api/models/block.py)</code> -- Block successfully updated.

**On `Failure`**: `error` is <code>[UpdateBlockErrorBody](notion_api/errors/update_block_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 404, 429 | <code>[Error](notion_api/models/error.py)</code> |
| anything unmapped | <code>[RawError](notion_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

