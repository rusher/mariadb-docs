# Transactions with MariaDB Connector/Python

A database transaction is a single unit of logic. A transaction can consist of one or more database operations. Transactions are useful and sometimes essential in several types of data operations. For example, many applications require that a set of SQL statements either complete, or fail, as a single unit.

The common characteristics of transactions are atomicity, consistency, isolation, and durability, what is termed as ACID (atomic, consistent, isolated, durable) transactions. MariaDB transactions are [ACID compliant](https://mariadb.com/resources/blog/acid-compliance-what-it-means-and-why-you-should-care/).

### Transactions with MariaDB Connector/Python

You can enable auto-committed transactions using the `autocommit` connection attribute.

By default, MariaDB Connector/Python disables auto-commit. With auto-commit disabled transactions must be committed explicitly.

You may want to use explicit transactions so that either all statements are committed together or all statements are completely rolled back. For example, explicit transactions are almost always necessary for financial transactions. Otherwise, a situation could occur where, money is removed from the payer's account, but it is not properly moved to the payee's account.

To use explicit transactions, MariaDB's standard transaction related statements can be executed with MariaDB Connector/Python using a cursor:

* [START TRANSACTION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/start-transaction)
* [ROLLBACK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/rollback)
* [COMMIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/commit)

Additionally, instances of the `Connection` class can use the `commit()` and `rollback()` methods instead.

### Code Example: Transactions

The following example shows how to update the example table `accounts` created in [Setup for Examples](setup-for-examples.md). The email data is updated from the format `firstnamelastname@example.com` to the new format `firstname.lastname@example.com`. Call the functions to update data in a transaction. Because the updates are made within a transaction, either all contacts' emails are updated to the new format, or none are.

```python
# Module Import
import mariadb
import sys

# Adds account
def add_account(cur, first_name, last_name, email, amount):
   """Adds the given account to the accounts table"""

   cur.execute("INSERT INTO test.accounts(first_name, last_name, email, amount) VALUES (?, ?, ?, ?)",
      (first_name, last_name, email, amount))

# Update Last Name
def update_account_amount(cur, email, change):
   """Updates amount of an account in the table"""

   cur.execute("UPDATE test.accounts SET amount=(amount-?) WHERE email=?",
         (change, email))

# Instantiate Connection
try:
   conn = mariadb.connect(
      host="192.0.2.1",
      port=3306,
      user="db_user",
      password="USER_PASSWORD")

   cur = conn.cursor()

   new_account_fname = "John"
   new_account_lname = "Rockefeller"
   new_account_email = "john.rockefeller@example.com"
   new_account_amount = 418000000000.00

   add_account(cur,
      new_account_fname,
      new_account_lname,
      new_account_email,
      new_account_amount)

   new_account_change = 1000000.00

   update_account_amount(cur,
      new_account_email,
      new_account_change)

   conn.commit()
   conn.close()
except Exception as e:
   print(f"Error committing transaction: {e}")

   conn.rollback()
```

* The functions to add and update account data must be defined before being called with regards to their ordering in the script.
* The `add_account()` function adds a new account to the table.
* The `execute()` method is called on the cursor in the `add_account()` method, which executes an [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) statement to insert a new row into the table.
* The `update_account_amount()` function updates the amount in an account associated with the given email.
* The `execute()` method is called on the cursor in the `update_account_amount()` method, which executes an [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) statement to update a row in the table.
* In each of these functions, the query string is the first value specified to the `execute()` method.
* In each of these functions, the new values for the row, and the values for the where clause if present, are specified to the `execute()` method using a tuple.
* In each of these functions, the values in the tuple are substituted for the question marks (`?`) in the query string.

Confirm the `test.accounts` table was properly updated by using [MariaDB Client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client) to execute a [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statement:

```sql
SELECT * from test.accounts;
```

```
+----+------------+-------------+------------------------------+-----------------+
| id | first_name | last_name   | email                        | amount          |
+----+------------+-------------+------------------------------+-----------------+
|  1 | John       | Rockefeller | john.rockefeller@example.com | 417999000000.00 |
+----+------------+-------------+------------------------------+-----------------+
```

### Code Example: Enable Auto-commit

MariaDB Connector/Python disables auto-committing transactions by default, following the PEP-249 DBAPI 2.0 specification.

To auto-commit transactions, enable auto-commit either when initializing a connection or by manually setting the `autocommit` connection attribute.

To enable auto-commit using `connect()`:

```python
try:
   conn = mariadb.connect(
      host="192.0.2.1",
      port=3306,
      user="db_user",
      password="USER_PASSWORD",
      autocommit=True)

except Exception as e:
     print(f"Connection Error: {e}")
```

To enable auto-commit using `autocommit` connection attribute:

```python
# Enable Auto-commit
conn.autocommit = True
```

With auto-commit enabled, MariaDB Connector/Python commits a transaction after each statement executes.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
