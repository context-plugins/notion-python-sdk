
# Page

A Page object represents a page in a Notion workspace. Pages can exist as standalone pages in a workspace or as items within a database. Each page has properties, which are metadata fields defined by its parent database schema or by the page itself.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Page`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object` | [`Object21`](../../doc/models/object-21.md) | Required | Always "page" for page objects. |
| `id` | `uuid\|str` | Required | Unique identifier for the page. |
| `created_time` | `datetime` | Required | Date and time when the page was created (ISO 8601). |
| `last_edited_time` | `datetime` | Required | Date and time when the page was last edited (ISO 8601). |
| `created_by` | [`PartialUser`](../../doc/models/partial-user.md) | Required | A partial User object containing only the object type and ID. Used in created_by and last_edited_by fields. |
| `last_edited_by` | [`PartialUser`](../../doc/models/partial-user.md) | Required | A partial User object containing only the object type and ID. Used in created_by and last_edited_by fields. |
| `archived` | `bool` | Required | Whether the page has been archived (trashed). |
| `in_trash` | `bool` | Optional | Whether the page is in the trash. |
| `icon` | [Emoji](../../doc/models/emoji.md) \| [File](../../doc/models/file.md) \| None | Optional | This is a container for one-of cases. |
| `cover` | [`File`](../../doc/models/file.md) | Optional | Page cover image. |
| `properties` | [`Any`](../../doc/models/object.md) | Required | Property values of the page. Keys are property names or IDs. |
| `parent` | [`Parent`](../../doc/models/parent.md) | Required | A Parent object represents the parent of a page, database, or block. The parent can be a workspace, page, database, or block. |
| `url` | `str` | Required | The URL of the page in Notion. |
| `public_url` | `str` | Optional | The public URL of the page, if the page has been published to the web. Otherwise null. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from notion.models.annotations import Annotations
from notion.models.emoji import Emoji
from notion.models.equation import Equation
from notion.models.file import File
from notion.models.file_1 import File1
from notion.models.link import Link
from notion.models.mtype import Type
from notion.models.object_2 import Object2
from notion.models.object_21 import Object21
from notion.models.page import Page
from notion.models.parent import Parent
from notion.models.partial_user import PartialUser
from notion.models.rich_text import RichText
from notion.models.text import Text
from notion.models.type_2 import Type2
from notion.models.type_21 import Type21
from notion.models.type_3 import Type3

page = Page(
    object=Object21.PAGE,
    id='0000202e-0000-0000-0000-000000000000',
    created_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    last_edited_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    created_by=PartialUser(
        object=Object2.USER,
        id='00001f9c-0000-0000-0000-000000000000',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    last_edited_by=PartialUser(
        object=Object2.USER,
        id='000022e4-0000-0000-0000-000000000000',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    archived=False,
    properties=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    parent=Parent(
        mtype=Type.BLOCK_ID,
        database_id='000015f2-0000-0000-0000-000000000000',
        page_id='00001234-0000-0000-0000-000000000000',
        block_id='00001a0c-0000-0000-0000-000000000000',
        workspace=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    url='url2',
    in_trash=False,
    icon=Emoji(
        mtype=Type3.EMOJI,
        emoji='emoji6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    cover=File(
        mtype=Type21.FILE,
        file=File1(
            url='url4',
            expiry_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        external=Link(
            url='url2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        name='name6',
        caption=[
            RichText(
                mtype=Type2.TEXT,
                plain_text='plain_text6',
                text=Text(
                    content='content4',
                    link=Link(
                        url='url4',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                mention=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                equation=Equation(
                    expression='expression2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                annotations=Annotations(
                    bold=False,
                    italic=False,
                    strikethrough=False,
                    underline=False,
                    code=False,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                href='href6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            RichText(
                mtype=Type2.TEXT,
                plain_text='plain_text6',
                text=Text(
                    content='content4',
                    link=Link(
                        url='url4',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                mention=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                equation=Equation(
                    expression='expression2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                annotations=Annotations(
                    bold=False,
                    italic=False,
                    strikethrough=False,
                    underline=False,
                    code=False,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                href='href6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    public_url='public_url0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

