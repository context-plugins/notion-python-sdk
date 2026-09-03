from __future__ import annotations

from functools import cached_property
from types import TracebackType
from uuid import UUID, uuid4

from typing_extensions import Self

from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseNotionApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiResult,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncRawClient,
    BearerAuthScheme,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    no_auth,
    param,
)
from .errors.append_block_children_error import AppendBlockChildrenErrorBody, append_block_children_error_mapper
from .errors.delete_block_error import DeleteBlockErrorBody, delete_block_error_mapper
from .errors.retrieve_block_children_error import RetrieveBlockChildrenErrorBody, retrieve_block_children_error_mapper
from .errors.retrieve_block_error import RetrieveBlockErrorBody, retrieve_block_error_mapper
from .errors.update_block_error import UpdateBlockErrorBody, update_block_error_mapper
from .models.block import Block
from .models.blocks_children_request import BlocksChildrenRequest, BlocksChildrenRequestDict
from .models.blocks_request import BlocksRequest, BlocksRequestDict
from .models.paginated_list import PaginatedList
from .server.server import Server


class AsyncNotionApiClient(BaseNotionApiClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        bearer_auth: str | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            global_headers=[
                param[str]("User-Agent", "NotionApiClient/0.1.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "0.1.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(bearer_auth=BearerAuthScheme(bearer_auth) if bearer_auth is not None else no_auth)

    @cached_property
    def with_raw_response(self) -> AsyncApiWithRawResponse:
        return AsyncApiWithRawResponse(self._raw_client, self._server, self._auth)

    async def append_block_children(
        self,
        block_id: UUID,
        body: BlocksChildrenRequest | BlocksChildrenRequestDict,
        *,
        notion_version: str = "2022-06-28",
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaginatedList:
        """Creates and appends new children blocks to the parent block specified by block_id. Returns the updated parent
        block. Blocks can be appended to pages, or to other blocks that support children. The maximum number of blocks
        that can be appended in a single request is 100.

        Args:
            block_id: The ID of the block to append children to. This can be a page ID to add content to a page.
            body: The request body.
            notion_version: The version of the Notion API to use. The current version is 2022-06-28. This header is
                required for all API requests.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Block children successfully appended.

        Raises:
            ApiError: The request was invalid or malformed. The bearer token is missing, invalid, or the integration
                lacks access. The requested resource does not exist or the integration lacks access to it. The request
                has been rate limited. Notion enforces rate limits of 3 requests per second for integrations. Retry
                after the specified delay. ``error`` is ``Error | RawError``."""
        return (
            await self.with_raw_response.append_block_children(
                block_id, body, notion_version=notion_version, request_options=request_options
            )
        ).unwrap()

    async def delete_block(
        self, block_id: UUID, *, notion_version: str = "2022-06-28", request_options: RequestOptionsOrDict | None = None
    ) -> Block:
        """Sets a Block object, including page blocks, to archived: true using the ID specified in the path. This is
        equivalent to trashing the block in the Notion UI. To restore an archived block, use the update block endpoint
        to set archived to false.

        Args:
            block_id: The ID of the block to delete (archive).
            notion_version: The version of the Notion API to use. The current version is 2022-06-28. This header is
                required for all API requests.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Block successfully deleted (archived).

        Raises:
            ApiError: The bearer token is missing, invalid, or the integration lacks access. The requested resource does
                not exist or the integration lacks access to it. The request has been rate limited. Notion enforces rate
                limits of 3 requests per second for integrations. Retry after the specified delay. ``error`` is ``Error
                | RawError``."""
        return (
            await self.with_raw_response.delete_block(
                block_id, notion_version=notion_version, request_options=request_options
            )
        ).unwrap()

    async def retrieve_block(
        self, block_id: UUID, *, notion_version: str = "2022-06-28", request_options: RequestOptionsOrDict | None = None
    ) -> Block:
        """Retrieves a Block object using the ID specified in the path. If the block is a page, the page properties will
        be returned. The block's children are not included; use the retrieve block children endpoint to get them.

        Args:
            block_id: The ID of the block to retrieve.
            notion_version: The version of the Notion API to use. The current version is 2022-06-28. This header is
                required for all API requests.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Block successfully retrieved.

        Raises:
            ApiError: The bearer token is missing, invalid, or the integration lacks access. The requested resource does
                not exist or the integration lacks access to it. The request has been rate limited. Notion enforces rate
                limits of 3 requests per second for integrations. Retry after the specified delay. ``error`` is ``Error
                | RawError``."""
        return (
            await self.with_raw_response.retrieve_block(
                block_id, notion_version=notion_version, request_options=request_options
            )
        ).unwrap()

    async def retrieve_block_children(
        self,
        block_id: UUID,
        *,
        start_cursor: str | None = None,
        page_size: int | None = None,
        notion_version: str = "2022-06-28",
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaginatedList:
        """Returns a paginated array of child block objects contained in the block using the ID specified. This is used
        to read page content by passing a page ID as the block_id. Responses include a maximum of 100 blocks per request
        and are returned in the order they appear in the parent block.

        Args:
            block_id: The ID of the block whose children to retrieve. This can be a page ID to retrieve page content.
            start_cursor: Pagination cursor to continue fetching results.
            page_size: Maximum number of blocks to return (max 100).
            notion_version: The version of the Notion API to use. The current version is 2022-06-28. This header is
                required for all API requests.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Block children successfully retrieved.

        Raises:
            ApiError: The bearer token is missing, invalid, or the integration lacks access. The requested resource does
                not exist or the integration lacks access to it. The request has been rate limited. Notion enforces rate
                limits of 3 requests per second for integrations. Retry after the specified delay. ``error`` is ``Error
                | RawError``."""
        return (
            await self.with_raw_response.retrieve_block_children(
                block_id,
                start_cursor=start_cursor,
                page_size=page_size,
                notion_version=notion_version,
                request_options=request_options,
            )
        ).unwrap()

    async def update_block(
        self,
        block_id: UUID,
        body: BlocksRequest | BlocksRequestDict,
        *,
        notion_version: str = "2022-06-28",
        request_options: RequestOptionsOrDict | None = None,
    ) -> Block:
        """Updates the content of a block. The fields that can be updated depend on the block type. Blocks can also be
        archived by setting the archived field to true.

        Args:
            block_id: The ID of the block to update.
            body: The request body.
            notion_version: The version of the Notion API to use. The current version is 2022-06-28. This header is
                required for all API requests.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Block successfully updated.

        Raises:
            ApiError: The request was invalid or malformed. The bearer token is missing, invalid, or the integration
                lacks access. The requested resource does not exist or the integration lacks access to it. The request
                has been rate limited. Notion enforces rate limits of 3 requests per second for integrations. Retry
                after the specified delay. ``error`` is ``Error | RawError``."""
        return (
            await self.with_raw_response.update_block(
                block_id, body, notion_version=notion_version, request_options=request_options
            )
        ).unwrap()

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


class AsyncApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def append_block_children(
        self,
        block_id: UUID,
        body: BlocksChildrenRequest | BlocksChildrenRequestDict,
        *,
        notion_version: str = "2022-06-28",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaginatedList, AppendBlockChildrenErrorBody]:
        """Creates and appends new children blocks to the parent block specified by block_id. Returns the updated parent
        block. Blocks can be appended to pages, or to other blocks that support children. The maximum number of blocks
        that can be appended in a single request is 100.

        Args:
            block_id: The ID of the block to append children to. This can be a page ID to add content to a page.
            body: The request body.
            notion_version: The version of the Notion API to use. The current version is 2022-06-28. This header is
                required for all API requests.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/blocks/{block_id}/children"),
            path_params=[param[UUID]("block_id", block_id)],
            headers=[param[str]("Notion-Version", notion_version), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BlocksChildrenRequest | BlocksChildrenRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[PaginatedList],
            error_mapper=append_block_children_error_mapper,
            request_options=request_options,
        )

    async def delete_block(
        self, block_id: UUID, *, notion_version: str = "2022-06-28", request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Block, DeleteBlockErrorBody]:
        """Sets a Block object, including page blocks, to archived: true using the ID specified in the path. This is
        equivalent to trashing the block in the Notion UI. To restore an archived block, use the update block endpoint
        to set archived to false.

        Args:
            block_id: The ID of the block to delete (archive).
            notion_version: The version of the Notion API to use. The current version is 2022-06-28. This header is
                required for all API requests.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/blocks/{block_id}"),
            path_params=[param[UUID]("block_id", block_id)],
            headers=[param[str]("Notion-Version", notion_version), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[Block],
            error_mapper=delete_block_error_mapper,
            request_options=request_options,
        )

    async def retrieve_block(
        self, block_id: UUID, *, notion_version: str = "2022-06-28", request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Block, RetrieveBlockErrorBody]:
        """Retrieves a Block object using the ID specified in the path. If the block is a page, the page properties will
        be returned. The block's children are not included; use the retrieve block children endpoint to get them.

        Args:
            block_id: The ID of the block to retrieve.
            notion_version: The version of the Notion API to use. The current version is 2022-06-28. This header is
                required for all API requests.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/blocks/{block_id}"),
            path_params=[param[UUID]("block_id", block_id)],
            headers=[param[str]("Notion-Version", notion_version)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[Block],
            error_mapper=retrieve_block_error_mapper,
            request_options=request_options,
        )

    async def retrieve_block_children(
        self,
        block_id: UUID,
        *,
        start_cursor: str | None = None,
        page_size: int | None = None,
        notion_version: str = "2022-06-28",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaginatedList, RetrieveBlockChildrenErrorBody]:
        """Returns a paginated array of child block objects contained in the block using the ID specified. This is used
        to read page content by passing a page ID as the block_id. Responses include a maximum of 100 blocks per request
        and are returned in the order they appear in the parent block.

        Args:
            block_id: The ID of the block whose children to retrieve. This can be a page ID to retrieve page content.
            start_cursor: Pagination cursor to continue fetching results.
            page_size: Maximum number of blocks to return (max 100).
            notion_version: The version of the Notion API to use. The current version is 2022-06-28. This header is
                required for all API requests.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/blocks/{block_id}/children"),
            path_params=[param[UUID]("block_id", block_id)],
            query_params=[param[str | None]("start_cursor", start_cursor), param[int | None]("page_size", page_size)],
            headers=[param[str]("Notion-Version", notion_version)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[PaginatedList],
            error_mapper=retrieve_block_children_error_mapper,
            request_options=request_options,
        )

    async def update_block(
        self,
        block_id: UUID,
        body: BlocksRequest | BlocksRequestDict,
        *,
        notion_version: str = "2022-06-28",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Block, UpdateBlockErrorBody]:
        """Updates the content of a block. The fields that can be updated depend on the block type. Blocks can also be
        archived by setting the archived field to true.

        Args:
            block_id: The ID of the block to update.
            body: The request body.
            notion_version: The version of the Notion API to use. The current version is 2022-06-28. This header is
                required for all API requests.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/blocks/{block_id}"),
            path_params=[param[UUID]("block_id", block_id)],
            headers=[param[str]("Notion-Version", notion_version), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BlocksRequest | BlocksRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[Block],
            error_mapper=update_block_error_mapper,
            request_options=request_options,
        )


AsyncClient = AsyncNotionApiClient
