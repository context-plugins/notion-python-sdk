
# Type 1

The type of block. Determines which type-specific content field is present. Common types include paragraph, heading_1, heading_2, heading_3, bulleted_list_item, numbered_list_item, to_do, toggle, code, image, divider, table, and many more.

## Enumeration

`Type1`

## Fields

| Name |
|  --- |
| `PARAGRAPH` |
| `HEADING_1` |
| `HEADING_2` |
| `HEADING_3` |
| `BULLETED_LIST_ITEM` |
| `NUMBERED_LIST_ITEM` |
| `TO_DO` |
| `TOGGLE` |
| `CHILD_PAGE` |
| `CHILD_DATABASE` |
| `EMBED` |
| `IMAGE` |
| `VIDEO` |
| `FILE` |
| `PDF` |
| `BOOKMARK` |
| `CALLOUT` |
| `QUOTE` |
| `EQUATION` |
| `DIVIDER` |
| `TABLE_OF_CONTENTS` |
| `COLUMN_LIST` |
| `COLUMN` |
| `LINK_PREVIEW` |
| `SYNCED_BLOCK` |
| `TEMPLATE` |
| `LINK_TO_PAGE` |
| `TABLE` |
| `TABLE_ROW` |
| `CODE` |
| `AUDIO` |
| `BREADCRUMB` |

## Example

```python
from notion.models.type_1 import Type1

type_1 = Type1.TABLE_ROW
```

