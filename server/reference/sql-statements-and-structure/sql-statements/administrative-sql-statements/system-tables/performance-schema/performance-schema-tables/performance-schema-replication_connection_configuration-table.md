
# Performance Schema replication_connection_configuration Table


##### MariaDB starting with [10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
The `replication_connection_configuration` table was added in [MariaDB 10.6.0](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md).


The [Performance Schema](performance-schema-table_handles-table.md) replication_connection_configuration table displays replica's configuration settings used for connecting to the primary.


It contains the following fields.



| Column | Type | Null | Description |
| --- | --- | --- | --- |
| Column | Type | Null | Description |
| CHANNEL_NAME | varchar(256) | NO | The replication channel used. |
| HOST | char(60) | NO | The host name of the source that the replica is connected to. |
| PORT | int(11) | NO | The port used to connect to the source. |
| USER | char(32) | NO | The user name of the replication user account used to connect to the source. |
| USING_GTID | enum('NO', 'CURRENT_POS', 'SLAVE_POS') | NO | Whether replication is using GTIDs or not. |
| SSL_ALLOWED | enum('YES', 'NO', 'IGNORED') | NO | Whether SSL is allowed for the replica connection. |
| SSL_CA_FILE | varchar(512) | NO | Path to the file that contains one or more certificates for trusted Certificate Authorities (CA) to use for TLS. |
| SSL_CA_PATH | varchar(512) | NO | Path to a directory that contains one or more PEM files that contain X509 certificates for a trusted Certificate Authority (CA) to use for TLS. |
| SSL_CERTIFICATE | varchar(512) | NO | Path to the certificate used to authenticate the master. |
| SSL_CIPHER | varchar(512) | NO | Which cipher is used for encription. |
| SSL_KEY | varchar(512) | NO | Path to the private key used for TLS. |
| SSL_VERIFY_SERVER_CERTIFICATE | enum('YES','NO') | NO | Whether the server certificate is verified as part of the SSL connection. |
| SSL_CRL_FILE | varchar(255) | NO | Path to the PEM file containing one or more revoked X.509 certificates. |
| SSL_CRL_PATH | varchar(255) | NO | PATH to a folder containing PEM files containing one or more revoked X.509 certificates. |
| CONNECTION_RETRY_INTERVAL | int(11) | NO | The number of seconds between connect retries. |
| CONNECTION_RETRY_COUNT | bigint(20) unsigned | NO | The number of times the replica can attempt to reconnect to the source in the event of a lost connection. |
| HEARTBEAT_INTERVAL | double(10,3) unsigned | NO | Number of seconds after which a heartbeat will be sent. |
| IGNORE_SERVER_IDS | longtext | NO | Binary log events from servers (ids) to ignore. |
| REPL_DO_DOMAIN_IDS | longtext | NO | Only apply binary logs from these domain ids. |
| REPL_IGNORE_DOMAIN_IDS | longtext | NO | Binary log events from domains to ignore. |


