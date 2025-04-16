
# Differences in MariaDB in Debian (and Ubuntu)


The `[.deb](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md)` packages provided by MariaDB Foundation's and MariaDB Corporation's repositories are not identical to the official `[.deb](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md)` packages provided by Debian's and Ubuntu's default repositories.


The packages provided by MariaDB Foundation's and MariaDB Corporation's repositories are generated using the Debian packaging in MariaDB's official [source code](../../../../clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md). The Debian packaging scripts are specifically in the `debian/` directory.


The packages provided by Debian's and Ubuntu's default repositories are generated using the Debian packaging in Debian's mirror of MariaDB's source code, which contains some custom changes. The source tree can be found here:


* [mariadb-server](https://salsa.debian.org/mariadb-team/mariadb-server)


As a consequence, MariaDB behaves a bit differently if it is installed from Debian's and Ubuntu's default repositories.


## Option File Locations


* The [option file](../../configuring-mariadb-with-option-files.md) located at `/etc/mysql/my.cnf` is handled by the `[update-alternatives](https://manpages.ubuntu.com/manpages/trusty/en/man8/update-alternatives.8.html)` mechanism when the `mysql-common` package is installed. It is a symbolic link that references either `mysql.cnf` or `mariadb.cnf` depending on whether MySQL or MariaDB is installed. Most of the MariaDB [option files](../../configuring-mariadb-with-option-files.md) are therefore actually located in `/etc/mysql/mariadb.d/`.


## System Variables


Since [MariaDB 11.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-116.md) there is no system variable difference from the Standard MariaDB.



| Variable | MariaDB in Debian | Standard MariaDB | Notes |
| --- | --- | --- | --- |
| Variable | MariaDB in Debian | Standard MariaDB | Notes |
| [character_set_server](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_server) | utf8mb4 | latin1 (for <= [MariaDB 11.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md)) | [MariaDB 11.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-116.md) also defaults to utf8mb4 hence no difference for this version and greater |
| [collation_server](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_server) | utf8mb4_general_ci (for < [MariaDB 11.5.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-2-release-notes.md)) | latin1_swedish_ci | [character_set_collations](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_collations) has dominant effect hence removal from Debian default settings |



## Options



| Option | MariaDB in Debian | Standard MariaDB | Notes |
| --- | --- | --- | --- |
| Option | MariaDB in Debian | Standard MariaDB | Notes |
| [plugin-load-add](../../starting-and-stopping-mariadb/mariadbd-options.md) | auth_socket.so | - | Before [MariaDB 10.4.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md), MariaDB did not enable the [unix_socket](../../../../ref/plugins/authentication-plugins/authentication-plugin-unix-socket.md) authentication plugin by default.This is default in Debian, allowing passwordless login. |



## TLS


* MariaDB binaries from `[.deb](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md)` packages provided by Debian's and Ubuntu's default repositories are linked with a different TLS library than MariaDB binaries from `[.deb](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md)` packages provided by MariaDB Foundation's and MariaDB Corporation's repositories.


* MariaDB Server binaries:

  * In [MariaDB 10.4.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1046-release-notes.md) and later, MariaDB Server is statically linked with the bundled [wolfSSL](https://www.wolfssl.com/products/wolfssl/) libraries in `[.deb](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md)` packages provided by Debian's and Ubuntu's default repositories.
  * In [MariaDB 10.4.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1045-release-notes.md) and before, MariaDB Server is statically linked with the bundled [yaSSL](https://www.wolfssl.com/products/yassl/) libraries in `[.deb](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md)` packages provided by Debian's and Ubuntu's default repositories.
  * In contrast, MariaDB Server is dynamically linked with the system's [OpenSSL](https://www.openssl.org/) libraries in `[.deb](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md)` packages provided by MariaDB Foundation and MariaDB Corporation.


* MariaDB [client and utility](/kb/en/clients-utilities/) binaries:

  * In [MariaDB 10.4.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1046-release-notes.md) and later, MariaDB's [clients and utilities](/kb/en/clients-utilities/) and [MariaDB Connector/C](../../../../../connectors/mariadb-connector-cpp/mariadb-connector-cpp-sample-application.md) are dynamically linked with the system's [GnuTLS](https://www.gnutls.org/) libraries in `[.deb](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md)` packages provided by Debian's and Ubuntu's default repositories. [libmysqlclient](https://dev.mysql.com/doc/refman/5.5/en/c-api.html) is still statically linked with the bundled [wolfSSL](https://www.wolfssl.com/products/wolfssl/) libraries.
  * In [MariaDB 10.2](../../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md) and later, MariaDB's [clients and utilities](/kb/en/clients-utilities/) and [MariaDB Connector/C](../../../../../connectors/mariadb-connector-cpp/mariadb-connector-cpp-sample-application.md) are dynamically linked with the system's [GnuTLS](https://www.gnutls.org/) libraries in `[.deb](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md)` packages provided by Debian's and Ubuntu's default repositories. [libmysqlclient](https://dev.mysql.com/doc/refman/5.5/en/c-api.html) is still statically linked with the bundled [yaSSL](https://www.wolfssl.com/products/yassl/) libraries.
  * In [MariaDB 10.1](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md) and earlier, MariaDB's [clients and utilities](/kb/en/clients-utilities/) and [libmysqlclient](https://dev.mysql.com/doc/refman/5.5/en/c-api.html) are statically linked with the bundled [yaSSL](https://www.wolfssl.com/products/yassl/) libraries in `[.deb](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md)` packages provided by Debian's and Ubuntu's default repositories.
  * In contrast, MariaDB's [clients and utilities](/kb/en/clients-utilities/), [libmysqlclient](https://dev.mysql.com/doc/refman/5.5/en/c-api.html), and [MariaDB Connector/C](../../../../../connectors/mariadb-connector-cpp/mariadb-connector-cpp-sample-application.md) are dynamically linked with the system's [OpenSSL](https://www.openssl.org/) libraries in `[.deb](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md)` packages provided by MariaDB Foundation's and MariaDB Corporation's repositories.


* See [TLS and Cryptography Libraries Used by MariaDB](../../../../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.


## Authentication


* The `[unix_socket](../../../../ref/plugins/authentication-plugins/authentication-plugin-unix-socket.md)` authentication plugin is installed by default in new installations that use the `[.deb](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md)` packages provided by Debian's default repositories in Debian 9 and later and Ubuntu's default repositories in Ubuntu 15.10 and later.


* The `root@localhost` created by [mariadb-install-db](../../mariadb-install-db-exe.md) will also be created to authenticate via the [unix_socket](../../../../ref/plugins/authentication-plugins/authentication-plugin-unix-socket.md) authentication plugin in these builds.


## See Also


* [Moving from MySQL to MariaDB in Debian 9](moving-from-mysql-to-mariadb-in-debian-9.md)


## More Information


For details, check out the Debian and Ubuntu official repositories:


* [search?keywords=mariadb-server&searchon=names&suite=all§ion=all](https://packages.debian.org/search?keywords=mariadb-server&searchon=names&suite=all§ion=all)
* [search?keywords=mariadb-server&searchon=names&suite=all§ion=all](https://packages.ubuntu.com/search?keywords=mariadb-server&searchon=names&suite=all§ion=all)

