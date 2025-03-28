# What is the Goal of MariaDB?

To provide a [community](/en/community/) developed, stable, and [always Free](../licensing-questions/mariadb-licenses.md) DBMS that is, on the user level, broadly compatible with MySQL.

We strive for interoperability with both our own, and our upstream, communities.

Until [MariaDB 5.5](/en/what-is-mariadb-55/), MariaDB was kept up to date with the latest MySQL release from the same branch.
For example [MariaDB 5.1.47](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-51-series/mariadb-5147-release-notes) was up to date with MySQL 5.1.47, and so on.

We did a merge from the main MySQL branch for every new MySQL release or when
there was some critical bugfix applied to the main branch.

Since [MariaDB 10.0](/en/what-is-mariadb-100/), MariaDB includes backported features from MySQL as well as entirely new features not found anywhere else, but does not necessarily include all MySQL features.

We strive to keep our main trees as free from bugs as possible. It should be
reasonably safe to pull from our trees at any time.