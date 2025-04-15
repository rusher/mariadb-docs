
# mysql.server


The [mysql.server](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-servers-table.md) startup script is in MariaDB distributions on Linux and Unix. It is a wrapper that works as a standard [sysVinit](sysvinit.md) script. However, it can be used independently of [sysVinit](sysvinit.md) as a regular `<code>sh</code>` script. The script starts the `<code>[mariadbd](mariadbd-options.md)</code>` server process by first changing its current working directory to the MariaDB install directory and then starting `<code>[mariadbd-safe](mariadbd-safe.md)</code>`. The script requires the standard [sysVinit](sysvinit.md) arguments, such as `<code>start</code>`, `<code>stop</code>`, `<code>restart</code>`, and `<code>status</code>`. For example:


```
mysql.server start
mysql.server restart
mysql.server stop
mysql.server status
```

It can be used on systems such as Linux, Solaris, and Mac OS X.


The `<code>mysql.server</code>` script starts `<code>[mariadbd](mariadbd-options.md)</code>` by first changing to the MariaDB install directory and then calling [mariadbd-safe](mariadbd-safe.md).


## Using mysql.server


The command to use `<code>mysql.server</code>` and the general syntax is:


```
mysql.server [ start | stop | restart | status ] <options> <mariadbd_options>
```

### Options


If an unknown option is provided to `<code>mariadbd-safe</code>` on the command-line, then it is passed to `<code>mariadbd-safe</code>`.


`<code>mysql.server</code>` supports the following options:



| Option | Description |
| --- | --- |
| Option | Description |
| --basedir=path | The path to the MariaDB installation directory. |
| --datadir=path | The path to the MariaDB data directory. |
| --pid-file=file_name | The path name of the file in which the server should write its process ID. If not provided, the default, host_name.pid is used. |
| --service-startup-timeout=file_name | How long in seconds to wait for confirmation of server startup. If the server does not start within this time, mysql.server exits with an error. The default value is 900. A value of 0 means not to wait at all for startup. Negative values mean to wait forever (no timeout). |
| --use-mysqld_safe | Use [mariadbd-safe](mariadbd-safe.md) to start the server. This is the default. |
| --use-manager | Use Instance Manager to start the server. |
| --user=user_name | The login user name to use for running mariadbd. |



### Option Files


In addition to reading options from the command-line, `<code>mysql.server</code>` can also read options from [option files](../configuring-mariadb-with-option-files.md).


The following options relate to how MariaDB command-line tools handles option files. They must be given as the first argument on the command-line:



| Option | Description |
| --- | --- |
| Option | Description |
| --print-defaults | Print the program argument list and exit. |
| --no-defaults | Don't read default options from any option file. |
| --defaults-file=# | Only read default options from the given file #. |
| --defaults-extra-file=# | Read this file after the global files are read. |



#### Option Groups


