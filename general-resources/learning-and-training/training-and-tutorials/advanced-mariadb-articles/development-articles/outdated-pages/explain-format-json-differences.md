
# EXPLAIN FORMAT=JSON Differences From MySQL

[EXPLAIN FORMAT=JSON](explain-formatjson-in-mysql.md) output in MySQL and MariaDB.


MariaDB's EXPLAIN JSON output is different from MySQL's. Here's a list of differences. (Currently they come in no particular order).



## Attached Conditions are Prettier


MySQL prints conditions with too many quotes and braces. Also, subqueries are printed in full (despite that you also get a plan for this subquery). You see something like this:


```
"attached_condition": "((`test`.`t1`.`a` < (/* select#2 */ select min(`test`.`t10`.`b`) from `test`.`t10`)) or (`test`.`t1`.`a` > (/* select#3 */ select max(`test`.`t10`.`b`) from `test`.`t10`)))",

      "attached_condition": "((`test`.`t20`.`col1` > `test`.`t20`.`col2`) or (`test`.`t20`.`col3` = 4))"
```

in MariaDB, the same conditions are printed like this:


```
"attached_condition": "((t1.a < (subquery#2)) or (t1.a > (subquery#3)))"

      "attached_condition": "((t20.col1 > t20.col2) or (t20.col3 = 4))"
```

## JSON Pretty-printer is Smarter


MySQL's JSON pretty-printer is pretty dumb:


```
"possible_keys": [
        "a"
      ],
      "key": "a",
      "used_key_parts": [
        "a"
      ],
```

MariaDB's JSON pretty-printer is a bit smarter:


```
"possible_keys": ["a"],
      "key": "a",
      "key_length": "5",
      "used_key_parts": ["a"],
```

## Index Merge Shows used_key_parts


For multi-part keys, tabular EXPLAIN shows key_length column and leaves the
user to do column-size arithmetic to figure out how many key parts are used.


MySQL's EXPLAIN=JSON may show used_key_parts member which shows which key parts
are used. For range access, key_length is also provided:


```
"access_type": "range",
      "possible_keys": [
        "col1"
      ],
      "key": "col1",
      "used_key_parts": [
        "col1",
        "col2"
      ],
      "key_length": "10",
```

But if you are using index_merge, you will still have to decode key_length:


```
"table": {
      "table_name": "t22",
      "access_type": "index_merge",
      "possible_keys": [
        "col1",
        "col3"
      ],
      "key": "sort_union(col1,col3)",
      "key_length": "10,5",
      "rows": 2398,
```

In MariaDB, you get used_key_parts for all parts of index_merge:


```
"table_name": "t22",
      "access_type": "index_merge",
      "possible_keys": ["col1", "col3"],
      "key_length": "10,5",
      "index_merge": {
        "sort_union": {
          "range": {
            "key": "col1",
            "used_key_parts": ["col1", "col2"]
          },
          "range": {
            "key": "col3",
            "used_key_parts": ["col3"]
          }
        }
```

## Range Checked for Each Record


In MySQL, you need to decode hex index number bitmaps (like in the tabular form):


```
"table": {
          "table_name": "t2",
          "access_type": "ALL",
          "possible_keys": [
            "key1",
            "key3"
          ],
          "rows": 1000,
          "filtered": 100,
          "range_checked_for_each_record": "index map: 0x5"
        }
```

In MariaDB, the keys are shown explicitly


```
"range-checked-for-each-record": {
      "keys": ["key1", "key3"],
      "table": {
        "table_name": "t2",
        "access_type": "ALL",
        "possible_keys": ["key1", "key3"],
        "rows": 1000,
        "filtered": 100
      }
```

also, the structure of display ("range checked ..." embeds the table access) is closer to query plan's structure.
(TODO: should we move "range-checked-for-each-record" inside the "table" ? )


## Full Scan on NULL Key


Tabular EXPLAIN shows "Full scan on NULL key" in the Extra column. MySQL has made a direct translation to JSON:


```
"table": {
        "table_name": "t1",
        "access_type": "ref_or_null",
        ...
        ...
        "rows": 2,
        "filtered": 100,
        "using_index": true,
        "full_scan_on_NULL_key": true,
        ...
      }
```

This is not appropriate for MariaDB because it would like to have place for ANALYZE to show #loops for each construct. It is also illogical - some attribute at the end says "btw all of the above is not used in some cases".
Because of that, MariaDB uses:


```
"full-scan-on-null_key": {
            "table": {
              "table_name": "t1",
              "access_type": "ref_or_null",
              "possible_keys": ["a"],
              "key": "a",
              ...
            }
```

## Join Buffer Plan is Shown in Greater Detail.


MySQL displays "using join buffer" as just another kind of table access. It doesn't separate reading from join buffer and writing to join buffer.


```
"nested_loop": [
      {
        "table": {
          "table_name": "A",
          "access_type": "ALL",
          "rows": 10,
          "filtered": 100,
          "attached_condition": "(`test`.`A`.`b` = 3)"
        }
      },
      {
        "table": {
          "table_name": "B",
          "access_type": "ALL",
          "rows": 20,
          "filtered": 100,
          "using_join_buffer": "Block Nested Loop",
          "attached_condition": "((`test`.`B`.`b` = 4) and ((`test`.`A`.`a` + `test`.`B`.`a`) < 3))"
        }
      }
```

MariaDB shows what is really is going on:


```
"table": {
      "table_name": "A",
      "access_type": "ALL",
      "rows": 10,
      "filtered": 100,
      "attached_condition": "(A.b = 3)"
    },                                                                                                                                                          
    "block-nl-join": {                                                                                                                                          
      "table": {                                                                                                                                                
        "table_name": "B",                                                                                                                                      
        "access_type": "ALL",                                                                                                                                   
        "rows": 10,                                                                                                                                             
        "filtered": 100,                                                                                                                                        
        "attached_condition": "(B.b = 4)"
      },
      "buffer_type": "flat",
      "buffer_size": "128Kb",
      "join_type": "BNL",
      "attached_condition": "((A.a + B.a) < 3)"
    }
```

## TODO: other differences

