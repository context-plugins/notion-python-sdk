
# User

A User object represents a user in a Notion workspace. Users can be either people (human workspace members) or bots (API integrations). User objects include identifying information such as name, email, and avatar URL.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`User`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object` | [`Object2`](../../doc/models/object-2.md) | Required | Always "user" for user objects. |
| `id` | `uuid\|str` | Required | Unique identifier for the user. |
| `mtype` | [`Type4`](../../doc/models/type-4.md) | Optional | The type of user. "person" for human workspace members, "bot" for API integrations. |
| `name` | `str` | Optional | Display name of the user. |
| `avatar_url` | `str` | Optional | URL of the user's avatar image. |
| `person` | [`Person`](../../doc/models/person.md) | Optional | Person-specific information. Only present when type is "person". |
| `bot` | [`Bot`](../../doc/models/bot.md) | Optional | Bot-specific information. Only present when type is "bot". |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.bot import Bot
from notion.models.object_2 import Object2
from notion.models.owner import Owner
from notion.models.person import Person
from notion.models.type_12 import Type12
from notion.models.type_4 import Type4
from notion.models.user import User

user = User(
    object=Object2.USER,
    id='0000143c-0000-0000-0000-000000000000',
    mtype=Type4.PERSON,
    name='name0',
    avatar_url='avatar_url6',
    person=Person(
        email='email8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    bot=Bot(
        owner=Owner(
            mtype=Type12.WORKSPACE,
            workspace=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        workspace_name='workspace_name6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

