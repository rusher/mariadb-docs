
# Catalog Status Variables


##### MariaDB starting with [12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/what-is-mariadb-120)
Catalog support is planned for 12.0.



When using a MariaDB Server with [catalogs](README.md) support, all status information is collected for the whole server, per catalog and per session.


```
SHOW SERVER STATUS;
```

shows the status for the whole server. Note that only the super user in the 'def' catalog has privileges for the above statement.


```
SHOW GLOBAL STATUS;
SHOW CATALOG STATUS;
```

Both commands show the status for the current catalog.
The reason that `GLOBAL` shows catalog status is that because catalogs are 'multi-tenant', a
catalog user should not be able to see the status from other users (for most things).


```
SHOW [SESSION] STATUS;
```

Shows the status for the current connection.


The main "new thing" is that catalogs enable SAS providers to see the status for a single tenant (catalog user).
This makes it much easier to find 'bad neighbors' (tenants that cause problems for other tenants) so that they can be moved to other servers.


When the MariaDB server is not configured for catalogs, the following commands are equivalent:


```
SHOW GLOBAL STATUS
SHOW SERVER STATUS 
SHOW CATALOG STATUS
```

## See Also


* [SHOW STATUS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-status.md)


CC BY-SA / Gnu FDL

