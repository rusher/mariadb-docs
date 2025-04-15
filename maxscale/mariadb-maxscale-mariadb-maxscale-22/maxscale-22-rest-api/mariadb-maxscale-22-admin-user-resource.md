
# Admin User Resource

# Admin User Resource


Admin users represent administrative users that are able to query and change
MaxScale's configuration.


## Resource Operations


### Get network user


Get a single network user. The The *:name* in the URI must be a valid network
user name.



```
GET /v1/users/inet/:name
```



#### Response


`<code>Status: 200 OK</code>`



```
{
    "links": {
        "self": "http://localhost:8989/v1/users/inet/my-user"
    },
    "data": {
        "id": "my-user",
        "type": "inet",
        "attributes": {
            "account": "admin"
        },
        "relationships": {
            "self": "http://localhost:8989/v1/users/inet/my-user"
        }
    }
}
```



### Get all network users


Get all network users.



```
GET /v1/users/inet
```



#### Response


`<code>Status: 200 OK</code>`



```
{
    "links": {
        "self": "http://localhost:8989/v1/users/inet"
    },
    "data": [
        {
            "id": "my-user",
            "type": "inet",
            "attributes": {
                "account": "admin"
            },
            "relationships": {
                "self": "http://localhost:8989/v1/users/inet/my-user"
            }
        }
    ]
}
```



### Get enabled UNIX account


Get a single enabled UNIX account. The The *:name* in the URI must be a valid
UNIX account name that has been enabled.



```
GET /v1/users/unix/:name
```



#### Response


`<code>Status: 200 OK</code>`



```
{
    "links": {
        "self": "http://localhost:8989/v1/users/unix/maxscale"
    },
    "data": {
        "id": "maxscale",
        "type": "unix",
        "attributes": {
            "account": "basic"
        },
        "relationships": {
            "self": "http://localhost:8989/v1/users/unix/maxscale"
        }
    }
}
```



### Get all enabled UNIX accounts


Get all enabled UNIX accounts.



```
GET /v1/users/unix
```



#### Response


`<code>Status: 200 OK</code>`



```
{
    "links": {
        "self": "http://localhost:8989/v1/users/unix"
    },
    "data": [
        {
            "id": "maxscale",
            "type": "unix",
            "attributes": {
                "account": "admin"
            },
            "relationships": {
                "self": "http://localhost:8989/v1/users/unix/maxscale"
            }
        }
    ]
}
```



### Get all users


Get all administrative users. This fetches both network users and local UNIX
accounts.



```
GET /v1/users
```



#### Response


`<code>Status: 200 OK</code>`



```
{
    "links": {
        "self": "http://localhost:8989/v1/users/"
    },
    "data": [ // List of all users
        {
            "id": "my-user",
            "type": "inet", // A network user
            "attributes": {
                "account": "admin"
            },
            "relationships": {
                "self": "http://localhost:8989/v1/users/inet/my-user"
            }
        },
        {
            "id": "maxscale",
            "type": "unix", // A local UNIX account
            "attributes": {
                "account": "admin"
            },
            "relationships": {
                "self": "http://localhost:8989/v1/users/unix/maxscale"
            }
        }
    ]
}
```



### Create a network user


Create a new network user.



```
POST /v1/users/inet
```



The request body must fulfill the following requirements.


* The `<code>/data/id</code>`, `<code>/data/type</code>`, `<code>/data/attributes/account</code>` and
 `<code>/data/attributes/password</code>` fields must be defined.
* The `<code>/data/id</code>` field defines the name of the account
* The `<code>/data/attributes/password</code>` field defines the password for this user.
* The `<code>/data/attributes/account</code>` field should be set to `<code>admin</code>` for
 administrative users and `<code>basic</code>` to read-only users.
* The value of the `<code>/data/type</code>` field must always be `<code>inet</code>`.


Here is an example request body defining the network user *my-user* with the
password *my-password* that is allowed to execute only read-only operations.



```
{
    "data": {
        "id": "my-user",
        "type": "inet",
        "attributes": {
            "password": "my-password",
            "account": "basic"
        }
    }
}
```



#### Response



```
Status: 204 No Content
```



### Enable a UNIX account


This enables an existing UNIX account on the system for administrative
operations.



```
POST /v1/users/unix
```



The request body must fulfill the following requirements.


* The `<code>/data/id</code>`, `<code>/data/type</code>` and `<code>/data/attributes/account</code>` fields must be defined.
* The `<code>/data/id</code>` field defines the name of the account
* The `<code>/data/attributes/account</code>` field should be set to `<code>admin</code>` for
 administrative users and `<code>basic</code>` to read-only users.
* The value of the `<code>/data/type</code>` field must always be `<code>unix</code>`.


Here is an example request body enabling the UNIX account *jdoe* for read-only operations.



```
{
    "data": {
        "id": "jdoe",
        "type": "unix"
        "attributes": {
            "account": "basic"
        }
    }
}
```



#### Response



```
Status: 204 No Content
```



### Delete a network user


The *:name* part of the URI must be a valid user name.



```
DELETE /v1/users/inet/:name
```



#### Response



```
Status: 204 No Content
```



### Disable a UNIX account


The *:name* part of the URI must be a valid user name.



```
DELETE /v1/users/unix/:name
```



#### Response



```
Status: 204 No Content
```

