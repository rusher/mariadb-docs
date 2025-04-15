
# Extent Map Backup & Recovery

ColumnStore uses a smart structure called an Extent Map to provide a logical range for partitioning and remove the need for indexing, manual table partitioning, materialized views, summary tables and other structures and objects that row-based databases must implement for query performance.


Extents are logical blocks of space that exist within a physical segment file, and is anywhere between 8 and 64 MB in size. Each Extent supports the same number of rows, with smaller data types using less disk space. The Extent Map catalogs Extents to their corresponding blocks (LBID's), along with minimum and maximum values for the column's data within the Extent.


The primary node has a **master copy** of the Extent Map. On system startup, the file is read into memory, then physically copied to all other participating nodes for disaster recovery and failover. Nodes keep the Extent Map in memory for quick access.


If this **master copy** were to become corrupted, your system could become unusable and data loss could occur.


The ColumnStore team currently has two projects under development to address this. One will address the crash proofing of this file and the other ([MCOL-312](https://jira.mariadb.org/browse/MCOL-312)) will allow for extent map rebuild via a new utility.


In the interim, we recommend that users of ColumnStore follow the following procedures to allow a quick recovery from such an outage.


### BACKUP OF MASTER COPY


* `<code>$ mariadb -e "FLUSH TABLES WITH READ LOCK;"</code>`
* `<code>$ save_brm</code>`
* `<code>$ mkdir -p /extent_map_backup</code>`
* `<code>$ cp -f /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_em /extent_map_backup</code>`
* `<code>$ mariadb -e "UNLOCK TABLES;"</code>`


### RECOVERY FOR SINGLE NODE SYSTEM


* `<code>$ systemctl stop mariadb-columnstore</code>`
* `<code>$ mv /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_em /tmp/BRM_saves_em.bad</code>`
* `<code>$ cat /dev/null > /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_vbbm</code>`
* `<code>$ cat /dev/null > /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_vss</code>`
* `<code>$ cp -f /extent_map_backup/BRM_saves_em /var/lib/columnstore/data1/systemFiles/dbrm/</code>`
* `<code>$ chown -R mysql:mysql /var/lib/columnstore/data1/systemFiles/dbrm/</code>`
* `<code>$ systemctl start mariadb-columnstore</code>`


### RECOVERY FOR CLUSTERED SYSTEM


* `<code>$ curl -s -X PUT https://127.0.0.1:8640/cmapi/0.4.0/cluster/shutdown --header 'Content-Type:application/json' --header 'x-api-key:somekey123' --data '{"timeout":60}' -k</code>`
* `<code>$ mv /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_em /tmp/BRM_saves_em.bad</code>`
* `<code>$ cat /dev/null > /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_vbbm</code>`
* `<code>$ cat /dev/null > /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_vss</code>`
* `<code>$ cp -f /extent_map_backup/BRM_saves_em /var/lib/columnstore/data1/systemFiles/dbrm/</code>`
* `<code>$ chown -R mysql:mysql /var/lib/columnstore/data1/systemFiles/dbrm/</code>`
* `<code>$ curl -s -X PUT https://127.0.0.1:8640/cmapi/0.4.0/cluster/start --header 'Content-Type:application/json' --header 'x-api-key:somekey123' --data '{"timeout":60}' -k </code>`


### AUTOMATION


It might be a good idea to include a simple `<code>save_brm</code>` command to the end of any [cpimport](../columnstore-data-ingestion/columnstore-bulk-data-loading.md) scripting that you might current be using. Please see this GitHub link for a working example of a simple [backup script](https://raw.githubusercontent.com/mariadb-corporation/columnstore-extent-backup/main/copy_extents).

