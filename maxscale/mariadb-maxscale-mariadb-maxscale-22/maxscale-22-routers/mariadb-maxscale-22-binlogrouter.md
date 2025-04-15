
# Binlogrouter

# Binlogrouter


The binlogrouter is a replication protocol proxy module for MariaDB
MaxScale. This module allows MariaDB MaxScale to connect to a master server and
retrieve binary logs while slave servers can connect to MariaDB MaxScale like
they would connect to a normal master server. If the master server goes down,
the slave servers can still connect to MariaDB MaxScale and read binary
logs. You can switch to a new master server without the slaves noticing that the
actual master server has changed. This allows for a more highly available
replication setup where replication is high-priority.


# Configuration


## Mandatory Router Parameters


The binlogrouter requires the `<code>user</code>` and `<code>password</code>` parameters. These should be
configured according to the
[Configuration Guide](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#service).


In addition to these two parameters, the `<code>server_id</code>` and `<code>binlogdir</code>` parameters needs to be defined.


## Router Parameters


The binlogrouter accepts the following parameters.


**Note:** Earlier versions of MaxScale supported the configuration of the
binlogrouter only via `<code>router_options</code>` (a the comma-separated list of key-value
pairs). As of MaxScale 2.1, all of the router options should be defined as
parameters. The values defined in `<code>router_options</code>` will have priority over the
parameters to support legacy configurations. The use of `<code>router_options</code>` is
deprecated.


### `<code>binlogdir</code>`


This parameter controls the location where MariaDB MaxScale stores the binary log
files. This is a mandatory parameter.


The *binlogdir* also contains the *cache* subdirectory which stores data
retrieved from the master during the slave registration phase. The
master.ini file also resides in the *binlogdir*. This file keeps track of
the current master configuration and it is updated when a `<code>CHANGE MASTER
TO</code>` query is executed.


From 2.1 onwards, the 'cache' directory is stored in the same location as other
user credential caches. This means that with the default options, the user
credential cache is stored in
`<code>/var/cache/maxscale/<Service Name>/<Listener Name>/cache/</code>`.


Read the [MySQL Authenticator](../maxscale-22-authenticators/mariadb-maxscale-22-mysql-authenticator.md)
documentation for instructions on how to define a custom location for the user
cache.


### `<code>server_id</code>`


MariaDB MaxScale must have a unique *server_id*. This parameter configures
the value of the *server_id* that MariaDB MaxScale will use when
connecting to the master. This is a mandatory parameter.


Older versions of MaxScale allowed the ID to be specified using `<code>server-id</code>`.
This has been deprecated and will be removed in a future release of MariaDB MaxScale.


### `<code>master_id</code>`


The *server_id* value that MariaDB MaxScale should use to report to the slaves
that connect to MariaDB MaxScale.


This may either be the same as the server id of the real master or can be
chosen to be different if the slaves need to be aware of the proxy
layer. The real master server ID will be used if the option is not set.


Older versions of MaxScale allowed the ID to be specified using `<code>master-id</code>`.
This has been deprecated and will be removed in a future release of MariaDB MaxScale.


### `<code>uuid</code>`


This is used to set the unique UUID that the binlog router uses when it connects
to the master server. By default the UUID will be generated.


### `<code>master_uuid</code>`


It is a requirement of replication that each server has a unique UUID value. If
this option is not set, binlogrouter will identify itself to the slaves using
the UUID of the real master.


### `<code>master_version</code>`


By default, the router will identify itself to the slaves using the server
version of the real master. This option allows the router to use a custom
version string.


### `<code>master_hostname</code>`


By default, the router will identify itself to the slaves using the hostname of
the real master. This option allows the router to use a custom hostname.


### `<code>slave_hostname</code>`


Since MaxScale 2.1.6 the router can optionally identify itself to the master
using a custom hostname. The specified hostname can be seen in the master via
`<code>SHOW SLAVE HOSTS</code>` command. The default is not to send any hostname string
during registration.


### `<code>user</code>`


*Note:* This is option can only be given to the `<code>router_options</code>` parameter. Use
 the `<code>user</code>` parameter of the service instead.


This is the user name that MariaDB MaxScale uses when it connects to the
master. This user name must have the rights required for replication as with any
other user that a slave uses for replication purposes. If the user parameter is
not given in the router options then the same user as is used to retrieve the
credential information will be used for the replication connection, i.e. the
user in the service entry.


This user is the only one available for MySQL connection to MaxScale Binlog
Server for administration when master connection is not done yet.


In MaxScale 2.1, the service user injection is done by the MySQLAuth
authenticator module. Read the
[MySQL Authenticator](../maxscale-22-authenticators/mariadb-maxscale-22-mysql-authenticator.md)
documentation for more details.


The user that is used for replication must be granted replication privileges on
the database server.



```
CREATE USER 'repl'@'maxscalehost' IDENTIFIED by 'password';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'maxscalehost';
```



### `<code>password</code>`


*Note:* This is option can only be given to the `<code>router_options</code>` parameter. Use
 the `<code>password</code>` parameter of the service instead.


The password for the user. If the password is not explicitly given then the
password in the service entry will be used. For compatibility with other
username and password definitions within the MariaDB MaxScale configuration file
it is also possible to use the parameter `<code>passwd</code>`.


### `<code>heartbeat</code>`


This defines the value of the heartbeat interval in seconds for the connection
to the master. The default value for the heartbeat period is every 5 minutes.


MariaDB MaxScale requests the master to ensure that a binlog event is sent at
least every heartbeat period. If there are no real binlog events to send the
master will sent a special heartbeat event. The current interval value is
reported in the diagnostic output.


### `<code>burstsize</code>`


This parameter is used to define the maximum amount of data that will be sent to
a slave by MariaDB MaxScale when that slave is lagging behind the master. The
default value is `<code>1M</code>`.


The burst size can be provided as specified
[here](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#sizes), except that IEC binary
prefixes can be used as suffixes only from MaxScale 2.1 onwards. MaxScale 2.0
and earlier only support `<code>burstsize</code>` defined in bytes.


In this situation the slave is said to be in "catchup mode", this parameter is
designed to both prevent flooding of that slave and also to prevent threads
within MariaDB MaxScale spending disproportionate amounts of time with slaves
that are lagging behind the master.


### `<code>mariadb10-compatibility</code>`


This parameter allows binlogrouter to replicate from a MariaDB 10.0 master
server: this parameter is enabled by default since MaxScale 2.2.0.
In earlier versions the parameter was disabled by default.



```
# Example
mariadb10-compatibility=1
```



Additionally, since MaxScale 2.2.1, MariaDB 10.x slave servers
can connect to binlog server using GTID value instead of binlog name and position.


Example of a MariaDB 10.x slave connection to MaxScale



```
MariaDB> SET @@global.gtid_slave_pos='0-10122-230';
MariaDB> CHANGE MASTER TO
         MASTER_HOST='192.168.10.8',
         MASTER_PORT=5306,
         MASTER_USE_GTID=Slave_pos;
MariaDB> START SLAVE;
```



**Note:**


* Slave servers can connect either with file and pos or GTID.
* MaxScale saves all the incoming MariaDB GTIDs (DDLs and DMLs)
in a sqlite3 database located in binlogdir (`<code>gtid_maps.db</code>`).
When a slave server connects with a GTID request a lookup is made for
the value match and following binlog events will be sent.


### `<code>transaction_safety</code>`


This parameter is used to enable/disable incomplete transactions detection in
binlog router. The default value is *off*.


When MariaDB MaxScale starts an error message may appear if current binlog file
is corrupted or an incomplete transaction is found. During normal operations
binlog events are not distributed to the slaves until a COMMIT is seen. Set
transaction_safety=on to enable detection of incomplete transactions.


### `<code>send_slave_heartbeat</code>`


This defines whether MariaDB MaxScale sends the heartbeat packet to the slave
when there are no real binlog events to send. This parameter takes a boolean
value and the default value is false. This means that no heartbeat events are
sent to slave servers.


If value is set to true the interval value (requested by the slave during
registration) is reported in the diagnostic output and the packet is send after
the time interval without any event to send.


### `<code>semisync</code>`


This parameter controls whether binlog server could ask Master server to start
the Semi-Synchronous replication. This parameter takes a boolean value and the
default value is false.


In order to get semi-sync working, the Master server must have the
*rpl_semi_sync_master* plugin installed. The availability of the plugin and the
value of the GLOBAL VARIABLE *rpl_semi_sync_master_enabled* are checked in the
Master registration phase: if the plugin is installed in the Master database,
the binlog server subsequently requests the semi-sync option.


Note:
 - the network replication stream from Master has two additional bytes before
 each binlog event.
 - the Semi-Sync protocol requires an acknowledge packet to be sent back to
 Master only when requested: the semi-sync flag will have value of 1.
 This flag is set only if *rpl_semi_sync_master_enabled=1* is set in the
 Master, otherwise it will always have value of 0 and no ack packet is sent
 back.


Please note that semi-sync replication is only related to binlog server to
Master communication.


### `<code>ssl_cert_verification_depth</code>`


This parameter sets the maximum length of the certificate authority chain that
will be accepted. Legal values are positive integers. This applies to SSL
connection to master server that could be acivated either by writing options in
master.ini or later via a *CHANGE MASTER TO* command. This parameter cannot be
modified at runtime. The default verification depth is 9.


### `<code>encrypt_binlog</code>`


Whether to encrypt binlog files: the default is *off*.


When set to *on* the binlog files will be encrypted using specified AES algorithm
and the KEY in the specified key file.


**Note:** binlog encryption must be used while replicating from a MariaDB 10.1
server and serving data to MariaDB 10.x slaves. In order to use binlog
encryption the master server MariaDB 10.1 must have encryption active
(encrypt-binlog=1 in my.cnf). This is required because both master and maxscale
must store encrypted data for a working scenario for Secure
data-at-rest. Additionally, as long as Master server doesn't send the
StartEncryption event (which contains encryption setup information for the
binlog file), there is a position gap between end of FormatDescription event pos
and next event start pos. The StartEncryption event size is 36 or 40 (depending
on CRC32 being used), so the gap has that size.


MaxScale binlog server adds its own StartEncryption to binlog files consequently
the binlog events positions in binlog file are the same as in the master binlog
file and there is no position mismatch.


### `<code>encryption_algorithm</code>`


The encryption algorithm, either 'aes_ctr' or 'aes_cbc'. The default is 'aes_cbc'


### `<code>encryption_key_file</code>`


The specified key file must contains lines with following format:


`<code>id;HEX(KEY)</code>`


Id is the scheme identifier, which must have the value 1 for binlog encryption
, the ';' is a separator and HEX(KEY) contains the hex representation of the KEY.
The KEY must have exact 16, 24 or 32 bytes size and the selected algorithm
(aes_ctr or aes_cbc) with 128, 192 or 256 ciphers will be used.


**Note:** the key file has the same format as MariaDB 10.1 server so it's
possible to use an existing key file (not encrypted) which could contain several
`<code>scheme;key</code>` values: only key id with value 1 will be parsed, and if not found
an error will be reported.


Example key file with multiple keys:



```
#
# This is the Encryption Key File
# key id 1 is for binlog files encryption: it's mandatory
# The keys come from a 32bytes value, 64 bytes with HEX format
#
2;abcdef1234567890abcdef12345678901234567890abcdefabcdef1234567890
1;5132bbabcde33ffffff12345ffffaaabbbbbbaacccddeee11299000111992aaa
3;bbbbbbbbbaaaaaaabbbbbccccceeeddddd3333333ddddaaaaffffffeeeeecccd
```



### `<code>mariadb10_master_gtid</code>`


This option allows MaxScale binlog router to register with MariaDB 10.X master
using GTID instead of *binlog_file* name and *position* in CHANGE MASTER TO
admin command. This feature is disabled by default.


The user can set a known GTID or an empty value (in this case the Master server
will send events from it's first available binlog file).


Example of MaxScale connection to a MariaDB 10.X Master



```
# mysql -h $MAXSCALE_HOST -P $MAXCALE_PORT
MariaDB> SET @@global.gtid_slave_pos='0-198-123';
MariaDB> CHANGE MASTER TO
         MASTER_HOST='192.168.10.5',
         MASTER_PORT=3306,
         MASTER_USE_GTID=Slave_pos;
MariaDB> START SLAVE;
```



If using GTID request then it's no longer possible to use MASTER_LOG_FILE and
MASTER_LOG_POS in `<code>CHANGE MASTER TO</code>` command: an error will be reported.


If this feature is enabled, the *transaction_safety* option will be
automatically enabled. The binlog files will also be stored in a
hierarchical directory tree instead of a single directory.


**Note:**


* When the option is On, the connecting slaves can only use GTID request:
specifying file and pos will end up in an error sent by MaxScale and
replication cannot start.
* The GTID request could cause the writing of events
in any position of the binlog file, whose name has been sent
by the master server before any event.
In order to avoid holes in the binlog files, MaxScale will fill all gaps
in the binlog files with ignorable events.
* It's not possible to specify the GTID _domain_id: the master one
is being used for all operations. All slave servers must use the same replication domain as the master server.


### `<code>master_retry_count</code>`


This option sets the maximum number of connection retries when the master server is disconnected or not reachable.
Default value is 1000.


### `<code>connect_retry</code>`


The option sets the time interval for a new connection retry to master server, default value is 60 seconds.


**A complete example** of a service entry for a binlog router service would be as
follows.



```
[Replication]
type=service
router=binlogrouter
user=maxscale
passwd=maxpwd
server_id=3
binlogdir=/var/lib/maxscale/
mariadb10-compatibility=1
encrypt_binlog=1
encryption_algorithm=aes_ctr
encryption_key_file=/var/binlogs/enc_key.txt
```



## Examples


The [Replication Proxy](../maxscale-22-tutorials/mariadb-maxscale-22-mariadb-maxscale-as-a-binlog-server.md) tutorial will
show you how to configure and administrate a binlogrouter installation.


Tutorial also includes SSL communication setup to the master server and SSL
client connections setup to MaxScale Binlog Server.
