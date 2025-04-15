
# SETVAL

## Syntax


```
SETVAL(sequence_name, next_value, [is_used, [round]])
```


## Description


Set the next value to be returned for a `<code>SEQUENCE</code>`.


This function is compatible with PostgreSQL syntax, extended
with the `<code>round</code>` argument.


If the `<code>is_used</code>` argument is not given or is `<code>1</code>` or `<code>true</code>`, then the next used value will
one after the given value. If `<code>is_used</code>` is `<code>0</code>` or `<code>false</code>` then the next generated value
will be the given value.


If `<code>round</code>` is used then it will set the `<code>round</code>` value (or the internal cycle count, starting at zero) for the sequence.
If `<code>round</code>` is not used, it's assumed to be 0.


`<code>next_value</code>` must be an integer literal.


For `<code>SEQUENCE</code>` tables defined with `<code>CYCLE</code>` (see [CREATE SEQUENCE](../create-sequence.md)) one should use both `<code>next_value</code>` and `<code>round</code>` to define the next value. In this case the
current sequence value is defined to be `<code>round</code>`, `<code>next_value</code>`.


The result returned by `<code>SETVAL()</code>` is `<code>next_value</code>` or NULL if the given `<code>next_value</code>` and `<code>round</code>` is smaller than the current value.


`<code>SETVAL()</code>` will not set the `<code>SEQUENCE</code>` value to a something that is less than
its current value. This is needed to ensure that `<code>SETVAL()</code>`
is replication safe. If you want to set the SEQUENCE to a smaller number
use [ALTER SEQUENCE](../alter-sequence.md).


If `<code>CYCLE</code>` is used, first `<code>round</code>` and then `<code>next_value</code>` are compared
to see if the value is bigger than the current value.


Internally, in the MariaDB server, `<code>SETVAL()</code>` is used to inform
replicas that a `<code>SEQUENCE</code>` has changed value. The replica may get
`<code>SETVAL()</code>` statements out of order, but this is ok as only the
biggest one will have an effect.


`<code>SETVAL</code>` requires the [INSERT privilege](../../sql-statements/account-management-sql-commands/grant.md).


## Examples


```
SELECT setval(foo, 42);           -- Next nextval will return 43
SELECT setval(foo, 42, true);     -- Same as above
SELECT setval(foo, 42, false);    -- Next nextval will return 42
```

SETVAL setting higher and lower values on a sequence with an increment of 10:


```
SELECT NEXTVAL(s);
+------------+
| NEXTVAL(s) |
+------------+
|         50 |
+------------+

SELECT SETVAL(s, 100);
+----------------+
| SETVAL(s, 100) |
+----------------+
|            100 |
+----------------+

SELECT NEXTVAL(s);
+------------+
| NEXTVAL(s) |
+------------+
|        110 |
+------------+

SELECT SETVAL(s, 50);
+---------------+
| SETVAL(s, 50) |
+---------------+
|          NULL |
+---------------+

SELECT NEXTVAL(s);
+------------+
| NEXTVAL(s) |
+------------+
|        120 |
+------------+
```

Example demonstrating `<code>round</code>`:


```
CREATE OR REPLACE SEQUENCE s1
  START WITH 1
  MINVALUE 1
  MAXVALUE 99
  INCREMENT BY 1 
  CACHE 20 
  CYCLE;

SELECT SETVAL(s1, 99, 1, 0);
+----------------------+
| SETVAL(s1, 99, 1, 0) |
+----------------------+
|                   99 |
+----------------------+

SELECT NEXTVAL(s1);
+-------------+
| NEXTVAL(s1) |
+-------------+
|           1 |
+-------------+
```

The following statement returns NULL, as the given `<code>next_value</code>` and `<code>round</code>` is smaller than the current value.


```
SELECT SETVAL(s1, 99, 1, 0);
+----------------------+
| SETVAL(s1, 99, 1, 0) |
+----------------------+
|                 NULL |
+----------------------+

SELECT NEXTVAL(s1);
+-------------+
| NEXTVAL(s1) |
+-------------+
|           2 |
+-------------+
```

Increasing the round from zero to 1 will allow `<code>next_value</code>` to be returned.


```
SELECT SETVAL(s1, 99, 1, 1);
+----------------------+
| SETVAL(s1, 99, 1, 1) |
+----------------------+
|                   99 |
+----------------------+

SELECT NEXTVAL(s1);
+-------------+
| NEXTVAL(s1) |
+-------------+
|           1 |
+-------------+
```

## See Also


* [Sequence Overview](../sequence-overview.md)
* [ALTER SEQUENCE](../alter-sequence.md)
* [CREATE SEQUENCE](../create-sequence.md)
* [NEXT VALUE FOR](next-value-for-sequence_name.md)
* [PREVIOUS VALUE FOR](previous-value-for-sequence_name.md)
* [Information Schema SEQUENCES Table](../../sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-sequences-table.md)
* [Error 4084: Sequence has run out](../../../mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4000-to-4099/e4084.md)

