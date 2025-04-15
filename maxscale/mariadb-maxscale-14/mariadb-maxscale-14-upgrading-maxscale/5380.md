
# Upgrading MaxScale from 1.0 to 1.1

# Upgrading MaxScale from 1.0 to 1.1


This document describes upgrading MaxScale from version 1.0.5 to 1.1.0 and the major differences in the new version compared to the old version. The major changes can be found in the `<code>Changelog.txt</code>` file in the installation directory and the official release notes in the `<code>ReleaseNotes.txt</code>` file.


## Installation


If you are installing MaxScale from a RPM package, we recommend you back up your configuration and log files and that you remove the old installation of MaxScale completely. If you choose to upgrade MaxScale instead of removing it and re-installing it afterwards, the init scripts in `<code>/etc/init.d</code>` folder will be missing. This is due to the RPM packaging system but the script can be re-installed by running the `<code>postinst</code>` script found in the `<code>/usr/local/mariadb-maxscale</code>` folder.



```
# Re-install init scripts
cd /usr/local/mariadb-maxscale
./postinst
```



The 1.1.0 version of MaxScale installs into `<code>/usr/local/mariadb-maxscale</code>` instead of `<code>/usr/local/skysql/maxscale</code>`. This will cause external references to MaxScale's home directory to stop working so remember to update all paths with the new version.


## MaxAdmin changes


The MaxAdmin client's default password in MaxScale 1.1.0 is `<code>mariadb</code>` instead of `<code>skysql</code>`.
