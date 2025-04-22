
# mariadb-tzinfo-to-sql

`mariadb-tzinfo-to-sql` is a utility used to load [time zones](../reference/data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) on systems that have a zoneinfo database to load the time zone tables ([time_zone](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-time_zone-table.md), [time_zone_leap_second](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-time_zone_leap_second-table.md), [time_zone_name](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-time_zone_name-table.md), [time_zone_transition](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-time_zone_transition-table.md) and [time_zone_transition_type](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-time_zone_transition_type-table.md)) into the mysql database.


Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105), the client was called `mysql_tzinfo_to_sql`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.


Most Linux, Mac OS X, FreeBSD and Solaris systems will have a zoneinfo database - Windows does not. The database is commonly found in the /usr/share/zoneinfo directory, or, on Solaris, the /usr/share/lib/zoneinfo directory.


## Usage


`mariadb-tzinfo-to-sql` can be called in several ways. The output is usually passed straight to the [mariadb client](mariadb-client/README.md) for direct loading in the mysql database.


```
shell> mariadb-tzinfo-to-sql timezone_dir
shell> mariadb-tzinfo-to-sql timezone_file timezone_name
shell> mariadb-tzinfo-to-sql --leap timezone_file
```

## Resetting timezone tables


If there is a need to reset the timezone to the default, to before using `mariadb-tzinfo-to-sql`, one can do that by executing:


```
truncate table mysql.time_zone;
truncate table mysql.time_zone_name;
truncate table mysql.time_zone_transition;
truncate table mysql.time_zone_transition_type;
truncate table mysql.time_zone_leap_second;
```

The old timezone values will be in effect until the server is [restarted](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/shutdown.md).


## Examples


Most commonly, the whole directory is passed:


```
shell>mariadb-tzinfo-to-sql /usr/share/zoneinfo | mariadb -u root mysql
```

Load a single time zone file, `timezone_file`, corresponding to the time zone called `timezone_name`.


```
shell> mariadb-tzinfo-to-sql timezone_file timezone_name | mariadb -u root mysql
```

A separate command for each time zone and time zone file the server needs is required.


To account for leap seconds, use:


```
shell> mariadb-tzinfo-to-sql --leap timezone_file | mariadb -u root mysql
```

After populating the time zone tables, you should usually restart the server so that the new time zone data is correctly loaded.

