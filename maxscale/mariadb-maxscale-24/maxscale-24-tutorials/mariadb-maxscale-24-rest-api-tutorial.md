
# MaxScale REST API Tutorial

# REST API Tutorial


This tutorial is a quick overview of what the MaxScale REST API offers, how it
can be used to inspect the state of MaxScale and how to use it to modify the
runtime configuration of MaxScale. The tutorial uses the `<code>curl</code>` command line
client to demonstrate how the API is used.


## Configuration and Hardening


The MaxScale REST API listens on port 8989 on the local host. The `<code>admin_port</code>`
and `<code>admin_host</code>` parameters control which port and address the REST API listens
on. Note that for security reasons the API only listens for local connections
with the default configuration. It is critical that the default credentials are
changed and TLS/SSL encryption is configured before exposing the REST API to a
network.


The default user for the REST API is `<code>admin</code>` and the password is `<code>mariadb</code>`. The
easiest way to secure the REST API is to use the `<code>maxctrl</code>` command line client
to create a new admin user and delete the default one. To do this, run the
following commands:



```
maxctrl create user my_user my_password --type=admin
maxctrl destroy user admin
```



This will create the user `<code>my_user</code>` with the password `<code>my_password</code>` that is an
administrative account. After this account is created, the default `<code>admin</code>`
account is removed with the next command.


The next step is to enable TLS encryption. To do this, you need a CA
certificate, a private key and a public certificate file all in PEM format. Add
the following three parameters under the `<code>[maxscale]</code>` section of the MaxScale
configuration file and restart MaxScale.



```
admin_ssl_key=/certs/server-key.pem
admin_ssl_cert=/certs/server-cert.pem
admin_ssl_ca_cert=/certs/ca-cert.pem
```



Use `<code>maxctrl</code>` to verify that the TLS encryption is enabled. In this tutorial our
server certificates are self-signed so the `<code>--tls-verify-server-cert=false</code>`
option is required.



```
maxctrl --user=my_user --password=my_password --secure --tls-ca-cert=/certs/ca-cert.pem --tls-verify-server-cert=false show maxscale
```



If no errors are raised, this means that the communication via the REST API is
now secure and can be used across networks.


## Requesting Data


**Note:** For the sake of brevity, the rest of this tutorial will omit the
TLS/SSL options from the `<code>curl</code>` command line. For more information, refer to the
`<code>curl</code>` manpage.


The most basic task to do with the REST API is to see whether MaxScale is up and
running. To do this, we do a HTTP request on the root resource (the `<code>-i</code>` option
shows the HTTP headers).


`<code>curl -i 127.0.0.1:8989/v1/</code>`



```
HTTP/1.1 200 OK
Connection: Keep-Alive
Content-Length: 0
Last-Modified: Mon, 04 Mar 2019 08:23:09 GMT
ETag: "0"
Date: Mon, 04 Mar 19 08:29:41 GMT
```



To query a resource collection endpoint, append it to the URL. The `<code>/v1/filters/</code>`
endpoint shows the list of filters configured in MaxScale. This is a *resource
collection* endpoint: it contains the list of all resources of a particular
type.


`<code>curl 127.0.0.1:8989/v1/filters</code>`



```
{
    "links": {
        "self": "http://127.0.0.1:8989/v1/filters/"
    },
    "data": [
        {
            "id": "Hint",
            "type": "filters",
            "relationships": {
                "services": {
                    "links": {
                        "self": "http://127.0.0.1:8989/v1/services/"
                    },
                    "data": [
                        {
                            "id": "RW-Split-Hint-Router",
                            "type": "services"
                        }
                    ]
                }
            },
            "attributes": {
                "module": "hintfilter",
                "parameters": {}
            },
            "links": {
                "self": "http://127.0.0.1:8989/v1/filters/Hint"
            }
        },
        {
            "id": "Logger",
            "type": "filters",
            "relationships": {
                "services": {
                    "links": {
                        "self": "http://127.0.0.1:8989/v1/services/"
                    },
                    "data": []
                }
            },
            "attributes": {
                "module": "qlafilter",
                "parameters": {
                    "match": null,
                    "exclude": null,
                    "user": null,
                    "source": null,
                    "filebase": "/tmp/log",
                    "options": "ignorecase",
                    "log_type": "session",
                    "log_data": "date,user,query",
                    "newline_replacement": "\" \"",
                    "separator": ",",
                    "flush": false,
                    "append": false
                },
                "filter_diagnostics": {
                    "separator": ",",
                    "newline_replacement": "\" \""
                }
            },
            "links": {
                "self": "http://127.0.0.1:8989/v1/filters/Logger"
            }
        }
    ]
}
```



The `<code>data</code>` holds the actual list of resources: the `<code>Hint</code>` and `<code>Logger</code>`
filters. Each object has the `<code>id</code>` field which is the unique name of that
object. It is the same as the section name in `<code>maxscale.cnf</code>`.


Each resource in the list has a `<code>relationships</code>` object. This shows the
relationship links between resources. In our example, the `<code>Hint</code>` filter is used
by a service named `<code>RW-Split-Hint-Router</code>` and the `<code>Logger</code>` is not currently in
use.


To request an individual resource, we add the object name to the resource
collection URL. For example, if we want to get only the `<code>Logger</code>` filter we
execute the following command.


`<code>curl 127.0.0.1:8989/v1/filters/Logger</code>`



