
# Information Schema COLLATION_CHARACTER_SET_APPLICABILITY Table

The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>COLLATION_CHARACTER_SET_APPLICABILITY</code>` table shows which [character sets](../../../../../../data-types/string-data-types/character-sets/README.md) are associated with which collations.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| COLLATION_NAME | Collation name. |
| CHARACTER_SET_NAME | Name of the associated character set. |
| FULL_COLLATION_NAME | Name of the associated character set/collation combination. Added in [MariaDB 10.10.1](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10101-release-notes.md). |
| ID | The unique identifier of this character set/collation combination. Added in [MariaDB 10.10.1](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10101-release-notes.md). |
| IS_DEFAULT | If the collation is the default for this character set. Added in [MariaDB 10.10.1](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10101-release-notes.md). |



The `<code>[COLLATIONS](information-schema-collations-table.md)</code>` table is table of the base `<code>COLLATION_NAMES</code>` in the same way that `<code>[CHARACTER_SETS](https://mariadb.com/kb/en/information-schema-character-sets-table)</code>` table is table of the base `<code>CHARACTER_SET_NAMES</code>`. The `<code>COLLATION_CHARACTER_SET_APPLICABILITY</code>` table is the mapping between collations and character sets.


When joining the `<code>[information_schema.TABLES](information-schema-tables-table.md)</code>` table with its field `<code>TABLE_COLLATIONS</code>`, this should be joined to `<code>FULL_COLLATION_NAME</code>` in the `<code>COLLATION_CHARACTER_SET_APPLICABILITY</code>` table.


See [Setting Character Sets and Collations](../../../../../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md) for details on specifying the character set at the server, database, table and column levels.


## Example


```
SELECT * FROM information_schema.COLLATION_CHARACTER_SET_APPLICABILITY  WHERE
  CHARACTER_SET_NAME='utf32' ORDER BY IS_DEFAULT DESC, ID LIMIT 10;
+--------------------+--------------------+---------------------+-----+------------+
| COLLATION_NAME     | CHARACTER_SET_NAME | FULL_COLLATION_NAME | ID  | IS_DEFAULT |
+--------------------+--------------------+---------------------+-----+------------+
| utf32_general_ci   | utf32              | utf32_general_ci    |  60 | Yes        |
| utf32_bin          | utf32              | utf32_bin           |  61 |            |
| utf32_unicode_ci   | utf32              | utf32_unicode_ci    | 160 |            |
| utf32_icelandic_ci | utf32              | utf32_icelandic_ci  | 161 |            |
| utf32_latvian_ci   | utf32              | utf32_latvian_ci    | 162 |            |
| utf32_romanian_ci  | utf32              | utf32_romanian_ci   | 163 |            |
| utf32_slovenian_ci | utf32              | utf32_slovenian_ci  | 164 |            |
| utf32_polish_ci    | utf32              | utf32_polish_ci     | 165 |            |
| utf32_estonian_ci  | utf32              | utf32_estonian_ci   | 166 |            |
| utf32_spanish_ci   | utf32              | utf32_spanish_ci    | 167 |            |
+--------------------+--------------------+---------------------+-----+------------+
10 rows in set (0.004 sec)
```
