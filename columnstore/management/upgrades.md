# Upgrading MariaDB Enterprise ColumnStore (Alpha)

{% hint style="info" %}
This page documents an Alpha version of the upgrade procedure using the `mcs install_es` command. Behavior may change. Validate in a non‑production environment first.
{% endhint %}

This guide explains how to upgrade MariaDB Enterprise Server (ES) and MariaDB Enterprise ColumnStore across all nodes in a cluster using the unified `mcs` CLI tool.

The `mcs install_es` command:
- Validates your MariaDB Enterprise Repository access using an ES API token
- Stops ColumnStore and MariaDB services in a controlled sequence
- Installs/configures the ES repository for the target version
- Creates a pre‑upgrade backup of ColumnStore DBRM and config files on each node
- Upgrades MariaDB Enterprise Server, ColumnStore, and CMAPI
- Waits for CMAPI to come back online on each node and, for upgrades, automatically restarts services

## Prerequisites

- Administrative privileges on all cluster nodes (package installation and service management required)
- A valid ES API token with access to the MariaDB Enterprise Repository
- Network access from the nodes to the MariaDB Enterprise Repository endpoints
- A maintenance window: the upgrade will stop ColumnStore and MariaDB services
- Recent backups
  - At minimum, ensure Extent Map and configuration backups exist
  - Recommended: take a full backup with the `mcs backup` command

Related docs:
- [Extent Map backup and recovery](./extent-map-backup-recovery.md)
- General backup and restore guidance: [ColumnStore Backup and Restore](./column-store-backup-and-restore/)

{% hint style="warning" %}
Always back up your data before upgrading. While the tool performs a pre‑upgrade backup of DBRM and configs, it is not a substitute for a full database backup.
{% endhint %}

## Command overview

The command can target a specific ES version or use the latest tested version (currently latest 10.6 version).

- Install latest tested version:

```console
mcs install_es --token <ES_API_TOKEN>
```
or
```console
mcs install_es --token <ES_API_TOKEN> --version=latest
```

- Install a specific version:

```console
mcs install_es --token <ES_API_TOKEN> --version <ES_VERSION>
```

- Proceed even if nodes report different installed package versions (use the majority version as baseline):

```console
mcs install_es --token <ES_API_TOKEN> --version <ES_VERSION> --ignore-mismatch
```

Options summary:
- `--token TEXT`: ES API Token to use for the upgrade (required)
- `-v, --version TEXT`: ES version to install; if omitted or set to "latest", upgrades to the latest tested version
- `--ignore-mismatch`: Continue even if cluster nodes report different package versions; uses majority versions as the baseline

## Before you begin

- Quiesce or pause write workloads and heavy ingestion (e.g., cpimport, large INSERT/LOAD DATA jobs)
- Drain or put traffic managers/proxies (for example, MaxScale) into maintenance/drain mode
- Ensure you have administrative/SSH and package manager access on all nodes
- Verify time synchronization across all nodes (NTP/Chrony) to avoid coordination issues
- Confirm recent backups are complete and restorable

## What the command does (high level)

1) Validate token and target version
- If `--version=latest`, the tool resolves the latest tested ES version.
- If a specific version is requested, it is validated against the repository. Some versions could exists only for specific operating systems.

2) Stop services
- Gracefully stops the ColumnStore cluster
- Stops the MariaDB server

3) Configure repository
- Installs/configures the MariaDB Enterprise Server repository for the chosen version on each node automatically
- Validate installed repo on each node separately

4) Pre‑upgrade backups (per node)
- Creates a backup of DBRM and key configuration files with name `preupgrade_dbrm_backup` in default backup directory

5) Upgrade packages (per node)
- Upgrades MariaDB Enterprise Server and ColumnStore packages
- Upgrades CMAPI and waits for it to become ready again on each node (up to 5 minutes)

6) Service handling after upgrade
- On upgrades: automatically restarts MariaDB and the ColumnStore cluster
- On downgrades: automatic restarts are intentionally skipped; manual steps are required

## Post-upgrade checks

- Run `mcs cluster status` to verify all services are up and the cluster is healthy
- Verify CMAPI readiness on all nodes (for example, via CLI or your monitoring)
- Run a quick smoke test:
  - Create a small ColumnStore table, insert a few rows, and run a SELECT
  - Check for errors in server/ColumnStore logs
- Review `/var/tmp/mcs_cli_install_es.log` for the full sequence and ensure no errors were reported

## Downgrades

- Downgrades are supported up to MariaDB 10.6.9-5 and ColumnStore 22.08.4.
- When downgrading, the tool will not automatically restart services. Complete these steps manually:
  1. Start MariaDB on each node (for example, via your service manager)
  2. Start the ColumnStore cluster (for example, using the `mcs cluster start` command)
  3. Verify cluster health before resuming traffic

{% hint style="danger" %}
Downgrades can cause data loss or cluster inconsistency if not planned and validated. Always test and ensure backups are restorable.
{% endhint %}

## Verification and logs

After a successful upgrade or a manual restart (downgrade case):
- Validate that CMAPI is ready on all nodes
- Check ColumnStore and MariaDB services are running and the cluster is healthy