```
{
    "links": {
        "self": "http://127.0.0.1:8989/v1/filters/Logger"
    },
    "data": {
        "id": "Logger",
        "type": "filters",
        "relationships": {
            "services": {
                "links": {
                    "self": "http://127.0.0.1:8989/v1/services/"
                },
                "data": []
            }
        },
        "attributes": {
            "module": "qlafilter",
            "parameters": {
                "match": null,
                "exclude": null,
                "user": null,
                "source": null,
                "filebase": "/tmp/log",
                "options": "ignorecase",
                "log_type": "session",
                "log_data": "date,user,query",
                "newline_replacement": "\" \"",
                "separator": ",",
                "flush": false,
                "append": false
            },
            "filter_diagnostics": {
                "separator": ",",
                "newline_replacement": "\" \""
            }
        },
        "links": {
            "self": "http://127.0.0.1:8989/v1/filters/Logger"
        }
    }
}
```



Note that this time the `<code>data</code>` member holds an object instead of an array of
objects. All other parts of the response are similar to what was shown in the
previous example.


## Creating Objects


One of the uses of the REST API is to create new objects in MaxScale at
runtime. This allows new servers, services, filters, monitor and listeners to be
created without restarting MaxScale.


For example, to create a new server in MaxScale the JSON definition of a server
must be sent to the REST API at the `<code>/v1/servers/</code>` endpoint. The request body
defines the server name as well as the parameters for it.


To create objects with `<code>curl</code>`, first write the JSON definition into a file.



```
{
    "data": {
        "id": "server1",
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



To send the data, use the following command.



```
curl -X POST -d @new_server.txt 127.0.0.1:8989/v1/servers
```



The `<code>-d</code>` option takes a file name prefixed with a `<code>@</code>` as an argument. Here we
have `<code>@new_server.txt</code>` which is the name of the file where the JSON definition
was stored. The `<code>-X</code>` option defines the HTTP verb to use and to create a new
object we must use the POST verb.


To verify the data request the newly created object.



```
curl 127.0.0.1:8989/v1/servers/server1
```



## Modifying Data


The easiest way to modify an object is to first request it, store the result in
a file, edit it and then send the updated object back to the REST API.


Let's say we want to modify the port that the server we created earlier listens
on. First we request the current object and store the result in a file.



```
curl 127.0.0.1:8989/v1/servers/server1 > server1.txt
```



After that we edit the file and change the port from 3003 to 3306. Next the
modified JSON object is sent to the REST API as a PATCH command. To do this,
execute the following command.



```
curl -X PATCH -d @server1.txt 127.0.0.1:8989/v1/servers/server1
```



To verify that the data was updated correctly, request the updated object.



```
curl 127.0.0.1:8989/v1/servers/server1
```



## Object Relationships


To continue with our previous example, we add the updated server to a
service. To do this, the `<code>relationships</code>` object of the server must be modified
to include the service we want to add the server to.


To define a relationship between a server and a service, the `<code>data</code>` member must
have the `<code>relationships</code>` field and it must contain an object with the `<code>services</code>`
field (some fields omitted for brevity).



```
{
    "data": {
        "id": "server1",
        "type": "servers",
        "relationships": {
            "services": {
                "data": [
                    {
                        "id": "RW-Split-Router",
                        "type": "services"
                    }
                ]
            }
        },
        "attributes":  ...
    }
}
```



The `<code>data.relationships.services.data</code>` field contains a list of objects that
define the `<code>id</code>` and `<code>type</code>` fields. The id is the name of the object (a service
or a monitor for servers) and the type tells which type it is. Only `<code>services</code>`
type objects should be present in the `<code>services</code>` object.


In our example we are linking the `<code>server1</code>` server to the `<code>RW-Split-Router</code>`
service. As was seen with the previous example, the easiest way to do this is to
store the result, edit it and then send it back with a HTTP PATCH.


If we want to remove a server from *all* services and monitors, we can set the
`<code>data</code>` member of the `<code>services</code>` and `<code>monitors</code>` relationships to an empty array:



```
{
    "data": {
        "relationships": {
            "services": {
                "data": []
            },
            "monitors": {
                "data": []
            }
        }
    }
}
```



This is useful if you want to delete the server which can only be done if it has
no relationships to other objects.


## Deleting Objects


To delete an object, simply execute a HTTP DELETE request on the resource you
want to delete. For example, to delete the `<code>server1</code>` server, execute the
following command.



```
curl -X DELETE 127.0.0.1:8989/v1/servers/server1
```



In order to delete an object, it must not have any relationships to other
objects.


## Further Reading


The full list of all available endpoints in MaxScale can be found in the
[REST API documentation](../maxscale-24-rest-api/maxscale-24-rest-api-maxscale-rest-api.md).


The `<code>maxctrl</code>` command line client is self-documenting and the `<code>maxctrl help</code>`
command is a good tool for exploring the various commands that are available in
it. The `<code>maxctrl api get</code>` command can be useful way to explore the REST API as
it provides a way to easily extract values out of the JSON data generated by the
REST API.


There is a multitude of REST API clients readily available and most of them are
far more convenient to use than `<code>curl</code>`. We recommend investigating what you need
and how you intend to either integrate or use the MaxScale REST API. Most modern
languages either have a built-in HTTP library or there exists a de facto
standard library.


The MaxScale REST API follows the JSON API specification and there exist
libraries that are built specifically for these sorts of APIs
