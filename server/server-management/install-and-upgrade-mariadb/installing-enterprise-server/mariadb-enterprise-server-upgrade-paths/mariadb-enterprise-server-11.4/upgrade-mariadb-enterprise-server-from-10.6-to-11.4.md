# Upgrade MariaDB Enterprise Server from 10.6 to 11.4

The upgrade guide details the standard upgrade path from MariaDB Enterprise Server 10.6 to MariaDB Enterprise Server 11.4. The upgrade process involves significant changes, particularly to the query optimizer, which was rewritten in version 11.0. While performance is generally improved, query execution plans may change.

This guide provides two strategies:

1. Standard In-Place Upgrade: The direct procedure for upgrading an existing node.
2. Staged Rollout (Recommended for Mission-Critical Systems): A low-risk approach using replication and validation.

Prerequisite: [Review What's New in MariaDB Enterprise Server 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/about/mariadb-enterprise-server-differences/differences-in-mariadb-enterprise-server-11.4).

## Part 1: Standard In-Place Upgrade Process

This section details the standard procedure for performing an in-place upgrade. This involves replacing the server binaries while keeping the data directory intact.

### 1. Backup Database

Before performing any upgrade, it is critical to perform a full backup of your database. MariaDB Backup (`mariadb-backup`) is recommended for this purpose.

```bash
# Example backup command
sudo mariadb-backup --backup \
      --user=mariadb-backup_user \
      --password=mariadb-backup_passwd \
      --target-dir=/data/backup/preupgrade_backup
```

### 2. Modify Repository Configuration

Update your system's package manager repository to point to MariaDB Enterprise Server 11.4. You will need to regenerate your repository configuration command using the [MariaDB Customer Download Token](https://www.google.com/search?q=https://dlm.mariadb.com/).

{% tabs %}
{% tab title="APT (Debian/Ubuntu)" %}
{% code overflow="wrap" %}
```bash
sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply --mariadb-server-version="11.4"
```
{% endcode %}
{% endtab %}

{% tab title="YUM (RHEL/CentOS/Rocky)" %}
{% code overflow="wrap" %}
```bash
sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply --mariadb-server-version="11.4"
```
{% endcode %}
{% endtab %}

{% tab title=" ZYpp (SLES)" %}
{% code overflow="wrap" %}
```bash
sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply --mariadb-server-version="11.4"
```
{% endcode %}
{% endtab %}
{% endtabs %}

### 3. Stop MariaDB Service

Stop the running `mariadbd` process to release locks on the data files.

```bash
sudo systemctl stop mariadb
```

{% hint style="warning" %}
Ensure `innodb_fast_shutdown` is set to `1` and check for open XA transactions before stopping.
{% endhint %}

### 4. Uninstall Old Version

Remove the existing MariaDB 10.6 packages. This removes the binaries but preserves the configuration and data directory.

{% tabs %}
{% tab title="Debian/Ubuntu" %}
```bash
sudo apt-get remove "mariadb-*" galera-enterprise-4
```
{% endtab %}

{% tab title="RHEL/CentOS/Rocky" %}
```bash
sudo yum remove "MariaDB-*" galera-enterprise-4
```
{% endtab %}
{% endtabs %}

### 5. Install New Version

Install the new MariaDB 11.4 packages.

{% tabs %}
{% tab title="Debian/Ubuntu" %}
```bash
sudo apt-get install mariadb-server mariadb-backup galera-enterprise-4
```
{% endtab %}

{% tab title="RHEL/CentOS/Rocky" %}
```bash
sudo yum install MariaDB-server MariaDB-backup
```
{% endtab %}
{% endtabs %}

### 6. Update Configuration (Critical)

Before starting the server, you must update your option files (e.g., `my.cnf`) to remove unsupported parameters.

* Remove `innodb_defragment`: This variable and its associated options (e.g., `innodb_defragment_fill_factor`) have been removed.
* Remove `optimizer_adjust_secondary_key_costs`: This variable has no effect in 11.4 and must be removed.
* Check `innodb_flush_method`: This variable is deprecated in 11.4.

### 7. Start MariaDB Service

Start the new `mariadbd` process.

```bash
sudo systemctl start mariadb
```

### 8. Run mariadb-upgrade

Execute `mariadb-upgrade` to check and update system tables to be compatible with the new version.

```bash
sudo mariadb-upgrade
```

## Part 2: Alternative Strategy: Staged Rollout for Mission-Critical Systems

For environments sensitive to performance changes or requiring zero downtime, the following staged rollout strategy is recommended.

{% stepper %}
{% step %}
### Introduce Replica

Provision a new server with MariaDB Enterprise Server 11.4. Configure this server as a Replica of your existing 10.6 Primary server.

{% hint style="info" %}
_See "Backward Replication Compatibility" in Part 3 for requirements._
{% endhint %}
{% endstep %}

{% step %}
### Validate and Compare (Recommended)

To identify potential performance regressions caused by the optimizer rewrite:

1. Deploy a MaxScale server (or use an existing instance) configured with the Diff Router (an Enterprise feature).
2. Route traffic to both the existing 10.6 replicas and the new 11.4 replica simultaneously.
3. Generate reports comparing the query results and execution times. Flag and investigate any queries that are notably slower on 11.4.
{% endstep %}

{% step %}
### Shift Read Traffic

Once validated, gradually move read-only traffic and reporting workloads to the 11.4 replica. Monitor the server for stability and performance.
{% endstep %}

{% step %}
### Promote to Primary

After verifying the stability of the 11.4 replica under load, schedule a maintenance window to promote the 11.4 server to be the Primary.
{% endstep %}

{% step %}
### Shift Application Traffic

Move the remaining application traffic to the new 11.4 Primary.
{% endstep %}
{% endstepper %}

## Part 3: Critical Upgrade Information

### 1. Optimizer Changes and Application Testing

The Query Optimizer was rewritten in version 11.0. While performance is generally better, query plans can change. It is vital to perform validation (as described in the Staged Rollout section) to catch regressions before production deployment. You should also run `ANALYZE TABLE` on major tables after upgrading to update statistics.

### 2. Required Configuration Changes

The following variables must be addressed in your configuration files (`my.cnf`) to prevent startup failures or warnings:

* `optimizer_adjust_secondary_key_costs`: MUST REMOVE. This variable has no effect in 11.4 as features are integrated into the new cost model.
* `innodb_defragment`: MUST REMOVE. This variable has been removed.
* `des_encrypt` / `des_decrypt`: Functions have been removed.

### 3. Backward Replication Compatibility

You can replicate from a MariaDB 11.4 Primary to a MariaDB 10.6 Replica (Backward Replication) under specific conditions:

* No new features specific to 11.4 (e.g., new JSON functions, `UUID` data type) are used in DML or DDL.
* The variable `binlog_alter_two_phase` must be set to `0` (default) on the 11.4 Primary.

### 4. System-Versioned Tables Conversion

If using System-Versioned Tables, the `row_end` column format must be updated to support the extended `TIMESTAMP` range (up to year 2106).

{% tabs %}
{% tab title="mariadb-dump" %}
Use the new `--update-history` option with `mariadb-dump` to convert `row_end` values during export.
{% endtab %}

{% tab title="In-Place" %}
Use `ALTER TABLE` to convert the tables after upgrade.

```sql
ALTER TABLE my_table FORCE;
```
{% endtab %}
{% endtabs %}