The `mcs install_es` command writes a detailed run log to:
- `/var/tmp/mcs_cli_install_es.log`

If CMAPI readiness times out or services do not start cleanly, review:
- CMAPI and service logs on each node
- The install_es log file above for the full sequence and any errors

## Known issues and limitations (Alpha/Beta)

- Mixed package versions across nodes
  - If nodes report different installed versions of Server/ColumnStore/CMAPI, the command will fail with a mismatch message
  - You can force continuation with `--ignore-mismatch`; the tool uses the majority version per package as the baseline, but this carries risk—align versions whenever possible

- CMAPI readiness timeout
  - After upgrading CMAPI, the command waits up to 300 seconds per node for readiness
  - On slow nodes or constrained environments, this timeout may be insufficient and the command will exit with a failure; verify services manually and adjust operational expectations

- Downgrade restarts are skipped by design
  - After a downgrade, automatic restarts are not performed; you must start MariaDB and the ColumnStore cluster manually and validate health

- MaxScale maintenance handling not automated
  - Transitioning MaxScale to maintenance/normal mode during upgrades is not automated at this time; manage traffic routing and maintenance state manually if applicable

- Repository access and version validation
  - Invalid tokens, network restrictions, or unsupported version strings can result in validation errors (for example, HTTP 422). Ensure the token has the correct entitlements and the requested version exists for your platform

- Single‑node detection
  - If no active nodes are detected, the tool falls back to localhost only; ensure this matches your topology

- Downgrading to 22.08.4 (10.6.9-5) techincally working but finished with known issues:
  - Got ERROR on waiting CMAPI ready. But in fact CMAPI start and working fine (check `mcs status` and `systemctl status mariadb-columnstore-cmapi` on each node)
  - If you try to run `mariadb` command you got error due to unknown configuration flag. Tool forcing to save current config files while installing packages and older MariaDB version doesn't support never flag obviously. To fix it just remove this flag from cnf file or restore config from last installed package

- Tool currently supported limited packages.
  - Only `MariaDB-server` (and dependencies), `MariaDB-columnstore-engine` (MariaDB-plugin-columnstore) and `MariaDB-columnstore-cmapi` packages remove and install supported. So packages like MariaDB-backup currently not supported and should be upgraded/downgraded manually.

## Troubleshooting tips

- Re‑run with `-v/--verbose` to enable console debug logging
- Inspect `/var/tmp/mcs_cli_install_es.log` for the complete sequence and API responses
- If package repository installation fails, verify token validity and outbound access from all nodes
- If CMAPI does not become ready, check service logs on each node.
- For mismatched node versions, align package versions before re‑running, or proceed with `--ignore-mismatch` only after assessing the risk

## Environment and network requirements

- Cluster state: ColumnStore cluster should be healthy before starting
- Node access: All nodes must be reachable (SSH/admin access) and responsive
- Disk space: Ensure sufficient free space for package downloads and pre-upgrade backups
- Internet access: Nodes must reach MariaDB Enterprise repositories (per your OS)
- CMAPI communication: Port 8640 (default) must be reachable between nodes
- Time sync: Keep NTP/Chrony synchronized across nodes

### Additional usage example (downgrade)

```console
mcs install_es --token <ES_API_TOKEN> --version 10.6.15-10
```

This will prompt for confirmation, as downgrades can be destructive. After downgrade, services are not restarted automatically—start MariaDB and the ColumnStore cluster manually and verify health.

## Recovery procedures

If the upgrade fails or CMAPI does not become ready on all nodes:

1. Review the detailed log at `/var/tmp/mcs_cli_install_es.log` for errors
2. Check service status on each node:
   - `systemctl status mariadb`
   - `systemctl status mariadb-columnstore-cmapi`
3. Verify network/ports (CMAPI 8640) and repository reachability
4. Manually start services if safe to do so:
   - `systemctl start mariadb`
   - `mcs start` (or `mcs cluster start`)
5. If corruption is suspected, follow your backup recovery plan (for example, restore from a recent backup and/or extent map backup)

## Best practices

- Pre-upgrade:
  - Create a full backup and verify restore procedures
  - Test the process in staging with similar topology/data
  - Document current package versions and configs
  - Schedule a maintenance window and inform stakeholders
- During upgrade:
  - Monitor the console output and `/var/tmp/mcs_cli_install_es.log`
  - Avoid interrupting the process; ensure network stability
- Post-upgrade:
  - Validate services and cluster health (`mcs cluster status`)
  - Run basic data integrity and application smoke tests
  - Monitor performance and logs for regressions

## Support and reporting issues

Contact MariaDB Support if you encounter unexpected failures, data issues, or performance regressions. Provide:

- The complete log file: `/var/tmp/mcs_cli_install_es.log`
- The exact command used (with parameters, masking sensitive values)
- Cluster topology (nodes, versions, OS, network)
- Source and target versions (Server, ColumnStore, CMAPI)
- Exact error messages and timestamps

## See also

- Command reference: `mcs install_es` in the CLI help and tool README
- Backups: `mcs backup` and Extent Map backup guidance
- Cluster management: `mcs cluster start|stop|status`
