# Creating a REST API User for MaxScale with MaxCtrl

## Overview

MaxScale has a [MaxScale's REST API](./), which can be configured to require authentication. When it is first installed, it has a single default admin user (admin) and password (mariadb). However, this user can be deleted, and other users can be created.

[MaxCtrl](../) is a command-line utility that can perform administrative tasks using MaxScale's REST API. It can be used to create a user for the [Configure the REST API](broken-reference).

## User Types

There are two types of users:

| User Type | Description                                                             |
| --------- | ----------------------------------------------------------------------- |
| Basic     | The user has read-only access                                           |
| Admin     | The user can change global MaxScale parameters and reconfigure modules. |

## Creating a Basic User

1. [Configure the REST API](broken-reference) if the default configuration is not sufficient.
2. Use [MaxCtrl](../) to execute the create user command:

```
$ maxctrl --secure \
   --user=admin \
   --password=mariadb \
   --hosts=192.0.2.100:8443
   --tls-key=/certs/client-key.pem \
   --tls-cert=/certs/client-cert.pem \
   --tls-ca-cert=/certs/ca.pem \
   create user "maxscale_rest" "maxscale_rest_password"
```

Replace maxscale\_rest and maxscale\_rest\_password with the desired user and password.

## Creating an Admin User

1. [Configure the REST API](broken-reference) if the default configuration is not sufficient.
2. Use [MaxCtrl](../) to execute the create user command with the --type=admin option:

```
$ maxctrl --secure \
   --user=admin \
   --password=mariadb \
   --hosts=192.0.2.100:8443
   --tls-key=/certs/client-key.pem \
   --tls-cert=/certs/client-cert.pem \
   --tls-ca-cert=/certs/ca.pem \
   create user "maxscale_rest_admin" "maxscale_rest_admin_password" --type=admin
```

3. Replace maxscale\_rest\_admin and maxscale\_rest\_admin\_password with the desired user and password.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
