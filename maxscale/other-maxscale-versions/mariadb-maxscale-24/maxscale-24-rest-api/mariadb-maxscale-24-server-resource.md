# Server Resource

A server resource represents a backend database server.

### Resource Operations

#### Get a server

```
GET /v1/servers/:name
```

Get a single server. The _:name_ in the URI must be a valid server name with all\
whitespace replaced with hyphens. The server names are case-insensitive.

**Note**: The _parameters_ field contains all custom parameters for\
servers, including the server weighting parameters.

**Response**

`Status: 200 OK`

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

#### Get all servers

```
GET /v1/servers
```

**Response**

Response contains a resource collection with all servers.

`Status: 200 OK`

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

#### Create a server

```
POST /v1/servers
```

Create a new server by defining the resource. The posted object must define at\
least the following fields.

* `data.id`
* Name of the server
* `data.type`
* Type of the object, must be `servers`
* `data.attributes.parameters.protocol`
* The [protocol](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md) to use.\
  Must be defined.
* `data.attributes.parameters.address` OR `data.attributes.parameters.socket`
* The [address](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md) or[socket](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md) to use. Only\
  one of the fields can be defined.
* `data.attributes.parameters.port`
* The [port](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md) to use. Needs\
  to be defined if the `address` field is defined.

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

The relationships of a server can also be defined at creation time. This allows\
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

* [address](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [port](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [protocol](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [authenticator](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [ssl\_key](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [ssl\_cert](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [ssl\_ca\_cert](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [ssl\_version](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [ssl\_cert\_verify\_depth](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [ssl\_verify\_peer\_certificate](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)

**Response**

Server created:

`Status: 204 No Content`

Invalid JSON body:

`Status: 403 Forbidden`

#### Update a server

```
PATCH /v1/servers/:name
```

The _:name_ in the URI must map to a server name with all whitespace replaced\
with hyphens and the request body must be a valid JSON document representing the\
modified server. If the server in question is not found, a 404 Not Found\
response is returned.

#### Modifiable Fields

The following standard server parameters can be modified.

* [address](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [port](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [monitoruser](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [monitorpw](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)

Refer to the documentation on these parameters for valid values.

The server weighting parameters can also be added, removed and updated. To\
remove a parameter, define the value of that parameter as the _null_ JSON type\
e.g. `{ "my-param": null }`. To add a parameter, add a new key-value pair to\
the _parameters_ object with a name that does not conflict with the standard\
parameters. To modify a weighting parameter, simply change the value.

In addition to standard parameters, the _services_ and _monitors_ fields of th&#x65;_&#x72;elationships_ object can be modified. Removal, addition and modification of\
the links will change which service and monitors use this server.

For example, removing the first value in the _services_ list in th&#x65;_&#x72;elationships_ object from the following JSON document will remove th&#x65;_&#x73;erver1_ from the service _RW-Split-Router_.

Removing a service from a server is analogous to removing the server from the\
service. Both unlink the two objects from each other.

Response to `GET /v1/servers/server1`:

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

Request for `PATCH /v1/servers/server1`:

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

If parts of the resource are not defined (e.g. the `attributes` field in the\
above example), those parts of the resource are not modified. All parts that are\
defined are interpreted as the new definition of those part of the resource. In\
the above example, the `relationships` of the resource are completely redefined.

**Response**

Server modified:

`Status: 204 No Content`

Invalid JSON body:

`Status: 403 Forbidden`

#### Update server relationships

```
PATCH /v1/servers/:name/relationships/:type
```

The _:name_ in the URI must map to a server name with all whitespace replaced\
with hyphens. The _:type_ in the URI must be either _services_, for service\
relationships, or _monitors_, for monitor relationships.

The request body must be a JSON object that defines only the _data_ field. The\
value of the _data_ field must be an array of relationship objects that define\
the _id_ and _type_ fields of the relationship. This object will replace the\
existing relationships of the particular type from the server.

The following is an example request and request body that defines a single\
service relationship for a server.

```
PATCH /v1/servers/my-db-server/relationships/services

{
    data: [
          { "id": "my-rwsplit-service", "type": "services" }
    ]
}
```

All relationships for a server can be deleted by sending an empty array as th&#x65;_&#x64;ata_ field value. The following example removes the server from all services.

```
PATCH /v1/servers/my-db-server/relationships/services

{
    data: []
}
```

**Response**

Server relationships modified:

`Status: 204 No Content`

Invalid JSON body:

`Status: 403 Forbidden`

#### Destroy a server

```
DELETE /v1/servers/:name
```

The _:name_ in the URI must map to a server name with all whitespace replaced\
with hyphens.

A server can only be deleted if it is not used by any services or monitors.

**Response**

Server is destroyed:

`Status: 204 No Content`

Server is in use:

`Status: 403 Forbidden`

#### Set server state

```
PUT /v1/servers/:name/set
```

The _:name_ in the URI must map to a server name with all whitespace replaced\
with hyphens. This endpoint requires that the `state` parameter is passed with\
the request. The value of `state` must be one of the following values.

| Value       | State Description                |
| ----------- | -------------------------------- |
| Value       | State Description                |
| master      | Server is a Master               |
| slave       | Server is a Slave                |
| maintenance | Server is put into maintenance   |
| running     | Server is up and running         |
| synced      | Server is a Galera node          |
| drain       | Server is drained of connections |

For example, to set the server _db-server-1_ into maintenance mode, a request to\
the following URL must be made:

```
PUT /v1/servers/db-server-1/set?state=maintenance
```

This endpoint also supports the `force=yes` parameter that will cause all\
connections to the server to be closed if `state=maintenance` is also set. By\
default setting a server into maintenance mode will cause connections to be\
closed only after the next request is sent.

The following example forcefully closes all connections to server _db-server-1_\
and sets it into maintenance mode:

```
PUT /v1/servers/db-server-1/set?state=maintenance&force=yes
```

**Response**

Server state modified:

`Status: 204 No Content`

Missing or invalid parameter:

`Status: 403 Forbidden`

#### Clear server state

```
PUT /v1/servers/:name/clear
```

The _:name_ in the URI must map to a server name with all whitespace replaced\
with hyphens. This endpoint requires that the `state` parameter is passed with\
the request. The value of `state` must be one of the values defined in th&#x65;_&#x73;et_ endpoint documentation.

**Response**

Server state modified:

`Status: 204 No Content`

Missing or invalid parameter:

`Status: 403 Forbidden`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
