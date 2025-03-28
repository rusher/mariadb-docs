# Optimizations for Derived Tables

Derived tables are subqueries in the `FROM` clause. Prior to [MariaDB 5.3](/en/what-is-mariadb-53/)/MySQL 5.6, they were too slow to be usable. In [MariaDB 5.3](/en/what-is-mariadb-53/)/MySQL 5.6, there are two
optimizations which provide adequate performance: