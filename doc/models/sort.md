
# Sort

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Sort`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `property` | `str` | Optional | The name of the property to sort by. |
| `timestamp` | [`Timestamp`](../../doc/models/timestamp.md) | Optional | The timestamp to sort by. Possible values are created_time or last_edited_time. |
| `direction` | [`Direction`](../../doc/models/direction.md) | Optional | The sort direction. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.direction import Direction
from notion.models.sort import Sort
from notion.models.timestamp import Timestamp

sort = Sort(
    property='property0',
    timestamp=Timestamp.CREATED_TIME,
    direction=Direction.ASCENDING,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

