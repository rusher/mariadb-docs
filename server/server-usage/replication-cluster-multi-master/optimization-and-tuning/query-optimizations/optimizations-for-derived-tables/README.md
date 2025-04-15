
# Optimizations for Derived Tables

Derived tables are subqueries in the `<code>FROM</code>` clause. Prior to [MariaDB 5.3](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md)/MySQL 5.6, they were too slow to be usable. In [MariaDB 5.3](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md)/MySQL 5.6, there are two
optimizations which provide adequate performance:

