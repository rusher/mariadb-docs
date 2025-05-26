
# Introduction to Relational Databases


## What is a Database?


The easiest way to understand a database is as a collection of related files. Imagine a file (either paper or digital) of sales orders in a shop. Then there's another file of products, containing stock records. To fulfil an order, you'd need to look up the product in the order file and then look up and adjust the stock levels for that particular product in the product file. A database and the software that controls the database, called a *database management system* (DBMS), helps with this kind of task.


Most databases today are *relational* databases, named such because they deal with tables of data related by a common field. For example, Table 1 below shows the product table, and Table 2 shows the invoice table. As you can see, the relation between the two tables is based on the common field `product_code`. Any two tables can relate to each other simply by having a field in common.


### Table 1



| Product_code | Description | Price |
| --- | --- | --- |
| Product_code | Description | Price |
| A416 | Nails, box | $0.14 |
| C923 | Drawing pins, box | $0.08 |



### Table 2



| Invoice_code | Invoice_line | Product_code | Quantity |
| --- | --- | --- | --- |
| Invoice_code | Invoice_line | Product_code | Quantity |
| 3804 | 1 | A416 | 10 |
| 3804 | 2 | C923 | 15 |



## Database Terminology


Let's take a closer look at the previous two tables to see how they are organized:


* Each table consists of many rows and columns.
* Each new row contains data about one single entity (such as one product or one order line). This is called a record. For example, the first row in Table 1 is a record; it describes the A416 product, which is a box of nails that costs fourteen cents. The terms row and record are interchangeable.
* Each column (also called an attribute) contains one piece of data that relates to the record, called a tuple. Examples of attributes are the quantity of an item sold or the price of a product. An attribute, when referring to a database table, is called a field. For example, the data in the Description column in Table 1 are fields. The terms attribute and field are interchangeable.


Given this kind of structure, the database gives you a way to manipulate this data: SQL. SQL (structured query language) is a powerful way to search for records or make changes. Almost all DBMSs use SQL, although many have added their own enhancements to it. This means that when you learn SQL while using MariaDB, almost all of it is not specific to MariaDB and can be used with other relational databases as well, such as PostgreSQL, MySQL, Oracle and SQL Server. MariaDB was originally-created as a drop-in replacement to MySQL, so MariaDB and MySQL are particularly close.


## See Also


* [What Is a Database?](https://blog.devart.com/what-is-a-database.html)
* [What is an RDBMS?](https://www.devart.com/what-is-rdbms/)
* [DBMS vs RDBMS: Definitions, Differences, and a Comparison Table](https://www.devart.com/difference-between-rdbms-and-dbms/)


CC BY-SA / Gnu FDL

