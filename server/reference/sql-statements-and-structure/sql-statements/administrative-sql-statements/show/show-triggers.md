
# SHOW TRIGGERS

## Syntax


```
SHOW TRIGGERS [FROM db_name]
    [LIKE 'pattern' | WHERE expr]
```


## Description


`<code class="highlight fixed" style="white-space:pre-wrap">SHOW TRIGGERS</code>` lists the triggers currently defined for
tables in a database (the default database unless a `<code class="highlight fixed" style="white-space:pre-wrap">FROM</code>`
clause is given). This statement requires the
`<code class="highlight fixed" style="white-space:pre-wrap">[TRIGGER](show-privileges.md)</code>` privilege (prior to MySQL
5.1.22, it required the `<code class="highlight fixed" style="white-space:pre-wrap">SUPER</code>` privilege).


The `<code class="highlight fixed" style="white-space:pre-wrap">LIKE</code>` clause, if present on its own, indicates which table names to
match and causes the statement to display triggers for those tables. The `<code class="highlight fixed" style="white-space:pre-wrap">WHERE</code>` and `<code class="highlight fixed" style="white-space:pre-wrap">LIKE</code>` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).


Similar information is stored in the `<code>[information_schema.TRIGGERS](../system-tables/information-schema/information-schema-tables/information-schema-triggers-table.md)</code>` table.


If there are multiple triggers for the same action, then the triggers are shown in action order.


## Examples


For the trigger defined at [Trigger Overview](../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/trigger-overview.md):


```
SHOW triggers Like 'animals' \G
*************************** 1. row ***************************
             Trigger: the_mooses_are_loose
               Event: INSERT
               Table: animals
           Statement: BEGIN
 IF NEW.name = 'Moose' THEN
  UPDATE animal_count SET animal_count.animals = animal_count.animals+100;
 ELSE 
  UPDATE animal_count SET animal_count.animals = animal_count.animals+1;
 END IF;
END
              Timing: AFTER
             Created: 2016-09-29 13:53:34.35
            sql_mode: 
             Definer: root@localhost
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

Listing all triggers associated with a certain table:


```
SHOW TRIGGERS FROM test WHERE `Table` = 'user' \G
*************************** 1. row ***************************
             Trigger: user_ai
               Event: INSERT
               Table: user
           Statement: BEGIN END
              Timing: AFTER
             Created:  2016-09-29 13:53:34.35
            sql_mode: 
             Definer: root@%
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

```
SHOW triggers WHERE Event Like 'Insert' \G
*************************** 1. row ***************************
             Trigger: the_mooses_are_loose
               Event: INSERT
               Table: animals
           Statement: BEGIN
 IF NEW.name = 'Moose' THEN
  UPDATE animal_count SET animal_count.animals = animal_count.animals+100;
 ELSE 
  UPDATE animal_count SET animal_count.animals = animal_count.animals+1;
 END IF;
END
              Timing: AFTER
             Created: 2016-09-29 13:53:34.35
            sql_mode: 
             Definer: root@localhost
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

* `<code class="highlight fixed" style="white-space:pre-wrap">character_set_client</code>` is the session value of the `<code>[character_set_client](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client)</code>` system variable when the trigger was created.
* `<code class="highlight fixed" style="white-space:pre-wrap">collation_connection</code>` is the session value of the `<code>[collation_connection](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection)</code>` system variable when the trigger was
 created.
* `<code class="highlight fixed" style="white-space:pre-wrap">Database Collation</code>` is the collation of the database 
 with which the trigger is associated.


These columns were added in MariaDB/MySQL 5.1.21.


Old triggers created before MySQL 5.7 and [MariaDB 10.2.3](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md) have NULL in the `<code>Created</code>` column.


## See also


* [Trigger Overview](../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/trigger-overview.md)
* [CREATE TRIGGER](../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/create-trigger.md)
* [DROP TRIGGER](../../data-definition/drop/drop-trigger.md)
* [information_schema.TRIGGERS](../system-tables/information-schema/information-schema-tables/information-schema-triggers-table.md) table
* [SHOW CREATE TRIGGER](show-create-trigger.md)
* [Trigger Limitations](../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/trigger-limitations.md)

