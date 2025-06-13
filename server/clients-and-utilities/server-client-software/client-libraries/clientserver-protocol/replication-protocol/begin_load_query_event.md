
# BEGIN_LOAD_QUERY_EVENT

This event is written into the binary log file for [LOAD DATA INFILE](https://mariadb.com/kb/en/LOAD_DATA_INFILE) events if the server variable binlog_mode was set to "STATEMENT".


### Header


* Event Type = 0x11


### Fields


Fixed data part:





* [uint<4>](../protocol-data-types.md#fixed-length-integers) The ID of the file


Variable data part:


* [byte<NULL>](../protocol-data-types.md#fixed-length-bytes) Null terminated data block.


### Example


TODO: Add an example


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
