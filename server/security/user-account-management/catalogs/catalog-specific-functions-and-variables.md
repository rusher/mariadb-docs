# Catalog-Specific Functions and Variables

{% include "../../../.gitbook/includes/catalogs.md" %}

### Catalog Functions

#### catalog()

\`catalog()

## returns the name of the current catalog.\`

```
MariaDB [def.test]> select catalog();
+-----------+
| catalog() |
+-----------+
| def       |
+-----------+
```

### Catalog Variables

#### @@catalogs

One can check if a server supports catalogs with:

```sql
SELECT @@catalogs;
+------------+
| @@catalogs |
+------------+
|          1 |
+------------+
```

1 means that the server is configured for catalogs.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
