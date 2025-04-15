
# mariadb-install-db.exe

The `<code>mariadb-install-db.exe</code>` utility is the Windows equivalent of [mariadb-install-db](mariadb-install-db-exe.md).


## Functionality


The functionality of `<code>mariadb-install-db.exe</code>` is comparable with the shell
script `<code>mariadb-install-db</code>` used on Unix, however it has been extended with
both Windows specific functionality (creating a Windows service) and to
generally useful functionality. For example, it can set the 'root' user
password during database creation. It also creates the `<code>my.ini</code>` configuration
file in the data directory and adds most important parameters to it (e.g port).


`<code>mariadb-install-db.exe</code>` is used by the MariaDB installer for Windows if the
"Database instance" feature is selected. It obsoletes similar utilities and
scripts that were used in the past such as `<code>mysqld.exe</code>` `<code><code>--</code>install</code>`,
`<code>mysql_install_db.pl</code>`, and `<code>mysql_secure_installation.pl</code>`.



| Parameter | Description |
| --- | --- |
| Parameter | Description |
| -?, --help | Display help message and exit |
| -d, --datadir=name | Data directory of the new database |
| -S, --service=name | Name of the Windows service |
| -p, --password=name | Password of the root user |
| -P, --port=# | mysqld port |
| -W, --socket=name | named pipe name |
| -D, --default-user | Create default user |
| -R, --allow-remote-root-access | Allow remote access from network for user root |
| -N, --skip-networking | Do not use TCP connections, use pipe instead |
| -i, --innodb-page-size | Innodb page size, since [MariaDB 10.2.5](../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1025-release-notes.md) |
| -s,--silent | Print less information |
| -o,--verbose-bootstrap | Include mysqld bootstrap output |
| -l,--large-pages | Use large pages, since [MariaDB 10.6.1](../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md) |
| -c,--config | my.ini config template file, since [MariaDB 10.6.1](../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md) |



**Note**: to create a Windows service, `<code>mariadb-install-db.exe</code>` should be run
by a user with full administrator privileges (which means elevated command
prompt on systems with UAC).


## Example


```
mariadb-install-db.exe --datadir=C:\db --service=MyDB --password=secret
```

will create the database in the directory C:\db, register the auto-start
Windows service "MyDB", and set the root password to 'secret'.


To start the service from the command line, execute


```
sc start MyDB
```

## Removing Database Instances


If you run your database instance as service, to remove it completely from the
command line, use


```
sc stop <servicename>
sc delete <servicename>
rmdir /s /q <path-to-datadir>
```
