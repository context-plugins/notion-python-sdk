
# Paginated List

A paginated list of results returned by list and query endpoints. All paginated responses follow the same structure with a results array, pagination info, and object type.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`PaginatedList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object` | [`Object`](../../doc/models/object.md) | Required | Always "list" for paginated responses. |
| `results` | [`List[Any]`](../../doc/models/object.md) | Required | The array of result objects for the current page. |
| `next_cursor` | `str` | Required | The cursor to use for the next page of results, or null if there are no more results. |
| `has_more` | `bool` | Required | Whether there are more results available beyond this page. |
| `mtype` | `str` | Optional | The type of objects in the results array. |
| `request_id` | `str` | Optional | A unique identifier for this API request. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.object import Object
from notion.models.paginated_list import PaginatedList

paginated_list = PaginatedList(
    object=jsonpickle.decode('"list"'),
    results=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    next_cursor='next_cursor0',
    has_more=False,
    mtype='type6',
    request_id='request_id4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

