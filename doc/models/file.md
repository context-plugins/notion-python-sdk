
# File

A File object represents a file in Notion. Files can be either hosted by Notion (type "file") or externally hosted (type "external").

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`File`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type21`](../../doc/models/type-21.md) | Required | The type of file hosting. |
| `file` | [`File1`](../../doc/models/file-1.md) | Optional | Notion-hosted file details. Present when type is "file". These URLs expire after one hour. |
| `external` | [`Link`](../../doc/models/link.md) | Optional | External file details. Present when type is "external". |
| `name` | `str` | Optional | The name of the file. |
| `caption` | [`List[RichText]`](../../doc/models/rich-text.md) | Optional | Caption for the file as rich text. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from notion.models.annotations import Annotations
from notion.models.equation import Equation
from notion.models.file import File
from notion.models.file_1 import File1
from notion.models.link import Link
from notion.models.rich_text import RichText
from notion.models.text import Text
from notion.models.type_2 import Type2
from notion.models.type_21 import Type21

file = File(
    mtype=Type21.FILE,
    file=File1(
        url='url4',
        expiry_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    external=Link(
        url='url2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    name='name0',
    caption=[
        RichText(
            mtype=Type2.TEXT,
            plain_text='plain_text6',
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
            href='href6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        RichText(
            mtype=Type2.TEXT,
            plain_text='plain_text6',
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
            href='href6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

