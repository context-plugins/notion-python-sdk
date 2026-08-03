
# Blocks Request

Block type-specific content to update. Include the block type key with the fields to modify.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`BlocksRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `archived` | `bool` | Optional | Set to true to archive the block. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.blocks_request import BlocksRequest

blocks_request = BlocksRequest(
    archived=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

