
# Database

A Database object represents a database in Notion. Databases are collections of pages that share a common schema of properties. The schema defines the columns and their types that all pages in the database will have.

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Database`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object` | [`Object12`](../../doc/models/object-12.md) | Required | Always "database" for database objects. |
| `id` | `uuid\|str` | Required | Unique identifier for the database. |
| `created_time` | `datetime` | Required | Date and time when the database was created (ISO 8601). |
| `last_edited_time` | `datetime` | Required | Date and time when the database was last edited (ISO 8601). |
| `created_by` | [`PartialUser`](../../doc/models/partial-user.md) | Required | A partial User object containing only the object type and ID. Used in created_by and last_edited_by fields. |
| `last_edited_by` | [`PartialUser`](../../doc/models/partial-user.md) | Required | A partial User object containing only the object type and ID. Used in created_by and last_edited_by fields. |
| `title` | [`List[RichText]`](../../doc/models/rich-text.md) | Required | Title of the database as rich text. |
| `description` | [`List[RichText]`](../../doc/models/rich-text.md) | Required | Description of the database as rich text. |
| `icon` | [Emoji](../../doc/models/emoji.md) \| [File](../../doc/models/file.md) \| None | Optional | This is a container for one-of cases. |
| `cover` | [`File`](../../doc/models/file.md) | Optional | Database cover image. |
| `properties` | [`Dict[str, PropertySchema]`](../../doc/models/property-schema.md) | Required | Schema of database properties. Keys are property names, values are property schema objects defining the type and configuration of each column. |
| `parent` | [`Parent`](../../doc/models/parent.md) | Required | A Parent object represents the parent of a page, database, or block. The parent can be a workspace, page, database, or block. |
| `url` | `str` | Required | The URL of the database in Notion. |
| `public_url` | `str` | Optional | The public URL of the database, if published to the web. Otherwise null. |
| `archived` | `bool` | Required | Whether the database has been archived. |
| `in_trash` | `bool` | Optional | Whether the database is in the trash. |
| `is_inline` | `bool` | Optional | Whether the database is inline (appears within its parent page rather than as a full page). |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from notion.models.annotations import Annotations
from notion.models.database import Database
from notion.models.emoji import Emoji
from notion.models.equation import Equation
from notion.models.file import File
from notion.models.file_1 import File1
from notion.models.link import Link
from notion.models.mtype import Type
from notion.models.object_12 import Object12
from notion.models.object_2 import Object2
from notion.models.parent import Parent
from notion.models.partial_user import PartialUser
from notion.models.property_schema import PropertySchema
from notion.models.rich_text import RichText
from notion.models.text import Text
from notion.models.type_2 import Type2
from notion.models.type_21 import Type21
from notion.models.type_3 import Type3
from notion.models.type_31 import Type31

database = Database(
    object=Object12.DATABASE,
    id='0000092e-0000-0000-0000-000000000000',
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
    title=[
        RichText(
            mtype=Type2.EQUATION,
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
    description=[
        RichText(
            mtype=Type2.TEXT,
            plain_text='plain_text2',
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
            href='href2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    properties={
        'key0': PropertySchema(
            id='id2',
            name='name2',
            mtype=Type31.PEOPLE,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        'key1': PropertySchema(
            id='id2',
            name='name2',
            mtype=Type31.PEOPLE,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    },
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
    url='url4',
    archived=False,
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
    public_url='public_url8',
    in_trash=False,
    is_inline=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

