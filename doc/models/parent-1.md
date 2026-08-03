
# Parent 1

The parent page or block the comment belongs to.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Parent1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type11`](../../doc/models/type-11.md) | Optional | - |
| `page_id` | `uuid\|str` | Optional | - |
| `block_id` | `uuid\|str` | Optional | - |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.parent_1 import Parent1
from notion.models.type_11 import Type11

parent_1 = Parent1(
    mtype=Type11.PAGE_ID,
    page_id='0000059a-0000-0000-0000-000000000000',
    block_id='00000d72-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

