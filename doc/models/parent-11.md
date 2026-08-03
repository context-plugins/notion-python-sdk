
# Parent 11

The parent page to create the comment on. Required if discussion_id is not provided.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Parent11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_id` | `uuid\|str` | Optional | The ID of the parent page. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.parent_11 import Parent11

parent_11 = Parent11(
    page_id='000008b8-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

