
# Information Schema USERS Table


##### MariaDB starting with [11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115)
The [Information Schema](../README.md) `USERS` table contains information about users, [password expiry](../../../../../../../security/user-account-management/user-password-expiry.md), and the limits set by [max_password_errors](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_password_errors). Unprivileged users can access their own data, which is different to what [mysql.global_priv](../../the-mysql-database-tables/mysql-global_priv-table.md) provides.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| USER | In the format user_name@host_name. |
| PASSWORD_ERRORS | A current accumulated value of consecutive password login failures. If password_errors is not applicable for the user (see [max_password_errors](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_password_errors)), PASSWORD_ERRORS will be NULL. Only password login attempts with nonempty password are taken into account. |
| PASSWORD_EXPIRATION_TIME | A timestamp with the exact point in time calculated from password_last_changed and password_lifetime (i.e. days) stored for the user. |


