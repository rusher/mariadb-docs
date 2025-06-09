# mysql.spider\_xa Table

The `mysql.spider_xa` table is installed by the [Spider storage engine](../../../../../storage-engines/spider/).

This table uses the [Aria](../../../../../storage-engines/aria/) storage engine.

It contains the following fields:

| Field         | Type        | Null | Key | Default | Description |
| ------------- | ----------- | ---- | --- | ------- | ----------- |
| Field         | Type        | Null | Key | Default | Description |
| format\_id    | int(11)     | NO   | PRI | 0       |             |
| gtrid\_length | int(11)     | NO   | PRI | 0       |             |
| bqual\_length | int(11)     | NO   |     | 0       |             |
| data          | binary(128) | NO   | PRI |         |             |
| status        | char(8)     | NO   | MUL |         |             |

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
