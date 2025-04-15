
# MaxScale Filters Masking

# MaxScale Filters Masking


This filter was introduced in MariaDB MaxScale 2.1.


## Overview


With the *masking* filter it is possible to obfuscate the returned
value of a particular column.


For instance, suppose there is a table *person* that, among other
columns, contains the column *ssn* where the social security number
of a person is stored.


With the masking filter it is possible to specify that when the *ssn*
field is queried, a masked value is returned unless the user making
the query is a specific one. That is, when making the query



```
> SELECT name, ssn FROM person;
```



instead of getting the real result, as in



```
+-------+-------------+
+ name  | ssn         |
+-------+-------------+
| Alice | 721-07-4426 |
| Bob   | 435-22-3267 |
...
```



the *ssn* would be masked, as in



```
+-------+-------------+
+ name  | ssn         |
+-------+-------------+
| Alice | XXX-XX-XXXX |
| Bob   | XXX-XX-XXXX |
...
```



## Security


Note that he masking filter alone is *not* sufficient for preventing
access to a particular column. As the masking filter works on the column
name alone a query like



```
> SELECT name, concat(ssn) FROM person;
```



will reveal the value. Also, executing a query like



```
> SELECT name FROM person WHERE ssn = ...;
```



a sufficient number of times with different *ssn* values, will, eventually,
reveal the social security number of all persons in the database.


For a secure solution, the masking filter *must* be combined with the
firewall filter to prevent the use of functions using which the masking
can be bypassed.


In a future release, the combined use of the masking filter and the
database firewall filter will be simplified.


## Limitations


The masking filter can *only* be used for masking columns of the following
types: `<code>BINARY</code>`, `<code>VARBINARY</code>`, `<code>CHAR</code>`, `<code>VARCHAR</code>`, `<code>BLOB</code>`, `<code>TINYBLOB</code>`,
`<code>MEDIUMBLOB</code>`, `<code>LONGBLOB</code>`, `<code>TEXT</code>`, `<code>TINYTEXT</code>`, `<code>MEDIUMTEXT</code>`, `<code>LONGTEXT</code>`,
`<code>ENUM</code>` and `<code>SET</code>`. If the type of the column is something else, then no
masking will be performed.


Currently, the masking filter can only work on packets whose payload is less
than 16MB. If the masking filter encounters a packet whose payload is exactly
that, thus indicating a situation where the payload is delivered in multiple
packets, the value of the parameter `<code>large_payloads</code>` specifies how the masking
filter should handle the situation.


## Configuration


The masking filter is taken into use with the following kind of
configuration setup.



```
[Mask-SSN]
type=filter
module=masking
rules=...

[SomeService]
type=service
...
filters=Mask-SSN
```



## Filter Parameters


The masking filter has one mandatory parameter - `<code>rules</code>`.


#### `<code>rules</code>`


Specifies the path of the file where the masking rules are stored.
A relative path is interpreted relative to the *module configuration directory*
of MariaDB MaxScale. The default module configuration directory is
*/etc/maxscale.modules.d*.



```
rules=/path/to/rules-file
```



#### `<code>warn_type_mismatch</code>`


With this optional parameter the masking filter can be instructed to log
a warning if a masking rule matches a column that is not of one of the
allowed types.


The values that can be used are `<code>never</code>` and `<code>always</code>`, with `<code>never</code>` being
the default.



```
warn_type_mismatch=always
```



#### `<code>large_payload</code>`


This optional parameter specifies how the masking filter should treat
payloads larger than `<code>16MB</code>`, that is, payloads that are delivered in
multiple MySQL protocol packets.


The values that can be used are `<code>ignore</code>`, which means that columns in
such payloads are not masked, and `<code>abort</code>`, which means that if such
payloads are encountered, the client connection is closed. The default
is `<code>abort</code>`.


Note that the aborting behaviour is applied only to resultsets that
contain columns that should be masked. There are *no* limitations on
resultsets that do not contain such columns.



```
large_payload=ignore
```



# Rules


The masking rules are expressed as a JSON object.


The top-level object is expected to contain a key `<code>rules</code>` whose
value is an array of rule objects.



```
{
    "rules": [ ... ]
}
```



## Rule


Each rule in the rules array is a JSON object, expected to
contain the keys `<code>replace</code>`, `<code>with</code>`, `<code>applies_to</code>` and
`<code>exempted</code>`. The two former ones are obligatory and the two
latter ones optional.



```
{
    "rules": [
        {
            "replace": { ... },
            "with": { ... },
            "applies_to": [ ... ],
            "exempted": [ ... ]
        }
    ]
}
```



