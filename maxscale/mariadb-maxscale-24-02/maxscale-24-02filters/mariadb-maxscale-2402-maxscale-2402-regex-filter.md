
# MaxScale 24.02 Regex Filter

# Regex Filter




* [Regex Filter](#regex-filter)

  * [Overview](#overview)
  * [Configuration](#configuration)
  * [Filter Parameters](#filter-parameters)

    * [match](#match)
    * [options](#options)
    * [replace](#replace)
    * [source](#source)
    * [user](#user)
    * [log_file](#log_file)
    * [log_trace](#log_trace)
  * [Examples](#examples)

    * [Example 1 - Replace MySQL 5.1 create table syntax with that for later versions](#example-1-replace-mysql-51-create-table-syntax-with-that-for-later-versions)




## Overview


The Regex filter is a filter module for MariaDB MaxScale that is able to rewrite
query content using regular expression matches and text substitution. The
regular expressions use the
[PCRE2 syntax](https://www.pcre.org/current/doc/html/pcre2syntax.html).


PCRE2 library uses a different syntax than POSIX to refer to capture
groups in the replacement string. The main difference is the usage of the dollar
character instead of the backslash character for references e.g. `<code>$1</code>` instead of
`<code>\1</code>`. For more details about the replacement string differences, please read the
[Creating a new string with substitutions](https://www.pcre.org/current/doc/html/pcre2api.html#SEC34)
chapter in the PCRE2 manual.


## Configuration


The following demonstrates a minimal configuration.



```
[MyRegexFilter]
type=filter
module=regexfilter
match=some string
replace=replacement string

[MyService]
type=service
router=readconnroute
servers=server1
user=myuser
password=mypasswd
filters=MyRegexfilter
```



## Filter Parameters


The Regex filter has two mandatory parameters: *match* and *replace*.


### `<code>match</code>`


* Type: [regex](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md)
* Mandatory: Yes
* Dynamic: Yes


Defines the text in the SQL statements that is replaced.



```
match=TYPE[ ]*=
options=case
```



### `<code>options</code>`


* Type: [enum](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>ignorecase</code>`, `<code>case</code>`, `<code>extended</code>`
* Default: `<code>ignorecase</code>`


The *options*-parameter affects how the patterns are compiled as
[usual](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md).


### `<code>replace</code>`


* Type: string
* Mandatory: Yes
* Dynamic: Yes


This is the text that should replace the part of the SQL-query matching the
pattern defined in *match*.



```
replace=ENGINE =
```



### `<code>source</code>`


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


The optional source parameter defines an address that is used to match against
the address from which the client connection to MariaDB MaxScale
originates. Only sessions that originate from this address will have the match
and replacement applied to them.



```
source=127.0.0.1
```



### `<code>user</code>`


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


The optional user parameter defines a username that is used to match against
the user from which the client connection to MariaDB MaxScale originates. Only
sessions that are connected using this username will have the match and
replacement applied to them.



```
user=john
```



### `<code>log_file</code>`


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


The optional log_file parameter defines a log file in which the filter writes
all queries that are not matched and matching queries with their replacement
queries. All sessions will log to this file so this should only be used for
diagnostic purposes.



```
log_file=/tmp/regexfilter.log
```



### `<code>log_trace</code>`


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


The optional log_trace parameter toggles the logging of non-matching and
matching queries with their replacements into the log file on the *info* level.
This is the preferred method of diagnosing the matching of queries since the log
level can be changed at runtime. For more details about logging levels and
session specific logging, please read the
[Configuration Guide](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md).



```
log_trace=true
```



## Examples


### Example 1 - Replace MySQL 5.1 create table syntax with that for later versions


MySQL 5.1 used the parameter TYPE = to set the storage engine that should be
used for a table. In later versions this changed to be ENGINE =. Imagine you
have an application that you cannot change for some reason, but you wish to
migrate to a newer version of MySQL. The regexfilter can be used to transform
the create table statements into the form that could be used by MySQL 5.5



```
[CreateTableFilter]
type=filter
module=regexfilter
options=ignorecase
match=TYPE\s*=
replace=ENGINE=

[MyService]
type=service
router=readconnroute
servers=server1
user=myuser
password=mypasswd
filters=CreateTableFilter
```

