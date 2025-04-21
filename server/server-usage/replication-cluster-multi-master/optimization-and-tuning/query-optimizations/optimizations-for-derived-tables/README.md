
# Optimizations for Derived Tables

Derived tables are subqueries in the `FROM` clause. Prior to [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)/MySQL 5.6, they were too slow to be usable. In [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)/MySQL 5.6, there are two
optimizations which provide adequate performance:

