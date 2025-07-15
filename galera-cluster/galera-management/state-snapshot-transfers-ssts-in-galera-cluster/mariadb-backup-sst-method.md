# mariadb-backup SST Method

The `mariadb-backup` SST method uses the [mariadb-backup](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup) utility for performing SSTs. It is one of the methods that does not block the donor node. mariadb-backup was originally forked from Percona XtraBackup, and similarly, the mariadb-backup SST method was originally forked from the `xtrabackup-v2` SST method.Note that if you use the mariadb-backup SST method, then you also need to have `socat` installed on the server. This is needed to stream the backup from the donor node to the joiner node. This is a limitation that was inherited from the `xtrabackup-v2` SST method.

#### Choosing mariadb-backup for SSTs <a href="#choosing-mariabackup-for-ssts" id="choosing-mariabackup-for-ssts"></a>

To use the mariadb-backup SST method, you must set the [`wsrep_sst_method=mariabackup`](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/~/changes/171/reference/wsrep-variable-details/wsrep_sst_method) on both the donor and joiner node. It can be changed dynamically with [`SET GLOBAL`](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set) on the node that you intend to be an SST donor. For example:SET GLOBAL wsrep\_sst\_method='mariadbbackup';It can be set in a server [option group](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) prior to starting up a node:\[mariadb]...wsrep\_sst\_method = mariadbbackupFor an SST to work properly, the donor and joiner node must use the same SST method. Therefore, it is recommended to set [`wsrep_sst_method`](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/~/changes/171/reference/wsrep-variable-details/wsrep_sst_method) to the same value on all nodes, since any node will usually be a donor or joiner node at some point.

#### Major Version Upgrades <a href="#major-version-upgrades" id="major-version-upgrades"></a>

