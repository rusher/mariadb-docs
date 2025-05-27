# EXPLAIN FOR CONNECTION

## Syntax

```sql
EXPLAIN [FORMAT=JSON|...] FOR CONNECTION <connection_id>
```

Or

```sql
SHOW EXPLAIN [FORMAT=JSON] FOR <connection_id>
```

## Description

{% tabs %}
{% tab title="Current" %}
This statement works exactly like the [EXPLAIN](explain.md) statement. It narrows down results to the specified connection ID, though, excluding any other connections.
{% endtab %}

{% tab title="MariaDB < 11.4" %}
The SHOW EXPLAIN variant of the statement isn't available.
{% endtab %}

{% tab title="MariaDB < 10.9" %}
The SHOW EXPLAIN variant of the statement isn't available.
{% endtab %}
{% endtabs %}

## See Also

* [SHOW EXPLAIN](../show/show-explain.md)
* [Ignored Indexes](../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/ignored-indexes.md)

