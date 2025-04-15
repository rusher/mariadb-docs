
# mariabackup SST Method

The `<code>mariabackup</code>` SST method uses the [Mariabackup](../../../../server-management/backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md) utility for performing SSTs. It is one of the methods that does not block the donor node. [Mariabackup](../../../../server-management/backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md) was originally forked from [Percona XtraBackup](../../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/README.md), and similarly, the `<code>mariabackup</code>` SST method was originally forked from the `<code>[xtrabackup-v2](https://mariadb.com/kb/en/)</code>` SST method.


Note that if you use the `<code>mariabackup</code>` SST method, then you also need to have `<code>[socat](#socat-dependency)</code>` installed on the server. This is needed to stream the backup from the donor node to the joiner node. This is a limitation that was inherited from the `<code>[xtrabackup-v2](https://mariadb.com/kb/en/)</code>` SST method.



## Choosing Mariabackup for SSTs


To use the `<code>mariabackup</code>` SST method, you must set the `<code>[wsrep_sst_method=mariabackup](../galera-cluster-system-variables.md#wsrep_sst_method)</code>` on both the donor and joiner node. It can be changed dynamically with `<code>[SET GLOBAL](../../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md#global-session)</code>` on the node that you intend to be a SST donor. For example:


```
SET GLOBAL wsrep_sst_method='mariabackup';
```

