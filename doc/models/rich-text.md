
# Rich Text

A Rich Text object represents styled text content in Notion. Rich text can include annotations like bold, italic, and color, as well as links and mentions of other Notion objects.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`RichText`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type2`](../../doc/models/type-2.md) | Required | The type of this rich text object. |
| `text` | [`Text`](../../doc/models/text.md) | Optional | Text content and optional link. Present when type is "text". |
| `mention` | [`Any`](../../doc/models/object.md) | Optional | Mention content. Present when type is "mention". Can reference users, pages, databases, dates, or link previews. |
| `equation` | [`Equation`](../../doc/models/equation.md) | Optional | Equation content in KaTeX format. Present when type is "equation". |
| `annotations` | [`Annotations`](../../doc/models/annotations.md) | Optional | Styling annotations applied to the text. |
| `plain_text` | `str` | Required | The plain text content without annotations. |
| `href` | `str` | Optional | The URL of any link in the text, or null. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.annotations import Annotations
from notion.models.equation import Equation
from notion.models.link import Link
from notion.models.rich_text import RichText
from notion.models.text import Text
from notion.models.type_2 import Type2

rich_text = RichText(
    mtype=Type2.EQUATION,
    plain_text='plain_text4',
    text=Text(
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
    ),
    mention=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    equation=Equation(
        expression='expression2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    annotations=Annotations(
        bold=False,
        italic=False,
        strikethrough=False,
        underline=False,
        code=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    href='href4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

