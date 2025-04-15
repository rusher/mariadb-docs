# REGEXP_SUBSTR

#

# Syntax

```
REGEXP_SUBSTR(subject,pattern)
```

#

# Description

Returns the part of the string `subject` that matches the regular expression `pattern`, or an empty string if `pattern` was not found.

The function follows the case sensitivity rules of the effective [collation](/kb/en/data-types-character-sets-and-collations/). Matching is performed case insensitively for case insensitive collations, and case sensitively for case sensitive collations and for binary data.

The collation case sensitivity can be overwritten using the (?i) and (?-i) PCRE flags.

MariaDB uses the [PCRE regular expression](/kb/en/pcre-regular-expressions/) library for enhanced regular expression performance, and `REGEXP_SUBSTR` was introduced as part of this enhancement.

The [default_regex_flags](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_regex_flags) variable addresses the remaining compatibilities between PCRE and the old regex library.

#

# Examples

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