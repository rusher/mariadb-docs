
# Information Schema KEY_CACHES Table

The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>KEY_CACHES</code>` table shows statistics about the [segmented key cache](../../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmarks/segmented-key-cache-performance.md),.


It contains the following columns:



| Column Name | Description |
| --- | --- |
| Column Name | Description |
| KEY_CACHE_NAME | The name of the key cache |
| SEGMENTS | total number of segments (set to NULL for regular key caches) |
| SEGMENT_NUMBER | segment number (set to NULL for any regular key caches and for rows containing aggregation statistics for segmented key caches) |
| FULL_SIZE | memory for cache buffers/auxiliary structures |
| BLOCK_SIZE | size of the blocks |
| USED_BLOCKS | number of currently used blocks |
| UNUSED_BLOCKS | number of currently unused blocks |
| DIRTY_BLOCKS | number of currently dirty blocks |
| READ_REQUESTS | number of read requests |
| READS | number of actual reads from files into buffers |
| WRITE_REQUESTS | number of write requests |
| WRITES | number of actual writes from buffers into files |



## Example


```
SELECT * FROM information_schema.KEY_CACHES \G
********************** 1. row **********************
KEY_CACHE_NAME: default
SEGMENTS: NULL
SEGMENT_NUMBER: NULL
     FULL_SIZE: 134217728
    BLOCK_SIZE: 1024
   USED_BLOCKS: 36
 UNUSED_BLOCKS: 107146
  DIRTY_BLOCKS: 0
 READ_REQUESTS: 40305
         READS: 21
WRITE_REQUESTS: 19239
        WRITES: 358
```