#### `<code>replace</code>`


The value of this key is an object that specifies the column
whose values should be masked. The object must contain the key
`<code>column</code>` and may contain the keys `<code>table</code>` and `<code>database</code>`. The
value of these keys must be a string.


If only `<code>column</code>` is specified, then a column with that name
matches irrespective of the table and database. If `<code>table</code>`
is specified, then the column matches only if it is in a table
with the specified name, and if `<code>database</code>` is specified when
the column matches only if it is in a database with the
specified name.



```
{
    "rules": [
        {
            "replace": {
                "database": "db1",
                "table": "person",
                "column": "ssn"
            },
            "with": { ... },
            "applies_to": [ ... ],
            "exempted": [ ... ]
        }
    ]
}
```



#### `<code>with</code>`


The value of this key is an object that specifies what the value of the matched
column should be replaced with. Currently, the object is expected to contain
either the key `<code>value</code>` or the key `<code>fill</code>`. The value of both must be a string
with length greater than zero. If both keys are specified, `<code>value</code>` takes
precedence. If `<code>fill</code>` is not specified, the default `<code>X</code>` is used as its value.


If `<code>value</code>` is specified, then its value is used to replace the actual value
verbatim and the length of the specified value must match the actual returned
value (from the server) exactly. If the lengths do not match, the value of
`<code>fill</code>` is used to mask the actual value.


When the value of `<code>fill</code>` (fill-value) is used for masking the returned value,
the fill-value is used as many times as necessary to match the length of the
return value. If required, only a part of the fill-value may be used in the end
of the mask value to get the lengths to match.



```
{
    "rules": [
        {
            "replace": {
                "column": "ssn"
            },
            "with": {
                "value": "XXX-XX-XXXX"
            },
            "applies_to": [ ... ],
            "exempted": [ ... ]
        },
        {
            "replace": {
                "column": "age"
            },
            "with": {
                "fill": "*"
            },
            "applies_to": [ ... ],
            "exempted": [ ... ]
        },
        {
            "replace": {
                "column": "creditcard"
            },
            "with": {
                "value": "1234123412341234",
                "fill": "0"
            },
            "applies_to": [ ... ],
            "exempted": [ ... ]
        },
    ]
}
```



#### `<code>applies_to</code>`


With this *optional* key, whose value must be an array of strings,
it can be specified what users the rule is applied to. Each string
should be a MariaDB account string, that is, `<code>%</code>` is a wildcard.



```
{
    "rules": [
        {
            "replace": { ... },
            "with": { ... },
            "applies_to": [ "'alice'@'host'", "'bob'@'%'" ],
            "exempted": [ ... ]
        }
    ]
}
```



If this key is not specified, then the masking is performed for all
users, except the ones exempted using the key `<code>exempted</code>`.


#### `<code>exempted</code>`


With this *optional* key, whose value must be an array of strings,
it can be specified what users the rule is *not* applied to. Each
string should be a MariaDB account string, that is, `<code>%</code>` is a wildcard.



```
{
    "rules": [
        {
            "replace": { ... },
            "with": { ... },
            "applies_to": [ ... ],
            "exempted": [ "'admin'" ]
        }
    ]
}
```



## Module commands


Read [Module Commands](../maxscale-21-reference/mariadb-maxscale-21-module-commands.md) documentation for details about module commands.


The masking filter supports the following module commands.


### `<code>reload</code>`


Reload the rules from the rules file. The new rules are taken into use
only if the loading succeeds without any errors.



```
MaxScale> call command masking reload MyMaskingFilter
```



`<code>MyMaskingFilter</code>` refers to a particular filter section in the
MariaDB MaxScale configuration file.


# Example


In the following we configure a masking filter *MyMasking* that should always log a
warning if a masking rule matches a column that is of a type that cannot be masked,
and that should abort the client connection if a resultset package is larger than
16MB. The rules for the masking filter are in the file `<code>masking_rules.json</code>`.


### Configuration



```
[MyMasking]
type=filter
module=masking
warn_type_mismatch=always
large_payload=abort
rules=masking_rules.json

[MyService]
type=service
...
filters=MyMasking
```



### `<code>masking_rules.json</code>`


The rules specify that the data of a column whose name is `<code>ssn</code>`, should
be replaced with the string *012345-ABCD*. If the length of the data is
not exactly the same as the length of the replacement value, then the
data should be replaced with as many *X* characters as needed.



```
{
    "rules": [
        {
            "replace": {
                "column": "ssn"
            },
            "with": {
                "value": "012345-ABCD",
                "fill": "X"
            }
        }
    ]
}
```

