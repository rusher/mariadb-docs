
# Service Resource

# Service Resource


A service resource represents a service inside MaxScale. A service is a
collection of network listeners, filters, a router and a set of backend servers.


## Resource Operations


### Get a service



```
GET /v1/services/:name
```



Get a single service. The *:name* in the URI must be a valid service name with
all whitespace replaced with hyphens. The service names are case-insensitive.


#### Response


`<code>Status: 200 OK</code>`



```
{
    "links": {
        "self": "http://localhost:8989/v1/services/Read-Connection-Router"
    },
    "data": {
        "id": "Read-Connection-Router",
        "type": "services",
        "attributes": {
            "router": "readconnroute",
            "state": "Started",
            "router_diagnostics": {
                "connections": 0,
                "current_connections": 1,
                "queries": 0
            },
            "started": "Mon May 22 12:54:05 2017",
            "total_connections": 1,
            "connections": 1,
            "parameters": { // Service parameters
                "router_options": "master",
                "user": "maxuser",
                "password": "maxpwd",
                "enable_root_user": false,
                "max_retry_interval": 3600,
                "max_connections": 0,
                "connection_timeout": 0,
                "auth_all_servers": false,
                "strip_db_esc": true,
                "localhost_match_wildcard_host": true,
                "version_string": "",
                "log_auth_warnings": true,
                "retry_on_failure": true
            },
            "listeners": [ // Listeners that point to this service
                {
                    "attributes": {
                        "parameters": {
                            "port": 4008,
                            "protocol": "MariaDBClient",
                            "authenticator": "MySQLAuth"
                        }
                    },
                    "id": "Read-Connection-Listener",
                    "type": "listeners"
                }
            ]
        },
        "relationships": {
            "servers": {
                "links": {
                    "self": "http://localhost:8989/v1/servers/"
                },
                "data": [ // List of servers that this service uses
                    {
                        "id": "server1",
                        "type": "servers"
                    }
                ]
            }
        },
        "links": {
            "self": "http://localhost:8989/v1/services/Read-Connection-Router"
        }
    }
}
```



### Get all services



```
GET /v1/services
```



Get all services.


#### Response


`<code>Status: 200 OK</code>`



```
{
    "links": {
        "self": "http://localhost:8989/v1/services/"
    },
    "data": [ // Collection of service resources
        {
            "id": "Read-Connection-Router",
            "type": "services",
            "attributes": {
                "router": "readconnroute",
                "state": "Started",
                "router_diagnostics": {
                    "connections": 0,
                    "current_connections": 1,
                    "queries": 0
                },
                "started": "Mon May 22 13:00:46 2017",
                "total_connections": 1,
                "connections": 1,
                "parameters": {
                    "router_options": "master",
                    "user": "maxuser",
                    "password": "maxpwd",
                    "enable_root_user": false,
                    "max_retry_interval": 3600,
                    "max_connections": 0,
                    "connection_timeout": 0,
                    "auth_all_servers": false,
                    "strip_db_esc": true,
                    "localhost_match_wildcard_host": true,
                    "version_string": "",
                    "log_auth_warnings": true,
                    "retry_on_failure": true
                },
                "listeners": [
                    {
                        "attributes": {
                            "parameters": {
                                "port": 4008,
                                "protocol": "MariaDBClient",
                                "authenticator": "MySQLAuth"
                            }
                        },
                        "id": "Read-Connection-Listener",
                        "type": "listeners"
                    }
                ]
            },
            "relationships": {
                "servers": {
                    "links": {
                        "self": "http://localhost:8989/v1/servers/"
                    },
                    "data": [
                        {
                            "id": "server1",
                            "type": "servers"
                        }
                    ]
                }
            },
            "links": {
                "self": "http://localhost:8989/v1/services/Read-Connection-Router"
            }
        },
        {
            "id": "CLI",
            "type": "services",
            "attributes": {
                "router": "cli",
                "state": "Started",
                "started": "Mon May 22 13:00:46 2017",
                "total_connections": 2,
                "connections": 2,
                "parameters": {
                    "router_options": "",
                    "user": "",
                    "password": "",
                    "enable_root_user": false,
                    "max_retry_interval": 3600,
                    "max_connections": 0,
                    "connection_timeout": 0,
                    "auth_all_servers": false,
                    "strip_db_esc": true,
                    "localhost_match_wildcard_host": true,
                    "version_string": "",
                    "log_auth_warnings": true,
                    "retry_on_failure": true
                },
                "listeners": [
                    {
                        "attributes": {
                            "parameters": {
                                "address": "default",
                                "port": 0,
                                "protocol": "maxscaled",
                                "authenticator": "MaxAdminAuth"
                            }
                        },
                        "id": "CLI-Listener",
                        "type": "listeners"
                    },
                    {
                        "attributes": {
                            "parameters": {
                                "address": "0.0.0.0",
                                "port": 6603,
                                "protocol": "maxscaled",
                                "authenticator": "MaxAdminAuth"
                            }
                        },
                        "id": "CLI-Network-Listener",
                        "type": "listeners"
                    }
                ]
            },
            "relationships": {},
            "links": {
                "self": "http://localhost:8989/v1/services/CLI"
            }
        }
    ]
}
```



