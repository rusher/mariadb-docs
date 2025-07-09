# Information Schema THREAD\_POOL\_WAITS Table

{% hint style="info" %}
This table is available as of MariaDB [10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105).
{% endhint %}

The table provides wait counters for the [thread pool](../../../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb.md), and contains the following columns:

| Column | Description                                                     |
| ------ | --------------------------------------------------------------- |
| Column | Description                                                     |
| REASON | name of the reason for waiting, e.g. ROW\_LOCK, DISKIO, NET ... |
| COUNT  | how often a wait for this specific reason has happened so far   |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
