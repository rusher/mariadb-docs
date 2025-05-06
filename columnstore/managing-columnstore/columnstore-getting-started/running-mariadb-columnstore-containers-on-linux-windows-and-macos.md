# Running MariaDB ColumnStore containers on Linux, Windows and MacOS

## Introduction

The ColumnStore container allows for a simple and lightweight setup of a MariaDB ColumnStore single server instance for evaluation purposes. The configuration is designed for simplified developer / evaluation setup rather than production use. It allows to evaluate ColumnStore on a Windows or MacOS system, setting up a Linux system in a container. The image uses a base OS of RockyLinux.

## Windows Linux Subsystem

If you have Windows 10 Creators update installed, then you can install the Ubuntu installation into the Bash console. Please follow the Ubuntu instructions in getting started. If you have recently upgraded and had Bash installed previously, ensure you uninstall and reinstall Bash first to have a clean Ubuntu installation. Note that ColumnStore will be terminated should you terminate the Bash console.

## MariaDB Containers

[MariaDB Containers](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/binary-packages/automated-mariadb-deployment-and-administration/docker-and-mariadb) manages lightweight containers that allows for creation of lightweight and reproducible containers with a dedicated function. On Windows and MacOS systems, Docker Engine transparently runs on a Linux virtual machine.

Since MariaDB ColumnStore relies on a Syslog daemon, the container must start both ColumnStore and rsyslogd and the runit utility is used to achieve this.

A single node image can be found at [MariaDB on Docker Hub](https://hub.docker.com/r/mariadb/columnstore/).

```
docker run -d  --name mcs mariadb/columnstore
docker exec -it mcs bash
```

A ColumnStore cluster can be brought up using a compose file provided in the ColumnStore github repository:

```
git clone https://github.com/mariadb-corporation/mariadb-columnstore-docker.git
cd mariadb-columnstore-docker/columnstore
docker-compose up -d
```

For more information about how to manage containers, see [Installing and Using MariaDB via Docker](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/binary-packages/automated-mariadb-deployment-and-administration/docker-and-mariadb/installing-and-using-mariadb-via-docker).

To test an application that uses ColumnStore, it is desirable to setup several containers that will communicate with each other. To do this, we can use Docker Compose. See [Setting Up a LAMP Stack with Docker Compose](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/binary-packages/automated-mariadb-deployment-and-administration/docker-and-mariadb/setting-up-a-lamp-stack-with-docker-compose) for more information.

CC BY-SA / Gnu FDL
