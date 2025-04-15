
# MaxScale 25.01 Listener Resource

# Listener Resource


A listener resource represents a listener of a service in MaxScale. All
listeners point to a service in MaxScale.




* [Listener Resource](#listener-resource)

  * [Resource Operations](#resource-operations)

    * [Get a listener](#get-a-listener)

      * [Response](#response)
    * [Get all listeners](#get-all-listeners)

      * [Response](#response_1)
    * [Create a new listener](#create-a-new-listener)

      * [Response](#response_2)
    * [Update a listener](#update-a-listener)

      * [Response](#response_3)
    * [Destroy a listener](#destroy-a-listener)

      * [Response](#response_4)
    * [Stop a listener](#stop-a-listener)

      * [Parameters](#parameters)
      * [Response](#response_5)
    * [Start a listener](#start-a-listener)

      * [Response](#response_6)




## Resource Operations


### Get a listener



```
GET /v1/listeners/:name
```



Get a single listener. The *:name* in the URI must be the name of a listener in
MaxScale.


#### Response


`<code>Status: 200 OK</code>`



```
{
    "data": {
        "attributes": {
            "parameters": {
                "MariaDBProtocol": {
                    "allow_replication": true
                },
                "address": "::",
                "authenticator": null,
                "authenticator_options": null,
                "connection_init_sql_file": null,
                "connection_metadata": [
                    "character_set_client=auto",
                    "character_set_connection=auto",
                    "character_set_results=auto",
                    "max_allowed_packet=auto",
                    "system_time_zone=auto",
                    "time_zone=auto",
                    "tx_isolation=auto",
                    "maxscale=auto"
                ],
                "port": 4006,
                "protocol": "MariaDBProtocol",
                "proxy_protocol_networks": null,
                "service": "RW-Split-Router",
                "socket": null,
                "sql_mode": "default",
                "ssl": false,
                "ssl_ca": null,
                "ssl_cert": null,
                "ssl_cert_verify_depth": 9,
                "ssl_cipher": null,
                "ssl_crl": null,
                "ssl_key": null,
                "ssl_verify_peer_certificate": false,
                "ssl_verify_peer_host": false,
                "ssl_version": "MAX",
                "type": "listener",
                "user_mapping_file": null
            },
            "source": {
                "file": "/etc/maxscale.cnf",
                "type": "static"
            },
            "state": "Running"
        },
        "id": "RW-Split-Listener",
        "relationships": {
            "services": {
                "data": [
                    {
                        "id": "RW-Split-Router",
                        "type": "services"
                    }
                ],
                "links": {
                    "related": "http://localhost:8989/v1/services/",
                    "self": "http://localhost:8989/v1/listeners/RW-Split-Listener/relationships/services/"
                }
            }
        },
        "type": "listeners"
    },
    "links": {
        "self": "http://localhost:8989/v1/listeners/RW-Split-Listener/"
    }
}
```



### Get all listeners



```
GET /v1/listeners
```



Get all listeners.


#### Response


`<code>Status: 200 OK</code>`



```
{
    "data": [
        {
            "attributes": {
                "parameters": {
                    "MariaDBProtocol": {
                        "allow_replication": true
                    },
                    "address": "::",
                    "authenticator": null,
                    "authenticator_options": null,
                    "connection_init_sql_file": null,
                    "connection_metadata": [
                        "character_set_client=auto",
                        "character_set_connection=auto",
                        "character_set_results=auto",
                        "max_allowed_packet=auto",
                        "system_time_zone=auto",
                        "time_zone=auto",
                        "tx_isolation=auto",
                        "maxscale=auto"
                    ],
                    "port": 4006,
                    "protocol": "MariaDBProtocol",
                    "proxy_protocol_networks": null,
                    "service": "RW-Split-Router",
                    "socket": null,
                    "sql_mode": "default",
                    "ssl": false,
                    "ssl_ca": null,
                    "ssl_cert": null,
                    "ssl_cert_verify_depth": 9,
                    "ssl_cipher": null,
                    "ssl_crl": null,
                    "ssl_key": null,
                    "ssl_verify_peer_certificate": false,
                    "ssl_verify_peer_host": false,
                    "ssl_version": "MAX",
                    "type": "listener",
                    "user_mapping_file": null
                },
                "source": {
                    "file": "/etc/maxscale.cnf",
                    "type": "static"
                },
                "state": "Running"
            },
            "id": "RW-Split-Listener",
            "relationships": {
                "services": {
                    "data": [
                        {
                            "id": "RW-Split-Router",
                            "type": "services"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/services/",
                        "self": "http://localhost:8989/v1/listeners/RW-Split-Listener/relationships/services/"
                    }
                }
            },
            "type": "listeners"
        },
        {
            "attributes": {
                "parameters": {
                    "MariaDBProtocol": {
                        "allow_replication": true
                    },
                    "address": "::",
                    "authenticator": null,
                    "authenticator_options": null,
                    "connection_init_sql_file": null,
                    "connection_metadata": [
                        "character_set_client=auto",
                        "character_set_connection=auto",
                        "character_set_results=auto",
                        "max_allowed_packet=auto",
                        "system_time_zone=auto",
                        "time_zone=auto",
                        "tx_isolation=auto",
                        "maxscale=auto"
                    ],
                    "port": 4008,
                    "protocol": "MariaDBProtocol",
                    "proxy_protocol_networks": null,
                    "service": "Read-Connection-Router",
                    "socket": null,
                    "sql_mode": "default",
                    "ssl": false,
                    "ssl_ca": null,
                    "ssl_cert": null,
                    "ssl_cert_verify_depth": 9,
                    "ssl_cipher": null,
                    "ssl_crl": null,
                    "ssl_key": null,
                    "ssl_verify_peer_certificate": false,
                    "ssl_verify_peer_host": false,
                    "ssl_version": "MAX",
                    "type": "listener",
                    "user_mapping_file": null
                },
                "source": {
                    "file": "/etc/maxscale.cnf",
                    "type": "static"
                },
                "state": "Running"
            },
            "id": "Read-Connection-Listener",
            "relationships": {
                "services": {
                    "data": [
                        {
                            "id": "Read-Connection-Router",
                            "type": "services"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/services/",
                        "self": "http://localhost:8989/v1/listeners/Read-Connection-Listener/relationships/services/"
                    }
                }
            },
            "type": "listeners"
        }
    ],
    "links": {
        "self": "http://localhost:8989/v1/listeners/"
    }
}
```



### Create a new listener



```
POST /v1/listeners
```



Creates a new listener. The request body must define the following fields.


* `<code>data.id</code>`
* Name of the listener
* `<code>data.type</code>`
* Type of the object, must be `<code>listeners</code>`
* `<code>data.attributes.parameters.port</code>` OR `<code>data.attributes.parameters.socket</code>`
* The TCP port or UNIX Domain Socket the listener listens on. Only one of the
 fields can be defined.
* `<code>data.relationships.services.data</code>`
* The service relationships data, must define a JSON object with an `<code>id</code>` value
 that defines the service to use and a `<code>type</code>` value set to `<code>services</code>`.


The following is the minimal required JSON object for defining a new listener.



```
{
    "data": {
        "id": "my-listener",
        "type": "listeners",
        "attributes": {
            "parameters": {
                "port": 3306
            }
        },
        "relationships": {
            "services": {
                "data": [
                    {"id": "RW-Split-Router", "type": "services"}
                ]
            }
        }
    }
}
```



Refer to the [Configuration Guide](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md) for
a full list of listener parameters.


#### Response


Listener is created:


`<code>Status: 204 No Content</code>`


### Update a listener



```
PATCH /v1/listeners/:name
```



The request body must be a JSON object which represents a set of new definitions
for the listener.


All parameters marked as modifiable at runtime can be modified. Currently, all
TLS/SSL parameters and the `<code>connection_init_sql_file</code>` and `<code>sql_mode</code>` parameters
can be modified at runtime.


Parameters that affect the network address or the port the listener listens on
cannot be modified at runtime. To modify these parameters, recreate the
listener.


#### Response


Listener is modified:


`<code>Status: 204 No Content</code>`


### Destroy a listener



```
DELETE /v1/listeners/:name
```



The *:name* must be a valid listener name. When a listener is destroyed, the
network port it listens on is available for reuse.


#### Response


Listener is destroyed:


`<code>Status: 204 No Content</code>`


Listener cannot be deleted:


`<code>Status: 400 Bad Request</code>`


### Stop a listener



```
PUT /v1/listeners/:name/stop
```



Stops a started listener. When a listener is stopped, new connections are no
longer accepted and are queued until the listener is started again.


#### Parameters


This endpoint supports the following parameters:


* `<code>force=yes</code>`
* Close all existing connections that were created through this listener.


#### Response


Listener is stopped:


`<code>Status: 204 No Content</code>`


### Start a listener



```
PUT /v1/listeners/:name/start
```



Starts a stopped listener.


#### Response


Listener is started:


`<code>Status: 204 No Content</code>`
