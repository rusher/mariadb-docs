---
title: Tabbed Navigation block
---

{% tabs %}
{% tab title="Current" %}
`SHOW CREATE PROCEDURE` quotes identifiers, according to the value of the [sql\_quote\_show\_create](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable.
{% endtab %}

{% tab title="< 10.6.5 / 10.5.13 / 10.4.22" %}
`SHOW CREATE PROCEDURE` quotes identifiers according to the value of the [sql\_quote\_show\_create](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable. However, the output of this statement is unreliably affected by the [sql\_quote\_show\_create](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable.
{% endtab %}
{% endtabs %}
