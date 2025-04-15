
# Getting Data from MariaDB

The simplest way to retrieve data from MariaDB is to use the [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statement. Since the [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statement is an essential SQL statement, it has many options available with it. It's not necessary to know or use them all—you could execute very basic [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statements if that satisfies your needs. However, as you use MariaDB more, you may need more powerful [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statements. In this article we will go through the basics of [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) and will progress to more involved [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statements;we will move from the beginner level to the more intermediate and hopefully you will find some benefit from this article regardless of your skill level. For absolute beginners who are just starting with MariaDB, you may want to read the [MariaDB Basics article](mariadb-basics.md).


#### Creating and Populating the Tables


In order to follow the examples that follow, you can create and pre-populate the tables, as follows:


```
CREATE OR REPLACE TABLE books (
isbn CHAR(20) PRIMARY KEY, 
title VARCHAR(50),
author_id INT,
publisher_id INT,
year_pub CHAR(4),
description TEXT );

CREATE OR REPLACE TABLE authors
(author_id INT AUTO_INCREMENT PRIMARY KEY,
name_last VARCHAR(50),
name_first VARCHAR(50),
country VARCHAR(50) );

INSERT INTO authors (name_last, name_first, country) VALUES
  ('Kafka', 'Franz', 'Czech Republic'),
  ('Dostoevsky', 'Fyodor', 'Russia');
  
INSERT INTO books (title, author_id, isbn, year_pub) VALUES
 ('The Trial', 1, '0805210407', '1995'),
 ('The Metamorphosis', 1, '0553213695', '1995'),
 ('America', 2, '0805210644', '1995'),
 ('Brothers Karamozov', 2, '0553212168', ''),
 ('Crime & Punishment', 2, '0679420290', ''),
 ('Crime & Punishment', 2, '0553211757', ''),
 ('Idiot', 2, '0192834118', ''),
 ('Notes from Underground', 2, '067973452X', '');
```

If you are unclear what these statements do, review the [MariaDB Primer](a-mariadb-primer.md) and [MariaDB Basics](mariadb-basics.md) tutorials.


#### Basic Elements


The basic, minimal elements of the [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statement call for the keyword `<code>SELECT</code>`, of course, the columns to select or to retrieve, and the table from which to retrieve rows of data. Actually, for the columns to select, we can use the asterisk as a wildcard to select all columns in a particular table. Using a database from a fictitious bookstore, we might enter the following SQL statement to get a list of all columns and rows in a table containing information on books:


```
SELECT * FROM books;
```

```
+------------+------------------------+-----------+--------------+----------+-------------+
| isbn       | title                  | author_id | publisher_id | year_pub | description |
+------------+------------------------+-----------+--------------+----------+-------------+
| 0192834118 | Idiot                  |         2 |         NULL |          | NULL        |
| 0553211757 | Crime & Punishment     |         2 |         NULL |          | NULL        |
| 0553212168 | Brothers Karamozov     |         2 |         NULL |          | NULL        |
| 0553213695 | The Metamorphosis      |         1 |         NULL | 1995     | NULL        |
| 0679420290 | Crime & Punishment     |         2 |         NULL |          | NULL        |
| 067973452X | Notes from Underground |         2 |         NULL |          | NULL        |
| 0805210407 | The Trial              |         1 |         NULL | 1995     | NULL        |
| 0805210644 | America                |         2 |         NULL | 1995     | NULL        |
+------------+------------------------+-----------+--------------+----------+-------------+
8 rows in set (0.001 sec)
```

This will retrieve all of the data contained in the `<code>books</code>` table. As you can see, not all values have been populated. If we want to retrieve only certain columns, we would list them in place of the asterisk in a comma-separated list like so:


```
SELECT isbn, title, author_id
FROM books;
```

```
+------------+------------------------+-----------+
| isbn       | title                  | author_id |
+------------+------------------------+-----------+
| 0192834118 | Idiot                  |         2 |
| 0553211757 | Crime & Punishment     |         2 |
| 0553212168 | Brothers Karamozov     |         2 |
| 0553213695 | The Metamorphosis      |         1 |
| 0679420290 | Crime & Punishment     |         2 |
| 067973452X | Notes from Underground |         2 |
| 0805210407 | The Trial              |         1 |
| 0805210644 | America                |         2 |
+------------+------------------------+-----------+
8 rows in set (0.001 sec)
```

This narrows the width of the results set by retrieving only three columns, but it still retrieves all of the rows in the table. If the table contains thousands of rows of data, this may be more data than we want. If we want to limit the results to just a few books, say five, we would include what is known as a [LIMIT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#limit) clause:


```
SELECT isbn, title, author_id
FROM books 
LIMIT 5;
```

```
+------------+--------------------+-----------+
| isbn       | title              | author_id |
+------------+--------------------+-----------+
| 0192834118 | Idiot              |         2 |
| 0553211757 | Crime & Punishment |         2 |
| 0553212168 | Brothers Karamozov |         2 |
| 0553213695 | The Metamorphosis  |         1 |
| 0679420290 | Crime & Punishment |         2 |
+------------+--------------------+-----------+
5 rows in set (0.001 sec)
```

This will give us the first five rows found in the table. If we want to get the next ten found, we would add a starting point parameter just before the number of rows to display, separated by a comma:


```
SELECT isbn, title, author_id
FROM books 
LIMIT 5, 10;
```

```
+------------+------------------------+-----------+
| isbn       | title                  | author_id |
+------------+------------------------+-----------+
| 067973452X | Notes from Underground |         2 |
| 0805210407 | The Trial              |         1 |
| 0805210644 | America                |         2 |
+------------+------------------------+-----------+
3 rows in set (0.001 sec)
```

In this case, there are only three further records.


#### Selectivity and Order


The previous statements have narrowed the number of columns and rows retrieved, but they haven't been very selective. Suppose that we want only books written by a certain author, say Dostoevsky. Looking in the authors table we find that his author identification number is 2. Using a `<code>WHERE</code>` clause, we can retrieve a list of books from the database for this particular author like so:


```
SELECT isbn, title
FROM books
WHERE author_id = 2
LIMIT 5;
```

```
+------------+------------------------+
| isbn       | title                  |
+------------+------------------------+
| 0192834118 | Idiot                  |
| 0553211757 | Crime & Punishment     |
| 0553212168 | Brothers Karamozov     |
| 0679420290 | Crime & Punishment     |
| 067973452X | Notes from Underground |
+------------+------------------------+
5 rows in set (0.000 sec)
```

I removed the author_id from the list of columns to select, but left the basic [LIMIT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#limit) clause in because we want to point out that the syntax is fairly strict on ordering of clauses and flags. You can't enter them in any order. You'll get an error in return.


The SQL statements we've looked at thus far will display the titles of books in the order in which they're found in the database. If we want to put the results in alphanumeric order based on the values of the title column, for instance, we would add an [ORDER BY](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#order-by) clause like this:


```
SELECT isbn, title
FROM books
WHERE author_id = 2
ORDER BY title ASC
LIMIT 5;
```

```
+------------+--------------------+
| isbn       | title              |
+------------+--------------------+
| 0805210644 | America            |
| 0553212168 | Brothers Karamozov |
| 0553211757 | Crime & Punishment |
| 0679420290 | Crime & Punishment |
| 0192834118 | Idiot              |
+------------+--------------------+
5 rows in set (0.001 sec)
```

Notice that the [ORDER BY](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#order-by) clause goes after the `<code>WHERE</code>` clause and before the [LIMIT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#limit) clause. Not only will this statement display the rows in order by book title, but it will retrieve only the first five based on the ordering. That is to say, MariaDB will first retrieve all of the rows based on the `<code>WHERE</code>` clause, order the data based on the [ORDER BY](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#order-by) clause, and then display a limited number of rows based on the [LIMIT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#limit) clause. Hence the reason for the order of clauses. You may have noticed that we slipped in the ASC flag. It tells MariaDB to order the rows in ascending order for the column name it follows. It's not necessary, though, since ascending order is the default. However, if we want to display data in descending order, we would replace the flag with `<code>DESC</code>`. To order by more than one column, additional columns may be given in the [ORDER BY](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#order-by) clause in a comma separated list, each with the `<code>ASC</code>` or `<code>DESC</code>` flags if preferred.


#### Friendlier and More Complicated


So far we've been working with one table of data containing information on books for a fictitious bookstore. A database will usually have more than one table, of course. In this particular database, there's also one called authors in which the name and other information on authors is contained. To be able to select data from two tables in one [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statement, we will have to tell MariaDB that we want to join the tables and will need to provide a join point. This can be done with a [JOIN](../../../../server/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/join-syntax.md) clause as shown in the following SQL statement, with the results following it:


```
SELECT isbn, title, 
CONCAT(name_first, ' ', name_last) AS author
FROM books
JOIN authors USING (author_id)
WHERE name_last = 'Dostoevsky'
ORDER BY title ASC
LIMIT 5;
```

```
+------------+--------------------+-------------------+
| isbn       | title              | author            |
+------------+--------------------+-------------------+
| 0805210644 | America            | Fyodor Dostoevsky |
| 0553212168 | Brothers Karamozov | Fyodor Dostoevsky |
| 0553211757 | Crime & Punishment | Fyodor Dostoevsky |
| 0679420290 | Crime & Punishment | Fyodor Dostoevsky |
| 0192834118 | Idiot              | Fyodor Dostoevsky |
+------------+--------------------+-------------------+
5 rows in set (0.00 sec)
```

Our [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statement is getting hefty, but it's the same one to which we've been adding. Don't let the clutter fluster you. Looking for the new elements, let's focus on the [JOIN](../../../../server/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/join-syntax.md) clause first. There are a few possible ways to construct a join. This method works if both tables contain a column of the same name and value. Otherwise you'll have to redo the [JOIN](../../../../server/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/join-syntax.md) clause to look something like this:


```
...
JOIN authors ON author_id = row_id
...
```

This excerpt is based on the assumption that the key field in the authors table is not called author_id, but row_id instead. There's much more that can be said about joins, but that would make for a much longer article. If you want to learn more on joins, look at MariaDB's documentation page on [JOIN](../../../../server/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/join-syntax.md) syntax.


Looking again at the last full SQL statement above, you must have spotted the [CONCAT()](../../../../server/reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/concat_ws.md) function that we added to the on-going example statement. This string function takes the values of the columns and strings given and pastes them together, to give one neat field in the results. We also employed the AS parameter to change the heading of the results set for the field to author. This is much tidier. Since we joined the books and the authors tables together, we were able to search for books based on the author's last name rather than having to look up the author ID first. This is a much friendlier method, albeit more complicated. Incidentally, we can have MariaDB check columns from both tables to narrow our search. We would just add *column = value* pairs, separated by commas in the WHERE clause. Notice that the string containing the author's name is wrapped in quotes—otherwise, the string would be considered a column name and we'd get an error.


The name Dostoevsky is sometimes spelled Dostoevskii, as well as a few other ways. If we're not sure how it's spelled in the authors table, we could use the [LIKE](../../../../server/reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/like.md) operator instead of the equal sign, along with a wildcard. If we think the author's name is probably spelled either of the two ways mentioned, we could enter something like this:


```
SELECT isbn, title, 
CONCAT(name_first, ' ', name_last) AS author
FROM books
JOIN authors USING (author_id)
WHERE name_last LIKE 'Dostoevsk%'
ORDER BY title ASC
LIMIT 5;
```

```
+------------+--------------------+-------------------+
| isbn       | title              | author            |
+------------+--------------------+-------------------+
| 0805210644 | America            | Fyodor Dostoevsky |
| 0553212168 | Brothers Karamozov | Fyodor Dostoevsky |
| 0553211757 | Crime & Punishment | Fyodor Dostoevsky |
| 0679420290 | Crime & Punishment | Fyodor Dostoevsky |
| 0192834118 | Idiot              | Fyodor Dostoevsky |
+------------+--------------------+-------------------+
5 rows in set (0.001 sec)
```

This will match any author last name starting with Dostoevsk. Notice that the wildcard here is not an asterisk, but a percent-sign.


#### Some Flags


There are many flags or parameters that can be used in a [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statement. To list and explain all of them with examples would make this a very lengthy article. The reality is that most people never use some of them anyway. So, let's take a look at a few that you may find useful as you get more involved with MariaDB or if you work with large tables on very active servers.


The first flag that may be given, it goes immediately after the `<code>SELECT</code>` keyword, is `<code>ALL</code>`. By default, all rows that meet the requirements of the various clauses given are selected, so this isn't necessary. If instead we would only want the first occurrence of a particular criteria to be displayed, we could add the [DISTINCT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#distinct) option. For instance, for authors like Dostoevsky there will be several printings of a particular title. In the results shown earlier you may have noticed that there were two copies of *Crime & Punishment* listed, however they have different ISBN numbers and different publishers. Suppose that for our search we only want one row displayed for each title. We could do that like so:


```
SELECT DISTINCT title
FROM books
JOIN authors USING (author_id)
WHERE name_last = 'Dostoevsky'
ORDER BY title;
```

```
+------------------------+
| title                  |
+------------------------+
| America                |
| Brothers Karamozov     |
| Crime & Punishment     |
| Idiot                  |
| Notes from Underground |
+------------------------+
```

We've thinned out the ongoing SQL statement a bit for clarity. This statement will result in only one row displayed for *Crime & Punishment* and it will be the first one found.


If we're retrieving data from an extremely busy database, by default any other SQL statements entered simultaneously which are changing or updating data will be executed before a [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statement. [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statements are considered to be of lower priority. However, if we would like a particular [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statement to be given a higher priority, we can add the keyword HIGH_PRIORITY. Modifying the previous SQL statement for this factor, we would enter it like this:


```
SELECT DISTINCT HIGH_PRIORITY title
FROM books
JOIN authors USING (author_id)
WHERE name_last = 'Dostoevsky'
ORDER BY title;
```

```
+------------------------+
| title                  |
+------------------------+
| America                |
| Brothers Karamozov     |
| Crime & Punishment     |
| Idiot                  |
| Notes from Underground |
+------------------------+
```

You may have noticed in the one example earlier in which the results are shown, that there's a status line displayed that specifies the number of rows in the results set. This is less than the number of rows that were found in the database that met the statement's criteria. It's less because we used a [LIMIT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#limit) clause. If we add the [SQL_CALC_FOUND_ROWS](../../../../server/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/optimizer-hints.md#sql_calc_found_rows) flag just before the column list, MariaDB will calculate the number of columns found even if there is a [LIMIT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#limit) clause.


```
SELECT SQL_CALC_FOUND_ROWS isbn, title
FROM books
JOIN authors USING (author_id)
WHERE name_last = 'Dostoevsky'
LIMIT 5;
```

```
+------------+------------------------+
| isbn       | title                  |
+------------+------------------------+
| 0192834118 | Idiot                  |
| 0553211757 | Crime & Punishment     |
| 0553212168 | Brothers Karamozov     |
| 0679420290 | Crime & Punishment     |
| 067973452X | Notes from Underground |
+------------+------------------------+
5 rows in set (0.001 sec)
```

To retrieve this information, though, we will have to use the [FOUND_ROWS()](../../../../server/reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/found_rows.md) function like so:


```
SELECT FOUND_ROWS();
```

```
+--------------+
| FOUND_ROWS() |
+--------------+
|            6 |
+--------------+
1 row in set (0.000 sec
```

This value is temporary and will be lost if the connection is terminated. It cannot be retrieved by any other client session. It relates only to the current session and the value for the variable when it was last calculated.


#### Conclusion


There are several more parameters and possibilities for the [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statement that we had to skip to keep this article a reasonable length. A popular one that we left out is the [GROUP BY](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#group-by) clause for calculating aggregate data for columns (e.g., an average). There are several flags for caching results and a clause for exporting a results set to a text file. If you would like to learn more about [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) and all of the options available, look at the on-line documentation for [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statements.

