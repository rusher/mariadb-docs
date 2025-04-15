
# NEXT VALUE for sequence_name

## Syntax


```
NEXT VALUE FOR sequence
```

or


```
NEXTVAL(sequence_name)
```

or in Oracle mode ([SQL_MODE=ORACLE](../../../../server-management/variables-and-modes/sql-mode.md))


```
sequence_name.nextval
```


`<code>NEXT VALUE FOR</code>` is ANSI SQL syntax while `<code>NEXTVAL()</code>` is PostgreSQL syntax.


## Description


Generate next value for a `<code>SEQUENCE</code>`.


* You can greatly speed up `<code>NEXT VALUE</code>` by creating the sequence with the `<code>CACHE</code>` option. If not, every `<code>NEXT VALUE</code>` usage will cause changes in the stored `<code>SEQUENCE</code>` table.
* When using `<code>NEXT VALUE</code>` the value will be reserved at once and will not be reused, except if the `<code>SEQUENCE</code>` was created with `<code>CYCLE</code>`. This means that when you are using `<code>SEQUENCE</code>`s you have to expect gaps in the generated sequence numbers.
* If one updates the `<code>SEQUENCE</code>` with [SETVAL()](setval.md) or [ALTER SEQUENCE ... RESTART](../alter-sequence.md), `<code>NEXT VALUE FOR</code>` will notice this and start from the next requested value.
* [FLUSH TABLES](../../sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) will close the sequence and the next sequence number generated will be according to what's stored in the `<code>SEQUENCE</code>` object. In effect, this will discard the cached values.
* A server restart (or closing the current connection) also causes a drop of all cached values. The cached sequence numbers are reserved only for the current connection.
* `<code>NEXT VALUE</code>` requires the `<code>INSERT</code>` [privilege](../../sql-statements/account-management-sql-commands/grant.md).
* You can also use `<code>NEXT VALUE FOR sequence</code>` for column `<code>DEFAULT</code>`.


Once the sequence is complete, unless the sequence has been created with the [CYCLE](../create-sequence.md#cycle-nocycle) attribute (not the default), calling the function will result in [Error 4084: Sequence has run out](../../../mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4000-to-4099/e4084.md).


## Examples


```
CREATE OR REPLACE SEQUENCE s MAXVALUE=2;

SELECT NEXTVAL(s);
+------------+
| NEXTVAL(s) |
+------------+
|          1 |
+------------+

SELECT NEXTVAL(s);
+------------+
| NEXTVAL(s) |
+------------+
|          2 |
+------------+

SELECT NEXTVAL(s);
ERROR 4084 (HY000): Sequence 'test.s' has run out

ALTER SEQUENCE s MAXVALUE=2 CYCLE;

SELECT NEXTVAL(s);
+------------+
| NEXTVAL(s) |
+------------+
|          1 |
+------------+
```

## See Also


* [Sequence Overview](../sequence-overview.md)
* [CREATE SEQUENCE](../create-sequence.md)
* [ALTER SEQUENCE](../alter-sequence.md)
* [PREVIOUS VALUE FOR](previous-value-for-sequence_name.md)
* [SETVAL()](setval.md). Set next value for the sequence.
* [AUTO_INCREMENT](../../../storage-engines/innodb/auto_increment-handling-in-innodb.md)
* [Information Schema SEQUENCES Table](../../sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-sequences-table.md)

