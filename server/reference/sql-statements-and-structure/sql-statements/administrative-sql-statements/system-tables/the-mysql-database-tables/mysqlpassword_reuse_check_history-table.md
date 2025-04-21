
# mysql.password_reuse_check_history Table


##### MariaDB starting with [10.7.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1070-release-notes)
The mysql.password_reuse_check_history Table is installed as part of the [password_reuse_check plugin](../../../../../plugins/password-validation-plugins/password-reuse-check-plugin.md), available from [MariaDB 10.7.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1070-release-notes).


The `mysql.password_reuse_check_history` table stores old passwords, so that when a user sets a new password, it can be checked for purposes of preventing password reuse.


It contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| hash | binary(64) | NO | PRI | NULL |  |
| time | timestamp | NO | MUL | current_timestamp() |  |


