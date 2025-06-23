# Files Backed Up By mariadb-backup

## Files Backed Up By mariadb-backup

### Files Included in Backup

mariadb-backup backs up the files listed below.

#### InnoDB Data Files

mariadb-backup backs up the following InnoDB data files:

* [InnoDB system tablespace](../../storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md)
* [InnoDB file-per-table tablespaces](../../storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md)

#### MyRocks Data Files

{% tabs %}
{% tab title="Current" %}
This data data is located in the directory defined by the [rocksdb\_datadir](../../../reference/storage-engines/myrocks/myrocks-system-variables.md#rocksdb_datadir) system variable. mariadb-backup backs this data up by performing a checkpoint using the [rocksdb\_create\_checkpoint](../../../reference/storage-engines/myrocks/myrocks-system-variables.md#rocksdb_create_checkpoint) system variable.
{% endtab %}

{% tab title="< 10.3.8 / 10.2.16" %}
mariadb-backup will back up tables that use the [MyRocks](../../storage-engines/myrocks/) storage engine.&#x20;
{% endtab %}
{% endtabs %}



{% tabs %}
{% tab title="Current" %}
mariadb-backup will not back up tables that use the [MyRocks](../../storage-engines/myrocks/) storage engine. This data data is located in the directory defined by the [rocksdb\_datadir](../../../reference/storage-engines/myrocks/myrocks-system-variables.md#rocksdb_datadir) system variable. mariadb-backup backs this data up by performing a checkpoint using the [rocksdb\_create\_checkpoint](../../../reference/storage-engines/myrocks/myrocks-system-variables.md#rocksdb_create_checkpoint) system variable.
{% endtab %}

{% tab title="< 10.3.8 / 10.2.16" %}
mariadb-backup does not back up tables that use the [MyRocks](../../storage-engines/myrocks/) storage engine.
{% endtab %}
{% endtabs %}

mariadb-backup does not currently support [partial backups](partial-backup-and-restore-with-mariabackup.md) for MyRocks.

#### Other Data Files

mariadb-backup also backs up files with the following extensions:

* `frm`
* `isl`
* `MYD`
* `MYI`
* `MAD`
* `MAI`
* `MRG`
* `TRG`
* `TRN`
* `ARM`
* `ARZ`
* `CSM`
* `CSV`
* `opt`
* `par`

### Files Excluded From Backup

mariadb-backup does **not** back up the files listed below.

* [InnoDB Temporary Tablespaces](../../storage-engines/innodb/innodb-tablespaces/innodb-temporary-tablespaces.md)
* [Binary logs](../../../server-management/server-monitoring-logs/binary-log/)
* [Relay logs](../../../server-management/server-monitoring-logs/binary-log/relay-log.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
