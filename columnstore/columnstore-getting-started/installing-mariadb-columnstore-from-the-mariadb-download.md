
# Installing MariaDB ColumnStore from the MariaDB Download


# Introduction


MariaDB ColumnStore packages can be downloaded from the [MariaDB Downloads](https://mariadb.com/downloads/#mariadb-platform-mariadb_columnstore)


MariaDB ColumnStore packages:


* MariaDB ColumnStore Platform
* MariaDB ColumnStore API (Bulk Write SDK)
* MariaDB ColumnStore Data-Adapters

  * MaxScale kafka
  * Kafka Avro
  * Kettle bulk exporter plugin
  * Maxscale CDC
* MariaDB ColumnStore Tools
* MariaDB Maxscale
* MariaDB Connectors

  * MariaDB Maxscale CDC Connector
  * MariaDB ODBC Connector
  * MariaDB Java-client Connector jar file


NOTE: Centos 6 and Suse 12 doesn't contain all of the above packages. Some features arent supported for those 2 OSs.


You can install MariaDB ColumnStore packages for Single-Server installs and for Multi-Server installs. For Multi-Server systems, the Downloaded package will need to be installed on all servers in the ColumnStore deployment.


Before install, make sure you go through the preparation guide to complete the system setup before installs the packages


[preparing-for-columnstore-installation-11x.md](preparing-and-installing-mariadb-columnstore-11x/preparing-for-columnstore-installation-11x.md)


NOTE: the Release is shown as x.x.x-x. replace that will the matching version that is downloaded. Example 1.1.3-1.


# Centos 6


## Centos 6 RPM package


Once the package is downloaded, it can be untarred with the following command:


```
tar zxvf mariadb-columnstore-x.x.x-x-centos6.x86_64.rpm.tar.gz
```

This is the contents of the installed package:


* MariaDB-ColumnStore/

  * mariadb-columnstore-1.1.3-1-centos6.x86_64.rpm.tar.gz
* MariaDB-ColumnStore-Tools/

  * mariadb-columnstore-tools-1.1.3-1.rpm
* MariaDB-Connectors/

  * mariadb-connector-[ODBC-3](https://jira.mariadb.org/browse/ODBC-3).0.2-ga-rhel6-i686.tar.gz
  * mariadb-java-client-2.2.2.jar
* MariaDB-MaxScale/

  * maxscale-2.2.2-1.centos.6.x86_64.rpm
  * maxscale-cdc-connector-2.2.2-1.centos.6.x86_64.rpm


## Centos 6 RPM package installation


### MariaDB ColumnStore


Follow the instructions for installing MariaDB Columnstore RPMs


[preparing-for-columnstore-installation-11x.md](preparing-and-installing-mariadb-columnstore-11x/preparing-for-columnstore-installation-11x.md)


### MariaDB ColumnStore Tools


Follow the instructions for installing MariaDB Columnstore Tools


[backup-and-restore-for-mariadb-columnstore-110-onwards.md](../managing-columnstore/managing-columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110-onwards.md)


### MariaDB ColumnStore Connectors


#### ODBC Connector


How to Install the ODBC Connector:


[](https://mariadb.com/kb/en/library/about-mariadb-connector-odbc/)


Additional Information on the ODBC connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/)


#### Java Connector


How to Install the Java Connector:


[installing-mariadb-connectorj](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/installing-mariadb-connectorj)


Additional information on the Java Connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/)


How to Install on the MariaDB MaxScale:


[](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-21-06/)


## Centos 6 Binary Package


Once the package is downloaded, it can be untarred with the following command:


```
tar zxvf mariadb-columnstore-x.x.x-x-centos6.x86_64.bin.tar.gz
```

This is the contents of the installed package:


* MariaDB-ColumnStore/

  * mariadb-columnstore-1.1.3-1-centos6.x86_64.bin.tar.gz
* MariaDB-ColumnStore-Tools/

  * mariadb-columnstore-tools-1.1.3-1.bin.tar.gz
* MariaDB-Connectors/

  * mariadb-connector-[ODBC-3](https://jira.mariadb.org/browse/ODBC-3).0.2-ga-rhel6-i686.tar.gz
  * mariadb-java-client-2.2.2.jar
* MariaDB-MaxScale/

  * maxscale-2.2.2-1.centos.6.tar.gz
  * maxscale-cdc-connector-2.2.2-1.centos.6.x86_64.rpm


## Centos 6 Binary Package installation


### MariaDB ColumnStore


Follow the instructions for installing MariaDB Columnstore binary package


[preparing-for-columnstore-installation-11x.md](preparing-and-installing-mariadb-columnstore-11x/preparing-for-columnstore-installation-11x.md)


### MariaDB ColumnStore Tools


Follow the instructions for installing MariaDB Columnstore Tools


[backup-and-restore-for-mariadb-columnstore-110-onwards.md](../managing-columnstore/managing-columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110-onwards.md)


### MariaDB ColumnStore Connectors


#### ODBC Connector


How to Install the ODBC Connector:


[](https://mariadb.com/kb/en/library/about-mariadb-connector-odbc/)


Additional Information on the ODBC connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/)


#### Java Connector


How to Install the Java Connector:


[installing-mariadb-connectorj](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/installing-mariadb-connectorj)


Additional information on the Java Connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/)


### MariaDB MaxScale


How to Install on the MariaDB MaxScale:


[](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-21-06/)


# Centos 7


## Centos 7 RPM package


Once the package is downloaded, it can be untarred with the following command:


```
tar zxvf mariadb-columnstore-x.x.x-x-centos7.x86_64.rpm.tar.gz
```

This is the contents of the installed package:


* MariaDB-ColumnStore/

  * mariadb-columnstore-1.1.3-1-centos7.x86_64.rpm.tar.gz
* MariaDB-ColumnStore-API/

  * mariadb-columnstore-api-1.1.3-1-x86_64-centos7.rpm
* MariaDB-ColumnStore-Tools/

  * mariadb-columnstore-tools-1.1.3-1.rpm
* MariaDB-Connectors/

  * mariadb-connector-[ODBC-3](https://jira.mariadb.org/browse/ODBC-3).0.2-ga-rhel7-i686.tar.gz
  * mariadb-java-client-2.2.2.jar
* MariaDB-Data-Adapters/

  * mariadb-columnstore-kafka-adapters-1.1.3-1-x86_64-centos7.rpm
  * mariadb-columnstore-maxscale-cdc-adapters-1.1.3-1-x86_64-centos7.rpm
* MariaDB-MaxScale/

  * maxscale-2.2.2-1.centos.7.x86_64.rpm
  * maxscale-cdc-connector-2.2.2-1.centos.7.x86_64.rpm


## Centos 7 RPM package installation


### MariaDB ColumnStore


Follow the instructions for installing MariaDB Columnstore RPMs


[preparing-for-columnstore-installation-11x.md](preparing-and-installing-mariadb-columnstore-11x/preparing-for-columnstore-installation-11x.md)


### MariaDB ColumnStore API (Bulk Write SDK)


Follow the instructions for installing MariaDB Columnstore API RPM


[columnstore-bulk-write-sdk.md](../columnstore-data-ingestion/columnstore-bulk-write-sdk.md)


### MariaDB ColumnStore Tools


Follow the instructions for installing MariaDB Columnstore Tools


[backup-and-restore-for-mariadb-columnstore-110-onwards.md](../managing-columnstore/managing-columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110-onwards.md)


### MariaDB ColumnStore Connectors


#### ODBC Connector


How to Install the ODBC Connector:


[](https://mariadb.com/kb/en/library/about-mariadb-connector-odbc/)


Additional Information on the ODBC connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/)


#### Java Connector


How to Install the Java Connector:


[installing-mariadb-connectorj](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/installing-mariadb-connectorj)


Additional information on the Java Connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/)


### MariaDB ColumnStore Data Adapters


How to Install on the Data Adapters:


[columnstore-streaming-data-adapters.md](../columnstore-data-ingestion/columnstore-streaming-data-adapters.md)


### MariaDB MaxScale


How to Install on the MariaDB MaxScale:


[](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-21-06/)


## Centos 7 Binary Package


Once the package is downloaded, it can be untarred with the following command:


```
tar zxvf mariadb-columnstore-x.x.x-x-centos7.x86_64.bin.tar.gz
```

This is the contents of the installed package:


* MariaDB-ColumnStore/

  * mariadb-columnstore-1.1.3-1-centos7.x86_64.bin.tar.gz
* MariaDB-ColumnStore-API/

  * mariadb-columnstore-api-1.1.3-1-x86_64-centos7.rpm
* MariaDB-ColumnStore-Tools/

  * mariadb-columnstore-tools-1.1.3-1.bin.tar.gz
* MariaDB-Connectors/

  * mariadb-connector-[ODBC-3](https://jira.mariadb.org/browse/ODBC-3).0.2-ga-rhel7-i686.tar.gz
  * mariadb-java-client-2.2.2.jar
* MariaDB-Data-Adapters/

  * mariadb-columnstore-kafka-adapters-1.1.3-1-x86_64-centos7.rpm
  * mariadb-columnstore-maxscale-cdc-adapters-1.1.3-1-x86_64-centos7.rpm
* MariaDB-MaxScale/

  * maxscale-2.2.2-1.centos.7.tar.gz
  * maxscale-cdc-connector-2.2.2-1.centos.7.x86_64.rpm


## Centos 7 Binary Package installation


### MariaDB ColumnStore


Follow the instructions for installing MariaDB Columnstore binary package


[preparing-for-columnstore-installation-11x.md](preparing-and-installing-mariadb-columnstore-11x/preparing-for-columnstore-installation-11x.md)


### MariaDB ColumnStore API (Bulk Write SDK)


Follow the instructions for installing MariaDB Columnstore API RPM


[columnstore-bulk-write-sdk.md](../columnstore-data-ingestion/columnstore-bulk-write-sdk.md)


### MariaDB ColumnStore Tools


Follow the instructions for installing MariaDB Columnstore Tools


[backup-and-restore-for-mariadb-columnstore-110-onwards.md](../managing-columnstore/managing-columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110-onwards.md)


### MariaDB ColumnStore Connectors


#### ODBC Connector


How to Install the ODBC Connector:


[](https://mariadb.com/kb/en/library/about-mariadb-connector-odbc/)


Additional Information on the ODBC connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/)


#### Java Connector


How to Install the Java Connector:


[installing-mariadb-connectorj](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/installing-mariadb-connectorj)


Additional information on the Java Connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/)


### MariaDB ColumnStore Data Adapters


How to Install on the Data Adapters:


[columnstore-streaming-data-adapters.md](../columnstore-data-ingestion/columnstore-streaming-data-adapters.md)


### MariaDB MaxScale


How to Install on the MariaDB MaxScale:


[](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-21-06/)


# Suse 12


## Suse 12 RPM package


Once the package is downloaded, it can be untarred with the following command:


```
tar zxvf mariadb-columnstore-x.x.x-x-sles12.x86_64.rpm.tar.gz
```

This is the contents of the installed package:


* MariaDB-ColumnStore/

  * mariadb-columnstore-1.1.3-1-sles12.x86_64.rpm.tar.gz
* MariaDB-ColumnStore-Tools/

  * mariadb-columnstore-tools-1.1.3-1.rpm
* MariaDB-Connectors/

  * mariadb-java-client-2.2.2.jar
* MariaDB-MaxScale/

  * maxscale-2.2.2-1.sles/12.x86_64.rpm
  * maxscale-cdc-connector-2.2.2-1.sles.12.x86_64.rpm


## Suse 12 RPM package installation


### MariaDB ColumnStore


Follow the instructions for installing MariaDB Columnstore RPMs


[preparing-for-columnstore-installation-11x.md](preparing-and-installing-mariadb-columnstore-11x/preparing-for-columnstore-installation-11x.md)


### MariaDB ColumnStore Tools


Follow the instructions for installing MariaDB Columnstore Tools


[backup-and-restore-for-mariadb-columnstore-110-onwards.md](../managing-columnstore/managing-columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110-onwards.md)


### MariaDB ColumnStore Connectors


#### ODBC Connector


How to Install the ODBC Connector:


[](https://mariadb.com/kb/en/library/about-mariadb-connector-odbc/)


Additional Information on the ODBC connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/)


#### Java Connector


How to Install the Java Connector:


[installing-mariadb-connectorj](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/installing-mariadb-connectorj)


Additional information on the Java Connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/)


