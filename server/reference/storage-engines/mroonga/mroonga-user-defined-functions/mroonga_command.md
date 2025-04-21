
# mroonga_command


## Syntax


```
mroonga_command (command)
```

## Description


`mroonga_command` is a [user-defined function](../../../../server-usage/programming-customizing-mariadb/user-defined-functions/README.md) (UDF) included with the [Mroonga storage engine](../README.md). It passes a command to Groonga for execution. See [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md) for details on creating this UDF if required.


* `command` - string, required parameter specifying the command to pass that will be executed by Groonga. See [the Groonga reference](https://groonga.org/docs/reference/command.html) for a list of commands.


Returns the result of the Groonga command.


## Example


```
SELECT mroonga_command('status');
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| mroonga_command('status')                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {"alloc_count":593,"starttime":1512022368,"start_time":1512022368,"uptime":13510,"version":"7.0.7","n_queries":0,"cache_hit_rate":0.0,"command_version":1,"default_command_version":1,"max_command_version":3} |
```

## See Also


* [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md)