### Create a service



```
POST /v1/services
```



Create a new service by defining the resource. The posted object must define at
least the following fields.


* `<code>data.id</code>`
* Name of the service
* `<code>data.type</code>`
* Type of the object, must be `<code>services</code>`
* `<code>data.attributes.router</code>`
* The router module to use
* `<code>data.attributes.parameters.user</code>`
* The [user](../../mariadb-maxscale-21-06/README.md) to use
* `<code>data.attributes.parameters.password</code>`
* The [password](../../mariadb-maxscale-21-06/README.md) to use


The `<code>data.attributes.parameters</code>` object is used to define router and service
parameters. All configuration parameters that can be defined in the
configuration file can also be added to the parameters object. The exceptions to
this are the `<code>type</code>`, `<code>router</code>`, `<code>servers</code>` and `<code>filters</code>` parameters which must not
be defined.


As with other REST API resources, the `<code>data.relationships</code>` field defines the
relationships of the service to other resources. Services can have two types of
relationships: `<code>servers</code>` and `<code>filters</code>` relationships.


If the request body defines a valid `<code>relationships</code>` object, the service is
linked to those resources. For servers, this is equivalent to adding the list of
server names into the
[servers](../../mariadb-maxscale-21-06/README.md) parameter. For
filters, this is equivalent to adding the filters in the
`<code>data.relationships.filters.data</code>` array to the
[filters](../../mariadb-maxscale-21-06/README.md) parameter in the
order they appear.


The following example defines a new service with both a server and a filter
relationship.



```
{
    "data": {
        "id": "my-service",
        "type": "services",
        "attributes": {
            "router": "readwritesplit",
            "parameters": {
                "user": "maxuser",
                "password": "maxpwd"
            }
        },
        "relationships": {
            "filters": {
                "data": [
                    {
                        "id": "QLA",
                        "type": "filters"
                    }
                ]
            },
            "servers": {
                "data": [
                    {
                        "id": "server1",
                        "type": "servers"
                    }
                ]
            }
        }
    }
}
```



#### Response


Service is created:


`<code>Status: 204 No Content</code>`


### Destroy a service



```
DELETE /v1/services/:service
```



In the URI , the *:service* must map to a service that is destroyed.


A service can only be destroyed if the service uses no servers or filters and
all the listeners pointing to the service have been destroyed. This means that
the `<code>data.relationships</code>` must be an empty object and `<code>data.attributes.listeners</code>`
must be an empty array in order for the service to qualify for destruction.


If there are open client connections that use the service when it is destroyed,
they are allowed to gracefully close before the service is destroyed. This means
that the destruction of a service can be acknowledged via the REST API before
the destruction process has fully completed.


To find out whether a service is still in use after it has been destroyed, the
[sessions](mariadb-maxscale-23-session-resource.md) resource should be used. If a session for
the service is still open, it has not yet been destroyed.


#### Response


Service is destroyed:


`<code>Status: 204 No Content</code>`


### Get service listeners


Get the listeners of a service. The *:name* in the URI must be a valid service
name with all whitespace replaced with hyphens.



```
GET /v1/services/:name/listeners
```



#### Response


`<code>Status: 200 OK</code>`



```
{
    "links": {
        "self": "http://localhost:8989/v1/services/Read-Connection-Router/listeners"
    },
    "data": [
        {
            "attributes": {
                "parameters": {
                    "port": 4008,
                    "protocol": "MariaDBClient",
                    "authenticator": "MySQLAuth"
                }
            },
            "id": "Read-Connection-Listener",
            "type": "listeners"
        }
    ]
}
```



### Get a single service listener



```
GET /v1/services/:name/listeners/:listener
```



Get the listeners of a service. The *:name* in the URI must be a valid service
name and *:listener* must be a valid listener name, both with all whitespace
replaced with hyphens.


#### Response


`<code>Status: 200 OK</code>`



```
{
    "links": {
        "self": "http://localhost:8989/v1/services/RW-Split-Router/listeners/RW-Split-Listener"
    },
    "data": {
        "attributes": {
            "parameters": {
                "port": 4006,
                "protocol": "MariaDBClient",
                "authenticator": "MySQLAuth"
            }
        },
        "id": "RW-Split-Listener",
        "type": "listeners"
    }
}
```



