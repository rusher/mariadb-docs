# MariaDB MaxScale Installation Guide

### Normal Installation

Download the MaxScale package from the MariaDB Downloads page:

* [maxscale](https://mariadb.com/downloads/mariadb-tx/maxscale)

Select your operating system and download the package. You can also use[the MariaDB package repository](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/binary-packages/mariadb-package-repository-setup-and-usage)\
to install MaxScale.

### Install MariaDB MaxScale Using a Tarball

MaxScale can also be installed using a tarball.\
That may be required if you are using a Linux distribution for which there\
exist no installation package or if you want to install many different\
MaxScale versions side by side. For instructions on how to do that, please refer to[Install MariaDB MaxScale using a Tarball](mariadb-maxscale-22-installing-mariadb-maxscale-using-a-tarball.md).

### Building MariaDB MaxScale From Source Code

Alternatively you may download the MariaDB MaxScale source and build your own binaries.\
To do this, refer to the separate document[Building MariaDB MaxScale from Source Code](../../mariadb-maxscale-mariadb-maxscale-23/maxscale-23-getting-started/mariadb-maxscale-23-building-mariadb-maxscale-from-source-code.md)

### Configuring MariaDB MaxScale

[The MaxScale Tutorial](../maxscale-22-tutorials/mariadb-maxscale-22-setting-up-mariadb-maxscale.md) covers the first\
steps in configuring your MariaDB MaxScale installation. Follow this tutorial\
to learn how to configure and start using MaxScale.

For a detailed list of all configuration parameters, refer to the[Configuration Guide](mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md) and the module specific documents\
listed in the [Documentation Contents](../../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/).

### Encrypting Passwords

Read the [Encrypting Passwords](mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md#encrypting-passwords)\
section of the configuration guide to set up password encryption for the\
configuration file.

### Administration Of MariaDB MaxScale

There are various administration tasks that may be done with MariaDB MaxScale.\
Two command line tools are available, `maxctrl` and `maxadmin`, that will interact with a running\
MariaDB MaxScale and allow the status of MariaDB MaxScale to be monitored and\
give some control of the MariaDB MaxScale functionality.\
There are a separate reference guides for the [maxctrl](../../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/) and [maxadmin](../maxscale-22-reference/mariadb-maxscale-22-maxadmin-admin-interface.md) utilities.

[The administration tutorial](../../mariadb-maxscale-mariadb-maxscale-23/maxscale-tutorials/mariadb-maxscale-23-mariadb-maxscale-administration-tutorial.md)\
covers the common administration tasks that need to be done with MariaDB MaxScale.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
