
# USER

## Syntax


```
USER()
```

## Description


Returns the current MariaDB user name and host name, given when authenticating to MariaDB, as a string in the utf8 [character set](../../../../../data-types/string-data-types/character-sets/README.md).


Note that the value of USER() may differ from the value of [CURRENT_USER()](current_user.md), which is the user used to authenticate the current client. [CURRENT_ROLE()](current_role.md) returns the current active role.


`SYSTEM_USER()` and, prior to [MariaDB 11.7](../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md), [SESSION_USER](session_user.md), are synonyms for `USER()`.


Statements using the `USER()` function or one of its synonyms are not [safe for statement level replication](../../../../../../server-usage/replication-cluster-multi-master/standard-replication/unsafe-statements-for-statement-based-replication.md).


## Examples


```
shell> mysql --user="anonymous"

SELECT USER(),CURRENT_USER();
+---------------------+----------------+
| USER()              | CURRENT_USER() |
+---------------------+----------------+
| anonymous@localhost | @localhost     |
+---------------------+----------------+
```

To select only the IP address, use [SUBSTRING_INDEX()](../../string-functions/substring_index.md),


```
SELECT SUBSTRING_INDEX(USER(), '@', -1);
+----------------------------------+
| SUBSTRING_INDEX(USER(), '@', -1) |
+----------------------------------+
| 192.168.0.101                    |
+----------------------------------+
```

## See Also


* [CURRENT_USER()](current_user.md)

