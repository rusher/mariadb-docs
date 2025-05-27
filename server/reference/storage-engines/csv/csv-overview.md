# CSV Overview

The CSV Storage Engine can read and append to files stored in CSV (comma-separated-values) format.

However, since [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), a better storage engine is able to read and write such files: [CONNECT](../connect/).

## The CSV storage engine and logging to tables

The CSV storage engine is the default storage engine when using [logging of SQL queries](../../../server-management/server-monitoring-logs/writing-logs-into-tables.md) to tables.

```
mysqld --log-output=table
```

## CSV Storage Engine files

When you create a table using the CSV storage engine, three files are created:

* `<table_name>.frm`
* `<table_name>.CSV`
* `<table_name>.CSM`

The `.frm` file is the table format file.

The `.CSV` file is a plain text file. Data you enter into the table is stored as plain text in comma-separated-values format.

The `.CSM` file stores metadata about the table such as the state and the number of rows in the table.

## Limitations

* CSV tables do not support indexing.
* CSV tables cannot be partitioned.
* Columns in CSV tables must be declared as NOT NULL.
* No [transactions](../../sql-statements/transactions/).
* The original CSV-format does not enable IETF-compatible parsing of embedded quote and comma characters. From [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes), it is possible to do so by setting the [IETF\_QUOTES](../../sql-statements/data-definition/create/create-table.md#ietf_quotes) option when creating a table.

## Examples

Forgetting to add NOT NULL:

```
CREATE TABLE csv_test (x INT, y DATE, z CHAR(10)) ENGINE=CSV;
ERROR 1178 (42000): The storage engine for the table doesn't support nullable columns
```

Creating, inserting and selecting:

```
CREATE TABLE csv_test (
  x INT NOT NULL, y DATE NOT NULL, z CHAR(10) NOT NULL
  ) ENGINE=CSV;
```

```
INSERT INTO csv_test VALUES
    (1,CURDATE(),'one'),
    (2,CURDATE(),'two'),
    (3,CURDATE(),'three');
```

```
SELECT * FROM csv_test;
+---+------------+-------+
| x | y          | z     |
+---+------------+-------+
| 1 | 2011-11-16 | one   |
| 2 | 2011-11-16 | two   |
| 3 | 2011-11-16 | three |
+---+------------+-------+
```

Viewing in a text editor:

```
$ cat csv_test.CSV
1,"2011-11-16","one"
2,"2011-11-16","two"
3,"2011-11-16","three"
```

## See Also

* [Checking and Repairing CSV Tables](checking-and-repairing-csv-tables.md)

CC BY-SA / Gnu FDL
