# GPG

The MariaDB project signs their MariaDB packages for Debian, Ubuntu, Fedora, CentOS, and Red Hat.

## Debian / Ubuntu key

Our repositories for Debian "Sid" and the Ubuntu 16.04 and beyond "Xenial" use the following GPG signing key. As detailed in [MDEV-9781](https://jira.mariadb.org/browse/MDEV-9781), APT 1.2.7 (and later) prefers SHA2 GPG keys and now prints warnings when a repository is signed using a SHA1 key like our previous GPG key. We have created a SHA2 key for use with these.

Information about this key:

* The short Key ID is: `0xC74CD1D8`
* The long Key ID is: `0xF1656F24C74CD1D8`
* The full fingerprint of the key is: `177F 4010 FE56 CA33 3630 0305 F165 6F24 C74C D1D8`
* The key can be added on Debian-based systems using the following command:

```
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
```

* Usage of the `apt-key` command is deprecated in the latest versions of Debian and Ubuntu, and the replacement method is to download the keyring file to the `/etc/apt/trusted.gpg.d/` directory. This can be done with the following:

```
sudo curl -LsSo /etc/apt/trusted.gpg.d/mariadb-keyring-2019.gpg https://supplychain.mariadb.com/mariadb-keyring-2019.gpg
```

## RPM / Source Key 2023+

Beginning in 2023 we migrated the key used to sign our yum/dnf/zypper repositories and to sign our source code and binary tarballs to the same key we use for Debian and Ubuntu. This unifies our GPG signing and enables our repositories to be compatible with FIPS and other regulations that mandate a stronger signing key.

The key can be imported on RPM-based systems using the following command:

```
sudo rpm --import https://supplychain.mariadb.com/MariaDB-Server-GPG-KEY
```

or

```
sudo rpmkeys --import https://supplychain.mariadb.com/MariaDB-Server-GPG-KEY
```

## RPM / Source key pre-2023

The GPG Key ID of the MariaDB signing key we used for yum/dnf/zypper repositories and to sign our source code tarballs until the end of 2022 was `0xCBCB082A1BB943DB`. The short form of the id is `0x1BB943DB` and the full key fingerprint is:

```
1993 69E5 404B D5FC 7D2F E43B CBCB 082A 1BB9 43DB
```

This key was used by the yum/dnf/zypper repositories for RedHat, CentOS, Fedora, openSUSE, and SLES.

If you configure the mariadb.org rpm repositories using the repository configuration tool (see below) then your package manager will prompt you to import the key the first time you install a package from the repository.

You can also import the key directly using the following command:

```
sudo rpmkeys --import https://supplychain.mariadb.com/MariaDB-Server-GPG-KEY
```

## Configuring Repositories

See the [this page](mariadb-package-repository-setup-and-usage.md) for details on using the `mariadb_repo_setup` script to configure repositories that use these keys.

See the [this page](https://downloads.mariadb.org/mariadb/repositories/) for details on configuring MariaDB Foundation repositories that use these keys.

CC BY-SA / Gnu FDL
