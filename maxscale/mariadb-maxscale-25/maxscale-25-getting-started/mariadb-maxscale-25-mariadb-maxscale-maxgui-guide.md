
# MariaDB MaxScale MaxGUI Guide

# MariaDB MaxScale MaxGUI Guide




* [MariaDB MaxScale MaxGUI Guide](#mariadb-maxscale-maxgui-guide)
* [Introduction](#introduction)
* [Enabling MaxGUI](#enabling-maxgui)

  * [Securing the GUI](#securing-the-gui)
* [Authentication](#authentication)
* [Features](#features)

  * [Dashboard page](#dashboard-page)
  * [Detail page](#detail-page)
  * [Resource creation](#resource-creation)
  * [Viewing and modifying Maxscale parameters](#viewing-and-modifying-maxscale-parameters)
  * [Global search](#global-search)




# Introduction


*MaxGUI* is the new browser based tool for configuring and managing
MaxScale. It is a more user friendly and intuitive to use companion
to the command line tool `<code>maxctrl</code>`.


# Enabling MaxGUI


To enable MaxGUI in a testing mode, add `<code>admin_host=0.0.0.0</code>` and
`<code>admin_secure_gui=false</code>` under the `<code>[maxscale]</code>` section of the MaxScale
configuration file. Once enabled, MaxGUI will be available on port 8989:
`<code>http://127.0.0.1:8989/</code>`


## Securing the GUI


To make MaxGUI secure, set `<code>admin_secure_gui=true</code>` and configure both the
`<code>admin_ssl_key</code>` and `<code>admin_ssl_cert</code>` parameters.


Check the [Configuration Guide](mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md) for the parameter
documentation and read the *Configuration and Hardening* section of the
[REST API tutorial](../maxscale-25-tutorials/mariadb-maxscale-25-rest-api-tutorial.md) for instructions on
how to harden your MaxScale installation for production use.


# Authentication


MaxGUI cannot be used without providing credentials. MaxGUI uses
the same credentials as `<code>maxctrl</code>`, so by default, the username is
`<code>admin</code>` and the password is `<code>mariadb</code>`.


MaxGUI uses [JSON Web Tokens](https://jwt.io/introduction/) as the
authentication method for persisting the user's session.
If the *Remember me* checkbox is ticked, the session will persist for
8 hours, otherwise, as soon as MaxGUI is closed, the session will expire.


To log out, simply click the username section in the top right corner of
the page header to access the logout menu.


# Features


## Dashboard page


The dashboard shows three graphs:


* Sessions graph illustrates the total number of current sessions
 updating every 10 seconds.
* Connections graph shows servers current connections
 updating every 10 seconds.
* Load graph shows the last second load of thread,
 which is updated every second.


Under the graphs section, there is a tab navigation allowing to switch
table view which contains overview information of the
following resources: all servers grouped by monitor, current sessions
and all services. The information of these resources are
updated every 10 seconds.


## Detail page


The monitor, server and services resources have their own details page.
It can be accessed by clicking the resource name on the dashboard page.


In the details page, resource parameters as well as relationships
can be modified in the resource's parameters section.


Deletion of a resource or other actions can be done by clicking the
setting icon located next to the resource name.
For instance, clicking the setting icon in Monitor detail page will
popup three icons allowing a monitor to be started, stopped, and deleted.


For Servers, the monitor relationship can be modified by hovering
over the rectangular *Monitor* block section at the top of the page.


## Resource creation


A resource can be created by clicking the *+ Create New* button at
the top right corner of the dashboard or the detail page.


*Note*: Resources that depend on a module can be created only if that
module has been loaded by MaxScale.


## Viewing and modifying Maxscale parameters


MaxScale parameters can be viewed and modified at runtime on the Settings
page, which can be accessed by clicking the settings icon in the sidebar
navigation.


## Global search


The global search input located next to the *+ Create New* button can be
used for searching for keywords in tables.
