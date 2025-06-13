# MariaDB MaxScale Installation Guide

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
MaxScale versions side by side. For instructions on how to do that, please refer to[Install MariaDB MaxScale using a Tarball](mariadb-maxscale-25-installing-mariadb-maxscale-using-a-tarball.md).

### Building MariaDB MaxScale From Source Code

Alternatively you may download the MariaDB MaxScale source and build your own binaries.\
To do this, refer to the separate document[Building MariaDB MaxScale from Source Code](mariadb-maxscale-25-building-mariadb-maxscale-from-source-code.md)

### Configuring MariaDB MaxScale

[The MaxScale Tutorial](../maxscale-25-tutorials/mariadb-maxscale-25-setting-up-mariadb-maxscale.md) covers the first\
steps in configuring your MariaDB MaxScale installation. Follow this tutorial\
to learn how to configure and start using MaxScale.

For a detailed list of all configuration parameters, refer to the[Configuration Guide](mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md) and the module specific documents\
listed in the [Documentation Contents](../mariadb-maxscale-25-contents.md).

### Encrypting Passwords

Read the [Encrypting Passwords](mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md#encrypting-passwords)\
section of the configuration guide to set up password encryption for the\
configuration file.

### Administration Of MariaDB MaxScale

There are various administration tasks that may be done with MariaDB MaxScale.\
A command line tools is available, [maxctrl](../maxscale-25-reference/mariadb-maxscale-25-maxctrl.md), that will\
interact with a running MariaDB MaxScale and allow the status of MariaDB\
MaxScale to be monitored and give some control of the MariaDB MaxScale\
functionality.

[The administration tutorial](../maxscale-25-tutorials/mariadb-maxscale-25-mariadb-maxscale-administration-tutorial.md)\
covers the common administration tasks that need to be done with MariaDB MaxScale.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