How to Install on the MariaDB MaxScale:


[](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-21-06/)


## Suse 12 Binary Package


Once the package is downloaded, it can be untarred with the following command:


```
tar zxvf mariadb-columnstore-x.x.x-x-sles12.x86_64.bin.tar.gz
```

This is the contents of the installed package:


* MariaDB-ColumnStore

  * mariadb-columnstore-1.1.3-1-sles12.x86_64.bin.tar.gz
* MariaDB-ColumnStore-Tools

  * mariadb-columnstore-tools-1.1.3-1.bin.tar.gz
* MariaDB-Connectors/

  * mariadb-java-client-2.2.2.jar
* MariaDB-MaxScale/

  * maxscale-2.2.2-1.sles.12.tar.gz
  * maxscale-cdc-connector-2.2.2-1.sles.12.x86_64.rpm


## Suse 12 Binary Package installation


### MariaDB ColumnStore


Follow the instructions for installing MariaDB Columnstore binary package


[preparing-for-columnstore-installation-11x.md](preparing-and-installing-mariadb-columnstore-11x/preparing-for-columnstore-installation-11x.md)


### MariaDB ColumnStore Tools


Follow the instructions for installing MariaDB Columnstore Tools


[backup-and-restore-for-mariadb-columnstore-110-onwards.md](../managing-columnstore/managing-columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110-onwards.md)


