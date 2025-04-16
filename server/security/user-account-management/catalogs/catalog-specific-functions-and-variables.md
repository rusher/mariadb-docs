
# Catalog-Specific Functions and Variables


##### MariaDB starting with [12.0](../../../../release-notes/mariadb-community-server/what-is-mariadb-120.md)
Catalog support is planned for 12.0.



## Catalog Functions


### catalog()


`catalog()

# returns the name of the current catalog.`


```
MariaDB [def.test]> select catalog();
+-----------+
| catalog() |
+-----------+
| def       |
+-----------+
```

## Catalog Variables


### @@catalogs


One can check if a server supports catalogs with:


```
select @@catalogs;
+------------+
| @@catalogs |
+------------+
|          1 |
+------------+
```

1 means that the server is configured for catalogs.

