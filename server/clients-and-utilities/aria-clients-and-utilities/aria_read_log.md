
# aria_read_log

**aria_read_log** is a tool for displaying and applying log records from an [Aria](../../reference/storage-engines/aria/README.md) [transaction log](../../reference/storage-engines/aria/aria-storage-engine.md#aria-log-files).


Note: Aria is compiled without -DIDENTICAL_PAGES_AFTER_RECOVERY
which means that the table files are not byte-to-byte identical to
files created during normal execution. This should be ok, except for
test scripts that try to compare files before and after recovery.


Usage:


```
aria_read_log OPTIONS
```

You need to use one of `-d` or `-a`.


## Options


The following variables can be set while passed as commandline options to aria_read_log, or set in the `[aria_read_log]` section in your [my.cnf](../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) file.



| Option | Description |
| --- | --- |
| Option | Description |
| -a, --apply | Apply log to tables: modifies tables! you should make a backup first! Displays a lot of information if not run with --silent. |
| --character-sets-dir=name | Directory where character sets are. |
| -c, --check | if --display-only, check if record is fully readable (for debugging). |
| -?, --help | Display help and exit. |
| -d, --display-only | Display brief info read from records' header. |
| -e, --end-lsn=# | Stop applying at this lsn. If end-lsn is used, UNDO:s will not be applied |
| -h, --aria-log-dir-path=name | Path to the directory where to store transactional log |
| -P, --page-buffer-size=# | The size of the buffer used for index blocks for Aria tables. |
| -l, --print-log-control-file | Print the content of the aria_log_control_file. From [MariaDB 10.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1041-release-notes). |
| -o, --start-from-lsn=# | Start reading log from this lsn. |
| -C, --start-from-checkpoint | Start applying from last checkpoint. |
| -s, --silent | Print less information during apply/undo phase. |
| -T, --tables-to-redo=name | List of comma-separated tables that we should apply REDO on. Use this if you only want to recover some tables. |
| -t, --tmpdir=name | Path for temporary files. Multiple paths can be specified, separated by colon (:) |
| --translog-buffer-size=# | The size of the buffer used for transaction log for Aria tables. |
| -u, --undo | Apply UNDO records to tables. (disable with --disable-undo) (Defaults to on; use --skip-undo to disable.) |
| -v, --verbose | Print more information during apply/undo phase. |
| -V, --version | Print version and exit. |




CC BY-SA / Gnu FDL

