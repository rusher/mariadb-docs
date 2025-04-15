
# MaxScale 21.06 Admin User Resource

# Admin User Resource


Admin users represent administrative users that are able to query and change
MaxScale's configuration.




* [Admin User Resource](#admin-user-resource)

  * [Resource Operations](#resource-operations)

    * [Get network user](#get-network-user)

      * [Response](#response)
    * [Get all network users](#get-all-network-users)

      * [Response](#response_1)
    * [Get enabled UNIX account](#get-enabled-unix-account)
    * [Get all enabled UNIX accounts](#get-all-enabled-unix-accounts)
    * [Get all users](#get-all-users)

      * [Response](#response_2)
    * [Create a network user](#create-a-network-user)

      * [Response](#response_3)
    * [Enable a UNIX account](#enable-a-unix-account)

      * [Response](#response_4)
    * [Delete a network user](#delete-a-network-user)

      * [Response](#response_5)
    * [Disable a UNIX account](#disable-a-unix-account)

      * [Response](#response_6)
    * [Update a network user](#update-a-network-user)

      * [Response](#response_7)




## Resource Operations


### Get network user



```
GET /v1/users/inet/:name
```



Get a single network user. The The *:name* in the URI must be a valid network
user name.


#### Response


`<code>Status: 200 OK</code>`



```
{
    "data": {
        "attributes": {
            "account": "admin"
        },
        "id": "admin",
        "links": {
            "self": "http://localhost:8989/v1/users/inet/admin/"
        },
        "type": "inet"
    },
    "links": {
        "self": "http://localhost:8989/v1/users/inet/admin/"
    }
}
```



### Get all network users



```
GET /v1/users/inet
```



Get all network users.


#### Response


`<code>Status: 200 OK</code>`



```
{
    "data": [
        {
            "attributes": {
                "account": "admin"
            },
            "id": "admin",
            "links": {
                "self": "http://localhost:8989/v1/users/inet/admin/"
            },
            "type": "inet"
        }
    ],
    "links": {
        "self": "http://localhost:8989/v1/users/inet/"
    }
}
```



### Get enabled UNIX account



```
GET /v1/users/unix/:name
```



**Note:** This endpoint has been deprecated and does nothing.


### Get all enabled UNIX accounts



```
GET /v1/users/unix
```



**Note:** This endpoint has been deprecated and does nothing.


### Get all users



```
GET /v1/users
```



Get all administrative users.


#### Response


`<code>Status: 200 OK</code>`



```
{
    "data": [
        {
            "attributes": {
                "account": "admin"
            },
            "id": "admin",
            "links": {
                "self": "http://localhost:8989/v1/users/inet/admin/"
            },
            "type": "inet"
        }
    ],
    "links": {
        "self": "http://localhost:8989/v1/users/inet/"
    }
}
```



### Create a network user



```
POST /v1/users/inet
```



Create a new network user. The request body must define at least the
following fields.


* `<code>data.id</code>`
* The username
* `<code>data.type</code>`
* Type of the object, must be `<code>inet</code>`
* `<code>data.attributes.password</code>`
* The password for this user
* `<code>data.attributes.account</code>`
* Set to `<code>admin</code>` for administrative users and `<code>basic</code>` to read-only users


Only admin accounts can perform POST, PUT, DELETE and PATCH requests. If a basic
account performs one of the aforementioned request, the REST API will respond
with a `<code>401 Unauthorized</code>` error.


Here is an example request body defining the network user *my-user* with the
password *my-password* that is allowed to execute only read-only operations.



```
{
    "data": {
        "id": "my-user", // The user to create
        "type": "inet", // The type of the user
        "attributes": {
            "password": "my-password", // The password to use for the user
            "account": "basic" // The type of the account
        }
    }
}
```



#### Response



```
Status: 204 No Content
```



### Enable a UNIX account



```
POST /v1/users/unix
```



This enables an existing UNIX account on the system for administrative
operations. The request body must define at least the following fields.


* `<code>data.id</code>`
* The username
* `<code>data.type</code>`
* Type of the object, must be `<code>unix</code>`
* `<code>data.attributes.account</code>`
* Set to `<code>admin</code>` for administrative users and `<code>basic</code>` to read-only users


Here is an example request body enabling the UNIX account *jdoe* for read-only operations.



```
{
    "data": {
        "id": "jdoe", // Account name
        "type": "unix" // Account type
        "attributes": {
            "account": "basic" // Type of the user account in MaxScale
        }
    }
}
```



#### Response



```
Status: 204 No Content
```



### Delete a network user



```
DELETE /v1/users/inet/:name
```



The *:name* part of the URI must be a valid user name.


#### Response



```
Status: 204 No Content
```



### Disable a UNIX account



```
DELETE /v1/users/unix/:name
```



The *:name* part of the URI must be a valid user name.


#### Response



```
Status: 204 No Content
```



### Update a network user



```
PATCH /v1/users/inet/:name
```



Update network user. Currently, only the password can be updated. This
means that the request body must define the `<code>data.attributes.password</code>`
field.


Here is an example request body that updates the password.



```
{
    "data": {
        "attributes": {
            "password": "new-password"
        }
    }
}
```



#### Response



```
Status: 204 No Content
```

