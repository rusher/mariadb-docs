---
icon: earth-africa
---

# MBRContains

## Syntax

```sql
MBRContains(g1,g2)
```

## Description

Returns 1 or 0 to indicate whether the [Minimum Bounding Rectangle](mbr-definition.md) of g1 contains the Minimum Bounding Rectangle of g2. This tests the opposite relationship as [MBRWithin()](mbrwithin.md).

## Examples

```sql
SET @g1 = GeomFromText('Polygon((0 0,0 3,3 3,3 0,0 0))');

SET @g2 = GeomFromText('Point(1 1)');

SELECT MBRContains(@g1,@g2), MBRContains(@g2,@g1);
+----------------------+----------------------+
| MBRContains(@g1,@g2) | MBRContains(@g2,@g1) |
+----------------------+----------------------+
|                    1 |                    0 |
+----------------------+----------------------+
```

## See Also

* [MBRWithin](mbrwithin.md)

GPLv2 fill\_help\_tables.sql
