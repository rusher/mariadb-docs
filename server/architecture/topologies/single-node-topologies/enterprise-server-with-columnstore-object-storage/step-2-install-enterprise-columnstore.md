# Step 2: Install Enterprise ColumnStore

## Overview

This page details step 2 of a 5-step procedure for deploying [Single-Node Enterprise ColumnStore with Object storage](./).

This step installs MariaDB Enterprise Server and MariaDB Enterprise ColumnStore 23.10.

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Retrieve Download Token

MariaDB Corporation provides package repositories for CentOS / RHEL (YUM) and Debian / Ubuntu (APT). A download token is required to access the MariaDB Enterprise Repository.

Customer Download Tokens are customer-specific and are available through the MariaDB Customer Portal.

To retrieve the token for your account:

1. Navigate to [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/)
2. Log in.
3. Copy the Customer Download Token.

Substitute your token for `CUSTOMER_DOWNLOAD_TOKEN` when configuring the package repositories.

## Set Up Repository

1. On each Enterprise ColumnStore node, install the prerequisites for downloading the software from the Web.\
   Install on CentOS / RHEL (YUM):

```bash
$ sudo yum install curl
```

Install on Debian / Ubuntu (APT):

```bash
$ sudo apt install curl apt-transport-https
```

2. On each Enterprise ColumnStore node, configure package repositories and specify Enterprise Server:

```bash
$ curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
```

```bash
$ echo "99ea6c55dbf32bfc42cdcd05c892aebc5e51b06f4c72ec209031639d6e7db9fe  mariadb_es_repo_setup" \
      
 | sha256sum -c -
```

```bash
$ chmod +x mariadb_es_repo_setup
```

```bash
$ sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
      --skip-maxscale \
      --skip-tools \
      --mariadb-server-version="11.4"
```

## Install Enterprise ColumnStore

Install additional dependencies:

Install on CentOS / RHEL (YUM)

```bash
$ sudo yum install epel-release

$ sudo yum install jemalloc
```

Install of Debian 10 and Ubuntu 20.04 (APT):

```bash
$ sudo apt install libjemalloc2
```

Install on Debian 9 and Ubuntu 18.04 (APT):

```bash
$ sudo apt install libjemalloc1
```

Install MariaDB Enterprise Server and MariaDB Enterprise ColumnStore:

Install on CentOS / RHEL (YUM):

```bash
$ sudo yum install MariaDB-server \
   MariaDB-backup \
   MariaDB-shared \
   MariaDB-client \
   MariaDB-columnstore-engine
```

Install on Debian / Ubuntu (APT):

```bash
$ sudo apt install mariadb-server \
   mariadb-backup \
   libmariadb3 \
   mariadb-client \
   mariadb-plugin-columnstore
```

## Next Step

Navigation in the Single-Node Enterprise ColumnStore topology with Object storage deployment procedure:

This page was step 2 of 5.

Next: Step 3: Start and Configure MariaDB Enterprise ColumnStore.

Copyright © 2025 MariaDB
