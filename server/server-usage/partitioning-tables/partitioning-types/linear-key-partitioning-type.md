---
description: >-
  Learn about LINEAR KEY partitioning, which combines the internal key hashing
  with a linear algorithm for efficient partition handling.
---

# LINEAR KEY Partitioning Type

## Syntax

{% tabs %}
{% tab title="Current" %}
```sql
LINEAR PARTITION BY KEY ([column_names])
ALGORITHM={MYSQL51|MYSQL55|BASE31|CRC32C|XXH32|XXH3} 
          (<column1>, <column2>, ...)
[PARTITIONS (number_of_partitions)]
```

* `CRC32C`, `XXH32`, and `XXH3` use the established hash algorithms of the same names. These are recommended algorithms to use.
* `BASE31` uses a base-31 representation of the bytes and serves as a simple baseline that is more evenly distributed than `MYSQL51` or `MYSQL55` for simple sequential data.
{% endtab %}

{% tab title="< 12.3" %}
```sql
LINEAR PARTITION BY KEY ([column_names])
ALGORITHM={MYSQL51|MYSQL55} 
          (<column1>, <column2>, ...)
[PARTITIONS (number_of_partitions)]
```
{% endtab %}
{% endtabs %}

## Description

`LINEAR KEY` partitioning is a form of [partitioning](../), similar to [KEY partitioning](key-partitioning-type.md).

`LINEAR KEY` partitioning makes use of a powers-of-two algorithm, while `KEY` partitioning uses modulo arithmetic to determine the partition number.

`ALGORITHM` is a hash algorithm. The default is `MYSQL55`.

Adding, dropping, merging and splitting partitions is much faster than with the [KEY partitioning type](key-partitioning-type.md); however, data is less likely to be evenly distributed over the partitions.

## Example

```sql
CREATE OR REPLACE TABLE t1 (v1 INT)
  PARTITION BY LINEAR KEY (v1)
  PARTITIONS 2;
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
