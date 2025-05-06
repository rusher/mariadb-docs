
# Connecting to MaxScale using TLS with MaxCtrl


# Overview


[MaxCtrl](../README.md) is a command-line utility that can perform administrative tasks using MaxScale's [MaxScale's REST API](README.md). It is possible to connect to MaxScale using TLS with MaxCtrl.


# Connecting to MaxScale using TLS


1. [Create a basic](../creating-a-rest-api-user-for-maxscale-with-maxctrl.md#creating-a-basic-user) or [admin user](../creating-a-rest-api-user-for-maxscale-with-maxctrl.md#creating-an-admin-user), depending on what kind of user you need:


```
$ maxctrl create user "maxscale_rest_admin" "maxscale_rest_admin_password" --type=admin
```

Replace maxscale_rest_admin and maxscale_rest_admin_password with the desired user and password.


2. If you want to use MaxCtrl remotely, configure the REST API for remote connections.
Several global parameters must be configured in maxscale.cnf.



| Parameter | Description |
| --- | --- |
| Parameter | Description |
| [admin_host](../../../mariadb-maxscale-23-02/mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#admin_host) | * This parameter defines the network address that the REST API listens on. |
|  | * The default value is 127.0.0.1. |
| [admin_port](../../../mariadb-maxscale-23-02/mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#admin_port) | *This parameter defines the network port that the REST API listens on. |
|  | * The default value is 8989. |



For example:


```
[maxscale]
...
admin_host            = 0.0.0.0
admin_port            = 8443
```

3. Enable TLS for MaxScale's [Configure the REST API](../../administrative-tools-for-mariadb-maxscale-rest-api/README.md).
Several global parameters must be configured in maxscale.cnf.



| Parameter | Description |
| --- | --- |
| Parameter | Description |
| [admin_ssl_key](../../../mariadb-maxscale-23-02/mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#admin_ssl_key) | * This parameter defines the private key used by the REST API. |
| [admin_ssl_cert](../../../mariadb-maxscale-23-02/mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#admin_ssl_cert) | * This parameter defines the certificate used by the REST API. |
| [admin_ssl_ca_cert](../../../mariadb-maxscale-23-02/mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#admin_ssl_ca_cert) | *This parameter defines the CA certificate that signed the REST API's certificate. |



For example:


```
[maxscale]
...
admin_ssl_key=/certs/server-key.pem
admin_ssl_cert=/certs/server-cert.pem
admin_ssl_ca_cert=/certs/ca-cert.pem
```

4. Ensure that the client also has a TLS certificate, a private key, and the CA certificate.


5. Use [MaxCtrl](../README.md) to connect with TLS:


```
$ maxctrl --secure \
   --user=maxscale_rest_admin \
   --password=maxscale_rest_admin_password \
   --hosts=192.0.2.100:8443
   --tls-key=/certs/client-key.pem \
   --tls-cert=/certs/client-cert.pem \
   --tls-ca-cert=/certs/ca.pem
```

6. Replace `maxscale_rest_admin and maxscale_rest_admin_password` with the actual user and password.


Copyright © 2025 MariaDB

