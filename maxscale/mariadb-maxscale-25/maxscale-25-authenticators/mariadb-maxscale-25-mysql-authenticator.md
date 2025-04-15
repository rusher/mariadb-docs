
# MaxScale 2.5 MySQL Authenticator

# MariaDB/MySQL Authenticator


The *MariaDBAuth*-module implements the client and backend authentication for the
server plugin *mysql_native_password*. This is the default authentication
plugin used by both MariaDB and MySQL.


## Authenticator options


The following settings may be given in the *authenticator_options* of the
listener.


### `<code>log_password_mismatch</code>`


Boolean, default value is "false". The service setting *log_auth_warnings* must
also be enabled for this setting to have effect. When both settings are enabled,
password hashes are logged if a client gives a wrong password. This feature may
be useful when diagnosing authentication issues. It should only be enabled on a
secure system as the logging of password hashes may be a security risk.


### `<code>cache_dir</code>`


Deprecated and ignored.


### `<code>inject_service_user</code>`


Deprecated and ignored.
