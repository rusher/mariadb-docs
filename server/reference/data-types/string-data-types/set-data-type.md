
# SET Data Type

## Syntax


```
SET('value1','value2',...) [CHARACTER SET charset_name] [COLLATE collation_name]
```

## Description


A set. A string object that can have zero or more values, each of
which must be chosen from the list of values 'value1', 'value2', ... A
SET column can have a maximum of 64 members. SET values are
represented internally as integers.


SET values cannot contain commas.


If a SET contains duplicate values, an error will be returned if [strict mode](../../../server-management/variables-and-modes/sql-mode.md#strict-mode) is enabled, or a warning if strict mode is not enabled.


## EXAMPLES


```
CREATE TABLE set_example (
  description VARCHAR(20),
  example SET('Foo', 'Bar', 'Baz', 'Bob')
);
```

```
INSERT INTO set_example VALUES
  ('1 val', 'Foo'),
  ('2 vals', 'Baz,Foo'),
  ('4 vals', 'Bob,Foo,Bar,Foo,Baz,Bob');
```

```
SELECT * FROM set_example;

+-------------+-----------------+
| description | example         |
+-------------+-----------------+
| 1 val       | Foo             |
| 2 vals      | Foo,Baz         |
| 4 vals      | Foo,Bar,Baz,Bob |
+-------------+-----------------+
```

## See Also


* [Character Sets and Collations](character-sets/supported-character-sets-and-collations.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)


<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>


{% @marketo/form formId="4316" %}
