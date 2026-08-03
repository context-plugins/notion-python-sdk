
# Blocks Children Request

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`BlocksChildrenRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `children` | [`List[Block]`](../../doc/models/block.md) | Required | Array of block objects to append as children. Maximum 100 blocks per request.<br><br>**Constraints**: *Maximum Items*: `100` |
| `after` | `uuid\|str` | Optional | The ID of an existing block to insert the new children after. If omitted, blocks are appended to the end. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from notion.models.block import Block
from notion.models.blocks_children_request import BlocksChildrenRequest
from notion.models.mtype import Type
from notion.models.object_1 import Object1
from notion.models.object_2 import Object2
from notion.models.parent import Parent
from notion.models.partial_user import PartialUser
from notion.models.type_1 import Type1

blocks_children_request = BlocksChildrenRequest(
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
    after='00000802-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

