
# Equation

Equation content in KaTeX format. Present when type is "equation".

*This model accepts additional fields of type [Any](../../doc/models/object.md).*

## Structure

`Equation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `expression` | `str` | Optional | The LaTeX equation expression. |
| `additional_properties` | [`Dict[str, Any]`](../../doc/models/object.md) | Optional | - |

## Example

```python
import jsonpickle

from notion.models.equation import Equation

equation = Equation(
    expression='expression2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

