---
title: Untitled
---

{% tabs %}
{% tab title="Current" %}
If the `COMMENT` clause is present, it will be shown in the output, too:

```sql
SHOW CREATE DATABASE p;
+----------+--------------------------------------------------------------------------------------+
| Database | Create Database                                                                      |
+----------+--------------------------------------------------------------------------------------+
| p        | CREATE DATABASE `p` /*!40100 DEFAULT CHARACTER SET latin1 */ COMMENT 'presentations' |
+----------+--------------------------------------------------------------------------------------+
```
{% endtab %}

{% tab title="< 10.5" %}
The `COMMENT` clause is not available, and will thus not appear in the output.
{% endtab %}
{% endtabs %}
