# Authentication Modules in MaxScale

This document describes the modular authentication in MaxScale. It contains\
protocol specific information on authentication and how it is handled in\
MaxScale.

The constants described in this document are defined in the authenticator.h\
header unless otherwise mentioned.

Authenticator modules compatible with MySQL protocol in MaxScale are[MySQL](mariadb-maxscale-23-mysql-authenticator.md), [GSSAPI](../../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/) and[PAM](mariadb-maxscale-23-pam-authenticator.md).

### Authenticator initialization

When the authentication module is first loaded, the `initialize` entry point is\
called. The return value of this function will be passed as the first argument\
to the other entry points.

The `loadUsers` entry point of the client side authenticator is called when a\
service starts. The authenticator can load external user data when this entry\
point is called. This entry point is also called when user authentication has\
failed and the external user data needs to be refreshed.

When a connection is created, the `create` entry point is called to create per\
connection data. The return value of this function is stored in the`dcb->authenticator_data` field of the DCB object. This data is freed in the`destroy` entry point and the value returned by `create` will be given as the\
first parameter.

## MySQL Authentication Modules

The MySQL protocol authentication starts when the server sends the handshake\
packet to the client to which the client responds with a handshake response\
packet. If the server is using the default _mysql\_native\_password_\
authentication plugin, the server responds with either an OK packet or an ERR\
packet and the authentication is complete.

If a different authentication plugin is required to complete the authentication,\
instead of sending an OK or ERR packet, the server responds with an\
AuthSwitchRequest packet. This is where the pluggable authentication in MaxScale\
starts.

### Client authentication in MaxScale

The first packet the client side authenticator plugins will receive is the\
client's handshake response packet.

The client protocol module will call the `extract` entry point of the\
authenticator where the authenticator should extract client information. If the`extract` entry point returns MXS\_AUTH\_SUCCEEDED, the `authenticate` entry point\
will be called.

The `authenticate` entry point is where the authenticator plugin should\
authenticate the client. If authentication is successful, the `authenticate`\
entry point should return MXS\_AUTH\_SUCCEEDED. If authentication is not yet\
complete or if the authentication module should be changed, the `authenticate`\
entry point should return MXS\_AUTH\_INCOMPLETE.

Authenticator plugins which do not use the default _mysql\_native\_password_\
authentication plugin should send an AuthSwitchRequest packet to the client and\
return MXS\_AUTH\_INCOMPLETE. When more data is available, the `extract` and`authenticate` entry points will be called again.

If either of the aforementioned entry points returns one of the following\
constants, the authentication is considered to have failed and the session will\
be closed.

* MXS\_AUTH\_FAILED
* MXS\_AUTH\_FAILED\_DB
* MXS\_AUTH\_FAILED\_SSL

Read the individual authenticator module documentation for more details on the\
authentication process of each authentication plugin.

### Backend authentication in MaxScale

The first packet the authentication plugins in MaxScale will receive is either\
the AuthSwitchRequest packet or, in case of _mysql\_native\_password_, the OK\
packet. At this point, the protocol plugin will call the `extract` entry point\
of the backend authenticator. If the return value of the call is one of the\
following constants, the protocol plugin will call the `authenticate` entry\
point of the authenticator.

* MXS\_AUTH\_SUCCEEDED
* MXS\_AUTH\_INCOMPLETE

If the `authenticate` entry point returns MXS\_AUTH\_SUCCEEDED, then\
authentication is complete and any queued queries from the clients will be sent\
to the backend server. If the return value is MXS\_AUTH\_INCOMPLETE or\
MXS\_AUTH\_SSL\_INCOMPLETE, the protocol module will continue the authentication by\
calling the `extract` entry point once more data is available.

If either of the aforementioned entry points returns one of the following\
constants, the authentication is considered to have failed and the session will\
be closed.

* MXS\_AUTH\_FAILED
* MXS\_AUTH\_FAILED\_DB
* MXS\_AUTH\_FAILED\_SSL

Read the individual authenticator module documentation for more details on the\
authentication process of each authentication plugin.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
