# SHOW TRIGGERS

## Syntax

```sql
SHOW TRIGGERS [FROM db_name]
    [LIKE 'pattern' | WHERE expr]
```

## Description

`SHOW TRIGGERS` lists the triggers currently defined for tables in a database (the default database unless a `FROM` clause is given). This statement requires the[TRIGGER](show-privileges.md) privilege (prior to MySQL 5.1.22, it required the `SUPER` privilege).

The `LIKE` clause, if present on its own, indicates which table names to match and causes the statement to display triggers for those tables. The `WHERE` and `LIKE` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).

Similar information is stored in the [information_schema.TRIGGERS](../system-tables/information-schema/information-schema-tables/information-schema-triggers-table.md) table.

If there are multiple triggers for the same action, then the triggers are shown in action order.

## Examples

For the trigger defined at [Trigger Overview](../../../../server-usage/triggers-events/triggers/trigger-overview.md):

```sql
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

```sql
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

```sql
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

* `character_set_client` is the session value of the [character_set_client](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client) system variable when the trigger was created.
* `collation_connection` is the session value of the [collation_connection](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variable when the trigger was   created.
* `Database Collation` is the collation of the database   with which the trigger is associated.

These columns were added in MariaDB/MySQL 5.1.21.

Old triggers created before MySQL 5.7 and [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes) have NULL in the `Created` column.

## See also

* [Trigger Overview](../../../../server-usage/triggers-events/triggers/trigger-overview.md)
* [CREATE TRIGGER](../../../../server-usage/triggers-events/triggers/create-trigger.md)
* [DROP TRIGGER](../../data-definition/drop/drop-trigger.md)
* [information\_schema.TRIGGERS](../system-tables/information-schema/information-schema-tables/information-schema-triggers-table.md) table
* [SHOW CREATE TRIGGER](show-create-trigger.md)
* [Trigger Limitations](../../../../server-usage/triggers-events/triggers/trigger-limitations.md)

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
