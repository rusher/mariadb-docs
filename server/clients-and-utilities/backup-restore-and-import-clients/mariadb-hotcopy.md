# mariadb-hotcopy

`mariadb-hotcopy` is a Perl script that was originally written and contributed by Tim Bunce. It uses [FLUSH TABLES](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md), [LOCK TABLES](../../reference/sql-statements/transactions/lock-tables.md), and cp or scp to make a database backup.

Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105), the client was called `mysqlhotcopy`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

It is a fast way to make a backup of the database or single tables, but it can be run only on the same machine where the database\
directories are located. `mariadb-hotcopy`> works only for backing up [MyISAM](../../reference/storage-engines/myisam-storage-engine/) and [ARCHIVE](../../reference/storage-engines/archive/) tables. It runs on Unix and NetWare.

To use `mariadb-hotcopy`, you must have read access to the files\
for the tables that you are backing up, the SELECT [privilege](../../reference/sql-statements/account-management-sql-statements/grant.md) for\
those tables, the RELOAD privilege (to be able to execute FLUSH TABLES), and\
the LOCK TABLES privilege (to be able to lock the tables).

```
shell> mariadb-hotcopy db_name [/path/to/new_directory]
shell> mariadb-hotcopy db_name_1 ... db_name_n /path/to/new_directory
```

Back up tables in the given database that match a regular expression:

```
shell> mariadb-hotcopy db_name./regex/
```

The regular expression for the table name can be negated by prefixing it with a\
tilde (“`~`”):

```
shell> mariadb-hotcopy db_name./~regex/
```

`mariadb-hotcopy` supports the following options, which can be\
specified on the command line or in the \[`mariadb-hotcopy`] and\
\[`client`] option file groups.

| Option                                | Description                                                                                                                                                                                                                                                                                     |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Option                                | Description                                                                                                                                                                                                                                                                                     |
| --help, -?                            | Display a help message and exit.                                                                                                                                                                                                                                                                |
| --addtodest                           | Do not rename target directory (if it exists); merely add files to it.                                                                                                                                                                                                                          |
| --allowold                            | Do not abort if a target exists; rename it by adding an \_old suffix.                                                                                                                                                                                                                           |
| --checkpoint=db\_name.tbl\_name       | Insert checkpoint entries into the specified database db\_name and table tbl\_name.                                                                                                                                                                                                             |
| --chroot=path                         | Base directory of the chroot jail in which mariadbd operates. The path value should match that of the --chroot option given to mariadbd.                                                                                                                                                        |
| --debug                               | Enable debug output.                                                                                                                                                                                                                                                                            |
| --dryrun, -n                          | Report actions without performing them.                                                                                                                                                                                                                                                         |
| --flushlog                            | Flush logs after all tables are locked.                                                                                                                                                                                                                                                         |
| --host=host\_name, -h host\_name      | The host name of the local host to use for making a TCP/IP connection to the local server. By default, the connection is made to localhost using a Unix socket file.                                                                                                                            |
| --keepold                             | Do not delete previous (renamed) target when done.                                                                                                                                                                                                                                              |
| --method=command                      | The method for copying files (cp or scp). The default is cp.                                                                                                                                                                                                                                    |
| --noindices                           | Do not include full index files for MyISAM tables in the backup. This makes the backup smaller and faster. The indexes for reloaded tables can be reconstructed later with [myisamchk -rq](../myisam-clients-and-utilities/myisamchk.md).                                                       |
| --old-server                          | Connect to old MySQL-server (before v5.5) which doesn't have [FLUSH TABLES WITH READ LOCK](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) fully implemented.                                                                                             |
| --password=password, -ppassword       | The password to use when connecting to the server. The password value is not optional for this option, unlike for other MariaDB programs. Specifying a password on the command line should be considered insecure. You can use an option file to avoid giving the password on the command line. |
| --port=port\_num, -P port\_num        | The TCP/IP port number to use when connecting to the local server.                                                                                                                                                                                                                              |
| --quiet, -q                           | Be silent except for errors.                                                                                                                                                                                                                                                                    |
| --record\_log\_pos=db\_name.tbl\_name | Record master and slave status in the specified database db\_name and table tbl\_name.                                                                                                                                                                                                          |
| --regexp=expr                         | Copy all databases with names that match the given regular expression.                                                                                                                                                                                                                          |
| --resetmaster                         | Reset the binary log after locking all the tables.                                                                                                                                                                                                                                              |
| --resetslave                          | Reset the master.info file after locking all the tables.                                                                                                                                                                                                                                        |
| --socket=path, -S path                | The Unix socket file to use for connections to localhost.                                                                                                                                                                                                                                       |
| --suffix=str                          | The suffix to use for names of copied databases.                                                                                                                                                                                                                                                |
| --tmpdir=path                         | The temporary directory. The default is /tmp.                                                                                                                                                                                                                                                   |
| --user=username, -u username          | The MariaDB username to use when connecting to the server.                                                                                                                                                                                                                                      |

Use perldoc for additional `mariadb-hotcopy` documentation,\
including information about the structure of the tables needed for the`--checkpoint` and `--record_log_pos` options:

```
shell> perldoc mariadb-hotcopy
```

## See Also

* [mariadb-ldump](mariadb-ldump/)
* [Mariabackup](../../server-management/backing-up-and-restoring-databases/mariabackup/)

CC BY-SA / Gnu FDL
