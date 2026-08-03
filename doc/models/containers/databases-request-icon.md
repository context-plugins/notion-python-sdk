
# Databases Request Icon

## Data Type

`Emoji | ExternalFile`

## Cases

| Type |
|  --- |
| [`Emoji`](../../../doc/models/emoji.md) |
| [`ExternalFile`](../../../doc/models/external-file.md) |

## Emoji

### Initialization Code

#### Example

```python
value = Emoji(
    mtype=Type3.EMOJI,
    emoji='emoji6'
)
```

## ExternalFile

### Initialization Code

#### Example

```python
value = ExternalFile(
    mtype=Type5.EXTERNAL,
    external=External1(
        url='url2'
    )
)
```

