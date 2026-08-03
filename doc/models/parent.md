
# Parent

A Parent object represents the parent of a page, database, or block. The parent can be a workspace, page, database, or block.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Parent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type`](../../doc/models/type.md) | Required | The type of parent. |
| `database_id` | `uuid\|str` | Optional | The ID of the parent database. Present when type is "database_id". |
| `page_id` | `uuid\|str` | Optional | The ID of the parent page. Present when type is "page_id". |
| `block_id` | `uuid\|str` | Optional | The ID of the parent block. Present when type is "block_id". |
| `workspace` | `bool` | Optional | Always true when the parent is the workspace. Present when type is "workspace". |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.mtype import Type
from notion.models.parent import Parent

parent = Parent(
    mtype=Type.BLOCK_ID,
    database_id='000015f2-0000-0000-0000-000000000000',
    page_id='00001234-0000-0000-0000-000000000000',
    block_id='00001a0c-0000-0000-0000-000000000000',
    workspace=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

