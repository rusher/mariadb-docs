
# Lua Filter

# Lua Filter


The luafilter is a filter that calls a set of functions in a Lua script.


Read the [Lua language documentation](https://www.lua.org/docs.html) for
information on how to write Lua scripts.


*Note:* This module is a part of the experimental module package,
 `<code>maxscale-experimental</code>`.


## Filter Parameters


The luafilter has two parameters. They control which scripts will be called by
the filter. Both parameters are optional but at least one should be defined. If
both `<code>global_script</code>` and `<code>session_script</code>` are defined, the entry points in both
scripts will be called.


### `<code>global_script</code>`


The global Lua script. The parameter value is a path to a readable Lua script
which will be executed.


This script will always be called with the same global Lua state and it can be
used to build a global view of the whole service.


### `<code>session_script</code>`


The session level Lua script. The parameter value is a path to a readable Lua
script which will be executed once for each session.


Each session will have its own Lua state meaning that each session can have a
unique Lua environment. Use this script to do session specific tasks.


## Lua Script Calling Convention


The entry points for the Lua script expect the following signatures:


* `<code>nil createInstance()</code>` - global script only, called when MaxScale is started


  * The global script will be loaded in this function and executed once on a
 global level before calling the createInstance function in the Lua script.
* `<code>nil newSession(string, string)</code>` - new session is created


  * After the session script is loaded, the newSession function in the Lua
 scripts is called. The first parameter is the username of the client and
 the second parameter is the client's network address.
* `<code>nil closeSession()</code>` - session is closed


  * The `<code>closeSession</code>` function in the Lua scripts will be called.
* `<code>(nil | bool | string) routeQuery(string)</code>` - query is being routed


  * The Luafilter calls the `<code>routeQuery</code>` functions of both the session and the
 global script. The query is passed as a string parameter to the
 routeQuery Lua function and the return values of the session specific
 function, if any were returned, are interpreted. If the first value is
 bool, it is interpreted as a decision whether to route the query or to
 send an error packet to the client. If it is a string, the current query
 is replaced with the return value and the query will be routed. If nil is
 returned, the query is routed normally.
* `<code>nil clientReply()</code>` - reply to a query is being routed


  * This function calls the `<code>clientReply</code>` function of the Lua scripts.
* `<code>string diagnostic()</code>` - global script only, print diagnostic information


  * This will call the matching `<code>diagnostics</code>` entry point in the Lua script. If
 the Lua function returns a string, it will be printed to the client.


These functions, if found in the script, will be called whenever a call to the
matching entry point is made.


#### Script Template


Here is a script template that can be used to try out the luafilter. Copy it
into a file and add `<code>global_script=<path to script></code>` into the filter
configuration. Make sure the file is readable by the `<code>maxscale</code>` user.



```
function createInstance()

end

function newSession()

end

function closeSession()

end

function routeQuery(query)

end

function clientReply(query)

end

function diagnostic()

end
```



### Functions Exposed by the Luafilter


The luafilter exposes three functions that can be called from the Lua script.


* `<code>string lua_qc_get_type_mask()</code>`
* Returns the type of the current query being executed as a string. The values
 are the string versions of the query types defined in query_classifier.h
 are separated by vertical bars (`<code>|</code>`).
This function can only be called from the `<code>routeQuery</code>` entry point.
* `<code>string lua_qc_get_operation()</code>`
* Returns the current operation type as a string. The values are defined in
 query_classifier.h.
This function can only be called from the `<code>routeQuery</code>` entry point.
* `<code>string lua_get_canonical()</code>`
* Returns the canonical version of a query by replacing all user-defined constant values with question marks.
This function can only be called from the `<code>routeQuery</code>` entry point.
* `<code>number id_gen()</code>`
* This function generates unique integers that can be used to distinct
 sessions from each other.


## Example Configuration and Script


Here is a minimal configuration entry for a luafilter definition.



```
[MyLuaFilter]
type=filter
module=luafilter
global_script=/path/to/script.lua
```



And here is a script that opens a file in `<code>/tmp/</code>` and logs output to it.



```
f = io.open("/tmp/test.log", "a+")

function createInstance()
    f:write("createInstance\n")
end

function newSession(a, b)
    f:write("newSession for: " .. a .. "@" .. b .. "\n")
end

function closeSession()
    f:write("closeSession\n")
end

function routeQuery(string)
    f:write("routeQuery: " .. string .. " -- type: " .. lua_qc_get_type_mask() .. " operation: " .. lua_qc_get_operation() .. "\n")
end

function clientReply()
    f:write("clientReply\n")
end

function diagnostic()
    f:write("diagnostics\n")
    return "Hello from Lua!"
end
```

