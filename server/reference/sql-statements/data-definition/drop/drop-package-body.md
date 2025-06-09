# DROP PACKAGE BODY

## Syntax

```
DROP PACKAGE BODY [IF EXISTS]  [ db_name . ] package_name
```

## Description

The `DROP PACKAGE BODY` statement can be used when [Oracle SQL\_MODE](broken-reference) is set.

The `DROP PACKAGE BODY` statement drops the package body (i.e the implementation), previously created using the [CREATE PACKAGE BODY](../create/create-package-body.md) statement.

Note, `DROP PACKAGE BODY` drops only the package implementation, but does not drop the package specification. Use [DROP PACKAGE](drop-package.md) to drop the package entirely (i.e. both implementation and specification).

## See also

* [CREATE PACKAGE](../create/create-package.md)
* [SHOW CREATE PACKAGE](../../administrative-sql-statements/show/show-create-package.md)
* [DROP PACKAGE](drop-package.md)
* [CREATE PACKAGE BODY](../create/create-package-body.md)
* [SHOW CREATE PACKAGE BODY](../../administrative-sql-statements/show/show-create-package-body.md)
* [Oracle SQL\_MODE](broken-reference)

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
