
# mysql.servers Table

**System tables should not normally be edited directly. Use the related SQL statements instead.**



The `mysql.servers` table contains information about servers as used by the [Spider](../../../../../storage-engines/spider/spider-functions/spider_copy_tables.md), [FEDERATED](../../../../../storage-engines/legacy-storage-engines/federated-storage-engine.md) or [FederatedX](../../../../../storage-engines/federatedx-storage-engine/README.md), [Connect](../../../../../../../connectors/mariadb-connector-nodejs/connector-nodejs-pipelining.md) storage engines.


The contents are modified by the [CREATE SERVER](../../../data-definition/create/create-server.md), [ALTER SERVER](../../../data-definition/alter/alter-server.md) and [DROP SERVER](../../../data-definition/drop/drop-server.md) statements.


This table uses the [Aria](../../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine.


The `mysql.servers` table contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| Server_name | char(64) | NO | PRI |  |  |
| Host | char(64) | NO |  |  |  |
| Db | char(64) | NO |  |  |  |
| Username | char(80) | NO |  |  |  |
| Password | char(64) | NO |  |  |  |
| Port | int(4) | NO |  | 0 |  |
| Socket | char(64) | NO |  |  |  |
| Wrapper | char(64) | NO |  |  | mysql or mariadb |
| Owner | char(64) | NO |  |  |  |



## Example


```
SELECT * FROM mysql.servers\G
*************************** 1. row ***************************
Server_name: s
       Host: 192.168.1.106
         Db: test
   Username: Remote
   Password: 
       Port: 0
     Socket: 
    Wrapper: mariadb
      Owner:
```
