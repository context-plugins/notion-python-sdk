
# Block

A Block object represents a piece of content within a Notion page. Blocks are the building blocks of all page content and can be of many types including paragraphs, headings, lists, images, code, tables, and more. Blocks can contain other blocks as children, forming a tree structure.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Block`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object` | [`Object1`](../../doc/models/object-1.md) | Required | Always "block" for block objects. |
| `id` | `uuid\|str` | Required | Unique identifier for the block. |
| `parent` | [`Parent`](../../doc/models/parent.md) | Optional | A Parent object represents the parent of a page, database, or block. The parent can be a workspace, page, database, or block. |
| `mtype` | [`Type1`](../../doc/models/type-1.md) | Required | The type of block. Determines which type-specific content field is present. Common types include paragraph, heading_1, heading_2, heading_3, bulleted_list_item, numbered_list_item, to_do, toggle, code, image, divider, table, and many more. |
| `created_time` | `datetime` | Required | Date and time when the block was created (ISO 8601). |
| `last_edited_time` | `datetime` | Required | Date and time when the block was last edited (ISO 8601). |
| `created_by` | [`PartialUser`](../../doc/models/partial-user.md) | Optional | A partial User object containing only the object type and ID. Used in created_by and last_edited_by fields. |
| `last_edited_by` | [`PartialUser`](../../doc/models/partial-user.md) | Optional | A partial User object containing only the object type and ID. Used in created_by and last_edited_by fields. |
| `archived` | `bool` | Optional | Whether the block has been archived. |
| `in_trash` | `bool` | Optional | Whether the block is in the trash. |
| `has_children` | `bool` | Required | Whether the block has child blocks nested within it. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from notion.models.block import Block
from notion.models.mtype import Type
from notion.models.object_1 import Object1
from notion.models.object_2 import Object2
from notion.models.parent import Parent
from notion.models.partial_user import PartialUser
from notion.models.type_1 import Type1

block = Block(
    object=Object1.BLOCK,
    id='00001d58-0000-0000-0000-000000000000',
    mtype=Type1.TO_DO,
    created_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    last_edited_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    has_children=False,
    parent=Parent(
        mtype=Type.BLOCK_ID,
        database_id='000015f2-0000-0000-0000-000000000000',
        page_id='00001234-0000-0000-0000-000000000000',
        block_id='00001a0c-0000-0000-0000-000000000000',
        workspace=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    created_by=PartialUser(
        object=Object2.USER,
        id='00001f9c-0000-0000-0000-000000000000',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    last_edited_by=PartialUser(
        object=Object2.USER,
        id='000022e4-0000-0000-0000-000000000000',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    archived=False,
    in_trash=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

