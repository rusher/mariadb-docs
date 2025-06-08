# mariadb-find-rows

`mariadb-find-rows` reads files containing SQL statements and extracts statements that match a given regular expression or that contain [USE db\_name](../../reference/sql-statements/administrative-sql-statements/use-database.md) or [SET](../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statements.

Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), the client was called `mysql_find_rows`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

The utility was written for use with update log files (as used prior to MySQL 5.0) and as such expects statements to be terminated with semicolon (;) characters. It may be useful with other files that contain SQL statements as long as statements are terminated with semicolons.

## Usage

```
mariadb-find-rows [options] [file_name ...]
```

Each file\_name argument should be the name of file containing SQL statements. If no file names are given, _mariadb-find-rows_ reads the standard input.

## Options

mariadb-find-rows supports the following options:

| Option                | Description                                                                                                                           |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Option                | Description                                                                                                                           |
| --help, --Information | Display help and exit.                                                                                                                |
| --regexp=pattern      | Display queries that match the pattern.                                                                                               |
| --rows=N              | Quit after displaying N queries.                                                                                                      |
| --skip-use-db         | Do not include [USE db\_name](../../reference/sql-statements/administrative-sql-statements/use-database.md) statements in the output. |
| --start\_row=N        | Start output from this row (first row is 1).                                                                                          |

## Examples

```
mariadb-find-rows --regexp=problem_table --rows=20 < update.log
mariadb-find-rows --regexp=problem_table  update-log.1 update-log.2
```

CC BY-SA / Gnu FDL
