# MaxScale 24.08 Beta MariaDB MaxScale Installation Guide

### Normal Installation

Download the MaxScale package from the MariaDB Downloads page:

* [#mariadb\_platform-mariadb\_maxscale](https://mariadb.com/downloads/#mariadb_platform-mariadb_maxscale)

Select your operating system and download either the RPM or the DEB package.

* For RHEL/CentOS variants, use `yum` to install the downloaded RPM
* For SLES, use `zypper`
* For Debian/Ubuntu systems, install the package with `dpkg -i` and run `apt-get install`\
  after it to install the dependencies

You can also use[the MariaDB package repository](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/binary-packages/mariadb-package-repository-setup-and-usage)\
to install MaxScale by first configuring the repository and then\
installing the `maxscale` package via your package manager.

### Install MariaDB MaxScale Using a Tarball

MaxScale can also be installed using a tarball.\
That may be required if you are using a Linux distribution for which there\
exist no installation package or if you want to install many different\
MaxScale versions side by side. For instructions on how to do that, please refer to[Install MariaDB MaxScale using a Tarball](mariadb-maxscale-2408-maxscale-2408-beta-installing-mariadb-maxscale-using-a-tarball.md).

### Building MariaDB MaxScale From Source Code

Alternatively you may download the MariaDB MaxScale source and build your own binaries.\
To do this, refer to the separate document[Building MariaDB MaxScale from Source Code](mariadb-maxscale-2408-maxscale-2408-beta-building-mariadb-maxscale-from-source-code.md)

### Assumptions

#### Memory allocation behavior

MaxScale assumes that memory allocations always succeed and in general does\
not check for memory allocation failures. This assumption is compatible with\
the Linux kernel parameter[vm.overcommit\_memory](https://www.kernel.org/doc/Documentation/vm/overcommit-accounting)\
having the value `0`, which is also the default on most systems.

With `vm.overcommit_memory` being `0`, memory _allocations_ made by an\
application never fail, but instead the application may be killed by the\
so-called OOM (out-of-memory) killer if, by the time the application\
actually attempts to _use_ the allocated memory, there is not available\
free memory on the system.

If the value is `2`, then a memory allocation made by an application may\
fail and unless the application is prepared for that possibility, it will\
likely crash with a SIGSEGV. As MaxScale is not prepared to handle memory\
allocation failures, it will crash in this situation.

The current value of `vm.overcommit_memory` can be checked with

```
sysctl vm.overcommit_memory
```

or

```
cat /proc/sys/vm/overcommit_memory
```

### Configuring MariaDB MaxScale

[The MaxScale Tutorial](../mariadb-maxscale-24-08-beta-tutorials/mariadb-maxscale-2408-maxscale-2408-beta-setting-up-mariadb-maxscale.md) covers the first\
steps in configuring your MariaDB MaxScale installation. Follow this tutorial\
to learn how to configure and start using MaxScale.

For a detailed list of all configuration parameters, refer to the[Configuration Guide](mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md) and the module specific documents\
listed in the [Documentation Contents](../mariadb-maxscale-2408-maxscale-2408-beta-contents.md).

### Encrypting Passwords

Read the [Encrypting Passwords](mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)\
section of the configuration guide to set up password encryption for the\
configuration file.

### Administration Of MariaDB MaxScale

There are various administration tasks that may be done with MariaDB MaxScale.\
A command line tools is available, [maxctrl](../mariadb-maxscale-24-08-beta-reference/mariadb-maxscale-2408-maxscale-2408-beta-maxctrl.md), that will\
interact with a running MariaDB MaxScale and allow the status of MariaDB\
MaxScale to be monitored and give some control of the MariaDB MaxScale\
functionality.

[The administration tutorial](../mariadb-maxscale-24-08-beta-tutorials/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-administration-tutorial.md)\
covers the common administration tasks that need to be done with MariaDB MaxScale.

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
