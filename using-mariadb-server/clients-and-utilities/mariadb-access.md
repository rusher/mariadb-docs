# mariadb-access

{% tabs %}
{% tab title="Current" %}
`mariadb-access` is a tool for checking access privileges, developed by Yves Carlier.

The client used to be called `mysqlaccess`, and can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.
{% endtab %}

{% tab title="MariaDB < 10.5" %}
The client is named `mysqlaccess`.
{% endtab %}
{% endtabs %}

It checks the access privileges for a host name, user name, and database combination. Note that mariadb-access checks access using only the [user](https://mariadb.com/kb/en/mysqluser-table/), [db](https://mariadb.com/kb/en/mysqldb-table/), and host tables. It does not check table, column, or routine privileges specified in the [tables\_priv](https://mariadb.com/kb/en/mysqltables_priv-table/), [columns\_priv](https://mariadb.com/kb/en/mysqlcolumns_priv-table/), or [procs\_priv](https://mariadb.com/kb/en/mysqlprocs_priv-table/) tables.

### Usage <a href="#usage" id="usage"></a>

{% tabs %}
{% tab title="Current" %}
```
mariadb-access [host [user [db]]] OPTIONS
```
{% endtab %}

{% tab title="MariaDB < 10.5" %}
```
mysqlaccess [host [user [db]]] OPTIONS
```
{% endtab %}
{% endtabs %}

If your MariaDB distribution is installed in some non-standard location, you must change the location where _mariadb-access_ expects to find the mariadb client. Edit the _mariadb-access_ script at approximately line 18. Search for a line that looks like this: <\<code> $MYSQL = ´/usr/local/bin/mariadb; # path to mariadb executable <\</code>> Change the path to reflect the location where _mariadb_ actually is stored on your system. If you do not do this, a _Broken pipe error_ will occur when you run _mariadb-access_.

### Options <a href="#options" id="options"></a>

| Option                                  | Description                                                                                                                                                                         |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-?`, `--help`                          | Displayhelp and exit.                                                                                                                                                               |
| `-v`, `--version`                       | Display version.                                                                                                                                                                    |
| `-u username`, `--user=username`        | Username for logging in to the db.                                                                                                                                                  |
| `-p[password]`, `--password[=password]` | Password to use for user. If omitted, `mariadb-access` prompts for one.                                                                                                             |
| `-h hostname`, `--host=hostname`        | Name or IP of the host.                                                                                                                                                             |
| `-d dbname`, `--db=dbname`              | Name of the database.                                                                                                                                                               |
| `-U username`, `--superuser=username`   | Connect as superuser.                                                                                                                                                               |
| `-P password`, `--spassword=password`   | Password for superuser.                                                                                                                                                             |
| `-H server`, `--rhost=server`           | Remote server to connect to.                                                                                                                                                        |
| `--old_server`                          | Connect to a very old MySQL servers (before version 3.21) that does not know how to handle full WHERE clauses.                                                                      |
| `-b`, `--brief`                         | Single-line tabular report.                                                                                                                                                         |
| `-t`, `--table`                         | Report in table-format.                                                                                                                                                             |
| `--relnotes`                            | Print release-notes.                                                                                                                                                                |
| `--plan`                                | Print suggestions/ideas for future releases.                                                                                                                                        |
| `--howto`                               | Some examples of how to run \`mariadb-access'.                                                                                                                                      |
| `--debug=N`                             | Enter debug level N (0..3).                                                                                                                                                         |
| `--copy`                                | Reload temporary grant-tables from original ones.                                                                                                                                   |
| `--preview`                             | Show differences in privileges after making changes in (temporary) grant-tables.                                                                                                    |
| `--commit`                              | Copy grant-rules from temporary tables to grant-tables (the grant tables must be flushed after, for example with [mariadb-admin reload](https://mariadb.com/kb/en/mariadb-admin/)). |
| `--rollback`                            | Undo the last changes to the grant-tables.                                                                                                                                          |

### Note <a href="#note" id="note"></a>

At least the user (`-u`) and the database (`-d`) must be given, even with wildcards. If no host is provided, \`localhost' is assumed. Wildcards (\*,?,%,\_) are allowed for _host_, _user_ and _db_, but be sure to escape them from your shell!! (ie type \\\* or '\*')
