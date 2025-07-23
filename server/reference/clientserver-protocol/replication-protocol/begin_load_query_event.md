# BEGIN\_LOAD\_QUERY\_EVENT

This event is written to the binary log file for [LOAD DATA INFILE](../../sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) events if the server variable `binlog_mode` is set to "`STATEMENT`".

## Header

* Event Type = 0x11.

## Fields

Fixed data part:

* [uint<4>](../protocol-data-types.md#fixed-length-integers) The ID of the file.

Variable data part:

* [byte](../protocol-data-types.md#fixed-length-bytes) Null terminated data block.

## Example



<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
