
# SHOW FUNCTION STATUS

## Syntax


```
SHOW FUNCTION STATUS
    [LIKE 'pattern' | WHERE expr]
```

## Description


This statement is similar to 
`<code class="highlight fixed" style="white-space:pre-wrap">[SHOW PROCEDURE STATUS](show-procedure-status.md)</code>` but for
[stored functions](../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md).


The LIKE clause, if present on its own, indicates which function names to match.


The `<code class="highlight fixed" style="white-space:pre-wrap">WHERE</code>` and `<code class="highlight fixed" style="white-space:pre-wrap">LIKE</code>` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).


The `<code>[information_schema.ROUTINES](../system-tables/information-schema/information-schema-tables/information-schema-routines-table.md)</code>` table contains more detailed information.


## Examples


Showing all stored functions:


```
SHOW FUNCTION STATUS\G
*************************** 1. row ***************************
                  Db: test
                Name: VatCents
                Type: FUNCTION
             Definer: root@localhost
            Modified: 2013-06-01 12:40:31
             Created: 2013-06-01 12:40:31
       Security_type: DEFINER
             Comment: 
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

Stored functions whose name starts with 'V':


```
SHOW FUNCTION STATUS LIKE 'V%' \G
*************************** 1. row ***************************
                  Db: test
                Name: VatCents
                Type: FUNCTION
             Definer: root@localhost
            Modified: 2013-06-01 12:40:31
             Created: 2013-06-01 12:40:31
       Security_type: DEFINER
             Comment: 
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

Stored functions with a security type of 'DEFINER':


```
SHOW FUNCTION STATUS WHERE Security_type LIKE 'DEFINER' \G
*************************** 1. row ***************************
                  Db: test
                Name: VatCents
                Type: FUNCTION
             Definer: root@localhost
            Modified: 2013-06-01 12:40:31
             Created: 2013-06-01 12:40:31
       Security_type: DEFINER
             Comment: 
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```
