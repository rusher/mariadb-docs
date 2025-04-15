
# NoSQL Protocol Module

# NoSQL Protocol Module


The `<code>nosqlprotocol</code>` module allows a MariaDB server or cluster to be
used as the backend of an application using a MongoDB® client library.
Internally, all documents are stored in a table containing two columns;
an `<code>id</code>` column for the object id and a `<code>doc</code>` column for the document itself.


When the MongoDB® client application issues MongoDB protocol *commands*,
either directly or indirectly via the client library, they are transparently
converted into the equivalent SQL and executed against the MariaDB backend.
The MariaDB responses are then in turn converted into the format expected by
the MongoDB® client library and application.




* [NoSQL Protocol Module](#nosql-protocol-module)
* [Configuring](#configuring)
* [Authentication](#authentication)

  * [NoSQL and MariaDB Users](#nosql-and-mariadb-users)

    * [The mariadb database](#the-mariadb-database)
  * [Roles and Privileges](#roles-and-privileges)
  * [Client Authentication](#client-authentication)

    * [Anonymously](#anonymously)
    * [Shared Credentials](#shared-credentials)
    * [Unique Credentials](#unique-credentials)
    * [Enforce Authentication](#enforce-authentication)
  * [Authorization](#authorization)
  * [Bootstrapping the Authentication/Authorization](#bootstrapping-the-authenticationauthorization)

    * [Explicit bootstrapping](#explicit-bootstrapping)
    * [Implicit bootstrapping](#implicit-bootstrapping)

      * [Grants](#grants)
      * [Examples](#examples)

        * [Admin User](#admin-user)
        * [Test User](#test-user)
    * [TLS/SSL](#tlsssl)
  * [NoSQL Account Database](#nosql-account-database)

    * [Private](#private)
  * [Shared](#shared)
* [Wire Protocol](#wire-protocol)
* [Client Library](#client-library)
* [Parameters](#parameters)

  * [user](#user)
  * [password](#password)
  * [authentication_required](#authentication_required)
  * [authentication_shared](#authentication_shared)
  * [authentication_db](#authentication_db)
  * [authentication_key_id](#authentication_key_id)
  * [authentication_user](#authentication_user)
  * [authentication_password](#authentication_password)
  * [authorization_enabled](#authorization_enabled)
  * [host](#host)
  * [on_unknown_command](#on_unknown_command)
  * [log_unknown_command](#log_unknown_command)
  * [auto_create_databases](#auto_create_databases)
  * [auto_create_tables](#auto_create_tables)
  * [id_length](#id_length)
  * [ordered_insert_behavior](#ordered_insert_behavior)
  * [cursor_timeout](#cursor_timeout)
  * [debug](#debug)
* [Databases and Tables](#databases-and-tables)
* [Operators](#operators)

  * [Query and Projection Operators](#query-and-projection-operators)

    * [Comparison Query Operators](#comparison-query-operators)
    * [Logical Query Operators](#logical-query-operators)
    * [Element Query Operators](#element-query-operators)

      * [$type](#type)
    * [Evaluation Query Operators](#evaluation-query-operators)
    * [Array Query Operators](#array-query-operators)

      * [$elemMatch](#elemmatch)
  * [Update Operators](#update-operators)

    * [Field Update Operators](#field-update-operators)
* [Database Commands](#database-commands)

  * [Aggregation Commands](#aggregation-commands)

    * [count](#count)
    * [distinct](#distinct)
  * [Query and Write Operation Commands](#query-and-write-operation-commands)

    * [delete](#delete)
    * [find](#find)

      * [Projection](#projection)

        * [Embedded Field Specification](#embedded-field-specification)
        * [_id Field Projection](#_id-field-projection)
      * [Inclusion or Exclusion](#inclusion-or-exclusion)
      * [Filtering by _id](#filtering-by-_id)
    * [findAndModify](#findandmodify)
    * [getLastError](#getlasterror)
    * [getMore](#getmore)
    * [insert](#insert)

      * [ordered](#ordered)

        * [default](#default)
        * [atomic](#atomic)
      * [Performance](#performance)
    * [resetError](#reseterror)
    * [update](#update)

      * [Update Statements](#update-statements)

        * [Behavior](#behavior)

          * [Update with an Update Operator Expressions document](#update-with-an-update-operator-expressions-document)
          * [Update with a Replacement Document](#update-with-a-replacement-document)
  * [Authentication Commands](#authentication-commands)

    * [Logout](#logout)
  * [User Management Commands](#user-management-commands)

    * [createUser](#createuser)
    * [dropAllUsersFromDatabase](#dropallusersfromdatabase)
    * [dropUser](#dropuser)
    * [grantRolesToUser](#grantrolestouser)
    * [revokeRolesFromUser](#revokerolesfromuser)
    * [updateUser](#updateuser)
    * [usersInfo](#usersinfo)
  * [Replication Commands](#replication-commands)

    * [isMaster](#ismaster)
    * [replSetGetStatus](#replsetgetstatus)
  * [Sessions Commands](#sessions-commands)

    * [endSessions](#endsessions)
  * [Administration Commands](#administration-commands)

    * [create](#create)
    * [createIndexes](#createindexes)
    * [drop](#drop)
    * [dropDatabase](#dropdatabase)
    * [dropIndexes](#dropindexes)
    * [fsync](#fsync)
    * [killCursors](#killcursors)
    * [listCollections](#listcollections)
    * [listDatabases](#listdatabases)
    * [listIndexes](#listindexes)
    * [renameCollection](#renamecollection)
    * [setParameter](#setparameter)
  * [Diagnostic Commands](#diagnostic-commands)

    * [buildInfo](#buildinfo)
    * [explain](#explain)
    * [getCmdLineOpts](#getcmdlineopts)
    * [getLog](#getlog)
    * [hostInfo](#hostinfo)
    * [listCommands](#listcommands)
    * [ping](#ping)
    * [serverStatus](#serverstatus)
    * [validate](#validate)
    * [whatsmyuri](#whatsmyuri)
  * [Free Monitoring Commands](#free-monitoring-commands)

    * [getFreeMonitoringStatus](#getfreemonitoringstatus)
  * [MaxScale Specific Commands](#maxscale-specific-commands)

    * [mxsAddUser](#mxsadduser)

      * [Definition](#definition)

        * [mxsAddUser](#mxsadduser_1)
      * [Syntax](#syntax)

        * [Command Fields](#command-fields)
        * [Returns](#returns)
    * [mxsCreateDatabase](#mxscreatedatabase)

      * [Definition](#definition_1)

        * [mxsCreateDatabase](#mxscreatedatabase_1)
      * [Syntax](#syntax_1)

        * [Command Fields](#command-fields_1)
        * [Returns](#returns_1)
    * [mxsDiagnose](#mxsdiagnose)

      * [Definition](#definition_2)

        * [mxsDiagnose](#mxsdiagnose_1)
      * [Syntax](#syntax_2)

        * [Command Fields](#command-fields_2)
        * [Returns](#returns_2)
    * [mxsGetConfig](#mxsgetconfig)

      * [Definition](#definition_3)
      * [mxsGetConfig](#mxsgetconfig_1)
      * [Syntax](#syntax_3)

        * [Command Fields](#command-fields_3)
        * [Returns](#returns_3)
    * [mxsRemoveUser](#mxsremoveuser)

      * [Definition](#definition_4)

        * [mxsRemoveUser](#mxsremoveuser_1)
      * [Syntax](#syntax_4)

        * [Command Fields](#command-fields_4)
        * [Returns](#returns_4)
    * [mxsSetConfig](#mxssetconfig)

      * [Definition](#definition_5)
      * [mxsSetConfig](#mxssetconfig_1)
      * [Syntax](#syntax_5)

        * [Command Fields](#command-fields_5)
        * [Returns](#returns_5)
    * [mxsUpdateUser](#mxsupdateuser)

      * [Definition](#definition_6)

        * [mxsUpdateUser](#mxsupdateuser_1)
      * [Syntax](#syntax_6)

        * [Command Fields](#command-fields_6)
        * [Returns](#returns_6)
* [Object Id](#object-id)
* [Compatibility](#compatibility)
* [Example](#example)

  * [Configuring MaxScale](#configuring-maxscale)
  * [MongoDB® Shell](#mongodb-shell)
  * [MongoDB® Node.JS Driver](#mongodb-nodejs-driver)

    * [Inserting a Document](#inserting-a-document)
    * [Finding a Document](#finding-a-document)




# Configuring


There are a number of [parameters](#parameters) with which the behavior
of *nosqlprotocol* can be adjusted. A minimal configuration looks
like:



```
[TheService]
type=service
...

[NoSQL-Listener]
type=listener
service=TheService
protocol=nosqlprotocol
nosqlprotocol.user=the_user
nosqlprotocol.password=the_password
port=17017
```



`<code>nosqlprotocol.user</code>` and `<code>nosqlprotocol.password</code>` specify the
credentials that will be used when accessing the backend database or
cluster. Note that the same credentials will be used for *all* connecting
MongoDB® clients.


Since *nosqlprotocol* is a *listener*, there must be a *service* to which
the client requests will be sent. *Nosqlprotocol* places no limitations
on what filters, routers or backends can be used.


To configure the same listener with MaxCtrl, the parameters must be passed in a
JSON object in the following manner:



```
maxctrl create listener TheService MongoDB-Listener --protocol=nosqlprotocol 'nosqlprotocol={"user":"the_user", "password": "the_password"}'
```



All the parameters that the nosqlprotocol module takes must be passed in the
same JSON object.


A complete example can be found at the [end](#example) of this document.


# Authentication


Nosqlprotocol supports *SCRAM* *authentication* as implemented by MongoDB®.
The mechanisms `<code>SCRAM-SHA-1</code>` and `<code>SCRAM-SHA-256</code>` are both supported.


If nosqlprotocol has been setup so that no authentication is required, then
when connecting only the host and port should be provided, but neither a
username nor a password.


For instance, if the *MongoDB Node.JS Driver* is used, then the connection
string should look like:



```
const uri = "mongodb://127.0.0.1:17017"
```



Similarly, if the *Mongo Shell* is used, only the host and port should
be provided:



```
$ mongo --host 127.0.0.1 --port 17017
MongoDB shell version v4.4.1
...
>
```



## NoSQL and MariaDB Users


A MariaDB user consists of a name and a host part. A user `<code>'user'@'%'</code>`
and a user `<code>'user'@'127.0.0.1'</code>` are completely different. The host part
specifies where a user may connect from, with `<code>%</code>` being a wildcard that
matches all hosts. What data a user is allowed to access and modify is
specified by what *privileges* are granted to the user.


A NoSQL user is somewhat different. It is created in the context of a
particular database, so there may be a user `<code>userx</code>` in the database `<code>dbA</code>`
and different user with the same name `<code>userx</code>` in the database `<code>dbB</code>`. What
hosts a user may connect from can be restricted, but that is a property of
the user and not an implicit part of it. What data a user is allowed to
access and modify is specified by the *roles* that have been assigned to
the user.


From the above it should be clear that there is not a 1-to-1
correspondence between the concept of a user in NoSQL and the concept
of a user in MariaDB, but that some additional conventions are needed.


To make it possible to have different NoSQL users with the same name,
the database in whose context the user is created is prepended to the
user name, separated with a dot, when the MariaDB user is created.


This is perhaps easiest to illustrate using an example:



```
MariaDB [(none)]> select user, host from mysql.user;
+-------------+-----------+
| User        | Host      |
+-------------+-----------+
| bob         | %         |
| mysql       | localhost |
+-------------+-----------+
2 rows in set (0.001 sec)
```



Currently there are two user accounts defined. Even though there is
a user `<code>bob</code>`, creating a NoSQL user `<code>bob</code>` succeeds.



```
> use test;
switched to db test
> db.runCommand({createUser: "bob", pwd: "bobspwd", roles: []});
{ "ok" : 1 }
```



If we now, from the MariaDB prompt, check the users we will see:



```
MariaDB [(none)]> select user, host from mysql.user;
+-------------+-----------+
| User        | Host      |
+-------------+-----------+
| bob         | %         |
| test.bob    | %         |
| mysql       | localhost |
+-------------+-----------+
3 rows in set (0.001 sec)
```



The MariaDB user corresponding to the NoSQL user `<code>bob</code>`, created in the
context of the database `<code>test</code>`, has `<code>test</code>` as a prefix.


### The `<code>mariadb</code>` database


The fact that NoSQL users have the database embedded in the MariaDB
name may be inconvenient if the same data is accessed both as NoSQL
via nosqlprotocol and as SQL directly from MariaDB. It also makes
it impossible to use an existing MariaDB account from NoSQL.


To provide a solution for this problem, the database `<code>mariadb</code>` is treated
in a specific fashion. A user created in the context of the `<code>mariadb</code>`
database is created in the MariaDB server without the database prefix.
If we now try to create a user `<code>bob</code>` in the `<code>mariadb</code>` database it will fail,
because the user `<code>'bob'@'%'</code>` exists already.



```
> use mariadb
switched to db mariadb
> db.runCommand({createUser: "bob", pwd: "bobspwd", roles: []});
{
    "ok" : 0,
    "errmsg" : "User \"bob\" already exists",
    "code" : 51003,
    "codeName" : "Location51003"
}
```



If we create a user with another name it will succeed.



```
> db.runCommand({createUser: "alice", pwd: "alicespwd", roles: []});
{ "ok" : 1 }
```



And if we check the situation from MariaDB,



```
MariaDB [(none)]> select user, host from mysql.user;
+-------------+-----------+
| User        | Host      |
+-------------+-----------+
| alice       | %         |
| bob         | %         |
| test.bob    | %         |
| mysql       | localhost |
+-------------+-----------+
4 rows in set (0.001 sec)
```



we will see that `<code>alice</code>` was created without a database prefix.


## Roles and Privileges


When creating a user nosqlprotocol accepts all roles as predefined by
MongoDB®, but not all of them are translated into GRANT privileges.
The following table shows what privilege(s) a particular role is
converted to.


| Role | Privileges |
| --- | --- |
| Role | Privileges |
| dbAdmin | ALTER, CREATE, DROP, SHOW DATABASES, SELECT |
| read | SELECT |
| readWrite | CREATE, DELETE, INDEX, INSERT, SELECT, UPDATE |
| userAdmin | CREATE USER, GRANT OPTION |


The following roles are shorthands for several other roles.


| Role | Shorthand for |
| --- | --- |
| Role | Shorthand for |
| dbOwner | dbAdmin, readWrite, userAdmin |
| root | dbAdmin, readWrite, userAdmin |


`<code>dbOwner</code>` differs from `<code>root</code>` in that the privileges of the former
apply only to a particular database, while the privileges of the
latter apply to *all* databases. However, the role `<code>root</code>` can
only be assigned to a user in the `<code>admin</code>` database.


In addition there are `<code>AnyDatabase</code>` versions of `<code>dbAdmin</code>`, `<code>read</code>` and
`<code>readWrite</code>` (e.g `<code>readAnyDatabase</code>`) that can be assigned to a user in
the `<code>admin</code>` database. If so, then the privilege is granted on `<code>*.*</code>`,
otherwise on `<code><db>.*</code>`.


If the `<code>root</code>` role is assigned to a user in the `<code>admin</code>` database,
then the privileges are granted on `<code>*.*</code>`, otherwise on `<code><db>.*</code>`.


Other pre-defined roles are recognized and stored in the local
nosqlprotocol account database, but they do not affect what privileges
are granted to the MariaDB user. Currently user-defined roles are
not supported.


## Client Authentication


Authenticationwise nosqlprotocol can be used in three different ways:
- Anonymously
- Shared credentials
- Unique credentials


### Anonymously


If there is an anonymous user on the MariaDB server and if nosqlprotocol
is configured without a user/password, then all nosqlprotocol clients will
access the MariaDB server as anonymous users.


Note that the anonymous MariaDB user is only intended for testing and
should in general not be used, but deleted.


### Shared Credentials


If nosqlprotocol is configured with



```
...
nosqlprotocol.user=theuser
nosqlprotocol.password=thepassword
```



then each MongoDB® client will use those credentials when accessing the
MariaDB server. Note that from the perspective of the MariaDB server, it
is not possibe to distinguish between different MongoDB® clients.


### Unique Credentials


If nosqlprotocol authentication has been taken into use and a MongoDB®
client authenticates, either when connecting or later, then the credentials
of MongoDB® client will be used when accessing the MariaDB server.


Note that even if nosqlprotocol authentication has been enabled, authentication
is not required, and if the MongoDB® client has not authenticated itself, the
credentials specified with `<code>nosqlprotocol.[user|password]</code>` (or the anonymous
user) will be used when accessing the MariaDB server.


### Enforce Authentication


To enforce authentication, specify



```
nosqlprotocol.authentication_required=true
```



in the configuration. If authentication is required, then any command
that requires access to the MariaDB server will fail, unless the client
has authenticated.


## Authorization


By default nosqlprotocol does no authorization. However, a nosqlprotocol
client is *always* subject to the authorization performed by the MariaDB
server.


When nosqlprotocol authorization is enabled by adding



```
nosqlprotocol.authorization_enabled=true
```



to the configuration file, some commands will be subject to authorization,
by nosqlprotocol. The following table lists the commands and what role they
require.


| Command | Role |
| --- | --- |
| Command | Role |
| [createUser](#createUser) | userAdmin |
| [dropUser](#dropUser) | userAdmin |
| [grantRolesToUser](#grantRolesToUser) | userAdmin |
| [revokeRolesFromUser](#revokeRolesFromUser) | userAdmin |
| [mxsAddUser](#mxsAddUser) | userAdmin |
| [mxsRemoveUser](#mxsRemoveUser) | userAdmin |
| [mxsUpdateUser](#mxsUpdateUser) | userAdmin |
| [updateUser](#updateUser) | userAdmin |
| [usersInfo](#usersInfo) | userAdmin |


It is important to note that even if nosqlprotocol authorization
is enabled, the MariaDB server has the final word. That is, even if the
roles of a user would be sufficient for a particular operation, if the
granted privileges are not, the operation will not succeed. There may
be a mismatch between roles and grants, for instance, if the wrong roles
were specified when the user was added, or if the grants have been
altered directly and not via nosqlprotocol.


## Bootstrapping the Authentication/Authorization


The authentication/authorization can be bootstrapped explicitly
or implicitly. Bootstrapping explicitly provides more control, while
bootstrapping implicitly is much more convenient.


### Explicit bootstrapping


In order to enable authorization you need to have NoSQL users and
those can be created with [createUser](#createUser) or added
with [mxsAddUser](#addUser).


If you want to *create* a user, then you first need to configure
nosqlprotocol with credentials that are sufficient for creating a user:



```
nosqlprotocol.user = user_with_privileges_for_creating_a_user
nosqlprotocol.password = the_users_password
```



At this point `<code>nosqlprotocol.authentication_required</code>` and
`<code>nosqlprotocol.authorization_enabled</code>` should both be `<code>false</code>`. Note that
as those are their default values, they do not have to be specified.


Start MaxScale and connect to it with the MongoDB® command line client



```
$ mongo --port 17017
...
>
```



Then create the user.



```
> use admin;
switched to db admin
> db.runCommand({createUser: "nosql_admin", pwd: "nosql_pwd", roles: ["userAdmin"]});
{ "ok" : 1 }
```



Alternatively you can add an existing user. Note that it should be
added to the `<code>mariadb</code>` database, unless it was created with the
convention of having the database as a prefix, e.g. `<code>db.bob</code>`.



```
> use mariadb;
switched to db admin
> db.runCommand({mxsAddUser: "bob", pwd: "bob_pwd", roles: ["userAdmin"]});
{ "ok" : 1 }
```



Now you should shutdown MaxScale and add the entries



```
nosqlprotocol.authentication_required=true
nosqlprotocol.authorization_enabled=true
```



and start MaxScale.


The `<code>nosqlprotocol.user</code>` and `<code>nosqlprotocol.password</code>` can be removed but
as they will be ignored with `<code>nosqlprotocol.authentication_required=true</code>`
being present, it is not mandatory.


If you now try to create a user when not having been authenticated or
when authenticated as a user without the `<code>userAdmin</code>` role, the result
will be:



```
> use test;
switched to db test
> db.runCommand({createUser: "alice", pwd: "alices_pwd", roles: []});
{
    "ok" : 0,
    "errmsg" : "command createUser requires authentication",
    "code" : 13,
    "codeName" : "Unauthorized"
}
```



**NOTE** When a client authenticates, the password will not be
transferred in cleartext over the network, so, even without SSL,
it is not possible to gain access to a password by monitoring the
network traffic.


However, when a user is created or added (or the password is changed),
the password will be transferred in *cleartext*. To prevent eavesdropping,
create/add users when connecting over a domain socket, or use
[TLS/SSL](#tlsssl)


### Implicit bootstrapping


With implicit bootstrapping, you should first create the MariaDB
user that should appear as the initial NoSQL user. As explained
[here](#nosql-and-mariadb-users), the concept of a user is somewhat
different in MariaDB and NoSQL, which means that certain factors
must be taken into account when creating the MariaDB user. Then
at first startup, nosqlprotocol will create the corresponding
NoSQL user, which will enable the authenticated and authorized
use of nosqlprotocol.


When MaxScale is started, if the following hold


* `<code>nosqlprotocol.authentication_required</code>` and
 `<code>nosqlprotocol.authorization_enabled</code>` are true in the configuration
 section of the nosqlprotocol listener,
* `<code>nosqlprotocol.user</code>` and `<code>nosqlprotocol.password</code>` are provided, and
* there are no NoSQL users in the NoSQL account database.


then, MaxScale will


* wait until the primary of the service pointed to by the listener
 is available,
* connect using the credentials specified in `<code>nosqlprotocol.user</code>`
 and `<code>nosqlprotocol.password</code>`,
* execute `<code>SHOW GRANTS</code>`,
* translate the privileges into the equivalent NoSQL roles, and
* create a corresponding NoSQL user into the NoSQL account database.


Immediately thereafter it is possible to connect to the nosqlprotocol
port with a MongoDB® client using the specified credentials.


Note that after the bootstrapping, nosqlprotocol will not use
the `<code>user</code>` and `<code>password</code>` settings and they can be removed.


#### Grants


When a NoSQL user is created using [createUser](#createUser)
the MariaDB grants are obtained from the specified NoSQL roles
as explained [here](#Roles_and_privileges).


When implicitly creating a NoSQL user from an existing user in
MariaDB, the inverse operation must be performed. There are
many factors that affect what NoSQL roles the grants of a user
are translated into:


* whether the user is a regular or admin user,
* whether the privileges are on `<code>*.*</code>` or some specific `<code>db.*</code>`, and
* the privileges themselves, e.g. `<code>SELECT</code>`, `<code>DELETE</code>`, etc.


In NoSQL, every user resides in a specific database. Note that
this does **not** mean that that database would have to exist
in MariaDB.


When it comes to users, the database effectively means a scope,
which in the case of nosqlprotocol is handled by prefixing the
corresponding MariaDB user name with the database/scope name.


When creating a user to be used from NoSQL, there are three
options for the user's name:


* The name can be of the format `<code>some_db.user_name</code>` where
 `<code>some_db</code>` can be anything (subject to the naming rules of
 MariaDB), except `<code>admin</code>` or `<code>mariadb</code>`. In this case, the
 user will be a regular user, who can access data in
 databases that she has been granted access to.
* The name can be of the format `<code>admin.user_name</code>` where `<code>admin</code>`
 is exactly just that. In this case, the user will be an
 admin user, who can access any database.
* The name can be of the format `<code>user_name</code>`. In this case, the
 user will be a regular user that from the NoSQL side appears
 to reside in the `<code>mariadb</code>` database. The primary purpose of
 this alternative is to enable the use of existing users from
 the NoSQL side.


What database the privileges can be specified `<code>ON</code>` depends on
what kind of user is being created.


* If it is a regular user, the privileges must be granted on a
 specific database, such as `<code>\</code>`dbA``<code>.*</code>`. Note that there is no
 dependency between this database and the (conceptual) database
 the user resides in.
* If it is an admin user, the privileges must be granted on
 the `<code>*.*</code>` database.


In NoSQL, a role can be database specific or generic. However,
a generic role can *only* be assigned to a user in the *admin*
database. In practice this means that if the privileges are
on `<code>*.*</code>`, then the user must reside in the *admin* database
(e.g. `<code>admin.bob</code>`) or it is treated as an error.


The following table shows what privileges are required for a
role to be assigned. Note that `<code>ALL PRIVILEGES</code>` can be used as
well.


| ALTER | CREATE | CREATE USER | DROP | DELETE | INDEX | INSERT | SHOW DATABASES(1) | SELECT | UPDATE | WITH GRANT OPTION | Role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ALTER | CREATE | CREATE USER | DROP | DELETE | INDEX | INSERT | SHOW DATABASES(1) | SELECT | UPDATE | WITH GRANT OPTION | Role |
| X | X |  | X |  |  |  | X | X |  |  | dbAdmin[AnyDatabase] |
|  |  |  |  |  |  |  |  | X |  |  | read[AnyDatabase] |
|  | X |  |  | X | X | X |  | X | X |  | readWrite[AnyDatabase] |
|  |  | X |  |  |  |  |  |  |  | X | userAdmin[AnyDatabase] |


1. Only required if the user is an admin user.


The `<code>AnyDatabase</code>` version will be assigned, if the user is
an *admin* user.


If certain roles are assigned, then other roles will be
assigned as well.


* If the roles `<code>dbAdmin</code>`, `<code>readWrite</code>` and `<code>userAdmin</code>` are
 assigned, then `<code>dbOwner</code>` will be assigned as well.
* If the roles `<code>dbAdminAnyDatabase</code>`, `<code>readWriteAnyDatabase</code>`
 and `<code>userAdminAnyDatabase</code>` are assigned, then `<code>root</code>` will
 be assigned as well.


Once the user has been created and the desired privileges have
been granted, the NoSQL listener should be configured as follows:



```
[NoSQL-Listener]
...
nosqlprotocol.user=db.the_user
nosqlprotocol.password=the_password
nosqlprotocol.authentication_required=true
nosqlprotocol.authorization_enabled=true
...
```



At MaxScale startup, the NoSQL user will then be created.


#### Examples


##### Admin User


We want the initial NoSQL user to be an administrator, with
full rights.



```
CREATE USER 'admin.nosql_admin'@'%' IDENTIFIED BY 'nosql_password';
GRANT ALL PRIVILEGES ON *.* TO 'admin.nosql_admin'@'%' WITH GRANT OPTION;
```



As we want an admin user, the name is prefixed with `<code>admin</code>`,
which will have that effect. And since it is an admin user, the
privileges are granted ON `<code>*.*</code>`.


Thereafter, we specify the following in the configuration file,



```
[NoSQL-Listener]
type=listener
service=...
protocol=nosqlprotocol
nosqlprotocol.user=admin.nosql_admin
nosqlprotocol.password=nosql_password
nosqlprotocol.authentication_required=true
nosqlprotocol.authorization_enabled=true
```



and start MaxScale.


As the creation of the initial user can be made only after the
monitor for the listener's service has marked one server as primary,
whether the creation succeeded or not must be checked from MaxScale'
log file:



```
... notice : [nosqlprotocol] Created initial NoSQL user 'admin.nosql_admin'.
```



Under normal conditions, the bootstrapping will be almost
instantaneous.


It is now possible to connect using any MongoDB® client application.



```
$ mongo --quiet --port 17017 -u nosql_admin -p nosql_password admin
>
```



Note that when connecting the user is passed as `<code>nosql_admin</code>` and *not*
as `<code>admin.nosql_admin</code>`. The fact that we want to authenticate against
the `<code>admin</code>` database is expressed by passing the database as the last
argument.



```
> db.runCommand({usersInfo: 1});
{
    "users" : [
        {
            "_id" : "admin.nosql_admin",
            "userId" : UUID("7d921459-3099-42a7-ad06-ed37ac002161"),
            "user" : "nosql_admin",
            "db" : "admin",
            "roles" : [
                {
                    "db" : "admin",
                    "role" : "dbAdminAnyDatabase"
                },
                {
                    "db" : "admin",
                    "role" : "readWriteAnyDatabase"
                },
                {
                    "db" : "admin",
                    "role" : "userAdminAnyDatabase"
                },
                {
                    "db" : "admin",
                    "role" : "root"
                }
            ],
            "mechanisms" : [
                "SCRAM-SHA-256"
            ]
        }
    ],
    "ok" : 1
}
```



As can be seen, the user has the *any* roles on the `<code>admin</code>`
database, which means that all databases can be accessed and
modified, and that new users can be created.


##### Test User


We want the initial NoSQL user to be a user with limited rights,
intended to be used for testing.



```
CREATE USER 'test.test_user'@'%' IDENTIFIED BY 'test_password';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, INDEX ON `test`.* TO 'test.test_user'@'%';
```



As we want a user with limited rights, the name is *not* prefixed
with `<code>admin</code>`. The privileges are granted specifically on database
`<code>test.*</code>`. Indeed, if `<code>*.*</code>` had been used, the creation of the initial
NoSQL user would have failed with an error. Here, the user is created
in the same database that the user is given access to, but it could
have been another one. Further, several `<code>GRANT</code>` statements could have
been used, had we wanted to give access to several databases.


Thereafter, we specify the following in the configuration file,



```
[NoSQL-Listener]
type=listener
service=...
protocol=nosqlprotocol
nosqlprotocol.user=test.test_user
nosqlprotocol.password=test_password
nosqlprotocol.authentication_required=true
nosqlprotocol.authorization_enabled=true
```



and start MaxScale.


As the creation of the initial user can be made only after the
monitor for the listener's service has marked one server as primary,
whether the creation succeeded or not must be checked from MaxScale'
log file:



```
... notice : [nosqlprotocol] Created initial NoSQL user 'test.test_user'.
```



Under normal conditions, the bootstrapping will be almost
instantaneous.


It is now possible to connect using any MongoDB® client application.



```
$ mongo --quiet --port 17017 -u test_user -p test_password test
>
```



Note that when connecting the user is passed as `<code>test_user</code>` and *not*
as `<code>test.test_user</code>`. The fact that we want to authenticate against
the `<code>test</code>` database is expressed by passing the database as the last
argument.



```
> db.runCommand({usersInfo: 1});
{
    "users" : [
        {
            "_id" : "test.test_user",
            "userId" : UUID("714f35e7-4276-45af-863c-0be4d1f5dd74"),
            "user" : "test_user",
            "db" : "test",
            "roles" : [
                {
                    "db" : "test",
                    "role" : "readWrite"
                }
            ],
            "mechanisms" : [
                "SCRAM-SHA-256"
            ]
        }
    ],
    "ok" : 1
}
```



As can be seen, the user has the `<code>readWrite</code>` role on the `<code>test</code>` database,
which means that only the `<code>test</code>` database can be accessed and modified.


### TLS/SSL


Since `<code>nosqlprotocol</code>` is a regular protocol module used in a listener,
the TLS/SSL support of listeners is available. Please see
[TSLSSL encryption](https://mariadb.com/kb/en/Getting-Started/Configuration-Guide#tsl-encryption)
for details.


## NoSQL Account Database


So as to be able to connect to the MariaDB server on behalf of
clients, nosqlprotocol must know their password. As the password
is not transferred to nosqlprotocol during the authentication in
a way that could be used when logging into MariaDB, the password
must be stored when the user is created with [createUser](#createUser)
or added with [mxsAddUser](#mxsAddUser).


Note that the password is not stored in cleartext but as three
different hashes; hashed with sha1 for use with MariaDB, salted
and hashed with sha1 for use with the `<code>SCRAM-SHA-1</code>` authentication
mechanism (if that is enabled for the user) and salted and hashed
with sha256 for use with the `<code>SCRAM-SHA-256</code>` authentication mechanism
(if that is enabled for the user).


The account information can be stored *privately*, in which case it
can be used only by a particular MaxScale instance, or in a
*shared* manner, in which case multiple MaxScale instances can
share the information and a user created/added on one instance
can be used on another.


### Private


In the private case, the account information of nosqlprotocol is
stored in an [sqlite3](https://sqlite.org/index.html) database
whose name is `<code><libdir>/nosqlprotocol/<listener-name>-v1.db</code>`,
where `<code><libdir></code>` is the *libdir* of MaxScale, typically
`<code>/var/lib/maxscale</code>`, `<code><listener-name></code>` is the name of the
listener section in the MaxScale configuration file, and `<code>-v1</code>`
a suffix for making schema evolution easier, should there be
a need for that.


For instance, given a configuration like



```
[NoSQL-Listener]
type=listener
service=TheService
protocol=nosqlprotocol
...
```



the account information will be stored in the file
`<code><libdir>/nosqlprotocol/NoSQL-Listener-v1.db</code>`.


Note that since the database name is derived from the listener
name, changing the name of the listener in the configuration
file will have the effect of making all accounts disappear.
To retain the accounts, the database file should also be
renamed.


At first startup, the `<code>nosqlprotocol</code>` directory and
the file `<code>NoSQL-Listener-v1.db</code>` will be created. They will
be created with file permissions that only allow MaxScale
access. At subsequent startups the permissions will be checked
and MaxScale will refuse to start if the permissions allow
access to others.


**We strongly recommend that no manual modifications are made
to the database.**


Note that we make **no** guarantees that the way in which the
account information is stored by `<code>nosqlprotocol</code>` will remain the
same *even* between maintenance releases. We do guarantee,
however, that even if the way in which the account information is
stored changes, existing account information will automatically
be converted and no manual intervention, such as re-creation of
accounts, will be needed.


## Shared


In the shared case, the account information of nosqlprotocol
is stored in the cluster of the service in front of which the
NoSQL listener resides. The primary of the cluster will be used
both for reading and writing data.


A table whose name is the same as the listener's name in the
MaxScale configuration will be created in the database
specified with the [authentication_db](#authentication_db)
parameter. If it is not specified explicitly, the default is
`<code>nosqlprotocol</code>`. The name of the table will be the name of
the listener section in the MaxScale configuration file.


For instance, given a configuration like



```
[NoSQL-Listener]
type=listener
service=TheService
protocol=nosqlprotocol
...
```



the account information will be stored in the table
`<code>nosqlprotocol.NoSQL-Listener</code>`.


Note that since the table name is derived from the listener
name, changing the name of the listener in the configuration
file will have the effect of making all accounts disappear.
To retain the accounts, the table should also be renamed.


`<code>nosqlprotocol</code>` will create the table when needed, so the
user specified with [authentication_user](#authentication_user)
must have sufficient grants to be able to do that.


`<code>nosqlprotocol</code>` will store in the table, data that allow
any MaxScale to authenticate a MongoDB® client, irrespective
of which MaxScale instance was used when the user was created.


`<code>nosqlprotocol</code>` also stores in the table the SHA1 of a user's
password, to be able to authenticate against the MariaDB server.
Therefore it is **strongly** suggested to enable encryption key
management in MaxScale and to provide an authentication
key ID with [authentication_key_id](#authentication_key_id) so
that the data will be encrypted.


If shared authentication has been enabled with
[authentication_shared](#authentication_shared) then
[authentication_user](#authentication_user) and
[authentication_password](#authentication_password) must also
be provided. With [authentication_db](#authentication_db) the
database name can optionally be changed, and with
[authentication_key_id](#authentication_key_id) an
encryption key ID, using which the sensitive data is encrypted,
can optionally be provided.


Note that we make **no** guarantees that the table in which the
account information is stored by `<code>nosqlprotocol</code>` will remain the
same *even* between maintenance releases. We do guarantee,
however, that even if the way in which the account information is
stored changes, existing account information will automatically
be converted and no manual intervention, such as re-creation of
accounts, will be needed.


# Wire Protocol


*Nosqlprotocol* fully supports wire protocol version 6 and only provides
rudimentary support for earlier wire protocol versions, but reports at
startup that it would support versions 0 to 6. The reason is that some
client libraries are buggy and use an old wire protocol version if the
server claims to support only version 6. Consequently, one should use a
client library version that at least supports wire protocol version 6.


# Client Library


As the goal of *nosqlprotocol* is to implement, to the extent that it
is feasible, the wire protocol and the database commands the way MongoDB®
implements them, it should be possible to use any language specific driver.


However, during the development of *nosqlprotocol*, the *only* client library
that has been verified to work is version 3.6 of *MongoDB Node.JS Driver*.


# Parameters


Using the following parameters, the behavior of *nosqlprotocol* can be
adjusted. As they are not generic listener parameters, but specific to
*nosqlprotocol* they must be qualified with the `<code>nosqlprotocol</code>`-prefix.


For instance:



```
[NoSQL-Listener]
type=listener
service=TheService
protocol=nosqlprotocol
nosqlprotocol.user=the_user
nosqlprotocol.password=the_password
nosqlprotocol.on_unknown_command=return_error
...
```



## `<code>user</code>`


* Type: string
* Mandatory: No
* Default: `<code>""</code>`


Specifies the *user* to be used when connecting to the backend, if the MongoDB®
client is not authenticated.


## `<code>password</code>`


* Type: string
* Mandatory: No
* Default: `<code>""</code>`


Specifies the *password* to be used when connecting to the backend, is the MongoDB®
client is not authenticated. Note that the same *user*/*password* combination will be
used for all unauthenticated MongoDB® clients connecting to the same listener port.


## `<code>authentication_required</code>`


* Type: [boolean](../mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `<code>false</code>`


Specifies whether the client always must authenticate. If authentication is required,
it does not matter whether `<code>user</code>` and `<code>password</code>` have been specified, the client must
authenticate.


Authentication should not be required before users have been created with
[createUser](#createUser) or added with [mxsAddUser](#mxsAddUser),
with authentication being optional and authorization being disabled.


NOTE: All client activity is *always* subject to authorization performed by the
MariaDB server.


## `<code>authentication_shared</code>`


* Type: [boolean](../mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `<code>false</code>`


Specifies whether the NoSQL account information should be stored in a shared
manner or privately.


## `<code>authentication_db</code>`


* Type: string
* Mandatory: No
* Default: `<code>"NoSQL"</code>`


Specifies the database of the table where the NoSQL account information
is stored, if `<code>authentication_shared</code>` is `<code>true</code>`. If the database does not
exist, nosqlprotocol will attempt to create it, so either is should be
manually created or the used specified with `<code>authentication_user</code>` should
have the grants required to do so.


## `<code>authentication_key_id</code>`


* Type: string
* Mandatory: No
* Default: `<code>""</code>`


The encryption key ID, using which the NoSQL account information should be
encrypted with when stored in the MariaDB server. If an encryption key ID is
given, the encryption key manager in MaxScale must also be enabled.


The encryption key must be a 256-bit key. Keys of shorter length are rejected
as invalid encryption keys.


## `<code>authentication_user</code>`


* Type: string
* Mandatory: Yes, if `<code>authentication_shared</code>` is true.


Specifies the *user* to be used when modifying and accessing the NoSQL
account information stored in the MariaDB server.


## `<code>authentication_password</code>`


* Type: string
* Mandatory: No
* Default: `<code>""</code>`


Specifies the *password* of `<code>authentication_user</code>`.


## `<code>authorization_enabled</code>`


* Type: [boolean](../mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `<code>false</code>`


Specifies whether nosqlprotocol itself should perform authorization in the context
of the commands [mxsAddUser](#mxsAddUser), [mxsRemoveUser](#mxsRemoveUser) and
[mxsUpdateUser](#mxsUpdateUser). Authorization should not be enabled before users
have been created with [createUser](#createUser) or added with [mxsAddUser](#mxsAddUser)
with authorization being disabled.


NOTE: All client activity is *always* subject to authorization performed by the
MariaDB server.


## `<code>host</code>`


* Type: string
* Mandatory: No
* Default: `<code>"%"</code>`


Specifies the *host* to be used when a MariaDB user is created via nosqlprotocol.
By default all users are created as `<code>...@'%'</code>`, which means that it is possible to
connect to the MariaDB server from any host using the credentials of the created
user. For tighter security, the IP-address of the MaxScale host can be specified.


NOTE: This value does **not** specify from which host it is allowed to connect to
MaxScale.


## `<code>on_unknown_command</code>`


* Type: [enum](../mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Values: `<code>return_error</code>`, `<code>return_empty</code>`
* Default: `<code>return_error</code>`


Specifies what should happen in case a clients sends an unrecognized command.


Enumeration values:


* `<code>return_error</code>`: An error document is returned.
* `<code>return_empty</code>`: An empty document is returned.


## `<code>log_unknown_command</code>`


* Type: [boolean](../mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `<code>false</code>`


Specifies whether an unknown command should be logged. This is primarily
for debugging purposes, to find out whether a client uses a command that
currently is not supported.


## `<code>auto_create_databases</code>`


* Type: [boolean](../mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `<code>true</code>`


Specifies whether databases should automatically be created, as needed.


Note that setting this parameter to `<code>true</code>`, without also setting
`<code>auto_create_tables</code>` to `<code>true</code>`, has no effect at all.


## `<code>auto_create_tables</code>`


* Type: [boolean](../mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `<code>true</code>`


Specifies whether tables should automatically be created, as needed.


Note that this applies only if the relevant database already exists.
If a database should also be created if needed, then `<code>auto_create_databases</code>`
must also be set to `<code>true</code>`.


## `<code>id_length</code>`


* Type: count
* Mandatory: No
* Range: `<code>[35, 2048]</code>`
* *Default: `<code>35</code>`


Specifies the length of the id column in tables that are automatically created.


## `<code>ordered_insert_behavior</code>`


* Type: [enum](../mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Values: `<code>atomic</code>`, `<code>default</code>`
* Default: `<code>default</code>`


Enumeration values:


* `<code>default</code>`: Each document is inserted using a separate `<code>INSERT</code>`, either in a
 multi-statement or in a compound statement. Whether an error causes the remaining
 insertions to be aborted, depends on the value of `<code>ordered</code>` specified in the
 insert command.
* `<code>atomic</code>`: If the value of `<code>ordered</code>` in the insert command is `<code>true</code>`
 (the default) then all documents are inserted using a single `<code>INSERT</code>` statement,
 that is, either all insertions succeed or none will. If `<code>ordered</code>` is false, then
 the behavior is as in the `<code>default</code>` case.


What combination of `<code>ordered_insert_behavior</code>` and `<code>ordered</code>` (in the insert command
document) is used, has an impact on the performance. Please see the discussion at
[insert](#insert).


## `<code>cursor_timeout</code>`


* Type: [duration](../mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#durations)
* Mandatory: No
* Default: `<code>60s</code>`


Specifies how long a cursor can be idle, that is, not accessed, before it is
automatically closed.


## `<code>debug</code>`


* Type: [enum_mask](../mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Values: `<code>none</code>`, `<code>in</code>`, `<code>out</code>`, `<code>back</code>`
* Default: `<code>none</code>`


Specifies what should be logged as *notice* messages.


Enumeration values:


* `<code>none</code>`: Nothing is logged.
* `<code>in</code>`: The incoming protocol command is logged.
* `<code>out</code>`: The outgoing SQL sent to the backend is logged.
* `<code>back</code>`: The response sent back to the client is logged.


So, specify



```
nosqlprotocol.debug=in,out,back
```



to have the incoming command, the corresponding SQL sent to the backend
and the resulting response sent to the client logged.


# Databases and Tables


By default, *nosqlprotocol* automatically creates databases as needed.
The default behavior can be changed by setting `<code>auto_create_databases</code>` to
false. In that case, databases must manually be created.


Each MongoDB® *collection* corresponds to a MariaDB table with the same name.
However, it is always possible to access a collection irrespective of whether
the corresponding table exists or not; it will simply appear to be empty.


Inserting documents into a collection, whose corresponding table does not
exist, succeeds, provided `<code>auto_create_tables</code>` is `<code>true</code>`, as the table will
in that case be created.


When *nosqlprotocol* creates a table, it uses a statement like



```
CREATE TABLE name (id VARCHAR(35) AS (JSON_COMPACT(JSON_EXTRACT(doc, "$._id"))) UNIQUE KEY,
                   doc JSON,
                   CONSTRAINT id_not_null CHECK(id IS NOT NULL));
```



where the length of the `<code>VARCHAR</code>` is specified by the value of `<code>id_length</code>`,
whose default and minimum is 35.


*NOTE* If the tables are created manually, then the `<code>CREATE</code>` statement
*must* contain a similar `<code>AS</code>`-clause as the one above and *should* contain
a similar constraint.


Note that *nosqlprotocol* does not in any way verify that the table
corresponding to a collection being accessed or modified does indeed
have the expected columns `<code>id</code>` and `<code>doc</code>` of the expected types, but it
simply uses the table, which will fail if the layout is not the expected
one.


To reduce the risk for confusion, the recommendation is to use a specific
database for tables that contain documents.


# Operators


The following operators are currently supported.


## Query and Projection Operators


### Comparison Query Operators


* $eq
* $gt
* $gte
* $in
* $lt
* $lte
* $ne
* $nin


### Logical Query Operators


* $and
* $not
* $nor
* $or
* $alwaysFalse
* $alwaysTrue


### Element Query Operators


* $exists
* $type


#### `<code>$type</code>`


When `<code>$type</code>` is used, it will be converted into a condition involving one or more
[JSON_TYPE](../../../server/reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/json-functions/json_type.md) comparisons. The following subset
of types can be used in `<code>$type</code>` queries:


| Type | Number | Alias | MariaDB Type |
| --- | --- | --- | --- |
| Type | Number | Alias | MariaDB Type |
| Double | 1 | "double" | DOUBLE |
| String | 2 | "string" | STRING |
| object | 3 | "object" | OBJECT |
| Array | 4 | "array" | ARRAY |
| Boolean | 5 | "bool" | BOOLEAN |
| 32-bit integer | 16 | "int" | INTEGER |


The *"number"* alias is supported and will match values whose MariaDB type is
`<code>DOUBLE</code>` or `<code>INTEGER</code>`.


### Evaluation Query Operators


* $mod
* $regex


### Array Query Operators


* $all
* $elemMatch
* $size


#### `<code>$elemMatch</code>`


As arguments, only the operators `<code>$eq</code>` and `<code>$ne</code>` are supported.


## Update Operators


### Field Update Operators


* $bit
* $currentDate
* $inc
* $max
* $min
* $mul
* $pop
* $push
* $rename
* $set
* $unset


# Database Commands


The following commands are supported. At each command is specified
what fields are relevant for the command.


**All** non-listed fields are ignored; their presence or absence have no
impact, unless otherwise explicitly specified.


## Aggregation Commands


### count


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| count | string | The name of the collection to count. |
| query | document | Optional. A query that selects which documents to count in the collection |
| limit | integer | Optional. The maximum number of matching documents to return. |
| skip | integer | Optional. The number of matching documents to skip before returning results. |


### distinct


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| distinct | string | The name of the collection to query for distinct values. |
| key | string | The field for which to return distinct values. |
| query | document | Optional. A query that selects which documents to count in the collection |


## Query and Write Operation Commands


### delete


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| delete | string | The name of the target table. |
| deletes | array | An array of one or more delete statements to perform in the named collection. |
| ordered | boolean | Optional. If true, then when a delete statement fails, return without performing the remaining delete statements. If false, then when a delete statement fails, continue with the remaining delete statements, if any. Defaults to true. |


Each element of the deletes array contains the following fields:


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| q | document | The query that matches documents to delete. |
| limit | integer | The number of matching documents to delete. Specify either a 0 to delete all matching documents or 1 to delete a single document. |


### find


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| find | string | The name of the target table. |
| filter | document | Optional. The query predicate. If unspecified, then all documents in the collection will match the predicate. |
| sort | document | Optional. The sort specification for the ordering of the results. |
| projection | document | Optional. The projection specification to determine which fields to includein the returned documents. |
| skip | Positive integer | Optional. Number of documents to skip. Defaults to 0. |
| limit | Non-negative integer | Optional. The maximum number of documents to return. If unspecified, then defaults to no limit. A limit of 0 is equivalent to setting no limit. |
| batchSize | Non-negative integer | Optional. The number of documents to return in the first batch. Defaults to 101. A batchSize of 0 means that the cursor will be established, but no documents will be returned in the first batch. |
| singleBatch | boolean | Optional. Determines whether to close the cursor after the first batch. Defaults to false. |


All other fields are ignored.


#### Projection


The `<code>projection</code>` parameter determines which fields are returned in the matching documents.
The `<code>projection</code>` parameter takes a document of the following form:



```
{ <field1>: <value>, <field2>: <value> ... }
```



If a `<code>projection</code>` document is not provided or if it is empty, the entire document
will be returned.


| Projection | Description |
| --- | --- |
| Projection | Description |
| <field>: <1 or true> | Specifies the inclusion of a field. |
| <field>: <0 or false> | Specifies the exclusion of a field. |


##### Embedded Field Specification


For fields in an embedded documents, the field can be specified using:


* dot notation; e.g. `<code>"field.nestedfield": <value></code>`


In particular, specifying fields in embedded documents using nested form
is not supported.


##### `<code>_id</code>` Field Projection


The `<code>_id</code>` field is included in the returned documents by default unless you
explicitly specify `<code>_id: 0</code>` in the projection to suppress the field.


#### Inclusion or Exclusion


A `<code>projection</code>` cannot contain both include and exclude specifications,
with the exception of the `<code>_id</code>` field:


* In projections that explicitly include fields, the `<code>_id</code>` field is the only field that can be explicitly excluded.
* In projections that explicitly excludes fields, the `<code>_id</code>` field is the only field that can be explicitly include; however, the `<code>_id</code>` field is included by default.


*NOTE* Currently `<code>_id</code>` is the only field that can be excluded, and *only*
if other fields are explicitly included.
*NOTE* Currently exclusion of other fields but `<code>_id</code>` is not supported.


#### Filtering by `<code>_id</code>`


Note that there is a significant difference between



```
> db.runCommand({find: "collection", filter: { _id: 4711 }});
```



and



```
> db.runCommand({find: "collection", filter: { _id: { $eq: 4711 }}});
```



In the former case the generated `<code>WHERE</code>` clause will be



```
... WHERE (id = '4711')
```



and in the latter



```
... WHERE (JSON_EXTRACT(doc, '$._id') = 4711)
```



That is, in the former case the *indexed* column `<code>id</code>` will be used, in the
latter it will not.


### findAndModify


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| findAndModify | string | The name of the target table. |
| query | document | Optional. The query predicate. |
| sort | document | Optional. The sort specification used when the document is selected. |
| remove | boolean | Mandatory, if update is not specified. If true, the document will be deleted. |
| update | document | Mandatory, if remove is not specified. See [Update.behavior](#behavior) for details. |
| new | boolean | Optional. If true the modified document and not the original document is returned. If remove is specified, then the original document is always returned. |
| fields | document | Optional. Specified which fields to return. See [Find.projection](#projection) for details. |
| upsert | boolean | Optional. If true then a document will be created, if one is not found. |


All other fields are ignored.


### getLastError


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| getLastError | any | Ignored. |


### getMore


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| getMore | long | The cursor id. |
| collection | string | The name of the collection over which the cursor is operating. |
| batchSize | positive integer | Optional. The number of documents to return in the batch. |


### insert


The `<code>insert</code>` command inserts one or more documents into the table whose
name is the same as that of the collection. If the option `<code>auto_create_tables</code>`
is `<code>true</code>`, then the table is created if it does not already exist. If the
value is `<code>false</code>`, then the insert will fail unless the table already exists.


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| insert | string | The name of the target collection (i.e. table). |
| documents | array | An array of one or more documents to be inserted to the named collection. |
| ordered | boolean | Optional, with default being true. See below for description. |


#### `<code>ordered</code>`


The impact of `<code>ordered</code>` is dependent upon the value of `<code>ordered_insert_behavior</code>`.


##### `<code>default</code>`


In this case `<code>ordered</code>` has the same impact as in MongoDB®. That is, if the value
is `<code>true</code>`, then when an insert of a document fails, return without inserting any
remaining documents listed in the inserts array. If `<code>false</code>`, then when an insert
of a document fails, continue to insert the remaining documents.


##### `<code>atomic</code>`


If `<code>ordered</code>` is `<code>true</code>`, then all documents will be inserted using a single
INSERT command. That is, if the insertion of any document fails, for instance,
due to a duplicate id, then no document will be inserted. If `<code>ordered</code>` is `<code>false</code>`,
then the behavior is identical with that of `<code>default</code>`.


#### Performance


What combination of `<code>ordered_insert_behavior</code>` and `<code>ordered</code>` is used, has an
impact on the performance.


| ordered_insert_behavior | ordered = true | ordered = false |
| --- | --- | --- |
| ordered_insert_behavior | ordered = true | ordered = false |
| default | All documents are inserted within a compound statement, in a transaction containing as many INSERT statements as there are documents. | All documents are inserted in a single multi-statement transaction containing as many INSERT IGNORE statements as there are documents. |
| atomic | All documents are inserted using a single INSERT statement. | Same as above |


Of these, `<code>atomic + true</code>` is the fastest and `<code>atomic|default + false</code>` the slowest,
being roughly twice as slow. The performance of 'default + true' is halfway between
the two.


### resetError


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| resetError | any | Ignored. |


### update


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| update | string | The name of the target table. |
| updates | array | An array of documents that describe what to updated. |


All other fields are ignored.


#### Update Statements


Each element of the updates array is an update statement document.
Each document contains the following fields:


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| q | document | The query that matches documents to update. |
| u | document | The modifications to apply. See behavior below for details. |
| multi | boolean | Optional. If true, updates all documents that meet the query criteria. If false limit the update to one document that meets the query criteria. Defaults to false. |


Note that currently it is possible to set `<code>multi</code>` to `<code>true</code>` in conjunction
with a *replacement-style* update, even though MongoDB® rejects that.


All other fields are ignored, with the exception of `<code>upsert</code>` that if present
with the value of `<code>true</code>` will cause the command to fail.


##### Behavior


Currently only updating using *update operator expressions* or with a
*replacement document* is supported. In particular, updating using an
*aggregation pipeline* is not supported.


###### Update with an Update Operator Expressions document


The update statement field `<code>u</code>` can accept a document that only contains
[update operator](#update-operators) expressions. For example:



```
updates: [
   {
     q: <query>,
     u: { $set: { status: "D" } },
      ...
   },
   ...
]
```



In this case, the update command updates only the corresponding fields in the document.


###### Update with a Replacement Document


The update statement field `<code>u</code>` field can accept a *replacement document*,
i.e. the document contains only `<code>field:value</code>` expressions. For example:



```
updates: [
   {
      q: <query>,
      u: { status: "D", quantity: 4 },
      ...
   },
   ...
]
```



In this case, the update command replaces the matching document with the update document.
The update command can only replace a single matching document; i.e. the multi field
cannot be true.


**Note** If the replacement document contains an `<code>_id</code>` field, it will be ignored and the
document id will remain non-changed while the document otherwise is replaced. This is
different from MongoDB® where the presence of the `<code>_id</code>` field in the replacement document
causes an error, if the value is not the same as it is in the document being replaced.


## Authentication Commands


### Logout


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| logout | any | Ignored. |


If you are not logged in and using authentication, `<code>logout</code>` has no effect.


Note that in order to be logged out, the logging out must be done while
using the same database that was used when you logged on.


Always returns



```
{ ok: 1 }
```



## User Management Commands


### createUser


Creates a new MariaDB user and adds an entry to the local nosqlprotocol
account database.


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| createUser | string | The name of the user to be added. |
| pwd | string | The password in cleartext. |
| customData | document | Optional. Any arbitrary information. |
| roles | array | The roles granted to the user. |
| mechanisms | array | Optional. The specific supported SCRAM mechanisms for this user. Must be a subset of the supported mechanisms. |
| digestPassword | boolean | Optional. If specified, must be true. |


The MariaDB user will be created as `<code>'<db>.<user>'@'%'</code>` where `<code><db></code>` is
the name of the NoSQL database in whose context the user is created, and
`<code><user></code>` the value of the `<code>createUser</code>` field. For instance, with the
following command



```
> use myDatabase;
> db.runCommand({createUser: "user1", pwd: "pwd1", roles: []});
```



the MariaDB user `<code>'myDatabase.user1'@'%'</code>` will be created.


The elements of the `<code>roles</code>` array are converted into privileges
as explained in [here](#roles_and_privileges).


In practice the creation is performed as follows:
*First the MariaDB user is created.* Then the privileges are granted.
* Finally the local nosqlprotocol account database is updated.


If the granting of privileges fails, an attempt will be made to
drop the user.


### dropAllUsersFromDatabase


Drops all users from the local nosqlprotocol account database and
the corresponding MariaDB users.


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| dropAllUsersFromDatabase | any | Ignored. |


If *no* users can be dropped, e.g. due to an authorization error,
then an error will be returned. If even a single user can be dropped
the returned document tells how many were dropped, which does not
necessarily indicate that *all* users were dropped.


### dropUser


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| dropUser | string | The name of the user to be dropped. |


The user will first be dropped from the MariaDB server and if
that succeeds also from the local nosqlprotocol account database.


### grantRolesToUser


This command *adds* more roles to a NoSQL user, which may imply
that additional privileges are granted to the corresponding MariaDB
user.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| grantRolesToUser | string | The name of the user to give additional roles. |
| roles | array | An array of additional roles. |


Note that roles assigned to different databases will result in separate
GRANT statements, which means that it is possible that some succeed and
others do not.


### revokeRolesFromUser


This command *removes* roles from an NoSQL user, which may imply
that privileges are revoked from the corresponding MariaDB user.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| revokeRolesFromUser | string | The name of the user to remove roles from. |
| roles | array | An array of roles to remove. |


Note that roles to be removed from different databases will result in
separate REVOKE statements, which means that it is possible that some
succeed and others do not.


### updateUser


This command updates the information about a particular user.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| updateUser | string | The user whose information should be updated. |
| pwd | string | Optional. The new password in cleartext. |
| customData | document | Optional. Any arbitrary information. |
| roles | array | Optional. The roles granted to the user. Note that the existing ones are replaced and not amended with these roles. |
| mechanisms | array | Optional. The specific SCRAM mechanisms for user credentials. Note that if a new pwd is provided, then the array can contain all supported SCRAM mechanisms. If a new pwd is not provided, then the array must be a subset of the existing mechanisms of the user. |


Changes to `<code>customData</code>` or `<code>mechanisism</code>` are made only to the local
nosqlprotocol database, but changes to `<code>pwd</code>` or `<code>roles</code>` require
the MariaDB server to be updated.


### usersInfo


This command returns information about one or more users.


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| usersInfo | various | Specifies what to return. See below. |
| showCredentials | boolean | Optional, default false. Specifies whether the credentials should be returned. |


The returned information depends the valie of `<code>usersInfo</code>`:


| Argument | Result |
| --- | --- |
| Argument | Result |
| { usersInfo: 1 } | Returns information of all users in the database where the command is run. |
| { usersInfo: <username> } | Returns information about a specific user in the database where the command is run. |
| { usersInfo: { user: <name>, db: <db> }} | Returns information about the user specified by the name and database. |
| { usersInfo: [{ user: <name>, db: <db> }, ...]} | Returns information about specified users. |
| { usersInfo: [ <username>, ... ]} | Returns information about specified users in the database where the command is run. |


Note that users may always view their own information. Otherwise the user must
have the `<code>userAdmin</code>` or `<code>userAdminAnyDatabase</code>` role.


If `<code>showCredentials</code>` is true, the returned object(s) will contain a
`<code>mariadb: { password: "*..."}</code>` field, where `<code>password</code>` is the
`<code>SHA1(SHA1())</code>` value of the password used when logging to MariaDB.
That is, the same string that is found in the `<code>password</code>` column in
the `<code>mysql.user</code>` table.


## Replication Commands


### isMaster


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| isMaster | any | Ignored. |


### replSetGetStatus


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| replSetGetStatus | any | Ignored. |


All other fields are ignored.


This command will always return the document



```
{
    "ok" : 0,
    "errmsg" : "not running with --replSet",
    "code" : 76,
    "codeName" : "NoReplicationEnabled"
}
```



## Sessions Commands


### endSessions


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| endSessions | array | Ignored. |


The following document will always be returned:



```
{ "ok" : 1 }
```



## Administration Commands


### create


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| create | string | The name of the collection to create. |
| capped | boolean | Optional. If specified, the value must be false as capped collections are not supported. |
| viewOn | string | Optional. If specified, the command will fail as views are not supported. |


Currently, *capped collections* and *views* are not supported. Consequently,
specifying that the collection should be capped or that it should be a
view on another collection, will cause the command to fail.


### createIndexes


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| createIndexes | string | The collection for which to create indexes. |


**NOTE** Currently it is not possible to create indexes, but the command
will nonetheless return success, provide the index specification passes
some rudimentary sanity checks. Note also that the collection will be
created if it does not exist.


### drop


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| drop | string | The name of the collection to drop. |


### dropDatabase


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| dropDatabase | any | Ignored. |


### dropIndexes


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| dropIndexes | any | Ignored. |


**NOTE** Currently it is not possible to create indexes and thus there
will never be any indexes that could be dropped. However, provided the
specfied collection exists, dropping indexes will always succeed except
for an attempt to drop the built-in `<code>_id_</code>` index.


### fsync


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| fsync | any | Ignored |


The response will always be



```
{
  "errmsg" : "fsync not supported by MaxScale:nosqlprotocol",
  "code" : 115,
  "codeName" : "CommandNotSupported",
  "ok" : 0
}
```



### killCursors


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| killCursors | string | The name of the collection. |
| cursors | array | The ids of the cursors to kill. |


### listCollections


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| listCollections | any | Ignored. |
| filter | document | The field name is honored, other fields are not but cause warnings to be logged. |
| nameOnly | boolean | Optional. A flag to indicate whether the command should return just the collection names and type or return both the name and other information. |


Note that the command lists all collections (that is, tables) that are found
in the current database. The listed collections may or may not be suitable
for being accessed using *nosqlprotocol*.


### listDatabases


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| listDatabases | any | Ignored. |
| nameOnly | boolean | Optional. A flag to indicate whether the command should return just the database names, or return both database names and size information. |


### listIndexes


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| listIndexes | string | The name of the collection. |


**NOTE** As it currently is not possible to actually create indexes,
although an attempt to do so using `<code>createIndexes</code>` will succeed, the
result will always only contain information about the built-in
index `<code>_id_</code>`.


### renameCollection


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| renameCollection | string | The namespace of the collection to rename. The namespace is a combination of the database name and the name of the collection. |
| to | string | The new namespace of the collection. Moving a collection/table from one database to another succeeds provided the databases reside in the same filesystem. |
| dropTarget | boolean | Optional. If true, the target collection/table will be dropped before the renaming is made. The default value is false. |


### setParameter


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| setParameter | any | Ignored. |


Any kind of parameter is accepted and the response will always be:



```
{ "ok" : 1 }
```



## Diagnostic Commands


### buildInfo


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| buildInfo | any | Ignored. |


The command returns a document containing the stable fields. In addition, there is a field `<code>maxscale</code>` whose value is the MaxScale version, expressed as a string.


### explain


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| explain | document | Document specifying the command to be explained. The commands are aggregate, count, delete, distinct, find, findAndModify, mapReduce and update. |
| verbosity | string | Either queryPlanner, executionStats or allPlansExecution. |


The command will return a document of the expected layout, but the content is only rudimentary.


### getCmdLineOpts


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| getCmdLineOpts | any | Ignored. |


### getLog


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| getLog | string | *, global and startupWarnings |


The command returns a document of the correct format, but *no* actual log data will be returned.


### hostInfo


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| hostInfo | any | Ignored. |


### listCommands


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| listCommands | any | Ignored. |


### ping


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| ping | any | Ignored. |


### serverStatus


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| serverStatus | any | Ignored. |


### validate


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| validate | string | The name of the collection to validate. |


The command does not actually perform any validation but for checking
that the collection exists. The response will contain in `<code>nrecords</code>`
the current number of documents/rows it contains.


### whatsmyuri


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| whatsmyri | any | Ignored. |


This is an internal command, implemented only because the Mongo Shell uses it.


## Free Monitoring Commands


### getFreeMonitoringStatus


The following fields are relevant.


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| getFreeMonitoringStatus | any | Ignored. |


The following document will always be returned:



```
{ "state" : "undecided", "ok" : 1 }
```



## MaxScale Specific Commands


### mxsAddUser


#### Definition


##### mxsAddUser


The `<code>mxsAddUser</code>` command adds an *existing* MariaDB user to the local
nosqlprotocol account database. Use [createUser](#createUser) if the
MariaDB user should be created as well.


Note that the `<code>mxsAddUser</code>` command does not check that the user exists
or that the specified roles are compatible with the grants of the user.


#### Syntax


The 'mxsAddUser' command has the following syntax:



```
db.runCommand(
    {
        mxsAddUser: "<name>",
        pwd: passwordPrompt(),  // Or "<cleartext password>"
        customData: { <any information> },
        roles: [
            { role: "<role>", db: "<database>" } | "<role>",
            ...
        ],
        mechanisms: [ "<scram-mechanism>", ...],
        digestPassword: <boolean>
    }
)
```



##### Command Fields


The command has the following fields:


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| mxsAddUser | string | The name of the user to be added. |
| pwd | string | The password in cleartext. |
| customData | document | Optional. Any arbitrary information. |
| roles | array | The roles granted to the user. |
| mechanisms | array | Optional. The specific supported SCRAM mechanisms for this user. Must be a subset of the supported mechanisms. |
| digestPassword | boolean | Optional. If specified, must be true. |


The value of `<code>mxsAddUser</code>` should be the name (without the host part) of
an existing user in the MariaDB server and the value of `<code>pwd</code>` should be
that user's password in cleartext.


The `<code>roles</code>` array should contain roles that a compatible with the
grants of the user. Please check [roles and grants](#roles_and_grants)
for a discussion on how to map roles map to grants.


##### Returns


If the addition of the user succeeds, the command returns a document
with the single field `<code>ok</code>` whose value is `<code>1</code>`.



```
> db.runCommand({mxsAddUser: "user", pwd: "pwd", roles: ["readWrite"]});
{ "ok" : 1 }
```



If there is a failure of some kind, the command returns an error document



```
> db.runCommand({mxsAddUser: "user2", pwd: "pwd2", roles: ["redWrite"]});
{
    "ok" : 0,
    "errmsg" : "No role named redWrite@test",
    "code" : 31,
    "codeName" : "RoleNotFound"
}
```



### mxsCreateDatabase


#### Definition


##### mxsCreateDatabase


The 'mxsCreateDatabase' command creates a new database and must be run
against the `<code>admin</code>` database.


#### Syntax


The 'mxsCreateDatabase' has the following syntax:



```
db.adminCommand(
    {
       mxsCreateDatabase: <name>
    }
)
```



##### Command Fields


The command takes the following fields:


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| mxsCreateDatabase | string | The name of the database to be created. |


##### Returns


If database creation succeeds, the command returns a document with the
single field `<code>ok</code>` whose value is `<code>1</code>`.



```
> db.adminCommand({mxsCreateDatabase: "db"});
{ "ok" : 1 }
```



If the database creation fails, the command returns an error document.



```
> db.adminCommand({mxsCreateDatabase: "db"});
{
    "ok" : 0,
    "errmsg" : "The database 'db' exists already.",
    "code" : 48,
    "codeName" : "NamespaceExists"
}
```



### mxsDiagnose


#### Definition


##### mxsDiagnose


The `<code>mxsDiagnose</code>` command provides diagnostics for any other command; that is, how
MaxScale will handle that command.


#### Syntax


The `<code>mxsDiagnose</code>` command has the following syntax:



```
db.runCommand(
    {
       mxsDiagnose: <command>
    }
)
```



##### Command Fields


The command takes the following fields:


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| mxsDiagnose | document | A command as provided to db.runCommand(...). |


##### Returns


The command returns a document that contains diagnostics of the command
provided as argument. For example:



```
> db.runCommand({mxsDiagnose: {ping:1}});
{ "kind" : "immediate", "response" : { "ok" : 1 }, "ok" : 1 }

> db.runCommand({mxsDiagnose: {find:"person", filter: { name: "Bob"}}});
{
  "kind" : "single",
  "sql" : "SELECT doc FROM `test`.`person` WHERE ( JSON_EXTRACT(doc, '$.name') = 'Bob') ",
  "ok" : 1
}

> db.runCommand({mxsDiagnose: {delete:"person", deletes: [{q: { name: "Bob"}, limit:0}, {q: {name: "Alice"}, limit:0}]}});
{
  "kind" : "single",
  "sql" : [
    "DELETE FROM `test`.`person` WHERE ( JSON_EXTRACT(doc, '$.name') = 'Bob') ",
    "DELETE FROM `test`.`person` WHERE ( JSON_EXTRACT(doc, '$.name') = 'Alice') "
  ],
  "ok" : 1
}
```



`<code>kind</code>` specifies of what kind the command is; an *immediate* command is one for
which MaxScale autonomously can generate the response, a *single* command is one
where the command will cause a single SQL statement to be sent to the backend, and
a *multi* command is one where potentially multiple SQL statements will be sent to
the backend.


If the command is *immediate* then there will be a field `<code>response</code>` containing
the actual response of the command, if the command is *single* then there will be
a field `<code>sql</code>` containing the actual statement that would have been sent to the backend,
and if the command is *multi* then there will be a field `<code>sql</code>` containing an array
of statements that would have been sent to the backend.


If an error occurs while the command is being diagnosed, then there will be no
`<code>response</code>` field but an `<code>error</code>` field whose value is an error document. Note that
the value of `<code>ok</code>` will always be 1.


### mxsGetConfig


#### Definition


#### mxsGetConfig


The `<code>mxsGetConfig</code>` command returns the current configuration of the session
and must be run against the 'admin' database.


#### Syntax


The `<code>mxsGetConfig</code>` has the following syntax:



```
db.runCommand(
    {
        mxsGetConfig: <any>
    });
```



##### Command Fields


The command takes the following fields:


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| mxsGetConfig | <any> | Ignored. |


##### Returns


The command returns a document that contains the current configuration of
the session. For example:



```
> db.runCommand({mxsGetConfig: 1});
{
    "config" : {
        "on_unknown_command" : "return_error",
        "auto_create_tables" : true,
        "id_length" : 35
                ...
    },
    "ok" : 1
}
```



### mxsRemoveUser


#### Definition


##### mxsRemoveUser


The `<code>mxsRemoveUser</code>` removes a user from the local nosqlprotocol account
database. Use [dropUser](#dropUser) if the MariaDB user should be dropped
as well.


#### Syntax


The 'mxsRemoveUser' command has the following syntax:



```
db.runCommand(
    {
        mxsRemoveUser: "<name>"
    }
)
```



##### Command Fields


The command has the following fields:


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| mxsRemoveUser | string | The name of the user to be removed. |


##### Returns


If the removal of the user succeeds, the command returns a document
with the single field `<code>ok</code>` whose value is `<code>1</code>`.



```
> db.runCommand({mxsRemoveUser: "user"});
{ "ok" : 1 }
```



If there is a failure of some kind, the command returns an error document



```
> db.runCommand({mxsRemoveUser: "user"});
{
    "ok" : 0,
    "errmsg" : "User 'user@test' not found",
    "code" : 11,
    "codeName" : "UserNotFound"
}
```



### mxsSetConfig


#### Definition


#### mxsSetConfig


The `<code>mxsSetConfig</code>` command changes the configuration of the session
and must be run against the 'admin' database.


Note that the changes only affect the current session and are **not**
persisted.


#### Syntax


The `<code>mxsSetConfig</code>` has the following syntax:



```
db.runCommand(
    {
        mxsSetConfig: document
    });
```



##### Command Fields


The command takes the following fields:


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| mxsSetConfig | document | A document specifying the configuration. |


The document takes the following fields:


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| on_unknown_command | string | Either "return_error" or "return_empty" |
| auto_create_tables | boolean | Whether tables should be created as needed. |
| id_length | integer | id column VARCHAR size in created tables. |


##### Returns


The command returns a document that contains the changed configuration of
the session. For example:



```
> db.runCommand({mxsGetConfig: 1});
{
    "config" : {
        "on_unknown_command" : "return_error",
        "auto_create_tables" : true,
        "id_length" : 35
                ...
    },
    "ok" : 1
}
> db.runCommand({mxsSetConfig: { auto_create_tables: false}});
{
    "config" : {
        "on_unknown_command" : "return_error",
        "auto_create_tables" : false,
        "id_length" : 35
                ...
    },
    "ok" : 1
}
```



### mxsUpdateUser


#### Definition


##### mxsUpdateUser


The `<code>mxsUpdateUser</code>` command updates a user in the local nosqlprotocol
account database. Use [updateUser](#updateUser) to update MariaDB user
as well.


Note that the `<code>mxsUpdateUser</code>` command does not check that the changed
data is compatible e.g. with the grants of the corresponding MariaDB
user.


#### Syntax


The 'mxsUpdateUser' command has the following syntax:



```
db.runCommand(
    {
        mxsUpdateUser: "<name>",
        pwd: passwordPrompt(),  // Or "<cleartext password>"
        customData: { <any information> },
        roles: [
            { role: "<role>", db: "<database>" } | "<role>",
            ...
        ],
        mechanisms: [ "<scram-mechanism>", ...],
        digestPassword: <boolean>
    }
)
```



##### Command Fields


The command has the following fields:


| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| mxsUpdateUser | string | The name of the user to be updated. |
| pwd | string | The password in cleartext. |
| customData | document | Optional. Any arbitrary information. |
| roles | array | The roles granted to the user. |
| mechanisms | array | Optional. The specific supported SCRAM mechanisms for this user. If a new password is not provided, the specified mechanisms must be a subset of the current mechanisms. |
| digestPassword | boolean | Optional. If specified, must be true. |


The `<code>roles</code>` array should contain roles that a compatible with the
grants of the user. Please check [roles and grants](#roles_and_grants)
for a discussion on how to map roles map to grants.


##### Returns


If the updating of the user succeeds, the command returns a document
with the single field `<code>ok</code>` whose value is `<code>1</code>`.



```
> db.runCommand({mxsUpdateUser: "user", pwd: "pwd", roles: ["readWrite"]});
{ "ok" : 1 }
```



If there is a failure of some kind, the command returns an error document



```
> db.runCommand({mxsUpdateUser: "user", roles: ["redWrite"]});
{
    "ok" : 0,
    "errmsg" : "No role named redWrite@test",
    "code" : 31,
    "codeName" : "RoleNotFound"
}
```



# Object Id


When a document is created, an id of type `<code>ObjectId</code>` will be autogenerated by
the MongoDB® client library. If the id is provided explicitly, by assigning a
value to the `<code>_id</code>` field, the value must be an `<code>ObjectId</code>`, a string or an
integer.


# Compatibility


Currently 30% of the tests in the
[MongoDB® core](https://github.com/mongodb/mongo/tree/master/jstests/core)
test-suite pass.


# Example


The following is a minimal setup for getting *nosqlprotocol* up and
running. It is assumed the reader knows how to configure MaxScale for
normal use. If not, please start with the
[MaxScale tutorial](../mariadb-maxscale-23-02-tutorials/mariadb-maxscale-2302-setting-up-mariadb-maxscale.md).
Note that as *nosqlprotocol* is the first component in the MaxScale
routing chain, it can be used with all routers and filters.


## Configuring MaxScale


In the following it is assumed that MaxScale already has been configured
for normal use and that there exists a *service* `<code>[TheService]</code>`.



```
[TheService]
type=service
...

[NoSQL-Listener]
type=listener
service=TheService
protocol=nosqlprotocol
nosqlprotocol.user=the_user
nosqlprotocol.password=the_password
port=17017
```



The values `<code>the_user</code>` and `<code>the_password</code>` must be replaced with the
actual credentials to be used for every MongoDB® client that connects.


If MaxScale is now started, the following entry should appear in the
log file.



```
... notice : (NoSQL-Listener); Listening for connections at [127.0.0.1]:17017
```



## MongoDB® Shell


The mongo Shell is a powerful tool with which to access and manipulate a
MongoDB database. It is part of the MongoDB® package. Having the native
MongoDB database installed is convenient, as it makes it easy to ascertain
whether a problem is due to *nosqlprotocol* not fully implementing something
or due to the API not being used in the correct fashion.


With the *mongo shell*, all that is needed is to invoke it with the port
*nosqlprotocol* is listening on:



```
$ mongo --port 17017
MongoDB shell version v4.4.1
connecting to: mongodb://127.0.0.1:17017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("694f3eed-329f-487a-8d73-9a2d4cf82d62") }
MongoDB server version: 4.4.1
---
        ...
---
>
```



If the shell prompt appears, then a connection was successfully
established and the shell can be used.



```
> db.runCommand({insert: "collection", documents: [{_id: 1, "hello": "world"}]});
{ "n" : 1, "ok" : 1 }
```



The `<code>db</code>` variable is implicitly available, and refers by default to
the `<code>test</code>` database.


The command inserted a document into the collection called `<code>collection</code>`.
The table corresponding to that collection is created implicitly because
the default value of `<code>auto_create_tables</code>` is `<code>true</code>`. Here, the object id
is specified explicitly, but there is no need for that, as one will be
created if needed.


To check whether the documents was inserted into the collection, the
`<code>find</code>` command can be issued:



```
> db.runCommand({find: "collection"});
{
    "cursor" : {
        "firstBatch" : [
            {
                "_id" : 1,
                "hello" : "world"
            }
        ],
        "id" : NumberLong(0),
        "ns" : "test.collection"
    },
    "ok" : 1
}
```



As can be seen, the document was indeed inserted into the collection


With the `<code>mysql</code>` shell, the content of the actual table can be checked.



```
MariaDB [(none)]> select * from test.collection;
+------+------------------------------------+
| id   | doc                                |
+------+------------------------------------+
| 1.0  | { "_id" : 1.0, "hello" : "world" } |
+------+------------------------------------+
```



The collection `<code>collection</code>` is represented by a table `<code>collection</code>` with
the two colums `<code>id</code>` and `<code>doc</code>`. `<code>id</code>` is a virtual column whose content is
the value of the `<code>_id</code>` field of the document in the `<code>doc</code>` column.


All MongoDB® commands that *mongdbprotocol* support (but for the ones that
do not require database access), basically access or manipulate the
content in the `<code>doc</code>` column using the
[JSON functions](../../../server/reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/json-functions/README.md) of MariaDB.


From within the mongo shell itself it is easy to find out just what SQL
a particular MongoDB command is translated into.


For instance, the SQL that the insert command with which the document was
added can be found out like:



```
> db.runCommand({mxsDiagnose: {insert: "collection", documents: [{_id: 1, "hello": "world"}]}});
{
    "kind" : "multi",
    "sql" : [
        "INSERT INTO `test`.`collection` (doc) VALUES ('{ \"_id\" : 1.0, \"hello\" : \"world\" }')"
    ],
    "ok" : 1
}
```



Similarily, the SQL of the `<code>find</code>` command can be find out like:



```
> db.runCommand({mxsDiagnose: {find: "collection"}});
{
    "kind" : "single",
    "sql" : "SELECT doc FROM `test`.`collection` ",
    "ok" : 1
}
```



The returned SQL can be directly pasted at the `<code>mysql</code>` prompt, which is
quite convenient in case the MongoDB® command does not behave as expected.


## MongoDB® Node.JS Driver


As all client libraries implement and depend on the the MongoDB® wire protocol,
all client libraries should work with *nosqlprotocol*. However, the
only client library that has been used and that has been verified to work
is version 3.6 of the *MongoDB Node.JS Driver*.


In principle, the only thing that needs to be altered in an existing
program using the library is to change the uri string that typically
is something like



```
const uri = "mongodb+srv://<user>:<password>@<cluster-url>?writeConcern=majority";
```



to



```
const uri = "mongodb://<maxscale-ip>:17017";
```



with the assumption that the default *nosqlprotocol* port is used.


In practice, additional modifications may be needed since *nosqlprotocol*
does not implement all commands and does not in all cases implement the
full functionality of the commands that it supports.


### Inserting a Document


Store the following into a file called `<code>insert.js</code>`.



```
const { MongoClient } = require("mongodb");

const uri = "mongodb://127.0.0.1:17017";

const client = new MongoClient(uri, { useUnifiedTopology: true });
async function run() {
  try {
    await client.connect();
    const database = client.db("mydb");
    const movies = database.collection("movies");
    // create a document to be inserted
    const movie = { title: "Apocalypse Now", director: "Francis Ford Coppola" };
    const result = await movies.insertOne(movie);
    console.log(
      `${result.insertedCount} documents were inserted with the _id: ${result.insertedId}`,
    );
  } finally {
    await client.close();
  }
}
run().catch(console.dir);
```



Then, run the program like



```
$ nodejs insert.js
1 documents were inserted with the _id: 60afca73bf486114e3fb48b8
```



As the id is not explicitly provided, it will not be the same.


### Finding a Document


Store the following into a file called `<code>find.js</code>`.



```
const { MongoClient } = require("mongodb");

const uri = "mongodb://127.0.0.1:17017";

const client = new MongoClient(uri, { useUnifiedTopology: true });
async function run() {
  try {
    await client.connect();
    const database = client.db("mydb");
    const movies = database.collection("movies");
    // Query for a movie that has the title 'Apocalypse Now'
    const query = { title: "Apocalypse Now" };
    const options = {
      // Include only the 'director' field in the returned document
      projection: { _id: 0, director: 1 },
    };
    const movie = await movies.findOne(query, options);
    // Returns a document and not a cursor, so print directly.
    console.log(movie);
  } finally {
    await client.close();
  }
}
run().catch(console.dir);
```



Then, run the program like



```
$ nodejs find.js
{ director: 'Francis Ford Coppola' }
```

