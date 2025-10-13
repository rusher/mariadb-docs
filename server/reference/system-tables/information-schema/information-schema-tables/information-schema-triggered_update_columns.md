# Information Schema TRIGGERED\_UPDATE\_COLUMNS

{% hint style="info" %}
This table is available from [MariaDB 12.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.2-rolling-release/mariadb-12.2-changes-and-improvements).
{% endhint %}

The [Information Schema](../) `TRIGGERED_UPDATE_COLUMNS` table shows columns specified in [triggers](../../../../server-usage/triggers-events/triggers/) for [update](../../../sql-statements/data-manipulation/changing-deleting-data/update.md) operations.

It contains the following columns:

<table><thead><tr><th width="231.86663818359375">Column</th><th>Description</th></tr></thead><tbody><tr><td>TRIGGER_CATALOG</td><td>Always <code>def</code> in MariaDB.</td></tr><tr><td>TRIGGER_SCHEMA</td><td>Name of the database containing the trigger.</td></tr><tr><td>TRIGGER_NAME</td><td>Name of the trigger.</td></tr><tr><td>EVENT_OBJECT_CATALOG</td><td>Always <code>def</code> in MariaDB</td></tr><tr><td>EVENT_OBJECT_SCHEMA</td><td>Name of the database containing the table that the trigger is defined on. </td></tr><tr><td>EVENT_OBJECT_TABLE</td><td>Name of the table that the trigger is defined on.</td></tr><tr><td>EVENT_OBJECT_COLUMN</td><td>Name of the column that the trigger is defined on.</td></tr></tbody></table>

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
