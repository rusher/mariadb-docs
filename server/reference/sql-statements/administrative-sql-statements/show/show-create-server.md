# SHOW CREATE SERVER

**MariaDB starting with** [**11.7**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-7-rolling-releases/what-is-mariadb-117)

The SHOW CREATE SERVER statement was introduced in [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-7-rolling-releases/what-is-mariadb-117).

## Syntax

```
SHOW CREATE SERVER server_name
```

## Description

Shows the [CREATE SERVER](../../data-definition/create/create-server.md) statement that created the given server definition.

## Example

```
SHOW CREATE SERVER srv1\G
*************************** 1. row ***************************
       Server: srv1
Create Server: CREATE SERVER `srv1` FOREIGN DATA WRAPPER mysql 
  OPTIONS (HOST '172.30.0.58', DATABASE 'db1', USER 'maxscale', PASSWORD 'password');
```

## See Also

* [CREATE SERVER](../../data-definition/create/create-server.md)
* [SHOW](./)

CC BY-SA / Gnu FDL
