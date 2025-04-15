
# mariadb-find-rows

`<code>mariadb-find-rows</code>` reads files containing SQL statements and extracts statements that match a given regular expression or that contain [USE db_name](../../general-resources/learning-and-training/training-and-tutorials/beginner-mariadb-articles/useful-mariadb-queries.md) or [SET](../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md) statements.


Prior to [MariaDB 10.5](../../release-notes/mariadb-community-server/what-is-mariadb-105.md), the client was called `<code>mysql_find_rows</code>`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.


The utility was written for use with update log files (as used prior to MySQL 5.0) and as such expects statements to be terminated with semicolon (;) characters. It may be useful with other files that contain SQL statements as long as statements are terminated with semicolons.


## Usage


```
mariadb-find-rows [options] [file_name ...]
```

Each file_name argument should be the name of file containing SQL statements. If no file names are given, *mariadb-find-rows* reads the standard input.


## Options


mariadb-find-rows supports the following options:



| Option | Description |
| --- | --- |
| Option | Description |
| --help, --Information | Display help and exit. |
| --regexp=pattern | Display queries that match the pattern. |
| --rows=N | Quit after displaying N queries. |
| --skip-use-db | Do not include [USE db_name](../../general-resources/learning-and-training/training-and-tutorials/beginner-mariadb-articles/useful-mariadb-queries.md) statements in the output. |
| --start_row=N | Start output from this row (first row is 1). |



## Examples


```
mariadb-find-rows --regexp=problem_table --rows=20 < update.log
mariadb-find-rows --regexp=problem_table  update-log.1 update-log.2
```