### MariaDB ColumnStore Connectors


#### ODBC Connector


How to Install the ODBC Connector:


[](https://mariadb.com/kb/en/library/about-mariadb-connector-odbc/)


Additional Information on the ODBC connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/)


#### Java Connector


How to Install the Java Connector:


[installing-mariadb-connectorj](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/installing-mariadb-connectorj)


Additional information on the Java Connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/)


### MariaDB MaxScale


How to Install on the MariaDB MaxScale:


[](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-21-06/)


# Debian 8 (jessie)


## Debian 8 DEB package


Once the package is downloaded, it can be untarred with the following command:


```
tar zxvf mariadb-columnstore-1.1.3-1-jessie.amd64.deb.tar.gz
```

This is the contents of the installed package:


* MariaDB-ColumnStore

  * mariadb-columnstore-1.1.3-1-jessie.amd64.rpm.tar.gz
* MariaDB-ColumnStore-API/

  * mariadb-columnstore-api-1.1.3-1-x86_64.jessie.deb
* MariaDB-ColumnStore-Tools

  * mariadb-columnstore-tools-1.1.3-1.amd64.deb
* MariaDB-Connectors/

  * mariadb-connector-[ODBC-3](https://jira.mariadb.org/browse/ODBC-3).0.2-ga-debian-i686.tar.gz
  * mariadb-java-client-2.2.2.jar
* MariaDB-Data-Adapters/

  * mariadb-columnstore-kafka-adapters-1.1.3-1-x86_64-jessie.deb
  * mariadb-columnstore-maxscale-cdc-adapters-1.1.3-1-x86_64-jessie.deb
* MariaDB-MaxScale/

  * maxscale-2.2.2-1.debian.jessie.x86_64.deb
  * maxscale-cdc-connector-2.2.2-1.debian.jessie.x86_64.deb


## Debian 8 DEB package installation


### MariaDB ColumnStore


Follow the instructions for installing MariaDB Columnstore DEBs


[preparing-for-columnstore-installation-11x.md](preparing-and-installing-mariadb-columnstore-11x/preparing-for-columnstore-installation-11x.md)


### MariaDB ColumnStore API (Bulk Write SDK)


Follow the instructions for installing MariaDB Columnstore API DEB


[columnstore-bulk-write-sdk.md](../columnstore-data-ingestion/columnstore-bulk-write-sdk.md)


### MariaDB ColumnStore Tools


Follow the instructions for installing MariaDB Columnstore Tools


[backup-and-restore-for-mariadb-columnstore-110-onwards.md](../managing-columnstore/managing-columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110-onwards.md)


### MariaDB ColumnStore Connectors


#### ODBC Connector


How to Install the ODBC Connector:


[](https://mariadb.com/kb/en/library/about-mariadb-connector-odbc/)


Additional Information on the ODBC connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/)


#### Java Connector


How to Install the Java Connector:


[installing-mariadb-connectorj](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/installing-mariadb-connectorj)


Additional information on the Java Connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/)


