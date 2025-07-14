# Failover and High availability with MariaDB Connector/J

_This guide will cover:_

* The load balancing and high availability concepts in Mariadb Connector/J.
* The different options.

{% hint style="info" %}
This concerns only 3.0 version and above. see [documentation for previous version](failover-and-high-availability-with-mariadb-connector-j-for-2x-driver.md)
{% endhint %}

## Load balancing and failover distinction

Failover occurs when a connection to a primary database server fails and the connector opens up a connection to another database server.\
For example, server A has the current connection. After a failure (server crash, network down …) the connection will switch to another server (B).

Load balancing allows load (read and write) to be distributed over multiple servers.

## Replication cluster type

In MariaDB (and MySQL) replication, there are 2 different replication roles:

* primary role: Database server that permits read and write operations
* replica role: Database server that permits only read operations

This document describes configuration and implementation for 3 types of clusters:

* Multi-primary replication cluster. All hosts have a primary role. (example: Galera)
* Primary/replicas cluster: one primary host with one or multiple replicas.
* Hybrid cluster: multiple primary hosts with one or multiple replicas.

## Load balancing implementation

### Random picking

When initializing a connection or after a failed connection, the connector will attempt to connect to a host with a certain role (primary/replica).\
The connection is selected randomly among the valid hosts. Thereafter, all statements will run on that database server until the connection will be closed (or fails).

The load-balancing includes a pooling mechanism.\
Example: when creating a pool of 60 connections, each one will use a random host. With 3 master hosts, the pool will have about 20 connections to each host.

### Primary/replica distributed load

For a cluster composed of primary and replicas on connection initialization, there will be 2 underlying connections: one with a primary host, another with a replica host. Only one connection is used at a time.\
For a cluster composed of primary hosts only, each connection has only one underlying connection.\
The load will be distributed due to the random distribution of connections..

### Primary/replica connection selection

