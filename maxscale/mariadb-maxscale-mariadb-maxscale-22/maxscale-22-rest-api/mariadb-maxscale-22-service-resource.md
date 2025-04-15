
# Service Resource

# Service Resource


A service resource represents a service inside MaxScale. A service is a
collection of network listeners, filters, a router and a set of backend servers.


## Resource Operations


### Get a service


Get a single service. The *:name* in the URI must be a valid service name with
all whitespace replaced with hyphens. The service names are case-insensitive.



```
GET /v1/services/:name
```



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


Get all services.



```
GET /v1/services
```



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


Get the listeners of a service. The *:name* in the URI must be a valid service
name and *:listener* must be a valid listener name, both with all whitespace
replaced with hyphens.



```
GET /v1/services/:name/listeners/:listener
```



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


* [address](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#user-content-address-1)
* [port](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#user-content-port-1)
* [protocol](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#user-content-protocol-1)
* [authenticator](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#user-content-authenticator-1)
* [authenticator_options](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#user-content-authenticator-options-1)
* [ssl_key](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#user-content-ssl_key-1)
* [ssl_cert](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#user-content-ssl_cert-1)
* [ssl_ca_cert](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#user-content-ssl_ca_cert-1)
* [ssl_version](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#user-content-ssl_version-1)
* [ssl_cert_verify_depth](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#user-content-ssl_cert_verify_depth-1)


### Destroy a listener



```
DELETE /v1/services/:service/listeners/:name
```



In the URI , the *:name* must map to a listener and the *:service* must map to a
service. Both names must have all whitespace replaced with hyphens.


#### Response


Listener is destroyed:


`<code>Status: 204 No Content</code>`


Listener cannot be deleted:


`<code>Status: 403 Forbidden</code>`


### Update a service


The *:name* in the URI must map to a service name and the request body must be a
valid JSON Patch document which is applied to the resource.



```
PATCH /v1/services/:name
```



The following standard service parameters can be modified.


* [user](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#user)
* [password](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#password)
* [enable_root_user](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#enable_root_user)
* [max_retry_interval](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#max_retry_interval)
* [max_connections](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#max_connections)
* [connection_timeout](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#connection_timeout)
* [auth_all_servers](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#auth_all_servers)
* [strip_db_esc](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#strip_db_esc)
* [localhost_match_wildcard_host](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#localhost_match_wildcard_host)
* [version_string](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#version_string)
* [weightby](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#weightby)
* [log_auth_warnings](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#log_auth_warnings)
* [retry_on_failure](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#retry_on_failure)


Refer to the documentation on these parameters for valid values.


#### Response


Service is modified:


`<code>Status: 204 No Content</code>`


### Update service relationships



```
PATCH /v1/services/:name/relationships/servers
```



The *:name* in the URI must map to a service name with all whitespace replaced
with hyphens.


The request body must be a JSON object that defines only the *data* field. The
value of the *data* field must be an array of relationship objects that define
the *id* and *type* fields of the relationship. This object will replace the
existing relationships of the service.


The following is an example request and request body that defines a single
server relationship for a service.



```
PATCH /v1/services/my-rw-service/relationships/servers

{
    data: [
          { "id": "my-server", "type": "servers" }
    ]
}
```



All relationships for a service can be deleted by sending an empty array as the
*data* field value. The following example removes all servers from a service.



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


Stops a started service.



```
PUT /v1/services/:name/stop
```



#### Response


Service is stopped:


`<code>Status: 204 No Content</code>`


### Start a service


Starts a stopped service.



```
PUT /v1/services/:name/start
```



#### Response


Service is started:


`<code>Status: 204 No Content</code>`
