
# ColumnStore Update

The UPDATE statement changes data stored in rows.

 
1. [Syntax "Syntax"](#syntax)





## Syntax


Single-table syntax:


```
UPDATE  table_reference 
  SET col1={expr1|DEFAULT} [,col2={expr2|DEFAULT}] ...
  [WHERE where_condition]
  [ORDER BY ...]
  [LIMIT row_count]
```

Multiple-table syntax:


```
UPDATE table_references
    SET col1={expr1|DEFAULT} [, col2={expr2|DEFAULT}] ...
    [WHERE where_condition]
```

{% hint style="info" %}
Note: It can only 1 table (but multiple columns) be updated from the table list in table_references.
{% endhint %}

CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
