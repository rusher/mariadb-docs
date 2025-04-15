
# ALTER SEQUENCE

## Syntax


```
ALTER SEQUENCE [IF EXISTS] sequence_name
[ INCREMENT [ BY | = ] number ]
[ MINVALUE [=] number | NO MINVALUE | NOMINVALUE ]
[ MAXVALUE [=] number | NO MAXVALUE | NOMAXVALUE ]
[ START [ WITH | = ] number ] [ CACHE [=] number ] [ [ NO ] CYCLE ]
[ RESTART [[WITH | =] number]
```


`<code>ALTER SEQUENCE</code>` allows one to change any values for a `<code>SEQUENCE</code>` created with [CREATE SEQUENCE](create-sequence.md).


The options for `<code>ALTER SEQUENCE</code>` can be given in any order.


## Description


`<code>ALTER SEQUENCE</code>` changes the parameters of an existing sequence generator. Any parameters not specifically set in the `<code>ALTER SEQUENCE</code>` command retain their prior settings.


`<code>ALTER SEQUENCE</code>` requires the [ALTER privilege](../sql-statements/account-management-sql-commands/grant.md).


### Arguments to `<code>ALTER SEQUENCE</code>`


The following options may be used:



| Option | Default value | Description |
| --- | --- | --- |
| Option | Default value | Description |
| INCREMENT | 1 | Increment to use for values. May be negative. |
| MINVALUE | 1 if INCREMENT > 0 and -9223372036854775807 if INCREMENT < 0 | Minimum value for the sequence. |
| MAXVALUE | 9223372036854775806 if INCREMENT > 0 and -1 if INCREMENT < 0 | Max value for sequence. |
| START | MINVALUE if INCREMENT > 0 and MAX_VALUE if INCREMENT< 0 | First value that the sequence will generate. |
| CACHE | 1000 | Number of values that should be cached. 0 if no CACHE. The underlying table will be updated first time a new sequence number is generated and each time the cache runs out. |
| CYCLE | 0 (= NO CYCLE) | 1 if the sequence should start again from MINVALUE

# after it has run out of values. |
| RESTART | START if restart value not is given | If RESTART option is used, NEXT VALUE will return the restart value. |



The optional clause `<code>RESTART [ WITH restart ]</code>` sets the next value for the sequence. This is equivalent to calling the [SETVAL()](sequence-functions/setval.md) function with the `<code>is_used</code>` argument as 0. The specified value will be returned by the next call of nextval. Using `<code>RESTART</code>` with no restart value is
equivalent to supplying the start value that was recorded by
[CREATE SEQUENCE](create-sequence.md) or last set by `<code>ALTER SEQUENCE START WITH</code>`.


`<code>ALTER SEQUENCE</code>` will not allow you to change the sequence so that it's inconsistent. For example:


```
CREATE SEQUENCE s1;
ALTER SEQUENCE s1 MINVALUE 10;
ERROR 4061 (HY000): Sequence 'test.t1' values are conflicting

ALTER SEQUENCE s1 MINVALUE 10 RESTART 10;
ERROR 4061 (HY000): Sequence 'test.t1' values are conflicting

ALTER SEQUENCE s1 MINVALUE 10 START 10 RESTART 10;
```

### INSERT


To allow `<code>SEQUENCE</code>` objects to be backed up by old tools, like [mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md), one can use `<code>SELECT</code>` to read the current state of a `<code>SEQUENCE</code>` object and use an `<code>INSERT</code>` to update the `<code>SEQUENCE</code>` object. `<code>INSERT</code>` is only allowed if all fields are specified:



```
CREATE SEQUENCE s1;
INSERT INTO s1 VALUES(1000,10,2000,1005,1,1000,0,0);
SELECT * FROM s1;

+------------+-----------+-----------+-------+-----------+-------+-------+-------+
| next_value | min_value | max_value | start | increment | cache | cycle | round |
+------------+-----------+-----------+-------+-----------+-------+-------+-------+
|       1000 |        10 |      2000 |  1005 |         1 |  1000 |     0 |     0 |
+------------+-----------+-----------+-------+-----------+-------+-------+-------+

SHOW CREATE SEQUENCE s1;
+-------+--------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                 |
+-------+--------------------------------------------------------------------------------------------------------------+
| s1    | CREATE SEQUENCE `s1` start with 1005 minvalue 10 maxvalue 2000 increment by 1 cache 1000 nocycle ENGINE=Aria |
+-------+--------------------------------------------------------------------------------------------------------------+
```


### Notes


`<code>ALTER SEQUENCE</code>` will instantly affect all future `<code>SEQUENCE</code>` operations. This is in contrast to some other databases where the changes requested by `<code>ALTER SEQUENCE</code>` will not be seen until the sequence cache has run out.


`<code>ALTER SEQUENCE</code>` will take a full table lock of the sequence object during
its (brief) operation. This ensures that `<code>ALTER SEQUENCE</code>` is replicated
correctly. If you only want to set the next sequence value to a
higher value than current, then you should use [SETVAL()](sequence-functions/setval.md)
instead, as this is not blocking.


If you want to change storage engine, sequence comment or rename the sequence, you can use [ALTER TABLE](../sql-statements/data-definition/alter/alter-tablespace.md) for this.


## See Also


* [Sequence Overview](sequence-overview.md)
* [CREATE SEQUENCE](create-sequence.md)
* [DROP SEQUENCE](drop-sequence.md)
* [NEXT VALUE FOR](sequence-functions/next-value-for-sequence_name.md)
* [PREVIOUS VALUE FOR](sequence-functions/previous-value-for-sequence_name.md)
* [SETVAL()](sequence-functions/setval.md). Set next value for the sequence.
* [AUTO INCREMENT](../../storage-engines/innodb/auto_increment-handling-in-innodb.md)
* [ALTER TABLE](../sql-statements/data-definition/alter/alter-tablespace.md)
* [Information Schema SEQUENCES Table](../sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-sequences-table.md)

