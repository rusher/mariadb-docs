# LOAD DATA With LOAD DATA LOCAL INFILE

## Overview

MariaDB Enterprise Server users can import data into a database using the `LOAD DATA LOCAL INFILE` statement:

* The `LOAD DATA LOCAL INFILE` statement can import data from TSV and CSV files
* The `LOAD DATA LOCAL INFILE` statement can be executed by any client or connector

## Compatibility

## Import Schema

1. Determine the [connection parameters](../../../mariadb-quickstart-guides/mariadb-connecting-guide.md#connection-parameters) for your MariaDB Enterprise Server database.
2. Use [mariadb client](../../mariadb-client/) with the connection information to import your schema into your MariaDB Enterprise Server database:

```
$ mariadb --host FULLY_QUALIFIED_DOMAIN_NAME --port TCP_PORT \
      --user DATABASE_USER --password \
      --ssl-verify-server-cert \
      --ssl-ca ~/PATH_TO_PEM_FILE \
      --default-character-set=utf8 \
      < mariadb_schema.sql
```

* Replace `FULLY_QUALIFIED_DOMAIN_NAME` with the IP address or Fully Qualified Domain Name of your database
* Replace `TCP_PORT` with the TCP port of your database
* Replace `DATABASE_USER` with the username for your database user account
* If TLS is required, replace `/PATH_TO_PEM_FILE` with the path to the certificate authority chain (.pem) file

3. After the command is executed, you is prompted for the password of your database user account.

## Import Data

1. Determine the connection parameters for your MariaDB Enterprise Server database.
2. Connect with the [mariadb client](../../mariadb-client/) and specify the `--local-infile` option, which is needed by the next step:

```
$ mariadb --host FULLY_QUALIFIED_DOMAIN_NAME --port TCP_PORT \
      --user DATABASE_USER --password \
      --ssl-verify-server-cert \
      --ssl-ca ~/PATH_TO_PEM_FILE \
      --default-character-set=utf8 \
      --local-infile
```

**Replace `FULLY_QUALIFIED_DOMAIN_NAME` with the IP address or Fully Qualified Domain Name of your database**

**Replace `TCP_PORT` with the TCP port of your database**

**Replace `DATABASE_USER` with the username for your database user account**

**If TLS is required, replace `/PATH_TO_PEM_FILE` with the path to the certificate authority chain (.pem) file**

3. After the command is executed, you is prompted for the password of your database user account.
4. For each table that you want to import, execute the `LOAD DATA LOCAL INFILE` statement to import the data from the TSV or CSV file into your MariaDB Enterprise Server database.

For a TSV file:

```
LOAD DATA LOCAL INFILE 'contacts.tsv'
INTO TABLE accounts.contacts;
For a CSV file:
```

```
LOAD DATA LOCAL INFILE 'contacts.csv'
INTO TABLE accounts.contacts
FIELDS TERMINATED BY ',';
```

## MariaDB Connectors

To execute the `LOAD DATA LOCAL INFILE` statement, most clients and connectors require a specific option to be enabled.

The section above mentions that [mariadb client](../../mariadb-client/) requires the `--local-infile` option to be specified.

If you are using a [MariaDB Connector](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors) instead of the [mariadb client](../../mariadb-client/), then you must use a different method to enable support for the `LOAD DATA LOCAL INFILE` statement.

If you are using [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c), the `MYSQL_OPT_LOCAL_INFILE` option can be set with the mysql\_optionsv() function:

```
/* enable local infile */
unsigned int enable_local_infile = 1;
mysql_optionsv(mysql, MYSQL_OPT_LOCAL_INFILE, (void *) &enable_local_infile);
```

If you are using [MariaDB Connector/J](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j), the allowLocalInfile parameter can be set for the connection:

```
Connection connection = DriverManager.getConnection("jdbc:mariadb://FULLY_QUALIFIED_DOMAIN_NAME:TCP_PORT/test?user=DATABASE_USER&password=DATABASE_PASSWORD&allowLocalInfile=true");
```

If you are using [MariaDB Connector/Node.js](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs/node-js-connection-options), the permitLocalInfile parameter can be set for the connection:

```
mariadb.createConnection({
   host: 'FULLY_QUALIFIED_DOMAIN_NAME',
   port: 'TCP_PORT',
   user:'DATABASE_USER',
   password: 'DATABASE_PASSWORD',
   permitLocalInfile: 'true'
 });
```

If you are using [MariaDB Connector/Python](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/connectors-quickstart-guides/connector-python-guide), the `local_infile` parameter can be set for the connection:

```
conn = mariadb.connect(
   user="DATABASE_USER",
   password="DATABASE_PASSWORD",
   host="FULLY_QUALIFIED_DOMAIN_NAME",
   port=TCP_PORT,
   local_infile=true)
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
