# Identifier to File Name Mapping

Some identifiers map to a file name on the filesystem. Databases each have their own directory, while, depending on the [storage engine](../../../server-usage/storage-engines/), table names and index names may map to a file name.

Not all characters that are allowed in table names can be used in file names. Every filesystem has its own rules of what characters can be used in file names. To let the user create tables using all characters allowed in the SQL Standard and to not depend on whatever particular filesystem a particular database resides, MariaDB encodes "potentially unsafe" characters in the table name to derive the corresponding file name.

This is implemented using a special character set. MariaDB converts a table name to the "filename" character set to get the file name for this table. And it converts the file name from the "filename" character set to, for example, utf8 to get the table name for this file name.

The conversion rules are as follows: if the identifier is made up only of basic Latin numbers, letters and/or the underscore character, the encoding matches the name (see however [Identifier Case Sensitivity](identifier-case-sensitivity.md)). Otherwise they are encoded according to the following table:

| Code Range | Pattern            | Number     | Used | Unused | Blocks                                |
| ---------- | ------------------ | ---------- | ---- | ------ | ------------------------------------- |
| Code Range | Pattern            | Number     | Used | Unused | Blocks                                |
| 00C0..017F | \[@]\[0..4]\[g..z] | 5\*20= 100 | 97   | 3      | Latin-1 Supplement + Latin Extended-A |
| 0370..03FF | \[@]\[5..9]\[g..z] | 5\*20= 100 | 88   | 12     | Greek and Coptic                      |
| 0400..052F | \[@]\[g..z]\[0..6] | 20\*7= 140 | 137  | 3      | Cyrillic + Cyrillic Supplement        |
| 0530..058F | \[@]\[g..z]\[7..8] | 20\*2= 40  | 38   | 2      | Armenian                              |
| 2160..217F | \[@]\[g..z]\[9]    | 20\*1= 20  | 16   | 4      | Number Forms                          |
| 0180..02AF | \[@]\[g..z]\[a..k] | 20\*11=220 | 203  | 17     | Latin Extended-B + IPA Extensions     |
| 1E00..1EFF | \[@]\[g..z]\[l..r] | 20\*7= 140 | 136  | 4      | Latin Extended Additional             |
| 1F00..1FFF | \[@]\[g..z]\[s..z] | 20\*8= 160 | 144  | 16     | Greek Extended                        |
| .... ....  | \[@]\[a..f]\[g..z] | 6\*20= 120 | 0    | 120    | RESERVED                              |
| 24B6..24E9 | \[@]\[@]\[a..z]    | 26         | 26   | 0      | Enclosed Alphanumerics                |
| FF21..FF5A | \[@]\[a..z]\[@]    | 26         | 26   | 0      | Halfwidth and Fullwidth forms         |

Code Range values are UCS-2.

All of this encoding happens transparently at the filesystem level with one exception. Until MySQL 5.1.6, an old encoding was used. Identifiers created in a version before MySQL 5.1.6, and which haven't been updated to the new encoding, the server prefixes `mysql50` to their name.

### Examples

Find the file name for a table with a non-Latin1 name:

```
select cast(convert("this_is_таблица" USING filename) as binary);
+------------------------------------------------------------------+
| cast(convert("this_is_таблица" USING filename) as binary)        |
+------------------------------------------------------------------+
| this_is_@y0@g0@h0@r0@o0@i1@g0                                    |
+------------------------------------------------------------------+
```

Find the table name for a file name:

```
select convert(_filename "this_is_@y0@g0@h0@r0@o0@i1@g0" USING utf8);
+---------------------------------------------------------------+
| convert(_filename "this_is_@y0@g0@h0@r0@o0@i1@g0" USING utf8) |
+---------------------------------------------------------------+
| this_is_таблица                                               |
+---------------------------------------------------------------+
```

An old table created before MySQL 5.1.6, with the old encoding:

```
SHOW TABLES;
+--------------------+
| Tables_in_test     |
+--------------------+
| #mysql50#table@1   |
+--------------------+
```

The prefix needs to be supplied to reference this table:

```
SHOW COLUMNS FROM `table@1`;
ERROR 1146 (42S02): Table 'test.table@1' doesn't exist

SHOW COLUMNS FROM `#mysql50#table@1`;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| i     | int(11) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
```

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
