# operating-maxscale-with-maxctrl-deleting-a-rest-api-user-for-maxscale-with-

## Deleting a REST API User for MaxScale with MaxCtrl

## Overview

MaxScale has a [MaxScale's REST API](./), which can be configured to require authentication. When it is first installed, it has a single default admin user (admin) and password (mariadb). However, this user can be deleted, and other users can be created.

MaxCtrl is a command-line utility that can perform administrative tasks using MaxScale's [MaxScale's REST API](./). It can be used to delete a user for the [MaxScale's REST API](./).

## Deleting a User

1. [Configure the REST API](../../administrative-tools-for-mariadb-maxscale-rest-api/) if the default configuration is not sufficient.
2. Use [MaxCtrl](../) to execute the [destroy user](../../../other-maxscale-versions/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl.md#destroy-user) command:

```
$ maxctrl --secure \
   --user=maxscale_rest_admin \
   --password=maxscale_rest_admin_password \
   --hosts=192.0.2.100:8443
   --tls-key=/certs/client-key.pem \
   --tls-cert=/certs/client-cert.pem \
   --tls-ca-cert=/certs/ca.pem \
   destroy user "admin"
```

3. Replace admin with the actual user.

MaxScale will refuse to delete the last remaining admin user.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
