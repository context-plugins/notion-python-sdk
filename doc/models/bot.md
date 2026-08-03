
# Bot

Bot-specific information. Only present when type is "bot".

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Bot`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `owner` | [`Owner`](../../doc/models/owner.md) | Optional | Information about the bot's owner. |
| `workspace_name` | `str` | Optional | The name of the workspace the bot belongs to. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.bot import Bot
from notion.models.owner import Owner
from notion.models.type_12 import Type12

bot = Bot(
    owner=Owner(
        mtype=Type12.WORKSPACE,
        workspace=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    workspace_name='workspace_name6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

