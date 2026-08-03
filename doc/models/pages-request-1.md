
# Pages Request 1

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`PagesRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `properties` | [`Any`](../../doc/models/object.md) | Optional | Property values to update. |
| `archived` | `bool` | Optional | Set to true to archive (trash) the page. |
| `icon` | [Emoji](../../doc/models/emoji.md) \| [ExternalFile](../../doc/models/external-file.md) \| None | Optional | This is a container for one-of cases. |
| `cover` | [`ExternalFile`](../../doc/models/external-file.md) | Optional | Page cover image to set or remove. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.emoji import Emoji
from notion.models.external_1 import External1
from notion.models.external_file import ExternalFile
from notion.models.pages_request_1 import PagesRequest1
from notion.models.type_3 import Type3
from notion.models.type_5 import Type5

pages_request_1 = PagesRequest1(
    properties=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    archived=False,
    icon=Emoji(
        mtype=Type3.EMOJI,
        emoji='emoji6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    cover=ExternalFile(
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
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

