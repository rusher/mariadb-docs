# Files Backed Up By mariadb-backup

## Files Backed Up By mariadb-backup

### Files Included in Backup

mariadb-backup backs up the files listed below.

#### InnoDB Data Files

mariadb-backup backs up the following InnoDB data files:

* InnoDB system tablespace
* InnoDB file-per-table tablespaces

#### MyRocks Data Files

{% tabs %}
{% tab title="Current" %}
mariadb-backup will back up tables that use the MyRocks storage engine. This data data is located in the directory defined by the [rocksdb\_datadir](../../storage-engines/myrocks/myrocks-system-variables.md#rocksdb_datadir) system variable. mariadb-backup backs this data up by performing a checkpoint using the [rocksdb\_create\_checkpoint](../../storage-engines/myrocks/myrocks-system-variables.md#rocksdb_create_checkpoint) system variable.
{% endtab %}

{% tab title="< 10.3.8 to 10.2.16" %}
mariadb-backup will back up tables that use the MyRocks storage engine.
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Current" %}
mariadb-backup will not back up tables that use the MyRocks storage engine. This data data is located in the directory defined by the [rocksdb\_datadir](../../storage-engines/myrocks/myrocks-system-variables.md#rocksdb_datadir) system variable. mariadb-backup backs this data up by performing a checkpoint using the [rocksdb\_create\_checkpoint](../../storage-engines/myrocks/myrocks-system-variables.md#rocksdb_create_checkpoint) system variable.
{% endtab %}

{% tab title="< 10.3.8 to 10.2.16" %}
mariadb-backup will back up tables that use the MyRocks storage engine.
{% endtab %}
{% endtabs %}

Other Data Files
----------------

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

* InnoDB Temporary Tablespaces
* Binary logs
* Relay logs

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
