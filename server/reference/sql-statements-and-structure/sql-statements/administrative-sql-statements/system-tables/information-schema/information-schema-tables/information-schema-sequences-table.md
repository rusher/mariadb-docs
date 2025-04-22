
# Information Schema SEQUENCES Table


##### MariaDB starting with [11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115)
The [Information Schema](../README.md) `SEQUENCES` table stores information about [sequences](../../../../../sequences/README.md) on the server. 


It contains the following columns. See [CREATE SEQUENCE](../../../../../sequences/create-sequence.md) for details.



| Column | Description |
| --- | --- |
| Column | Description |
| SEQUENCE_CATALOG | Catalog name |
| SEQUENCE_SCHEMA | Database name |
| SEQUENCE_NAME | Sequence name |
| DATA_TYPE | Data type, for example BIGINT or TINYINT UNSIGNED |
| NUMERIC_PRECISION |  |
| NUMERIC_PRECISION_RADIX |  |
| NUMERIC_SCALE |  |
| START_VALUE |  |
| MINIMUM_VALUE |  |
| MAXIMUM_VALUE |  |
| INCREMENT |  |
| CYCLE_OPTION | 1 if the CYCLE OPTION is set, otherwise 0 |



## Example


```
CREATE SEQUENCE s START WITH 100 INCREMENT BY 10;

SELECT * FROM INFORMATION_SCHEMA.SEQUENCES\G
*************************** 1. row ***************************
       SEQUENCE_CATALOG: def
        SEQUENCE_SCHEMA: test
          SEQUENCE_NAME: s
              DATA_TYPE: bigint
      NUMERIC_PRECISION: 64
NUMERIC_PRECISION_RADIX: 2
          NUMERIC_SCALE: 0
            START_VALUE: 100
          MINIMUM_VALUE: 1
          MAXIMUM_VALUE: 9223372036854775806
              INCREMENT: 10
           CYCLE_OPTION: 0
```

## See Also


* [Sequence Overview](../../../../../sequences/sequence-overview.md)
* [CREATE SEQUENCE](../../../../../sequences/create-sequence.md)
* [ALTER SEQUENCE](../../../../../sequences/alter-sequence.md)
* [DROP SEQUENCE](../../../../../sequences/drop-sequence.md)
* [NEXT VALUE FOR](../../../../../sequences/sequence-functions/next-value-for-sequence_name.md)
* [PREVIOUS VALUE FOR](../../../../../sequences/sequence-functions/previous-value-for-sequence_name.md)
* [SETVAL()](../../../../../sequences/sequence-functions/setval.md). Set next value for the sequence.
* [AUTO INCREMENT](../../../../../../data-types/auto_increment.md)
* [Sequence Storage Engine](../../../../../../storage-engines/sequence-storage-engine.md)

