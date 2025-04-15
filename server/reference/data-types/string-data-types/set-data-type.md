
# SET Data Type

## Syntax


```
SET('value1','value2',...) [CHARACTER SET charset_name] [COLLATE collation_name]
```

## Description


A set. A string object that can have zero or more values, each of
which must be chosen from the list of values 'value1', 'value2', ... A
SET column can have a maximum of 64 members. SET values are
represented internally as integers.


SET values cannot contain commas.


If a SET contains duplicate values, an error will be returned if [strict mode](../../../server-management/variables-and-modes/sql-mode.md#strict-mode) is enabled, or a warning if strict mode is not enabled.


## See Also


* [Character Sets and Collations](character-sets/supported-character-sets-and-collations.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)

