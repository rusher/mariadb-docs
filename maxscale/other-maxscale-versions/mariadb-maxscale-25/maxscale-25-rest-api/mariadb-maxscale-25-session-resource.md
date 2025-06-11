# Session Resource

A session is an abstraction of a client connection, any number of related backend\
connections, a router module session and possibly filter module sessions. Each\
session is created on a service and each service can have multiple sessions.

* [Session Resource](mariadb-maxscale-25-session-resource.md#session-resource)
  * [Resource Operations](mariadb-maxscale-25-session-resource.md#resource-operations)
    * [Get a session](mariadb-maxscale-25-session-resource.md#get-a-session)
      * [Response](mariadb-maxscale-25-session-resource.md#response)
    * [Get all sessions](mariadb-maxscale-25-session-resource.md#get-all-sessions)
      * [Response](mariadb-maxscale-25-session-resource.md#response_1)

### Resource Operations

#### Get a session

```
GET /v1/sessions/:id
```

Get a single session. _:id_ must be a valid session ID. The session ID is the\
same that is exposed to the client as the connection ID.

This endpoint also supports the `rdns=true` parameter, which instructs MaxScale to\
perform reverse DNS on the client IP address. As this requires communicating with\
an external server, the operation may be expensive.

**Response**

`Status: 200 OK`

```
{
    "data": {
        "attributes": {
            "client": {
                "cipher": ""
            },
            "connected": "Thu Jul 20 07:28:51 2023",
            "connections": [
                {
                    "cipher": "",
                    "connection_id": 9,
                    "server": "server1"
                },
                {
                    "cipher": "",
                    "connection_id": 9,
                    "server": "server2"
                }
            ],
            "default_database": "test",
            "idle": 0.10000000000000001,
            "log": [],
            "queries": [],
            "remote": "::ffff:127.0.0.1",
            "state": "Session started",
            "user": "maxuser"
        },
        "id": "1",
        "links": {
            "self": "http://localhost:8989/v1/sessions/1"
        },
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
                    "self": "http://localhost:8989/v1/sessions/1/relationships/services"
                }
            }
        },
        "type": "sessions"
    },
    "links": {
        "self": "http://localhost:8989/v1/sessions/1"
    }
}
```

#### Get all sessions

```
GET /v1/sessions
```

Get all sessions.

**Response**

`Status: 200 OK`

```
{
    "data": [
        {
            "attributes": {
                "client": {
                    "cipher": ""
                },
                "connected": "Thu Jul 20 07:28:51 2023",
                "connections": [
                    {
                        "cipher": "",
                        "connection_id": 9,
                        "server": "server1"
                    },
                    {
                        "cipher": "",
                        "connection_id": 9,
                        "server": "server2"
                    }
                ],
                "default_database": "test",
                "idle": 0.10000000000000001,
                "log": [],
                "queries": [],
                "remote": "::ffff:127.0.0.1",
                "state": "Session started",
                "user": "maxuser"
            },
            "id": "1",
            "links": {
                "self": "http://localhost:8989/v1/sessions/1"
            },
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
                        "self": "http://localhost:8989/v1/sessions/1/relationships/services"
                    }
                }
            },
            "type": "sessions"
        }
    ],
    "links": {
        "self": "http://localhost:8989/v1/sessions/"
    }
}
```

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
