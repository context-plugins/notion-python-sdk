
# Partial User

A partial User object containing only the object type and ID. Used in created_by and last_edited_by fields.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`PartialUser`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object` | [`Object2`](../../doc/models/object-2.md) | Required | Always "user". |
| `id` | `uuid\|str` | Required | Unique identifier for the user. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.object_2 import Object2
from notion.models.partial_user import PartialUser

partial_user = PartialUser(
    object=Object2.USER,
    id='00000094-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