It can be set in a server [option group](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up a node:


```
[mariadb]
...
wsrep_sst_method = mariabackup
```

For an SST to work properly, the donor and joiner node must use the same SST method. Therefore, it is recommended to set `<code>[wsrep_sst_method](../galera-cluster-system-variables.md#wsrep_sst_method)</code>` to the same value on all nodes, since any node will usually be a donor or joiner node at some point.


## Major version upgrades


The InnoDB redo log format has been changed in [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md) and [MariaDB 10.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md) in a way that will not allow the crash recovery or the preparation of a backup from an older major version. Because of this, the `<code>mariabackup</code>` SST method cannot be used for some major version upgrades, unless you temporarily edit the `<code>wsrep_sst_mariabackup</code>` script so that the `<code>--prepare</code>` step on the newer-major-version joiner will be executed using the older-major-version `<code>mariabackup</code>` tool.


The default method `<code>wsrep_sst_method=rsync</code>` will work for major version upgrades; see [MDEV-27437](https://jira.mariadb.org/browse/MDEV-27437).


## Authentication and Privileges


To use the `<code>mariabackup</code>` SST method, [Mariabackup](../../../../server-management/backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md) needs to be able to authenticate locally on the donor node, so that it can create a backup to stream to the joiner. You can tell the donor node what username and password to use by setting the `<code>[wsrep_sst_auth](../galera-cluster-system-variables.md#wsrep_sst_auth)</code>` system variable. It can be changed dynamically with `<code>[SET GLOBAL](../../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md#global-session)</code>` on the node that you intend to be a SST donor. For example:


```
SET GLOBAL wsrep_sst_auth = 'mariabackup:mypassword';
```

It can also be set in a server [option group](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up a node:


```
[mariadb]
...
wsrep_sst_auth = mariabackup:mypassword
```

Some [authentication plugins](../../../../reference/plugins/authentication-plugins/README.md) do not require a password. For example, the `<code>[unix_socket](../../../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md)</code>` and `<code>[gssapi](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md)</code>` authentication plugins do not require a password. If you are using a user account that does not require a password in order to log in, then you can just leave the password component of `<code>[wsrep_sst_auth](../galera-cluster-system-variables.md#wsrep_sst_auth)</code>` empty. For example:


```
[mariadb]
...
wsrep_sst_auth = mariabackup:
```

The user account that performs the backup for the SST needs to have [the same privileges as Mariabackup](../../../../server-management/backing-up-and-restoring-databases/mariabackup/mariabackup-overview.md#authentication-and-privileges), which are the `<code>RELOAD</code>` , `<code>PROCESS</code>`, `<code>LOCK TABLES</code>` and `<code>BINLOG MONITOR</code>`, `<code>REPLICA MONITOR</code>` [global privileges](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#global-privileges). To be safe, you should ensure that these privileges are set on each node in your cluster. [Mariabackup](../../../../server-management/backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md) connects locally on the donor node to perform the backup, so the following user should be sufficient:


```
CREATE USER 'mariabackup'@'localhost' IDENTIFIED BY 'mypassword';
GRANT RELOAD, PROCESS, LOCK TABLES, BINLOG MONITOR ON *.* TO 'mariabackup'@'localhost';
```

### Passwordless Authentication - Unix Socket


It is possible to use the `<code>[unix_socket](../../../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md)</code>` authentication plugin for the user account that performs SSTs. This would provide the benefit of not needing to configure a plain-text password in `<code>[wsrep_sst_auth](../galera-cluster-system-variables.md#wsrep_sst_auth)</code>`.


The user account would have to have the same name as the operating system user account that is running the `<code>mysqld</code>` process. On many systems, this is the user account configured as the `<code>[user](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` option, and it tends to default to `<code>mysql</code>`.


For example, if the `<code>[unix_socket](../../../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md)</code>` authentication plugin is already installed, then you could execute the following to create the user account:


```
CREATE USER 'mysql'@'localhost' IDENTIFIED VIA unix_socket;
GRANT RELOAD, PROCESS, LOCK TABLES, REPLICATION CLIENT ON *.* TO 'mysql'@'localhost';
```

And then to configure `<code>[wsrep_sst_auth](../galera-cluster-system-variables.md#wsrep_sst_auth)</code>`, you could set the following in a server [option group](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up a node:


```
[mariadb]
...
wsrep_sst_auth = mysql:
```

### Passwordless Authentication - GSSAPI


It is possible to use the `<code>[gssapi](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md)</code>` authentication plugin for the user account that performs SSTs. This would provide the benefit of not needing to configure a plain-text password in `<code>[wsrep_sst_auth](../galera-cluster-system-variables.md#wsrep_sst_auth)</code>`.


The following steps would need to be done beforehand:


* You need a KDC running [MIT Kerberos](https://web.mit.edu/Kerberos/krb5-1.12/doc/index.html) or [Microsoft Active Directory](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview).
* You will need to [create a keytab file](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md#creating-a-keytab-file-on-a-unix-server) for the MariaDB server.
* You will need to [install the package](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md#installing-the-plugins-package) containing the `<code>[gssapi](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md)</code>` authentication plugin.
* You will need to [install the plugin](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md#installing-the-plugin) in MariaDB, so that the `<code>[gssapi](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md)</code>` authentication plugin is available to use.
* You will need to [configure the plugin](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md#configuring-the-plugin).
* You will need to [create a user account](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md#creating-users) that authenticates with the `<code>[gssapi](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md)</code>` authentication plugin, so that the user account can be used for SSTs. This user account will need to correspond with a user account that exists on the backend KDC.


For example, you could execute the following to create the user account in MariaDB:


```
CREATE USER 'mariabackup'@'localhost' IDENTIFIED VIA gssapi;
GRANT RELOAD, PROCESS, LOCK TABLES, BINLOG MONITOR ON *.* TO 'mariabackup'@'localhost';
```

And then to configure `<code>[wsrep_sst_auth](../galera-cluster-system-variables.md#wsrep_sst_auth)</code>`, you could set the following in a server [option group](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up a node:


```
[mariadb]
...
wsrep_sst_auth = mariabackup:
```

## Choosing a Donor Node


When Mariabackup is used to create the backup for the SST on the donor node, Mariabackup briefly requires a system-wide lock at the end of the backup. This is done with `<code>[BACKUP STAGE BLOCK_COMMIT](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/backup-commands/backup-stage.md)</code>`.


If a specific node in your cluster is acting as the *primary* node by receiving all of the application's write traffic, then this node should not usually be used as the donor node, because the system-wide lock could interfere with the application. In this case, you can define one or more preferred donor nodes by setting the `<code>[wsrep_sst_donor](../galera-cluster-system-variables.md#wsrep_sst_donor)</code>` system variable.


For example, let's say that we have a 5-node cluster with the nodes `<code>node1</code>`, `<code>node2</code>`, `<code>node3</code>`, `<code>node4</code>`, and `<code>node5</code>`, and let's say that `<code>node1</code>` is acting as the *primary* node. The preferred donor nodes for `<code>node2</code>` could be configured by setting the following in a server [option group](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up a node:


```
[mariadb]
...
wsrep_sst_donor=node3,node4,node5,
```

The trailing comma tells the server to allow any other node as donor when the preferred donors are not available. Therefore, if `<code>node1</code>` is the only node left in the cluster, the trailing comma allows it to be used as the donor node.


## Socat Dependency


During the SST process, the donor node uses [socat](https://www.dest-unreach.org/socat/doc/socat.html) to stream the backup to the joiner node. Then the joiner node prepares the backup before restoring it. The socat utility must be installed on both the donor node and the joiner node in order for this to work. Otherwise, the MariaDB error log will contain an error like:


```
WSREP_SST: [ERROR] socat not found in path: /usr/sbin:/sbin:/usr//bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin (20180122 14:55:32.993)
```

### Installing Socat on RHEL/CentOS


On RHEL/CentOS, `<code>socat</code>` can be installed from the [Extra Packages for Enterprise Linux (EPEL)](https://fedoraproject.org/wiki/EPEL) repository.


## TLS


This SST method supports two different TLS methods. The specific method can be selected by setting the `<code>encrypt</code>` option in the `<code>[sst]</code>` section of the MariaDB configuration file. The options are:


* TLS using OpenSSL encryption built into `<code>socat</code>` (`<code>encrypt=2</code>`)
* TLS using OpenSSL encryption with Galera-compatible certificates and keys (`<code>encrypt=3</code>`)


Note that `<code>encrypt=1</code>` refers to a TLS encryption method that has been deprecated and removed. `<code>encrypt=4</code>` refers to a TLS encryption method in `<code>xtrabackup-v2</code>` that has not yet been ported to `<code>mariabackup</code>`. See [MDEV-18050](https://jira.mariadb.org/browse/MDEV-18050) about that.


### TLS Using OpenSSL Encryption Built into Socat


To generate keys compatible with this encryption method, you can follow [these directions](https://www.dest-unreach.org/socat/doc/socat-openssltunnel.html).


For example:


* First, generate the keys and certificates:


```
FILENAME=sst
openssl genrsa -out $FILENAME.key 1024
openssl req -new -key $FILENAME.key -x509 -days 3653 -out $FILENAME.crt
cat $FILENAME.key $FILENAME.crt >$FILENAME.pem
chmod 600 $FILENAME.key $FILENAME.pem
```

* On some systems, you may also have to add dhparams to the certificate:


```
openssl dhparam -out dhparams.pem 2048
cat dhparams.pem >> sst.pem
```

* Then, copy the certificate and keys to all nodes in the cluster.


* Then, configure the following on all nodes in the cluster:


```
[sst]
encrypt=2
tca=/etc/my.cnf.d/certificates/sst.crt
tcert=/etc/my.cnf.d/certificates/sst.pem
```

But replace the paths with whatever is relevant on your system.


This should allow your SSTs to be encrypted.


### TLS Using OpenSSL Encryption with Galera-compatible Certificates and Keys


To generate keys compatible with this encryption method, you can follow [these directions](https://galeracluster.com/library/documentation/ssl-cert.html).


For example:


* First, generate the keys and certificates:


```
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


```
[sst]
encrypt=3
tkey=/etc/my.cnf.d/certificates/server1-key.pem
tcert=/etc/my.cnf.d/certificates/server1-cert.pem
```

But replace the paths with whatever is relevant on your system.


This should allow your SSTs to be encrypted.


## Logs


The `<code>mariabackup</code>` SST method has its own logging outside of the MariaDB Server logging.


### Logging to SST Logs


Logging for `<code>mariabackup</code>` SSTs works the following way.


By default, on the donor node, it logs to `<code>mariabackup.backup.log</code>`. This log file is located in the `<code>[datadir](../../optimization-and-tuning/system-variables/server-system-variables.md#datadir)</code>`.


By default, on the joiner node, it logs to `<code>mariabackup.prepare.log</code>` and `<code>mariabackup.move.log</code>` These log files are also located in the `<code>[datadir](../../optimization-and-tuning/system-variables/server-system-variables.md#datadir)</code>`.


By default, before a new SST is started, existing `<code>mariabackup</code>` SST log files are compressed and moved to `<code>/tmp/sst_log_archive</code>`. This behavior can be disabled by setting `<code>sst-log-archive=0</code>` in the `<code>[sst]</code>` [option group](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). Similarly, the archive directory can be changed by setting `<code>sst-log-archive-dir</code>`. For example:


```
[sst]
sst-log-archive=1
sst-log-archive-dir=/var/log/mysql/sst/
```

See [MDEV-17973](https://jira.mariadb.org/browse/MDEV-17973) for more information.
<</product>>


### Logging to Syslog


You can redirect the SST logs to the syslog instead by setting the following in the `<code>[sst]</code>` [option group](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md):


```
[sst]
sst-syslog=1
```

You can also redirect the SST logs to the syslog by setting the following in the `<code>[mysqld_safe]</code>` [option group](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md):


```
[mysqld_safe]
syslog
```

## Performing SSTs with IPv6 Addresses


If you are performing Mariabackup SSTs with IPv6 addresses, then the `<code>socat</code>` utility needs to be passed the `<code>pf=ip6</code>` option. This can be done by setting the `<code>sockopt</code>` option in the `<code>[sst]</code>` [option group](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[sst]
sockopt=",pf=ip6"
```

See [MDEV-18797](https://jira.mariadb.org/browse/MDEV-18797) for more information.


## Manual SST with Mariabackup


In some cases, if Galera Cluster's automatic SSTs repeatedly fail, then it can be helpful to perform a "manual SST". See the following page on how to do that:


* [Manual SST of Galera Cluster node with Mariabackup](manual-sst-of-galera-cluster-node-with-mariabackup.md)


## See Also


* [Percona XtraBackup SST Configuration](https://www.percona.com/doc/percona-xtradb-cluster/5.7/manual/xtrabackup_sst.html)
* [Encrypting PXC Traffic: 
ENCRYPTING SST TRAFFIC](https://www.percona.com/doc/percona-xtradb-cluster/5.7/security/encrypt-traffic.html#encrypt-sst)
* [XTRABACKUP PARAMETERS](https://galeracluster.com/library/documentation/xtrabackup-options.html)
* [SSL FOR STATE SNAPSHOT TRANSFERS: ENABLING SSL FOR XTRABACKUP](https://galeracluster.com/library/documentation/ssl-sst.html#ssl-xtrabackup)

