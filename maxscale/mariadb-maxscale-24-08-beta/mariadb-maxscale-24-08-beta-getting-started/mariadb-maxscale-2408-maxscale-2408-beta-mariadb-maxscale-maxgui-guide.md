
# MaxScale 24.08 Beta MariaDB MaxScale MaxGUI Guide

# MariaDB MaxScale MaxGUI Guide




* [MariaDB MaxScale MaxGUI Guide](#mariadb-maxscale-maxgui-guide)
* [Introduction](#introduction)
* [Enabling MaxGUI](#enabling-maxgui)

  * [Securing the GUI](#securing-the-gui)
* [Authentication](#authentication)
* [Pages](#pages)

  * [Dashboard](#dashboard)
  * [Detail](#detail)
  * [Visualization](#visualization)
  * [Settings](#settings)
  * [Logs Archive](#logs-archive)
  * [Workspace](#workspace)

    * [1. Run Queries](#1-run-queries)
    * [2. Data Migration](#2-data-migration)
    * [3. Create an ERD](#3-create-an-erd)




# Introduction


*MaxGUI* is a browser-based interface for MaxScale REST-API and query execution.


# Enabling MaxGUI


To enable MaxGUI in a testing mode, add `<code>admin_host=0.0.0.0</code>` and
`<code>admin_secure_gui=false</code>` under the `<code>[maxscale]</code>` section of the MaxScale
configuration file. Once enabled, MaxGUI will be available on port 8989:
`<code>http://127.0.0.1:8989/</code>`


## Securing the GUI


To make MaxGUI secure, set `<code>admin_secure_gui=true</code>` and configure both the
`<code>admin_ssl_key</code>` and `<code>admin_ssl_cert</code>` parameters.


See [Configuration Guide](mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md) and
[Configuration and Hardening](../mariadb-maxscale-24-08-beta-tutorials/mariadb-maxscale-2408-maxscale-2408-beta-rest-api-tutorial.md)
for instructions on how to harden your MaxScale installation for production use.


# Authentication


MaxGUI uses the same credentials as `<code>maxctrl</code>`. The default username is `<code>admin</code>`
with `<code>mariadb</code>` as the password.


Internally, MaxGUI uses [JSON Web Tokens](https://jwt.io/introduction/) as the
authentication method for persisting the user's session. If the *Remember me*
checkbox is ticked, the session will persist for 24 hours. Otherwise, the
session will expire as soon as MaxGUI is closed.


To log out, simply click the username section in the top right corner of the
page header to access the logout menu.


# Pages


## Dashboard


This page provides an overview of MaxScale configuration which includes
Monitors, Servers, Services, Sessions, Listeners, and Filters.


By default, the refresh interval is 10 seconds.


## Detail


This page shows information on each
[MaxScale object](mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md) and allow to edit its
parameter, relationships and perform other manipulation operations.


Access this page by clicking on the MaxScale object name on the
[dashboard page](#dashboard)


## Visualization


This page visualizes MaxScale configuration and clusters.


* Configuration: Visualizing MaxScale configuration.
* Cluster: Visualizing a replication cluster into a tree graph and provides
 manual cluster manipulation operations such as
 `<code>switchover, reset-replication, release-locks, failover, rejoin</code>` . At the
 moment, it supports only servers monitored by Monitor using
 [mariadbmon](../mariadb-maxscale-2408-beta-maxscale-24-08-beta-monitors/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-monitor.md) module.


Access this page by clicking the graph icon on the sidebar navigation.


## Settings


This page shows and allows editing of MaxScale parameters.


Access this page by clicking the gear icon on the sidebar navigation.


## Logs Archive


Realtime MaxScale logs can be accessed by clicking the logs icon on the sidebar
navigation.


## Workspace


The "Workspace" page offers a versatile set of tools for effectively managing
data and database interactions. It includes the following key tasks:


### 1. Run Queries


Execute queries on various servers, services, or listeners to retrieve data and
perform database operations. Visualize query results using different graph
types such as line, bar, or scatter graphs. Export query results in formats
like CSV or JSON for further analysis and sharing.


### 2. Data Migration


The "Data Migration" feature facilitates seamless transitions from PostgreSQL
to MariaDB. Transfer data and database structures between the two systems while
ensuring data integrity and consistency throughout the process.


### 3. Create an ERD


Generating Entity-Relationship Diagrams (ERDs) to gain insights regarding data
structure, optimizing database design for both efficiency and clarity.
