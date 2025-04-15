
# MariaDB MaxScale plugin development guide

# MariaDB MaxScale plugin development guide


This document and the attached example code explain prospective plugin
developers the MariaDB MaxScale plugin API and also present and explain some
best practices and possible pitfalls in module development. We predict that
*filters* and *routers* are the module types developers are most likely to work
on, so the APIs of these two are discussed in detail.




* [MariaDB MaxScale plugin development guide](#mariadb-maxscale-plugin-development-guide)

  * [Introduction](#introduction)
  * [Module categories](#module-categories)
  * [Common definitions and headers](#common-definitions-and-headers)

    * [Module information container](#module-information-container)
  * [Module API](#module-api)

    * [Overview](#overview)
    * [General module management](#general-module-management)
    * [Protocol](#protocol)
    * [Authenticator](#authenticator)
    * [Filter and Router](#filter-and-router)
    * [Monitor](#monitor)
  * [Compiling, installing and running](#compiling-installing-and-running)

    * [Hands-on example: RoundRobinRouter](#hands-on-example-roundrobinrouter)
  * [Summary and conclusion](#summary-and-conclusion)




## Introduction


MariaDB MaxScale is designed to be an extensible program. Much, if not most, of
the actual processing is done by plugin modules. Plugins receive network data,
process it and relay it to its destination. The MaxScale core loads plugins,
manages client sessions and threads and, most importantly, offers a selection of
functions for the plugins to call upon. This collection of functions is called
the *MaxScale Public Interface* or just **MPI** for short.


The plugin modules are shared libraries (.so-files) implementing a set of
interface functions, the plugin API. Different plugin types have different APIs,
although there are similarities. The MPI is a set of C and C++ header files,
from which the module code includes the ones required. MariaDB MaxScale is
written in C/C++ and the plugin API is in pure C. Although it is possible
to write plugins in any language capable of exposing a C interface and
dynamically binding to the core program, in this document we assume plugin
modules are written in C++.


The *RoundRobinRouter* is a practical example of a simple router plugin. The
RoundRobinRouter is compiled, installed and ran in [section
5.1](#hands-on-example:-roundrobinrouter). The source for the router is located
in the `<code>examples</code>`-folder.


## Module categories


This section lists all the module types and summarises their core tasks. The
modules are listed in the order a client packet would typically travel through.
For more information about a particular module type, see the corresponding
folder in `<code>MaxScale/Documentation/</code>`, located in the main MariaDB MaxScale
repository.


**Protocol** modules implement I/O between clients and MaxScale, and between
MaxScale and backend servers. Protocol modules read and write to socket
descriptors using raw I/O functions provided by the MPI, and implement
protocol-specific I/O functions to be used through a common interface. The
Protocol module API is defined in `<code>protocol.h</code>`. Currently, the only implemented
database protocol is *MySQL*.


**Authenticator** modules retrieve user account information from the backend
databases, store it and use it to authenticate connecting clients. MariaDB
MaxScale includes authenticators for MySQL (normal and GSSApi). The
authenticator API is defined in `<code>authenticator.h</code>`.


**Filter** modules process data from clients before routing. A data buffer may
travel through multiple filters before arriving in a router. For a data buffer
going from a backend to the client, the router receives it first and the
filters receive it in reverse order. MaxScale includes a healthly selection of
filters ranging from logging, overwriting query data and caching. The filter
API is defined in `<code>filter.h</code>`.


**Router** modules route packets from the last filter in the filter chain to
backends and reply data from backends to the last filter. The routing decisions
may be based on a variety of conditions; typically packet contents and backend
status are the most significant factors. Routers are often used for load
balancing, dividing clients and even individual queries between backends.
Routers use protocol functions to write to backends, making them somewhat
protocol-agnostic. The router API is defined in `<code>router.h</code>`.


**Monitor** modules do not process data flowing through MariaDB MaxScale, but
support the other modules in their operation by updating the status of the
backend servers. Monitors are ran in their own threads to minimize
interference to the worker threads. They periodically connect to all their
assigned backends, query their status and write the results in global structs.
The monitor API is defined in `<code>monitor.h</code>`.


## Common definitions and headers


Generally, most type definitions, macros and functions exposed by the MPI to be
used by modules are prefixed with **MXS**. This should avoid name collisions
in the case a module includes many symbols from the MPI.


Every compilation unit in a module should begin with `<code>#define MXS_MODULE_NAME
"<name>"</code>`. This definition will be used by log macros for clarity, prepending
`<code><name></code>` to every log message. Next, the module should
`<code>#include <maxscale/cppdefs.h></code>` (for C++) or `<code>#include <maxscale/cdefs.h></code>` (for
C). These headers contain compilation environment dependent definitions and
global constants, and include some generally useful headers. Including one of
them first in every source file enables later global redefinitions across all
MaxScale modules. If your module is composed of multiple source files, the above
should be placed to a common header file included in the beginning of the source
files. The file with the module API definition should also include the header
for the module type, e.g. `<code>filter.h</code>`.


Other common MPI header files required by most modules are listed in the table
below.


| Header | Contents |
| --- | --- |
| Header | Contents |
| alloc.h | Malloc, calloc etc. replacements |
| buffer.h | Packet buffer management |
| config.h | Configuration settings |
| dcb.h | I/O using descriptor control blocks |
| debug.h | Debugging macros |
| modinfo.h | Module information structure |
| server.h | Backend server information |
| service.h | Service definition |
| session.h | Client session definition |
| logmanager.h | Logging macros and functions |


### Module information container


A module must implement the `<code>MXS_CREATE_MODULE()</code>`-function, which returns a
pointer to a `<code>MXS_MODULE</code>`-structure. This function is called by the module
loader during program startup. `<code>MXS_MODULE</code>` (type defined in `<code>modinfo.h</code>`)
contains function pointers to further module entrypoints, miscellaneous
information about the module and the configuration parameters accepted by the
module. This function must be exported without C++ name mangling, so in C++ code
it should be defined `<code>extern "C"</code>`.


The information container describes the module in general and is constructed
once during program excecution. A module may have multiple *instances* with
different values for configuration parameters. For example, a filter module can
be used with two different configurations in different services (or even in the
same service). In this case the loader uses the same module information
container for both but creates two module instances.


The MariaDB MaxScale configuration file `<code>maxscale.cnf</code>` is parsed by the core.
The core also checks that all the defined parameters are of the correct type for
the module. For this, the `<code>MXS_MODULE</code>`-structure includes a list of parameters
accepted by the module, defining parameter names, types and default values. In
the actual module code, parameter values should be extracted using functions
defined in `<code>config.h</code>`.


## Module API


### Overview


This section explains some general concepts encountered when implementing a
module API. For more detailed information, see the module specific subsection,
header files or the doxygen documentation.


Modules with configuration data define an *INSTANCE* object, which is created by
the module code in a `<code>createInstance</code>`-function or equivalent. The instance
creation function is called during MaxScale startup, usually when creating
services. MaxScale core holds the module instance data in the
`<code>SERVICE</code>`-structure (or other higher level construct) and gives it as a
parameter when calling functions from the module in question. The instance
structure should contain all non-client-specific information required by the
functions of the module. The core does not know what the object contains (since
it is defined by the module itself), nor will it modify the pointer or the
referenced object in any way.


Modules dealing with client-specific data require a *SESSION* object for every
client. As with the instance data, the definition of the module session
structure is up to the module writer and MaxScale treats it as an opaque type.
Usually the session contains status indicators and any resources required by the
client. MaxScale core has its own `<code>MXS_SESSION</code>` object, which tracks a variety
of client related information. The `<code>MXS_SESSION</code>` is given as a parameter to
module-specific session creation functions and is required for several typical
operations such as connecting to backends.


Descriptor control blocks (`<code>DCB</code>`), are generalized I/O descriptor types. DCBs
store the file descriptor, state, remote address, username, session, and other
data. DCBs are created whenever a new socket is created. Typically this happens
when a new client connects or MaxScale connects the client session to backend
servers. The module writer should use DCB handling functions provided by the MPI
to manage connections instead of calling general networking libraries. This
ensures that I/O is handled asynchronously by epoll. In general, module code
should avoid blocking I/O, *sleep*, *yield* or other potentially costly
operations, as the same thread is typically used for many client sessions.


Network data such as client queries and backend replies are held in a buffer
container called `<code>GWBUF</code>`. Multiple GWBUFs can form a linked list with type
information and properties in each GWBUF-node. Each node includes a pointer to a
reference counted shared buffer (`<code>SHARED_BUF</code>`), which finally points to a slice
of the actual data. In effect, multiple GWBUF-chains can share some data while
keeping some parts private. This construction is meant to minimize the need for
data copying and makes it easy to append more data to partially received data
packets. Plugin writers should use the MPI to manipulate GWBUFs. For more
information on the GWBUF, see [Filter and Router](#filter-and-router).


### General module management



```
int process_init()
void process_finish()
int thread_init()
void thread_finish()
```



These four functions are present in all `<code>MXS_MODULE</code>` structs and are not part of
the API of any individual module type. `<code>process_init</code>` and `<code>process_finish</code>` are
called by the module loader right after loading a module and just before
MaxScale terminates, respectively. Usually, these can be set to null in
`<code>MXS_MODULE</code>` unless the module needs some general initializations before
creating any instances. `<code>thread_init</code>` and `<code>thread_finish</code>` are thread-specific
equivalents.



```
void diagnostics(INSTANCE *instance, DCB *dcb)
```



A diagnostics printing routine is present in nearly all module types, although
with varying signatures. This entrypoint should print various statistics and
status information about the module instance `<code>instance</code>` in string form. The
target of the printing is the given DCB, and printing should be implemented by
calling `<code>dcb_printf</code>`.


### Protocol



```
int32_t read(struct dcb *)
int32_t write(struct dcb *, GWBUF *)
int32_t write_ready(struct dcb *)
int32_t error(struct dcb *)
int32_t hangup(struct dcb *)
int32_t accept(struct dcb *)
int32_t connect(struct dcb*, struct server*, MXS_SESSION*)
int32_t close(struct dcb *)
int32_t listen(struct dcb *, char *)
int32_t auth(struct dcb*, struct server*, MXS_SESSION*, GWBUF*)
int32_t session(struct dcb *, void *)
char auth_default()
int32_t connlimit(struct dcb *, int limit)
```



Protocol modules are laborous to implement due to their low level nature. Each
DCB maintains pointers to the correct protocol functions to be used with it,
allowing the DCB to be used in a protocol-independent manner.


`<code>read</code>`, `<code>write_ready</code>`, `<code>error</code>` and `<code>hangup</code>` are *epoll* handlers for their
respective events. `<code>write</code>` implements writing and is usually called in a router
module. `<code>accept</code>` is a listener socker handler. `<code>connect</code>` is used during session
creation when connecting to backend servers. `<code>listen</code>` creates a listener socket.
`<code>close</code>` closes a DCB created by `<code>accept</code>`, `<code>connect</code>` or `<code>listen</code>`.


In the ideal case modules other than the protocol modules themselves should not
be protocol-specific. This is currently difficult to achieve, since many actions
in the modules are dependent on protocol-speficic details. In the future,
protocol modules may be expanded to implement a generic query parsing and
information API, allowing filters and routers to be used with different SQL
variants.


### Authenticator



```
void* initialize(char **options)
void* create(void* instance)
int extract(struct dcb *, GWBUF *)
bool connectssl(struct dcb *)
int authenticate(struct dcb *)
void free(struct dcb *)
void destroy(void *)
int loadusers(struct servlistener *)
void diagnostic(struct dcb*, struct servlistener *)
int reauthenticate(struct dcb *, const char *user, uint8_t *token,
                   size_t token_len, uint8_t *scramble, size_t scramble_len,
                   uint8_t *output, size_t output_len);
```



Authenticators must communicate with the client or the backends and implement
authentication. The authenticators can be divided to client and backend modules,
although the two types are linked and must be used together. Authenticators are
also dependent on the protocol modules.


### Filter and Router


Filter and router APIs are nearly identical and are presented together. Since
these are the modules most likely to be implemented by plugin developers, their
APIs are discussed in more detail.



```
INSTANCE* createInstance(SERVICE* service, char** options)
void destroyInstance(INSTANCE* instance)
```



`<code>createInstance</code>` should read the `<code>options</code>` and initialize an instance object for
use with `<code>service</code>`. Often, simply saving the configuration values to fields is
enough. `<code>destroyInstance</code>` is called when the service using the module is
deallocated. It should free any resources claimed by the instance. All sessions
created by this instance should be closed before calling the destructor.



```
SESSION* newSession(INSTANCE* instance, MXS_SESSION* mxs_session, SERVICE* service)
void closeSession(INSTANCE* instance, SESSION* session)
void freeSession(INSTANCE* instance, SESSION* session)
```



These functions manage sessions. `<code>newSession</code>` should allocate a router or filter
session attached to the client session represented by `<code>mxs_session</code>`. MaxScale
will pass the returned pointer to all the API entrypoints that process user data
for the particular client. `<code>closeSession</code>` should close connections the session
has opened and release any resources specific to the served client. The
*SESSION* structure allocated in `<code>newSession</code>` should not be deallocated by
`<code>closeSession</code>` but in `<code>freeSession</code>`. These two are called in succession
by the core.



```
int routeQuery(INSTANCE *instance, SESSION session, GWBUF* queue) void
clientReply(INSTANCE* instance, SESSION session, GWBUF* queue, const mxs::ReplyRoute& down, const mxs::Reply& reply)
uint64_t getCapabilities(INSTANCE* instance)
```



`<code>routeQuery</code>` is called for client requests which should be routed to backends,
and `<code>clientReply</code>` for backend reply packets which should be routed to the
client. For some modules, MaxScale itself is the backend. For filters, these can
be NULL, in which case the filter will be skipped for that packet type.


`<code>routeQuery</code>` is often the most complicated function in a router, as it
implements the routing logic. It typically considers the client request `<code>queue</code>`,
the router settings in `<code>instance</code>` and the session state in `<code>session</code>` when making
a routing decision. For filters aswell, `<code>routeQuery</code>` typically implements the
main logic, although the routing target is constant. For router modules,
`<code>routeQuery</code>` should send data forward with `<code>dcb->func.write()</code>`. Filters should
directly call `<code>routeQuery</code>` for the next filter or router in the chain.


`<code>clientReply</code>` processes data flowing from backend back to client. For routers,
this function is often much simpler than `<code>routeQuery</code>`, since there is only one
client to route to. Depending on the router, some packets may not be routed to
the client. For example, if a client query was routed to multiple backends,
MaxScale will receive multiple replies while the client only expects one.
Routers should pass the reply packet to the last filter in the chain (reversed
order) using the function `<code>mxs_route_reply</code>`. Filters should call the
`<code>clientReply</code>` of the previous filter in the chain. There is no need for filters
to worry about being the first filter in the chain, as this is handled
transparently by the session creation routine.


Application data is not always received in complete packets from the network
stack. How partial packets are handled by the receiving protocol module depends
on the attached filters and the router, communicated by their
`<code>getCapabilities</code>`-functions. `<code>getCapabilities</code>` should return a bitfield
resulting from ORring the individual capabilities. `<code>routing.hh</code>` lists the allowed
capability flags.


If a router or filter sets no capabilities, `<code>routeQuery</code>` or `<code>clientReply</code>` may be
called to route partial packets. If the routing logic does not require any
information on the contents of the packets or even tracking the number of
packets, this may be fine. For many cases though, receiving a data packet in a
complete GWBUF chain or in one contiguos GWBUF is required. The former can be
requested by `<code>getCapabilities</code>` returning *RCAP_TYPE_STMT*, the latter by
*RCAP_TYPE_CONTIGUOUS*. Separate settings exist for queries and replies. For
replies, an additional value, *RCAP_TYPE_RESULTSET_OUTPUT* is defined. This
requests the protocol module to gather partial results into one result set.
Enforcing complete packets will delay processing, since the protocol module will
have to wait for the entire data packet to arrive before sending it down the
processing chain.



```
bool handleError(INSTANCE* instance, SESSION* session, GWBUF* errmsgbuf, mxs::Endpoint* problem, const mxs::Reply& reply);
```



This router-only entrypoint is called if a network error occurs in one of the
backend server connections in use by the session. When the entrypoint is called,
the router should try to continue the session if possible. If the session can
continue operating normally, the function should return `<code>true</code>`. If the router
cannot continue routing queries, for example due to a complete cluster outage,
the function should return `<code>false</code>` which will cause the whole session to close.


### Monitor



```
MONITOR* startMonitor(MXS_MONITOR *monitor, const MXS_CONFIG_PARAMETER *params)
void stopMonitor(MXS_MONITOR *monitor)
void diagnostics(DCB *, const MXS_MONITOR *)
```



Monitor modules typically run a repeated monitor routine with a used defined
interval. The `<code>MXS_MONITOR</code>` is a standard monitor definition used for all
monitors and contains a void pointer for storing module specific data.
`<code>startMonitor</code>` should create a new thread for itself using functions in the MPI
and have it regularly run a monitor loop. In the beginning of every monitor
loop, the monitor should lock the `<code>SERVER</code>`-structures of its servers. This
prevents any administrative action from interfering with the monitor during its
pass.


## Compiling, installing and running


The requirements for compiling a module are:
*The public headers (MPI)* A compatible compiler, typically GCC
* Libraries required by the public headers


Some of the public header files themselves include headers from other libraries.
These libraries need to be installed and it may be required to point out their
location to gcc. Some of the more commonly required libraries are:
 * *MySQL Connector-C*, used by the MySQL protocol module
 * *pcre2 regular expressions* (libpcre2-dev), used for example by the header
`<code>modutil.h</code>`


After all dependencies are accounted for, the module should compile with a
command similar to



```
gcc -I /usr/local/include/mariadb -shared -fPIC -g -o libmymodule.so mymodule.cpp
```



Large modules composed of several source files and using additional libraries
may require a more complicated compilation scheme, but that is outside the scope
of this document. The result of compiling a plugin should be a single shared
library file.


The compiled .so-file needs to be copied to the MaxScale library folder, which
is `<code>/usr/local/lib/maxscale</code>` by default. MaxScale expects the filename to be
`<code>lib<name>.so</code>`, where `<code><name></code>` must match the module name given in the
configuration file.


### Hands-on example: RoundRobinRouter


In this example, the RoundRobinRouter is compiled, installed and tested. The
software environment this section was written and tested is listed below. Any
recent Linux setup should be applicaple.


* Linux Mint 18
* gcc 5.4.0, glibc 2.23
* MariaDB MaxScale 2.1.0 debug build (binaries in `<code>usr/local/maxscale</code>`, modules in
`<code>/usr/local/lib/maxscale</code>`)
* MariaDB Connector-C 2.3.2 (installed to `<code>/usr/local/lib/mariadb</code>`, headers in
`<code>/usr/local/include/mariadb</code>`)
* `<code>roundrobinrouter.cpp</code>` in the current directory
* MaxScale plugin development headers (in `<code>usr/include/maxscale</code>`)


**Step 1** Compile RoundRobinRouter with `<code>$gcc -I /usr/local/include/mariadb
-shared -fPIC -g -o libroundrobinrouter.so roundrobinrouter.cpp</code>`.
Assuming all headers were found, the shared library `<code>libroundrobinrouter.so</code>`
is produced.


**Step 2** Copy the compiled module to the MaxScale module directory: `<code>$sudo cp
libroundrobinrouter.so /usr/local/lib/maxscale</code>`.


**Step 3** Modify the MaxScale configuration file to use the RoundRobinRouter as
a router. Example service and listener definitions are below. The *servers*
and *write_backend*-lines should be configured according to the actual backend
configuration.



```
[RR-Service]
type=service
router=roundrobinrouter
servers=LocalPrimary1,LocalReplica1,LocalReplica2
user=maxscale
password=maxscale
filters=MyLogFilter1
max_backends=10
write_backend=LocalPrimary1
print_on_routing=true
dummy_setting=two

[RR-Listener]
type=listener
service=RR-Service
port=4009
```



**Step 4** Start MaxScale: `<code>$ maxscale -d</code>`. Output:



```
MariaDB Corporation MaxScale 2.1.0  Mon Feb 20 17:22:18 2017
------------------------------------------------------
Info : MaxScale will be run in the terminal process.
    See the log from the following log files :

Configuration file : /etc/maxscale.cnf
Log directory      : /var/log/maxscale
Data directory     : /var/lib/maxscale
Module directory   : /usr/local/lib/maxscale
Service cache      : /var/cache/maxscale
```



**Step 5** Test with a MySQL client. The RoundRobinRouter has been tested with both a command line and a GUI client. With `<code>DEBUG_RRROUTER</code>` defined and `<code>print_on_routing</code>` enabled, the `<code>/var/log/maxscale/maxscale.log</code>` file will report nearly every action taken by the router.



```
2017-02-21 10:37:23   notice : [RoundRobinRouter] Creating instance.
2017-02-21 10:37:23   notice : [RoundRobinRouter] Settings read:
2017-02-21 10:37:23   notice : [RoundRobinRouter] 'max_backends': 10
2017-02-21 10:37:23   notice : [RoundRobinRouter] 'write_backend': 0xf0ce70
2017-02-21 10:37:23   notice : [RoundRobinRouter] 'print_on_routing': 1
2017-02-21 10:37:23   notice : [RoundRobinRouter] 'dummy_setting': 2
.
.
.
2017-02-21 10:37:37   notice : [RoundRobinRouter] Session with 4 connections created.
2017-02-21 10:37:37   notice : [RoundRobinRouter] QUERY: SHOW VARIABLES WHERE Variable_name in ('max_allowed_packet', 'system_time_zone', 'time_zone', 'sql_mode')
2017-02-21 10:37:37   notice : [RoundRobinRouter] Routing statement of length 110u  to backend 'LocalPrimary1'.
2017-02-21 10:37:37   notice : [RoundRobinRouter] Replied to client.
2017-02-21 10:37:37   notice : [RoundRobinRouter] QUERY: set session autocommit=1,sql_mode='NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES'
2017-02-21 10:37:37   notice : [RoundRobinRouter] Routing statement of length 103u to 4 backends.
2017-02-21 10:37:37   notice : [RoundRobinRouter] Replied to client.
2017-02-21 10:37:37   notice : [RoundRobinRouter] QUERY: SET @ApplicationName='DBeaver 3.8.5 - Main'
2017-02-21 10:37:37   notice : [RoundRobinRouter] Routing statement of length 48u to 4 backends.
2017-02-21 10:37:37   notice : [RoundRobinRouter] Replied to client.
2017-02-21 10:37:37   notice : [RoundRobinRouter] QUERY: select @@lower_case_table_names
2017-02-21 10:37:37   notice : [RoundRobinRouter] Routing statement of length 36u  to backend 'LocalReplica1'.
2017-02-21 10:37:37   notice : [RoundRobinRouter] Replied to client.
```



**Step 5** Connect with MaxCtrl, print diagnostics and call a custom command.



```
$ maxctrl
maxctrl show service RR-Service
┌─────────────────────┬────────────────────────────────────────────┐
│ Service             │ RR-Service                                 │
├─────────────────────┼────────────────────────────────────────────┤
│ Router              │ roundrobinrouter                           │
├─────────────────────┼────────────────────────────────────────────┤
│ State               │ Started                                    │
├─────────────────────┼────────────────────────────────────────────┤
│ Started At          │ Tue Apr 28 08:45:19 2020                   │
├─────────────────────┼────────────────────────────────────────────┤
│ Current Connections │ 0                                          │
├─────────────────────┼────────────────────────────────────────────┤
│ Total Connections   │ 0                                          │
├─────────────────────┼────────────────────────────────────────────┤
│ Max Connections     │ 0                                          │
├─────────────────────┼────────────────────────────────────────────┤
│ Cluster             │                                            │
├─────────────────────┼────────────────────────────────────────────┤
│ Servers             │ Server1                                    │
├─────────────────────┼────────────────────────────────────────────┤
│ Services            │                                            │
├─────────────────────┼────────────────────────────────────────────┤
│ Filters             │                                            │
├─────────────────────┼────────────────────────────────────────────┤
│ Parameters          │ {                                          │
│                     │     "router_options": null,                │
│                     │     "targets": null,                       │
│                     │     "user": "maxskysql",                   │
│                     │     "password": "*****",                   │
│                     │     "enable_root_user": false,             │
│                     │     "max_connections": 0,                  │
│                     │     "connection_timeout": 0,               │
│                     │     "net_write_timeout": 0,                │
│                     │     "auth_all_servers": false,             │
│                     │     "strip_db_esc": true,                  │
│                     │     "localhost_match_wildcard_host": true, │
│                     │     "version_string": null,                │
│                     │     "log_auth_warnings": true,             │
│                     │     "session_track_trx_state": false,      │
│                     │     "retain_last_statements": -1,          │
│                     │     "session_trace": false,                │
│                     │     "cluster": null,                       │
│                     │     "rank": "primary",                     │
│                     │     "connection_keepalive": 300,           │
│                     │     "connection_init_sql_file": null,      │
│                     │     "max_backends": 0,                     │
│                     │     "print_on_routing": false,             │
│                     │     "write_backend": null,                 │
│                     │     "dummy_setting": "the_answer"          │
│                     │ }                                          │
├─────────────────────┼────────────────────────────────────────────┤
│ Router Diagnostics  │ {                                          │
│                     │     "queries_ok": 0,                       │
│                     │     "queries_failed": 0,                   │
│                     │     "replies": 0                           │
│                     │ }                                          │
└─────────────────────┴────────────────────────────────────────────┘
maxctrl

MaxScale> call command roundrobinrouter test_command "one" 0
```



The result of the `<code>test_command "one" 0</code>` is printed to the terminal MaxScale is
running in:



```
RoundRobinRouter wishes the Admin a good day.
The module got 2 arguments.
Argument 0: type 'string' value 'one'
Argument 1: type 'boolean' value 'false'
```



## Summary and conclusion


Plugins offer a way to extend MariaDB MaxScale whenever the standard modules are
found insufficient. The plugins need only implement a set API, can be
independently compiled and installation is simply a file copy with some
configuration file modifications.


Out of the different plugin types, filters are the easiest to implement. They
work independently and have few requirements. Protocol and authenticator modules
require indepth knowledge of the database protocol they implement. Router module
complexity depends on the routing logic requirements.


The provided RoundRobinRouter example code should serve as a valid starting
point for both filters and routers. Studying the MaxScale Public Interface
headers to get a general idea of what services the core provides for plugins,
is also highly recommeded.


Lastly, MariaDB MaxScale is an open-source project, so code contributions can be
accepted if they fulfill the
[requirements](https://github.com/mariadb-corporation/MaxScale/wiki/Contributing).
