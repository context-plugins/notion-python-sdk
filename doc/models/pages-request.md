
# Pages Request

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`PagesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `parent` | [`Parent`](../../doc/models/parent.md) | Required | A Parent object represents the parent of a page, database, or block. The parent can be a workspace, page, database, or block. |
| `properties` | [`Any`](../../doc/models/object.md) | Required | Property values for the new page. Keys are property names or IDs. If the parent is a database, the values must conform to the database schema. |
| `children` | [`List[Block]`](../../doc/models/block.md) | Optional | Page content as an array of block objects. |
| `icon` | [Emoji](../../doc/models/emoji.md) \| [ExternalFile](../../doc/models/external-file.md) \| None | Optional | This is a container for one-of cases. |
| `cover` | [`ExternalFile`](../../doc/models/external-file.md) | Optional | Page cover image as an external URL. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from notion.models.block import Block
from notion.models.emoji import Emoji
from notion.models.external_1 import External1
from notion.models.external_file import ExternalFile
from notion.models.mtype import Type
from notion.models.object_1 import Object1
from notion.models.object_2 import Object2
from notion.models.pages_request import PagesRequest
from notion.models.parent import Parent
from notion.models.partial_user import PartialUser
from notion.models.type_1 import Type1
from notion.models.type_3 import Type3
from notion.models.type_5 import Type5

pages_request = PagesRequest(
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
    properties=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    children=[
        Block(
            object=Object1.BLOCK,
            id='000003b4-0000-0000-0000-000000000000',
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
    ],
    icon=Emoji(
        mtype=Type3.EMOJI,
        emoji='emoji6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    cover=ExternalFile(
        mtype=Type5.EXTERNAL,
        external=External1(
            url='url2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