### MariaDB ColumnStore Data Adapters


How to Install on the Data Adapters:


[columnstore-streaming-data-adapters.md](../columnstore-data-ingestion/columnstore-streaming-data-adapters.md)


### MariaDB MaxScale


How to Install on the MariaDB MaxScale:


[](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-21-06/)


## Debian 8 Binary Package


Once the package is downloaded, it can be untarred with the following command:


```
tar zxvf mariadb-columnstore-x.x.x-x-jessie.x86_64.bin.tar.gz
```

This is the contents of the installed package:


* MariaDB-ColumnStore

  * mariadb-columnstore-1.1.3-1-jessie.amd64.bin.tar.gz
* MariaDB-ColumnStore-API/

  * mariadb-columnstore-api-1.1.3-1-x86_64-jessie.deb
* MariaDB-ColumnStore-Tools

  * mariadb-columnstore-tools-1.1.3-1.tar.gz
* MariaDB-Connectors/

  * mariadb-connector-[ODBC-3](https://jira.mariadb.org/browse/ODBC-3).0.2-ga-debian-i686.tar.gz
  * mariadb-java-client-2.2.2.jar
* MariaDB-Data-Adapters/

  * mariadb-columnstore-kafka-adapters-1.1.3-1-x86_64-jessie.deb
  * mariadb-columnstore-maxscale-cdc-adapters-1.1.3-1-x86_64-jessie.deb
* MariaDB-MaxScale/

  * maxscale-2.2.2-1.debian.jessie.tar.gz
  * maxscale-cdc-connector-2.2.2-1.debian.jessie.x86_64.deb


## Debian 8 Binary Package installation


### MariaDB ColumnStore


Follow the instructions for installing MariaDB Columnstore binary package


[preparing-for-columnstore-installation-11x.md](preparing-and-installing-mariadb-columnstore-11x/preparing-for-columnstore-installation-11x.md)


### MariaDB ColumnStore API (Bulk Write SDK)


Follow the instructions for installing MariaDB Columnstore API RPM


[columnstore-bulk-write-sdk.md](../columnstore-data-ingestion/columnstore-bulk-write-sdk.md)


### MariaDB ColumnStore Tools


Follow the instructions for installing MariaDB Columnstore Tools


[backup-and-restore-for-mariadb-columnstore-110-onwards.md](../managing-columnstore/managing-columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110-onwards.md)


### MariaDB ColumnStore Connectors


#### ODBC Connector


How to Install the ODBC Connector:


[](https://mariadb.com/kb/en/library/about-mariadb-connector-odbc/)


Additional Information on the ODBC connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/)


#### Java Connector


How to Install the Java Connector:


[installing-mariadb-connectorj](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/installing-mariadb-connectorj)


Additional information on the Java Connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/)


