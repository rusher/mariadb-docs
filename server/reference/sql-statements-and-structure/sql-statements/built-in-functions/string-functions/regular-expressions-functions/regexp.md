
# REGEXP

## Syntax


```
expr REGEXP pat, expr RLIKE pat
```

## Description


Performs a pattern match of a string expression `expr` against a pattern
`pat`. The pattern can be an extended regular expression. See [Regular Expressions Overview](regular-expressions-overview.md) for details on the syntax for
regular expressions (see also [PCRE Regular Expressions](pcre.md)).


Returns `1` if `expr` matches `pat` or `0` if it doesn't match. If either `expr` or `pat` are NULL, the result is NULL.


The negative form [NOT REGEXP](../not-regexp.md) also exists, as an alias for `NOT (string REGEXP pattern)`. RLIKE and NOT RLIKE are synonyms for REGEXP and NOT REGEXP, originally provided for mSQL compatibility.


The pattern need not be a literal string. For example, it can be
specified as a string expression or table column.


**Note:** Because MariaDB uses the C escape syntax in strings (for
example, "\n" to represent the newline character), you must double any
"\" that you use in your REGEXP strings.


REGEXP is not case sensitive, except when used with binary strings.


[MariaDB 10.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes) moved to the PCRE regex library - see [PCRE Regular Expressions](pcre.md) for enhancements to REGEXP introduced in [MariaDB 10.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes).


The [default_regex_flags](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_regex_flags) variable addresses the remaining compatibilities between PCRE and the old regex library.


## Examples


```
SELECT 'Monty!' REGEXP 'm%y%%';
+-------------------------+
| 'Monty!' REGEXP 'm%y%%' |
+-------------------------+
|                       0 |
+-------------------------+

SELECT 'Monty!' REGEXP '.*';
+----------------------+
| 'Monty!' REGEXP '.*' |
+----------------------+
|                    1 |
+----------------------+

SELECT 'new*\n*line' REGEXP 'new\\*.\\*line';
+---------------------------------------+
| 'new*\n*line' REGEXP 'new\\*.\\*line' |
+---------------------------------------+
|                                     1 |
+---------------------------------------+

SELECT 'a' REGEXP 'A', 'a' REGEXP BINARY 'A';
+----------------+-----------------------+
| 'a' REGEXP 'A' | 'a' REGEXP BINARY 'A' |
+----------------+-----------------------+
|              1 |                     0 |
+----------------+-----------------------+

SELECT 'a' REGEXP '^[a-d]';
+---------------------+
| 'a' REGEXP '^[a-d]' |
+---------------------+
|                   1 |
+---------------------+
```

### default_regex_flags examples


[MariaDB 10.0.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10011-release-notes) introduced the [default_regex_flags](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_regex_flags) variable to address the remaining compatibilities between PCRE and the old regex library.


The default behaviour (multiline match is off)


```
SELECT 'a\nb\nc' RLIKE '^b$';
+---------------------------+
| '(?m)a\nb\nc' RLIKE '^b$' |
+---------------------------+
|                         0 |
+---------------------------+
```

Enabling the multiline option using the PCRE option syntax:


```
SELECT 'a\nb\nc' RLIKE '(?m)^b$';
+---------------------------+
| 'a\nb\nc' RLIKE '(?m)^b$' |
+---------------------------+
|                         1 |
+---------------------------+
```

Enabling the multiline option using default_regex_flags


```
SET default_regex_flags='MULTILINE';
SELECT 'a\nb\nc' RLIKE '^b$';
+-----------------------+
| 'a\nb\nc' RLIKE '^b$' |
+-----------------------+
|                     1 |
+-----------------------+
```

## See Also


* [Operator Precedence](../../../../operators/operator-precedence.md)

