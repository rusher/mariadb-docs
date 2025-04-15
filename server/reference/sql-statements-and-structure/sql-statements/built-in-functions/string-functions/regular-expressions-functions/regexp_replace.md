
# REGEXP_REPLACE

## Syntax


```
REGEXP_REPLACE(subject, pattern, replace)
```

## Description


`<code>REGEXP_REPLACE</code>` returns the string `<code>subject</code>` with all occurrences of the regular expression `<code>pattern</code>` replaced by the string `<code>replace</code>`. If no occurrences are found, then `<code>subject</code>` is returned as is.


The replace string can have backreferences to the subexpressions in the form \N, where N is a number from 1 to 9.


The function follows the case sensitivity rules of the effective [collation](../../../../../data-types/string-data-types/character-sets/README.md). Matching is performed case insensitively for case insensitive collations, and case sensitively for case sensitive collations and for binary data.


The collation case sensitivity can be overwritten using the (?i) and (?-i) PCRE flags.


MariaDB uses the [PCRE regular expression](pcre.md) library for enhanced regular expression performance, and `<code>REGEXP_REPLACE</code>` was introduced as part of this enhancement.


The [default_regex_flags](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_regex_flags) variable addresses the remaining compatibilities between PCRE and the old regex library.


## Examples


```
SELECT REGEXP_REPLACE('ab12cd','[0-9]','') AS remove_digits;
-> abcd

SELECT REGEXP_REPLACE('<html><head><title>title</title><body>body</body></htm>', '<.+?>',' ')
AS strip_html;
-> title  body
```

Backreferences to the subexpressions in the form `<code>\N</code>`, where N is a number from 1 to 9:


```
SELECT REGEXP_REPLACE('James Bond','^(.*) (.*)$','\\2, \\1') AS reorder_name;
-> Bond, James
```

Case insensitive and case sensitive matches:


```
SELECT REGEXP_REPLACE('ABC','b','-') AS case_insensitive;
-> A-C

SELECT REGEXP_REPLACE('ABC' COLLATE utf8_bin,'b','-') AS case_sensitive;
-> ABC

SELECT REGEXP_REPLACE(BINARY 'ABC','b','-') AS binary_data;
-> ABC
```

Overwriting the collation case sensitivity using the (?i) and (?-i) PCRE flags.


```
SELECT REGEXP_REPLACE('ABC','(?-i)b','-') AS force_case_sensitive;
-> ABC

SELECT REGEXP_REPLACE(BINARY 'ABC','(?i)b','-') AS force_case_insensitive;
-> A-C
```
