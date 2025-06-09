# ColumnStore Information Functions

1. [Functions "Functions"](columnstore-information-functions.md#functions)
2. [Example "Example"](columnstore-information-functions.md#example)

## Functions

MariaDB ColumnStore Information Functions are selectable pseudo functions that return MariaDB ColumnStore specific “meta” information to ensure queries can be locally directed to a specific node. These functions can be specified in the projection (SELECT), WHERE, GROUP BY, HAVING and ORDER BY portions of the SQL statement and will be processed in a distributed manner.

| Function                     | Description                                                                                                            |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Function                     | Description                                                                                                            |
| idbBlockId(column)           | The Logical Block Identifier (LBID) for the block containing the physical row                                          |
| idbDBRoot(column)            | The DBRoot where the physical row resides                                                                              |
| idbExtentId(column)          | The Logical Block Identifier (LBID) for the first block in the extent containing the physical row                      |
| idbExtentMax(column)         | The max value from the extent map entry for the extent containing the physical row                                     |
| idbExtentMin(column)         | The min value from the extent map entry for the extent containing the physical row                                     |
| idbExtentRelativeRid(column) | The row id (1 to 8,388,608) within the column's extent                                                                 |
| idbLocalPm()                 | The PM from which the query was launched. This function will return NULL if the query is launched from a standalone UM |
| idbPartition(column)         | The three part partition id (Directory.Segment.DBRoot)                                                                 |
| idbPm(column)                | The PM where the physical row resides                                                                                  |
| idbSegmentDir(column)        | The lowest level directory id for the column file containing the physical row                                          |
| idbSegment(column)           | The number of the segment file containing the physical row                                                             |


{% @marketo/form formId="4316" %}
