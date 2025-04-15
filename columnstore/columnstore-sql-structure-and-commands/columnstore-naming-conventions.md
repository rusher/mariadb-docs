
# ColumnStore Naming Conventions

This lists the different naming conventions enforced by the column store, compared to the normal [MariaDB naming conventions](../../server/reference/sql-statements-and-structure/sql-language-structure/identifier-names.md).


* User names: 64 characters (MariaDB has 80)
* Table and column names are restricted to alphanumeric and underscore only, i.e "A-Z a-z 0-9 _".
* The first character of all table and column names should be an ASCII letter (a-z A-Z).
* ColumnStore reserves certain words that MariaDB does not, such as SELECT, CHAR and TABLE, so even wrapped in backticks these cannot be used.


## Reserved words


In addition to MariaDB Server [reserved words](../../server/reference/sql-statements-and-structure/sql-language-structure/reserved-words.md), ColumnStore has additional reserved words that cannot be used as table names, column names or user defined variables, functions or stored procedure names.



| Keyword |
| --- |
| Keyword |
| ACTION |
| ADD |
| ALTER |
| AUTO_INCREMENT |
| BIGINT |
| BIT |
| CASCADE |
| CHANGE |
| CHARACTER |
| CHARSET |
| CHECK |
| CLOB |
| COLUMN |
| COLUMNS |
| COMMENT |
| CONSTRAINT |
| CONSTRAINTS |
| CREATE |
| CURRENT_USER |
| DATETIME |
| DEC |
| DECIMAL |
| DEFERRED |
| DEFAULT |
| DEFERRABLE |
| DOUBLE |
| DROP |
| ENGINE |
| EXISTS |
| FOREIGN |
| FULL |
| IDB_BLOB |
| IDB_CHAR |
| IDB_DELETE |
| IDB_FLOAT |
| IDB_INT |
| IF |
| IMMEDIATE |
| INDEX |
| INITIALLY |
| INTEGER |
| KEY |
| MATCH |
| MAX_ROWS |
| MIN_ROWS |
| MODIFY |
| NO |
| NOT |
| NULL_TOK |
| NUMBER |
| NUMERIC |
| ON |
| PARTIAL |
| PRECISION |
| PRIMARY |
| REAL |
| REFERENCES |
| RENAME |
| RESTRICT |
| SESSION_USER |
| SET |
| SMALLINT |
| SYSTEM_USER |
| TABLE |
| TIME |
| TINYINT |
| TO |
| TRUNCATE |
| UNIQUE |
| UNSIGNED |
| UPDATE |
| USER |
| VARBINARY |
| VARCHAR |
| VARYING |
| WITH |
| ZONE |


