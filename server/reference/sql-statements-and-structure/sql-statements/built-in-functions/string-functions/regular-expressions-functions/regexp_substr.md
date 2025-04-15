
# REGEXP_SUBSTR

## Syntax


```
REGEXP_SUBSTR(subject,pattern)
```

## Description


Returns the part of the string `<code>subject</code>` that matches the regular expression `<code>pattern</code>`, or an empty string if `<code>pattern</code>` was not found.


The function follows the case sensitivity rules of the effective [collation](../../../../../data-types/string-data-types/character-sets/README.md). Matching is performed case insensitively for case insensitive collations, and case sensitively for case sensitive collations and for binary data.


The collation case sensitivity can be overwritten using the (?i) and (?-i) PCRE flags.


MariaDB uses the [PCRE regular expression](pcre.md) library for enhanced regular expression performance, and `<code>REGEXP_SUBSTR</code>` was introduced as part of this enhancement.


The [default_regex_flags](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_regex_flags) variable addresses the remaining compatibilities between PCRE and the old regex library.


## Examples


```
SELECT REGEXP_SUBSTR('ab12cd','[0-9]+');
-> 12

SELECT REGEXP_SUBSTR(
  'See https://mariadb.org/en/foundation/ for details',
  'https?://[^/]*');
-> https://mariadb.org
```

```
SELECT REGEXP_SUBSTR('ABC','b');
-> B

SELECT REGEXP_SUBSTR('ABC' COLLATE utf8_bin,'b');
->

SELECT REGEXP_SUBSTR(BINARY'ABC','b');
->

SELECT REGEXP_SUBSTR('ABC','(?i)b');
-> B

SELECT REGEXP_SUBSTR('ABC' COLLATE utf8_bin,'(?+i)b');
-> B
```
