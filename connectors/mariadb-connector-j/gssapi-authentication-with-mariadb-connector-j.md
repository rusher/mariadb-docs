# GSSAPI Authentication with MariaDB Connector/J

MariaDB has supported GSSAPI authentication since [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1) when the `[gssapi](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi)` authentication plugin was added.

The following subsections show how to implement GSSAPI Authentication with MariaDB Connector/J.

Support history:

* version 1.4.0 : java connector support
* version 1.5.0 : added native windows implementation.

## General configuration

The `[gssapi](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi)` authentication plugin must be installed on the database server. The relevant user account must also be configured to use the plug-in for authentication. For example:

```sql
CREATE USER one IDENTIFIED VIA gssapi AS 'userOne@EXAMPLE.COM';
```

And then this user account could be used to connect to the database server with the Java connector by specifying the user name in the Java connection URL. For example:

```java
DriverManager.getConnection("jdbc:mariadb://db.example.com:3306/db?user=one");
```

Since the user account is configured to use the `[gssapi](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi)` authentication plugin on the server, the Java connector will use GSSAPI authentication when connecting.

The service principal name must be the one defined for the user account on the database server unless a different one is specified with the `[servicePrincipalName](https://mariadb.com/kb/en/about-mariadb-connector-j/#infrequently-used)` parameter in the connection URL.

Database server will wait for a ticket associated for the principal defined in user ('userOne@EXAMPLE').\
That mean on client, user must have obtained a TGT beforehand.

As part of the security context establishment, the driver will initiate a context that will be authenticated by database.\
Database also be authenticated back to the driver ("mutual authentication").

### GSSAPI configuration

#### Java system properties

Realm information are generally defined by DNS, but this can be forced using system properties.\
"java.security.krb5.kdc" defined the Key Distribution Center (KDC), realm by "java.security.krb5.realm".\
Example :

```java
System.setProperty("java.security.krb5.kdc", "kdc1.example.com");
        System.setProperty("java.security.krb5.realm", "EXAMPLE.COM");
```

Logging can be set using additional properties:

```java
System.setProperty("sun.security.krb5.debug", "true");
        System.setProperty("sun.security.jgss.debug", "true");
```

#### Java JCE

Depending on the kerberos ticket encryption, you may have to install the [Java Cryptography Extension (JCE)](https://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html) Unlimited Strength Jurisdiction Policy File.\
(CentOS/Red Hat Enterprise Linux 5.6 or later, Ubuntu are using AES-256 encryption by default for tickets).

On unix, you can execute the "klist -e" command to view the encryption type in use:\
If AES is being used, output like the following is displayed after you type the klist command (note that AES-256 is included in the output):

```
Ticket cache: FILE:/tmp/krb5cc_0
    Default principal: userOne@EXAMPLE
    Valid starting     Expires            Service principal
    03/30/15 13:25:04  03/31/15 13:25:04  krbtgt/EXAMPLE@EXAMPLE
    Etype (skey, tkt): AES-256 CTS mode with 96-bit SHA-1 HMAC, AES-256 CTS mode with 96-bit SHA-1 HMAC
```

### Implementations

On windows GSSAPI implementation is SSPI. The java 8 native implementation as many limitations ([see java ticket](https://bugs.java.com/bugdatabase/view_bug.do?bug_id=6722928)).

Driver contain 2 Different implementations:

* a java standard implementation will use JAAS to allow java to access TGT.
* a windows native implementation based on [Waffle](https://github.com/dblock/waffle)

#### Standard java SSPI implementation

**Jaas**

The driver will use the native ticket cache to get the TGT available in it using JAAS.\
If the System property "java.security.auth.login.config" is empty, driver will use the following configuration :

```
Krb5ConnectorContext {
        com.sun.security.auth.module.Krb5LoginModule required 
        useTicketCache=true 
        renewTGT=true 
        doNotPrompt=true; 
    };
```

This permit to use current user TGT cache

**limitation on windows**

Main limitation are :

* To permit java to retrieve TGT (Ticket-Granting-Ticket), windows host need to have a registry entry set.

```
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa\Kerberos\Parameters
  Value Name: AllowTGTSessionKey
  Value Type: REG_DWORD
  Value: 1
```

* Kinit command must have been executed previously to connection.

### Windows native java implementation

Implementation is based on [Waffle](https://github.com/dblock/waffle) that support windows SSPI based on [JNA](https://github.com/java-native-access/jna).

if waffle-jna (and dependencies) is in classpath, native implementation will automatically be used.\
(This permit to avoid any specific problem with admin right, registry, kinit ...)

Dependencies :

* [waffle-jna 1.8.1](https://maven-badges.herokuapp.com/maven-central/com.github.dblock.waffle/waffle-jna)
* [jna 4.2.1](https://maven-badges.herokuapp.com/maven-central/net.java.dev.jna/jna)
* [jna-platform 4.2.1](https://maven-badges.herokuapp.com/maven-central/net.java.dev.jna/jna-platform)
* [jcl-over-slf4j 1.7.14](https://maven-badges.herokuapp.com/maven-central/org.slf4j/jcl-over-slf4j)
* [slf4j-api 1.7.14](https://maven-badges.herokuapp.com/maven-central/org.slf4j/slf4j-api)
* [guava 19.0](https://maven-badges.herokuapp.com/com.google.guava/guava)

## Possible errors

* "GSSException: Failure unspecified at GSS-API level (Mechanism level: No Kerberos credentials available)"

There is no active credential. Check with klist that there is an existing credential. If not create it with the "kinit" command

* "java.sql.SQLInvalidAuthorizationSpecException: Could not connect: GSSAPI name mismatch, requested 'userOne@EXAMPLE.COM', actual name 'userTwo@EXEMPLE.COM'"

There is an existing credential, but doesn't correspond to the connection user.\
example :\
if user is created with a command like

```sql
CREATE USER userOne@'%' IDENTIFIED WITH gssapi AS 'userTwo@EXAMPLE.COM';
```

klist must show the same principal (userTwo@EXAMPLE.COM in this example)

* "GSSException: No valid credentials provided (Mechanism level: Clock skew too great (37))". The Kerberos protocol requires the time of the client

and server to match: if the system clocks of the client does not match that of the KDC server, authentication will fail with this kind of error.\
The simplest way to synchronize the system clocks is to use a Network Time Protocol (NTP) server.

{% @marketo/form formid="4316" %}
