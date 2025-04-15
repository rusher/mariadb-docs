# MariaDB Environment Variables

MariaDB makes use of numerous environment variables that may be set on your system. Environment variables have the lowest precedence, so any options set on the command line or in an option file will take precedence.

It's usually better not to rely on environment variables, and to rather set the options you need directly, as this makes the system a little more robust and easy to administer.

Here is a list of environment variables used by MariaDB.

| Environment Variable | Description |
| --- | --- |
| Environment Variable | Description |
| CXX | Name of the C++ compiler, used for running CMake. |
| CC | Name of the C compiler, used for running CMake. |
| DBI_USER | Perl DBI default username. |
| DBI_TRACE | Perl DBI trace options. |
| HOME | Default directory for the [mysql_history file](../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md#the-mysql_history-file). |
| MYSQL_DEBUG | Debug trace options used when debugging. |
| MYSQL_GROUP_SUFFIX | In addition to the given option groups, also read groups with this suffix. |
| MYSQL_HISTFILE | Path to the [mysql_history file](../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md#the-mysql_history-file), overriding the $HOME/.mysql_history setting. |
| MYSQL_HOME | Path to the directory containing the [my.cnf file](/kb/en/configuring-mariadb-with-mycnf/) used by the server. |
| MYSQL_HOST | Default host name used by the [mariadb command line client](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/c/mariadb-client-library-for-c-200-release-notes). |
| MYSQL_PS1 | Command prompt for use by the [mariadb command line client](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/c/mariadb-client-library-for-c-200-release-notes). |
| MYSQL_PWD | Default password when connecting to mysqld. It is strongly recommended to use a more secure method of sending the password to the server. |
| MYSQL_TCP_PORT | Default TCP/IP port number. |
| MYSQL_UNIX_PORT | On Unix, default socket file used for localhost connections. |
| PATH | Path to directories that hold executable programs (such as the [mariadb client](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/c/mariadb-client-library-for-c-200-release-notes), [mariadb-admin](../../clients-and-utilities/mariadb-admin.md)), so that these can be run from any location. |
| TMPDIR | Directory where temporary files are created. |
| TZ | Local [time zone](../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md). |
| UMASK | Creation mode when creating files. See [Specifying Permissions for Schema (Data) Directories and Tables](starting-and-stopping-mariadb/specifying-permissions-for-schema-data-directories-and-tables.md). |
| UMASK_DIR | Creation mode when creating directories. See [Specifying Permissions for Schema (Data) Directories and Tables](starting-and-stopping-mariadb/specifying-permissions-for-schema-data-directories-and-tables.md). |
| USER | On Windows, up to [MariaDB 5.5](/kb/en/what-is-mariadb-55/), the default user name when connecting to the mysqld server. API GetUserName() is used in later versions. |