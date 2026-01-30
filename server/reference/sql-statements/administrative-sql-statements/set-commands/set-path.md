# SET PATH

{% hint style="info" %}
This functionality is available from MariaDB 12.3.
{% endhint %}

## Syntax

```sql
<set path statement>       ::=  SET  <SQL-path characteristic>
<SQL-path characteristic>  ::=  PATH  <value specification>
```

* The declared type of the <`value specification`> must be a character string type. Assuming the following:
  * `S` = _`<value specification>` ._
  *   `V` = the character string that is the value of

      `TRIM ( BOTH ' ' FROM S )`
* With these assumptions:
  * If `V` does not conform to the format and syntax rules of a `<schema name list>`, an exception condition is raised: _invalid schema name list specification_.
  * A `<set path statement>` that is executed between a `<prepare statement>` and an `<execute statement>` has no effect on the prepared statement.

## Description

Set the `SQL-path` used to determine the subject routine of `<routine invocation>`s with unqualified `<routine name>`s in:

* `<preparable statement>`s that are prepared in the current SQL-session by an <`execute immediate statement`> or a <`prepare statement`>.
* In `<direct SQL statement>`s that are invoked directly.

The `SQL-path` remains the current `SQL-path` of the SQL session until another `SQL-path` is successfully set.

In MariaDB, `SQL-path` is also used to look up packages in package routine invocations. The following statement invokes `SYS.UTL_ENCODE.BASE64_DECODE('data')`, that is, the function `BASE64_DECODE()` in the package `UTL_ENCODE` in the `SYS` database (if such package and package routine exist):

```sql
SET PATH='sys'; 
SELECT UTL_ENCODE.BASE64_DECODE('data');
```

### Notes

* This functionality introduces the `@@path` system variable (session and global).
* The `SET PATH` statement sets the `@@session.path` variable. It is also possible to assign a new value to the `@@path` variable directory, using a statement like this: `SET @@path='sys'`.
* `<value specification>` has the following features:
  * You can use delimited identifiers, like this:\
    `` SET PATH = `test`,`sys` ``&#x20;
  * You can use double quotes, like this:\
    `SET PATH "test", "sys"`
  * You can use empty schema names:\
    `SET PATH = ',,,test,,,sys,,,'` sets the path to `'test,sys'`. They're removed and ignored when setting a `@@path`.
  * You can use internal schemas, particularly `MARIADB_SCHEMA` and `ORACLE_SCHEMA`, like this:\
    `SET PATH ORACLE_SCHEMA,sys,MARIADB_SCHEMA`&#x20;
* Database aliases can be used with `CURRENT_SCHEMA`:\
  `SET PATH CURRENT_SCHEMA,sys`&#x20;
* In [stored routines](../../../../server-usage/stored-routines/), the SQL standard path is a property of the stored routine, like [sql\_mode](../../../../server-management/variables-and-modes/sql_mode.md) is.&#x20;

## See Also

* [Preparable statements](../../prepared-statements/prepare-statement.md)

