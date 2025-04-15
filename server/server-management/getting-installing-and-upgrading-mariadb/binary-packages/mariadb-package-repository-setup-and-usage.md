
# MariaDB Package Repository Setup and Usage

If you are looking to set up MariaDB Server, it is often easiest to use a
repository. The MariaDB Foundation has a repository configuration tool at
[](https://mariadb.org/download/) and MariaDB Corporation provides a convenient
shell script to configure access to their MariaDB Package Repositories. It is
available at:


* [mariadb_repo_setup](https://r.mariadb.com/downloads/mariadb_repo_setup)


The script by default sets up 3 different repositories in a single repository configuration file. The repositories are


* MariaDB Server Repository
* MariaDB MaxScale Repository
* MariaDB Tools Repository


The script can be executed in the following way:


```
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash
```

For the script to work, the `<code>curl</code>` and `<code>ca-certificates</code>` packages need to be installed on your system. Additionally on Debian and Ubuntu the `<code>apt-transport-https</code>` package needs to be installed. The script will check if these are installed and let you know before it attempts to create the repository configuration on your system.



## Repositories


The script will will set up 3 different repositories in a single repository configuration file.


### MariaDB Repository


The **MariaDB Repository** contains software packages related to MariaDB Server, including the server itself, [clients and utilities](/kb/en/clients-utilities/), [client libraries](../../../clients-and-utilities/server-client-software/client-libraries/README.md), [plugins](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/general-development-information/development-plans/old-plans/plugins-storage-engines-summit-for-mysqlmariadbdrizzle-2011.md), and [Mariabackup](../../backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md).


The binaries in MariaDB Corporation's **MariaDB Repository** are currently identical to the binaries in MariaDB Foundation's MariaDB Repository that is configured with the [MariaDB Repository Configuration Tool](https://mariadb.org/download/?t=repo-config).


By default, the script will configure your system to install from the 11.rolling repository which contains the latest stable version of MariaDB. If you would like to stick to a major long-term release series, then you will need to either manually edit the repository configuration file to point to that specific version or series, or run the MariaDB Package Repository setup script again.


The script can also configure your system to install from the repository of a different version of MariaDB if you use the `<code>[--mariadb-server-version](#-mariadb-server-version)</code>` option.


If you would not like to configure the **MariaDB Repository** on your system, then you can use the `<code>--skip-server</code>` option to prevent the MariaDB Package Repository setup script from configuring it.


### MariaDB MaxScale Repository


The **MariaDB MaxScale Repository** contains software packages related to [MariaDB MaxScale](../../../../maxscale/mariadb-maxscale-14/maxscale-14-tutorials/maxscale-connection-routing-with-mysql-replication.md).


By default, the script will configure your system to install from the repository of the *latest* GA version of MariaDB MaxScale. When a new major GA release occurs, the repository will automatically switch to the new version. If instead you would like to stay on a particular version you will need to manually edit the repository configuration file and change '`<code>latest</code>`' to the version you want (e.g. '`<code>6.1</code>`') or run the MariaDB Package Repository setup script again, specifying the particular version or series you want.


Older versions of the MariaDB Package Repository setup script would configure a specific MariaDB MaxScale series in the repository (i.e. '`<code>2.4</code>`'), so if you used the script in the past to set up your repository and want MariaDB MaxScale to automatically use the latest GA version then change '`<code>2.4</code>`' or '`<code>2.3</code>`' in the repository configuration to '`<code>latest</code>`'. Or download the current version of the script and re-run it to set up the repository again.


The script can configure your system to install from the repository of an older version of MariaDB MaxScale if you use the `<code>[--mariadb-maxscale-version](#-mariadb-maxscale-version)</code>` option. For example, `<code>--mariadb-maxscale-version=2.4</code>` if you want the latest release in the MariaDB MaxScale 2.4.x series.


If you do not want to configure the **MariaDB MaxScale Repository** on your system, then you can use the `<code>--skip-maxscale</code>` option to prevent the MariaDB Package Repository setup script from configuring it.


MariaDB MaxScale is licensed under the [Business Source License 1.1](https://mariadb.com/bsl11/), so it is not entirely free to use for organizations who do not have a subscription with MariaDB Corporation. If you would like more information, see the information at [MariaDB Business Source License (BSL): Frequently Asked Questions](https://mariadb.com/bsl-faq-mariadb/). If you would like to know how much a subscription to use MariaDB MaxScale would cost, see [MariaDB Corporation's subscription pricing](https://mariadb.com/pricing/).


## Supported Distributions


The script supports Linux distributions that are officially supported by MariaDB Corporation's [MariaDB TX subscription](https://mariadb.com/products/mariadb-platform-transactional/). However, a MariaDB TX subscription with MariaDB Corporation is not required to use the MariaDB Package Repository.


The distributions currently supported by the script include:


* Red Hat Enterprise Linux (RHEL) 8, and 9
* Debian 10 (Buster), 11 (Bullseye), 12 (Bookworm)
* Ubuntu 20.04 LTS (Focal), 22.04 LTS (Jammy), and 24.04 LTS (Noble)
* SUSE Linux Enterprise Server (SLES) 12 and 15


To install MariaDB on distributions not supported by the MariaDB Package Repository setup script, please consider using MariaDB Foundation's [MariaDB Repository Configuration Tool](https://mariadb.org/download/?t=repo-config). Some Linux distributions also include MariaDB [in their own repositories](distributions-which-include-mariadb.md).


## Using the MariaDB Package Repository Setup Script


The script can be executed in the following way:


```
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash
```

The script will have to set up package repository configuration files, so it will need to be executed as root.


The script will also install the GPG public keys used to verify the signature of MariaDB software packages. If you want to avoid that, then you can use the `<code>--skip-key-import</code>` option.


If the script tries to create the repository configuration file and one with that name already exists, then the script will rename the existing file with an extension in the format ".old_[0-9]+", which would make the OS's package manager ignore the file. You can safely remove those files after you have confirmed that the updated repository configuration file works..


If you want to see the repository configuration file that would be created without actually doing so, then you can use the `<code>[--write-to-stdout](#-write-to-stdout)</code>` option. This also prevents the need to run the script as root,


If you want to download the script, rather than executing it, then you can do so in the following way:


```
curl -LO https://r.mariadb.com/downloads/mariadb_repo_setup
```

### Options


To provide options to the script, you must tell bash to expect them by executing bash with the options `<code>-s --</code>`, for example:


```
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash -s -- --help
```


| Option | Description |
| --- | --- |
| Option | Description |
| --help | Display a usage message and exit |
| --mariadb-server-version=<version> | Override the default MariaDB Server version. By default, the script will use '11.rolling' |
| --mariadb-maxscale-version=<version> | Override the default MariaDB MaxScale version. By default, the script will use 'latest' |
| --os-type=<type> | Override detection of OS type. Acceptable values include debian, ubuntu, rhel, and sles |
| --os-version=<version> | Override detection of OS version. Acceptable values depend on the OS type you specify |
| --skip-key-import | Skip importing GPG signing keys |
| --skip-maxscale | Skip the 'MaxScale' repository |
| --skip-server | Skip the 'MariaDB Server' repository |
| --skip-tools | Skip the 'Tools' repository |
| --skip-verify | Skip verification of MariaDB Server versions. Use with caution as this can lead to an invalid repository configuration file being created |
| --skip-check-installed | Skip tests for required prerequisites for this script |
| --skip-eol-check | Skip tests for versions being past their EOL date |
| --skip-os-eol-check | Skip tests for operating system versions being past EOL date |
| --write-to-stdout | Write output to stdout instead of to the OS's repository configuration file. This will also skip importing GPG public keys and updating the package cache on platforms where that behavior exists |



#### `<code>--mariadb-server-version</code>`


By default, the script will configure your system to install from the repository of the latest GA version of MariaDB. If a new major GA release occurs and you would like to upgrade to it, then you will need to either manually edit the repository configuration file to point to the new version, or run the MariaDB Package Repository setup script again.


The script can also configure your system to install from the repository of a different version of MariaDB if you use the `<code>--mariadb-server-version</code>` option.


The string `<code>mariadb-</code>` has to be prepended to the version number. For example, to configure your system to install from the repository of [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md), that would be:


```
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash -s -- --mariadb-server-version="mariadb-10.6"
```

The following MariaDB versions are currently supported:


* `<code>mariadb-10.5</code>`
* `<code>mariadb-10.6</code>`
* `<code>mariadb-10.11</code>`
* `<code>mariadb-11.4</code>`
* `<code>mariadb-11.7</code>`
* `<code>mariadb-11.8</code>`
* `<code>mariadb-11.rolling</code>`
* `<code>mariadb-11.rc</code>`


If you want to pin the repository of a specific minor release, such as [MariaDB
10.6.14](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-14-release-notes.md), then you can also specify the minor release. For example,
`<code>mariadb-10.6.14</code>`. This may be helpful if you want to avoid upgrades. However,
avoiding upgrades is not recommended, since minor maintenance releases may
contain important bug fixes and fixes for security vulnerabilities.


#### `<code>--mariadb-maxscale-version</code>`


By default, the script will configure your system to install from the
repository of the latest GA version of MariaDB MaxScale.


If you would like to pin the repository to a specific version of MariaDB
MaxScale then you will need
to either manually edit the repository configuration file to point to the
desired version, or use the `<code>--mariadb-maxscale-version</code>` option.


For example, to configure your system to install from the repository of MariaDB
MaxScale 6.1, that would be:


```
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash -s -- --mariadb-maxscale-version="6.1"
```

The following MariaDB MaxScale versions are currently supported:


* MaxScale 1.4
* MaxScale 2.0
* MaxScale 2.1
* MaxScale 2.2
* MaxScale 2.3
* MaxScale 2.4
* MaxScale 2.5
* MaxScale 6.1
* MaxScale 6.2


The special identifiers `<code>latest</code>` (for the latest GA release) and `<code>beta</code>`
(for the latest beta release) are also supported. By default the
`<code>mariadb_repo_setup</code>` script uses `<code>latest</code>` as the version.


#### `<code>--os-type</code>` and `<code>--os-version</code>`


If you want to run this script on an unsupported OS that you believe to be
package-compatible with an OS that is supported, then you can use the
`<code>--os-type</code>` and `<code>--os-version</code>` options to override the script's OS
detection. If you use either option, then you must use both options.


The supported values for `<code>--os-type</code>` are:


* `<code>rhel</code>`
* `<code>debian</code>`
* `<code>ubuntu</code>`
* `<code>sles</code>`


If you use a non-supported value, then the script will fail, just as it would
fail if you ran the script on an unsupported OS.


The supported values for `<code>--os-version</code>` are entirely dependent on the OS
type.


For Red Hat Enterprise Linux (RHEL) and CentOS, `<code>7</code>` and `<code>8</code>` are valid
options.


For Debian and Ubuntu, the version must be specified as the codename of the
specific release. For example, Debian 9 must be specified as `<code>stretch</code>`, and
Ubuntu 18.04 must be specified as `<code>bionic</code>`.


These options can be useful if your distribution is a fork of another
distribution. As an example, Linux Mint 8.1 is based on and is fully compatible
with Ubuntu 16.04 LTS (Xenial). Therefore, If you are using Linux Mint 8.1,
then you can configure your system to install from the repository of Ubuntu
16.04 LTS (Xenial). If you would like to do that, then you can do so by
specifying `<code>--os-type=ubuntu</code>` and `<code>--os-version=xenial</code>` to the MariaDB
Package Repository setup script.


For example, to manually set the `<code>--os-type</code>` and `<code>--os-version</code>` to RHEL 8
you could do:


```
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash -s -- --os-type=rhel --os-version=8
```

#### `<code>--write-to-stdout</code>`


The `<code>--write-to-stdout</code>` option will prevent the script from modifying
anything on the system. The repository configuration will not be written to the
repository configuration file. Instead, it will be printed to standard output.
That allows the configuration to be reviewed, redirected elsewhere, consumed by
another script, or used in some other way.


The `<code>--write-to-stdout</code>` option automatically enables `<code>--skip-key-import</code>`.


For example:


```
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash -s -- --write-to-stdout
```

### Platform-Specific Behavior


#### Platform-Specific Behavior on RHEL and CentOS


On Red Hat Enterprise Linux (RHEL) and CentOS, the MariaDB Package Repository setup script performs the following tasks:


1. Creates a repository configuration file
 at `<code>/etc/yum.repos.d/mariadb.repo</code>`.


1. Imports the GPG public key used to verify the signature of MariaDB software
 packages with `<code>rpm --import</code>` from `<code>downloads.mariadb.com</code>`.


#### Platform-Specific Behavior on Debian and Ubuntu


On Debian and Ubuntu, the MariaDB Package Repository setup script performs the
following tasks:


1. Creates a repository configuration file
 at `<code>/etc/apt/sources.list.d/mariadb.list</code>`.


1. Creates a package preferences file
 at `<code>/etc/apt/preferences.d/mariadb-enterprise.pref</code>`, which gives packages
 from MariaDB repositories a higher priority than packages from OS and other
 repositories, which can help avoid conflicts. It looks like the following:


```
Package: *
Pin: origin downloads.mariadb.com
Pin-Priority: 1000
```


1. Imports the GPG public key used to verify the signature of MariaDB software
 package with `<code>apt-key</code>` from the `<code>keyserver.ubuntu.com</code>` key server.


1. Updates the package cache with package definitions from the MariaDB Package
 Repository with `<code>apt-get update</code>`.


#### Platform-Specific Behavior on SLES


On SUSE Linux Enterprise Server (SLES), the MariaDB Package Repository setup script performs the following tasks:


1. Creates a repository configuration file at `<code>/etc/zypp/repos.d/mariadb.repo</code>`.


1. Imports the GPG public key used to verify the signature of MariaDB software
 packages with `<code>rpm --import</code>` from `<code>downloads.mariadb.com</code>`.


## Installing Packages with the MariaDB Package Repository


After setting up the MariaDB Package Repository, you can install the software packages in the supported repositories.


### Installing Packages on RHEL and CentOS


To install MariaDB on Red Hat Enterprise Linux (RHEL) and CentOS, see the instructions at [Installing MariaDB Packages with YUM](rpm/yum.md#installing-mariadb-packages-with-yum). For example:


```
sudo yum install MariaDB-server MariaDB-client MariaDB-backup
```

To install MariaDB MaxScale on Red Hat Enterprise Linux (RHEL) and CentOS, see the instructions at [MariaDB MaxScale Installation Guide](../../../../maxscale/mariadb-maxscale-mariadb-maxscale-23/maxscale-23-getting-started/mariadb-maxscale-23-mariadb-maxscale-installation-guide.md). For example:


```
sudo yum install maxscale
```

### Installing Packages on Debian and Ubuntu


To install MariaDB on Debian and Ubuntu, see the instructions at [Installing MariaDB Packages with APT](automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md#installing-mariadb-packages-with-apt). For example:


```
sudo apt-get install mariadb-server mariadb-client mariadb-backup
```

To install MariaDB MaxScale on Debian and Ubuntu, see the instructions at [MariaDB MaxScale Installation Guide](../../../../maxscale/mariadb-maxscale-mariadb-maxscale-23/maxscale-23-getting-started/mariadb-maxscale-23-mariadb-maxscale-installation-guide.md). For example:


```
sudo apt-get install maxscale
```

### Installing Packages on SLES


To install MariaDB on SUSE Linux Enterprise Server (SLES), see the instructions at [Installing MariaDB Packages with ZYpp](rpm/installing-mariadb-with-zypper.md#installing-mariadb-packages-with-zypp). For example:


```
sudo zypper install MariaDB-server MariaDB-client MariaDB-backup
```

To install MariaDB MaxScale on SUSE Linux Enterprise Server (SLES), see the instructions at [MariaDB MaxScale Installation Guide](../../../../maxscale/mariadb-maxscale-mariadb-maxscale-23/maxscale-23-getting-started/mariadb-maxscale-23-mariadb-maxscale-installation-guide.md). For example:


```
sudo zypper install maxscale
```

## Versions



| Version | sha256sum |
| --- | --- |
| Version | sha256sum |
| 2025-02-13 | c4a0f3dade02c51a6a28ca3609a13d7a0f8910cccbb90935a2f218454d3a914a |
| 2024-11-14 | ceaa5bd124c4d10a892c384e201bb6e0910d370ebce235306d2e4b860ed36560 |
| 2024-08-14 | 6083ef1974d11f49d42ae668fb9d513f7dc2c6276ffa47caed488c4b47268593 |
| 2024-05-30 | 26e5bf36846003c4fe455713777a4e4a613da0df3b7f74b6dad1cb901f324a84 |
| 2024-02-16 | 30d2a05509d1c129dd7dd8430507e6a7729a4854ea10c9dcf6be88964f3fdc25 |
| 2023-11-21 | 2d7291993f1b71b5dc84cc1d23a65a5e01e783aa765c2bf5ff4ab62814bb5da1 |
| 2023-08-21 | 935944a2ab2b2a48a47f68711b43ad2d698c97f1c3a7d074b34058060c2ad21b |
| 2023-08-14 | f5ba8677ad888cf1562df647d3ee843c8c1529ed63a896bede79d01b2ecc3c1d |
| 2023-06-09 | 3a562a8861fc6362229314772c33c289d9096bafb0865ba4ea108847b78768d2 |
| 2023-02-16 | ad125f01bada12a1ba2f9986a21c59d2cccbe8d584e7f55079ecbeb7f43a4da4 |
| 2022-11-17 | 367a80b01083c34899958cdd62525104a3de6069161d309039e84048d89ee98b |
| 2022-08-22 | 733cf126b03f73050e242102592658913d10829a5bf056ab77e7f864b3f8de1f |
| 2022-08-15 | f99e1d560bd72a3a23f64eaede8982d5494407cafa8f995de45fb9a7274ebc5c |
| 2022-06-14 | d4e4635eeb79b0e96483bd70703209c63da55a236eadd7397f769ee434d92ca8 |
| 2022-02-08 | b9e90cde27affc2a44f9fc60e302ccfcacf71f4ae02071f30d570e6048c28597 |
| 2022-01-18 | c330d2755e18e48c3bba300a2898b0fc8ad2d3326d50b64e02fe65c67b454599 |