{% hint style="warning" %}
The InnoDB redo log format has been changed in [MariaDB 10.5](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/mariadb-10-5-series/what-is-mariadb-105) and [MariaDB 10.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108) in a way that will not allow the crash recovery or the preparation of a backup from an older major version. Because of this, the `mariabackup` SST method cannot be used for some major version upgrades, unless you temporarily edit the `wsrep_sst_mariadbbackup` script so that the `--prepare` step on the newer-major-version joiner will be executed using the older-major-version mariadb-backup tool.The default method `wsrep_sst_method=rsync` will work for major version upgrades; see [MDEV-27437](https://jira.mariadb.org/browse/MDEV-27437).
{% endhint %}

#### Authentication and Privileges <a href="#authentication-and-privileges" id="authentication-and-privileges"></a>

To use the mariadb-backup SST method, [mariadb-backup](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup) needs to be able to authenticate locally on the donor node, so that it can create a backup to stream to the joiner. You can tell the donor node what username and password to use by setting the [`wsrep_sst_auth`](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/~/changes/171/reference/wsrep-variable-details/wsrep_sst_method) system variable. It can be changed dynamically with [`SET GLOBAL`](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set) on the node that you intend to be an SST donor. For example:SET GLOBAL wsrep\_sst\_auth = 'mariadbbackup:mypassword';It can also be set in a server [option group](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) prior to starting up a node:\[mariadb]...wsrep\_sst\_auth = mariadbbackup:mypasswordSome [authentication plugins](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins) do not require a password. For example, the [`unix_socket`](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-unix-socket) and [`gssapi`](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/security/authentication-with-enterprise-server/authentication-with-gssapi) authentication plugins do not require a password. If you are using a user account that does not require a password in order to log in, then you can just leave the password component of [`wsrep_sst_auth`](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/~/changes/171/reference/wsrep-variable-details/wsrep_sst_method) empty. For example:\[mariadb]...wsrep\_sst\_auth = mariadbbackup:The user account that performs the backup for the SST needs to have the same privileges as mariadb-backup, which are the RELOAD, PROCESS, LOCK TABLES and BINLOG MONITOR, REPLICA MONITORglobal privileges. To be safe, you should ensure that these privileges are set on each node in your cluster. mariadb-backup connects locally on the donor node to perform the backup, so the following user should be sufficient:CREATE USER 'mariadbbackup'@'localhost' IDENTIFIED BY 'mypassword';GRANT RELOAD, PROCESS, LOCK TABLES,BINLOG MONITOR ON \*.\* TO 'mariadbbackup'@'localhost';Passwordless Authentication - Unix SocketIt is possible to use theunix\_socketauthentication plugin for the user account that performs SSTs. This would provide the benefit of not needing to configure a plain-text password inwsrep\_sst\_auth.The user account would have to have the same name as the operating system user account that is running the mysqld process. On many systems, this is the user account configured as the user option, and it tends to default to mysql.For example, if theunix\_socketauthentication plugin is already installed, then you could execute the following to create the user account:CREATE USER 'mysql'@'localhost' IDENTIFIED VIA unix\_socket;GRANT RELOAD, PROCESS, LOCK TABLES,REPLICATION CLIENT ON \*.\* TO 'mysql'@'localhost';And then to configurewsrep\_sst\_auth, you could set the following in a serveroption groupin anoption fileprior to starting up a node:\[mariadb]...wsrep\_sst\_auth = mysql:Passwordless Authentication - GSSAPIIt is possible to use thegssapiauthentication plugin for the user account that performs SSTs. This would provide the benefit of not needing to configure a plain-text password inwsrep\_sst\_auth.The following steps would need to be done beforehand:You need a KDC runningMIT KerberosorMicrosoft Active Directory.You will need tocreate a keytab filefor the MariaDB server.You will need toinstall the packagecontaining thegssapiauthentication plugin.You will need toinstall the pluginin MariaDB, so that thegssapiauthentication plugin is available to use.You will need toconfigure the plugin.You will need tocreate a user accountgssapiFor example, you could execute the following to create the user account in MariaDB:CREATE USER 'mariadbbackup'@'localhost' IDENTIFIED VIA gssapi;GRANT RELOAD, PROCESS, LOCK TABLES,BINLOG MONITOR ON \*.\* TO 'mariadbbackup'@'localhost';And then to configurewsrep\_sst\_auth, you could set the following in a serveroption groupin anoption fileprior to starting up a node:\[mariadb]...wsrep\_sst\_auth = mariadbbackup:Choosing a Donor NodeWhen mariadb-backup is used to create the backup for the SST on the donor node, mariadb-backup briefly requires a system-wide lock at the end of the backup. This is done withBACKUP STAGE BLOCK\_COMMIT.If a specific node in your cluster is acting as the primary node by receiving all of the application's write traffic, then this node should not usually be used as the donor node, because the system-wide lock could interfere with the application. In this case, you can define one or more preferred donor nodes by setting thewsrep\_sst\_donorsystem variable.For example, let's say that we have a 5-node cluster with the nodes node1, node2, node3, node4, and node5, and let's say that node1 is acting as the primary node. The preferred donor nodes for node2 could be configured by setting the following in a serveroption groupin anoption fileprior to starting up a node:\[mariadb]...wsrep\_sst\_donor=node3,node4,node5,The trailing comma tells the server to allow any other node as donor when the preferred donors are not available. Therefore, if node1 is the only node left in the cluster, the trailing comma allows it to be used as the donor node.Socat DependencyDuring the SST process, the donor node uses socat to stream the backup to the joiner node. Then the joiner node prepares the backup before restoring it. The socat utility must be installed on both the donor node and the joiner node in order for this to work. Otherwise, the MariaDB error log will contain an error like:WSREP\_SST: \[ERROR] socat not found in path: /usr/sbin:/sbin:/usr//bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin (20180122 14:55:32.993)Installing Socat on RHEL/CentOSOn RHEL/CentOS, socat can be installed from theExtra Packages for Enterprise Linux (EPEL)repository.TLSThis SST method supports two different TLS methods. The specific method can be selected by setting the encrypt option in the \[sst] section of the MariaDB configuration file. The options are:TLS using OpenSSL encryption built into socat (encrypt=2)TLS using OpenSSL encryption with Galera-compatible certificates and keys (encrypt=3)Note that encrypt=1 refers to a TLS encryption method that has been deprecated and removed. encrypt=4 refers to a TLS encryption method in xtrabackup-v2 that has not yet been ported to mariadb-backup. SeeMDEV-18050about that.TLS Using OpenSSL Encryption Built into SocatTo generate keys compatible with this encryption method, you can followthese directions.For example:First, generate the keys and certificates:FILENAME=sstopenssl genrsa -out $FILENAME.key 1024openssl req -new -key $FILENAME.key -x509 -days 3653 -out $FILENAME.crtcat $FILENAME.key $FILENAME.crt >$FILENAME.pemchmod 600 $FILENAME.key $FILENAME.pemOn some systems, you may also have to add dhparams to the certificate:openssl dhparam -out dhparams.pem 2048cat dhparams.pem >> sst.pemThen, copy the certificate and keys to all nodes in the cluster.Then, configure the following on all nodes in the cluster:\[sst]encrypt=2tca=/etc/my.cnf.d/certificates/sst.crttcert=/etc/my.cnf.d/certificates/sst.pemBut replace the paths with whatever is relevant on your system. This should allow your SSTs to be encrypted.TLS Using OpenSSL Encryption with Galera-compatible Certificates and KeysTo generate keys compatible with this encryption method, you can followthese directions.For example:First, generate the keys and certificates:# CAopenssl genrsa 2048 > ca-key.pemopenssl req -new -x509 -nodes -days 365000 \\-key ca-key.pem -out ca-cert.pem# server1openssl req -newkey rsa:2048 -days 365000 \\-nodes -keyout server1-key.pem -out server1-req.pemopenssl rsa -in server1-key.pem -out server1-key.pemopenssl x509 -req -in server1-req.pem -days 365000 \\-CA ca-cert.pem -CAkey ca-key.pem -set\_serial 01 \\-out server1-cert.pemThen, copy the certificate and keys to all nodes in the cluster.Then, configure the following on all nodes in the cluster:\[sst]encrypt=3tkey=/etc/my.cnf.d/certificates/server1-key.pemtcert=/etc/my.cnf.d/certificates/server1-cert.pemBut replace the paths with whatever is relevant on your system.This should allow your SSTs to be encrypted.LogsThe mariadb-backup SST method has its own logging outside of the MariaDB Server logging.Logging to SST LogsLogging for mariadb-backup SSTs works the following way.By default, on the donor node, it logs to mariadb-backup.backup.log. This log file is located in thedatadir.By default, on the joiner node, it logs to mariadb-backup.prepare.log and mariadb-backup.move.log These log files are also located in the datadir.By default, before a new SST is started, existing mariadb-backup SST log files are compressed and moved to /tmp/sst\_log\_archive. This behavior can be disabled by setting sst-log-archive=0 in the \[sst]option groupin anoption file. Similarly, the archive directory can be changed by setting sst-log-archive-dir. For example:\[sst]sst-log-archive=1sst-log-archive-dir=/var/log/mysql/sst/SeeMDEV-17973for more information. <\</product>>Logging to SyslogYou can redirect the SST logs to the syslog instead by setting the following in the \[sst]option groupin anoption file:\[sst]sst-syslog=1You can also redirect the SST logs to the syslog by setting the following in the \[mysqld\_safe]option groupin anoption file:\[mysqld\_safe]syslogPerforming SSTs with IPv6 AddressesIf you are performingmariadb-backupSSTs with IPv6 addresses, then the socat utility needs to be passed the pf=ip6 option. This can be done by setting the sockopt option in the \[sst]option groupin anoption file. For example:\[sst]sockopt=",pf=ip6"SeeMDEV-18797for more information.Manual SST with mariadb-backupIn some cases, if Galera Cluster's automatic SSTs repeatedly fail, then it can be helpful to perform a "manual SST". See the following page on how to do that:Manual SST of Galera Cluster node withmariadb-backupSee Also\


The `mariadbbackup` SST method uses the [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup) utility for performing SSTs. It is one of the methods that does not block the donor node. mariadb-backup was originally forked from [Percona XtraBackup](https://kb-archive.mariadb.net/kb/en/backup-restore-and-import-clients-percona-xtrabackup/), and similarly, the mariadb-backup SST method was originally forked from the `xtrabackup-v2` SST method.

Note that if you use the mariadb-backup SST method, then you also need to have `socat` installed on the server. This is needed to stream the backup from the donor node to the joiner node. This is a limitation that was inherited from the `xtrabackup-v2` SST method.

### Choosing mariadb-backup for SSTs <a href="#choosing-mariabackup-for-ssts" id="choosing-mariabackup-for-ssts"></a>

To use the mariadb-backup SST method, you must set the [`wsrep_sst_method=mariabackup`](../../reference/wsrep-variable-details/wsrep_sst_method.md) on both the donor and joiner node. It can be changed dynamically with [`SET GLOBAL`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set) on the node that you intend to be an SST donor. For example:

```sql
SET GLOBAL wsrep_sst_method='mariadbbackup';
```

It can be set in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) prior to starting up a node:

```sql
[mariadb]
...
wsrep_sst_method = mariadbbackup
```

For an SST to work properly, the donor and joiner node must use the same SST method. Therefore, it is recommended to set [`wsrep_sst_method`](../../reference/wsrep-variable-details/wsrep_sst_method.md) to the same value on all nodes, since any node will usually be a donor or joiner node at some point.

### Major Version Upgrades <a href="#major-version-upgrades" id="major-version-upgrades"></a>

The InnoDB redo log format has been changed in [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/mariadb-10-5-series/what-is-mariadb-105) and [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108) in a way that will not allow the crash recovery or the preparation of a backup from an older major version. Because of this, the `mariabackup` SST method cannot be used for some major version upgrades, unless you temporarily edit the `wsrep_sst_mariadbbackup` script so that the `--prepare` step on the newer-major-version joiner will be executed using the older-major-version mariadb-backup tool.

The default method `wsrep_sst_method=rsync` will work for major version upgrades; see [MDEV-27437](https://jira.mariadb.org/browse/MDEV-27437).

### Authentication and Privileges <a href="#authentication-and-privileges" id="authentication-and-privileges"></a>

To use the mariadb-backup SST method, [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup) needs to be able to authenticate locally on the donor node, so that it can create a backup to stream to the joiner. You can tell the donor node what username and password to use by setting the [`wsrep_sst_auth`](../../reference/wsrep-variable-details/wsrep_sst_method.md) system variable. It can be changed dynamically with [`SET GLOBAL`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set) on the node that you intend to be an SST donor. For example:

```sql
SET GLOBAL wsrep_sst_auth = 'mariadbbackup:mypassword';
```

It can also be set in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) prior to starting up a node:

```sql
[mariadb]
...
wsrep_sst_auth = mariadbbackup:mypassword
```

Some [authentication plugins](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins) do not require a password. For example, the [`unix_socket`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-unix-socket) and [`gssapi`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/authentication-with-enterprise-server/authentication-with-gssapi) authentication plugins do not require a password. If you are using a user account that does not require a password in order to log in, then you can just leave the password component of [`wsrep_sst_auth`](../../reference/wsrep-variable-details/wsrep_sst_method.md) empty. For example:

```
[mariadb]
...
wsrep_sst_auth = mariadbbackup:
```

The user account that performs the backup for the SST needs to have the same privileges as mariadb-backup, which are the `RELOAD`, `PROCESS`, `LOCK TABLES` and `BINLOG MONITOR`, `REPLICA MONITOR` [global privileges](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-privileges). To be safe, you should ensure that these privileges are set on each node in your cluster. mariadb-backup connects locally on the donor node to perform the backup, so the following user should be sufficient:

```sql
CREATE USER 'mariadbbackup'@'localhost' IDENTIFIED BY 'mypassword';
GRANT RELOAD, PROCESS, LOCK TABLES, 
BINLOG MONITOR ON *.* TO 'mariadbbackup'@'localhost';
```

#### Passwordless Authentication - Unix Socket <a href="#passwordless-authentication-unix-socket" id="passwordless-authentication-unix-socket"></a>

It is possible to use the [`unix_socket`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-unix-socket) authentication plugin for the user account that performs SSTs. This would provide the benefit of not needing to configure a plain-text password in [`wsrep_sst_auth`](../../reference/wsrep-variable-details/wsrep_sst_method.md).

The user account would have to have the same name as the operating system user account that is running the `mysqld` process. On many systems, this is the user account configured as the `user` option, and it tends to default to `mysql`.

For example, if the [`unix_socket`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-unix-socket) authentication plugin is already installed, then you could execute the following to create the user account:

```sql
CREATE USER 'mysql'@'localhost' IDENTIFIED VIA unix_socket;
GRANT RELOAD, PROCESS, LOCK TABLES, 
REPLICATION CLIENT ON *.* TO 'mysql'@'localhost';
```

And then to configure [`wsrep_sst_auth`](../../reference/wsrep-variable-details/wsrep_sst_method.md), you could set the following in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) prior to starting up a node:

