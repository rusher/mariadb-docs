---
description: Application development with MariaDB Connector/Python
---

# Application Development

## Field Information

MariaDB Connector/Python provides the `Fieldinfo` class for retrieving data type and flag information on table columns in the database.

The following example shows how to get the field information for the example table created in [Setup for Examples](setup-for-examples.md):

### Retrieving Field Information for Query Results

To retrieve field information for query results:

1.  Import MariaDB Connector/Python:

    ```python
    # Module Import
    import mariadb
    ```
2.  Define a `select_contacts()` function that retrieves all contacts from the table:

    ```python
    # Print List of Contacts
    def select_contacts(cur):
       """Retrieves the list of contacts from the database"""

       # Retrieve Contacts
       cur.execute("SELECT first_name, last_name, email FROM test.contacts")
    ```
3.  Define a `get_field_info()` function that prints the field information associated with the cursor:

    ```python
    # Get field info from cursor
    def get_field_info(cur):
       """Retrieves the field info associated with a cursor"""

       field_info = mariadb.fieldinfo()

       field_info_text = []

       # Retrieve Column Information
       for column in cur.description:
          column_name = column[0]
          column_type = field_info.type(column)
          column_flags = field_info.flag(column)

          field_info_text.append(f"{column_name}: {column_type} {column_flags}")

       return field_info_text
    ```
4. Call these functions, then print the field information:

> ```python
>  try:
>    conn = mariadb.connect(
>       host="192.0.2.1",
>       port=3306,
>       user="db_user",
>       password="USER_PASSWORD")
>
>    cur = conn.cursor()
>
>    select_contacts(cur)
>
>    field_info_text = get_field_info(cur)
>
>    print("Columns in query results:")
>
>    print("\n".join(field_info_text))
>
>    conn.close()
>
> except Exception as e:
>    print(f"Error: {e}")
> ```
>
> The results should look like this:
>
> ```
> Columns in query results:
> first_name: VAR_STRING
> last_name: VAR_STRING
> email: VAR_STRING
> ```

### Retrieve Field Information for All Tables

To retrieve field information for all tables:

1.  Import MariaDB Connector/Python:

    ```python
    # Module Import
    import mariadb
    ```
2.  Define a `show_tables()` function that executes the [SHOW TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-tables) statement:

    ```python
    # Get list of tables
    def show_tables(cur):
       """Retrieves the list of tables from the database"""

       table_list = []

       # Retrieve Contacts
       cur.execute("SHOW TABLES")

       for (table,) in cur.fetchall():
          table_list.append(table)

       return table_list
    ```
3.  Define a `get_field_info()` function that prints the field information associated with the cursor:

    ```python
    # Get field info from cursor
    def get_field_info(cur):
       """Retrieves the field info associated with a cursor"""

       field_info = mariadb.fieldinfo()

       field_info_text = []

       # Retrieve Column Information
       for column in cur.description:
          column_name = column[0]
          column_type = field_info.type(column)
          column_flags = field_info.flag(column)

          field_info_text.append(f"{column_name}: {column_type} {column_flags}")

       return field_info_text
    ```
4.  Define a `get_table_field_info()` function that prints the field information associated with a table:

    ```python
    # Get field info from cursor
    def get_table_field_info(cur, table):
       """Retrieves the field info associated with a table"""

       # Fetch Table Information
       cur.execute(f"SELECT * FROM {table} LIMIT 1")

       field_info_text = get_field_info(cur)

       return field_info_text
    ```
5. Call these functions, and then print the field information for each table:

> ```python
> try:
>    conn = mariadb.connect(
>       host="192.0.2.1",
>       port=3306,
>       user="db_user",
>       password="USER_PASSWORD",
>       database="test")
>
>    cur = conn.cursor()
>
>    tables = show_tables(cur)
>
>    for table in tables:
>       field_info_text = get_table_field_info(cur, table)
>
>       print(f"Columns in table {table}:")
>       print("\n".join(field_info_text))
>       print("\n")
>
>    conn.close()
>
> except Exception as e:
>    print(f"Error: {e}")
> ```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
