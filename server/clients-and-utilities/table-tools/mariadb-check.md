# mariadb-check

## mariadb-check

`mariadb-check` is a maintenance tool that allows you to check, repair, analyze and optimize multiple tables from the command line.

Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), the client was called `mysqlcheck`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

It is essentially a commandline interface to the [CHECK TABLE](../../reference/sql-statements/table-statements/check-table.md), [REPAIR TABLE](../../reference/sql-statements/table-statements/repair-table.md), [ANALYZE TABLE](../../reference/sql-statements/table-statements/analyze-table.md) and [OPTIMIZE TABLE](../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) commands, and so, unlike [myisamchk](../myisam-clients-and-utilities/myisamchk.md) and [aria\_chk](../aria-clients-and-utilities/aria_chk.md), requires the server to be running.

This tool does not work with partitioned tables.

### Using mariadb-check

```
./client/mariadb-check [OPTIONS] database [tables]
```

OR

```
./client/mariadb-check [OPTIONS] --databases DB1 [DB2 DB3...]
```

OR

```
./client/mariadb-check [OPTIONS] --all-databases
```

`mariadb-check` can be used to CHECK (-c, -m, -C), REPAIR (-r), ANALYZE (-a),\
or OPTIMIZE (-o) tables. Some of the options (like -e or -q) can be\
used at the same time. Not all options are supported by all storage engines.

The -c, -r, -a and -o options are exclusive to each other.

The option `--check` will be used by default, if no other options were specified.\
You can change the default behavior by making a symbolic link to the binary, or\
copying it somewhere with another name, the alternatives are:

|               |                                            |
| ------------- | ------------------------------------------ |
| mysqlrepair   | The default option will be -r (--repair)   |
| mysqlanalyze  | The default option will be -a (--analyze)  |
| mysqloptimize | The default option will be -o (--optimize) |

#### Options

`mariadb-check` supports the following options:

| Option                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Option                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -A, --all-databases       | Check all the databases. This is the same as --databases with all databases selected.                                                                                                                                                                                                                                                                                                                                        |
| -1, --all-in-1            | Instead of issuing one query for each table, use one query per database, naming all tables in the database in a comma-separated list.                                                                                                                                                                                                                                                                                        |
| -a, --analyze             | Analyze given tables.                                                                                                                                                                                                                                                                                                                                                                                                        |
| --auto-repair             | If a checked table is corrupted, automatically fix it. Repairing will be done after all tables have been checked.                                                                                                                                                                                                                                                                                                            |
| --character-sets-dir=name | Directory where [character set](../../reference/data-types/string-data-types/character-sets/) files are installed.                                                                                                                                                                                                                                                                                                           |
| -c, --check               | Check table for errors.                                                                                                                                                                                                                                                                                                                                                                                                      |
| -C, --check-only-changed  | Check only tables that have changed since last check or haven't been closed properly.                                                                                                                                                                                                                                                                                                                                        |
| -g, --check-upgrade       | Check tables for version-dependent changes. May be used with --auto-repair to correct tables requiring version-dependent updates. Automatically enables the --fix-db-names and --fix-table-names options. Used [when upgrading](../../server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/migrating-to-mariadb-from-mysql-obsolete-articles/upgrading-to-mariadb-from-mysql-50-or-older.md) |
| --compress                | Compress all information sent between the client and server if both support compression.                                                                                                                                                                                                                                                                                                                                     |
| -B, --databases           | Check several databases. Note that normally mariadb-check treats the first argument as a database name, and following arguments as table names. With this option, no tables are given, and all name arguments are regarded as database names.                                                                                                                                                                                |
| -                         |                                                                                                                                                                                                                                                                                                                                                                                                                              |

## , --debug\[=name] | Output debug log. Often this is 'd:t:o,filename'. |

