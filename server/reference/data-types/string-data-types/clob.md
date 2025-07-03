# CLOB

## Overview

See [LONGTEXT](longtext.md).

## EXAMPLES

```sql
SET sql_mode='oracle';

CREATE TABLE clob_example (
  example CLOB
);
```

```sql
SHOW CREATE TABLE clob_example\G
```

```sql
*************************** 1. row ***************************
       Table: clob_example
Create Table: CREATE TABLE "clob_example" (
  "example" longtext DEFAULT NULL
)
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
