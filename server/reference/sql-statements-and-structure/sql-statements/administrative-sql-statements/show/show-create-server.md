
# SHOW CREATE SERVER


##### MariaDB starting with [11.7](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md)
The  SHOW CREATE SERVER statement was introduced in [MariaDB 11.7](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md).



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
* [SHOW](show-procedure-code.md)

