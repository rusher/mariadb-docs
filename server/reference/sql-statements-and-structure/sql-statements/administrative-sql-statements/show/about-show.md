
# About SHOW

`<code class="highlight fixed" style="white-space:pre-wrap">SHOW</code>` has many forms that provide information about
databases, tables, columns, or status information about the server. These include:


* [SHOW AUTHORS](show-authors.md)
* [SHOW BINLOG STATUS](show-binlog-status.md)
* [SHOW CHARACTER SET [like_or_where]](show-character-set.md)
* [SHOW COLLATION [like_or_where]](show-collation.md)
* [SHOW [FULL] COLUMNS FROM tbl_name [FROM db_name] [like_or_where]](show-columns.md)
* [SHOW CONTRIBUTORS](show-contributors.md)
* [SHOW CREATE DATABASE db_name](show-create-database.md)
* [SHOW CREATE EVENT event_name](show-create-event.md)
* [SHOW CREATE FUNCTION](show-create-function.md)
* [SHOW CREATE PACKAGE package_name](show-create-package.md)
* [SHOW CREATE PACKAGE BODY package_name](show-create-package-body.md)
* [SHOW CREATE PROCEDURE proc_name](show-create-procedure.md)
* [SHOW CREATE SEQUENCE sequence_name](show-create-sequence.md)
* [SHOW CREATE TABLE tbl_name](show-create-table.md)
* [SHOW CREATE TRIGGER trigger_name](show-create-trigger.md)
* [SHOW CREATE USER user](show-create-user.md)
* [SHOW CREATE VIEW view_name](show-create-view.md)
* [SHOW DATABASES [like_or_where]](show-databases.md)
* [SHOW ENGINE engine_name {STATUS | MUTEX}](show-engine-innodb-status.md)
* [SHOW [STORAGE] ENGINES](show-engines.md)
* [SHOW ERRORS [LIMIT [offset,] row_count]](show-errors.md)
* [SHOW [FULL] EVENTS](show-events.md)
* [SHOW FUNCTION CODE func_name](show-function-code.md)
* [SHOW FUNCTION STATUS [like_or_where]](show-function-status.md)
* [SHOW GRANTS FOR user](show-grants.md)
* [SHOW INDEX FROM tbl_name [FROM db_name]](show-index.md)
* [SHOW INDEX_STATISTICS](show-index-statistics.md)
* [SHOW LOCALES](show-locales.md)
* [SHOW MASTER STATUS](show-binlog-status.md)
* [SHOW OPEN TABLES [FROM db_name] [like_or_where]](show-open-tables.md)
* [SHOW PACKAGE BODY STATUS](show-package-body-status.md)
* [SHOW PACKAGE STATUS](show-package-status.md)
* [SHOW PLUGINS](show-plugins-soname.md)
* [SHOW PROCEDURE CODE proc_name](show-procedure-code.md)
* [SHOW PROCEDURE STATUS [like_or_where]](show-procedure-status.md)
* [SHOW PRIVILEGES](show-privileges.md)
* [SHOW [FULL] PROCESSLIST](show-processlist.md)
* [SHOW PROFILE [types] [FOR QUERY n] [OFFSET n] [LIMIT n]](show-profile.md)
* [SHOW PROFILES](show-profiles.md)
* [SHOW QUERY_RESPONSE_TIME](show-query_response_time.md)
* [SHOW RELAYLOG EVENTS](show-relaylog-events.md)
* [SHOW REPLICA HOSTS](show-replica-hosts.md)
* [SHOW REPLICA STATUS](show-replica-status.md)
* [SHOW [GLOBAL | SESSION] STATUS [like_or_where]](show-status.md)
* [SHOW TABLE STATUS [FROM db_name] [like_or_where]](show-table-status.md)
* [SHOW TABLE_STATISTICS](show-table-statistics.md)
* [SHOW TABLES [FROM db_name] [like_or_where]](show-tables.md)
* [SHOW TRIGGERS [FROM db_name] [like_or_where]](show-triggers.md)
* [SHOW USER_STATISTICS](show-user-statistics.md)
* [SHOW USER_VARIABLES](../../../../plugins/other-plugins/user-variables-plugin.md)
* [SHOW [GLOBAL | SESSION] VARIABLES [like_or_where]](show-variables.md)
* [SHOW WARNINGS [LIMIT [offset,] row_count]](show-warnings.md)
* [SHOW WSREP_MEMBERSHIP](show-wsrep_membership.md)
* [SHOW WSREP_STATUS](show-wsrep_status.md)


```
like_or_where:
    LIKE 'pattern'
  | WHERE expr
```

If the syntax for a given `<code class="highlight fixed" style="white-space:pre-wrap">SHOW</code>` statement includes a
`<code class="highlight fixed" style="white-space:pre-wrap">LIKE 'pattern'</code>` part, `<code class="highlight fixed" style="white-space:pre-wrap">'pattern'</code>` is a
string that can contain the SQL "`<code class="highlight fixed" style="white-space:pre-wrap">%</code>`" and
"`<code class="highlight fixed" style="white-space:pre-wrap">_</code>`" wildcard characters. The pattern is useful for
restricting statement output to matching values.


Several `<code class="highlight fixed" style="white-space:pre-wrap">SHOW</code>` statements also accept a
`<code class="highlight fixed" style="white-space:pre-wrap">WHERE</code>` clause that provides more flexibility in specifying
which rows to display. See [Extended Show](extended-show.md).

