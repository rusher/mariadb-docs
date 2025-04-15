# mariadb-tzinfo-to-sql

`mariadb-tzinfo-to-sql` is a utility used to load [time zones](../reference/data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) on systems that have a zoneinfo database to load the time zone tables ([time_zone](/kb/en/mysqltime_zone-table/), [time_zone_leap_second](/kb/en/mysqltime_zone_leap_second-table/), [time_zone_name](/kb/en/mysqltime_zone_name-table/), [time_zone_transition](/kb/en/mysqltime_zone_transition-table/) and [time_zone_transition_type](/kb/en/mysqltime_zone_transition_type-table/)) into the mysql database.

Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-105), the client was called `mysql_tzinfo_to_sql`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

Most Linux, Mac OS X, FreeBSD and Solaris systems will have a zoneinfo database - Windows does not. The database is commonly found in the /usr/share/zoneinfo directory, or, on Solaris, the /usr/share/lib/zoneinfo directory.

#

# Usage

`mariadb-tzinfo-to-sql` can be called in several ways. The output is usually passed straight to the [mariadb client](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/c/mariadb-client-library-for-c-200-release-notes) for direct loading in the mysql database.

```
shell> mariadb-tzinfo-to-sql timezone_dir
shell> mariadb-tzinfo-to-sql timezone_file timezone_name
shell> mariadb-tzinfo-to-sql --leap timezone_file
```

#

# Resetting timezone tables

If there is a need to reset the timezone to the default, to before using `mariadb-tzinfo-to-sql`, one can do that by executing:

```
truncate table mysql.time_zone;
truncate table mysql.time_zone_name;
truncate table mysql.time_zone_transition;
truncate table mysql.time_zone_transition_type;
truncate table mysql.time_zone_leap_second;
```

The old timezone values will be in effect until the server is [restarted](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/shutdown.md).

#

# Examples

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