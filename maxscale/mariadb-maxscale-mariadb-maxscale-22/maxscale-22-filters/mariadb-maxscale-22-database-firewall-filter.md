
# Database Firewall filter

# Database Firewall filter


## Overview


The Database Firewall filter is used to block queries that match a set of
rules. It can be used to prevent harmful queries from reaching the backend
database instances or to limit access to the database based on a more flexible
set of rules compared to the traditional GRANT-based privilege system. Currently
the filter does not support multi-statements.


## Configuration


The Database Firewall filter only requires minimal configuration in the
maxscale.cnf file. The actual rules of the Database Firewall filter are located
in a separate text file. The following is an example of a Database Firewall
filter configuration in maxscale.cnf.



```
[DatabaseFirewall]
type=filter
module=dbfwfilter
rules=/home/user/rules.txt

[Firewalled Routing Service]
type=service
router=readconnrouter
servers=server1
user=myuser
passwd=mypasswd
filters=DatabaseFirewall
```



### Filter Parameters


The Database Firewall filter has one mandatory parameter, `<code>rules</code>`.


#### `<code>rules</code>`


A path to a file with the rule definitions in it. The file should be readable by
the user MariaDB MaxScale is run with. If a relative path is given, the path is
interpreted relative to the module configuration directory. The default module
configuration directory is */etc/maxscale.modules.d*.


#### `<code>action</code>`


This parameter is optional and determines what action is taken when a query
matches a rule. The value can be either `<code>allow</code>`, which allows all matching
queries to proceed but blocks those that don't match, or `<code>block</code>`, which blocks
all matching queries, or `<code>ignore</code>` which allows all queries to proceed.


The following statement types will always be allowed through when `<code>action</code>` is
set to `<code>allow</code>`:


* COM_CHANGE_USER: The user is changed for an active connection
* COM_FIELD_LIST: Alias for the `<code>SHOW TABLES;</code>` query
* COM_INIT_DB: Alias for `<code>USE <db>;</code>`
* COM_PING: Server is pinged
* COM_PROCESS_INFO: Alias for `<code>SHOW PROCESSLIST;</code>`
* COM_PROCESS_KILL: Alias for `<code>KILL <id>;</code>` query
* COM_QUIT: Client closes connection
* COM_SET_OPTION: Client multi-statements are being configured


You can have both blacklist and whitelist functionality by configuring one
filter with `<code>action=allow</code>` and another one with `<code>action=block</code>`. You can then use
different rule files with each filter, one for blacklisting and another one for
whitelisting. After this you only have to add both of these filters to a service
in the following way.



```
[my-firewall-service]
type=service
servers=server1
router=readconnroute
user=maxuser
passwd=maxpwd
filters=dbfw-whitelist|dbfw-blacklist

[dbfw-whitelist]
type=filter
module=dbfwfilter
action=allow
rules=/home/user/whitelist-rules.txt

[dbfw-blacklist]
type=filter
module=dbfwfilter
action=block
rules=/home/user/blacklist-rules.txt
```



If a query is blocked, the filter will return an error to the client with the
error number 1141 and an SQL state of HY000.


#### `<code>log_match</code>`


Log all queries that match a rule. For the `<code>any</code>` matching mode, the name of the
rule that matched is logged and for other matching modes, the name of the last
matching rule is logged. In addition to the rule name the matched user and the
query itself is logged. The log messages are logged at the notice level.


#### `<code>log_no_match</code>`


Log all queries that do not match a rule. The matched user and the query is
logged. The log messages are logged at the notice level.


## Rule syntax


The rules are defined by using the following syntax:



```
rule NAME match RULE [at_times VALUE...] [on_queries {select|update|insert|delete|grant|revoke|drop|create|alter|use|load}]
```



Where *NAME* is the identifier for this rule and *RULE* is the mandatory rule definition.


Rules are identified by their name and have mandatory parts and optional parts.
You can add comments to the rule files by adding the `<code>#</code>` character at
the beginning of the line. Trailing comments are not supported.


The first step of defining a rule is to start with the keyword `<code>rule</code>` which
identifies this line of text as a rule. The second token is identified as
the name of the rule. After that the mandatory token `<code>match</code>` is required
to mark the start of the actual rule definition.


The rule definition must contain exactly one mandatory rule parameter. It can
also contain one of each type of optional rule parameter.


### Mandatory rule parameters


The Database Firewall filter's rules expect a single mandatory parameter for a
rule. You can define multiple rules to cover situations where you would like to
apply multiple mandatory rules to a query.


#### `<code>wildcard</code>`


This rule blocks all queries that use the wildcard character `<code>*</code>`.


##### Example


Use of the wildcard is not allowed:



```
rule examplerule match wildcard
```



#### `<code>columns</code>`


This rule expects a list of values after the `<code>columns</code>` keyword. These values are
interpreted as column names and if a query targets any of these, it is matched.


##### Example


Deny name and salary columns:



```
rule examplerule match columns name salary
```



#### `<code>function</code>`


This rule expects a list of values after the `<code>function</code>` keyword. These values
are interpreted as function names and if a query uses any of these, it is
matched. The symbolic comparison operators (`<code><</code>`, `<code>></code>`, `<code>>=</code>` etc.) are also
considered functions whereas the text versions (`<code>NOT</code>`, `<code>IS</code>`, `<code>IS NOT</code>` etc.) are
not considered functions.


##### Example


Match queries using the *sum* and *count* functions:



```
rule examplerule match function sum count
```



#### `<code>not_function</code>`


This rule expects a list of values after the `<code>not_function</code>` keyword. These values
are interpreted as function names and if a query uses any function other than these,
it is matched. The symbolic comparison operators (`<code><</code>`, `<code>></code>`, `<code>>=</code>` etc.) are also
considered functions whereas the text versions (`<code>NOT</code>`, `<code>IS</code>`, `<code>IS NOT</code>` etc.) are
not considered functions.


If the rule is given no values, then the rule will match a query using any function.


#### Example


Match queries using other functions but the *length* function:



```
rule examplerule match not_function length
```



Match queries using functions:



```
rule examplerule match not_function
```



#### `<code>uses_function</code>`


This rule expects a list of column names after the keyword. If any of the
columns are used with a function, the rule will match. This rule can be
used to prevent the use of a column with a function.


##### Example


Deny function usage with *name* and *address* columns:



```
rule examplerule match uses_function name address
```



#### `<code>function</code>` and `<code>columns</code>`


This rule combines the `<code>function</code>` and `<code>columns</code>` type rules to match if one
of the listed columns uses one of the listed functions. The rule expects
the `<code>function</code>` and `<code>columns</code>` keywords both followed by a list of values.


##### Example


Deny use of the *sum* function with *name* or *address* columns:



```
rule examplerule match function sum columns name address
```



#### `<code>not_function</code>` and `<code>columns</code>`


This rule combines the `<code>not_function</code>` and `<code>columns</code>` type rules to match if
one of the listed columns is used in conjunction with functions other than
the listed ones. The rule expects the `<code>not_function</code>` and `<code>columns</code>` keywords
both followed by a list of values.


If `<code>not_function</code>` is not provided with a list of values, then the rule
matches if any of the columns is used with any function.


##### Example


Match if any other function but *length* is used with the *name* or *address*
columns:



```
rule examplerule match not_function length columns name address
```



Match if any function is used with the _ssn_column:



```
rule examplerule match not_function columns ssn
```



#### `<code>regex</code>`


