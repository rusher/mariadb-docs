# MariaDB ColumnStore 25.10.0 Release Notes

{% hint style="info" %}
This is the first release of the 25.10 release series, and Alpha release status. For that reason, this page doesn't comprise minor bug fixes or feature changes.
{% endhint %}

{% hint style="info" %}
ColumnStore 25.10.0 works with MariaDB Enterprise Server 11.8.
{% endhint %}

## Role in MariaDB Enterprise Platform 2026

MariaDB ColumnStore, the columnar storage engine optimized for Online Analytical Processing (OLAP) workloads, enhances MariaDB Platform 2026 with advanced hybrid transactional-analytical processing (HTAP) capabilities. Its massively parallel processing (MPP) architecture enables real-time analytics directly on live InnoDB transactional data, eliminating the need for separate data pipelines or delayed imports. Tightly integrated with MariaDB Enterprise Server, ColumnStore supports parallel execution of complex analytical queries alongside transactional workloads, delivering instant insights from dynamic datasets. With enhanced scalability, streamlined cluster management, and robust data handling, ColumnStore in the 2026 Platform is the ideal solution for enterprises seeking seamless, high-performance analytics and transactional processing in modern data-driven applications.

Major improvements relative to previous release series include:

* Scalability & Performance
  * Horizontal scaling option via read-only nodes
  * New bulk loading import flags and improvements
* Operations & Usability
  * New, simplified upgrade process

## Features

<details>

<summary>Query Accelerator (Alpha)</summary>

Access your InnoDB data in real time by processing it in the ColumnStore engine. This allows you to run fast analytics on live data, without needing to maintain a pipeline or delayed/batched insert into ColumnStore. Parallel-execute your OLAP queries straight from your transactional data.&#x20;

</details>

<details>

<summary>Read-Replica Nodes</summary>

ColumnStore can now horizontally scale up and down faster and with less effort than ever before. By using shared storage, additional compute focused on just query execution, you can independently scale compute and QPS[^1] without needing to reimport your data. Example:&#x20;

```bash
mcs cluster node add --node $pm2 --read-replica
```

</details>

<details>

<summary>New Upgrades Architecture</summary>

The new upgrade architecture automates almost everything, saving time and reducing risks. New pre- and post-upgrade checks keep your cluster safe.

</details>

<details>

<summary>RHEL 10 Support</summary>

Columnstore now can be installed on Red Hat’s recently released RHEL 10 OS.

</details>

<details>

<summary>New quality of life cpimport headers <code>-e all</code> and <code>-L "/tmp/failed_records.out"</code> options</summary>

* `-e all`
  * Now you can skip all errors when importing records similar to `LOAD DATA INFILE IGNORE`. Before, you had to define a number of errors, and users tended to set it to a really high number like `99999`.
* `-L`
  * Rows that produce an error are now stored separately into a new file, so you can easily and quickly review what failed and reimport just the failed records. Previously, you would not know which specific records failed, requiring to do your own analysis of what was imported versus skipped.

</details>

<details>

<summary>New log bundling, backup &#x26; restore orchestration via CMAPI</summary>

* mcs review --help
  * No longer do you need to download our supports external script for log bundling as cmapi includes this on every install. This will make it easier and quicker to bundle your logs and run other common checks. External scripts for log bundling aren't required anymore, because CMAPI includes log bundling. Example: `mcs review --logs`

- `mcs backup --help` and `mcs restore --help`&#x20;
  * Back up and restore your ColumnStore database easier than ever. External scripts to manage those operations are no longer needed, because CMAPI includes it. Example: `mcs dbrm_backup`

</details>

## &#x20;Notable Bugs Fixed

* On failover, metadata could become corrupted when looking for a file that's not supposed to exist called `BRM_savesB_journal`.
* Added `ORDER BY` and `LIMIT`/`OFFSET` processing for `UNION` queries.
* `cpimport` maximum batch size `-q` raised to 8,000,000.

[^1]: Queries per second
