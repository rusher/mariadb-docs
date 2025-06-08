# MariaDB Server Docker Official Image Environment Variables

When you start the image, you can adjust the initialization of the MariaDB Server instance by passing one or more environment variables on the docker run command line. Do note that all of the variables below, except `MARIADB_AUTO_UPGRADE`, will have no effect if you start the container with a data directory that already contains a database: any pre-existing database will always be left untouched on container startup.

From tag 10.2.38, 10.3.29, 10.4.19, 10.5.10 onwards, and all 10.6 and later tags, the MARIADB\_\* equivalent variables are provided. MARIADB\_\* variants will always be used in preference to MYSQL\_\* variants.

One of MARIADB\_ROOT\_PASSWORD\_HASH, MARIADB\_ROOT\_PASSWORD, MARIADB\_ALLOW\_EMPTY\_ROOT\_PASSWORD, or MARIADB\_RANDOM\_ROOT\_PASSWORD (or equivalents, including \*\_FILE), is required. The other environment variables are optional.

### MARIADB\_ROOT\_PASSWORD\_HASH / MARIADB\_ROOT\_PASSWORD / MYSQL\_ROOT\_PASSWORD

This specifies the password that will be set for the MariaDB root superuser account.

### MARIADB\_ALLOW\_EMPTY\_ROOT\_PASSWORD / MYSQL\_ALLOW\_EMPTY\_PASSWORD

Set to a non-empty value, like `1`, to allow the container to be started with a blank password for the root user. NOTE: Setting this variable to yes is not recommended unless you really know what you are doing, since this will leave your MariaDB instance completely unprotected, allowing anyone to gain complete superuser access.

### MARIADB\_RANDOM\_ROOT\_PASSWORD / MYSQL\_RANDOM\_ROOT\_PASSWORD

Set to a non-empty value, like yes, to generate a random initial password for the root user. The generated root password will be printed to stdout (GENERATED ROOT PASSWORD: .....).

### MARIADB\_ROOT\_HOST / MYSQL\_ROOT\_HOST

This is the hostname part of the root user created. By default this is %, however it can be set to any default MariaDB allowed hostname component. Setting this to localhost will prevent any root user being accessible except via the unix socket.

### MARIADB\_DATABASE / MYSQL\_DATABASE

This variable allows you to specify the name of a database to be created on image startup.

### MARIADB\_USER / MYSQL\_USER, MARIADB\_PASSWORD\_HASH / MARIADB\_PASSWORD / MYSQL\_PASSWORD

Both user and password variables, along with a database, are required for a user to be created. This user will be granted all access (corresponding to GRANT ALL) to the MARIADB\_DATABASE database.

Do not use this mechanism to create the root superuser, that user gets created by default with the password specified by the MARIADB\_ROOT\_PASSWORD / MYSQL\_ROOT\_PASSWORD variable.

### MARIADB\_MYSQL\_LOCALHOST\_USER / MARIADB\_MYSQL\_LOCALHOST\_GRANTS

Set MARIADB\_MYSQL\_LOCALHOST\_USER to a non-empty value to create the mysql@locahost database user. This user is especially useful for a variety of health checks and backup scripts.

The mysql@localhost user gets `[USAGE](../../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#usage)` privileges by default. If more access is required, additional global privileges in the form of a comma separated list can be provided. If you are sharing a volume containing MariaDB's unix socket (/var/run/mysqld by default), privileges beyond `[USAGE](../../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#usage)` can result in confidentiality, integrity and availability risks, so use a minimal set. Its also possible to use for [Mariadb-backup](../../../../../../server-usage/backing-up-and-restoring-databases/mariabackup/). The [healthcheck.sh](using-healthcheck-sh.md) script also documents the required privileges for each health check test.

### MARIADB\_HEALTHCHECK\_GRANTS

Set MARIADB\_HEALTHCHECK\_GRANTS to the grants required to be given to the `healthcheck@localhost`, `healthcheck@127.0.0.1`, `healthcheck@::1`, users. When not specified the default grant is `[USAGE](../../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#usage)`.

The main value used here will be `[REPLICA MONITOR](../../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#replica-monitor) for the [healthcheck --replication](using-healthcheck-sh.md) test.`

### MARIADB\_INITDB\_SKIP\_TZINFO / MYSQL\_INITDB\_SKIP\_TZINFO

By default, the entrypoint script automatically loads the timezone data needed for the CONVERT\_TZ() function. If it is not needed, any non-empty value disables timezone loading.

### MARIADB\_AUTO\_UPGRADE / MARIADB\_DISABLE\_UPGRADE\_BACKUP

Set MARIADB\_AUTO\_UPGRADE to a non-empty value to have the entrypoint check whether [mariadb-upgrade](../../../../../../clients-and-utilities/mariadb-upgrade.md) needs to run, and if so, run the upgrade before starting the MariaDB server.

Before the upgrade, a backup of the system database is created in the top of the datadir with the name system\_mysql\_backup\_\*.sql.zst. This backup process can be disabled with by setting MARIADB\_DISABLE\_UPGRADE\_BACKUP to a non-empty value.

If `MARIADB_AUTO_UPGRADE` is set, and the `.my-healthcheck.cnf` file is missing, the `healthcheck` users are recreated if they don't exist, `MARIADB_HEALTHCHECK_GRANTS` grants are given, the passwords of the `healthcheck` users are reset to a random value and the `.my-healthcheck.cnf` file is recreated with the new password populated.

### MARIADB\_MASTER\_HOST

When specified, the container will connect to this host and replicate from it.

### MARIADB\_REPLICATION\_USER / MARIADB\_REPLICATION\_PASSWORD\_HASH / MARIADB\_REPLICATION\_PASSWORD

When MARIADB\_MASTER\_HOST is specified, MARIADB\_REPLICATION\_USER and MARIADB\_REPLICATION\_PASSWORD will be used to connect to the master.

When not specified, the MARIADB\_REPLICATION\_USER will be created with the REPLICATION REPLICA grants required to a client to start replication.

CC BY-SA / Gnu FDL
