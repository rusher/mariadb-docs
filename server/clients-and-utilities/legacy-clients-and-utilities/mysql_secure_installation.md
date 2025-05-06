
# mysql_secure_installation

Note that many of the reasons for the existence of this script no longer apply. In particular, from [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104), [Unix socket authentication](../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) is applied by default, and there is usually no need to create a root password. See [Authentication from MariaDB 10.4](../../security/user-account-management/authentication-from-mariadb-10-4.md).


From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105), the client is called `mariadb-secure-installation`. It can still be accessed under its original `mysql_secure_installation` name via a symlink in Linux, or an alternate binary in Windows.


See [mariadb-secure-installation](../mariadb-secure-installation.md) for details.


CC BY-SA / Gnu FDL

