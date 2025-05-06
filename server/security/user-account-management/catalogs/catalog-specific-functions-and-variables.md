
# Catalog-Specific Functions and Variables


##### MariaDB starting with [12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/what-is-mariadb-120)
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


CC BY-SA / Gnu FDL

