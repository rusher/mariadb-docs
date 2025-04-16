
# MariaDB Server Docker Official Image Environment Variables

When you start the image, you can adjust the initialization of the MariaDB Server instance by passing one or more environment variables on the docker run command line. Do note that all of the variables below, except `MARIADB_AUTO_UPGRADE`, will have no effect if you start the container with a data directory that already contains a database: any pre-existing database will always be left untouched on container startup.


From tag 10.2.38, 10.3.29, 10.4.19, 10.5.10 onwards, and all 10.6 and later tags, the MARIADB_* equivalent variables are provided. MARIADB_* variants will always be used in preference to MYSQL_* variants.


One of MARIADB_ROOT_PASSWORD_HASH, MARIADB_ROOT_PASSWORD, MARIADB_ALLOW_EMPTY_ROOT_PASSWORD, or MARIADB_RANDOM_ROOT_PASSWORD (or equivalents, including *_FILE), is required. The other environment variables are optional.


### MARIADB_ROOT_PASSWORD_HASH / MARIADB_ROOT_PASSWORD / MYSQL_ROOT_PASSWORD


This specifies the password that will be set for the MariaDB root superuser account.


### MARIADB_ALLOW_EMPTY_ROOT_PASSWORD / MYSQL_ALLOW_EMPTY_PASSWORD


Set to a non-empty value, like `1`, to allow the container to be started with a blank password for the root user. NOTE: Setting this variable to yes is not recommended unless you really know what you are doing, since this will leave your MariaDB instance completely unprotected, allowing anyone to gain complete superuser access.


### MARIADB_RANDOM_ROOT_PASSWORD / MYSQL_RANDOM_ROOT_PASSWORD


Set to a non-empty value, like yes, to generate a random initial password for the root user. The generated root password will be printed to stdout (GENERATED ROOT PASSWORD: .....).


### MARIADB_ROOT_HOST / MYSQL_ROOT_HOST


This is the hostname part of the root user created. By default this is %, however it can be set to any default MariaDB allowed hostname component. Setting this to localhost will prevent any root user being accessible except via the unix socket.


### MARIADB_DATABASE / MYSQL_DATABASE


This variable allows you to specify the name of a database to be created on image startup.


### MARIADB_USER / MYSQL_USER, MARIADB_PASSWORD_HASH / MARIADB_PASSWORD / MYSQL_PASSWORD


Both user and password variables, along with a database, are required for a user to be created. This user will be granted all access (corresponding to GRANT ALL) to the MARIADB_DATABASE database.


Do not use this mechanism to create the root superuser, that user gets created by default with the password specified by the MARIADB_ROOT_PASSWORD / MYSQL_ROOT_PASSWORD variable.


### MARIADB_MYSQL_LOCALHOST_USER / MARIADB_MYSQL_LOCALHOST_GRANTS


Set MARIADB_MYSQL_LOCALHOST_USER to a non-empty value to create the mysql@locahost database user. This user is especially useful for a variety of health checks and backup scripts.


The mysql@localhost user gets `[USAGE](../../../../../ref/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#usage)` privileges by default. If more access is required, additional global privileges in the form of a comma separated list can be provided. If you are sharing a volume containing MariaDB's unix socket (/var/run/mysqld by default), privileges beyond `[USAGE](../../../../../ref/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#usage)` can result in confidentiality, integrity and availability risks, so use a minimal set. Its also possible to use for [Mariadb-backup](../../../../backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md). The [healthcheck.sh](using-healthcheck-sh.md) script also documents the required privileges for each health check test.


### MARIADB_HEALTHCHECK_GRANTS


Set MARIADB_HEALTHCHECK_GRANTS to the grants required to be given to the `healthcheck@localhost`, `healthcheck@127.0.0.1`, `healthcheck@::1`, users. When not specified the default grant is `[USAGE](../../../../../ref/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#usage)`.


The main value used here will be `[REPLICA MONITOR](../../../../../ref/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#replica-monitor) for the [healthcheck --replication](using-healthcheck-sh.md) test.`


### MARIADB_INITDB_SKIP_TZINFO / MYSQL_INITDB_SKIP_TZINFO


By default, the entrypoint script automatically loads the timezone data needed for the CONVERT_TZ() function. If it is not needed, any non-empty value disables timezone loading.


### MARIADB_AUTO_UPGRADE / MARIADB_DISABLE_UPGRADE_BACKUP


Set MARIADB_AUTO_UPGRADE to a non-empty value to have the entrypoint check whether [mariadb-upgrade](../../../../../clients-and-utilities/mariadb-upgrade.md) needs to run, and if so, run the upgrade before starting the MariaDB server.


Before the upgrade, a backup of the system database is created in the top of the datadir with the name system_mysql_backup_*.sql.zst. This backup process can be disabled with by setting MARIADB_DISABLE_UPGRADE_BACKUP to a non-empty value.


If `MARIADB_AUTO_UPGRADE` is set, and the `.my-healthcheck.cnf` file is missing, the `healthcheck` users are recreated if they don't exist, `MARIADB_HEALTHCHECK_GRANTS
` grants are given, the passwords of the `healthcheck` users are reset to a random value and the `.my-healthcheck.cnf` file is recreated with the new password populated.


### MARIADB_MASTER_HOST


When specified, the container will connect to this host and replicate from it.


### MARIADB_REPLICATION_USER / MARIADB_REPLICATION_PASSWORD_HASH / MARIADB_REPLICATION_PASSWORD


When MARIADB_MASTER_HOST is specified, MARIADB_REPLICATION_USER and MARIADB_REPLICATION_PASSWORD will be used to connect to the master.


When not specified, the MARIADB_REPLICATION_USER will be created with the REPLICATION REPLICA grants required to a client to start replication.

