
# Sort 1

Sort conditions for the results.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Sort1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `direction` | [`Direction`](../../doc/models/direction.md) | Optional | The sort direction. |
| `timestamp` | [`Timestamp1`](../../doc/models/timestamp-1.md) | Optional | The timestamp to sort by. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.direction import Direction
from notion.models.sort_1 import Sort1
from notion.models.timestamp_1 import Timestamp1

sort_1 = Sort1(
    direction=Direction.ASCENDING,
    timestamp=Timestamp1.LAST_EDITED_TIME,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

