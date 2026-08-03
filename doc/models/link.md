
# Link

Optional link within the text., External file details. Present when type is "external"., Optional link within the text., External file details. Present when type is "external"., Optional link within the text.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Link`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | The URL the text links to. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.link import Link

link = Link(
    url='url4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

