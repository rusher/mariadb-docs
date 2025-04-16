
# CREATE PACKAGE

The `CREATE PACKAGE` statement can be used when [Oracle SQL_MODE](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md) is set, or in any mode from [MariaDB 11.4](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md).


In Oracle mode, the PL/SQL dialect is used, while if Oracle mode is not set (the default), SQL/PSM is used.


## Syntax (Oracle mode)


```
CREATE
    [ OR REPLACE]
    [DEFINER = { user | CURRENT_USER | role | CURRENT_ROLE }]
    PACKAGE [ IF NOT EXISTS ]
    [ db_name . ] package_name
    [ package_characteristic ... ]
{ AS | IS }
    [ package_specification_element ... ]
END [ package_name ]


package_characteristic:
    COMMENT 'string'
  | SQL SECURITY { DEFINER | INVOKER }


package_specification_element:
    FUNCTION_SYM package_specification_function ;
  | PROCEDURE_SYM package_specification_procedure ;


package_specification_function:
    func_name [ ( func_param [, func_param]... ) ]
    RETURN type
    [ package_routine_characteristic... ]

package_specification_procedure:
    proc_name [ ( proc_param [, proc_param]... ) ]
    [ package_routine_characteristic... ]

func_param:
    param_name [ IN | OUT | INOUT | IN OUT ] type

proc_param:
    param_name [ IN | OUT | INOUT | IN OUT ] type

type:
    Any valid MariaDB explicit or anchored data type


package_routine_characteristic:
      COMMENT  'string'
    | LANGUAGE SQL
    | { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
    | SQL SECURITY { DEFINER | INVOKER }
```

## Syntax (non-Oracle mode)


```
CREATE
    [ OR REPLACE]
    [DEFINER = { user | CURRENT_USER | role | CURRENT_ROLE }]
    PACKAGE [ IF NOT EXISTS ]
    [ db_name . ] package_name
    [ package_characteristic ... ]
    [ package_specification_element ... ]
END


package_characteristic:
    COMMENT 'string'
  | SQL SECURITY { DEFINER | INVOKER }


package_specification_element:
    FUNCTION_SYM package_specification_function ;
  | PROCEDURE_SYM package_specification_procedure ;


package_specification_function:
    func_name [ ( func_param [, func_param]... ) ]
    RETURNS type
    [ package_routine_characteristic... ]

package_specification_procedure:
    proc_name [ ( proc_param [, proc_param]... ) ]
    [ package_routine_characteristic... ]

func_param:
    param_name [ IN | OUT | INOUT | IN OUT ] type

proc_param:
    param_name [ IN | OUT | INOUT | IN OUT ] type

type:
    Any valid MariaDB explicit or anchored data type


package_routine_characteristic:
      COMMENT  'string'
    | LANGUAGE SQL
    | { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
    | SQL SECURITY { DEFINER | INVOKER }
```


## Description


The `CREATE PACKAGE` statement can be used when [Oracle SQL_MODE](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md) is set, or in any mode from [MariaDB 11.4](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md).


`CREATE PACKAGE` creates the specification for a stored package (a collection of logically related stored objects). A stored package specification declares public routines (procedures and functions) of the package, but does not implement these routines.


A package whose specification was created by the `CREATE PACKAGE` statement, should later be implemented using the [CREATE PACKAGE BODY](create-package-body.md) statement.


## Function parameter quantifiers IN | OUT | INOUT | IN OUT



##### MariaDB starting with [10.8.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes.md)
The function parameter quantifiers for `IN`, `OUT`, `INOUT`, and `IN OUT` where added in a 10.8.0 preview release. Prior to 10.8.0 quantifiers were supported only in procedures.


`OUT`, `INOUT` and its equivalent `IN OUT`, are only valid if called from `SET` and not `SELECT`. These quantifiers are especially useful for creating functions and procedures with more than one return value. This allows functions and procedures to be more complex and nested.


## Examples


Oracle mode:


```
SET sql_mode=ORACLE;
DELIMITER $$
CREATE OR REPLACE PACKAGE employee_tools AS
  FUNCTION getSalary(eid INT) RETURN DECIMAL(10,2);
  PROCEDURE raiseSalary(eid INT, amount DECIMAL(10,2));
  PROCEDURE raiseSalaryStd(eid INT);
  PROCEDURE hire(ename TEXT, esalary DECIMAL(10,2));
END;
$$
DELIMITER ;
```

From [MariaDB 11.4](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md), non-Oracle mode:


```
SET sql_mode='';

DELIMITER $$

CREATE OR REPLACE PACKAGE pkg
  PROCEDURE p1();
  FUNCTION f1() RETURNS INT;
END;
$$

DELIMITER ;
```

## See Also


* [CREATE PACKAGE BODY](create-package-body.md)
* [SHOW CREATE PACKAGE](../../administrative-sql-statements/show/show-create-package.md)
* [DROP PACKAGE](../drop/drop-package-body.md)
* [Oracle SQL_MODE](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)

