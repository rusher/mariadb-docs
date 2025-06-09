# Information Schema XTRADB\_READ\_VIEW Table

The [Information Schema](../../) `XTRADB_READ_VIEW` table contains information about the oldest active transaction in the system.

The `PROCESS` [privilege](../../../../../account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column                              | Description                                                                                                                                    |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Column                              | Description                                                                                                                                    |
| READ\_VIEW\_UNDO\_NUMBER            |                                                                                                                                                |
| READ\_VIEW\_LOW\_LIMIT\_TRX\_NUMBER | Highest transaction number at the time the view was created.                                                                                   |
| READ\_VIEW\_UPPER\_LIMIT\_TRX\_ID   | Highest transaction ID at the time the view was created. Should not see newer transactions with IDs equal to or greater than the value.        |
| READ\_VIEW\_LOW\_LIMIT\_TRX\_ID     | Latest committed transaction ID at the time the oldest view was created. Should see all transactions with IDs equal to or less than the value. |

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
