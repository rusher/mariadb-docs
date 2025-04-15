# Installing MariaDB Windows ZIP Packages

Users need to run [mariadb-install-db.exe](../mariadb-install-db-exe.md), without parameters to create a data directory, e.g

```
C:\zip_unpack\directory> bin\mariadb-install-db.exe
```

Then you can start server like this

```
C:\zip_unpack\directory> bin\mariadbd.exe --console
```

If you like to customize the server instance (data directory, install as service etc), please refer to [mariadb-install-db.exe documentation](../mariadb-install-db-exe.md)