### MariaDB ColumnStore Data Adapters


How to Install on the Data Adapters:


[columnstore-streaming-data-adapters.md](../columnstore-data-ingestion/columnstore-streaming-data-adapters.md)


### MariaDB MaxScale


How to Install on the MariaDB MaxScale:


[](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-21-06/)


# Debian 9 (stretch)


## Debian 9 DEB package


Once the package is downloaded, it can be untarred with the following command:


```
tar zxvf mariadb-columnstore-1.1.3-1-stretch.amd64.deb.tar.gz
```

This is the contents of the installed package:


* MariaDB-ColumnStore

  * mariadb-columnstore-1.1.3-1-stretch.amd64.rpm.tar.gz
* MariaDB-ColumnStore-API/

  * mariadb-columnstore-api-1.1.3-1-x86_64.stretch.deb
* MariaDB-ColumnStore-Tools

  * mariadb-columnstore-tools-1.1.3-1.amd64.deb
* MariaDB-Connectors/

  * mariadb-connector-[ODBC-3](https://jira.mariadb.org/browse/ODBC-3).0.2-ga-debian-i686.tar.gz
  * mariadb-java-client-2.2.2.jar
* MariaDB-Data-Adapters/

  * mariadb-columnstore-kafka-adapters-1.1.3-1-x86_64-stretch.deb
  * mariadb-columnstore-maxscale-cdc-adapters-1.1.3-1-x86_64-stretch.deb
* MariaDB-MaxScale/

  * maxscale-2.2.2-1.debian.stretch.x86_64.deb
  * maxscale-cdc-connector-2.2.2-1.debian.stretch.x86_64.deb


## Debian 9 DEB package installation


### MariaDB ColumnStore


Follow the instructions for installing MariaDB Columnstore DEBs


[preparing-for-columnstore-installation-11x.md](preparing-and-installing-mariadb-columnstore-11x/preparing-for-columnstore-installation-11x.md)


### MariaDB ColumnStore API (Bulk Write SDK)


Follow the instructions for installing MariaDB Columnstore API DEB


[columnstore-bulk-write-sdk.md](../columnstore-data-ingestion/columnstore-bulk-write-sdk.md)


### MariaDB ColumnStore Tools


Follow the instructions for installing MariaDB Columnstore Tools


[backup-and-restore-for-mariadb-columnstore-110-onwards.md](../managing-columnstore/managing-columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110-onwards.md)


### MariaDB ColumnStore Connectors


#### ODBC Connector


How to Install the ODBC Connector:


[](https://mariadb.com/kb/en/library/about-mariadb-connector-odbc/)


Additional Information on the ODBC connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/)


#### Java Connector


How to Install the Java Connector:


[installing-mariadb-connectorj](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/installing-mariadb-connectorj)


Additional information on the Java Connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/)


### MariaDB ColumnStore Data Adapters


How to Install on the Data Adapters:


[columnstore-streaming-data-adapters.md](../columnstore-data-ingestion/columnstore-streaming-data-adapters.md)


### MariaDB MaxScale


How to Install on the MariaDB MaxScale:


[](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-21-06/)


## Debian 9 Binary Package


Once the package is downloaded, it can be untarred with the following command:


