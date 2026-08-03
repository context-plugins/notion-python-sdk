
# Filter

Filter conditions. Currently only supports filtering by object type (page or database).

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | [`Value`](../../doc/models/value.md) | Optional | The type of object to filter by. |
| `property` | [`Property`](../../doc/models/property.md) | Optional | Must be "object". |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.filter import Filter
from notion.models.property import Property
from notion.models.value import Value

filter = Filter(
    value=Value.PAGE,
    property=Property.OBJECT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

