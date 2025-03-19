# BACKUP LOCK

BACKUP LOCK blocks a table from DDL statements. This is mainly intended to be used by tools like [mariabackup](https://mariadb.com/kb/en/mariabackup/) that need to ensure there are no DDLs on a table while the table files are opened. For example, for an Aria table that stores data in 3 files with extensions .frm, .MAI and .MAD. Normal read/write operations can continue as normal.

Here's another para.

{% hint style="info" %}
BACKUP LOCK is available from MariaDB 10.4.2.
{% endhint %}

### Syntax <a href="#syntax" id="syntax"></a>

To lock a table:

```
BACKUP LOCK table_name
```

To unlock a table:

```
BACKUP UNLOCK
```

### Usage in a Backup Tool <a href="#usage-in-a-backup-tool" id="usage-in-a-backup-tool"></a>

```
BACKUP LOCK [database.]table_name;
 - Open all files related to a table (for example, t.frm, t.MAI and t.MYD)
BACKUP UNLOCK;
- Copy data
- Close files
```

This ensures that all files are from the same generation, that is created at the same time by the MariaDB server. This works, because the open files will point to the original table files which will not be affected if there is any ALTER TABLE while copying the files.

### Privileges <a href="#privileges" id="privileges"></a>

{% tabs %}
{% tab title="Current" %}
BACKUP LOCK requires the RELOAD privilege or the LOCK TABLES privilege.
{% endtab %}

{% tab title="< 11.4.1" %}
BACKUP LOCK requires the RELOAD privilege.
{% endtab %}

{% tab title="< 11.3.2" %}
BACKUP LOCK requires the RELOAD privilege.
{% endtab %}

{% tab title="< 11.1.4" %}
BACKUP LOCK requires the RELOAD privilege.
{% endtab %}

{% tab title="< 11.0.5" %}
BACKUP LOCK requires the RELOAD privilege.
{% endtab %}

{% tab title="< 10.11.7" %}
BACKUP LOCK requires the RELOAD privilege.
{% endtab %}

{% tab title="< 10.6.17" %}
BACKUP LOCK requires the RELOAD privilege.
{% endtab %}

{% tab title="< 10.5.24" %}
BACKUP LOCK requires the RELOAD privilege.
{% endtab %}

{% tab title="< 10.4.33" %}
BACKUP LOCK requires the RELOAD privilege.
{% endtab %}
{% endtabs %}

_For demonstration purposes, what is now in tabbed navigation looked like this in the KB:_

> Prior to [MariaDB 10.4.33](https://mariadb.com/kb/en/mariadb-10433-release-notes/), [MariaDB 10.5.24](https://mariadb.com/kb/en/mariadb-10524-release-notes/), [MariaDB 10.6.17](https://mariadb.com/kb/en/mariadb-10617-release-notes/), [MariaDB 10.11.7](https://mariadb.com/kb/en/mariadb-10-11-7-release-notes/), [MariaDB 11.0.5](https://mariadb.com/kb/en/mariadb-11-0-5-release-notes/), [MariaDB 11.1.4](https://mariadb.com/kb/en/mariadb-11-1-4-release-notes/), [MariaDB 11.2.3](https://mariadb.com/kb/en/mariadb-11-2-3-release-notes/), [MariaDB 11.3.2](https://mariadb.com/kb/en/mariadb-11-3-2-release-notes/) and [MariaDB 11.4.1](https://mariadb.com/kb/en/mariadb-11-4-1-release-notes/), BACKUP LOCK requires the [RELOAD](https://mariadb.com/kb/en/grant/#reload) privilege.
>
> From [MariaDB 10.4.33](https://mariadb.com/kb/en/mariadb-10433-release-notes/), [MariaDB 10.5.24](https://mariadb.com/kb/en/mariadb-10524-release-notes/), [MariaDB 10.6.17](https://mariadb.com/kb/en/mariadb-10617-release-notes/), [MariaDB 10.11.7](https://mariadb.com/kb/en/mariadb-10-11-7-release-notes/), [MariaDB 11.0.5](https://mariadb.com/kb/en/mariadb-11-0-5-release-notes/), [MariaDB 11.1.4](https://mariadb.com/kb/en/mariadb-11-1-4-release-notes/), [MariaDB 11.2.3](https://mariadb.com/kb/en/mariadb-11-2-3-release-notes/), [MariaDB 11.3.2](https://mariadb.com/kb/en/mariadb-11-3-2-release-notes/) and [MariaDB 11.4.1](https://mariadb.com/kb/en/mariadb-11-4-1-release-notes/), BACKUP LOCK is also accessible to those with [database LOCK TABLES](https://mariadb.com/kb/en/grant/#database-privileges) privileges.

### Notes <a href="#notes" id="notes"></a>

* The idea is that the `BACKUP LOCK` should be held for as short a time as possible by the backup tool. The time to take an uncontested lock is very short! One can easily do 50,000 locks/unlocks per second on low end hardware.
* One should use different connections for [BACKUP STAGE](https://mariadb.com/kb/en/backup-stage/) commands and `BACKUP LOCK`.

### Implementation <a href="#implementation" id="implementation"></a>

* Internally, BACKUP LOCK is implemented by taking an `MDLSHARED_HIGH_PRIO` MDL lock on the table object, which protects the table from any DDL operations.
