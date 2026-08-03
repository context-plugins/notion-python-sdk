
# Text

Text content and optional link. Present when type is "text".

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Text`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | `str` | Optional | The actual text content. |
| `link` | [`Link`](../../doc/models/link.md) | Optional | Optional link within the text. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.link import Link
from notion.models.text import Text

text = Text(
    content='content4',
    link=Link(
        url='url4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

