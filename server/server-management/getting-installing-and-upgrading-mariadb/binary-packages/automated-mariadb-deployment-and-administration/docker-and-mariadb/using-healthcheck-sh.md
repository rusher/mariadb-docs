
# Using Healthcheck.sh

The healthcheck.sh script is part of the Docker Official Images of MariaDB Server. The script is part of the [repository of the Docker Official Image of MariaDB Server](https://github.com/MariaDB/mariadb-docker/blob/master/healthcheck.sh).


The script processes a number of argument and tests, together, in strict order. Arguments pertaining to a test must occur before the test name. If a test fails, no further processing is performed. Both arguments and tests begin with a double-hyphen.


By default, (since 2023-06-27), official images will create healthcheck@localhost, healthcheck@127.0.0.1, healthcheck@::1 users with a random password and USAGE privileges. `<code>[MARIADB_HEALTHCHECK_GRANTS](mariadb-server-docker-official-image-environment-variables.md#mariadb_healthcheck_grants)</code>` can be used for `<code>--replication</code>` where additional grants are required. This is stored in .my-healthcheck.cnf in the datadir of the container and passed as the `<code>--defaults-extra-file</code>` to the healthcheck.sh script if it exists. The `<code>.my-healthcheck.cnf</code>` also sets `<code>protocol=tcp</code>` for the `<code>mariadb</code>` so `<code>--connect</code>` is effectively there on all tests.


The `<code>[MARIADB_AUTO_UPGRADE=1](mariadb-server-docker-official-image-environment-variables.md#mariadb_auto_upgrade) will regenerate the .my-healthcheck.cnf file if missing and recreate the healthcheck users of the database with a new random password. The current port configuration of the MariaDB container is written into this file.</code>`


The `<code>[MARIADB_MYSQL_LOCALHOST_USER=1, MARIADB_MYSQL_LOCALHOST_GRANTS](mariadb-server-docker-official-image-environment-variables.md#mariadb_mysql_localhost_user-mariadb_mysql_localhost_grants)</code>` environment variables can also be used, but with the creation of the healthcheck user, these are backwards compatible.


# Compose File Example


An example of a compose file that uses the healthcheck.sh to determine a healthy service as a depedency before starting a wordpress service:


```
version: "3"
services:
  mariadb:
    image: mariadb:lts
    environment:
      - MARIADB_DATABASE=testdb
      - MARIADB_USER=testuser
      - MARIADB_PASSWORD=password
      - MARIADB_RANDOM_ROOT_PASSWORD=1
    healthcheck:
      test: ["CMD", "healthcheck.sh", "--connect", "--innodb_initialized"]
      start_period: 10s
      interval: 10s
      timeout: 5s
      retries: 3
  wordpress:
    image: wordpress
    environment:
      - WORDPRESS_DB_HOST=mariadb
      - WORDPRESS_DB_NAME=testdb
      - WORDPRESS_DB_USER=testuser
      - WORDPRESS_DB_PASSWORD=password
    depends_on:
      mariadb:
        condition: service_healthy
```




# Tests


## --connect


This is active when a external user can connect to the TCP port of MariaDB Server. This strictly tests just the TCP connection and not if any authentication works.


## --innodb_initialized


This test is true when InnoDB has completed initializing. This includes any rollback or crash recovery that may be occurring in the background as MariaDB is starting.


The connecting user must have [USAGE](../../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#the-usage-privilege) privileges to perform this test.


## --innodb_buffer_pool_loaded


This indicates that the buffer pool dump previously saved has been completed loaded into the InnoDB Buffer Pool and as such the server has a hot cache ready for use. This checks the [innodb_buffer_pool_load_status](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_buffer_pool_load_status) for a "complete" indicator.


This test doesn't check if [innodb-system-variables/#innodb_buffer_pool_load_at_startupinnodb_buffer_pool_load_at_startup](../../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_load_at_startupinnodb_buffer_pool_load_at_startup) is set at startup.


The connecting user must have [USAGE](../../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#the-usage-privilege) privileges to perform this test.


## --galera_online


This indicates that the galera node is online by the [wsrep_local_state](https://galeracluster.com/library/documentation/node-states.html#node-state-changes) variable. This includes states like "joining" and "donor" where it cannot serve SQL queries.


The connecting user must have [USAGE](../../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#the-usage-privilege) privileges to perform this test.


## --replication


This tests a replica based on the `<code>--replication_*</code>` parameters. The replica test must pass all of the subtests to be true. The subtests are:


* io - the IO thread is running
* sql - the sql thread is running
* seconds_behind_master - the replica is less than X seconds behind the master.
* sql_remaining_delay - the delayed replica is less than X seconds behind the master's execution of the same SQL.


These are tested for all connections, if `<code>--replication_all</code>` is set (default), or `<code>--replication_name</code>`.


The connecting user must have [REPLICATION_CLIENT](../../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#replication-client) if using a version less than [MariaDB 10.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), or [REPLICA MONITOR](../../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#replica-monitor) for [MariaDB 10.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md) or later.


## --mariadbupgrade


This healthcheck indicates that the mariadb is upgrade to the current version.


# Parameters


## --replication_all


Checks all replication sources


## --replication_name=n


Sets the multisource connection name tested. Unsets `<code>--replication_all</code>`.


## --replication_io


IO thread is running


## --replication_sql


SQL thread is running


## --replication_seconds_behind_master=n


Less than or equal this seconds of delay


## --replication_sql_remaining_delay=n


Less than or equal this seconds of remaining delay


## --su=n


Change to this user. Can only be done once as the root user is default for healthchecks.


## --su-mysql


Change to the `<code>mysql</code>` unix user. Like `<code>--su</code>` this respawns the script so will reset all parameters. Should be the first argument. The `<code>[MARIADB_MYSQL_LOCALHOST_USER=1](mariadb-server-docker-official-image-environment-variables.md#mariadb_mysql_localhost_user-mariadb_mysql_localhost_grants)</code>` environment variable is designed around usage here.


## --datadir=n


For the `<code>--mariadbupgrade</code>` test where the upgrade file is located.


## --no-defaults --defaults-file --defaults-extra-file --defaults-group-suffix


These are passed to [mariadb shell](../../../../../clients-and-utilities/mariadb-client/README.md) for all tests except `<code>--mariadbupgrade</code>`


# Examples


```
healthcheck.sh --su-mysql --connect --innodb_initialized
```

Switch to `<code>mysql</code>` user, and check if can connect and the innodb is initialized.


```
healthcheck.sh --su-mysql --connect --replication_io --replication_sql --replication_seconds_behind_master=600  --replication_sql_remaining_delay=30 ----replication_name=archive --replication --replication_seconds_behind_master=10  --replication_name=channel1 --replication
```

Switch to `<code>mysql</code>` user, check if connections can be made, for the replication channel "archive", ensure io and sql threads are running and the seconds behind master < 600 seconds and the sql remaining delay < 30 seconds. For the "channel1", the seconds behind master is limit to 10 seconds maximum.

