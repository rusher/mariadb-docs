# mariadb-fix-extensions

`mariadb-fix-extensions` converts the extensions for [MyISAM](myisam-clients-and-utilities/myisamchk-table-information.md) (or ISAM) table files to their canonical forms.

Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-105), the client was called `mysql_fix_extensions`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

It looks for files with extensions matching any lettercase variant of `.frm`, `.myd`, `.myi`, `.isd`, and `.ism` and renames them to have extensions of `.frm`, `.MYD`, `.MYI`, `.ISD`, and `.ISM`, respectively. This can be useful after transferring the files from a system with case-insensitive file names (such as Windows) to a system with case-sensitive file names.

Invoke mariadb-fix-extensions as follows, where data_dir is the path name to the MariaDB data directory.

```
mariadb-fix-extensions data_dir
```