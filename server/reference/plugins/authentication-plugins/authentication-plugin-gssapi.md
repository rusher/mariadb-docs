
# Authentication Plugin - GSSAPI

The `<code>gssapi</code>` authentication plugin allows the user to authenticate with services that use the [Generic Security Services Application Program Interface (GSSAPI)](https://en.wikipedia.org/wiki/Generic_Security_Services_Application_Program_Interface). Windows has a slightly different but very similar API called [Security Support Provider Interface (SSPI)](https://docs.microsoft.com/en-us/windows/desktop/secauthn/sspi). The GSSAPI is a standardized API described in [RFC2743](https://tools.ietf.org/html/rfc2743.html) and [RFC2744](https://tools.ietf.org/html/rfc2744.html). The client and server negotiate using a standardized protocol described in [RFC7546](https://tools.ietf.org/html/rfc7546.html).


On Windows, this authentication plugin supports [Kerberos](https://docs.microsoft.com/en-us/windows/desktop/secauthn/microsoft-kerberos) and [NTLM](https://docs.microsoft.com/en-us/windows/desktop/secauthn/microsoft-ntlm) authentication. Windows authentication is supported regardless of whether a [domain](https://en.wikipedia.org/wiki/Windows_domain) is used in the environment.


On Unix systems, the most dominant GSSAPI service is [Kerberos](https://en.wikipedia.org/wiki/Kerberos_(protocol)). However, it is less commonly used on Unix systems than it is on Windows. Regardless, this authentication plugin also supports Kerberos authentication on Unix.


The `<code>gssapi</code>` authentication plugin is most often used for authenticating with [Microsoft Active Directory](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview).


This article gives instructions on configuring the `<code>gssapi</code>` authentication plugin
for MariaDB for passwordless login.



## Installing the Plugin's Package


Since [MariaDB 10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md), on Windows, the plugin is included in the server, and there is no need for separate installation.


The `<code>gssapi</code>` authentication plugin's shared library is included in MariaDB packages as the `<code>auth_gssapi.so</code>` or `<code>auth_gssapi.dll</code>` shared library on systems where it can be built.


### Installing on Linux


The `<code>gssapi</code>` authentication plugin is included in [binary tarballs](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/installing-mariadb-binary-tarballs.md) on Linux.


#### Installing with a Package Manager


The `<code>gssapi</code>` authentication plugin can also be installed via a package manager on Linux. In order to do so, your system needs to be configured to install from one of the MariaDB repositories.


You can configure your package manager to install it from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md).


You can also configure your package manager to install it from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/).


##### Installing with yum/dnf


On RHEL, CentOS, Fedora, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/README.md) from MariaDB's
repository using `<code>[yum](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/yum.md)</code>` or `<code>[dnf](https://en.wikipedia.org/wiki/DNF_(software))</code>`. Starting with RHEL 8 and Fedora 22, `<code>yum</code>` has been replaced by `<code>dnf</code>`, which is the next major version of `<code>yum</code>`. However, `<code>yum</code>` commands still work on many systems that use `<code>dnf</code>`. For example:


```
sudo yum install MariaDB-gssapi-server
```

##### Installing with apt-get


On Debian, Ubuntu, and other similar Linux distributions, it is highly recommended to install the relevant [DEB package](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md) from MariaDB's
repository using `<code>[apt-get](https://wiki.debian.org/apt-get)</code>`. For example:


```
sudo apt-get install mariadb-plugin-gssapi-server
```

##### Installing with zypper


On SLES, OpenSUSE, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/README.md) from MariaDB's repository using `<code>[zypper](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md)</code>`. For example:


```
sudo zypper install MariaDB-gssapi-server
```

### Installing on Windows


Since [MariaDB 10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md), the plugin is included in the server, and there is no need for separate installation.


Before [MariaDB 10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md), the `<code>gssapi</code>` authentication plugin is included in [MSI](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows.md) and [ZIP](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/installing-mariadb-windows-zip-packages.md) packages on Windows.


## Installing the Plugin


Since [MariaDB 10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md), on Windows, the plugin is included in the server, and there is no need for separate installation.


Before [MariaDB 10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md) on Windows, and on other operating systems, although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.


The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing `<code>[INSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md)</code>` or `<code>[INSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md)</code>`. For example:


```
INSTALL SONAME 'auth_gssapi';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) or the [--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) options. This can be specified as a command-line argument to [mariadbd](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
plugin_load_add = auth_gssapi
```

## Uninstalling the Plugin


You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md). For example:


```
UNINSTALL SONAME 'auth_gssapi';
```