`<code>mysql.server</code>` reads options from the following [option groups](../configuring-mariadb-with-option-files.md#option-groups) from [option files](../configuring-mariadb-with-option-files.md):



| Group | Description |
| --- | --- |
| Group | Description |
| [mysql.server] | Options read by mysql.server, which includes both MariaDB Server and MySQL Server. |



`<code>mysql.server</code>` also reads options from the following server [option groups](../configuring-mariadb-with-option-files.md#option-groups) from [option files](../configuring-mariadb-with-option-files.md):



| Group | Description |
| --- | --- |
| Group | Description |
| [mysqld] | Options read by mysqld, which includes both MariaDB Server and MySQL Server. |
| [server] | Options read by MariaDB Server. |
| [mysqld-X.Y] | Options read by a specific version of mysqld, which includes both MariaDB Server and MySQL Server. For example, [mysqld-5.5]. |
| [mariadbd] | Options read by MariaDB Server. |
| [mariadbd-X.Y] | Options read by a specific version of MariaDB Server. |
| [client-server] | Options read by all MariaDB [client programs](/en/clients-utilities/) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. |
| [galera] | Options read by a galera-capable MariaDB Server. Available on systems compiled with Galera support. |



### Customizing mysql.server


If you have installed MariaDB to a non-standard location, then you may need to edit the `<code>mysql.server</code>` script to get it to work right.


If you do not want to edit the `<code>mysql.server</code>` script itself, then `<code>mysql.server</code>` also sources a few other `<code>sh</code>` scripts. These files can be used to set any variables that might be needed to make the script work in your specific environment. The files are:


* /etc/default/mysql
* /etc/sysconfig/mysql
* /etc/conf.d/mysql


## Installed Locations


`<code>mysql.server</code>` can be found in the `<code>support-files</code>` directory under your MariaDB installation directory or in a MariaDB source distribution.


### Installed SysVinit Locations


On systems that use [sysVinit](sysvinit.md), `<code>mysql.server</code>` may also be installed in other locations and with other names.


If you installed MariaDB on Linux using [RPMs](../binary-packages/rpm/README.md), then the `<code>mysql.server</code>` script will be installed into the `<code>/etc/init.d</code>` directory with the name `<code>mysql</code>`. You need not install it manually.


#### Manually Installing with SysVinit


If you install MariaDB from [source](../compiling-mariadb-from-source/compiling-mariadb-from-source-mariadb-source-configuration-options.md) or from a [binary tarball](../binary-packages/installing-mariadb-binary-tarballs.md) that does not install `<code>[mysql.server](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-servers-table.md)</code>`
automatically, and if you are on a system that uses [sysVinit](sysvinit.md), then you can manually install `<code>mysql.server</code>` with [sysVinit](sysvinit.md). This is usually done by copying it to `<code class="highlight fixed" style="white-space:pre-wrap">/etc/init.d/</code>` and then creating specially named symlinks in the appropriate `<code class="highlight fixed" style="white-space:pre-wrap">/etc/rcX.d/</code>` directories (where 'X' is a number between 0 and 6).


In the examples below we will follow the historical convention of renaming the
 `<code class="highlight fixed" style="white-space:pre-wrap">mysql.server</code>` script to '`<code class="highlight fixed" style="white-space:pre-wrap">mysql</code>`' when we copy it to `<code class="highlight fixed" style="white-space:pre-wrap">/etc/init.d/</code>`.


The first step for most Linux distributions is to copy the `<code>mysql.server</code>` script to `<code class="highlight fixed" style="white-space:pre-wrap">/etc/init.d/</code>` and make it executable:


```
cd /path/to/your/mariadb-version/support-files/
cp mysql.server /etc/init.d/mysql
chmod +x /etc/init.d/mysql
```

Now all that is needed is to create the specially-named symlinks. On both RPM and Debian-based Linux distributions there are tools which do this for you. Consult your distribution's documentation if neither of these work for you and follow their instructions for generating the symlinks or creating them manually.


On RPM-based distributions (like Fedora and CentOS), you use `<code class="highlight fixed" style="white-space:pre-wrap">chkconfig</code>`:


```
chkconfig --add mysql
chkconfig --level 345 mysql on
```

On Debian-based distributions you use `<code class="highlight fixed" style="white-space:pre-wrap">update-rc.d</code>`:


```
update-rc.d mysql defaults
```

On FreeBSD, the location for startup scripts is
 `<code class="highlight fixed" style="white-space:pre-wrap">/usr/local/etc/rc.d/</code>` and when you copy the
 `<code class="highlight fixed" style="white-space:pre-wrap">mysql.server</code>` script there you should rename it so that it matches the `<code class="highlight fixed" style="white-space:pre-wrap">*.sh</code>` pattern, like so:


```
cd /path/to/your/mariadb/support-files/
cp mysql.server /usr/local/etc/rc.d/mysql.server.sh
```

As stated above, consult your distribution's documentation for more information on starting services like MariaDB at system startup.


See [mariadbd startup options](https://mariadb.com/kb/en/mariadbd-startup-options) for information on configuration options for `<code>mariadbd</code>`.

