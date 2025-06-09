
# MaxScale GSSAPI Client Authenticator

# MaxScale GSSAPI Client Authenticator


GSSAPI is an authentication protocol that is commonly implemented with
Kerberos on Unix or Active Directory on Windows. This document describes
the GSSAPI authentication in MaxScale.


The *GSSAPIAuth* module implements the client side authentication and the
*GSSAPIBackendAuth* module implements the backend authentication.


## Preparing the GSSAPI system


For Unix systems, the usual GSSAPI implementation is Kerberos. This is a short
guide on how to set up Kerberos for MaxScale.


The first step is to create a new principal for MaxScale. This can be done with
the *kadmin* or *kadmin.local* tools.



```
kadmin.local -q "addprinc -nokey mariadb/example.com@EXAMPLE.COM"
```



The `-nokey` option will make the principal a passwordless one. This allows the
*maxscale* user to acquire a ticket for it without a password being prompted.


The next step is to export this principal into the Kerberos keytab file.



```
kadmin.local -q "ktadd -k /etc/krb5.keytab -norandkey mariadb/example.com@EXAMPLE.COM"
```



This adds the *mariadb/[example.com@EXAMPLE.COM](https://mariadb.com/kb/en/mailto:example.com@EXAMPLE.COM)* principal into the keytab
file. The `-norandkey` option tells that the password we defined earlier,
i.e. no password at all, should be used instead of a random password.


The MariaDB documentation for the [GSSAPI Authentication Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi)
is a good example on how to set up a new principal for the MariaDB server.


## Authenticator options


The client side GSSAPIAuth authenticator supports one option, the service
principal name that MaxScale sends to the client. The backend authenticator
module has no options.


### `principal_name`


The service principal name to send to the client. This parameter is a
string parameter which is used by the client to request the token.


The default value for this option is *mariadb/localhost.localdomain*.


The parameter must be a valid GSSAPI principal name
e.g. `styx/pluto@EXAMPLE.COM`. The principal name can also be defined
without the realm part in which case the default realm will be used.


## Implementation details


Read the [Authentication Modules](mariadb-maxscale-21-authentication-modules-in-maxscale.md) document for more
details on how authentication modules work in MaxScale.


### GSSAPI authentication


The GSSAPI plugin authentication starts when the database server sends the
service principal name in the AuthSwitchRequest packet. The principal name will
usually be in the form `service@REALM.COM`.


The client will then request a token for this service from the GSSAPI server and
send the token to the database server. The database server will verify the
authenticity of the token by contacting the GSSAPI server and if the token is
authentic, the server sends the final OK packet.


## Limitations


Client side GSSAPI authentication is only supported when the backend
connections use GSSAPI authentication.


See the [Limitations](../about-maxscale-21/mariadb-maxscale-21-limitations-and-known-issues-within-mariadb-maxscale.md) document for more details.


## Building the module


The GSSAPI authenticator modules require the GSSAPI and the SQLite3 development
libraries (krb5-devel and sqlite-devel on CentOS 7).


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
