# ELT

#

# Syntax

```
ELT(N, str1[, str2, str3,...])
```

#

# Description

Takes a numeric argument and a series of string arguments. Returns the string that corresponds to the given numeric position. For instance, it returns `str1` if `N` is 1, `str2` if `N` is 2, and so on. If the numeric argument is a `[FLOAT](../../../../data-types/data-types-numeric-data-types/floating-point-accuracy.md)`, MariaDB rounds it to the nearest `[INTEGER](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/intvar_event.md)`. If the numeric argument is less than 1, greater than the total number of arguments, or not a number, `ELT()` returns `NULL`. It must have at least two arguments.

It is complementary to the `[FIELD()](field.md)` function.

#

# Examples

```
SELECT ELT(1, 'ej', 'Heja', 'hej', 'foo');
+------------------------------------+
| ELT(1, 'ej', 'Heja', 'hej', 'foo') |
+------------------------------------+
| ej |
+------------------------------------+

SELECT ELT(4, 'ej', 'Heja', 'hej', 'foo');
+------------------------------------+
| ELT(4, 'ej', 'Heja', 'hej', 'foo') |
+------------------------------------+
| foo |
+------------------------------------+
```

#

# See also

* [FIND_IN_SET()](find_in_set.md) function. Returns the position of a string in a set of strings.
* [FIELD()](field.md) function. Returns the index position of a string in a list.