# MariaDB MaxScale MaxGUI Guide

* [MariaDB MaxScale MaxGUI Guide](mariadb-maxscale-25-mariadb-maxscale-maxgui-guide.md#mariadb-maxscale-maxgui-guide)
* [Introduction](mariadb-maxscale-25-mariadb-maxscale-maxgui-guide.md#introduction)
* [Enabling MaxGUI](mariadb-maxscale-25-mariadb-maxscale-maxgui-guide.md#enabling-maxgui)
  * [Securing the GUI](mariadb-maxscale-25-mariadb-maxscale-maxgui-guide.md#securing-the-gui)
* [Authentication](mariadb-maxscale-25-mariadb-maxscale-maxgui-guide.md#authentication)
* [Features](mariadb-maxscale-25-mariadb-maxscale-maxgui-guide.md#features)
  * [Dashboard page](mariadb-maxscale-25-mariadb-maxscale-maxgui-guide.md#dashboard-page)
  * [Detail page](mariadb-maxscale-25-mariadb-maxscale-maxgui-guide.md#detail-page)
  * [Resource creation](mariadb-maxscale-25-mariadb-maxscale-maxgui-guide.md#resource-creation)
  * [Viewing and modifying Maxscale parameters](mariadb-maxscale-25-mariadb-maxscale-maxgui-guide.md#viewing-and-modifying-maxscale-parameters)
  * [Global search](mariadb-maxscale-25-mariadb-maxscale-maxgui-guide.md#global-search)

## Introduction

_MaxGUI_ is the new browser based tool for configuring and managing\
MaxScale. It is a more user friendly and intuitive to use companion\
to the command line tool `maxctrl`.

## Enabling MaxGUI

To enable MaxGUI in a testing mode, add `admin_host=0.0.0.0` and`admin_secure_gui=false` under the `[maxscale]` section of the MaxScale\
configuration file. Once enabled, MaxGUI will be available on port 8989:`http://127.0.0.1:8989/`

### Securing the GUI

To make MaxGUI secure, set `admin_secure_gui=true` and configure both the`admin_ssl_key` and `admin_ssl_cert` parameters.

Check the [Configuration Guide](mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md) for the parameter\
documentation and read the _Configuration and Hardening_ section of the[REST API tutorial](../maxscale-25-tutorials/mariadb-maxscale-25-rest-api-tutorial.md) for instructions on\
how to harden your MaxScale installation for production use.

## Authentication

MaxGUI cannot be used without providing credentials. MaxGUI uses\
the same credentials as `maxctrl`, so by default, the username is`admin` and the password is `mariadb`.

MaxGUI uses [JSON Web Tokens](https://jwt.io/introduction/) as the\
authentication method for persisting the user's session.\
If the _Remember me_ checkbox is ticked, the session will persist for\
8 hours, otherwise, as soon as MaxGUI is closed, the session will expire.

To log out, simply click the username section in the top right corner of\
the page header to access the logout menu.

## Features

### Dashboard page

The dashboard shows three graphs:

* Sessions graph illustrates the total number of current sessions\
  updating every 10 seconds.
* Connections graph shows servers current connections\
  updating every 10 seconds.
* Load graph shows the last second load of thread,\
  which is updated every second.

Under the graphs section, there is a tab navigation allowing to switch\
table view which contains overview information of the\
following resources: all servers grouped by monitor, current sessions\
and all services. The information of these resources are\
updated every 10 seconds.

### Detail page

The monitor, server and services resources have their own details page.\
It can be accessed by clicking the resource name on the dashboard page.

In the details page, resource parameters as well as relationships\
can be modified in the resource's parameters section.

Deletion of a resource or other actions can be done by clicking the\
setting icon located next to the resource name.\
For instance, clicking the setting icon in Monitor detail page will\
popup three icons allowing a monitor to be started, stopped, and deleted.

For Servers, the monitor relationship can be modified by hovering\
over the rectangular _Monitor_ block section at the top of the page.

### Resource creation

A resource can be created by clicking the _+ Create New_ button at\
the top right corner of the dashboard or the detail page.

_Note_: Resources that depend on a module can be created only if that\
module has been loaded by MaxScale.

### Viewing and modifying Maxscale parameters

MaxScale parameters can be viewed and modified at runtime on the Settings\
page, which can be accessed by clicking the settings icon in the sidebar\
navigation.

### Global search

The global search input located next to the _+ Create New_ button can be\
used for searching for keywords in tables.

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
