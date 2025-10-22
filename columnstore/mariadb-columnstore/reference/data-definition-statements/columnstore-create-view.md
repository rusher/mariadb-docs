# ColumnStore CREATE VIEW

Creates a stored query in the MariaDB ColumnStore.

## Syntax

```sql
CREATE
    [OR REPLACE]
    VIEW view_name [(column_list)]
    AS select_statement
```

## Notes

* If you describe a view in MariaDB ColumnStore, the column types reported may not match the actual column types in the underlying tables. This is normal and can be ignored.&#x20;

The following statement creates a customer view of orders with status:

```sql
CREATE VIEW v_cust_orders (cust_name, order_number, order_status) AS
SELECT c.cust_name, o.ordernum, o.status FROM customer c, orders o
WHERE c.custnum = o.custnum;
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
