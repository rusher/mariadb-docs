---
icon: question
---

# mariadb-import

## mariadb-import

`mariadb-import` loads tables from text files in various formats.

Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), the client was called `mysqlimport`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

`mariadb-import` loads tables from text files in various formats. The base name\
of the text file must be the name of the table that should be used. If one\
uses sockets to connect to the MariaDB server, the server will open and read the\
text file directly. In other cases the client will open the text file. The SQL\
command [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) is used to import the rows.

### Using mariadb-import

The command to use `mariadb-import` and the general syntax is:

```
mariadb-import [OPTIONS] database textfile1 [textfile2 ...]
```

#### Options

`mariadb-import` supports the following options:

| Variable| Description|
| - | - |
| --character-sets-dir=name | Directory for character set files. |
| -c cols, --columns=cols | Use only these columns to import the data to. Give the column names in a comma separated list. This is same as giving columns to [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md). |
| -C, --compress| Use compression in server/client protocol. |
| --database=name | Restore the specified database, ignoring others.To specify more than one database to include, use the directive multiple times, once for each database. Only takes effect when used together with the --dir option. From [MariaDB 11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116). |
| ## \[options] , --debug\[=options] | Output debug log. Often this is d:t:o,filename. The default is d:t:o. |
| --debug-check | Check memory and open file usage at exit. |
| --debug-info | Print some debug info at exit. |
| --default-auth=plugin | Default authentication client-side plugin to use. |
| --default-character-set=name | Set the default [character set](../../reference/data-types/string-data-types/character-sets/). |
| --defaults-extra-file=name | Read this file after the global files are read. Must be given as the first option. |
| --defaults-file=name | Only read default options from the given file name Must be given as the first option. |
| --defaults-group-suffix=name | In addition to the given groups, also read groups with this suffix. |
| -d, --delete | First delete all rows from table. |
| --dir=name | Restore all tables from backup directory created using [mariadb-dump --dir](mariadb-dump.md). From [MariaDB 11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116). |
| --fields-terminated-by=name | Fields in the input file are terminated by the given string. |
| --fields-enclosed-by=name | Fields in the import file are enclosed by the given character. |
| --fields-optionally-enclosed-by=name | Fields in the input file are optionally enclosed by the given character. |
| --fields-escaped-by=name | Fields in the input file are escaped by the given character. |
| -f, --force | Continue even if we get an SQL error. |
| -?, --help | Displays this help and exits. |
| -h name, --host=name | Connect to host. |
| -i, --ignore | If duplicate unique key was found, keep old row. |
| k, --ignore-foreign-keys | Disable foreign key checks while importing the data. |
| --ignore-database=name | Do not restore the specified database. To specify more than one database to ignore, use the directive multiple times, once for each database. Only takes effect when used together with the --dir option. From [MariaDB 11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116). |
| --ignore-lines=n | Ignore first n lines of data infile. |
| --ignore-table=name | Do not restore the specified table. To specify more than one table to ignore, use the directive multiple times, once for each table. Each table must be specified with both database and table names, e.g. --ignore-table=database.table. Only takes effect when used together with the --dir option. From [MariaDB 11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116). |
| --innodb-optimize-keys | Create secondary indexes after data load, which speeds up loading (InnoDB only). Defaults to on; use --skip-innodb-optimize-keys to disable. From [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-8-series/what-is-mariadb-118). |
| --lines-terminated-by=name | Lines in the input file are terminated by the given string. |
| -L, --local | Read all files through the client. |
| -l, --lock-tables | Lock all tables for write (this disables threads). |
| --low-priority | Use LOW\_PRIORITY when updating the table. |
| --no-defaults | Don't read default options from any option file. Must be given as the first option. |
| -j, --parallel=num | Number of LOAD DATA jobs executed in parallel. From [MariaDB 11.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/mariadb-11-4-1-release-notes). --use-threads is a synonym. |
| -p\[passwd], --password\[=passwd] | Password to use when connecting to server. If password is not given it's asked from the terminal. Specifying a password on the command line should be considered insecure. You can use an option file to avoid giving the password on the command line. |
| --pipe, -W | On Windows, connect to the server via a named pipe. This option applies only if the server supports named-pipe connections. |
| --plugin-dir | Directory for client-side plugins. |
| -P num, --port=num | Port number to use for connection or 0 for default to, in order of preference, my.cnf, the MYSQL\_TCP\_PORT [environment variable](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-environment-variables.md), /etc/services, built-in default (3306). |
| --print-defaults | Print the program argument list and exit. Must be given as the first option. |
| --protocol=name | The protocol to use for connection (tcp, socket, pipe, memory). |
| -r, --replace | If duplicate unique key was found, replace old row. |
| --shared-memory-base-name | Shared-memory name to use for Windows connections using shared memory to a local server (started with the --shared-memory option). Case-sensitive. |
| -s, --silent | Silent mode. Produce output only when errors occur. |
| -S, --socket=name | For connections to localhost, the Unix socket file to use, or, on Windows, the name of the named pipe to use. |
| --ssl | Enables [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). TLS is also enabled even without setting this option when certain other TLS options are set. The --ssl option does not enable [verifying the server certificate](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification) by default. In order to verify the server certificate, the user must specify the --ssl-verify-server-cert option. |
| --ssl-ca=name | Defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Authorities (CAs)](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information. This option implies the --ssl option. |
| --ssl-capath=name | Defines a path to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Authorities (CAs)](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information. This option is only supported if the client was built with OpenSSL or yaSSL. If the client was built with GnuTLS or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms. This option implies the --ssl option. |
| --ssl-cert=name | Defines a path to the X509 certificate file to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. This option implies the --ssl option. |
| --ssl-cipher=name | List of permitted ciphers or cipher suites to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option implies the --ssl option. |
| --ssl-crl=name | Defines a path to a PEM file that should contain one or more revoked X509 certificates to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information. This option is only supported if the client was built with OpenSSL or Schannel. If the client was built with yaSSL or GnuTLS, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms. |
| --ssl-crlpath=name | Defines a path to a directory that contains one or more PEM files that should each contain one revoked X509 certificate to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information. This option is only supported if the client was built with OpenSSL. If the client was built with yaSSL, GnuTLS, or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms. |
| --ssl-key=name | Defines a path to a private key file to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. This option implies the --ssl option. |
| --ssl-verify-server-cert | Enables [server certificate verification](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification). This option is disabled by default. |
| --table=name | Restore the specified table ignoring others. Use --table=dbname.tablename with this option. To specify more than one table to include, use the directive multiple times, once for each table. Only takes effect when used together with the --dir option. From [MariaDB 11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116). |
| --tls-version=name | This option accepts a comma-separated list of TLS protocol versions. A TLS protocol version will only be enabled if it is present in this list. All other TLS protocol versions will not be permitted. See [Secure Connections Overview: TLS Protocol Versions](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#tls-protocol-versions) for more information. |
| --use-threads=num | Load files in parallel. The argument is the number of threads to use for loading data. From [MariaDB 11.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/mariadb-11-4-1-release-notes), a synonym for -j, --parallel=num. |
| -u name, --user=name | User for login if not current user. |
| -v, --verbose | Print info about the various stages. |
| -V, --version | Output version information and exit. |

#### Option Files

In addition to reading options from the command-line, `mariadb-import` can also read options from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). If an unknown option is provided to `mariadb-import` in an option file, then it is ignored.

The following options relate to how MariaDB command-line tools handles option files. They must be given as the first argument on the command-line:

| Option| Description|
| - | - |
| --print-defaults| Print the program argument list and exit.|
| --no-defaults | Don't read default options from any option file. |
| --defaults-file=# | Only read default options from the given file #. |
| --defaults-extra-file=# | Read this file after the global files are read.|

`mariadb-import` is linked with [MariaDB Connector/C](../../../kb/en/about-mariadb-connector-c/). Therefore, it may be helpful to see [Configuring MariaDB Connector/C with Option Files](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/configuring-mariadb-connectorc-with-option-files) for more information on how MariaDB Connector/C handles option files.

**Option Groups**

`mariadb-import` reads options from the following [option groups](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group | Description |
| - | - |
| \[mysqlimport]| Options read by mysqlimport, which includes both MariaDB Server and MySQL Server. |
| \[mariadb-import] | Options read by mysqlimport.|
| \[client] | Options read by all MariaDB and MySQL [client programs](../../../kb/en/clients-utilities/), which includes both MariaDB and MySQL clients. For example, mysqldump.|
| \[client-server]| Options read by all MariaDB [client programs](../../../kb/en/clients-utilities/) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. |
| \[client-mariadb] | Options read by all MariaDB [client programs](../../../kb/en/clients-utilities/). |

#### Default Values

| Variables | Value (after reading options) |
| - | - |
| character-sets-dir | (No default value) |
| default-character-set | latin1 |
| columns | (No default value) |
| compress | FALSE |
| debug-check | FALSE |
| debug-info | FALSE |
| delete | FALSE |
| fields-terminated-by | (No default value) |
| fields-enclosed-by | (No default value) |
| fields-optionally-enclosed-by | (No default value) |
| fields-escaped-by | (No default value) |
| force | FALSE |
| host | (No default value) |
| ignore | FALSE |
| ignore-lines | 0 |
| lines-terminated-by | (No default value) |
| local | FALSE |
| lock-tables | FALSE |
| low-priority | FALSE |
| port | 3306 |
| replace | FALSE |
| silent | FALSE |
| socket | /var/run/mysqld/mysqld.sock |
| ssl | FALSE |
| ssl-ca | (No default value) |
| ssl-capath | (No default value) |
| ssl-cert | (No default value) |
| ssl-cipher | (No default value) |
| ssl-key | (No default value) |
| ssl-verify-server-cert | FALSE |
| use-threads | 0 |
| user | (No default value) |
| verbose | FALSE |

CC BY-SA / Gnu FDL
