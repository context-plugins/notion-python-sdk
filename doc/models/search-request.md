
# Search Request

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`SearchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query` | `str` | Optional | The text to search for in page and database titles. If omitted, returns all pages and databases. |
| `filter` | [`Filter`](../../doc/models/filter.md) | Optional | Filter conditions. Currently only supports filtering by object type (page or database). |
| `sort` | [`Sort1`](../../doc/models/sort-1.md) | Optional | Sort conditions for the results. |
| `start_cursor` | `str` | Optional | Pagination cursor to continue fetching results. |
| `page_size` | `int` | Optional | Maximum number of results to return (max 100).<br><br>**Default**: `100`<br><br>**Constraints**: `<= 100` |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.direction import Direction
from notion.models.filter import Filter
from notion.models.property import Property
from notion.models.search_request import SearchRequest
from notion.models.sort_1 import Sort1
from notion.models.timestamp_1 import Timestamp1
from notion.models.value import Value

search_request = SearchRequest(
    query='query6',
    filter=Filter(
        value=Value.PAGE,
        property=Property.OBJECT,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    sort=Sort1(
        direction=Direction.ASCENDING,
        timestamp=Timestamp1.LAST_EDITED_TIME,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    start_cursor='start_cursor4',
    page_size=100,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

