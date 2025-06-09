# mysql\_stmt\_send\_long\_data

## Syntax

```c
my_bool mysql_stmt_send_long_data(MYSQL_STMT * stmt,
                                  unsigned int,
                                  const char * data,
                                  unsigned long);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).
* `param_no` - indicates which parameter to associate the data with. Parameters are numbered beginning with 0.
* `data` - a buffer containing the data to send.
* `long` - size of the data buffer.

## Description

Allows sending parameter data to the server in pieces (or chunks), e.g. if the size of a blob exceeds the size of [max\_allowed\_packet](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#max_allowed_packet). This function can be called multiple times to send the parts of a character or binary data value for a column, which must be one of the [TEXT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/text) or [BLOB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/blob) datatypes.

Returns zero on success, nonzero if an error occurred.

{% @marketo/form formid="4316" %}
