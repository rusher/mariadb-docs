
# ColumnStore Create View

 
1. [Syntax "Syntax"](#syntax)





Creates a stored query in the MariaDB ColumnStore


## Syntax


```
CREATE
    [OR REPLACE]
    VIEW view_name [(column_list)]
    AS select_statement
```

Notes to CREATE VIEW:


* If you describe a view in MariaDB ColumnStore, the column types reported may not match the actual column types in the underlying tables. This is normal and can be ignored.
The following statement creates a customer view of orders with status:


```
CREATE VIEW v_cust_orders (cust_name, order_number, order_status) as
select c.cust_name, o.ordernum, o.status from customer c, orders o
where c.custnum = o.custnum;
```


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
