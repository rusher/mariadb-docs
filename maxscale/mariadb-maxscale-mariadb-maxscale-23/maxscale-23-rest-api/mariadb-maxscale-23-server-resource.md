
# Server Resource

# Server Resource


A server resource represents a backend database server.


## Resource Operations


### Get a server



```
GET /v1/servers/:name
```



Get a single server. The *:name* in the URI must be a valid server name with all
whitespace replaced with hyphens. The server names are case-insensitive.


**Note**: The *parameters* field contains all custom parameters for
 servers, including the server weighting parameters.


#### Response


`<code>Status: 200 OK</code>`



```
{
    "links": {
        "self": "http://localhost:8989/v1/servers/server1"
    },
    "data": {
        "id": "server1", // Resource identifier
        "type": "servers", // Resource type
        "relationships": { // Resource relationships to other resources
            "services": { // Services that use this server
                "links": {
                    "self": "http://localhost:8989/v1/services/"
                },
                "data": [ // References to service resources
                    {
                        "id": "RW-Split-Router",
                        "type": "services"
                    },
                    {
                        "id": "Read-Connection-Router",
                        "type": "services"
                    }
                ]
            },
            "monitors": { // The monitor that is monitoring this server
                "links": {
                    "self": "http://localhost:8989/v1/monitors/"
                },
                "data": [
                    {
                        "id": "MySQL-Monitor",
                        "type": "monitors"
                    }
                ]
            }
        },
        "attributes": { // Resource attributes
            "parameters": { // Server parameters
                "address": "127.0.0.1",
                "port": 3000,
                "protocol": "MariaDBBackend",
                "authenticator": "MySQLBackendAuth",
                "ssl_key": "/etc/certs/client-key.pem",
                "ssl_cert": "/etc/certs/client-cert.pem",
                "ssl_ca_cert": "/etc/certs/ca.pem",
                "ssl_cert_verify_depth": 9,
                "ssl_version": "MAX"
            },
            "state": "Master, Running", // Server state string
            "version_string": "10.1.22-MariaDB", // Server version
            "node_id": 3000, // Server node ID i.e. value of @@server_id
            "master_id": -1,
            "replication_depth": 0,
            "slaves": [ // List of slave server IDs
                3001
            ],
            "statistics": { // Server statistics
                "connections": 0,
                "total_connections": 0,
                "active_operations": 0
            }
        },
        "links": { // Link to the server itself
            "self": "http://localhost:8989/v1/servers/server1"
        }
    }
}
```



### Get all servers



```
GET /v1/servers
```



#### Response


Response contains a resource collection with all servers.


`<code>Status: 200 OK</code>`



```
{
    "links": {
        "self": "http://localhost:8989/v1/servers/"
    },
    "data": [ // List of server resouces
        {
            "id": "server1",
            "type": "servers",
            "relationships": {
                "services": {
                    "links": {
                        "self": "http://localhost:8989/v1/services/"
                    },
                    "data": [
                        {
                            "id": "RW-Split-Router",
                            "type": "services"
                        },
                        {
                            "id": "Read-Connection-Router",
                            "type": "services"
                        }
                    ]
                },
                "monitors": {
                    "links": {
                        "self": "http://localhost:8989/v1/monitors/"
                    },
                    "data": [
                        {
                            "id": "MySQL-Monitor",
                            "type": "monitors"
                        }
                    ]
                }
            },
            "attributes": {
                "parameters": {
                    "address": "127.0.0.1",
                    "port": 3000,
                    "protocol": "MariaDBBackend",
                    "authenticator": "MySQLBackendAuth",
                    "ssl_key": "/etc/certs/client-key.pem",
                    "ssl_cert": "/etc/certs/client-cert.pem",
                    "ssl_ca_cert": "/etc/certs/ca.pem",
                    "ssl_cert_verify_depth": 9,
                    "ssl_version": "MAX"
                },
                "state": "Master, Running",
                "version_string": "10.1.22-MariaDB",
                "node_id": 3000,
                "master_id": -1,
                "replication_depth": 0,
                "slaves": [
                    3001
                ],
                "statistics": {
                    "connections": 0,
                    "total_connections": 0,
                    "active_operations": 0
                }
            },
            "links": {
                "self": "http://localhost:8989/v1/servers/server1"
            }
        },
        {
            "id": "server2",
            "type": "servers",
            "relationships": {
                "services": {
                    "links": {
                        "self": "http://localhost:8989/v1/services/"
                    },
                    "data": [
                        {
                            "id": "RW-Split-Router",
                            "type": "services"
                        }
                    ]
                },
                "monitors": {
                    "links": {
                        "self": "http://localhost:8989/v1/monitors/"
                    },
                    "data": [
                        {
                            "id": "MySQL-Monitor",
                            "type": "monitors"
                        }
                    ]
                }
            },
            "attributes": {
                "parameters": {
                    "address": "127.0.0.1",
                    "port": 3001,
                    "protocol": "MariaDBBackend",
                    "ssl_key": "/etc/certs/client-key.pem",
                    "ssl_cert": "/etc/certs/client-cert.pem",
                    "ssl_ca_cert": "/etc/certs/ca.pem",
                    "ssl_cert_verify_depth": 9,
                    "ssl_version": "MAX"
                },
                "state": "Slave, Running",
                "version_string": "10.1.22-MariaDB",
                "node_id": 3001,
                "master_id": 3000,
                "replication_depth": 1,
                "slaves": [],
                "statistics": {
                    "connections": 0,
                    "total_connections": 0,
                    "active_operations": 0
                }
            },
            "links": {
                "self": "http://localhost:8989/v1/servers/server2"
            }
        }
    ]
}
```



