# ERR\_Packet

## ERR\_Packet

ERR\_Packet indicates that an error occured.

### Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) ERR\_Packet header = 0xFF
* [int<2>](../protocol-data-types.md#fixed-length-integers) error code. see [error list](broken-reference)
* if (errorcode == 0xFFFF) /\* progress reporting \*/
  * [int<1>](../protocol-data-types.md#fixed-length-integers) stage
  * [int<1>](../protocol-data-types.md#fixed-length-integers) max\_stage
  * [int<3>](../protocol-data-types.md#fixed-length-integers) progress
  * [string](../protocol-data-types.md#length-encoded-strings) progress\_info
* else
  * if (next byte = '#')
    * [string<1>](../protocol-data-types.md#fixed-length-strings) sql state marker '#'
    * [string<5>](../protocol-data-types.md#fixed-length-strings)sql state
    * [string](../protocol-data-types.md#fixed-length-strings) human-readable error message
  * else
    * [string](../protocol-data-types.md#fixed-length-strings) human-readable error message

Note that the ERR packet is supposed to send a server error to the client. In particular, all error codes in the range 2000 to 2999 and 5000 to 5999 (inclusive) are reserved for client errors and an ERR packet with such an error code will be considered malformed.

#### See also

["Progress reporting"](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
