
# ERR_Packet

## ERR_Packet


ERR_Packet indicates that an error occured.


### Fields



* [int<1>](../protocol-data-types.md#fixed-length-integers) ERR_Packet header = 0xFF
* [int<2>](../protocol-data-types.md#fixed-length-integers) error code. see [error list](../../../../../ref/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4000-to-4099/README.md)
* if (errorcode == 0xFFFF) /* progress reporting */

  * [int<1>](../protocol-data-types.md#fixed-length-integers) stage
  * [int<1>](../protocol-data-types.md#fixed-length-integers) max_stage
  * [int<3>](../protocol-data-types.md#fixed-length-integers) progress
  * [string<lenenc>](../protocol-data-types.md#length-encoded-strings) progress_info
* else

  * if (next byte = '#')

    * [string<1>](../protocol-data-types.md#fixed-length-strings) sql state marker '#'
    * [string<5>](../protocol-data-types.md#fixed-length-strings)sql state
    * [string<EOF>](../protocol-data-types.md#fixed-length-strings) human-readable error message
  * else

    * [string<EOF>](../protocol-data-types.md#fixed-length-strings) human-readable error message



Note that the ERR packet is supposed to send a server error to the client. In particular, all error codes in the range 2000 to 2999 and 5000 to 5999 (inclusive) are reserved for client errors and an ERR packet with such an error code will be considered malformed.


#### See also


["Progress reporting"](../../../../../ref/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting.md)

