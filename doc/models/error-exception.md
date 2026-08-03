
# Error Exception

An error response from the Notion API.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`ErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object` | [`Object3`](../../doc/models/object-3.md) | Required | Always "error" for error responses. |
| `status` | `int` | Required | The HTTP status code. |
| `code` | `str` | Required | A machine-readable error code. Common codes include invalid_json, invalid_request_url, invalid_request, validation_error, missing_version, unauthorized, restricted_resource, object_not_found, conflict_error, rate_limited, internal_server_error, service_unavailable, and database_connection_unavailable. |
| `message` | `str` | Required | A human-readable error message. |
| `request_id` | `str` | Optional | A unique identifier for the failed request. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
try:
    # make the API call
except ErrorException as e:
    print(e)
except ApiException as e:
    print(e)
```