### Create a server



```
POST /v1/servers
```



Create a new server by defining the resource. The posted object must define at
least the following fields.


* `<code>data.id</code>`
* Name of the server
* `<code>data.type</code>`
* Type of the object, must be `<code>servers</code>`
* `<code>data.attributes.parameters.address</code>`
* The [address](../../mariadb-maxscale-21-06/README.md) to use
* `<code>data.attributes.parameters.port</code>`
* The [port](../../mariadb-maxscale-21-06/README.md) to use


The following is the minimal required JSON object for defining a new server.



```
{
    "data": {
        "id": "server3",
        "type": "servers",
        "attributes": {
            "parameters": {
                "address": "127.0.0.1",
                "port": 3003
            }
        }
    }
}
```



The relationships of a server can also be defined at creation time. This allows
new servers to be created and immediately taken into use.



```
{
    "data": {
        "id": "server4",
        "type": "servers",
        "attributes": {
            "parameters": {
                "address": "127.0.0.1",
                "port": 3002
            }
        },
        "relationships": {
            "services": {
                "data": [
                    {
                        "id": "RW-Split-Router",
                        "type": "services"
                    },
                    {
                        "id": "Read-Connection-Router",
                        "type": "services"
                    }
                ]
            },
            "monitors": {
                "data": [
                    {
                        "id": "MySQL-Monitor",
                        "type": "monitors"
                    }
                ]
            }
        }
    }
}
```



The following parameters can be defined when a server is being created.


* [address](../../mariadb-maxscale-21-06/README.md)
* [port](../../mariadb-maxscale-21-06/README.md)
* [protocol](../../mariadb-maxscale-21-06/README.md)
* [authenticator](../../mariadb-maxscale-21-06/README.md)
* [ssl_key](../../mariadb-maxscale-21-06/README.md)
* [ssl_cert](../../mariadb-maxscale-21-06/README.md)
* [ssl_ca_cert](../../mariadb-maxscale-21-06/README.md)
* [ssl_version](../../mariadb-maxscale-21-06/README.md)
* [ssl_cert_verify_depth](../../mariadb-maxscale-21-06/README.md)
* [ssl_verify_peer_certificate](../../mariadb-maxscale-21-06/README.md)


#### Response


Server created:


`<code>Status: 204 No Content</code>`


Invalid JSON body:


`<code>Status: 403 Forbidden</code>`


### Update a server



```
PATCH /v1/servers/:name
```



The *:name* in the URI must map to a server name with all whitespace replaced
with hyphens and the request body must be a valid JSON document representing the
modified server. If the server in question is not found, a 404 Not Found
response is returned.


### Modifiable Fields


The following standard server parameters can be modified.


* [address](../../mariadb-maxscale-21-06/README.md)
* [port](../../mariadb-maxscale-21-06/README.md)
* [monitoruser](../../mariadb-maxscale-21-06/README.md)
* [monitorpw](../../mariadb-maxscale-21-06/README.md)


Refer to the documentation on these parameters for valid values.


The server weighting parameters can also be added, removed and updated. To
remove a parameter, define the value of that parameter as the *null* JSON type
e.g. `<code>{ "my-param": null }</code>`. To add a parameter, add a new key-value pair to
the *parameters* object with a name that does not conflict with the standard
parameters. To modify a weighting parameter, simply change the value.


In addition to standard parameters, the *services* and *monitors* fields of the
*relationships* object can be modified. Removal, addition and modification of
the links will change which service and monitors use this server.


For example, removing the first value in the *services* list in the
*relationships* object from the following JSON document will remove the
*server1* from the service *RW-Split-Router*.


Removing a service from a server is analogous to removing the server from the
service. Both unlink the two objects from each other.


Response to `<code>GET /v1/servers/server1</code>`:



