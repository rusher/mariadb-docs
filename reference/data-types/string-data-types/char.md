# CHAR

This article covers the CHAR data type. See [CHAR Function](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/char-function.md) for the function.

#

# Syntax

```
[NATIONAL] CHAR[(M)] [CHARACTER SET charset_name] [COLLATE collation_name]
```

#

# Description

A fixed-length string that is always right-padded with spaces to the specified
length when stored. `M` represents the column length in characters. The range
of `M` is `0` to `255`. If `M` is omitted, the length is `1`.

CHAR(0) columns can contain 2 values: an empty string or NULL. Such columns cannot be part of an index. The [CONNECT](../../../security/user-account-management/catalogs/connecting-to-a-server-configured-for-catalogs.md) storage engine does not support CHAR(0).

**Note:** Trailing spaces are removed when `CHAR` values are retrieved
unless the `PAD_CHAR_TO_FULL_LENGTH` [SQL mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/sql_modemssql) is enabled.

Before [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-102), all collations were of type PADSPACE, meaning that CHAR (as well as [VARCHAR](varchar.md) and [TEXT](text.md)) values are compared without regard for trailing spaces. This does not apply to the [LIKE](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/like.md) pattern-matching operator, which takes into account trailing spaces.

If a unique index consists of a column where trailing pad characters are stripped or ignored, inserts into that column where values differ only by the number of trailing pad characters will result in a duplicate-key error.

#

# Examples

Trailing spaces:

```
CREATE TABLE strtest (c CHAR(10));
INSERT INTO strtest VALUES('Maria ');

SELECT c='Maria',c='Maria ' FROM strtest;
+-----------+--------------+
| c='Maria' | c='Maria ' |
+-----------+--------------+
| 1 | 1 |
+-----------+--------------+

SELECT c LIKE 'Maria',c LIKE 'Maria ' FROM strtest;
+----------------+-------------------+
| c LIKE 'Maria' | c LIKE 'Maria ' |
+----------------+-------------------+
| 1 | 0 |
+----------------+-------------------+
```

#

# NO PAD Collations

NO PAD collations regard trailing spaces as normal characters. You can get a list of all NO PAD collations by querying the [Information Schema Collations table](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-collations-table.md), for example:

```
SELECT collation_name FROM information_schema.collations 
 WHERE collation_name LIKE "%nopad%"; 
+------------------------------+
| collation_name |
+------------------------------+
| big5_chinese_nopad_ci |
| big5_nopad_bin |
...
```

#

# See Also

* [CHAR Function](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/char-function.md)
* [VARCHAR](varchar.md)
* [BINARY](../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)