
# Comment

A Comment object represents a comment on a Notion page or block. Comments contain rich text content and are associated with discussion threads.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Comment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object` | [`Object11`](../../doc/models/object-11.md) | Required | Always "comment" for comment objects. |
| `id` | `uuid\|str` | Required | Unique identifier for the comment. |
| `parent` | [`Parent1`](../../doc/models/parent-1.md) | Required | The parent page or block the comment belongs to. |
| `discussion_id` | `uuid\|str` | Required | The ID of the discussion thread the comment belongs to. |
| `created_time` | `datetime` | Required | Date and time when the comment was created (ISO 8601). |
| `last_edited_time` | `datetime` | Required | Date and time when the comment was last edited (ISO 8601). |
| `created_by` | [`PartialUser`](../../doc/models/partial-user.md) | Required | A partial User object containing only the object type and ID. Used in created_by and last_edited_by fields. |
| `rich_text` | [`List[RichText]`](../../doc/models/rich-text.md) | Required | Rich text content of the comment. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from notion.models.annotations import Annotations
from notion.models.comment import Comment
from notion.models.equation import Equation
from notion.models.link import Link
from notion.models.object_11 import Object11
from notion.models.object_2 import Object2
from notion.models.parent_1 import Parent1
from notion.models.partial_user import PartialUser
from notion.models.rich_text import RichText
from notion.models.text import Text
from notion.models.type_11 import Type11
from notion.models.type_2 import Type2

comment = Comment(
    object=Object11.COMMENT,
    id='00002144-0000-0000-0000-000000000000',
    parent=Parent1(
        mtype=Type11.PAGE_ID,
        page_id='00001234-0000-0000-0000-000000000000',
        block_id='00001a0c-0000-0000-0000-000000000000',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    discussion_id='0000150e-0000-0000-0000-000000000000',
    created_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    last_edited_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    created_by=PartialUser(
        object=Object2.USER,
        id='00001f9c-0000-0000-0000-000000000000',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
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
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

