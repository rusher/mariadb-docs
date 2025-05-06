
# MaxScale 2.1 Support for MariaDB 10.2

# Support for MariaDB 10.2


MariaDB 10.2 introduces a fair amount of new
[features](https://mariadb.com/kb/en/mariadb/what-is-mariadb-102/).


In the following will be explained what impact some of those features have,
when used together with MaxScale 2.1.


## [Window Functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/window-functions/)


The parser of MariaDB MaxScale has not been extended with the window
function syntax (the `OVER` keyword is not recognized) and hence statements
using window functions will not be completely parsed.


Since the database firewall filter will block all statements that
cannot be completely parsed, all statements that use window functions
will be blocked, if the database firewall filter is used.


Otherwise the statements will be routed correctly.


## [SHOW CREATE USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-user)


Cannot be completely parsed by the MaxScale parser and hence will be
blocked by the database firewall filter, if it is used.


Otherwise the statements will be routed correctly.


## [CREATE USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user)


The new options are not parsed by the MaxScale parser and hence any
statements using those will be blocked by the database firewall filter,
if it is used.


Otherwise the statements will be routed correctly.


## [ALTER USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/alter-user)


The new options are not parsed by the MaxScale parser and hence any
statements using those will be blocked by the database firewall filter,
if it is used.


Otherwise the statements will be routed correctly.


## [WITH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/common-table-expressions/with)


The MaxScale parser correctly parses `WITH` statements such as



```
WITH t AS (SELECT a FROM t1 WHERE b >= 'c')
SELECT * FROM t2,t WHERE t2.c=t.a;
```



,



```
SELECT t1.a,t1.b FROM t1,t2
  WHERE t1.a>t2.c AND
        t2.c in (WITH t as (SELECT * FROM t1 WHERE t1.a<5)
                   SELECT t2.c FROM t2,t WHERE t2.c=t.a);
```



and



```
WITH engineers AS (
  SELECT * FROM employees WHERE dept IN ('Development','Support')
)
SELECT * FROM engineers E1
  WHERE NOT EXISTS (SELECT 1
    FROM engineers E2
    WHERE E2.country=E1.country
    AND E2.name <> E1.name);
```



.


However, the MaxScale parser fails to collect columns and table names
from the `SELECT` of the `WITH` clause and consequently the database
firewall filter will **NOT** be able to block `WITH` statements where
the `SELECT` of the `WITH` clause refers to to forbidden columns.


## [CHECK CONSTRAINT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-definition/constraint)


The new options are not parsed by the MaxScale parser and hence any
statements using those will be blocked by the database firewall filter,
if it is used.


Otherwise the statements will be routed correctly.


## [DEFAULT with expressions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-definition/create/create-table)


Parsed and handled correctly.


## [EXECUTE IMMEDIATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/prepared-statements/execute-immediate)


An `EXECUTE IMMEDIATE` statement will only be partially parsed, which means
that such statements will be blocked by the database firewall filter,
if it is used.


## [JSON functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/json-functions/)


The MaxScape parser treats them as any other function.


However, as the parser is not aware of which JSON functions are strictly
*read-only* any statement using a JSON function will always be routed to
*master*.


CC BY-SA / Gnu FDL

