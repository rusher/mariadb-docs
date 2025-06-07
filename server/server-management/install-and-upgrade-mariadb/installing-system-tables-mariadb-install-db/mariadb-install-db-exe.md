# Installing System Tables on Windows

The `mariadb-install-db.exe` utility is the Windows equivalent of [mariadb-install-db](../../../clients-and-utilities/mariadb-install-db.md).

## Functionality

The functionality of `mariadb-install-db.exe` is comparable with the shell\
script `mariadb-install-db` used on Unix, however it has been extended with\
both Windows specific functionality (creating a Windows service) and to\
generally useful functionality. For example, it can set the 'root' user\
password during database creation. It also creates the `my.ini` configuration\
file in the data directory and adds most important parameters to it (e.g port).

`mariadb-install-db.exe` is used by the MariaDB installer for Windows if the\
"Database instance" feature is selected. It obsoletes similar utilities and\
scripts that were used in the past such as `mysqld.exe` `--install`,`mysql_install_db.pl`, and `mysql_secure_installation.pl`.

| Parameter                      | Description                                                                                                                                                                                               |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Parameter                      | Description                                                                                                                                                                                               |
| -?, --help                     | Display help message and exit                                                                                                                                                                             |
| -d, --datadir=name             | Data directory of the new database                                                                                                                                                                        |
| -S, --service=name             | Name of the Windows service                                                                                                                                                                               |
| -p, --password=name            | Password of the root user                                                                                                                                                                                 |
| -P, --port=#                   | mysqld port                                                                                                                                                                                               |
| -W, --socket=name              | named pipe name                                                                                                                                                                                           |
| -D, --default-user             | Create default user                                                                                                                                                                                       |
| -R, --allow-remote-root-access | Allow remote access from network for user root                                                                                                                                                            |
| -N, --skip-networking          | Do not use TCP connections, use pipe instead                                                                                                                                                              |
| -i, --innodb-page-size         | Innodb page size, since [MariaDB 10.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1025-release-notes) |
| -s,--silent                    | Print less information                                                                                                                                                                                    |
| -o,--verbose-bootstrap         | Include mysqld bootstrap output                                                                                                                                                                           |
| -l,--large-pages               | Use large pages, since [MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1061-release-notes)                             |
| -c,--config                    | my.ini config template file, since [MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1061-release-notes)                 |

**Note**: to create a Windows service, `mariadb-install-db.exe` should be run\
by a user with full administrator privileges (which means elevated command\
prompt on systems with UAC).

## Example

```
mariadb-install-db.exe --datadir=C:\db --service=MyDB --password=secret
```

will create the database in the directory C:\db, register the auto-start\
Windows service "MyDB", and set the root password to 'secret'.

To start the service from the command line, execute

```
sc start MyDB
```

## Removing Database Instances

If you run your database instance as service, to remove it completely from the\
command line, use

```
sc stop <servicename>
sc delete <servicename>
rmdir /s /q <path-to-datadir>
```

CC BY-SA / Gnu FDL
