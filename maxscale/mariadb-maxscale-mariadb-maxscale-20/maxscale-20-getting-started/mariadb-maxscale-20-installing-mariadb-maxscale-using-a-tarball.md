
# Installing MariaDB MaxScale using a tarball

# Installing MariaDB MaxScale using a tarball


MariaDB MaxScale is also made available as a tarball, which is named like `<code>maxscale-x.y.z.OS.tar.gz</code>` where `<code>x.y.z</code>` is the same as the corresponding version and `<code>OS</code>` identifies the operating system, e.g. `<code>maxscale-2.0.1.centos.7.tar.gz</code>`.


In order to use the tarball, the following libraries are required:


* libcurl
* libaio
* OpenSSL


The tarball has been built with the assumption that it will be installed in `<code>/usr/local</code>`. However, it is possible to install it in any directory, but in that case MariaDB MaxScale must be invoked with a flag.


## Installing as root in `<code>/usr/local</code>`


If you have root access to the system you probably want to install MariaDB MaxScale under the user and group `<code>maxscale</code>`.


The required steps are as follows:


```
$ sudo groupadd maxscale
$ sudo useradd -g maxscale maxscale
$ cd /usr/local
$ sudo tar -xzvf maxscale-x.y.z.OS.tar.gz
$ sudo ln -s maxscale-x.y.z.OS maxscale
$ cd maxscale
$ sudo chown -R maxscale var
```


Creating the symbolic link is necessary, since MariaDB MaxScale has been built with with the assumption that the plugin directory is `<code>/usr/local/maxscale/lib/maxscale</code>`.


The symbolic link also makes it easy to switch between different versions of MariaDB MaxScale that have been installed side by side in `<code>/usr/local</code>`; just make the symbolic link point to another installation.


In addition, the first time you install MariaDB MaxScale from a tarball you need to create the following directories:


```
$ sudo mkdir /var/log/maxscale
$ sudo mkdir /var/lib/maxscale
$ sudo mkdir /var/run/maxscale
$ sudo mkdir /var/cache/maxscale
```


and make `<code>maxscale</code>` the owner of them:


```
$ sudo chown maxscale /var/log/maxscale
$ sudo chown maxscale /var/lib/maxscale
$ sudo chown maxscale /var/run/maxscale
$ sudo chown maxscale /var/cache/maxscale
```


The following step is to create the MariaDB MaxScale configuration file `<code>/etc/maxscale.cnf</code>`. The file `<code>etc/maxscale.cnf.template</code>` can be used as a base. Please refer to [Configuration Guide](../../mariadb-maxscale-21-06/README.md) for details.


When the configuration file has been created, MariaDB MaxScale can be started.


```
$ sudo bin/maxscale --user=maxscale -d
```


The `<code>-d</code>` flag causes maxscale *not* to turn itself into a daemon, which is adviseable the first time MariaDB MaxScale is started, as it makes it easier to spot problems.


If you want to place the configuration file somewhere else but in `<code>/etc</code>` you can invoke MariaDB MaxScale with the `<code>--config</code>` flag, for instance, `<code>--config=/usr/local/maxscale/etc/maxscale.cnf</code>`.


Note also that if you want to keep *everything* under `<code>/usr/local/maxscale</code>` you can invoke MariaDB MaxScale using the flag `<code>--basedir</code>`.


```
$ sudo bin/maxscale --user=maxscale --basedir=/usr/local/maxscale -d
```


That will cause MariaDB MaxScale to look for its configuration file in `<code>/usr/local/maxscale/etc</code>` and to store all runtime files under `<code>/usr/local/maxscale/var</code>`.


## Installing in any Directory


Enter a directory where you have the right to create a subdirectory. Then do as follows.


```
$ tar -xzvf maxscale-x.y.z.OS.tar.gz
```


The next step is to create the MaxScale configuration file `<code>maxscale-x.y.z/etc/maxscale.cnf</code>`. The file `<code>maxscale-x.y.z/etc/maxscale.cnf.template</code>` can be used as a base. Please refer to [Configuration Guide](../../mariadb-maxscale-21-06/README.md) for details.


When the configuration file has been created, MariaDB MaxScale can be started.


```
$ cd maxscale-x.y.z.OS
$ bin/maxscale -d --basedir=.
```


With the flag `<code>--basedir</code>`, MariaDB MaxScale is told where the `<code>lib</code>`, `<code>etc</code>` and `<code>var</code>` directories are found. Unless it is specified, MariaDB MaxScale assumes the `<code>lib</code>` directory is found in `<code>/usr/local/maxscale</code>`, and the `<code>var</code>` and `<code>etc</code>` directories in `<code>/</code>`.


It is also possible to specify the directories and the location of the configuration file individually. Invoke MaxScale like


```
$ bin/maxscale --help
```


to find out the appropriate flags.
