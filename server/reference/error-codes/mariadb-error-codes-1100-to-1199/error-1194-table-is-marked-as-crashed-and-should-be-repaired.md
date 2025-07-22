# Error 1194: Table is marked as crashed and should be repaired

| Error Code | SQLSTATE | Error                  | Description                                            |
| ---------- | -------- | ---------------------- | ------------------------------------------------------ |
| 1194       | HY000    | ER\_CRASHED\_ON\_USAGE | Table '%s' is marked as crashed and should be repaired |

## Possible Causes and Solutions

This error occurs, in particular to [MyISAM](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/storage-engines/myisam-storage-engine/README.md), [Aria](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/storage-engines/aria/README.md), [Archive](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/storage-engines/archive/README.md) or [CSV](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/storage-engines/csv/README.md) tables, if the table is marked as crashed. This can occur for a number of reasons, for example:

* running out of disk space
* sudden shutdown while the table was in use

Fixing the problem can usually be done by running a [REPAIR TABLE](../../sql-statements/table-statements/repair-table.md) statement, or one of the similar scripts, [aria\_chk](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/clients-and-utilities/aria-clients-and-utilities/aria_chk.md), [myisamchk](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/clients-and-utilities/myisam-clients-and-utilities/myisamchk.md) or [mariadb-check](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/clients-and-utilities/mariadb-check.md).

{% include "../../../.gitbook/includes/license-cc-by-sa-gnu-fdl.md" %}

<!-- This page is licensed: CC BY-SA / Gnu FDL -->

{% @marketo/form formId="4316" %}
