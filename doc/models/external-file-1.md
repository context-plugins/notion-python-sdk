
# External File 1

Database cover image.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`ExternalFile1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type5`](../../doc/models/type-5.md) | Required | Always "external". |
| `external` | [`External1`](../../doc/models/external-1.md) | Required | - |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.external_1 import External1
from notion.models.external_file_1 import ExternalFile1
from notion.models.type_5 import Type5

external_file_1 = ExternalFile1(
    mtype=Type5.EXTERNAL,
    external=External1(
        url='url2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

