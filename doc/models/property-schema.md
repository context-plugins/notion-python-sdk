
# Property Schema

A Property Schema object defines a database property's configuration including its type and type-specific settings. Common property types include title, rich_text, number, select, multi_select, date, people, files, checkbox, url, email, phone_number, formula, relation, rollup, created_time, created_by, last_edited_time, last_edited_by, and status.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`PropertySchema`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of the property. |
| `name` | `str` | Optional | The name of the property. |
| `mtype` | [`Type31`](../../doc/models/type-31.md) | Optional | The type of property. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.property_schema import PropertySchema
from notion.models.type_31 import Type31

property_schema = PropertySchema(
    id='id4',
    name='name4',
    mtype=Type31.MULTI_SELECT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

