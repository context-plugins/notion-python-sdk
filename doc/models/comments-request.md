
# Comments Request

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`CommentsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `parent` | [`Parent11`](../../doc/models/parent-11.md) | Optional | The parent page to create the comment on. Required if discussion_id is not provided. |
| `discussion_id` | `uuid\|str` | Optional | The ID of an existing discussion thread to add the comment to. Required if parent is not provided. |
| `rich_text` | [`List[RichText]`](../../doc/models/rich-text.md) | Required | Rich text content of the comment. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.annotations import Annotations
from notion.models.comments_request import CommentsRequest
from notion.models.equation import Equation
from notion.models.link import Link
from notion.models.parent_11 import Parent11
from notion.models.rich_text import RichText
from notion.models.text import Text
from notion.models.type_2 import Type2

comments_request = CommentsRequest(
    rich_text=[
        RichText(
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
    ],
    parent=Parent11(
        page_id='00001234-0000-0000-0000-000000000000',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    discussion_id='00001204-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