```
{
    "links": {
        "self": "http://localhost:8989/v1/servers/server1"
    },
    "data": {
        "id": "server1",
        "type": "servers",
        "relationships": {
            "services": {
                "links": {
                    "self": "http://localhost:8989/v1/services/"
                },
                "data": [
                    {
                        "id": "RW-Split-Router", // We'll remove this service
                        "type": "services"
                    },
                    {
                        "id": "Read-Connection-Router",
                        "type": "services"
                    }
                ]
            },
            "monitors": {
                "links": {
                    "self": "http://localhost:8989/v1/monitors/"
                },
                "data": [
                    {
                        "id": "MySQL-Monitor",
                        "type": "monitors"
                    }
                ]
            }
        },
        "attributes": {
            "parameters": {
                "address": "127.0.0.1",
                "port": 3000,
                "protocol": "MariaDBBackend"
            },
            "state": "Master, Running",
            "version_string": "10.1.22-MariaDB",
            "node_id": 3000,
            "master_id": -1,
            "replication_depth": 0,
            "slaves": [
                3001,
                3002
            ],
            "statistics": {
                "connections": 0,
                "total_connections": 0,
                "active_operations": 0
            }
        },
        "links": {
            "self": "http://localhost:8989/v1/servers/server1"
        }
    }
}
```



Request for `<code>PATCH /v1/servers/server1</code>`:



```
{
    "data": {
        "id": "server1",
        "type": "servers",
        "relationships": {
            "services": {
                "data": [
                    {
                        "id": "Read-Connection-Router",
                        "type": "services"
                    }
                ]
            },
            "monitors": {
                "data": [
                    {
                        "id": "MySQL-Monitor",
                        "type": "monitors"
                    }
                ]
            }
        }
    }
}
```



If parts of the resource are not defined (e.g. the `<code>attributes</code>` field in the
above example), those parts of the resource are not modified. All parts that are
defined are interpreted as the new definition of those part of the resource. In
the above example, the `<code>relationships</code>` of the resource are completely redefined.


#### Response


Server modified:


`<code>Status: 204 No Content</code>`


Invalid JSON body:


`<code>Status: 403 Forbidden</code>`


### Update server relationships



```
PATCH /v1/servers/:name/relationships/:type
```



The *:name* in the URI must map to a server name with all whitespace replaced
with hyphens. The *:type* in the URI must be either *services*, for service
relationships, or *monitors*, for monitor relationships.


The request body must be a JSON object that defines only the *data* field. The
value of the *data* field must be an array of relationship objects that define
the *id* and *type* fields of the relationship. This object will replace the
existing relationships of the particular type from the server.


The following is an example request and request body that defines a single
service relationship for a server.



```
PATCH /v1/servers/my-db-server/relationships/services

{
    data: [
          { "id": "my-rwsplit-service", "type": "services" }
    ]
}
```



All relationships for a server can be deleted by sending an empty array as the
*data* field value. The following example removes the server from all services.



```
PATCH /v1/servers/my-db-server/relationships/services

{
    data: []
}
```



#### Response


Server relationships modified:


`<code>Status: 204 No Content</code>`


Invalid JSON body:


`<code>Status: 403 Forbidden</code>`


### Destroy a server



```
DELETE /v1/servers/:name
```



The *:name* in the URI must map to a server name with all whitespace replaced
with hyphens.


A server can only be deleted if it is not used by any services or monitors.


#### Response


Server is destroyed:


`<code>Status: 204 No Content</code>`


Server is in use:


`<code>Status: 403 Forbidden</code>`


### Set server state



```
PUT /v1/servers/:name/set
```



The *:name* in the URI must map to a server name with all whitespace replaced
with hyphens. This endpoint requires that the `<code>state</code>` parameter is passed with
the request. The value of `<code>state</code>` must be one of the following values.


| Value | State Description |
| --- | --- |
| Value | State Description |
| master | Server is a Master |
| slave | Server is a Slave |
| maintenance | Server is put into maintenance |
| running | Server is up and running |
| synced | Server is a Galera node |
| ndb | Server is a NDBCluster node |
| stale | Server is a stale Master |


For example, to set the server *db-server-1* into maintenance mode, a request to
the following URL must be made:



```
PUT /v1/servers/db-server-1/set?state=maintenance
```



This endpoint also supports the `<code>force=yes</code>` parameter that will cause all
connections to the server to be closed if `<code>state=maintenance</code>` is also set. By
default setting a server into maintenance mode will cause connections to be
closed only after the next request is sent.


The following example forcefully closes all connections to server *db-server-1*
and sets it into maintenance mode:



```
PUT /v1/servers/db-server-1/set?state=maintenance&force=yes
```



#### Response


Server state modified:


`<code>Status: 204 No Content</code>`


Missing or invalid parameter:


`<code>Status: 403 Forbidden</code>`


### Clear server state



```
PUT /v1/servers/:name/clear
```



The *:name* in the URI must map to a server name with all whitespace replaced
with hyphens. This endpoint requires that the `<code>state</code>` parameter is passed with
the request. The value of `<code>state</code>` must be one of the values defined in the
*set* endpoint documentation.


#### Response


Server state modified:


`<code>Status: 204 No Content</code>`


Missing or invalid parameter:


`<code>Status: 403 Forbidden</code>`