```
tar zxvf mariadb-columnstore-x.x.x-x-stretch.x86_64.bin.tar.gz
```

This is the contents of the installed package:


* MariaDB-ColumnStore

  * mariadb-columnstore-1.1.3-1-stretch.amd64.bin.tar.gz
* MariaDB-ColumnStore-API/

  * mariadb-columnstore-api-1.1.3-1-x86_64-stretch.deb
* MariaDB-ColumnStore-Tools

  * mariadb-columnstore-tools-1.1.3-1.tar.gz
* MariaDB-Connectors/

  * mariadb-connector-[ODBC-3](https://jira.mariadb.org/browse/ODBC-3).0.2-ga-debian-i686.tar.gz
  * mariadb-java-client-2.2.2.jar
* MariaDB-Data-Adapters/

  * mariadb-columnstore-kafka-adapters-1.1.3-1-x86_64-stretch.deb
  * mariadb-columnstore-maxscale-cdc-adapters-1.1.3-1-x86_64-stretch.deb
* MariaDB-MaxScale/

  * maxscale-2.2.2-1.debian.stretch.tar.gz
  * maxscale-cdc-connector-2.2.2-1.debian.stretch.x86_64.deb


## Debian 9 Binary Package installation


### MariaDB ColumnStore


Follow the instructions for installing MariaDB Columnstore binary package


[preparing-for-columnstore-installation-11x.md](preparing-and-installing-mariadb-columnstore-11x/preparing-for-columnstore-installation-11x.md)


### MariaDB ColumnStore API (Bulk Write SDK)


Follow the instructions for installing MariaDB Columnstore API RPM


[columnstore-bulk-write-sdk.md](../columnstore-data-ingestion/columnstore-bulk-write-sdk.md)


### MariaDB ColumnStore Tools


Follow the instructions for installing MariaDB Columnstore Tools


[backup-and-restore-for-mariadb-columnstore-110-onwards.md](../managing-columnstore/managing-columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110-onwards.md)


### MariaDB ColumnStore Connectors


#### ODBC Connector


How to Install the ODBC Connector:


[](https://mariadb.com/kb/en/library/about-mariadb-connector-odbc/)


Additional Information on the ODBC connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/)


#### Java Connector


How to Install the Java Connector:


[installing-mariadb-connectorj](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/installing-mariadb-connectorj)


Additional information on the Java Connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/)


### MariaDB ColumnStore Data Adapters


How to Install on the Data Adapters:


[columnstore-streaming-data-adapters.md](../columnstore-data-ingestion/columnstore-streaming-data-adapters.md)


### MariaDB MaxScale


How to Install on the MariaDB MaxScale:


[](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-21-06/)


# Ubuntu 16 (xenial)


## Ubuntu 16 DEB package


Once the package is downloaded, it can be untarred with the following command:


```
tar zxvf mariadb-columnstore-1.1.3-1-xenial.amd64.deb.tar.gz
```

This is the contents of the installed package:


* MariaDB-ColumnStore

  * mariadb-columnstore-1.1.3-1-xenial.amd64.rpm.tar.gz
* MariaDB-ColumnStore-API/

  * mariadb-columnstore-api-1.1.3-1-x86_64.xenial.deb
* MariaDB-ColumnStore-Tools

  * mariadb-columnstore-tools-1.1.3-1.amd64.deb
* MariaDB-Connectors/

  * mariadb-connector-[ODBC-3](https://jira.mariadb.org/browse/ODBC-3).0.2-ga-debian-i686.tar.gz
  * mariadb-java-client-2.2.2.jar
* MariaDB-Data-Adapters/

  * mariadb-columnstore-kafka-adapters-1.1.3-1-x86_64-xenial.deb
  * mariadb-columnstore-maxscale-cdc-adapters-1.1.3-1-x86_64-xenial.deb
* MariaDB-MaxScale/

  * maxscale-2.2.2-1.debian.xenial.x86_64.deb
  * maxscale-cdc-connector-2.2.2-1.debian.xenial.x86_64.deb


## Ubuntu 16 DEB package installation


### MariaDB ColumnStore


Follow the instructions for installing MariaDB Columnstore DEBs


[preparing-for-columnstore-installation-11x.md](preparing-and-installing-mariadb-columnstore-11x/preparing-for-columnstore-installation-11x.md)


### MariaDB ColumnStore API (Bulk Write SDK)


Follow the instructions for installing MariaDB Columnstore API DEB


[columnstore-bulk-write-sdk.md](../columnstore-data-ingestion/columnstore-bulk-write-sdk.md)


### MariaDB ColumnStore Tools


Follow the instructions for installing MariaDB Columnstore Tools


[backup-and-restore-for-mariadb-columnstore-110-onwards.md](../managing-columnstore/managing-columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110-onwards.md)


### MariaDB ColumnStore Connectors


#### ODBC Connector


How to Install the ODBC Connector:


[](https://mariadb.com/kb/en/library/about-mariadb-connector-odbc/)


Additional Information on the ODBC connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/)


#### Java Connector


How to Install the Java Connector:


[installing-mariadb-connectorj](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/installing-mariadb-connectorj)


Additional information on the Java Connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/)