\| --debug-check | Check memory and open file usage at exit. |\
\| --debug-info | Print some debug info at exit. |\
\| --default-auth=plugin | Default authentication client-side plugin to use. |\
\| --default-character-set=name | Set the default [character set](../../reference/data-types/string-data-types/character-sets/). |\
\| -e, --extended | If you are using this option with --check, it will ensure that the table is 100 percent consistent, but will take a long time. If you are using this option with --repair, it will force using the old, slow, repair with keycache method, instead of the much faster repair by sorting. |\
\| -F, --fast | Check only tables that haven't been closed properly. |\
\| --fix-db-names | Convert database names to the format used since MySQL 5.1. Only database names that contain special characters are affected. Used [when upgrading](../../server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/migrating-to-mariadb-from-mysql-obsolete-articles/upgrading-to-mariadb-from-mysql-50-or-older.md) from an old MySQL version. |\
\| --fix-table-names | Convert table names (including [views](../../server-usage/views/)) to the format used since MySQL 5.1. Only table names that contain special characters are affected. Used [when upgrading](../../server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/migrating-to-mariadb-from-mysql-obsolete-articles/upgrading-to-mariadb-from-mysql-50-or-older.md) from an old MySQL version. |\
\| --flush | Flush each table after check. This is useful if you don't want to have the checked tables take up space in the caches after the check. |\
\| -f, --force | Continue even if we get an SQL error. |\
\| -?, --help | Display this help message and exit. |\
\| -h name, --host=name | Connect to the given host. |\
\| -m, --medium-check | Faster than extended-check, but only finds 99.99 percent of all errors. Should be good enough for most cases. |\
\| -o, --optimize | Optimize tables. |\
\| -p, --password\[=name] | Password to use when connecting to the server. If you use the short option form (-p), you cannot have a space between the option and the password. If you omit the password value following the --password or -p option on the command line, mariadb-check prompts for one. Specifying a password on the command line should be considered insecure. You can use an option file to avoid giving the password on the command line. |\
\| -Z, --persistent | When using ANALYZE TABLE (--analyze), uses the PERSISTENT FOR ALL option, which forces [Engine-independent Statistics](../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md) for this table to be updated. Added in [MariaDB 10.1.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10110-release-notes) |\
\| -W, --pipe | On Windows, connect to the server via a named pipe. This option applies only if the server supports named-pipe connections. |\
\| --plugin-dir | Directory for client-side plugins. |\
\| -P num, --port=num | Port number to use for connection or 0 for default to, in order of preference, my.cnf, $MYSQL\_TCP\_PORT, /etc/services, built-in default (3306). |\
\| --process-tables | Perform the requested operation (check, repair, analyze, optimize) on tables. Enabled by default. Use --skip-process-tables to disable. |\
\| --process-views\[=val] | Perform the requested operation (only [CHECK VIEW](../../reference/sql-statements/table-statements/check-view.md) or [REPAIR VIEW](../../reference/sql-statements/table-statements/repair-view.md)). Possible values are NO, YES (correct the checksum, if necessary, add the mariadb-version field), UPGRADE\_FROM\_MYSQL (same as YES and toggle the algorithm MERGE<->TEMPTABLE. |\
\| --protocol=name | The connection protocol (tcp, socket, pipe, memory) to use for connecting to the server. Useful when other connection parameters would cause a protocol to be used other than the one you want. |\
\| -q, --quick | If you are using this option with CHECK TABLE, it prevents the check from scanning the rows to check for wrong links. This is the fastest check. If you are using this option with REPAIR TABLE, it will try to repair only the index tree. This is the fastest repair method for a table. |\
\| -r, --repair | Can fix almost anything except unique keys that aren't unique. |\
\| --shared-memory-base-name | Shared-memory name to use for Windows connections using shared memory to a local server (started with the --shared-memory option). Case-sensitive. |\
\| -s, --silent | Print only error messages. |\
\| --skip-database | Don't process the database (case-sensitive) specified as argument. |\
\| -S name, --socket=name | For connections to localhost, the Unix socket file to use, or, on Windows, the name of the named pipe to use. |\
\| --ssl | Enables [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). TLS is also enabled even without setting this option when certain other TLS options are set. Starting with [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102), the --ssl option will not enable [verifying the server certificate](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification) by default. In order to verify the server certificate, the user must specify the --ssl-verify-server-cert option. |\
\| --ssl-ca=name | Defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Authorities (CAs)](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information. This option implies the --ssl option. |\
\| --ssl-capath=name | Defines a path to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Authorities (CAs)](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information. This option is only supported if the client was built with OpenSSL or yaSSL. If the client was built with GnuTLS or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms. This option implies the --ssl option. |\
\| --ssl-cert=name | Defines a path to the X509 certificate file to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. This option implies the --ssl option. |\
\| --ssl-cipher=name | List of permitted ciphers or cipher suites to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option implies the --ssl option. |\
\| --ssl-crl=name | Defines a path to a PEM file that should contain one or more revoked X509 certificates to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information. This option is only supported if the client was built with OpenSSL or Schannel. If the client was built with yaSSL or GnuTLS, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms. |\
\| --ssl-crlpath=name | Defines a path to a directory that contains one or more PEM files that should each contain one revoked X509 certificate to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information. This option is only supported if the client was built with OpenSSL. If the client was built with yaSSL, GnuTLS, or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms. |\
\| --ssl-key=name | Defines a path to a private key file to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. This option implies the --ssl option. |\
\| --ssl-verify-server-cert | Enables [server certificate verification](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification). This option is disabled by default. |\
\| --tables | Overrides the --databases or -B option such that all name arguments following the option are regarded as table names. |\
\| --use-frm | For repair operations on MyISAM tables, get table structure from .frm file, so the table can be repaired even if the .MYI header is corrupted. |\
\| -u, --user=name | User for login if not current user. |\
\| -v, --verbose | Print info about the various stages. You can give this option several times to get even more information. See [mariadb-check and verbose](mariadb-check.md#mariadb-check-and-verbose), below. |\
\| -V, --version | Output version information and exit. |\
\| --write-binlog | Write ANALYZE, OPTIMIZE and REPAIR TABLE commands to the [binary log](../../server-management/server-monitoring-logs/binary-log/). Enabled by default; use --skip-write-binlog when commands should not be sent to replication slaves. |

#### Option Files

In addition to reading options from the command-line, `mariadb-check` can also read options from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). If an unknown option is provided to `mariadb-check` in an option file, then it is ignored.

The following options relate to how MariaDB command-line tools handles option files. They must be given as the first argument on the command-line:

| Option                    | Description                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------- |
| Option                    | Description                                                                         |
| --print-defaults          | Print the program argument list and exit.                                           |
| --no-defaults             | Don't read default options from any option file.                                    |
| --defaults-file=#         | Only read default options from the given file #.                                    |
| --defaults-extra-file=#   | Read this file after the global files are read.                                     |
| --defaults-group-suffix=# | In addition to the default option groups, also read option groups with this suffix. |

`mariadb-check` is linked with [MariaDB Connector/C](../../../kb/en/about-mariadb-connector-c/). However, MariaDB Connector/C does not yet handle the parsing of option files for this client. That is still performed by the server option file parsing code. See [MDEV-19035](https://jira.mariadb.org/browse/MDEV-19035) for more information.

**Option Groups**

`mariadb-check` reads options from the following [option groups](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group             | Description                                                                                                                                                                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Group             | Description                                                                                                                                                                                                                               |
| \[mysqlcheck]     | Options read by mysqlcheck, which includes both MariaDB Server and MySQL Server.                                                                                                                                                          |
| \[mariadb-check]  | Options read by mariadb-check. Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes). |
| \[client]         | Options read by all MariaDB and MySQL [client programs](../../../kb/en/clients-utilities/), which includes both MariaDB and MySQL clients. For example, mysqldump.                                                                        |
| \[client-server]  | Options read by all MariaDB [client programs](../../../kb/en/clients-utilities/) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients.                             |
| \[client-mariadb] | Options read by all MariaDB [client programs](../../../kb/en/clients-utilities/).                                                                                                                                                         |

### Notes

#### Default Values

To see the default values for the options and also to see the arguments you get\
from configuration files you can do:

```
./client/mariadb-check --print-defaults
./client/mariadb-check --help
```

#### mariadb-check and auto-repair

When running `mariadb-check` with `--auto-repair` (as done by[mariadb-upgrade](../deployment-tools/mariadb-upgrade.md)), `mariadb-check` will first\
check all tables and then in a separate phase repair those that failed the\
check.

#### mariadb-check and all-databases

`mariadb-check --all-databases` will ignore the internal log tables [general\_log](../../reference/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysqlgeneral_log-table.md) and [slow\_log](../../reference/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-slow_log-table.md) as these can't be checked, repaired or optimized.

#### mariadb-check and verbose

Using one `--verbose` option will give you more information about what mariadb-check is doing.

Using two `--verbose` options will also give you connection information.

If you use three `--verbose` options you will also get, on stdout, all [ALTER](../../reference/sql-statements/data-definition/alter/alter-table.md), [RENAME](../../reference/sql-statements/data-definition/rename-table.md), and [CHECK](../../reference/sql-statements/table-statements/check-table.md) commands that mariadb-check executes.

CC BY-SA / Gnu FDL
