# INSERT IGNORE

## Ignoring Errors

Normally [INSERT](insert.md) stops and rolls back when it encounters an error.

By using the [IGNORE](ignore.md) keyword all errors are converted to warnings, which will not stop inserts of additional rows.

Invalid values are changed to the closest valid value and inserted, with a warning produced.

The IGNORE and DELAYED options are ignored when you use [ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md).

Prior to MySQL and [MariaDB 5.5.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/mariadb-5528-release-notes), no warnings were issued for duplicate key errors when using `IGNORE`.\
You can get the old behavior if you set [OLD\_MODE](../../../../server-management/variables-and-modes/old-mode.md) to `NO_DUP_KEY_WARNINGS_WITH_IGNORE`.

See [IGNORE](ignore.md) for a full description of effects.

## Examples

```
CREATE TABLE t1 (x INT UNIQUE);

INSERT INTO t1 VALUES(1),(2);

INSERT INTO t1 VALUES(2),(3);
ERROR 1062 (23000): Duplicate entry '2' for key 'x'
SELECT * FROM t1;
+------+
| x    |
+------+
|    1 |
|    2 |
+------+

INSERT IGNORE INTO t1 VALUES(2),(3);
Query OK, 1 row affected, 1 warning (0.04 sec)

SHOW WARNINGS;
+---------+------+---------------------------------+
| Level   | Code | Message                         |
+---------+------+---------------------------------+
| Warning | 1062 | Duplicate entry '2' for key 'x' |
+---------+------+---------------------------------+

SELECT * FROM t1;
+------+
| x    |
+------+
|    1 |
|    2 |
|    3 |
+------+
```

Converting values:

```
CREATE OR REPLACE TABLE t2(id INT, t VARCHAR(2) NOT NULL, n INT NOT NULL);

INSERT INTO t2(id) VALUES (1),(2);
ERROR 1364 (HY000): Field 't' doesn't have a default value

INSERT IGNORE INTO t2(id) VALUES (1),(2);
Query OK, 2 rows affected, 2 warnings (0.026 sec)
Records: 2  Duplicates: 0  Warnings: 2

SHOW WARNINGS;
+---------+------+----------------------------------------+
| Level   | Code | Message                                |
+---------+------+----------------------------------------+
| Warning | 1364 | Field 't' doesn't have a default value |
| Warning | 1364 | Field 'n' doesn't have a default value |
+---------+------+----------------------------------------+

SELECT * FROM t2;
+------+---+---+
| id   | t | n |
+------+---+---+
|    1 |   | 0 |
|    2 |   | 0 |
+------+---+---+
```

See [INSERT ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md) for further examples using that syntax.

## See Also

* [INSERT](insert.md)
* [INSERT DELAYED](insert-delayed.md)
* [INSERT SELECT](insert-select.md)
* [HIGH\_PRIORITY and LOW\_PRIORITY](../changing-deleting-data/high_priority-and-low_priority.md)
* [Concurrent Inserts](concurrent-inserts.md)
* [INSERT - Default & Duplicate Values](insert-default-duplicate-values.md)
* [INSERT ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md)

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
