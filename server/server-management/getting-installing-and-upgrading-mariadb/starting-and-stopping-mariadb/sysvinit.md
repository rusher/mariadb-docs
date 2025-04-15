
# sysVinit


[sysVinit](https://en.wikipedia.org/wiki/Init#SysV-style) is one of the most common service managers. On systems that use [sysVinit](https://en.wikipedia.org/wiki/Init#SysV-style), the `<code>[mysql.server](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-servers-table.md)</code>` script is normally installed to `<code>/etc/init.d/mysql</code>`.


## Interacting with the MariaDB Server Process


The service can be interacted with by using the `<code>[service](https://linux.die.net/man/8/service)</code>` command.


### Starting the MariaDB Server Process on Boot


On RHEL/CentOS and other similar distributions, the `<code>[chkconfig](https://linux.die.net/man/8/chkconfig)</code>` command can be used to enable the MariaDB Server process at boot:


```
chkconfig --add mysql
chkconfig --level 345 mysql on
```

On Debian and Ubuntu and other similar distributions, the `<code>[update-rc.d](https://manpages.debian.org/wheezy/sysv-rc/update-rc.d.8.en.html)</code>` command can be used:


```
update-rc.d mysql defaults
```

### Starting the MariaDB Server Process


```
service mysql start
```

### Stopping the MariaDB Server Process


```
service mysql stop
```

### Restarting the MariaDB Server Process


```
service mysql restart
```

### Checking the Status of the MariaDB Server Process


```
service mysql status
```

## Manually Installing mysql.server with SysVinit


If you install MariaDB from [source](../compiling-mariadb-from-source/compiling-mariadb-from-source-mariadb-source-configuration-options.md) or from a [binary tarball](../binary-packages/installing-mariadb-binary-tarballs.md) that does not install `<code>[mysql.server](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-servers-table.md)</code>`
automatically, and if you are on a system that uses [sysVinit](sysvinit.md), then you can manually install `<code>mysql.server</code>` with [sysVinit](sysvinit.md). See [mysql.server: Manually Installing with SysVinit](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-servers-table.md) for more information.


## SysVinit and Galera Cluster


### Bootstrapping a New Cluster


When using [Galera Cluster](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md) with sysVinit, the first node in a cluster has to be started with `<code>service mysql bootstrap</code>`. See [Getting Started with MariaDB Galera Cluster: Bootstrapping a New Cluster](../../../server-usage/replication-cluster-multi-master/galera-cluster/getting-started-with-mariadb-galera-cluster.md#bootstrapping-a-new-cluster) for more information.

