
# Problem migrating from SQL Server to MariaDB — "Record has changed since last read"

## Problem migrating from SQL Server to MariaDB — "Record has changed since last read"


### Environment:


* Web application in ASP.NET Web Forms (.aspx)
* Backend in C

# (.NET Framework 3.5 and/or 4.6)
* Originally using SQL Server Express
* Migrated the database to MariaDB 10.x
* Two applications access the same table concurrently


### What I’ve done so far:


* Converted all database objects from SQL Server to MariaDB:

  * Tables, columns, functions, triggers — all adjusted for compatibility
* Updated all SqlConnection / SqlCommand code to use MySqlConnection / MySqlCommand (MySql.Data)
* Most of the system is working perfectly after migration


### The problem:


There is **one table** (*gfilaimpressao*) accessed concurrently by two applications (both .NET apps), and when this happens, I frequently get the following error:


```
Record has changed since last read in table gfilaimpressao
```


This **never happened with SQL Server**, even under simultaneous access.


### What I’ve tried:


* Researched how SQL Server vs MariaDB handle concurrency and transactions
* Tried changing MariaDB's transaction isolation level (e.g., from REPEATABLE READ to READ COMMITTED)
* Reviewed my code to ensure proper use of transactions (BEGIN, COMMIT, ROLLBACK)
* Even tried using SELECT ... FOR UPDATE in some cases
* Issue still persists regularly under concurrent access


### Question:


* Has anyone experienced this issue when migrating from SQL Server to MariaDB?
* Is there a specific way to configure MariaDB to better mimic SQL Server's behavior in handling concurrent transactions?
* Or is there something I should change in my .NET data access layer?


Any help or insight would be very welcome! :) Thanks in advance.

