# EXECUTE Statement

## Syntax

```sql
EXECUTE stmt_name
    [USING expression[, expression] ...]
```

## Description

After preparing a statement with [PREPARE](prepare-statement.md), you execute it with an`EXECUTE` statement that refers to the prepared statement name. If the prepared statement contains any parameter markers, you must supply a`USING` clause that lists user variables containing the values to be bound to the parameters. Parameter values can be supplied only by user variables, and the `USING` clause must name exactly as many variables as the number of parameter markers in the statement.

You can execute a given prepared statement multiple times, passing different variables to it or setting the variables to different values before each execution.

If the specified statement has not been PREPAREd, an error similar to the following is produced:

```sql
ERROR 1243 (HY000): Unknown prepared statement handler (stmt_name) given to EXECUTE
```

{% tabs %}
{% tab title="Current" %}
`EXECUTE` with expression as parameters can be used, not just variables (@var\_name) as parameters.
{% endtab %}

{% tab title="< 10.2.3" %}
You can only use variables (@var\_name) as parameters.
{% endtab %}
{% endtabs %}

## Example

See [example in PREPARE](prepare-statement.md#example).

## See Also

* [EXECUTE IMMEDIATE](execute-immediate.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