If you installed the plugin by providing the `<code>[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or the `<code>[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` options in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.


## Configuring the Plugin


If the MariaDB server is running on Unix, then some additional configuration steps will need to be implemented in order to use the plugin.


If the MariaDB server is running on Windows, then no special configuration steps will need to be implemented in order to use the plugin, as long as the following is true:


* The Windows server is joined to a domain.
* The MariaDB server process is running as either a [NetworkService Account](https://docs.microsoft.com/en-us/windows/desktop/services/networkservice-account) or a [Domain User Account](https://docs.microsoft.com/en-us/windows/desktop/ad/domain-user-accounts).


### Creating a Keytab File on Unix


If the MariaDB server is running on Unix, then the KDC server will need to create a keytab file for the MariaDB server. The keytab file contains the service principal name, which is the identity that the MariaDB server will use to communicate with the KDC server. The keytab will need to be transferred to the MariaDB server, and the `<code>mysqld</code>` server process will need read access to this keytab file.


How this keytab file is generated depends on whether the KDC server is **[Microsoft Active Directory KDC](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)** or **[MIT Kerberos KDC](https://web.mit.edu/Kerberos/krb5-1.12/doc/index.html)**.


#### Creating a Keytab File with Microsoft Active Directory


If you are using **[Microsoft Active Directory KDC](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)**, then you may need to create a keytab using the `<code>[ktpass.exe](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ktpass)</code>` utility on a Windows host. The service principal will need to be mapped to an existing domain user. To do so, follow the steps listed below.


Be sure to replace the following items in the step below:


* Replace `<code>${HOST}</code>` with the fully qualified DNS name for the MariaDB server host.
* Replace `<code>${DOMAIN}</code>` with the Active Directory domain.
* Replace `<code>${AD_USER}</code>` with the existing domain user.
* Replace `<code>${PASSWORD}</code>` with the password for the service principal.


To create the service principal, execute the following:


```
ktpass.exe /princ mariadb/${HOST}@${DOMAIN} /mapuser ${AD_USER} /pass ${PASSWORD} /out mariadb.keytab /crypto all /ptype KRB5_NT_PRINCIPAL /mapop set
```

#### Creating a Keytab File with MIT Kerberos


If you are using **[MIT Kerberos KDC](https://web.mit.edu/Kerberos/krb5-1.12/doc/index.html)**, then you can create a [keytab](https://web.mit.edu/Kerberos/krb5-1.12/doc/admin/install_appl_srv.html#the-keytab-file) file using the `<code>[kadmin](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/admin_commands/kadmin_local.html)</code>` utility. To do so, follow the steps listed below.


In the following steps, be sure to replace `<code>${HOST}</code>` with the fully qualified DNS name for the MariaDB server host.


First, create the service principal using the `<code>[kadmin](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/admin_commands/kadmin_local.html)</code>` utility. For example:


```
kadmin -q "addprinc -randkey mariadb/${HOST}"
```

Then, export the newly created user to the keytab file using the `<code>[kadmin](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/admin_commands/kadmin_local.html)</code>` utility. For example:


```
kadmin -q "ktadd -k /path/to/mariadb.keytab mariadb/${HOST}"
```

More details can be found at the following links:


* [MIT Kerberos Documentation: Database administration](https://web.mit.edu/Kerberos/krb5-1.12/doc/admin/database.html)
* [MIT Kerberos Documentation: Application servers](https://web.mit.edu/Kerberos/krb5-1.12/doc/admin/appl_servers.html)


### Configuring the Path to the Keytab File on Unix


If the MariaDB server is running on Unix, then the path to the keytab file that was previously created can be set by configuring the `<code>[gssapi_keytab_path](#gssapi_keytab_path)</code>` system variable. This can be specified as a command-line argument to `<code>[mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
gssapi_keytab_path=/path/to/mariadb.keytab
```

### Configuring the Service Principal Name


The service principal name can be set by configuring the `<code>[gssapi_principal_name](#gssapi_principal_name)</code>` system variable. This can be specified as a command-line argument to `<code>[mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
gssapi_principal_name=service_principal_name/host.domain.com@REALM
```

If a service principal name is not provided, then the plugin will try to use `<code>mariadb/host.domain.com@REALM</code>` by default.


If the MariaDB server is running on Unix, then the plugin needs a service principal name in order to function.


If the MariaDB server is running on Windows, then the plugin does not usually need a service principal in order to function. However, if you want to use one anyway, then one can be created with the `<code>[setspn](https://social.technet.microsoft.com/wiki/contents/articles/717.service-principal-names-spns-setspn-syntax-setspn-exe.aspx)</code>` utility.


Different KDC implementations may use different canonical forms to identify principals. See [RFC2744: Section 3.10](https://tools.ietf.org/html/rfc2744.html#section-3.10) to learn what the standard says about principal names.


More details can be found at the following links:


* [Active Directory Domain Services: Service Principal Names](https://docs.microsoft.com/en-us/windows/win32/ad/service-principal-names)
* [MIT Kerberos Documentation: Realm configuration decisions](https://web.mit.edu/Kerberos/krb5-1.12/doc/admin/realm_config.html)
* [MIT Kerberos Documentation: Principal names and DNS](https://web.mit.edu/Kerberos/krb5-1.12/doc/admin/princ_dns.html)


## Creating Users


To create a user account via `<code>[CREATE USER](../../sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user.md)</code>`, specify the name of the plugin in the `<code>[IDENTIFIED VIA](../../sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user.md#identified-viawith-authentication_plugin)</code>` clause. For example:


```
CREATE USER username@hostname IDENTIFIED VIA gssapi;
```

If `<code>[SQL_MODE](../../../server-management/variables-and-modes/sql-mode.md)</code>` does not have `<code>NO_AUTO_CREATE_USER</code>` set, then you can also create the user account via `<code>[GRANT](../../sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md)</code>`. For example:


```
GRANT SELECT ON db.* TO username@hostname IDENTIFIED VIA gssapi;
```

You can also specify the user's [realm](https://docs.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-crp-realm-names) for MariaDB with the `<code>USING</code>` clause. For example:


```
CREATE USER username@hostname IDENTIFIED VIA gssapi USING 'username@EXAMPLE.COM';
```

The format of the realm depends on the specific authentication mechanism that is used. For example, the format would need to be `<code>machine\\username</code>` for Windows users authenticating with NTLM.


If the realm is not provided in the user account's definition, then the realm is **not** used for comparison. Therefore, 'usr1@EXAMPLE.COM', 'usr1@EXAMPLE.CO.UK' and 'mymachine\usr1' would all identify as the following user account:


```
CREATE USER usr1@hostname IDENTIFIED VIA gssapi;
```

### Creating Users Identified Via Group Membership or SID (Windows-specific)


Since 10.6.0, on Windows only, it is possible to login using a AD or local group-membership. 
This is achieved by using GROUP prefix in IDENTIFIED ... AS


```
CREATE USER root IDENTIFIED VIA gssapi as 'GROUP:Administrators'
CREATE USER root IDENTIFIED VIA gssapi as 'GROUP:BUILTIN\\Administrators'
```

Effect of the above definition is that every user that identifies as member of group Administrators can login
using user name root, passwordless.


User can also login using own or group [SID](https://en.wikipedia.org/wiki/Security_Identifier)


```
CREATE USER root IDENTIFIED VIA gssapi as 'SID:S-1-5-32-544'
```

Using SIDs will perform slightly faster than using name (since it will spare translation between SID and name which is otherwise done), also SIDs immune against user or group renaming.


## Passwordless login on Windows



##### MariaDB starting with [10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md)
From [MariaDB 10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md), on Windows, in addition to the usual authentication with a password, passwordless authentication is permitted, when creating the 'root' user during install.
This works in a similar manner to [Unix socket authentication](../../../security/user-account-management/authentication-from-mariadb-10-4.md). However, since auth_gssapi, unlike unix_socket, requires client support, to avoid failures when MariaDB is used with 3rd party drivers, authentication on Windows first attempts password-based native_authentication, and only if it fails, falls back to passwordless auth_gssapi.


## Client Authentication Plugins


For clients that use the `<code>libmysqlclient</code>` or [MariaDB Connector/C](../../../../connectors/mariadb-connector-cpp/mariadb-connector-cpp-sample-application.md) libraries, MariaDB provides one client authentication plugin that is compatible with the `<code>gssapi</code>` authentication plugin:


* `<code>auth_gssapi_client</code>`


When connecting with a [client or utility](/kb/en/clients-utilities/) to a server as a user account that authenticates with the `<code>gssapi</code>` authentication plugin, you may need to tell the client where to find the relevant client authentication plugin by specifying the `<code>--plugin-dir</code>` option. For example:


```
mysql --plugin-dir=/usr/local/mysql/lib64/mysql/plugin --user=alice
```

### `<code>auth_gssapi_client</code>`


The `<code>auth_gssapi_client</code>` client authentication plugin receives the principal name from the server, and then uses either the `<code>[gss_init_sec_context](https://web.mit.edu/kerberos/krb5-devel/doc/appdev/gssapi.html#initiator-credentials)</code>` function (on Unix) or the `<code>[InitializeSecurityContext](https://docs.microsoft.com/en-us/windows/desktop/api/sspi/nf-sspi-initializesecuritycontexta)</code>` function (on Windows) to establish a security context on the client.


## Support in Client Libraries


### Using the Plugin with MariaDB Connector/C


[MariaDB Connector/C](../../../../connectors/mariadb-connector-cpp/mariadb-connector-cpp-sample-application.md) supports `<code>gssapi</code>` authentication using the [client authentication plugins](#client-authentication-plugins) mentioned in the previous section since MariaDB Connector/C 3.0.1.


### Using the Plugin with MariaDB Connector/ODBC


[MariaDB Connector/ODBC](../../../../connectors/mariadb-connector-odbc/README.md) supports `<code>gssapi</code>` authentication using the [client authentication plugins](#client-authentication-plugins) mentioned in the previous section since MariaDB Connector/ODBC 3.0.0.


### Using the Plugin with MariaDB Connector/J


[MariaDB Connector/J](../../../../connectors/mariadb-connector-j/mariadb-connector-j-releases.md) supports `<code>gssapi</code>` authentication since MariaDB Connector/J 1.4.0. Current documentation can be found [here](../../../../connectors/mariadb-connector-j/gssapi-authentication-with-mariadb-connector-j.md).


### Using the Plugin with MariaDB Connector/Node.js


[MariaDB Connector/Node.js](/kb/en/nodejs-connector/) does not yet support `<code>gssapi</code>` authentication. See [CONJS-72](https://jira.mariadb.org/browse/CONJS-72) for more information.


### Using the Plugin with MySqlConnector for .NET


[MySqlConnector for ADO.NET](../../../../connectors/net-connector/mysqlconnector-for-ado-net.md) supports `<code>gssapi</code>` authentication since MySqlConnector 0.47.0.


The support is transparent. Normally, the connector only needs to be provided the correct user name, and no other parameters are required.


However, this connector also supports the `<code>[ServerSPN](https://mysql-net.github.io/MySqlConnector/connection-options)</code>` connection string parameter, which can be used for mutual authentication.


#### .NET specific problems/workarounds


When connecting from Unix client to Windows server with ADO.NET, in an Active Directory domain environment, be aware that .NET Core on Unix does not support principal names in UPN(User Principal Name) form, which is default on Windows (e.g machine$@domain.com) . Thus, upon encountering an authentication exception with "server not found in Kerberos database", use one of workarounds below


* Force host-based SPN on server side.

  * For example, this can be done by setting the `<code>[gssapi_principal_name](#gssapi_principal_name)</code>` system variable to `<code>HOST/machine</code>` in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md).
* Pass host-based SPN on client side.

  * For example, this can be done by setting the connector's `<code>[ServerSPN](https://mysql-net.github.io/MySqlConnector/connection-options)</code>` connection string parameter to `<code>HOST/machine</code>`.


## Versions



| Version | Status | Introduced |
| --- | --- | --- |
| Version | Status | Introduced |
| 1.0 | Stable | [MariaDB 10.1.15](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10115-release-notes.md) |
| 1.0 | Beta | [MariaDB 10.1.11](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10111-release-notes.md) |



## System Variables


### `<code>gssapi_keytab_path</code>`


* Description: Defines the path to the server's keytab file.

  * This system variable is only meaningful on Unix.
  * See [Creating a Keytab File on Unix](#creating-a-keytab-file) and [Configuring the Path to the Keytab File on Unix](#configuring-the-path-to-the-keytab-file-on-unix) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--gssapi-keytab-path</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: ''
* Introduced: [MariaDB 10.1.11](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10111-release-notes.md)



### `<code>gssapi_principal_name</code>`


* Description: Name of the service principal.

  * See [Configuring the Service Principal Name](#configuring-the-service-principal-name) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--gssapi-principal-name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: ''
* Introduced: [MariaDB 10.1.11](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10111-release-notes.md)



### `<code>gssapi_mech_name</code>`


* Description: Name of the SSPI package used by server. Can be either 'Kerberos' or 'Negotiate'. Set it to 'Kerberos', to prevent less secure NTLM in domain environments, but leave it as default (Negotiate) to allow non-domain environments (e.g if server does not run in a domain environment).

  * This system variable is only meaningful on Windows.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--gssapi-mech-name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>enumerated</code>`
* Default Value: `<code>Negotiate</code>`
* Valid Values: `<code>Kerberos</code>`, `<code>Negotiate</code>`
* Introduced: [MariaDB 10.1.11](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10111-release-notes.md)



## Options


### `<code>gssapi</code>`


* Description: Controls how the server should treat the plugin when the server starts up.

  * Valid values are:

    * `<code>OFF</code>` - Disables the plugin without removing it from the `<code>[mysql.plugins](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md)</code>` table.
    * `<code>ON</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `<code>FORCE</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `<code>FORCE_PLUS_PERMANENT</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with `<code>[UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)</code>` or `<code>[UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)</code>` while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--gssapi=value</code>`
* Data Type: `<code>enumerated</code>`
* Default Value: `<code>ON</code>`
* Valid Values: `<code>OFF</code>`, `<code>ON</code>`, `<code>FORCE</code>`, `<code>FORCE_PLUS_PERMANENT</code>`
* Introduced: [MariaDB 10.1.11](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10111-release-notes.md)


