
# REPLACE Function

## Syntax


```
REPLACE(str,from_str,to_str)
```

## Description


Returns the string `<code>str</code>` with all occurrences of the string `<code>from_str</code>`
replaced by the string `<code>to_str</code>`. REPLACE() performs a case-sensitive
match when searching for `<code>from_str</code>`.


## Examples


```
SELECT REPLACE('www.mariadb.org', 'w', 'Ww');
+---------------------------------------+
| REPLACE('www.mariadb.org', 'w', 'Ww') |
+---------------------------------------+
| WwWwWw.mariadb.org                    |
+---------------------------------------+
```
