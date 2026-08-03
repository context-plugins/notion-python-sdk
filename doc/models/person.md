
# Person

Person-specific information. Only present when type is "person".

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Person`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Optional | Email address of the person. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.person import Person

person = Person(
    email='email8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

