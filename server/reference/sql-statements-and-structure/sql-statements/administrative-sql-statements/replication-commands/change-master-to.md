# change-master-to

## CHANGE MASTER TO

The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.

##

## Syntax

```
CHANGE MASTER ['connection_name'] TO master_def [, master_def] ... 
 [FOR CHANNEL 'channel_name']

master_def:
 MASTER_BIND = 'interface_name'
 | MASTER_HOST = 'host_name'
 | MASTER_USER = 'user_name'
 | MASTER_PASSWORD = 'password'
 | MASTER_PORT = port_num
 | MASTER_CONNECT_RETRY = interval
 | MASTER_HEARTBEAT_PERIOD = interval
 | MASTER_LOG_FILE = 'master_log_name'
 | MASTER_LOG_POS = master_log_pos
 | RELAY_LOG_FILE = 'relay_log_name'
 | RELAY_LOG_POS = relay_log_pos
 | MASTER_DELAY = interval
 | MASTER_SSL = {0|1}
 | MASTER_SSL_CA = 'ca_file_name'
 | MASTER_SSL_CAPATH = 'ca_directory_name'
 | MASTER_SSL_CERT = 'cert_file_name'
 | MASTER_SSL_CRL = 'crl_file_name'
 | MASTER_SSL_CRLPATH = 'crl_directory_name'
 | MASTER_SSL_KEY = 'key_file_name'
 | MASTER_SSL_CIPHER = 'cipher_list'
 | MASTER_SSL_VERIFY_SERVER_CERT = {0|1}
 | MASTER_USE_GTID = {current_pos|slave_pos|no}
 | MASTER_DEMOTE_TO_SLAVE = bool
 | IGNORE_SERVER_IDS = (server_id_list)
 | DO_DOMAIN_IDS = ([N,..])
 | IGNORE_DOMAIN_IDS = ([N,..])
```

##

## Description

`CHANGE MASTER` is used on a replica to setup or change [replication](../../../../../kb/en/standard-replication/) settings for connecting to the primary.

##

**MariaDB starting with** [**10.7.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1070-release-notes)

The `FOR CHANNEL` keyword was added for MySQL compatibility. This is identical to\
using the channel\_name directly after `CHANGE MASTER`.

##

## Multi-Source Replication

If you are using [multi-source replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/multi-source-replication.md), then you need to specify a connection name when you execute `CHANGE MASTER`. There are two ways to do this:

