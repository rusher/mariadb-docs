# LOOP

#

# Syntax

```
[begin_label:] LOOP
 statement_list
END LOOP [end_label]
```

#

# Description

`LOOP` implements a simple loop construct, enabling repeated execution
of the statement list, which consists of one or more statements, each
terminated by a semicolon (i.e., `;`) statement delimiter. The statements
within the loop are repeated until the loop is exited; usually this is
accomplished with a [LEAVE](leave.md) statement.

A `LOOP` statement can be [labeled](labels.md). `end_label` cannot be given unless
`begin_label` also is present. If both are present, they must be the
same.

See [Delimiters](../../../clients-and-utilities/mariadb-client/delimiters.md) in the [mariadb](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/c/mariadb-client-library-for-c-200-release-notes) client for more on delimiter usage in the client.

#

# See Also

* [LOOP in Oracle mode](/kb/en/sql_modeoracle-from-mariadb-103/#loop)
* [ITERATE](iterate.md)
* [LEAVE](leave.md)
* [FOR Loops](../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/format_description_event.md)