# aria\_pack

aria\_pack is a tool for compressing [Aria](../../server-usage/storage-engines/aria/) tables. The resulting table are read-only, and usually about 40% to 70% smaller.

aria\_pack is run as follows

```
aria_pack [options] file_name [file_name2...]
```

The file name is the .MAI index file. The extension can be omitted, although keeping it permits wildcards, such as

```
aria_pack *.MAI
```

to compress all the files.

aria\_pack compresses each column separately, and, when the resulting data is read, only the individual rows and columns required need to be decompressed, allowing for quicker reading.

Once a table has been packed, use [aria\_chk -rq](aria_chk.md) (the quick and recover options) to rebuild its indexes.

## Options

The following variables can be set while passed as commandline options to aria\_pack, or set in the \[ariapack] section in your [my.cnf](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) file.

| Option                    | Description                                                                                                                                                                                               |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -b, --backup              | Make a backup of the table as table\_name.OLD.                                                                                                                                                            |
| --character-sets-dir=name | Directory where character sets are.                                                                                                                                                                       |
| -h, --datadir             | Path for control file (and logs if --logdir not used). From [MariaDB 10.5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1053-release-notes) |
| -#, --debug\[=name]       | Output debug log. Often this is 'd:t:o,filename'.                                                                                                                                                         |
| -?, --help                | Display help and exit.                                                                                                                                                                                    |
| -f, --force               | Force packing of table even if it gets bigger or if tempfile exists.                                                                                                                                      |
| --ignore-control-file     | Ignore the control file. From [MariaDB 10.5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1053-release-notes).                              |
| -j, --join=name           | Join all given tables into 'new\_table\_name'. All tables MUST have identical layouts.                                                                                                                    |
| --require-control-file    | Abort if cannot find control file. From [MariaDB 10.5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1053-release-notes).                    |
| -s, --silent              | Only write output when an error occurs.                                                                                                                                                                   |
| -t, --test                | Don't pack table, only test packing it.                                                                                                                                                                   |
| -T, --tmpdir=name         | Use temporary directory to store temporary table.                                                                                                                                                         |
| -v, --verbose             | Write info about progress and packing result. Use many -v for more verbosity!                                                                                                                             |
| -V, --version             | Output version information and exit.                                                                                                                                                                      |
| -w, --wait                | Wait and retry if table is in use.                                                                                                                                                                        |

## Unpacking

To unpack a table compressed with aria\_pack, use the [aria\_chk -u](aria_chk.md) option.

## Example

```
> aria_pack /my/data/test/posts
Compressing /my/data/test/posts.MAD: (1690 records)
- Calculating statistics
- Compressing file
37.71%     
> aria_chk -rq --ignore-control-file /my/data/test/posts
- check record delete-chain
- recovering (with keycache) Aria-table '/my/data/test/posts'
Data records: 1690
State updated
```

## See Also

* [FLUSH TABLES FOR EXPORT](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)
* [myisamchk](../myisam-clients-and-utilities/myisamchk.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
