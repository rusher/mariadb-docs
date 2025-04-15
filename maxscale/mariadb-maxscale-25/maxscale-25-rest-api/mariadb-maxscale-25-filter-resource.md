
# Filter Resource

# Filter Resource


A filter resource represents an instance of a filter inside MaxScale. Multiple
services can use the same filter and a single service can use multiple filters.




* [Filter Resource](#filter-resource)

  * [Resource Operations](#resource-operations)

    * [Get a filter](#get-a-filter)

      * [Response](#response)
    * [Get all filters](#get-all-filters)

      * [Response](#response_1)
    * [Create a filter](#create-a-filter)

      * [Response](#response_2)
    * [Destroy a filter](#destroy-a-filter)

      * [Response](#response_3)




## Resource Operations


The *:name* in all of the URIs must be the name of a filter in MaxScale.


### Get a filter


Get a single filter.



```
GET /v1/filters/:name
```



#### Response


`<code>Status: 200 OK</code>`



```
{
    "data": {
        "attributes": {
            "filter_diagnostics": {
                "newline_replacement": " ",
                "separator": ","
            },
            "module": "qlafilter",
            "parameters": {
                "append": false,
                "exclude": null,
                "filebase": "/tmp/qla.log",
                "flush": true,
                "log_data": "date,user,query",
                "log_type": "unified",
                "match": null,
                "newline_replacement": " ",
                "options": "ignorecase",
                "separator": ",",
                "source": null,
                "user": null
            }
        },
        "id": "QLA",
        "links": {
            "self": "http://localhost:8989/v1/filters/QLA"
        },
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
                    "self": "http://localhost:8989/v1/filters/QLA/relationships/services"
                }
            }
        },
        "type": "filters"
    },
    "links": {
        "self": "http://localhost:8989/v1/filters/QLA"
    }
}
```



### Get all filters


Get all filters.



```
GET /v1/filters
```



#### Response


`<code>Status: 200 OK</code>`



```
{
    "data": [
        {
            "attributes": {
                "module": "hintfilter",
                "parameters": {}
            },
            "id": "Hint",
            "links": {
                "self": "http://localhost:8989/v1/filters/Hint"
            },
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
                        "self": "http://localhost:8989/v1/filters/Hint/relationships/services"
                    }
                }
            },
            "type": "filters"
        },
        {
            "attributes": {
                "filter_diagnostics": {
                    "newline_replacement": " ",
                    "separator": ","
                },
                "module": "qlafilter",
                "parameters": {
                    "append": false,
                    "exclude": null,
                    "filebase": "/tmp/qla.log",
                    "flush": true,
                    "log_data": "date,user,query",
                    "log_type": "unified",
                    "match": null,
                    "newline_replacement": " ",
                    "options": "ignorecase",
                    "separator": ",",
                    "source": null,
                    "user": null
                }
            },
            "id": "QLA",
            "links": {
                "self": "http://localhost:8989/v1/filters/QLA"
            },
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
                        "self": "http://localhost:8989/v1/filters/QLA/relationships/services"
                    }
                }
            },
            "type": "filters"
        }
    ],
    "links": {
        "self": "http://localhost:8989/v1/filters/"
    }
}
```



### Create a filter



```
POST /v1/filters
```



Create a new filter. The posted object must define at
least the following fields.


* `<code>data.id</code>`
* Name of the filter
* `<code>data.type</code>`
* Type of the object, must be `<code>filters</code>`
* `<code>data.atttributes.module</code>`
* The filter module to use


All of the filter parameters should be defined at creation time in the
`<code>data.atttributes.parameters</code>` object.


As the service to filter relationship is ordered (filters are applied in the
order they are listed), filter to service relationships cannot be defined at
creation time.


The following example defines a request body which creates a new filter.



```
{
    "data": {
        "id": "test-filter", // Name of the filter
        "type": "filters",
        "attributes": {
            "module": "qlafilter", // The filter uses the qlafilter module
            "parameters": { // Filter parameters
                "filebase": "/tmp/qla.log"
            }
        }
    }
}
```



#### Response


Filter is created:


`<code>Status: 204 No Content</code>`


### Destroy a filter



```
DELETE /v1/filters/:filter
```



The *:filter* in the URI must map to the name of the filter to be destroyed.


A filter can only be destroyed if no service uses it. This means that the
`<code>data.relationships</code>` object for the filter must be empty. Note that the service
→ filter relationship cannot be modified from the filters resource and must be
done via the services resource.


This endpoint also supports the `<code>force=yes</code>` parameter that will unconditionally
delete the filter by first removing it from all services that it uses.


#### Response


Filter is destroyed:


`<code>Status: 204 No Content</code>`
