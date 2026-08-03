
# Databases Query Request

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`DatabasesQueryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter` | [`Any`](../../doc/models/object.md) | Optional | Filter conditions to apply. Supports compound filters using and/or as well as property-specific filters. |
| `sorts` | [`List[Sort]`](../../doc/models/sort.md) | Optional | Sort conditions to order the results. Multiple sorts can be applied; they are processed in the order provided. |
| `start_cursor` | `str` | Optional | Pagination cursor from a previous response to continue fetching results. |
| `page_size` | `int` | Optional | Maximum number of results to return (max 100).<br><br>**Default**: `100`<br><br>**Constraints**: `<= 100` |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.databases_query_request import DatabasesQueryRequest
from notion.models.direction import Direction
from notion.models.sort import Sort
from notion.models.timestamp import Timestamp

databases_query_request = DatabasesQueryRequest(
    filter=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    sorts=[
        Sort(
            property='property2',
            timestamp=Timestamp.CREATED_TIME,
            direction=Direction.ASCENDING,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Sort(
            property='property2',
            timestamp=Timestamp.CREATED_TIME,
            direction=Direction.ASCENDING,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    start_cursor='start_cursor6',
    page_size=100,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

