
# mariadb-fix-extensions

`<code>mariadb-fix-extensions</code>` converts the extensions for [MyISAM](../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md) (or ISAM) table files to their canonical forms.


Prior to [MariaDB 10.5](../../release-notes/mariadb-community-server/what-is-mariadb-105.md), the client was called `<code>mysql_fix_extensions</code>`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.


It looks for files with extensions matching any lettercase variant of `<code>.frm</code>`, `<code>.myd</code>`, `<code>.myi</code>`, `<code>.isd</code>`, and `<code>.ism</code>` and renames them to have extensions of `<code>.frm</code>`, `<code>.MYD</code>`, `<code>.MYI</code>`, `<code>.ISD</code>`, and `<code>.ISM</code>`, respectively. This can be useful after transferring the files from a system with case-insensitive file names (such as Windows) to a system with case-sensitive file names.


Invoke mariadb-fix-extensions as follows, where data_dir is the path name to the MariaDB data directory.


```
mariadb-fix-extensions data_dir
```
