
# Databases Request 1

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`DatabasesRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | [`List[RichText]`](../../doc/models/rich-text.md) | Optional | Updated database title as rich text. |
| `description` | [`List[RichText]`](../../doc/models/rich-text.md) | Optional | Updated database description as rich text. |
| `properties` | [`Any`](../../doc/models/object.md) | Optional | Updated property schema. Include only properties to add or modify. Set a property value to null to remove it. |
| `icon` | [Emoji](../../doc/models/emoji.md) \| [ExternalFile](../../doc/models/external-file.md) \| None | Optional | This is a container for one-of cases. |
| `cover` | [`ExternalFile`](../../doc/models/external-file.md) | Optional | Updated database cover image. |
| `is_inline` | `bool` | Optional | Whether the database is inline. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.annotations import Annotations
from notion.models.databases_request_1 import DatabasesRequest1
from notion.models.emoji import Emoji
from notion.models.equation import Equation
from notion.models.external_1 import External1
from notion.models.external_file import ExternalFile
from notion.models.link import Link
from notion.models.rich_text import RichText
from notion.models.text import Text
from notion.models.type_2 import Type2
from notion.models.type_3 import Type3
from notion.models.type_5 import Type5

databases_request_1 = DatabasesRequest1(
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
    properties=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
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