### MariaDB ColumnStore Data Adapters


How to Install on the Data Adapters:


[columnstore-streaming-data-adapters.md](../columnstore-data-ingestion/columnstore-streaming-data-adapters.md)


### MariaDB MaxScale


How to Install on the MariaDB MaxScale:


[](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-21-06/)


## Ubuntu 16 Binary Package


Once the package is downloaded, it can be untarred with the following command:


```
tar zxvf mariadb-columnstore-x.x.x-x-xenial.adm64.bin.tar.gz
```

This is the contents of the installed package:


* MariaDB-ColumnStore

  * mariadb-columnstore-1.1.3-1-xenial.amd64.bin.tar.gz
* MariaDB-ColumnStore-API/

  * mariadb-columnstore-api-1.1.3-1-x86_64-xenial.deb
* MariaDB-ColumnStore-Tools

  * mariadb-columnstore-tools-1.1.3-1.tar.gz
* MariaDB-Connectors

  * mariadb-connector-[ODBC-3](https://jira.mariadb.org/browse/ODBC-3).0.2-ga-debian-i686.tar.gz
  * mariadb-java-client-2.2.2.jar
* MariaDB-Data-Adapters

  * mariadb-columnstore-kafka-adapters-1.1.3-1-x86_64-xenial.deb
  * mariadb-columnstore-maxscale-cdc-adapters-1.1.3-1-x86_64-xenial.deb
* MariaDB-MaxScale

  * maxscale-2.2.2-1.debian.xenial.tar.gz
  * maxscale-cdc-connector-2.2.2-1.debian.xenial.x86_64.deb


## Ubuntu 16 Binary Package installation


### MariaDB ColumnStore


Follow the instructions for installing MariaDB Columnstore binary package


[preparing-for-columnstore-installation-11x.md](preparing-and-installing-mariadb-columnstore-11x/preparing-for-columnstore-installation-11x.md)


### MariaDB ColumnStore API (Bulk Write SDK)


Follow the instructions for installing MariaDB Columnstore API RPM


[columnstore-bulk-write-sdk.md](../columnstore-data-ingestion/columnstore-bulk-write-sdk.md)


### MariaDB ColumnStore Tools


Follow the instructions for installing MariaDB Columnstore Tools


[backup-and-restore-for-mariadb-columnstore-110-onwards.md](../managing-columnstore/managing-columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110-onwards.md)


### MariaDB ColumnStore Connectors


#### ODBC Connector


How to Install the ODBC Connector:


[](https://mariadb.com/kb/en/library/about-mariadb-connector-odbc/)


Additional Information on the ODBC connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/)


#### Java Connector


How to Install the Java Connector:


[installing-mariadb-connectorj](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/installing-mariadb-connectorj)


Additional information on the Java Connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/)


### MariaDB ColumnStore Data Adapters


How to Install on the Data Adapters:


[columnstore-streaming-data-adapters.md](../columnstore-data-ingestion/columnstore-streaming-data-adapters.md)


### MariaDB MaxScale


How to Install on the MariaDB MaxScale:


[](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-21-06/)


# Ubuntu 18 (bionic)


## Ubuntu 18 DEB package


Once the package is downloaded, it can be untarred with the following command:


```
tar zxvf mariadb-columnstore-1.1.3-1-bionic.amd64.deb.tar.gz
```

This is the contents of the installed package:


* MariaDB-ColumnStore

  * mariadb-columnstore-1.1.3-1-bionic.amd64.rpm.tar.gz
* MariaDB-ColumnStore-API

  * mariadb-columnstore-api-1.1.3-1-x86_64.bionic.deb
* MariaDB-ColumnStore-Tools

  * mariadb-columnstore-tools-1.1.3-1.amd64.deb
