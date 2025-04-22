
# Spider

The Spider storage engine is a federated database solution that supports partitioning and [xa transactions](../../sql-statements-and-structure/sql-statements/transactions/xa-transactions.md), and allows tables of different MariaDB instances to be handled as if they were on the same instance.


### Versions of Spider in MariaDB


From [MariaDB 10.9.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-1092-release-notes), the Spider version number matches the server version.


| Spider Version | Introduced | Maturity |
| --- | --- | --- |
| Spider Version | Introduced | Maturity |
| Spider 3.3.15 | [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1057-release-notes), [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes) | Stable |
| Spider 3.3.15 | [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1054-release-notes) | Gamma |
| Spider 3.3.14 | [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes), [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes) | Stable |
| Spider 3.3.13 | [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes) | Stable |
| Spider 3.3.13 | [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes) | Gamma |
| Spider 3.2.37 | [MariaDB 10.1.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10110-release-notes), [MariaDB 10.0.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10023-release-notes) | Gamma |
| Spider 3.2.21 | [MariaDB 10.1.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-5-release-notes), [MariaDB 10.0.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10018-release-notes) | Gamma |
| Spider 3.2.18 | [MariaDB 10.0.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10017-release-notes) | Gamma |
| Spider 3.2.11 | [MariaDB 10.0.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10014-release-notes) | Gamma |
| Spider 3.2.4 | [MariaDB 10.0.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10012-release-notes) | Gamma |
| Spider 3.2 | [MariaDB 10.0.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10011-release-notes) | Gamma |
| Spider 3.0 | [MariaDB 10.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes) | Beta |




## Spider Documentation


See the [spider-2.0-doc](https://bazaar.launchpad.net/~kentokushiba/spiderformysql/spider-2.0-doc/files) repository for complete, older, documentation.


[Presentation for new sharding features in Spider 3.3](https://speakerdeck.com/kentoku/new-features-and-enhancements-of-spider-storage-engine-for-sharding).

