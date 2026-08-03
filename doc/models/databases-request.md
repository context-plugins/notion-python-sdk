
# Databases Request

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`DatabasesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `parent` | [`Parent`](../../doc/models/parent.md) | Required | A Parent object represents the parent of a page, database, or block. The parent can be a workspace, page, database, or block. |
| `title` | [`List[RichText]`](../../doc/models/rich-text.md) | Optional | Rich text array for the database title. |
| `description` | [`List[RichText]`](../../doc/models/rich-text.md) | Optional | Rich text array for the database description. |
| `properties` | [`Dict[str, PropertySchema]`](../../doc/models/property-schema.md) | Required | Schema of the database properties. Keys are property names, values are property schema objects defining the type and configuration. |
| `is_inline` | `bool` | Optional | Whether the database appears inline within its parent page rather than as a full page. |
| `icon` | [Emoji](../../doc/models/emoji.md) \| [ExternalFile](../../doc/models/external-file.md) \| None | Optional | This is a container for one-of cases. |
| `cover` | [`ExternalFile1`](../../doc/models/external-file-1.md) | Optional | Database cover image. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.annotations import Annotations
from notion.models.databases_request import DatabasesRequest
from notion.models.emoji import Emoji
from notion.models.equation import Equation
from notion.models.external_1 import External1
from notion.models.external_file_1 import ExternalFile1
from notion.models.link import Link
from notion.models.mtype import Type
from notion.models.parent import Parent
from notion.models.property_schema import PropertySchema
from notion.models.rich_text import RichText
from notion.models.text import Text
from notion.models.type_2 import Type2
from notion.models.type_3 import Type3
from notion.models.type_31 import Type31
from notion.models.type_5 import Type5

databases_request = DatabasesRequest(
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
        ),
        'key2': PropertySchema(
            id='id2',
            name='name2',
            mtype=Type31.PEOPLE,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    },
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
        ),
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
        ),
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
        ),
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
    is_inline=False,
    icon=Emoji(
        mtype=Type3.EMOJI,
        emoji='emoji6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    cover=ExternalFile1(
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

