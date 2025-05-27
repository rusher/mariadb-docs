
# Dynamic Column API

This page describes the client-side API for reading and writing [Dynamic Columns](dynamic-columns.md) blobs.


Normally, you should use [Dynamic column functions](dynamic-columns.md#dynamic-columns-functions) which are run inside the MariaDB server and allow one to access Dynamic Columns content without any client-side libraries.


If you need to read/write dynamic column blobs **on the client** for some reason, this API enables that.



## Where to get it


The API is a part of `libmysql` C client library. In order to use it, you need to include this header file


```
#include <mysql/ma_dyncol.h>
```

and link against `libmysql`.


## Data structures


### DYNAMIC_COLUMN


`DYNAMIC_COLUMN` represents a packed dynamic column blob. It is essentially a string-with-length and is defined as follows:


```
/* A generic-purpose arbitrary-length string defined in MySQL Client API */
typedef struct st_dynamic_string
{
  char *str;
  size_t length,max_length,alloc_increment;
} DYNAMIC_STRING;

...

typedef DYNAMIC_STRING DYNAMIC_COLUMN;
```

### DYNAMIC_COLUMN_VALUE


Dynamic columns blob stores {name, value} pairs. `DYNAMIC_COLUMN_VALUE` structure is used to represent the value in accessible form.


```
struct st_dynamic_column_value
{
  DYNAMIC_COLUMN_TYPE type;
  union
  {
    long long long_value;
    unsigned long long ulong_value;
    double double_value;
    struct {
      MYSQL_LEX_STRING value;
      CHARSET_INFO *charset;
    } string;
    struct {
      decimal_digit_t buffer[DECIMAL_BUFF_LENGTH];
      decimal_t value;
    } decimal;
    MYSQL_TIME time_value;
  } x;
};
typedef struct st_dynamic_column_value DYNAMIC_COLUMN_VALUE;
```

Every value has a type, which is determined by the `type` member.



| type | structure field |
| --- | --- |
| type | structure field |
| DYN_COL_NULL | - |
| DYN_COL_INT | value.x.long_value |
| DYN_COL_UINT | value.x.ulong_value |
| DYN_COL_DOUBLE | value.x.double_value |
| DYN_COL_STRING | value.x.string.value, value.x.string.charset |
| DYN_COL_DECIMAL | value.x.decimal.value |
| DYN_COL_DATETIME | value.x.time_value |
| DYN_COL_DATE | value.x.time_value |
| DYN_COL_TIME | value.x.time_value |
| DYN_COL_DYNCOL | value.x.string.value |



Notes


* Values with type `DYN_COL_NULL` do not ever occur in dynamic columns blobs.
* Type `DYN_COL_DYNCOL` means that the value is a packed dynamic blob. This is how nested dynamic columns are done.
* Before storing a value to `value.x.decimal.value`, one must call `mariadb_dyncol_prepare_decimal()` to initialize the space for storage.


### enum_dyncol_func_result


`enum enum_dyncol_func_result` is used as return value.



| value | name | meaning |
| --- | --- | --- |
| value | name | meaning |
| 0 | ER_DYNCOL_OK | OK |
| 0 | ER_DYNCOL_NO | (the same as ER_DYNCOL_OK but for functions which return a YES/NO) |
| 1 | ER_DYNCOL_YES | YES response or success |
| 2 | ER_DYNCOL_TRUNCATED | Operation succeeded but the data was truncated |
| -1 | ER_DYNCOL_FORMAT | Wrong format of the encoded string |
| -2 | ER_DYNCOL_LIMIT | A limit of implementation reached |
| -3 | ER_DYNCOL_RESOURCE | Out of resources |
| -4 | ER_DYNCOL_DATA | Incorrect input data |
| -5 | ER_DYNCOL_UNKNOWN_CHARSET | Unknown character set |



Result codes that are less than zero represent error conditions.


## Function reference


Functions come in pairs:


* `xxx()` operates on the old (pre-MariaDB-10.0.1) dynamic column blob format where columns were identified by numbers.
* `xxx_named()` can operate on both old or new data format. If it modifies the blob, it will convert it to the new data format.


You should use `xxx_named()` functions, unless you need to keep the data compatible with MariaDB versions before 10.0.1.


### mariadb_dyncol_create_many


Create a packed dynamic blob from arrays of values and names.


```
enum enum_dyncol_func_result
mariadb_dyncol_create_many(DYNAMIC_COLUMN *str,
                           uint column_count,
                           uint *column_numbers,
                           DYNAMIC_COLUMN_VALUE *values,
                           my_bool new_string);
enum enum_dyncol_func_result
mariadb_dyncol_create_many_named(DYNAMIC_COLUMN *str,
                                 uint column_count,
                                 MYSQL_LEX_STRING *column_keys,
                                 DYNAMIC_COLUMN_VALUE *values,
                                 my_bool new_string);
```

where


|   |   |   |
| --- | --- | --- |
| str | OUT | Packed dynamic blob will be put here |
| column_count | IN | Number of columns |
| column_numbers | IN | Column numbers array (old format) |
| column_keys | IN | Column names array (new format) |
| values | IN | Column values array |
| new_string | IN | If TRUE then the str will be reinitialized (not freed) before usage |


### mariadb_dyncol_update_many


Add or update columns in a dynamic columns blob. To delete a column, update its value to a "non-value" of type `DYN_COL_NULL`


```
enum enum_dyncol_func_result
mariadb_dyncol_update_many(DYNAMIC_COLUMN *str,
                           uint column_count,
                           uint *column_numbers,
                           DYNAMIC_COLUMN_VALUE *values);
enum enum_dyncol_func_result
mariadb_dyncol_update_many_named(DYNAMIC_COLUMN *str,
                                 uint column_count,
                                 MYSQL_LEX_STRING *column_keys,
                                 DYNAMIC_COLUMN_VALUE *values);
```

|   |   |   |
| --- | --- | --- |
| str | IN/OUT | Dynamic columns blob to be modified. |
| column_count | IN | Number of columns in following arrays |
| column_numbers | IN | Column numbers array (old format) |
| column_keys | IN | Column names array (new format) |
| values | IN | Column values array |


### mariadb_dyncol_exists


Check if column with given name exists in the blob


```
enum enum_dyncol_func_result
mariadb_dyncol_exists(DYNAMIC_COLUMN *str, uint column_number);
enum enum_dyncol_func_result
mariadb_dyncol_exists_named(DYNAMIC_COLUMN *str, MYSQL_LEX_STRING *column_key);
```

|   |   |   |
| --- | --- | --- |
| str | IN | Packed dynamic columns string. |
| column_number | IN | Column number (old format) |
| column_key | IN | Column name (new format) |


The function returns YES/NO or Error code


### mariadb_dyncol_column_count


Get number of columns in a dynamic column blob


```
enum enum_dyncol_func_result
mariadb_dyncol_column_count(DYNAMIC_COLUMN *str, uint *column_count);
```

|   |   |   |
| --- | --- | --- |
| str | IN | Packed dynamic columns string. |
| column_count | OUT | Number of not NULL columns in the dynamic columns string |


### mariadb_dyncol_list


List columns in a dynamic column blob.


```
enum enum_dyncol_func_result
mariadb_dyncol_list(DYNAMIC_COLUMN *str, uint *column_count, uint **column_numbers);
enum enum_dyncol_func_result
mariadb_dyncol_list_named(DYNAMIC_COLUMN *str, uint *column_count,
                          MYSQL_LEX_STRING **column_keys);
```

|   |   |   |
| --- | --- | --- |
| str | IN | Packed dynamic columns string. |
| column_count | OUT | Number of columns in following arrays |
| column_numbers | OUT | Column numbers array (old format). Caller should free this array. |
| column_keys | OUT | Column names array (new format). Caller should free this array. |


### mariadb_dyncol_get


Get a value of one column


```
enum enum_dyncol_func_result
mariadb_dyncol_get(DYNAMIC_COLUMN *org, uint column_number,
                   DYNAMIC_COLUMN_VALUE *value);
enum enum_dyncol_func_result
mariadb_dyncol_get_named(DYNAMIC_COLUMN *str, MYSQL_LEX_STRING *column_key,
                         DYNAMIC_COLUMN_VALUE *value);
```

|   |   |   |
| --- | --- | --- |
| str | IN | Packed dynamic columns string. |
| column_number | IN | Column numbers array (old format) |
| column_key | IN | Column names array (new format) |
| value | OUT | Value of the column |


If the column is not found NULL returned as a value of the column.


### mariadb_dyncol_unpack


Get value of all columns


```
enum enum_dyncol_func_result
mariadb_dyncol_unpack(DYNAMIC_COLUMN *str,
                      uint *column_count,
                      MYSQL_LEX_STRING **column_keys,
                      DYNAMIC_COLUMN_VALUE **values);
```

|   |   |   |
| --- | --- | --- |
| str | IN | Packed dynamic columns string to unpack. |
| column_count | OUT | Number of columns in following arrays |
| column_keys | OUT | Column names array (should be free by caller) |
| values | OUT | Values of the columns array (should be free by caller) |


### mariadb_dyncol_has_names


Check whether the dynamic columns blob uses new data format (the one where columns are identified by names)


```
my_bool mariadb_dyncol_has_names(DYNAMIC_COLUMN *str);
```

|   |   |   |
| --- | --- | --- |
| str | IN | Packed dynamic columns string. |


### mariadb_dyncol_check


Check whether dynamic column blob has correct data format.


```
enum enum_dyncol_func_result
mariadb_dyncol_check(DYNAMIC_COLUMN *str);
```

|   |   |   |
| --- | --- | --- |
| str | IN | Packed dynamic columns string. |


### mariadb_dyncol_json


Get contents od a dynamic columns blob in a JSON form


```
enum enum_dyncol_func_result
mariadb_dyncol_json(DYNAMIC_COLUMN *str, DYNAMIC_STRING *json);
```

|   |   |   |
| --- | --- | --- |
| str | IN | Packed dynamic columns string. |
| json | OUT | JSON representation |


### mariadb_dyncol_val_TYPE


Get dynamic column value as one of the base types


```
enum enum_dyncol_func_result
mariadb_dyncol_val_str(DYNAMIC_STRING *str, DYNAMIC_COLUMN_VALUE *val,
                       CHARSET_INFO *cs, my_bool quote);
enum enum_dyncol_func_result
mariadb_dyncol_val_long(longlong *ll, DYNAMIC_COLUMN_VALUE *val);
enum enum_dyncol_func_result
mariadb_dyncol_val_double(double *dbl, DYNAMIC_COLUMN_VALUE *val);
```

|   |   |   |
| --- | --- | --- |
| str or ll or dbl | OUT | value of the column |
| val | IN | Value |


### mariadb_dyncol_prepare_decimal


Initialize `DYNAMIC_COLUMN_VALUE` before value of `value.x.decimal.value` can be set


```
void mariadb_dyncol_prepare_decimal(DYNAMIC_COLUMN_VALUE *value);
```

|   |   |   |
| --- | --- | --- |
| value | OUT | Value of the column |


This function links `value.x.decimal.value` to `value.x.decimal.buffer`.


### mariadb_dyncol_value_init


Initialize a `DYNAMIC_COLUMN_VALUE` structure to a safe default.


```
#define mariadb_dyncol_value_init(V) (V)->type= DYN_COL_NULL
```

### mariadb_dyncol_column_cmp_named


Compare two column names (currently, column names are compared with memcmp())


```
int mariadb_dyncol_column_cmp_named(const MYSQL_LEX_STRING *s1,
                                    const MYSQL_LEX_STRING *s2);
```


CC BY-SA / Gnu FDL