### Create a new listener



```
POST /v1/services/:name/listeners
```



Create a new listener for a service by defining the resource. The *:name* in the
URI must map to a service name with all whitespace replaced with hyphens. The
posted object must define the *data.id* field with the name of the server and
the *data.attributes.parameters.port* field with the port where the listener
will listen on. The following is the minimal required JSON object for defining a
new listener.



```
{
    "data": {
        "id": "my-listener",
        "type": "listeners",
        "attributes": {
            "parameters": {
                "port": 3306
            }
        }
    }
}
```



The following values can be given in the *parameters* object. If SSL options are
provided, the *ssl_key*, *ssl_cert* and *ssl_ca_cert* parameters must all be
defined.


* [address](../../mariadb-maxscale-21-06/README.md)
* [port](../../mariadb-maxscale-21-06/README.md)
* [protocol](../../mariadb-maxscale-21-06/README.md)
* [authenticator](../../mariadb-maxscale-21-06/README.md)
* [authenticator_options](../../mariadb-maxscale-21-06/README.md)
* [ssl_key](../../mariadb-maxscale-21-06/README.md)
* [ssl_cert](../../mariadb-maxscale-21-06/README.md)
* [ssl_ca_cert](../../mariadb-maxscale-21-06/README.md)
* [ssl_version](../../mariadb-maxscale-21-06/README.md)
* [ssl_cert_verify_depth](../../mariadb-maxscale-21-06/README.md)


#### Response


Listener is created:


`<code>Status: 204 No Content</code>`


### Destroy a listener



```
DELETE /v1/services/:service/listeners/:name
```



In the URI , the *:name* must map to a listener and the *:service* must map to a
service. Both names must have all whitespace replaced with hyphens.


When a listener is destroyed, the network port it listens on is available for
reuse.


#### Response


Listener is destroyed:


`<code>Status: 204 No Content</code>`


Listener cannot be deleted:


`<code>Status: 403 Forbidden</code>`


### Update a service



```
PATCH /v1/services/:name
```



The *:name* in the URI must map to a service name and the request body must be a
JSON object which is interpreted as the new definition of the service.


All standard service parameters can be modified. Refer to the
[service](../../mariadb-maxscale-21-06/README.md) documentation on
the details of these parameters.


In addition to the standard service parameters, router parameters can be updated
at runtime if the router module supports it. Refer to the individual router
documentation for more details on whether the router supports it and which
parameters can be updated at runtime.


The following example modifies a service by changing the `<code>user</code>` parameter to `<code>admin</code>`.



```
{
    "data": {
        "attributes": {
            "parameters": {
                "user": "admin"
            }
        }
    }
}
```



#### Response


Service is modified:


`<code>Status: 204 No Content</code>`


### Update service relationships



```
PATCH /v1/services/:name/relationships/:type
```



The *:name* in the URI must map to a service name with all whitespace replaced
with hyphens. The *:type* in the URI must be either *servers* or *filters*,
depending on which relationship is being modified.


The request body must be a JSON object that defines only the *data* field. The
value of the *data* field must be an array of relationship objects that define
the *id* and *type* fields of the relationship. This object will replace the
existing relationships of this type for the service. Both `<code>servers</code>` and
`<code>filters</code>` relationships can be modified.


*Note:* The order of the values in the `<code>filters</code>` relationship will define the
 order the filters are set up in. The order in which the filters appear in the
 array will be the order in which the filters are applied to each query. Refer
 to the [filters](../../mariadb-maxscale-21-06/README.md) parameter
 for more details.


The following is an example request and request body that defines a single
server relationship for a service that is equivalent to a `<code>servers=my-server</code>`
parameter.



```
PATCH /v1/services/my-rw-service/relationships/servers

{
    data: [
          { "id": "my-server", "type": "servers" }
    ]
}
```



All relationships for a service can be deleted by sending an empty array or a
`<code>null</code>` value as the *data* field value. The following example removes all
servers from a service.



```
PATCH /v1/services/my-rw-service/relationships/servers

{
    data: []
}
```



#### Response


Service relationships modified:


`<code>Status: 204 No Content</code>`


Invalid JSON body:


`<code>Status: 403 Forbidden</code>`


### Stop a service



```
PUT /v1/services/:name/stop
```



Stops a started service.


#### Response


Service is stopped:


`<code>Status: 204 No Content</code>`


### Start a service



```
PUT /v1/services/:name/start
```



Starts a stopped service.


#### Response


Service is started:


`<code>Status: 204 No Content</code>`
