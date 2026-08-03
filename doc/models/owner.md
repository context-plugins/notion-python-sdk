
# Owner

Information about the bot's owner.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Owner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type12`](../../doc/models/type-12.md) | Optional | - |
| `workspace` | `bool` | Optional | Whether the bot is owned by the workspace. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.owner import Owner
from notion.models.type_12 import Type12

owner = Owner(
    mtype=Type12.WORKSPACE,
    workspace=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

