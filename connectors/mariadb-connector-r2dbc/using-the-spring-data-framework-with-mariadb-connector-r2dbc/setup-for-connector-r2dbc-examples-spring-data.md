# Setup for Connector/R2DBC Examples (Spring Data)

## Overview

The examples in this MariaDB Connector/R2DBC documentation depend on a database test and table contact.

## Create the Schema

Create a test database if one does not exist with the CREATE DATABASE statement:

```sql
CREATE DATABASE IF NOT EXISTS test;
```

## Create the User

1. Create a user account to test connectivity with the CREATE USER statement:

```sql
CREATE USER 'connr2dbc_test'@'192.0.2.50'
   IDENTIFIED BY 'db_user_password';
```

1. Ensure that the user account has privileges to access the tables with the GRANT statement:

```sql
GRANT ALL PRIVILEGES
   ON test.*
   TO 'connr2dbc_test'@'192.0.2.50';
```

Copyright © 2025 MariaDB


{% @marketo/form formId="4316" %}
