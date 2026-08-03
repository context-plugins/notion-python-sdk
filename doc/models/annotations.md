
# Annotations

Styling annotations applied to the text.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Annotations`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bold` | `bool` | Optional | Whether the text is bold. |
| `italic` | `bool` | Optional | Whether the text is italic. |
| `strikethrough` | `bool` | Optional | Whether the text has a strikethrough. |
| `underline` | `bool` | Optional | Whether the text is underlined. |
| `code` | `bool` | Optional | Whether the text is formatted as inline code. |
| `color` | `str` | Optional | The color of the text. Possible values include default, gray, brown, orange, yellow, green, blue, purple, pink, red, and their background variants (e.g., gray_background). |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.annotations import Annotations

annotations = Annotations(
    bold=False,
    italic=False,
    strikethrough=False,
    underline=False,
    code=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

