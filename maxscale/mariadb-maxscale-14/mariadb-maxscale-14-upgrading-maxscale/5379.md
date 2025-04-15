
# Upgrading MaxScale from 1.1 to 1.2

# Upgrading MaxScale from 1.1 to 1.2


This document describes upgrading MaxScale from version 1.1.1 to 1.2 and the major differences in the new version compared to the old version. The major changes can be found in the `<code>Changelog.txt</code>` file in the installation directory and the official release notes in the `<code>ReleaseNotes.txt</code>` file.


## Installation


Before starting the upgrade, we recommend you back up your configuration, log and binary log files in `<code>/usr/local/mariadb-maxscale/</code>`.


Upgrading MaxScale will copy the `<code>MaxScale.cnf</code>` file in `<code>/usr/local/mariadb-maxscale/etc/</code>` to `<code>/etc/</code>` and renamed to `<code>maxscale.cnf</code>`. Binary log files are not automatically copied and should be manually moved from `<code>/usr/local/mariadb-maxscale</code>` to `<code>/var/lib/maxscale/</code>`.


## File location changes


MaxScale 1.2 follows the [FHS-standard](https://www.pathname.com/fhs/) and installs to `<code>/usr/</code>` and `<code>/var/</code>` subfolders. Here are the major changes and file locations.


* Configuration files are located in `<code>/etc/</code>` and use lowercase letters: `<code>/etc/maxscale.cnf</code>`
* Binary files are in `<code>/usr/bin/</code>`
* Libraries and modules are in `<code>/usr/lib64/maxscale/</code>`. If you are using custom modules, please make sure they are in this directory before starting MaxScale.
* Log files are in the `<code>var/log/maxscale/</code>` folder
* MaxScale's PID file is located in `<code>/var/run/maxscale/maxscale.pid</code>`
* Data files and other persistent files are in `<code>/var/lib/maxscale/</code>`


## Running MaxScale without root permissions


MaxScale can run as a non-root user with the 1.2 version. RPM and DEB packages install the `<code>maxscale</code>` user and `<code>maxscale</code>` group which are used by the init scripts and systemd configuration files. If you are installing from a binary tarball, you can run the `<code>postinst</code>` script included in it to manually create these groups.
