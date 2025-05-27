# About SHOW

`SHOW` has many forms that provide information about\
databases, tables, columns, or status information about the server. These include:

* [SHOW AUTHORS](show-authors.md)
* [SHOW BINLOG STATUS](show-binlog-status.md)
* [SHOW CHARACTER SET \[like\_or\_where\]](show-character-set.md)
* [SHOW COLLATION \[like\_or\_where\]](show-collation.md)
* [SHOW \[FULL\] COLUMNS FROM tbl\_name \[FROM db\_name\] \[like\_or\_where\]](show-columns.md)
* [SHOW CONTRIBUTORS](show-contributors.md)
* [SHOW CREATE DATABASE db\_name](show-create-database.md)
* [SHOW CREATE EVENT event\_name](show-create-event.md)
* [SHOW CREATE FUNCTION](show-create-function.md)
* [SHOW CREATE PACKAGE package\_name](show-create-package.md)
* [SHOW CREATE PACKAGE BODY package\_name](show-create-package-body.md)
* [SHOW CREATE PROCEDURE proc\_name](show-create-procedure.md)
* [SHOW CREATE SEQUENCE sequence\_name](show-create-sequence.md)
* [SHOW CREATE TABLE tbl\_name](show-create-table.md)
* [SHOW CREATE TRIGGER trigger\_name](show-create-trigger.md)
* [SHOW CREATE USER user](show-create-user.md)
* [SHOW CREATE VIEW view\_name](show-create-view.md)
* [SHOW DATABASES \[like\_or\_where\]](show-databases.md)
* [SHOW ENGINE engine\_name {STATUS | MUTEX}](show-engine.md)
* [SHOW \[STORAGE\] ENGINES](show-engines.md)
* [SHOW ERRORS \[LIMIT \[offset,\] row\_count\]](show-errors.md)
* [SHOW \[FULL\] EVENTS](show-events.md)
* [SHOW FUNCTION CODE func\_name](show-function-code.md)
* [SHOW FUNCTION STATUS \[like\_or\_where\]](show-function-status.md)
* [SHOW GRANTS FOR user](show-grants.md)
* [SHOW INDEX FROM tbl\_name \[FROM db\_name\]](show-index.md)
* [SHOW INDEX\_STATISTICS](show-index-statistics.md)
* [SHOW LOCALES](show-locales.md)
* [SHOW MASTER STATUS](show-binlog-status.md)
* [SHOW OPEN TABLES \[FROM db\_name\] \[like\_or\_where\]](show-open-tables.md)
* [SHOW PACKAGE BODY STATUS](show-package-body-status.md)
* [SHOW PACKAGE STATUS](show-package-status.md)
* [SHOW PLUGINS](show-plugins.md)
* [SHOW PROCEDURE CODE proc\_name](show-procedure-code.md)
* [SHOW PROCEDURE STATUS \[like\_or\_where\]](show-procedure-status.md)
* [SHOW PRIVILEGES](show-privileges.md)
* [SHOW \[FULL\] PROCESSLIST](show-processlist.md)
* [SHOW PROFILE \[types\] \[FOR QUERY n\] \[OFFSET n\] \[LIMIT n\]](show-profile.md)
* [SHOW PROFILES](show-profiles.md)
* [SHOW QUERY\_RESPONSE\_TIME](show-query_response_time.md)
* [SHOW RELAYLOG EVENTS](show-relaylog-events.md)
* [SHOW REPLICA HOSTS](show-replica-hosts.md)
* [SHOW REPLICA STATUS](show-replica-status.md)
* [SHOW \[GLOBAL | SESSION\] STATUS \[like\_or\_where\]](show-status.md)
* [SHOW TABLE STATUS \[FROM db\_name\] \[like\_or\_where\]](show-table-status.md)
* [SHOW TABLE\_STATISTICS](show-table-statistics.md)
* [SHOW TABLES \[FROM db\_name\] \[like\_or\_where\]](show-tables.md)
* [SHOW TRIGGERS \[FROM db\_name\] \[like\_or\_where\]](show-triggers.md)
* [SHOW USER\_STATISTICS](show-user-statistics.md)
* [SHOW USER\_VARIABLES](../../../plugins/other-plugins/user-variables-plugin.md)
* [SHOW \[GLOBAL | SESSION\] VARIABLES \[like\_or\_where\]](show-variables.md)
* [SHOW WARNINGS \[LIMIT \[offset,\] row\_count\]](show-warnings.md)
* [SHOW WSREP\_MEMBERSHIP](show-wsrep_membership.md)
* [SHOW WSREP\_STATUS](show-wsrep_status.md)

```
like_or_where:
    LIKE 'pattern'
  | WHERE expr
```

If the syntax for a given `SHOW` statement includes a`LIKE 'pattern'` part, `'pattern'` is a\
string that can contain the SQL "`%`" and\
"`_`" wildcard characters. The pattern is useful for\
restricting statement output to matching values.

Several `SHOW` statements also accept a`WHERE` clause that provides more flexibility in specifying\
which rows to display. See [Extended Show](extended-show.md).

GPLv2 fill\_help\_tables.sql
