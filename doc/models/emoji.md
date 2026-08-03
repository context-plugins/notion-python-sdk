
# Emoji

An emoji icon object.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Emoji`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type3`](../../doc/models/type-3.md) | Required | Always "emoji". |
| `emoji` | `str` | Required | The emoji character. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.emoji import Emoji
from notion.models.type_3 import Type3

emoji = Emoji(
    mtype=Type3.EMOJI,
    emoji='emoji4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

