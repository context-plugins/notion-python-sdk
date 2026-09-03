<!-- Generated file — do not edit; regenerated with the SDK. -->

# Client — operations

Accessor: `client` · Source: `notion_api/client.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.append_block_children

- **Route**: `PATCH /blocks/{block_id}/children`
- **Auth**: `bearer_auth`
- **Signature**: `def append_block_children(block_id: UUID, body: BlocksChildrenRequest | BlocksChildrenRequestDict, *, notion_version: str = "2022-06-28", request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `block_id`, `body`
- **Params**: `block_id` — path · `notion_version` — header `Notion-Version` · `body` — JSON body
- **Returns (parsed)**: `PaginatedList`
- **Returns (raw)**: `ApiResult[PaginatedList, AppendBlockChildrenErrorBody]`
- **Error**: `AppendBlockChildrenErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BlocksChildrenRequest` | `notion_api/models/blocks_children_request.py` |
| `BlocksChildrenRequestDict` | `notion_api/models/blocks_children_request.py` |
| `PaginatedList` | `notion_api/models/paginated_list.py` |
| `AppendBlockChildrenErrorBody` | `notion_api/errors/append_block_children_error.py` |
| `Error` | `notion_api/models/error.py` |

### client.delete_block

- **Route**: `DELETE /blocks/{block_id}`
- **Auth**: `bearer_auth`
- **Signature**: `def delete_block(block_id: UUID, *, notion_version: str = "2022-06-28", request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `block_id`
- **Params**: `block_id` — path · `notion_version` — header `Notion-Version`
- **Returns (parsed)**: `Block`
- **Returns (raw)**: `ApiResult[Block, DeleteBlockErrorBody]`
- **Error**: `DeleteBlockErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 404, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Block` | `notion_api/models/block.py` |
| `DeleteBlockErrorBody` | `notion_api/errors/delete_block_error.py` |
| `Error` | `notion_api/models/error.py` |

### client.retrieve_block

- **Route**: `GET /blocks/{block_id}`
- **Auth**: `bearer_auth`
- **Signature**: `def retrieve_block(block_id: UUID, *, notion_version: str = "2022-06-28", request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `block_id`
- **Params**: `block_id` — path · `notion_version` — header `Notion-Version`
- **Returns (parsed)**: `Block`
- **Returns (raw)**: `ApiResult[Block, RetrieveBlockErrorBody]`
- **Error**: `RetrieveBlockErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 404, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Block` | `notion_api/models/block.py` |
| `RetrieveBlockErrorBody` | `notion_api/errors/retrieve_block_error.py` |
| `Error` | `notion_api/models/error.py` |

### client.retrieve_block_children

- **Route**: `GET /blocks/{block_id}/children`
- **Auth**: `bearer_auth`
- **Signature**: `def retrieve_block_children(block_id: UUID, *, start_cursor: str | None = None, page_size: int | None = None, notion_version: str = "2022-06-28", request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `block_id`
- **Params**: `block_id` — path · `start_cursor` — query · `page_size` — query · `notion_version` — header `Notion-Version`
- **Returns (parsed)**: `PaginatedList`
- **Returns (raw)**: `ApiResult[PaginatedList, RetrieveBlockChildrenErrorBody]`
- **Error**: `RetrieveBlockChildrenErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 404, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaginatedList` | `notion_api/models/paginated_list.py` |
| `RetrieveBlockChildrenErrorBody` | `notion_api/errors/retrieve_block_children_error.py` |
| `Error` | `notion_api/models/error.py` |

### client.update_block

- **Route**: `PATCH /blocks/{block_id}`
- **Auth**: `bearer_auth`
- **Signature**: `def update_block(block_id: UUID, body: BlocksRequest | BlocksRequestDict, *, notion_version: str = "2022-06-28", request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `block_id`, `body`
- **Params**: `block_id` — path · `notion_version` — header `Notion-Version` · `body` — JSON body
- **Returns (parsed)**: `Block`
- **Returns (raw)**: `ApiResult[Block, UpdateBlockErrorBody]`
- **Error**: `UpdateBlockErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BlocksRequest` | `notion_api/models/blocks_request.py` |
| `BlocksRequestDict` | `notion_api/models/blocks_request.py` |
| `Block` | `notion_api/models/block.py` |
| `UpdateBlockErrorBody` | `notion_api/errors/update_block_error.py` |
| `Error` | `notion_api/models/error.py` |

