
# Character Set and Collation Overview


## What Are Character Sets and Collations


A character set is a set of characters while a collation is the rules for comparing and sorting a particular character set.


For example, a subset of a character set could consist of the letters `<code>A</code>`, `<code>B</code>` and `<code>C</code>`. A default collation could define these as appearing in an ascending order of `<code>A, B, C</code>`.


If we consider different case characters, more complexity is added. A binary collation would evaluate the characters `<code>A</code>` and `<code>a</code>` differently, ordering them in a particular way. A case-insensitive collation would evaluate `<code>A</code>` and `<code>a</code>` equivalently, while the German phone book collation evaluates the characters `<code>ue</code>` and `<code>ü</code>` equivalently.


A character set can have many collations associated with it, while each collation is only associated with one character set. In MariaDB, the character set name is always part of the collation name. For example, the `<code>latin1_german1_ci</code>` collation applies only to the `<code>latin1</code>` character set. Each character set also has one default collation. The `<code>latin1</code>` default collation is `<code>latin1_swedish_ci</code>`.


As an example, by default, the character `<code>y</code>` comes between `<code>x</code>` and `<code>z</code>`, while in Lithuanian, it's sorted between `<code>i</code>` and `<code>k</code>`. Similarly, the German phone book order is different to the German dictionary order, so while they share the same character set, the collation is different.


## Viewing Character Sets and Collations


Prior to [MariaDB 11.6.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-0-release-notes.md), the default [character set](README.md) is `<code>latin1</code>` and the default collation is `<code>latin1_swedish_ci</code>`. In [MariaDB 11.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-116.md) the default character set is `<code>utf8mb4</code>` and the default collation is `<code>utf8mb4_uca1400_ai_ci</code>`.
This may differ in some distros, see for example [Differences in MariaDB in Debian](../../../../server-management/getting-installing-and-upgrading-mariadb/troubleshooting-installation-issues/installation-issues-on-debian-and-ubuntu/differences-in-mariadb-in-debian-and-ubuntu.md).


You can view a full list of character sets and collations supported by MariaDB at [Supported Character Sets and Collations](supported-character-sets-and-collations.md), or see what's supported on your server with the [SHOW CHARACTER SET](../../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-character-set.md) and [SHOW COLLATION](../../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-collation.md) commands.


By default, `<code>A</code>` comes before `<code>Z</code>`, so the following evaluates to true:


```
SELECT "A" < "Z";
+-----------+
| "A" < "Z" |
+-----------+
|         1 |
+-----------+
```

By default, comparisons are case-insensitive:


```
SELECT "A" < "a", "A" = "a";
+-----------+-----------+
| "A" < "a" | "A" = "a" |
+-----------+-----------+
|         0 |         1 |
+-----------+-----------+
```

## Changing Character Sets and Collations


Character sets and collations can be set from the server level right down to the column level, as well as for client-server communication.


For example, `<code>ue</code>` and `<code>ü</code>` are by default evaluated differently.


```
SELECT 'Mueller' = 'Müller';
+----------------------+
| 'Müller' = 'Mueller' |
+----------------------+
|                    0 |
+----------------------+
```

By using the [collation_connection](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variable to change the connection character set to `<code>latin1_german2_ci</code>`, or German phone book, the same two characters will evaluate as equivalent.


```
SET collation_connection = latin1_german2_ci;

SELECT 'Mueller' = 'Müller';
+-----------------------+
| 'Mueller' = 'Müller'  |
+-----------------------+
|                     1 |
+-----------------------+
```

See [Setting Character Sets and Collations](setting-character-sets-and-collations.md) for more.

