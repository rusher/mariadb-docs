
# RENAME USER

## Syntax


```
RENAME USER old_user TO new_user
    [, old_user TO new_user] ...
```

## Description


The RENAME USER statement renames existing MariaDB accounts. To use it,
you must have the global [CREATE USER](grant.md#global-privileges) privilege
or the `<code>[UPDATE](grant.md#table-privileges)</code>` privilege for the `<code>mysql</code>` database.
Each account is named using the same format as for the [CREATE USER](create-user.md)
statement; for example, `<code>'jeffrey'@'localhost'</code>`.
If you specify only the user name part of the account name, a host
name part of `<code>'%'</code>` is used.


If any of the old user accounts do not exist or any of the new user accounts already
exist, `<code>ERROR 1396 (HY000)</code>` results. If an error occurs, `<code>RENAME USER</code>`
will still rename the accounts that do not result in an error.


For modifying an existing account, see [ALTER USER](alter-user.md).


## Examples


```
CREATE USER 'donald', 'mickey';
RENAME USER 'donald' TO 'duck'@'localhost', 'mickey' TO 'mouse'@'localhost';
```

Renaming the host component of a user


```
RENAME USER 'foo'@'1.2.3.4' TO 'foo'@'10.20.30.40';
```
