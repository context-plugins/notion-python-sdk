
# File 1

Notion-hosted file details. Present when type is "file". These URLs expire after one hour.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`File1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | The authenticated S3 URL for the file. |
| `expiry_time` | `datetime` | Optional | The expiration time of the URL. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from notion.models.file_1 import File1

file_1 = File1(
    url='url0',
    expiry_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