* Setting the [default\_master\_connection](../../../../../kb/en/replication-and-binary-log-server-system-variables/#default_master_connection) system variable prior to executing `CHANGE MASTER`.
* Setting the `connection_name` parameter when executing `CHANGE MASTER`.

##

### default\_master\_connection

```
SET default_master_connection = 'gandalf';
STOP SLAVE;
CHANGE MASTER TO 
 MASTER_PASSWORD='new3cret';
START SLAVE;
```

##

### connection\_name

```
STOP SLAVE 'gandalf';
CHANGE MASTER 'gandalf' TO 
 MASTER_PASSWORD='new3cret';
START SLAVE 'gandalf';
```

##

## Options

##

### Connection Options

##

#### MASTER\_USER

The `MASTER_USER` option for `CHANGE MASTER` defines the user account that the [replica](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) will use to connect to the [primary](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql).

{% tabs %}
{% tab title="Current" %}
This user account needs the [REPLICATION REPLICA](../../account-management-sql-commands/grant.md#replication-replica) privilege on the primary.
{% endtab %}

{% tab title="MariaDB < 10.5.1" %}
#### Heading, for the whole purpose of being able to link to the tab <a href="#this-is-a-test-anchor" id="this-is-a-test-anchor"></a>

This user account needs the [REPLICATION SLAVE](../../account-management-sql-commands/grant.md#replication-slave) privilege on the primary.
{% endtab %}
{% endtabs %}

For example:

```
STOP SLAVE;
CHANGE MASTER TO
 MASTER_USER='repl',
 MASTER_PASSWORD='new3cret';
START SLAVE;
```

The maximum length of the `MASTER_USER` string is 96 characters until [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-105), and 128 characters from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-106).

##

#### MASTER\_PASSWORD

The `MASTER_PASSWORD` option for `CHANGE MASTER` defines the password that the [replica](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) will use to connect to the [primary](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) as the user account defined by the [MASTER\_USER](change-master-to.md#master_user) option.

For example:

```
STOP SLAVE;
CHANGE MASTER TO 
 MASTER_PASSWORD='new3cret';
START SLAVE;
```

The maximum length of the `MASTER_PASSWORD` string is 32 characters. The effective maximum length of the string depends on how many bytes are used per character and can be up to 96 characters.

Due to [MDEV-29994](https://jira.mariadb.org/browse/MDEV-29994), the password can be silently truncated to 41 characters when MariaDB is restarted. For this reason it is recommended to use a password that is shorter than this.

##

#### MASTER\_HOST

The `MASTER_HOST` option for `CHANGE MASTER` defines the hostname or IP address of the [primary](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql).

If you set the value of the `MASTER_HOST` option to the empty string, then that is not the same as not setting the option's value at all. If you set the value of the `MASTER_HOST` option to the empty string, then the `CHANGE MASTER` command will fail with an error. In [MariaDB 5.3](../../../../../kb/en/what-is-mariadb-53/) and before, if you set the value of the `MASTER_HOST` option to the empty string, then the `CHANGE MASTER` command would succeed, but the subsequent [START SLAVE](../../../../../kb/en/start-slave/) command would fail.

For example:

```
STOP SLAVE;
CHANGE MASTER TO
 MASTER_HOST='dbserver1.example.com',
 MASTER_USER='repl',
 MASTER_PASSWORD='new3cret',
 MASTER_USE_GTID=slave_pos;
START SLAVE;
```

If you set the value of the `MASTER_HOST` option in a `CHANGE MASTER` command, then the replica assumes that the primary is different from before, even if you set the value of this option to the same value it had previously. In this scenario, the replica will consider the old values for the primary's [binary\
log](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) file name and position to be invalid for the new primary. As a side effect, if you do not explicitly set the values of the [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options in the statement, then the statement will be implicitly appended with `MASTER_LOG_FILE=''` and `MASTER_LOG_POS=4`. However, if you enable [GTID](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) mode for replication by setting the [MASTER\_USE\_GTID](change-master-to.md#master_use_gtid) option to some value other than `no` in the statement, then these values will effectively be ignored anyway.

Replicas cannot connect to primaries using Unix socket files or Windows named pipes. The replica must connect to the primary using TCP/IP.

The maximum length of the `MASTER_HOST` string is 60 characters until [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-105), and 255 characters from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-106).

##

#### MASTER\_PORT

The `MASTER_PORT` option for `CHANGE MASTER` defines the TCP/IP port of the [primary](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql).

For example:

```
STOP SLAVE;
CHANGE MASTER TO
 MASTER_HOST='dbserver1.example.com',
 MASTER_PORT=3307,
 MASTER_USER='repl',
 MASTER_PASSWORD='new3cret',
 MASTER_USE_GTID=slave_pos;
START SLAVE;
```

If you set the value of the `MASTER_PORT` option in a `CHANGE MASTER` command, then the replica assumes that the primary is different from before, even if you set the value of this option to the same value it had previously. In this scenario, the replica will consider the old values for the primary's [binary\
log](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) file name and position to be invalid for the new primary. As a side effect, if you do not explicitly set the values of the [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options in the statement, then the statement will be implicitly appended with `MASTER_LOG_FILE=''` and `MASTER_LOG_POS=4`. However, if you enable [GTID](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) mode for replication by setting the [MASTER\_USE\_GTID](change-master-to.md#master_use_gtid) option to some value other than `no` in the statement, then these values will effectively be ignored anyway.

Replicas cannot connect to primaries using Unix socket files or Windows named pipes. The replica must connect to the primary using TCP/IP.

##

#### MASTER\_CONNECT\_RETRY

The `MASTER_CONNECT_RETRY` option for `CHANGE MASTER` defines how many seconds that the replica will wait between connection retries. The default is `60`.

```
STOP SLAVE;
CHANGE MASTER TO 
 MASTER_CONNECT_RETRY=20;
START SLAVE;
```

The number of connection attempts is limited by the [master\_retry\_count](../../../../../kb/en/mysqld-options/#-master-retry-count) option. It can be set either on the command-line or in a server [option group](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```
[mariadb]
...
master_retry_count=4294967295
```

##

#### MASTER\_BIND

The `MASTER_BIND` option for `CHANGE MASTER` is only supported by MySQL 5.6.2 and later and by MySQL NDB Cluster 7.3.1 and later. This option is not supported by MariaDB. See [MDEV-19248](https://jira.mariadb.org/browse/MDEV-19248) for more information.

The `MASTER_BIND` option for `CHANGE MASTER` can be used on replicas that have multiple network interfaces to choose which network interface the replica will use to connect to the primary.

##

#### MASTER\_HEARTBEAT\_PERIOD

The `MASTER_HEARTBEAT_PERIOD` option for `CHANGE MASTER` can be used to set the interval in seconds between replication heartbeats. Whenever the primary's [binary log](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) is updated with an event, the waiting period for the next heartbeat is reset.

This option's _interval_ argument has the following characteristics:

* It is a decimal value with a range of `0` to `4294967` seconds.
* It has a resolution of hundredths of a second.
* Its smallest valid non-zero value is `0.001`.
* Its default value is the value of the [slave\_net\_timeout](../../../../../kb/en/replication-and-binary-log-server-system-variables/#slave_net_timeout) system variable divided by 2.
* If it's set to `0`, then heartbeats are disabled.

Heartbeats are sent by the primary only if there are no unsent events in the binary log file for a period longer than the interval.

If the [RESET SLAVE](../../../../../kb/en/reset-slave-connection_name/) statement is executed, then the heartbeat interval is reset to the default.

If the [slave\_net\_timeout](../../../../../kb/en/replication-and-binary-log-server-system-variables/#slave_net_timeout) system variable is set to a value that is lower than the current heartbeat interval, then a warning will be issued.

##

### TLS Options

The TLS options are used for providing information about [TLS](../../../../../kb/en/data-in-transit-encryption/). The options can be set even on replicas that are compiled without TLS support. The TLS options are saved to either the default `master.info` file or the file that is configured by the [master\_info\_file](../../../../../kb/en/mysqld-options/#-master-info-file) option, but these TLS options are ignored unless the replica supports TLS.

See [Replication with Secure Connections](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/replication-with-secure-connections.md) for more information.

##

#### MASTER\_SSL

The `MASTER_SSL` option for `CHANGE MASTER` tells the replica whether to force [TLS](../../../../../kb/en/data-in-transit-encryption/) for the connection. The valid values are `0` or `1`. Required to be set to `1` for the other `MASTER_SSL*` options to have any effect.

For example:

```
STOP SLAVE;
CHANGE MASTER TO
 MASTER_SSL=1;
START SLAVE;
```

##

#### MASTER\_SSL\_CA

The `MASTER_SSL_CA` option for `CHANGE MASTER` defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for [TLS](../../../../../kb/en/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path.

For example:

```
STOP SLAVE;
CHANGE MASTER TO
 MASTER_SSL_CERT='/etc/my.cnf.d/certificates/server-cert.pem',
 MASTER_SSL_KEY='/etc/my.cnf.d/certificates/server-key.pem',
 MASTER_SSL_CA='/etc/my.cnf.d/certificates/ca.pem',
 MASTER_SSL_VERIFY_SERVER_CERT=1;
START SLAVE;
```

See [Secure Connections Overview: Certificate Authorities (CAs)](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information.

The maximum length of `MASTER_SSL_CA` string is 511 characters.

##

#### MASTER\_SSL\_CAPATH

The `MASTER_SSL_CAPATH` option for `CHANGE MASTER` defines a path to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for [TLS](../../../../../kb/en/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command.

For example:

```
STOP SLAVE;
CHANGE MASTER TO
 MASTER_SSL_CERT='/etc/my.cnf.d/certificates/server-cert.pem',
 MASTER_SSL_KEY='/etc/my.cnf.d/certificates/server-key.pem',
 MASTER_SSL_CAPATH='/etc/my.cnf.d/certificates/ca/',
 MASTER_SSL_VERIFY_SERVER_CERT=1;
START SLAVE;
```

See [Secure Connections Overview: Certificate Authorities (CAs)](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information.

The maximum length of `MASTER_SSL_CA_PATH` string is 511 characters.

##

#### MASTER\_SSL\_CERT

The `MASTER_SSL_CERT` option for `CHANGE MASTER` defines a path to the X509 certificate file to use for [TLS](../../../../../kb/en/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path.

For example:

```
STOP SLAVE;
CHANGE MASTER TO
 MASTER_SSL_CERT='/etc/my.cnf.d/certificates/server-cert.pem',
 MASTER_SSL_KEY='/etc/my.cnf.d/certificates/server-key.pem',
 MASTER_SSL_CA='/etc/my.cnf.d/certificates/ca.pem',
 MASTER_SSL_VERIFY_SERVER_CERT=1;
START SLAVE;
```

The maximum length of `MASTER_SSL_CERT` string is 511 characters.

##

#### MASTER\_SSL\_CRL

The `MASTER_SSL_CRL` option for `CHANGE MASTER` defines a path to a PEM file that should contain one or more revoked X509 certificates to use for [TLS](../../../../../kb/en/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path.

This option is only supported if the server was built with OpenSSL. If the server was built with yaSSL, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../../../../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.

For example:

```
STOP SLAVE;
CHANGE MASTER TO
 MASTER_SSL_CERT='/etc/my.cnf.d/certificates/server-cert.pem',
 MASTER_SSL_KEY='/etc/my.cnf.d/certificates/server-key.pem',
 MASTER_SSL_CA='/etc/my.cnf.d/certificates/ca.pem',
 MASTER_SSL_VERIFY_SERVER_CERT=1,
 MASTER_SSL_CRL='/etc/my.cnf.d/certificates/crl.pem';
START SLAVE;
```

See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information.

The maximum length of `MASTER_SSL_CRL` string is 511 characters.

##

#### MASTER\_SSL\_CRLPATH

The `MASTER_SSL_CRLPATH` option for `CHANGE MASTER` defines a path to a directory that contains one or more PEM files that should each contain one revoked X509 certificate to use for [TLS](../../../../../kb/en/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this variable needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command.

This option is only supported if the server was built with OpenSSL. If the server was built with yaSSL, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../../../../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.

For example:

```
STOP SLAVE;
CHANGE MASTER TO
 MASTER_SSL_CERT='/etc/my.cnf.d/certificates/server-cert.pem',
 MASTER_SSL_KEY='/etc/my.cnf.d/certificates/server-key.pem',
 MASTER_SSL_CA='/etc/my.cnf.d/certificates/ca.pem',
 MASTER_SSL_VERIFY_SERVER_CERT=1,
 MASTER_SSL_CRLPATH='/etc/my.cnf.d/certificates/crl/';
START SLAVE;
```

See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information.

The maximum length of `MASTER_SSL_CRL_PATH` string is 511 characters.

##

#### MASTER\_SSL\_KEY

The `MASTER_SSL_KEY` option for `CHANGE MASTER` defines a path to a private key file to use for [TLS](../../../../../kb/en/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path.

For example:

```
STOP SLAVE;
CHANGE MASTER TO
 MASTER_SSL_CERT='/etc/my.cnf.d/certificates/server-cert.pem',
 MASTER_SSL_KEY='/etc/my.cnf.d/certificates/server-key.pem',
 MASTER_SSL_CA='/etc/my.cnf.d/certificates/ca.pem',
 MASTER_SSL_VERIFY_SERVER_CERT=1;
START SLAVE;
```

The maximum length of `MASTER_SSL_KEY` string is 511 characters.

##

#### MASTER\_SSL\_CIPHER

The `MASTER_SSL_CIPHER` option for `CHANGE MASTER` defines the list of permitted ciphers or cipher suites to use for [TLS](../../../../../kb/en/data-in-transit-encryption/). Besides cipher names, if MariaDB was compiled with OpenSSL, this option could be set to "SSLv3" or "TLSv1.2" to allow all SSLv3 or all TLSv1.2 ciphers. Note that the TLSv1.3 ciphers cannot be excluded when using OpenSSL, even by using this option. See [Using TLSv1.3](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/using-tlsv13.md) for details.

For example:

```
STOP SLAVE;
CHANGE MASTER TO
 MASTER_SSL_CERT='/etc/my.cnf.d/certificates/server-cert.pem',
 MASTER_SSL_KEY='/etc/my.cnf.d/certificates/server-key.pem',
 MASTER_SSL_CA='/etc/my.cnf.d/certificates/ca.pem',
 MASTER_SSL_VERIFY_SERVER_CERT=1,
 MASTER_SSL_CIPHER='TLSv1.2';
START SLAVE;
```

The maximum length of `MASTER_SSL_CIPHER` string is 511 characters.

##

#### MASTER\_SSL\_VERIFY\_SERVER\_CERT

The `MASTER_SSL_VERIFY_SERVER_CERT` option for `CHANGE MASTER` enables [server certificate verification](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification). This option is disabled by default prior to [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-114), and enabled by default from [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-114).

For example:

```
STOP SLAVE;
CHANGE MASTER TO
 MASTER_SSL_CERT='/etc/my.cnf.d/certificates/server-cert.pem',
 MASTER_SSL_KEY='/etc/my.cnf.d/certificates/server-key.pem',
 MASTER_SSL_CA='/etc/my.cnf.d/certificates/ca.pem',
 MASTER_SSL_VERIFY_SERVER_CERT=1;
START SLAVE;
```

See [Secure Connections Overview: Server Certificate Verification](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification) for more information.

##

### Binary Log Options

These options are related to the [binary log](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) position on the primary.

##

#### MASTER\_LOG\_FILE

The `MASTER_LOG_FILE` option for `CHANGE MASTER` can be used along with `MASTER_LOG_POS` to specify the coordinates at which the [replica's I/O thread](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#slave-io-thread) should begin reading from the primary's [binary logs](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) the next time the thread starts.

For example:

```
STOP SLAVE;
CHANGE MASTER TO
 MASTER_LOG_FILE='master2-bin.001',
 MASTER_LOG_POS=4;
START SLAVE;
```

The [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options cannot be specified if the [RELAY\_LOG\_FILE](change-master-to.md#relay_log_file) and [RELAY\_LOG\_POS](change-master-to.md#relay_log_pos) options were also specified.

The [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options are effectively ignored if you enable [GTID](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) mode for replication by setting the [MASTER\_USE\_GTID](change-master-to.md#master_use_gtid) option to some value other than `no` in the statement.

##

#### MASTER\_LOG\_POS

The `MASTER_LOG_POS` option for `CHANGE MASTER` can be used along with `MASTER_LOG_FILE` to specify the coordinates at which the [replica's I/O thread](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#slave-io-thread) should begin reading from the primary's [binary logs](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) the next time the thread starts.

For example:

```
STOP SLAVE;
CHANGE MASTER TO
 MASTER_LOG_FILE='master2-bin.001',
 MASTER_LOG_POS=4;
START SLAVE;
```

The [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options cannot be specified if the [RELAY\_LOG\_FILE](change-master-to.md#relay_log_file) and [RELAY\_LOG\_POS](change-master-to.md#relay_log_pos) options were also specified.

The [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options are effectively ignored if you enable [GTID](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) mode for replication by setting the [MASTER\_USE\_GTID](change-master-to.md#master_use_gtid) option to some value other than `no` in the statement.

##

### Relay Log Options

These options are related to the [relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) position on the replica.

##

#### RELAY\_LOG\_FILE

The `RELAY_LOG_FILE` option for `CHANGE MASTER` can be used along with the [RELAY\_LOG\_POS](change-master-to.md#relay_log_pos) option to specify the coordinates at which the [replica's SQL thread](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#slave-sql-thread) should begin reading from the [relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) the next time the thread starts.

The `CHANGE MASTER` statement usually deletes all [relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) files. However, if the `RELAY_LOG_FILE` and/or `RELAY_LOG_POS` options are specified, then existing [relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) files are kept.

When you want to change the [relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) position, you only need to stop the [replica's SQL thread](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#slave-sql-thread). The [replica's I/O thread](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#slave-io-thread) can continue running. The [STOP SLAVE](../../../../../kb/en/stop-slave/) and [START SLAVE](../../../../../kb/en/start-slave/) statements support the `SQL_THREAD` option for this scenario. For example:

```
STOP SLAVE SQL_THREAD;
CHANGE MASTER TO
 RELAY_LOG_FILE='slave-relay-bin.006',
 RELAY_LOG_POS=4025;
START SLAVE SQL_THREAD;
```

When the value of this option is changed, the metadata about the [replica's SQL thread's](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#slave-sql-thread) position in the [relay logs](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) will also be changed in the `relay-log.info` file or the file that is configured by the [relay\_log\_info\_file](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#relay_log_info_file) system variable.

The [RELAY\_LOG\_FILE](change-master-to.md#relay_log_file) and [RELAY\_LOG\_POS](change-master-to.md#relay_log_pos) options cannot be specified if the [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options were also specified.

##

#### RELAY\_LOG\_POS

The `RELAY_LOG_POS` option for `CHANGE MASTER` can be used along with the [RELAY\_LOG\_FILE](change-master-to.md#relay_log_file) option to specify the coordinates at which the [replica's SQL thread](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#slave-sql-thread) should begin reading from the [relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) the next time the thread starts.

The `CHANGE MASTER` statement usually deletes all [relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) files. However, if the `RELAY_LOG_FILE` and/or `RELAY_LOG_POS` options are specified, then existing [relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) files are kept.

When you want to change the [relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) position, you only need to stop the [replica's SQL thread](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#slave-sql-thread). The [replica's I/O thread](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#slave-io-thread) can continue running. The [STOP SLAVE](../../../../../kb/en/stop-slave/) and [START SLAVE](../../../../../kb/en/start-slave/) statements support the `SQL_THREAD` option for this scenario. For example:

```
STOP SLAVE SQL_THREAD;
CHANGE MASTER TO
 RELAY_LOG_FILE='slave-relay-bin.006',
 RELAY_LOG_POS=4025;
START SLAVE SQL_THREAD;
```

When the value of this option is changed, the metadata about the [replica's SQL thread's](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#slave-sql-thread) position in the [relay logs](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) will also be changed in the `relay-log.info` file or the file that is configured by the [relay\_log\_info\_file](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#relay_log_info_file) system variable.

The [RELAY\_LOG\_FILE](change-master-to.md#relay_log_file) and [RELAY\_LOG\_POS](change-master-to.md#relay_log_pos) options cannot be specified if the [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options were also specified.

##

### GTID Options

##

#### MASTER\_USE\_GTID

The `MASTER_USE_GTID` option for `CHANGE MASTER` can be used to configure the replica to use the [global transaction ID (GTID)](../../../../../kb/en/global-transaction-id/) when connecting to a primary. The possible values are:

* `current_pos` - Replicate in [GTID](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) mode and use [gtid\_current\_pos](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md#gtid_current_pos) as the position to start downloading transactions from the primary. Using to transition to primary can break the replication state if the replica executes local transactions due to actively updating gtid\_current\_pos with gtid\_binlog\_pos and gtid\_slave\_pos. Use the new, safe, [MASTER\_DEMOTE\_TO\_SLAVE=](change-master-to.md#master_demote_to_slave) option instead.
* `slave_pos` - Replicate in [GTID](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) mode and use [gtid\_slave\_pos](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md#gtid_slave_pos) as the position to start downloading transactions from the primary. From [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1051-release-notes), `replica_pos` is an alias for `slave_pos`.
* `no` - Don't replicate in [GTID](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) mode.

For example:

```
STOP SLAVE;
CHANGE MASTER TO
 MASTER_USE_GTID = current_pos;
START SLAVE;
```

Or:

```
STOP SLAVE;
SET GLOBAL gtid_slave_pos='0-1-153';
CHANGE MASTER TO
 MASTER_USE_GTID = slave_pos;
START SLAVE;
```

##

#### MASTER\_DEMOTE\_TO\_SLAVE

##

**MariaDB starting with** [**10.10**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-1010)

Used to transition a primary to become a replica. Replaces the old [MASTER\_USE\_GTID=current\_pos](change-master-to.md#master_use_gtid) with a safe alternative by forcing users to set `Using_Gtid=Slave_Pos` and merging `gtid_binlog_pos` into `gtid_slave_pos` once at `CHANGE MASTER TO` time. If `gtid_slave_pos` is more\
recent than `gtid_binlog_pos` (as in the case of chain replication), the replication state should be preserved.

For example:

```
STOP SLAVE;
CHANGE MASTER TO
 MASTER_DEMOTE_TO_SLAVE = 1;
START SLAVE;
```

##

### Replication Filter Options

Also see [Replication filters](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-filters.md).

##

#### IGNORE\_SERVER\_IDS

The `IGNORE_SERVER_IDS` option for `CHANGE MASTER` can be used to configure a [replica](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to ignore [binary log](binary_log/) events that originated from certain servers. Filtered [binary log](binary_log/) events will not get logged to the replica’s [relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md), and they will not be applied by the replica.

The option's value can be specified by providing a comma-separated list of [server\_id](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#server_id) values. For example:

```
STOP SLAVE;
CHANGE MASTER TO 
 IGNORE_SERVER_IDS = (3,5);
START SLAVE;
```

If you would like to clear a previously set list, then you can set the value to an empty list. For example:

```
STOP SLAVE;
CHANGE MASTER TO 
 IGNORE_SERVER_IDS = ();
START SLAVE;
```

##

#### DO\_DOMAIN\_IDS

The `DO_DOMAIN_IDS` option for `CHANGE MASTER` can be used to configure a [replica](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to only apply [binary log](binary_log/) events if the transaction's [GTID](../../../../../kb/en/global-transaction-id/) is in a specific [gtid\_domain\_id](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md#gtid_domain_id) value. Filtered [binary log](binary_log/) events will not get logged to the replica’s [relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md), and they will not be applied by the replica.

The option's value can be specified by providing a comma-separated list of [gtid\_domain\_id](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md#gtid_domain_id) values. Duplicate values are automatically ignored. For example:

```
STOP SLAVE;
CHANGE MASTER TO 
 DO_DOMAIN_IDS = (1,2);
START SLAVE;
```

If you would like to clear a previously set list, then you can set the value to an empty list. For example:

```
STOP SLAVE;
CHANGE MASTER TO 
 DO_DOMAIN_IDS = ();
START SLAVE;
```

The [DO\_DOMAIN\_IDS](change-master-to.md#do_domain_ids) option and the [IGNORE\_DOMAIN\_IDS](change-master-to.md#ignore_domain_ids) option cannot both be set to non-empty values at the same time. If you want to set the [DO\_DOMAIN\_IDS](change-master-to.md#do_domain_ids) option, and the [IGNORE\_DOMAIN\_IDS](change-master-to.md#ignore_domain_ids) option was previously set, then you need to clear the value of the [IGNORE\_DOMAIN\_IDS](change-master-to.md#ignore_domain_ids) option. For example:

```
STOP SLAVE;
CHANGE MASTER TO 
 IGNORE_DOMAIN_IDS = (), 
 DO_DOMAIN_IDS = (1,2);
START SLAVE;
```

The `DO_DOMAIN_IDS` option can only be specified if the replica is replicating in [GTID](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) mode. Therefore, the [MASTER\_USE\_GTID](change-master-to.md#master_use_gtid) option must also be set to some value other than `no` in order to use this option.

##

#### IGNORE\_DOMAIN\_IDS

The `IGNORE_DOMAIN_IDS` option for `CHANGE MASTER` can be used to configure a [replica](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to ignore [binary log](binary_log/) events if the transaction's [GTID](../../../../../kb/en/global-transaction-id/) is in a specific [gtid\_domain\_id](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md#gtid_domain_id) value. Filtered [binary log](binary_log/) events will not get logged to the replica’s [relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md), and they will not be applied by the replica.

The option's value can be specified by providing a comma-separated list of [gtid\_domain\_id](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md#gtid_domain_id) values. Duplicate values are automatically ignored. For example:

```
STOP SLAVE;
CHANGE MASTER TO 
 IGNORE_DOMAIN_IDS = (1,2);
START SLAVE;
```

If you would like to clear a previously set list, then you can set the value to an empty list. For example:

```
STOP SLAVE;
CHANGE MASTER TO 
 IGNORE_DOMAIN_IDS = ();
START SLAVE;
```

The [DO\_DOMAIN\_IDS](change-master-to.md#do_domain_ids) option and the [IGNORE\_DOMAIN\_IDS](change-master-to.md#ignore_domain_ids) option cannot both be set to non-empty values at the same time. If you want to set the [IGNORE\_DOMAIN\_IDS](change-master-to.md#ignore_domain_ids) option, and the [DO\_DOMAIN\_IDS](change-master-to.md#do_domain_ids) option was previously set, then you need to clear the value of the [DO\_DOMAIN\_IDS](change-master-to.md#do_domain_ids) option. For example:

```
STOP SLAVE;
CHANGE MASTER TO 
 DO_DOMAIN_IDS = (), 
 IGNORE_DOMAIN_IDS = (1,2);
START SLAVE;
```

The `IGNORE_DOMAIN_IDS` option can only be specified if the replica is replicating in [GTID](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) mode. Therefore, the [MASTER\_USE\_GTID](change-master-to.md#master_use_gtid) option must also be set to some value other than `no` in order to use this option.

##

### Delayed Replication Options

##

#### MASTER\_DELAY

The `MASTER_DELAY` option for `CHANGE MASTER` can be used to enable [delayed replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/delayed-replication.md). This option specifies the time in seconds (at least) that a replica should lag behind the primary up to a maximum value of 2147483647, or about 68 years. Before executing an event, the replica will first wait, if necessary, until the given time has passed since the event was created on the primary. The result is that the replica will reflect the state of the primary some time back in the past. The default is zero, no delay.

```
STOP SLAVE;
CHANGE MASTER TO 
 MASTER_DELAY=3600;
START SLAVE;
```

##

## Changing Option Values

If you don't specify a given option when executing the `CHANGE MASTER` statement, then the option keeps its old value in most cases. Most of the time, there is no need to specify the options that do not need to change. For example, if the password for the user account that the replica uses to connect to its primary has changed, but no other options need to change, then you can just change the [MASTER\_PASSWORD](change-master-to.md#master_password) option by executing the following commands:

```
STOP SLAVE;
CHANGE MASTER TO 
 MASTER_PASSWORD='new3cret';
START SLAVE;
```

There are some cases where options are implicitly reset, such as when the [MASTER\_HOST](change-master-to.md#master_host) and [MASTER\_PORT](change-master-to.md#master_port) options are changed.

##

## Option Persistence

The values of the [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options (i.e. the [binary log](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) position on the primary) and most other options are written to either the default `master.info` file or the file that is configured by the [master\_info\_file](../../../../../kb/en/mysqld-options/#-master-info-file) option. The [replica's I/O thread](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#slave-io-thread) keeps this [binary log](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) position updated as it downloads events only when [MASTER\_USE\_GTID](change-master-to.md#master_use_gtid) option\
is set to `NO`. Otherwise the file is not updated on a per event basis.

The [master\_info\_file](../../../../../kb/en/mysqld-options/#-master-info-file) option can be set either on the command-line or in a server [option group](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```
[mariadb]
...
master_info_file=/mariadb/myserver1-master.info
```

The values of the [RELAY\_LOG\_FILE](change-master-to.md#relay_log_file) and [RELAY\_LOG\_POS](change-master-to.md#relay_log_pos) options (i.e. the [relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) position) are written to either the default `relay-log.info` file or the file that is configured by the [relay\_log\_info\_file](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#relay_log_info_file) system variable. The [replica's SQL thread](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#slave-sql-thread) keeps this [relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) position updated as it applies events.

The [relay\_log\_info\_file](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#relay_log_info_file) system variable can be set either on the command-line or in a server [option group](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```
[mariadb]
...
relay_log_info_file=/mariadb/myserver1-relay-log.info
```

##

## GTID Persistence

If the replica is replicating [binary log](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) events that contain [GTIDs](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md), then the [replica's SQL thread](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#slave-sql-thread) will write every GTID that it applies to the [mysql.gtid\_slave\_pos](../system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) table. This GTID can be inspected and modified through the [gtid\_slave\_pos](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md#gtid_slave_pos) system variable.

If the replica has the [log\_slave\_updates](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#log_slave_updates) system variable enabled and if the replica has the [binary log](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) enabled, then every write by the [replica's SQL thread](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#slave-sql-thread) will also go into the replica's [binary log](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md). This means that [GTIDs](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) of replicated transactions would be reflected in the value of the [gtid\_binlog\_pos](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md#gtid_binlog_pos) system variable.

##

## Creating a Replica from a Backup

The `CHANGE MASTER` statement is useful for setting up a replica when you have a backup of the primary and you also have the [binary log](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) position or [GTID](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) position corresponding to the backup.

After restoring the backup on the replica, you could execute something like this to use the [binary log](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) position:

```
CHANGE MASTER TO
 MASTER_LOG_FILE='master2-bin.001',
 MASTER_LOG_POS=4;
START SLAVE;
```

Or you could execute something like this to use the [GTID](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) position:

```
SET GLOBAL gtid_slave_pos='0-1-153';
CHANGE MASTER TO
 MASTER_USE_GTID=slave_pos;
START SLAVE;
```

See [Setting up a Replication Slave with Mariabackup](../../../../../kb/en/setting-up-a-replication-slave-with-mariabackup/) for more information on how to do this with [Mariabackup](../../../../../server-usage/replication-cluster-multi-master/galera-cluster/state-snapshot-transfers-ssts-in-galera-cluster/mariabackup-sst-method.md).

##

## Example

The following example changes the primary and primary's binary log coordinates.\
This is used when you want to set up the replica to replicate the primary:

```
CHANGE MASTER TO
 MASTER_HOST='master2.mycompany.com',
 MASTER_USER='replication',
 MASTER_PASSWORD='bigs3cret',
 MASTER_PORT=3306,
 MASTER_LOG_FILE='master2-bin.001',
 MASTER_LOG_POS=4,
 MASTER_CONNECT_RETRY=10;
START SLAVE;
```

##

## See Also

* [Setting up replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/setting-up-replication.md)
* [START SLAVE](../../../../../kb/en/start-slave/)
* [Multi-source replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/multi-source-replication.md)
* [RESET SLAVE](../../../../../kb/en/reset-slave-connection_name/). Removes a connection created with `CHANGE MASTER TO`.
* [Global Transaction ID](../../../../../kb/en/global-transaction-id/)
