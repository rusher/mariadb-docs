
# SHOW REPLICA STATUS

## Syntax


```
SHOW { SLAVE | REPLICA } ["connection_name"] STATUS [FOR CHANNEL "connection_name"]
```

or


```
SHOW ALL { SLAVES | REPLICAS } STATUS
```


## Description


This statement is to be run on a replica and provides status information on essential parameters of the [replica](../../../../../server-usage/replication-cluster-multi-master/README.md) threads.


This statement requires the [SUPER](../../account-management-sql-commands/grant.md#super) privilege, the [REPLICATION_CLIENT](../../account-management-sql-commands/grant.md#replication-client) privilege, or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes), the [REPLICATION SLAVE ADMIN](../../account-management-sql-commands/grant.md#binlog-monitor) privilege, or, from [MariaDB 10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1059-release-notes), the [REPLICA MONITOR](../../account-management-sql-commands/grant.md#replica-monitor) privilege.


### Multi-Source


The `ALL` and `"connection_name"` options allow you to connect to [many primaries at the same time](../../../../../server-usage/replication-cluster-multi-master/standard-replication/multi-source-replication.md).


`ALL SLAVES` (or `ALL REPLICAS` from [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1051-release-notes)) gives you a list of all connections to the primary nodes.


The rows will be sorted according to `Connection_name`.


If you specify a `connection_name`, you only get the information about that
connection. If `connection_name` is not used, then the name set by `default_master_connection` is used. If the connection name doesn't exist you will get an error:
`There is no master connection for 'xxx'`.



##### MariaDB starting with [10.7.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1070-release-notes)
The `FOR CHANNEL` keyword was added for MySQL compatibility. This is identical to
using the channel_name directly after `SHOW SLAVE`.


### Column Descriptions


The order in which the columns appear depends on the MariaDB version. This means that extracting a column value is best done by comparing the field name instead of using a fixed offset into the row.



##### MariaDB starting with [11.6.0](/kb/en/mariadb-1160-release-notes/)
These columns can also be viewed/extracted from the `[INFORMATION_SCHEMA.SLAVE_STATUS](../system-tables/information-schema/information-schema-tables/information-schema-slave_status-table.md)` table



| Name | Description |
| --- | --- |
| Name | Description |
| Connection_name | Name of the primary connection. Returned with SHOW ALL SLAVES STATUS (or SHOW ALL REPLICAS STATUS from [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1051-release-notes)) only. |
| Slave_SQL_State | State of SQL thread. Returned with SHOW ALL SLAVES STATUS (or SHOW ALL REPLICAS STATUS from [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1051-release-notes)) only. See [Slave SQL Thread States](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-states/slave-sql-thread-states.md). |
| Slave_IO_State | State of I/O thread. See [Slave I/O Thread States](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-states/replica-io-thread-states.md). |
| Master_host | Master host that the replica is connected to. |
| Master_user | Account user name being used to connect to the primary. |
| Master_port | The port being used to connect to the primary. |
| Connect_Retry | Time in seconds between retries to connect. The default is 60. The [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement can set this. The [master-retry-count](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) option determines the maximum number of reconnection attempts. |
| Master_Log_File | Name of the primary [binary log](../../../../../server-management/server-monitoring-logs/binary-log/README.md) file that the I/O thread is currently reading from. |
| Read_Master_Log_Pos | Position up to which the I/O thread has read in the current primary [binary log](../../../../../server-management/server-monitoring-logs/binary-log/README.md) file. |
| Relay_Log_File | Name of the relay log file that the SQL thread is currently processing. |
| Relay_Log_Pos | Position up to which the SQL thread has finished processing in the current relay log file. |
| Relay_Master_Log_File | Name of the primary [binary log](../../../../../server-management/server-monitoring-logs/binary-log/README.md) file that contains the most recent event executed by the SQL thread. |
| Slave_IO_Running | Whether the replica I/O thread is running and connected (Yes), running but not connected to a primary (Connecting) or not running (No). |
| Slave_SQL_Running | Whether or not the SQL thread is running. |
| Replicate_Rewrite_DB | Databases specified for replicating and rewriting with the [replicate_rewrite_db](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) option. Added in [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-11-series/what-is-mariadb-1011) |
| Replicate_Do_DB | Databases specified for replicating with the [replicate_do_db](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) option. |
| Replicate_Ignore_DB | Databases specified for ignoring with the [replicate_ignore_db](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) option. |
| Replicate_Do_Table | Tables specified for replicating with the [replicate_do_table](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) option. |
| Replicate_Ignore_Table | Tables specified for ignoring with the [replicate_ignore_table](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) option. |
| Replicate_Wild_Do_Table | Tables specified for replicating with the [replicate_wild_do_table](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) option. |
| Replicate_Wild_Ignore_Table | Tables specified for ignoring with the [replicate_wild_ignore_table](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) option. |
| Last_Errno | Alias for Last_SQL_Errno (see below) |
| Last Error | Alias for Last_SQL_Error (see below) |
| Skip_Counter | Number of events that a replica skips from the master, as recorded in the [sql_slave_skip_counter](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) system variable. |
| Exec_Master_Log_Pos | Position up to which the SQL thread has processed in the current master [binary log](../../../../../server-management/server-monitoring-logs/binary-log/README.md) file. Can be used to start a new replica from a current replica with the [CHANGE MASTER TO ... MASTER_LOG_POS](../replication-statements/change-master-to.md) option. |
| Relay_Log_Space | Total size of all relay log files combined. |
| Until_Condition | One of four possible values: None, Master, Relay, or Gtid, depending on the respective [START SLAVE UNTIL](../replication-statements/start-replica.md) condition. |
| Until_Log_File | The MASTER_LOG_FILE value of the [START SLAVE UNTIL](../replication-statements/start-replica.md) condition. |
| Until_Log_Pos | The MASTER_LOG_POS value of the [START SLAVE UNTIL](../replication-statements/start-replica.md) condition. |
| Master_SSL_Allowed | Whether an SSL connection is permitted (Yes), not permitted (No) or permitted but without the replica having SSL support enabled (Ignored) |
| Master_SSL_CA_File | The MASTER_SSL_CA option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement. |
| Master_SSL_CA_Path | The MASTER_SSL_CAPATH option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement. |
| Master_SSL_Cert | The MASTER_SSL_CERT option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement. |
| Master_SSL_Cipher | The MASTER_SSL_CIPHER option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement. |
| Master_SSL_Key | The MASTER_SSL_KEY option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement. |
| Seconds_Behind_Master | Difference between the timestamp logged on the master for the event that the replica is currently processing, and the current timestamp on the replica. Zero if the replica is not currently processing an event. With serial replication, seconds_behind_master is updated when the SQL thread begins executing a transaction. With [parallel replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/parallel-replication.md), seconds_behind_master is updated only after transactions commit. Starting in MariaDB [10.5.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-10-5-19-release-notes), [10.6.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/mariadb-10-6-12-release-notes), [10.8.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-7-release-notes), [10.9.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-10-9-5-release-notes), [10.10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/mariadb-10-10-3-release-notes), and [10.11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-11-series/mariadb-10-11-2-release-notes), an exception is drawn on the parallel replica to additionally update seconds_behind_master when the first transaction received after idling is queued to a worker for execution, to provide a reliable initial value for the duration until a transaction commits. Additional behaviors to be aware of are as follows: 1) Seconds_Behind_Master will update for ignored events, e.g. those skipped due to [sql_slave_skip_counter](../replication-statements/set-global-sql_slave_skip_counter.md). 2) On the serial replica, transactions with prior timestamps can update Seconds_Behind_Master such that it can go backwards, though this is not true for the parallel replica. 3) When configured with [MASTER_DELAY](../../../../../server-usage/replication-cluster-multi-master/standard-replication/delayed-replication.md), as a replicated transaction begins executing (i.e. on a serial or post-idle parallel replica), Seconds_Behind_Master will update before delaying, and while delaying occurs will grow to encompass the configured value. 4) There is a known issue, tracked by [MDEV-17516](https://jira.mariadb.org/browse/MDEV-17516), such that Seconds_Behind_Master will initially present as 0 on replica restart until a replicated transaction begins executing, even if the last replica session was lagging behind when stopped. |
| Master_SSL_Verify_Server_Cert | The MASTER_SSL_VERIFY_SERVER_CERT option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement. |
| Last_IO_Errno | [Error code](../../../../mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-code-reference.md) of the most recent error that caused the I/O thread to stop (also recorded in the replica's error log). 0 means no error. [RESET SLAVE](../replication-statements/reset-replica.md) or [RESET MASTER](../replication-statements/reset-master.md) will reset this value. |
| Last_IO_Error | [Error message](../../../../mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-code-reference.md) of the most recent error that caused the I/O thread to stop (also recorded in the replica's error log). An empty string means no error. [RESET SLAVE](../replication-statements/reset-replica.md) or [RESET MASTER](../replication-statements/reset-master.md) will reset this value. |
| Last_SQL_Errno | [Error code](../../../../mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-code-reference.md) of the most recent error that caused the SQL thread to stop (also recorded in the replica's error log). 0 means no error. [RESET SLAVE](../replication-statements/reset-replica.md) or [RESET MASTER](../replication-statements/reset-master.md) will reset this value. |
| Last_SQL_Error | [Error message](../../../../mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-code-reference.md) of the most recent error that caused the SQL thread to stop (also recorded in the replica's error log). An empty string means no error. [RESET SLAVE](../replication-statements/reset-replica.md) or [RESET MASTER](../replication-statements/reset-master.md) will reset this value. |
| Replicate_Ignore_Server_Ids | List of [server_ids](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) that are currently being ignored for replication purposes, or an empty string for none, as specified in the IGNORE_SERVER_IDS option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md#ignore_server_ids) statement. |
| Master_Server_Id | The master's [server_id](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) value. |
| Master_SSL_Crl | The MASTER_SSL_CRL option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement. |
| Master_SSL_Crlpath | The MASTER_SSL_CRLPATH option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement. |
| Using_Gtid | Whether or not [global transaction ID's](../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) are being used for replication (can be No, Slave_Pos, or Current_Pos). |
| Gtid_IO_Pos | Current [global transaction ID](../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) value. |
| Retried_transactions | Number of retried transactions for this connection. Returned with SHOW ALL SLAVES STATUS only. |
| Max_relay_log_size | Max [relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) size for this connection. Returned with SHOW ALL SLAVES STATUS only. |
| Executed_log_entries | How many log entries the replica has executed. Returned with SHOW ALL SLAVES STATUS only. |
| Slave_received_heartbeats | How many heartbeats we have got from the master. Returned with SHOW ALL SLAVES STATUS only. |
| Slave_heartbeat_period | How often to request a heartbeat packet from the master (in seconds). Returned with SHOW ALL SLAVES STATUS only. |
| Gtid_Slave_Pos | GTID of the last event group replicated on a replica server, for each replication domain, as stored in the [gtid_slave_pos](../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) system variable. Returned with SHOW ALL SLAVES STATUS only. |
| SQL_Delay | Value specified by MASTER_DELAY in [CHANGE MASTER](../replication-statements/change-master-to.md) (or 0 if none). |
| SQL_Remaining_Delay | When the replica is delaying the execution of an event due to MASTER_DELAY, this is the number of seconds of delay remaining before the event will be applied. Otherwise, the value is NULL. |
| Slave_SQL_Running_State | The state of the SQL driver threads, same as in [SHOW PROCESSLIST](show-processlist.md). When the replica is delaying the execution of an event due to MASTER_DELAY, this field displays: "Waiting until MASTER_DELAY seconds after master executed event". |
| Slave_DDL_Groups | This status variable counts the occurrence of DDL statements. This is a replica-side counter for optimistic parallel replication. |
| Slave_Non_Transactional_Groups | This status variable counts the occurrence of non-transactional event groups. This is a replica-side counter for optimistic parallel replication. |
| Slave_Transactional_Groups | This status variable counts the occurrence of transactional event groups. This is a replica-side counter for optimistic parallel replication. |
| Replicate_Rewrite_DB | Value of configured [replicate_rewrite_db](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-filters.md#replicate_rewrite_db) system variable/option. |
| Retried_transactions | The number of times that replicating transactions have been retried due to temporary errors (e.g. deadlocks in parallel replication). |
| Max_relay_log_size | Maximum size of the relay log (configured by variable [max_relay_log_size](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#max_relay_log_size)). |
| Executed_log_entries | Number of binary log events that have been executed, irrespective of error outcome (i.e. if the event execution results in an error, this number will still increase). |
| Slave_received_heartbeats | Number of [Heartbeat Log Events](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/heartbeat_log_event.md) that the slave has received. Note this counter does not reset when the slave is restarted; only when a new [CHANGE MASTER](../replication-statements/change-master-to.md) command has executed. |
| Slave_heartbeat_period | Configured (by [CHANGE MASTER TO MASTER_HEARTBEAT_PERIOD](../replication-statements/change-master-to.md#master_heartbeat_period)) interval in seconds between replication heartbeats. |
| Gtid_Slave_Pos | The value of the global variable [gtid_slave_pos](../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md#gtid_slave_pos), i.e. the GTID of the last transaction applied to the database by the server's [replica threads](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#threads-on-the-slave) for each replication domain. |
| Master_last_event_time | Timestamp of the last event read from the primary by the IO thread. NULL until the replica has started and the replica has read one query event from the primary that changes data. From [MariaDB 11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116). |
| Slave_last_event_time | Primary timestamp of the last event committed on the replica. NULL until the replica has started and the replica has read one query event from the primary that changes data. From [MariaDB 11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116). |
| Master_Slave_time_diff | The difference of the above two timestamps. NULL until the replica has started and the replica has read one query event from the primary that changes data. From [MariaDB 11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116). |



## Examples


If you issue this statement using the [mariadb](../../../../../clients-and-utilities/mariadb-client/README.md) client,
you can use a `\G` statement terminator rather than a semicolon to
obtain a more readable vertical layout.


```
SHOW SLAVE STATUS\G
*************************** 1. row ***************************
                Slave_IO_State: Waiting for master to send event
                   Master_Host: db01.example.com
                   Master_User: replicant
                   Master_Port: 3306
                 Connect_Retry: 60
               Master_Log_File: mariadb-bin.000021
           Read_Master_Log_Pos: 17315
                Relay_Log_File: relay-bin.000042
                 Relay_Log_Pos: 17446
         Relay_Master_Log_File: mariadb-bin.000021
              Slave_IO_Running: Yes
             Slave_SQL_Running: Yes
               Replicate_Do_DB: 
           Replicate_Ignore_DB: 
            Replicate_Do_Table: 
        Replicate_Ignore_Table: 
       Replicate_Wild_Do_Table: 
   Replicate_Wild_Ignore_Table: 
                    Last_Errno: 0
                    Last_Error: 
                  Skip_Counter: 0
           Exec_Master_Log_Pos: 17146
               Relay_Log_Space: 17972
               Until_Condition: None
                Until_Log_File: 
                 Until_Log_Pos: 0
            Master_SSL_Allowed: Yes
            Master_SSL_CA_File: 
            Master_SSL_CA_Path: 
               Master_SSL_Cert: 
             Master_SSL_Cipher: 
                Master_SSL_Key: 
         Seconds_Behind_Master: 6
 Master_SSL_Verify_Server_Cert: No
                 Last_IO_Errno: 0
                 Last_IO_Error: 
                Last_SQL_Errno: 0
                Last_SQL_Error: 
   Replicate_Ignore_Server_Ids: 
              Master_Server_Id: 1
                Master_SSL_Crl: 
            Master_SSL_Crlpath: 
                    Using_Gtid: Slave_Pos
                   Gtid_IO_Pos: 0-1-2042
       Replicate_Do_Domain_Ids: 
   Replicate_Ignore_Domain_Ids: 
                 Parallel_Mode: optimistic
                     SQL_Delay: 0
           SQL_Remaining_Delay: NULL
       Slave_SQL_Running_State: Updating
              Slave_DDL_Groups: 1
Slave_Non_Transactional_Groups: 0
    Slave_Transactional_Groups: 2041
          Replicate_Rewrite_DB:
```

```
SHOW ALL SLAVES STATUS\G
*************************** 1. row ***************************
               Connection_name: 
               Slave_SQL_State: Updating
                Slave_IO_State: Waiting for master to send event
                   Master_Host: db01.example.com
                   Master_User: replicant
                   Master_Port: 3306
                 Connect_Retry: 60
               Master_Log_File: mariadb-bin.000021
           Read_Master_Log_Pos: 17315
                Relay_Log_File: relay-bin.000042
                 Relay_Log_Pos: 17446
         Relay_Master_Log_File: mariadb-bin.000021
              Slave_IO_Running: Yes
             Slave_SQL_Running: Yes
               Replicate_Do_DB: 
           Replicate_Ignore_DB: 
            Replicate_Do_Table: 
        Replicate_Ignore_Table: 
       Replicate_Wild_Do_Table: 
   Replicate_Wild_Ignore_Table: 
                    Last_Errno: 0
                    Last_Error: 
                  Skip_Counter: 0
           Exec_Master_Log_Pos: 17146
               Relay_Log_Space: 17972
               Until_Condition: None
                Until_Log_File: 
                 Until_Log_Pos: 0
            Master_SSL_Allowed: Yes
            Master_SSL_CA_File: 
            Master_SSL_CA_Path: 
               Master_SSL_Cert: 
             Master_SSL_Cipher: 
                Master_SSL_Key: 
         Seconds_Behind_Master: 6
 Master_SSL_Verify_Server_Cert: No
                 Last_IO_Errno: 0
                 Last_IO_Error: 
                Last_SQL_Errno: 0
                Last_SQL_Error: 
   Replicate_Ignore_Server_Ids: 
              Master_Server_Id: 1
                Master_SSL_Crl: 
            Master_SSL_Crlpath: 
                    Using_Gtid: Slave_Pos
                   Gtid_IO_Pos: 0-1-2042
       Replicate_Do_Domain_Ids: 
   Replicate_Ignore_Domain_Ids: 
                 Parallel_Mode: optimistic
                     SQL_Delay: 0
           SQL_Remaining_Delay: NULL
       Slave_SQL_Running_State: Updating
              Slave_DDL_Groups: 1
Slave_Non_Transactional_Groups: 0
    Slave_Transactional_Groups: 2041
          Replicate_Rewrite_DB: 
          Retried_transactions: 0
            Max_relay_log_size: 1073741824
          Executed_log_entries: 6330
     Slave_received_heartbeats: 0
        Slave_heartbeat_period: 60.000
                Gtid_Slave_Pos: 0-1-2041
        Master_last_event_time: 2024-12-12 06:53:52
         Slave_last_event_time: 2024-12-12 06:53:50
        Master_Slave_time_diff: 2
```

You can also access some of the variables directly from status variables:


```
SET @@default_master_connection="test" ;
show status like "%slave%"

Variable_name   Value
Com_show_slave_hosts    0
Com_show_slave_status   0
Com_start_all_slaves    0
Com_start_slave 0
Com_stop_all_slaves     0
Com_stop_slave  0
Rpl_semi_sync_slave_status      OFF
Slave_connections       0
Slave_heartbeat_period  1800.000
Slave_open_temp_tables  0
Slave_received_heartbeats       0
Slave_retried_transactions      0
Slave_running   OFF
Slaves_connected        0
Slaves_running  1
```

## See Also


* [MariaDB replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/README.md)


GPLv2 fill_help_tables.sql

