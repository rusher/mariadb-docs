
# Building RPM Packages From Source

To generate RPM packages from the build, supply the `<code>-DRPM=xxx</code>` flag to CMake, where the value `<code>xxx</code>` is the name of the distribution you're building for. For example, centos7 or rocky8 or fedora39 or sles15.


What these do are controlled in the following CMake files:


* `<code>cmake/cpack_rpm.cmake</code>`
* `<code>cmake/build_configurations/mysql_release.cmake</code>`
* `<code>cmake/mariadb_connector_c.cmake</code>`


To build the packages you should execute:


```
$ umask 0022
$ cmake --build . --target package
```

## See Also


* [About the MariaDB RPM Files](../binary-packages/rpm/about-the-mariadb-rpm-files.md)
* [Building MariaDB on CentOS](source-building-mariadb-on-centos.md)
* [Installing MariaDB RPM Files](../binary-packages/rpm/README.md)
* [MariaDB RPM Packages](../../../clients-and-utilities/server-client-software/download/mariadb-rpm-packages.md)

