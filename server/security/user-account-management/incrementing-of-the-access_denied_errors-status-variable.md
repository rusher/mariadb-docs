
# Incrementing of the access_denied_errors status variable

The [access_denied_errors](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#access_denied_errors) status variable is incremented when someone tries to access something they do not have rights to.


This happens in the following cases:


* When accessing a database, table or column that the user does not have rights to access. This error is sent to the client.
* When a login fails because of wrong user/password etc. The error is printed to the general log.
* If require_secure_transport option is enabled in the server and the user has not used a secure transport. The error is sent to the user.
* Users try to change to a database/schema they do not have access to. A warning is written to the error log if log_warnings > 1.
* Users try to use a SHOW command to access an object they do not have rights to see. The error is sent to the client.
* Users access something that requires global access, like "CREATE SERVER". The error is sent to the client.


Login failures can be found in the [general log](../../server-management/server-monitoring-logs/general-query-log.md). Errors that are sent to the user can be found by using the [SQL Error Log Plugin](../../server-management/server-monitoring-logs/sql-error-log-plugin.md). The plugin captures all errors sent to the client. From [MariaDB 10.11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-5-release-notes), it can also optionally capture all warnings sent to the client.


### See Also


* [Troubleshooting Connection Issues](https://app.gitbook.com/s/iJPrPCGi329TSR8WIXJW/learning-and-training/training-and-tutorials/basic-mariadb-articles/troubleshooting-connection-issues)
* [GRANT](../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md)
* [Error 1045: Access denied for user (using password)](../../reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-1000-to-1099/e1045.md)