It’s the application that has to decide to use primary or replica connection (the primary connection is set by default).\
Switching the type of connection is done by using JDBC [connection.setReadOnly(boolean readOnly)](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html#setReadOnly\(boolean\)) method. Setting read-only to true will use the replica connection, false, the primary connection.

Example in standard java:

```java
connection = DriverManager.getConnection("jdbc:mariadb:replication://primary1,replica1/test");
stmt = connection.createStatement();
stmt.execute("SELECT 1"); // will execute query on the underlying primary1 connection
connection.setReadOnly(true);
stmt.execute("SELECT 1"); // will execute query on the underlying replica1 connection
```

Some frameworks render this kind of operation easier, as for example Spring [@transactionnal](https://docs.spring.io/spring/docs/current/javadoc-api/org/springframework/transaction/annotation/Transactional.html#readOnly--) readOnly parameter (since spring 3.0.1).\
In this example, setting readOnly to false will call the connection.setReadOnly(false) and therefore use the master connection.

```java
@Autowired
private EntityManager em;

@Transactional(readOnly = false, propagation = Propagation.REQUIRED)
public void createContacts() {
  Contact contact1 = new Contact();
  contact1.setGender("M");
  contact1.setName("JIM");
  em.persist(contact1);
}
```

Generated Spring Data repository objects use the same logic: the find\* method will use the primary connection, other use primary connection without having to explicitly set that for each method.

On a cluster with primary hosts only, the use of connection.setReadOnly(false/true) won't have any impact.

## Failover behaviour

When a failover/high availability parameter is set. Check the [configuration](failover-and-high-availability-with-mariadb-connector-j.md#configuration) section for an overview on how to set the parameters.

There can be multiple fail causes. When a failure occurs many things will be done:

* connection recovery
* re-execute command if possible

During failover, the fail host address will be put on a blacklist (shared by JVM) for 60 seconds.The only time a blacklisted host can be used is if all hosts of the same type (primary/replica) are blacklisted.

#### Failover on replica connection

(connection.setReadOnly(true) was called)

If driver fails to recover connection, and connection was a replica, driver will try to connect to another replica if any and reexecute the command. If replica reconnection fails, driver will temporary use the primary connection, reexecuting the command on the primary connection, silently ignoring the error. driver won't try to reconnect to replica for 30s.

#### Failover on primary connection

The driver will try to reconnect to any valid host (not blacklisted, or if all primary host are blacklisted trying blacklisted hosts).\
If reconnection fail, an SQLException with be thrown with SQLState "08XXX". If using a pool, this connection will be discarded.

on successful reconnection, there will be different cases.

If driver identify that command can be replayed without issue (for example connection.isValid(), a PREPARE/ROLLBACK command), driver will execute command without throwing any error.

Driver cannot transparently handle all cases : imagine that the failover occurs when executing an INSERT command without a transaction: driver cannot know that command has been received and executed on server. In those case, an SQLException with be thrown with SQLState "25S03".

**option `transactionReplay` :**

Most of the time, queries occurs in transaction (ORM for example doesn't permit using auto-commit), so redo transaction implementation will solve most of failover cases transparently for user point of view.

Redo transaction approach is to save commands in transaction. When a failover occurs during a transaction, the connector can automatically reconnect and replay transaction, making failover completely transparent.

There is some limitations :

* driver will buffer up to option `transactionReplaySize` value (default 64) commands in a transaction
* huge command will temporary disable transaction buffering for current transaction.
* commands must be idempotent only (queries can be "replayable")

## Configuration

(See [About MariaDB java connector](about-mariadb-connector-j.md#connection-strings) for all connection parameters)\
JDBC connection string format is:

```java
jdbc:mariadb:[replication:|sequential:|loadbalance:]//<hostDescription>[,<hostDescription>...]/[database][?<key1>=<value1>[&<key2>=<value2>]...]
```

The standard option "connectTimeout" defines the socket connection timeout. By default, this option is set to 30s.\
Since there are many servers, setting this option to a small amount of time make sense.\
During the reconnection phase, the driver will try to connect to the hosts sequentially until the creation of an active connection.\
Set this option to a small value (such as 2000ms - to be set according to your environment) which will permit rejecting a faulty server quickly.

### Failover and Load Balancing Modes

Each parameter corresponds to a specific use case:

**`sequential`**

* Description: This mode supports connection failover in a multi-master environment, such as MariaDB Galera Cluster. This mode does not support load-balancing reads on slaves. The connector will try to connect to hosts in the order in which they were declared in the connection URL, so the first available host is used for all queries.For example, let's say that the connection URL is the following: `jdbc:mariadb:sequential:host1,host2,host3/testdb`When the connector tries to connect, it will always try host1 first. If that host is not available, then it will try host2. etc. When a host fails, the connector will try to reconnect to hosts in the same order.
* Introduced: 1.3.0

**`loadbalance`**

* Description: This mode supports connection load-balancing in a multi-master environment, such as MariaDB Galera Cluster. This mode does not support load-balancing reads on slaves. The connector performs load-balancing for all queries by randomly picking a host from the connection URL for each connection, so queries will be load-balanced as a result of the connections getting randomly distributed across all hosts. Before 2.4.2, this option was named `failover` - alias still exist for compatibility -
* Introduced: 1.2.0

**`replication`**

* Description: This mode supports connection failover in a master-slave environment, such as a MariaDB Replication cluster. The mode supports environments with one or more masters. This mode does support load-balancing reads on slaves if the connection is set to read-only before executing the read. The connector performs load-balancing by randomly picking a slave from the connection URL to execute read queries for a connection
* Introduced: 1.2.0

**`load-balance-read`**

* Description: When running a multi-master cluster (i.e. Galera), writing to more than one node can lead to optimistic locking errors ("deadlocks"). Writing concurrently to multiple nodes also doesn't bring a whole lot of performance, due to having to (synchronously) replicate to all nodes anyway. This mode supports connection failover in a multi-master environment, such as MariaDB Galera Cluster. This mode does support load-balancing reads on slaves. The connector will try to connect to primary hosts in the order in which they were declared in the connection URL, so the first available host is used for all queries.For example, let's say that the connection URL is the following: `jdbc:mariadb:load-balance-read:primary1,primary2,address=(host=replica1)(type=replica),address=(host=replica2)(type=replica)/DB`When the connector tries to connect, it will always try primary1 first. If that host is not available, then it will try primary2. etc. When a primary host fails, the connector will try to reconnect to hosts in the same order.For replica hosts, the connector performs load-balancing for all queries by randomly picking a replica host from the connection URL for each connection, so queries will be load-balanced as a result of the connections getting randomly distributed across all replica hosts.
* Introduced: 3.5.1

**`aurora`**

* Description: This mode supports connection failover in an Amazon Aurora cluster. This mode does support load-balancing reads on slave instances if the connection is set to read-only before executing the read. The connector performs load-balancing by randomly picking a slave instance to execute read queries for a connection
* Introduced: 1.2.0 and not supported anymore since 3.0 version

{% @marketo/form formId="4316" %}
