
# Listener Resource

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
    * [Destroy a listener](#destroy-a-listener)

      * [Response](#response_3)




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
                "address": "::",
                "authenticator": null,
                "authenticator_options": "",
                "connection_init_sql_file": null,
                "port": 4006,
                "protocol": "MariaDBClient",
                "socket": null,
                "sql_mode": null,
                "ssl": "false",
                "ssl_ca_cert": null,
                "ssl_cert": null,
                "ssl_cert_verify_depth": 9,
                "ssl_cipher": null,
                "ssl_crl": null,
                "ssl_key": null,
                "ssl_verify_peer_certificate": false,
                "ssl_verify_peer_host": false,
                "ssl_version": "MAX"
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
        "self": "http://localhost:8989/v1/listeners/RW-Split-Listener"
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
                    "address": "::",
                    "authenticator": null,
                    "authenticator_options": "",
                    "connection_init_sql_file": null,
                    "port": 4008,
                    "protocol": "MariaDBClient",
                    "socket": null,
                    "sql_mode": null,
                    "ssl": "false",
                    "ssl_ca_cert": null,
                    "ssl_cert": null,
                    "ssl_cert_verify_depth": 9,
                    "ssl_cipher": null,
                    "ssl_crl": null,
                    "ssl_key": null,
                    "ssl_verify_peer_certificate": false,
                    "ssl_verify_peer_host": false,
                    "ssl_version": "MAX"
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
        },
        {
            "attributes": {
                "parameters": {
                    "address": "::",
                    "authenticator": null,
                    "authenticator_options": "",
                    "connection_init_sql_file": null,
                    "port": 4006,
                    "protocol": "MariaDBClient",
                    "socket": null,
                    "sql_mode": null,
                    "ssl": "false",
                    "ssl_ca_cert": null,
                    "ssl_cert": null,
                    "ssl_cert_verify_depth": 9,
                    "ssl_cipher": null,
                    "ssl_crl": null,
                    "ssl_key": null,
                    "ssl_verify_peer_certificate": false,
                    "ssl_verify_peer_host": false,
                    "ssl_version": "MAX"
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



Refer to the [Configuration Guide](../maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md) for
a full list of listener parameters.


#### Response


Listener is created:


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


`<code>Status: 403 Forbidden</code>`
