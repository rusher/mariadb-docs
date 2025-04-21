
# Information Schema COLLATIONS Table

The [Information Schema](../README.md) `COLLATIONS` table contains a list of supported [collations](../../../../../../data-types/string-data-types/character-sets/README.md).


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| COLLATION_NAME | Name of the collation. |
| CHARACTER_SET_NAME | Associated character set. |
| ID | Collation id. |
| IS_DEFAULT | Whether the collation is the character set's default. |
| IS_COMPILED | Whether the collation is compiled into the server. |
| SORTLEN | Sort length, used for determining the memory used to sort strings in this collation. |
| COMMENT | For utf8mb4_0900 collations, contains the corresponding alias collation. From [MariaDB 11.4.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-5-release-notes), [MariaDB 11.7.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-11-7-rolling-releases/mariadb-11-7-2-release-notes), [MariaDB 11.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-11-8-series/mariadb-11-8-1-release-notes). |



The [SHOW COLLATION](../../../show/show-collation.md) statement returns the same results and both can be reduced in a similar way.


For example, in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-6-series/what-is-mariadb-106), the following two statements return the same results:


```
SHOW COLLATION WHERE Charset LIKE 'utf8mb3';
```

and


```
SELECT * FROM information_schema.COLLATIONS 
WHERE CHARACTER_SET_NAME LIKE 'utf8mb3';
```

In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-5-series/what-is-mariadb-105) and before, `utf8` should be specified instead of `utf8mb3`.


## NO PAD collations


`NO PAD` collations regard trailing spaces as normal characters. You can get a list of all `NO PAD` collations as follows:


```
SELECT collation_name FROM information_schema.COLLATIONS
WHERE collation_name LIKE "%nopad%";  
+------------------------------+
| collation_name               |
+------------------------------+
| big5_chinese_nopad_ci        |
| big5_nopad_bin               |
...
```

## Example


```
SELECT * FROM information_schema.COLLATIONS;
+------------------------------+--------------------+------+------------+-------------+---------+
| COLLATION_NAME               | CHARACTER_SET_NAME | ID   | IS_DEFAULT | IS_COMPILED | SORTLEN |
+------------------------------+--------------------+------+------------+-------------+---------+
| big5_chinese_ci              | big5               |    1 | Yes        | Yes         |       1 |
| big5_bin                     | big5               |   84 |            | Yes         |       1 |
| big5_chinese_nopad_ci        | big5               | 1025 |            | Yes         |       1 |
| big5_nopad_bin               | big5               | 1108 |            | Yes         |       1 |
| dec8_swedish_ci              | dec8               |    3 | Yes        | Yes         |       1 |
| dec8_bin                     | dec8               |   69 |            | Yes         |       1 |
| dec8_swedish_nopad_ci        | dec8               | 1027 |            | Yes         |       1 |
| dec8_nopad_bin               | dec8               | 1093 |            | Yes         |       1 |
| cp850_general_ci             | cp850              |    4 | Yes        | Yes         |       1 |
| cp850_bin                    | cp850              |   80 |            | Yes         |       1 |
...
```

## See Also


* [Setting Character Sets and Collations](../../../../../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md) - specifying the character set at the server, database, table and column levels
* [Supported Character Sets and Collations](../../../../../../data-types/string-data-types/character-sets/supported-character-sets-and-collations.md) - full list of supported characters sets and collations.