* MariaDB-Connectors

  * mariadb-connector-[ODBC-3](https://jira.mariadb.org/browse/ODBC-3).0.2-ga-debian-i686.tar.gz
  * mariadb-java-client-2.2.2.jar
* MariaDB-Data-Adapters

  * mariadb-columnstore-kafka-adapters-1.1.3-1-x86_64-bionic.deb
  * mariadb-columnstore-maxscale-cdc-adapters-1.1.3-1-x86_64-bionic.deb
* MariaDB-MaxScale

  * maxscale-2.2.2-1.debian.bionic.x86_64.deb
  * maxscale-cdc-connector-2.2.2-1.debian.bionic.x86_64.deb


## Ubuntu 18 DEB package installation


### MariaDB ColumnStore


Follow the instructions for installing MariaDB Columnstore DEBs


[preparing-for-columnstore-installation-11x.md](preparing-and-installing-mariadb-columnstore-11x/preparing-for-columnstore-installation-11x.md)


### MariaDB ColumnStore API (Bulk Write SDK)


Follow the instructions for installing MariaDB Columnstore API DEB


[columnstore-bulk-write-sdk.md](../columnstore-data-ingestion/columnstore-bulk-write-sdk.md)


### MariaDB ColumnStore Tools


Follow the instructions for installing MariaDB Columnstore Tools


[backup-and-restore-for-mariadb-columnstore-110-onwards.md](../managing-columnstore/managing-columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110-onwards.md)


### MariaDB ColumnStore Connectors


#### ODBC Connector


How to Install the ODBC Connector:


[](https://mariadb.com/kb/en/library/about-mariadb-connector-odbc/)


Additional Information on the ODBC connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/)


#### Java Connector


How to Install the Java Connector:


[installing-mariadb-connectorj](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/installing-mariadb-connectorj)


Additional information on the Java Connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/)


### MariaDB ColumnStore Data Adapters


How to Install on the Data Adapters:


[columnstore-streaming-data-adapters.md](../columnstore-data-ingestion/columnstore-streaming-data-adapters.md)


### MariaDB MaxScale


How to Install on the MariaDB MaxScale:


[](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-21-06/)


## Ubuntu 18 Binary Package


Once the package is downloaded, it can be untarred with the following command:


```
tar zxvf mariadb-columnstore-x.x.x-x-bionic.adm64.bin.tar.gz
```

This is the contents of the installed package:


* MariaDB-ColumnStore

  * mariadb-columnstore-1.1.3-1-bionic.amd64.bin.tar.gz
* MariaDB-ColumnStore-API/

  * mariadb-columnstore-api-1.1.3-1-x86_64-bionic.deb
* MariaDB-ColumnStore-Tools

  * mariadb-columnstore-tools-1.1.3-1.tar.gz
* MariaDB-Connectors

  * mariadb-connector-[ODBC-3](https://jira.mariadb.org/browse/ODBC-3).0.2-ga-debian-i686.tar.gz
  * mariadb-java-client-2.2.2.jar
* MariaDB-Data-Adapters

  * mariadb-columnstore-kafka-adapters-1.1.3-1-x86_64-bionic.deb
  * mariadb-columnstore-maxscale-cdc-adapters-1.1.3-1-x86_64-bionic.deb
* MariaDB-MaxScale

  * maxscale-2.2.2-1.debian.bionic.tar.gz
  * maxscale-cdc-connector-2.2.2-1.debian.bionic.x86_64.deb


## Ubuntu 18 Binary Package installation


### MariaDB ColumnStore


Follow the instructions for installing MariaDB Columnstore binary package


[preparing-for-columnstore-installation-11x.md](preparing-and-installing-mariadb-columnstore-11x/preparing-for-columnstore-installation-11x.md)


### MariaDB ColumnStore API (Bulk Write SDK)


Follow the instructions for installing MariaDB Columnstore API RPM


[columnstore-bulk-write-sdk.md](../columnstore-data-ingestion/columnstore-bulk-write-sdk.md)


### MariaDB ColumnStore Tools


Follow the instructions for installing MariaDB Columnstore Tools


[backup-and-restore-for-mariadb-columnstore-110-onwards.md](../managing-columnstore/managing-columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110-onwards.md)


### MariaDB ColumnStore Connectors


#### ODBC Connector


How to Install the ODBC Connector:


[](https://mariadb.com/kb/en/library/about-mariadb-connector-odbc/)


Additional Information on the ODBC connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/)


#### Java Connector


How to Install the Java Connector:


[installing-mariadb-connectorj](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/installing-mariadb-connectorj)


Additional information on the Java Connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/)


### MariaDB ColumnStore Data Adapters


How to Install on the Data Adapters:


[columnstore-streaming-data-adapters.md](../columnstore-data-ingestion/columnstore-streaming-data-adapters.md)


### MariaDB MaxScale


How to Install on the MariaDB MaxScale:


[](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-21-06/)


CC BY-SA / Gnu FDL

