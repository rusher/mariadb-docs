
# Why Source RPMs (SRPMs) Aren't Packaged For Some Platforms

MariaDB source RPMs (SRPMs) are not packaged on all platforms for which MariaDB RPMs are packaged.


The reason is that MariaDB's build process relies heavily on `<code>[cmake](https://cmake.org)</code>` for a lot of things. In this specific case, MariaDB's build process relies on [CMake CPack Package Generators](https://gitlab.kitware.com/cmake/community/wikis/doc/cpack/PackageGenerators) to build RPMs. The specific package generator that it uses to build RPMs is called `<code>[CPackRPM](https://cmake.org/cmake/help/v3.10/module/CPackRPM.html)</code>`.


Support for source RPMs in `<code>[CPackRPM](https://cmake.org/cmake/help/v3.10/module/CPackRPM.html)</code>` became usable with MariaDB's build system starting from around [cmake 3.10](https://cmake.org/cmake/help/v3.10/release/3.10.html). This means that we do not produce source RPMs on platforms where the installed `<code>[cmake](https://cmake.org)</code>` version is older than that.


See also [Building MariaDB from a Source RPM](../../compiling-mariadb-from-source/building-mariadb-from-a-source-rpm.md).