```
[mariadb]
...
wsrep_sst_auth = mysql:
```

#### Passwordless Authentication - GSSAPI <a href="#passwordless-authentication-gssapi" id="passwordless-authentication-gssapi"></a>

It is possible to use the [`gssapi`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/authentication-with-enterprise-server/authentication-with-gssapi) authentication plugin for the user account that performs SSTs. This would provide the benefit of not needing to configure a plain-text password in [`wsrep_sst_auth`](../../reference/wsrep-variable-details/wsrep_sst_method.md).

The following steps would need to be done beforehand:

* You need a KDC running [MIT Kerberos](https://web.mit.edu/Kerberos/krb5-1.12/doc/index.html) or [Microsoft Active Directory](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview).
* You will need to [create a keytab file](https://web.mit.edu/Kerberos/krb5-1.12/doc/admin/install_appl_srv.html#the-keytab-file) for the MariaDB server.
* You will need to [install the package](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi#installing-the-plugins-package) containing the [`gssapi`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi) authentication plugin.
* You will need to [install the plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi#installing-the-plugin) in MariaDB, so that the [`gssapi`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi) authentication plugin is available to use.
* You will need to [configure the plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi#configuring-the-plugin).
* You will need to [create a user account](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/authentication-with-enterprise-server/authentication-with-gssapi#create-user) [`gssapi`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi)

For example, you could execute the following to create the user account in MariaDB:

```sql
CREATE USER 'mariadbbackup'@'localhost' IDENTIFIED VIA gssapi;
GRANT RELOAD, PROCESS, LOCK TABLES, 
BINLOG MONITOR ON *.* TO 'mariadbbackup'@'localhost';
```

And then to configure [`wsrep_sst_auth`](../../reference/wsrep-variable-details/wsrep_sst_method.md), you could set the following in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) prior to starting up a node:

```
[mariadb]
...
wsrep_sst_auth = mariadbbackup:
```

### Choosing a Donor Node <a href="#choosing-a-donor-node" id="choosing-a-donor-node"></a>

When mariadb-backup is used to create the backup for the SST on the donor node, mariadb-backup briefly requires a system-wide lock at the end of the backup. This is done with [`BACKUP STAGE BLOCK_COMMIT`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/backup-commands/backup-stage).

If a specific node in your cluster is acting as the _primary_ node by receiving all of the application's write traffic, then this node should not usually be used as the donor node, because the system-wide lock could interfere with the application. In this case, you can define one or more preferred donor nodes by setting the [`wsrep_sst_donor`](../../reference/galera-cluster-system-variables.md#wsrep_sst_donor) system variable.

For example, let's say that we have a 5-node cluster with the nodes `node1`, `node2`, `node3`, `node4`, and `node5`, and let's say that `node1` is acting as the _primary_ node. The preferred donor nodes for `node2` could be configured by setting the following in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) prior to starting up a node:

```
[mariadb]
...
wsrep_sst_donor=node3,node4,node5,
```

The trailing comma tells the server to allow any other node as donor when the preferred donors are not available. Therefore, if `node1` is the only node left in the cluster, the trailing comma allows it to be used as the donor node.

### Socat Dependency <a href="#socat-dependency" id="socat-dependency"></a>

During the SST process, the donor node uses `socat` to stream the backup to the joiner node. Then the joiner node prepares the backup before restoring it. The `socat` utility must be installed on both the donor node and the joiner node in order for this to work. Otherwise, the MariaDB error log will contain an error like:

```sql
WSREP_SST: [ERROR] socat not found in path: /usr/sbin:/sbin:/usr//bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin (20180122 14:55:32.993)
```

#### Installing Socat on RHEL/CentOS <a href="#installing-socat-on-rhelcentos" id="installing-socat-on-rhelcentos"></a>

On RHEL/CentOS, `socat` can be installed from the [Extra Packages for Enterprise Linux (EPEL)](https://docs.fedoraproject.org/en-US/epel/) repository.

### TLS <a href="#tls" id="tls"></a>

This SST method supports two different TLS methods. The specific method can be selected by setting the `encrypt` option in the `[sst]` section of the MariaDB configuration file. The options are:

* TLS using OpenSSL encryption built into `socat` (`encrypt=2`)
* TLS using OpenSSL encryption with Galera-compatible certificates and keys (`encrypt=3`)

Note that `encrypt=1` refers to a TLS encryption method that has been deprecated and removed. `encrypt=4` refers to a TLS encryption method in `xtrabackup-v2` that has not yet been ported to `mariadb-backup`. See [MDEV-18050](https://jira.mariadb.org/browse/MDEV-18050) about that.

#### TLS Using OpenSSL Encryption Built into Socat <a href="#tls-using-openssl-encryption-built-into-socat" id="tls-using-openssl-encryption-built-into-socat"></a>

To generate keys compatible with this encryption method, you can follow [these directions](http://www.dest-unreach.org/socat/doc/socat-openssltunnel.html).

For example:

* First, generate the keys and certificates:

```sql
FILENAME=sst
openssl genrsa -out $FILENAME.key 1024
openssl req -new -key $FILENAME.key -x509 -days 3653 -out $FILENAME.crt
cat $FILENAME.key $FILENAME.crt >$FILENAME.pem
chmod 600 $FILENAME.key $FILENAME.pem
```

* On some systems, you may also have to add dhparams to the certificate:

```sql
openssl dhparam -out dhparams.pem 2048
cat dhparams.pem >> sst.pem
```

* Then, copy the certificate and keys to all nodes in the cluster.
* Then, configure the following on all nodes in the cluster:

```sql
[sst]
encrypt=2
tca=/etc/my.cnf.d/certificates/sst.crt
tcert=/etc/my.cnf.d/certificates/sst.pem
```

But replace the paths with whatever is relevant on your system. This should allow your SSTs to be encrypted.

#### TLS Using OpenSSL Encryption with Galera-compatible Certificates and Keys <a href="#tls-using-openssl-encryption-with-galera-compatible-certificates-and-keys" id="tls-using-openssl-encryption-with-galera-compatible-certificates-and-keys"></a>

To generate keys compatible with this encryption method, you can follow [these directions](https://galeracluster.com/library/documentation/ssl-cert.html).

For example:

* First, generate the keys and certificates:

```sql
# CA
openssl genrsa 2048 > ca-key.pem
openssl req -new -x509 -nodes -days 365000 \
-key ca-key.pem -out ca-cert.pem
 
# server1
openssl req -newkey rsa:2048 -days 365000 \
-nodes -keyout server1-key.pem -out server1-req.pem
openssl rsa -in server1-key.pem -out server1-key.pem
openssl x509 -req -in server1-req.pem -days 365000 \
-CA ca-cert.pem -CAkey ca-key.pem -set_serial 01 \
-out server1-cert.pem
```

* Then, copy the certificate and keys to all nodes in the cluster.
* Then, configure the following on all nodes in the cluster:

```sql
[sst]
encrypt=3
tkey=/etc/my.cnf.d/certificates/server1-key.pem
tcert=/etc/my.cnf.d/certificates/server1-cert.pem
```

But replace the paths with whatever is relevant on your system.

This should allow your SSTs to be encrypted.

### Logs <a href="#logs" id="logs"></a>

The `mariadb-backup` SST method has its own logging outside of the MariaDB Server logging.

#### Logging to SST Logs <a href="#logging-to-sst-logs" id="logging-to-sst-logs"></a>

Logging for mariadb-backup SSTs works the following way.

By default, on the donor node, it logs to `mariadb-backup.backup.log`. This log file is located in the [`datadir`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#datadir).

By default, on the joiner node, it logs to `mariadb-backup.prepare.log` and `mariadb-backup.move.log` These log files are also located in the `datadir`.

By default, before a new SST is started, existing `mariadb-backup` SST log files are compressed and moved to `/tmp/sst_log_archive`. This behavior can be disabled by setting `sst-log-archive=0` in the `[sst]` [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files). Similarly, the archive directory can be changed by setting `sst-log-archive-dir`. For example:

```sql
[sst]
sst-log-archive=1
sst-log-archive-dir=/var/log/mysql/sst/
```

See [MDEV-17973](https://jira.mariadb.org/browse/MDEV-17973) for more information. <\</product>>

#### Logging to Syslog <a href="#logging-to-syslog" id="logging-to-syslog"></a>

You can redirect the SST logs to the syslog instead by setting the following in the `[sst]` [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files):

```sql
[sst]
sst-syslog=1
```

You can also redirect the SST logs to the syslog by setting the following in the `[mysqld_safe]` [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files):

```
[mysqld_safe]
syslog
```

### Performing SSTs with IPv6 Addresses <a href="#performing-ssts-with-ipv6-addresses" id="performing-ssts-with-ipv6-addresses"></a>

If you are performing [mariadb-backup ](mariadb-backup-sst-method.md)SSTs with IPv6 addresses, then the `socat` utility needs to be passed the `pf=ip6` option. This can be done by setting the `sockopt` option in the `[sst]` [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files). For example:

```
[sst]
sockopt=",pf=ip6"
```

See [MDEV-18797](https://jira.mariadb.org/browse/MDEV-18797) for more information.

### Manual SST with mariadb-backup <a href="#manual-sst-with-mariabackup" id="manual-sst-with-mariabackup"></a>

In some cases, if Galera Cluster's automatic SSTs repeatedly fail, then it can be helpful to perform a "manual SST". See the following page on how to do that:

* [Manual SST of Galera Cluster node with ](manual-sst-of-galera-cluster-node-with-mariadb-backup.md)[mariadb-backup ](mariadb-backup-sst-method.md)

### See Also <a href="#see-also" id="see-also"></a>

* [Percona XtraBackup SST Configuration](https://www.percona.com/doc/percona-xtradb-cluster/5.7/manual/xtrabackup_sst.html)
* [Encrypting PXC Traffic: ENCRYPTING SST TRAFFIC](https://docs.percona.com/percona-xtradb-cluster/5.7/security/encrypt-traffic.html#encrypt-sst)
* [XTRABACKUP PARAMETERS](https://galeracluster.com/library/documentation/xtrabackup-options.html)
* [SSL FOR STATE SNAPSHOT TRANSFERS: ENABLING SSL FOR XTRABACKUP](https://galeracluster.com/library/documentation/ssl-sst.html#ssl-xtrabackup)