This rule blocks all queries matching a regex enclosed in single or double
quotes. The regex string expects a PCRE2 syntax regular expression. For more
information about the PCRE2 syntax, read the [PCRE2
documentation](https://www.pcre.org/current/doc/html/pcre2syntax.html).


##### Example


Block selects to accounts:



```
rule examplerule match regex '.*select.*from.*accounts.*'
```



#### `<code>limit_queries</code>`


The limit_queries rule expects three parameters. The first parameter is the
number of allowed queries during the time period. The second is the time period
in seconds and the third is the amount of time in seconds for which the rule is
considered active and blocking.


**WARNING:** Using `<code>limit_queries</code>` in `<code>action=allow</code>` is not supported.


##### Example


Over 50 queries within a window of 5 seconds will block for 100 seconds:



```
rule examplerule match limit_queries 50 5 100
```



#### `<code>no_where_clause</code>`


This rule inspects the query and blocks it if it has no WHERE clause. For
example, this would disallow a `<code>DELETE FROM ...</code>` query without a `<code>WHERE</code>`
clause. This does not prevent wrongful usage of the `<code>WHERE</code>` clause e.g. `<code>DELETE
FROM ... WHERE 1=1</code>`.


##### Example


Queries must have a where clause:



```
rule examplerule match no_where_clause
```



### Optional rule parameters


Each mandatory rule accepts one or more optional parameters. These are to be
defined after the mandatory part of the rule.


#### `<code>at_times</code>`


This rule expects a list of time ranges that define the times when the rule in
question is active. The time formats are expected to be ISO-8601 compliant and
to be separated by a single dash (the - character). For example, to define the
active period of a rule to be 5pm to 7pm, you would include `<code>at times
17:00:00-19:00:00</code>` in the rule definition. The rule uses local time to check if
the rule is active and has a precision of one second.


#### `<code>on_queries</code>`


This limits the rule to be active only on certain types of queries. The possible
values are:


| Keyword | Matching operations |
| --- | --- |
| Keyword | Matching operations |
| select | SELECT statements |
| insert | INSERT statements |
| update | UPDATE statements |
| delete | DELETE statements |
| grant | All grant operations |
| revoke | All revoke operations |
| create | All create operations |
| alter | All alter operations |
| drop | All drop operations |
| use | USE operations |
| load | LOAD DATA operations |


Multiple values can be combined using the pipe character `<code>|</code>` e.g.
`<code>on_queries select|insert|update</code>`.


### Applying rules to users


The `<code>users</code>` directive defines the users to which the rule should be applied.


`<code>users NAME... match { any | all | strict_all } rules RULE...</code>`


The first keyword is `<code>users</code>`, which identifies this line as a user definition
line.


The second component is a list of user names and network addresses in the format
*`<code>user</code>`*`<code>@</code>`*`<code>0.0.0.0</code>`*. The first part is the user name and the second part is
the network address. You can use the `<code>%</code>` character as the wildcard to enable
user name matching from any address or network matching for all users. After the
list of users and networks the keyword match is expected.


After this either the keyword `<code>any</code>`, `<code>all</code>` or `<code>strict_all</code>` is expected. This
defined how the rules are matched. If `<code>any</code>` is used when the first rule is
matched the query is considered as matched and the rest of the rules are
skipped. If instead the `<code>all</code>` keyword is used all rules must match for the query
to be considered as matched. The `<code>strict_all</code>` is the same as `<code>all</code>` but it checks the rules
from left to right in the order they were listed. If one of these does not
match, the rest of the rules are not checked. This could be useful in situations
where you would for example combine `<code>limit_queries</code>` and `<code>regex</code>` rules. By using
`<code>strict_all</code>` you can have the `<code>regex</code>` rule first and the `<code>limit_queries</code>` rule
second. This way the rule only matches if the `<code>regex</code>` rule matches enough times
for the `<code>limit_queries</code>` rule to match.


After the matching part comes the rules keyword after which a list of rule names
is expected. This allows reusing of the rules and enables varying levels of
query restriction.


If a particular *NAME* appears on several `<code>users</code>` lines, then when an
actual user matches that name, the rules of each line are checked
independently until there is a match for the statement in question. That
is, the rules of each `<code>users</code>` line are treated in an *OR* fashion with
respect to each other.


## Module commands


Read [Module Commands](../maxscale-22-reference/mariadb-maxscale-22-module-commands.md) documentation for
details about module commands.


The dbfwfilter supports the following module commands.


### `<code>rules/reload FILTER [FILE]</code>`


Load a new rule file or reload the current rules. New rules are only taken into
use if they are successfully loaded and in cases where loading of the rules
fail, the old rules remain in use. The *FILTER* parameter is the filter instance
whose rules are reloaded. The *FILE* argument is an optional path to a rule file
and if it is not defined, the current rule file is used.


### `<code>rules FILTER</code>`


Shows the current statistics of the rules. The *FILTER* parameter is the filter
instance to inspect.


## Use Cases


### Use Case 1 - Prevent rapid execution of specific queries


To prevent the excessive use of a database we want to set a limit on the rate of
queries. We only want to apply this limit to certain queries that cause unwanted
behaviour. To achieve this we can use a regular expression.


First we define the limit on the rate of queries. The first parameter for the
rule sets the number of allowed queries to 10 queries and the second parameter
sets the rate of sampling to 5 seconds. If a user executes queries faster than
this, any further queries that match the regular expression are blocked for 60
seconds.



```
rule limit_rate_of_queries match limit_queries 10 5 60
rule query_regex match regex '.*select.*from.*user_data.*'
```



To apply these rules we combine them into a single rule by adding a `<code>users</code>` line
to the rule file.



```
users %@% match all rules limit_rate_of_queries query_regex
```



### Use Case 2 - Only allow deletes with a where clause


We have a table which contains all the managers of a company. We want to prevent
accidental deletes into this table where the where clause is missing. This poses
a problem, we don't want to require all the delete queries to have a where
clause. We only want to prevent the data in the managers table from being
deleted without a where clause.


To achieve this, we need two rules. The first rule defines that all delete
operations must have a where clause. This rule alone does us no good so we need
a second one. The second rule blocks all queries that match a regular
expression.



```
rule safe_delete match no_where_clause on_queries delete
rule managers_table match regex '.*from.*managers.*'
```



When we combine these two rules we get the result we want. To combine these two
rules add the following line to the rule file.



```
users %@% match all rules safe_delete managers_table
```

