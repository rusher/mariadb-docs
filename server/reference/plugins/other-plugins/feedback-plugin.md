
# Feedback Plugin

The `<code>feedback</code>` plugin is designed to collect and, optionally, upload
configuration and usage information to [MariaDB.org](https://mariadb.org/) or to any other configured URL.


See the [MariaDB User Feedback](https://mariadb.org/feedback_plugin/) page on MariaDB.org to see collected MariaDB usage statistics.



The `<code>feedback</code>` plugin exists in all MariaDB versions.


MariaDB is usually distributed with this plugin included, but it is not enabled by default.
On Windows, this plugin is part of the server and has a special checkbox in the installer window. Either
way, you need to explicitly install and enable it in order for feedback data to be sent.


## Verifying the Plugin's Status


To verify whether the `<code>feedback</code>` plugin is installed and enabled, execute the
[SHOW PLUGINS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-plugins-soname.md) statement or query the [information_schema.plugins](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md) table.


Usually, the plugin is installed in MariaDB by default:


```
SELECT plugin_status FROM information_schema.plugins 
  WHERE plugin_name = 'feedback';
+---------------+
| plugin_status |
+---------------+
| DISABLED      |
+---------------+
```

See [Enabling the Plugin](feedback-plugin.md#enabling-the-plugin).


If that `<code>SELECT</code>` returns no rows, then you still need to [install the plugin](#installing-the-plugin).


When the plugin is installed and enabled, you will see:


```
SELECT plugin_status FROM information_schema.plugins 
  WHERE plugin_name = 'feedback';
+---------------+
| plugin_status |
+---------------+
| ACTIVE        |
+---------------+
```

## Installing the Plugin


In some releases, the plugin's shared library is distributed with MariaDB by default, but the plugin is not actually installed by MariaDB. There are two methods that can be used to install the plugin with MariaDB.


The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md). For example:


```
INSTALL SONAME 'feedback';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the `<code>[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or the `<code>[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` options. This can be specified as a command-line argument to `<code>[mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
plugin_load_add = feedback
```

## Uninstalling the Plugin


You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md). For example:


```
UNINSTALL SONAME 'feedback';
```

If you installed the plugin by providing the `<code>[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or the `<code>[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` options in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.


## Enabling the Plugin


You can enable the plugin by setting the `<code>[feedback](#feedback)</code>` option to `<code>ON</code>` in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
feedback=ON
```

In Windows, the plugin can also be enabled during a new [MSI](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows.md) installation. The MSI GUI installation provides the "Enable feedback plugin" checkbox to enable the plugin. The MSI command-line installation provides the FEEDBACK=1 command-line option to enable the plugin.


See the next section for how to verify the plugin is installed and active and (if needed) install the plugin.


## Collecting Data


The `<code>feedback</code>` plugin will collect:


* Certain rows from [SHOW STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-status.md) and [SHOW VARIABLES](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-variables.md).
* All installed [plugins](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/general-development-information/development-plans/old-plans/plugins-storage-engines-summit-for-mysqlmariadbdrizzle-2011.md) and their versions.
* System information such as CPU count, memory, architecture, and OS/linux distribution.
* The [feedback_server_uid](#feedback_server_uid), which is a SHA1 hash of the MAC address of the first network interface and the TCP port that the server listens on.


The `<code>feedback</code>` plugin creates the [FEEDBACK](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-feedback-table.md) table in the [INFORMATION_SCHEMA](../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) database. To see the data that has been collected by the plugin, you can execute:


```
SELECT * FROM information_schema.feedback;
```

Only the contents of this table are sent to the [feedback_url](#feedback_url).


MariaDB stores collation usage statistics. Each collation that has been used by the server
will have a record in "SELECT * FROM information_schema.feedback" output, for example:


```
+----------------------------------------+---------------------+
| VARIABLE_NAME                          | VARIABLE_VALUE      |
+----------------------------------------+---------------------+
| Collation used utf8_unicode_ci         | 10                  |
| Collation used latin1_general_ci       | 20                  |
+----------------------------------------+---------------------+
```

Collations that have not been used will not be included into the result.


## Sending Data


The `<code>feedback</code>` plugin sends the data using a `<code>POST</code>` request to any URL or a list of URLs
that you specify by setting the [feedback_url](#feedback_url) system variable. By default, this is set to the following URL:


* [post](https://mariadb.org/feedback_plugin/post)


Both HTTP and HTTPS protocols are supported.


If HTTP traffic requires a proxy in your environment, then you can specify the proxy by setting the [feedback_http_proxy](#feedback_http_proxy) system variable.


If the [feedback_url](#feedback_url) system variable is not set to an empty string, then the
plugin will automatically send a report to all URLs in the list a few minutes after the server starts up and then once a week after that.


If the [feedback_url](#feedback_url) system variable is set to an empty string, then the
plugin will **not** automatically send any data. This may be necessary if outbound HTTP communication from your database server is not permitted. In this case, you can still upload the data manually, if you'd like.


First, generate the report file with the MariaDB command-line [mariadb](../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) client:


```
$ mariadb -e 'select * from information_schema.feedback' > report.txt
```

Then you can upload the generated `<code>report.txt</code>` [here](https://mariadb.org/feedback_plugin/post) using your web browser.


Or you can do it from the command line with tools such as [curl](https://curl.haxx.se/docs/manpage.html). For example:


```
$ curl -F data=@report.txt https://mariadb.org/feedback_plugin/post
```

Manual uploading allows you to be absolutely sure that we receive only the data shown in the [INFORMATION_SCHEMA.FEEDBACK](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-feedback-table.md) table and that no private or sensitive information is being sent.


## Versions



| Version | Status | Introduced |
| --- | --- | --- |
| Version | Status | Introduced |
| 1.1 | Stable | [MariaDB 10.0.10](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10010-release-notes.md) |
| 1.1 | Beta | [MariaDB 5.5.20](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5520-release-notes.md), [MariaDB 5.3.3](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/mariadb-533-release-notes.md) |



## System Variables


### `<code>feedback_http_proxy</code>`


* Description: Proxy server for use when http calls cannot be made, such as in a firewall environment. The format is `<code>host:port</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--feedback-http=proxy=value</code>`
* Read-only: Yes
* Data Type: string
* Default Value: `<code>''</code>` (empty)



### `<code>feedback_send_retry_wait</code>`


* Description: Time in seconds before retrying if the plugin failed to send the data for any reason.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--feedback-send-retry-wait=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>60</code>`
* Valid Values: `<code>1</code>` to `<code>86400</code>`



### `<code>feedback_send_timeout</code>`


* Description: An attempt to send the data times out and fails after this many seconds.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--feedback-send-timeout=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>60</code>`
* Valid Values: `<code>1</code>` to `<code>86400</code>`



### `<code>feedback_server_uid</code>`


* Description: Automatically calculated server unique id hash.
* Scope: Global
* Dynamic: No
* Data Type: string



### `<code>feedback_url</code>`


* Description: URL to which the data is sent. More than one URL, separated by spaces, can be specified. Set it to an empty string to disable data sending.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--feedback-url=url</code>`
* Scope: Global
* Dynamic: No
* Data Type: string
* Default Value: `<code>[post](https://mariadb.org/feedback_plugin/post)</code>`



### `<code>feedback_user_info</code>`


* Description: The value of this option is not used by the plugin, but it is included in the feedback data. It can be used to add any user-specified string to the report. This could be used to help to identify it. For example, a support contract number, or a computer name (if you collect reports internally by specifying your own `<code>feedback-url</code>`).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--feedback-user-info=string</code>`
* Scope: Global
* Dynamic: No
* Data Type: string
* Default Value: Empty string



## Options


### `<code>feedback</code>`


* Description: Controls how the server should treat the plugin when the server starts up.

  * Valid values are:

    * `<code>OFF</code>` - Disables the plugin without removing it from the [mysql.plugins](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `<code>ON</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `<code>FORCE</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `<code>FORCE_PLUS_PERMANENT</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--feedback=value</code>`
* Data Type: `<code>enumerated</code>`
* Default Value: `<code>ON</code>`
* Valid Values: `<code>OFF</code>`, `<code>ON</code>`, `<code>FORCE</code>`, `<code>FORCE_PLUS_PERMANENT</code>`


