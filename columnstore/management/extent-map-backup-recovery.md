---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
---

# Extent Map Backup & Recovery

MariaDB ColumnStore utilizes an Extent Map to manage data distribution across extents—logical blocks within physical segment files ranging from 8 to 64 MB. Each extent holds a consistent number of rows, with the Extent Map cataloging these extents, their corresponding block identifiers (LBIDs), and the minimum and maximum values for each column's data within the extent.​

The primary node maintains the master copy of the Extent Map. Upon system startup, this map is loaded into memory and propagated to other nodes for redundancy and quick access. Corruption of the master Extent Map can render the system unusable and lead to data loss.​

## Purpose

ColumnStore's extent map is a smart structure that underpins its performance. By providing a logical partitioning scheme, it avoids the overhead associated with indexing and other common row-based database optimizations.

The primary node in a ColumnStore cluster holds the master copy of the extent map. Upon system startup, this master copy is read into memory and then replicated to all other participating nodes for high availability and disaster recovery. Nodes keep the extent map in memory for rapid access during query processing. As data within extents is modified, these updates are broadcast to all participating nodes to maintain consistency.

If the master copy of the extent map becomes corrupted, the entire system could become unusable, potentially leading to data loss. Having a recent backup of the extent map allows for a much faster recovery compared to reloading the entire database in such a scenario.

## Backup Procedure

**Note**: MariaDB recommends implementing regular backups to ensure data integrity and recovery. A common default is to back up every 3 hours and retain backups for at least 10 days.

To safeguard against potential Extent Map corruption, regularly back up the master copy:

1. Lock Table:

```
mariadb -e "FLUSH TABLES WITH READ LOCK;"
```

2. Save BRM:

```
save_brm
```

3. Create Backup Directory:

```
mkdir -p /extent_map_backup
```

4. Copy Extent Map:

```
cp -f /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_em /extent_map_backup
```

5. Unlock Tables:

```
mariadb -e "UNLOCK TABLES;"
```

## Recovery Procedures

### Single-Node System

1. Stop ColumnStore:

```
systemctl stop mariadb-columnstore
```

2. Rename Corrupted Map:

```
mv /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_em /tmp/BRM_saves_em.bad
```

3. Clear Versioning Files:

```
> /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_vbbm > /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_vss
```

1. Restore Backup:

```
cp -f /extent_map_backup/BRM_saves_em /var/lib/columnstore/data1/systemFiles/dbrm/
```

4. Set Ownership:

```
chown -R mysql:mysql /var/lib/columnstore/data1/systemFiles/dbrm/
```

5. Start ColumnStore:

```
systemctl start mariadb-columnstore
```

### Clustered System

1. Shutdown Cluster:

```
curl -s -X PUT https://127.0.0.1:8640/cmapi/0.4.0/cluster/shutdown \ --header 'Content-Type:application/json' \ --header 'x-api-key:your_api_key' \ --data '{"timeout":60}' -k
```

2. Rename Corrupted Map:

```
mv /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_em /tmp/BRM_saves_em.bad
```

3. Clear Versioning Files:

```
> /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_vbbm > /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_vss
```

4. Restore Backup:

```
mv cp -f /extent_map_backup/BRM_saves_em /var/lib/columnstore/data1/systemFiles/dbrm/
```

5. Set Ownership:

```
chown -R mysql:mysql /var/lib/columnstore/data1/systemFiles/dbrm
```

6. Start Cluster:

```
curl -s -X PUT https://127.0.0.1:8640/cmapi/0.4.0/cluster/start \ --header 'Content-Type:application/json' \ --header 'x-api-key:your_api_key' \ --data '{"timeout":60}' -k
```

## Automation Recommendation

Incorporate the `save_brm` command into your data import scripts (e.g., those using `cpimport`) to automate Extent Map backups. This practice ensures regular backups without manual intervention. Refer to the MariaDB ColumnStore Backup Script for an example implementation.​

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
