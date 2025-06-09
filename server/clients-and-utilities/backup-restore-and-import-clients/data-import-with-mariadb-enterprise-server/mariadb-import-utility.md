
# Mariadb Import Utility


# Overview


MariaDB Enterprise Server users can import data into a database using the mariadb-import utility:


* The mariadb-import utility provides a command-line interface (CLI)
* The mariadb-import utility can import data from TSV and CSV files
* The mariadb-import utility is available for Linux and Windows
* The mariadb-import utility supports many command-line options


# Compatibility


# Installation


Installation of MariaDB Import varies by operating system.


## Linux (Repository)


1. Configure a MariaDB repository.


Before MariaDB Import can be installed on Linux, a MariaDB repository must be configured. MariaDB Corporation offers multiple repositories:
**For MariaDB Corporation customers, the MariaDB Enterprise Repository is available.**For anyone else, the MariaDB Community Repository is publicly available.


For additional information on how to configure a MariaDB repository, see "Configure MariaDB Repository".


2. Install MariaDB Import and package dependencies.


Install on CentOS / RHEL / Rocky Linux (YUM):


```
$ sudo yum install MariaDB-client
```

Install on Debian / Ubuntu (APT):


```
$ sudo apt install mariadb-client
```

Install on SLES (ZYpp):


```
$ sudo zypper install MariaDB-client
```

## Windows


1. Access [MariaDB Downloads](https://mariadb.com/downloads/community/community-server/) for MariaDB Community Server.


2. In the "Version" dropdown, select the version you want to download.


3. In the "OS" dropdown, select "MS Windows (64-bit)".


4. Click the "Download" button to download the MSI package.


5. When the MSI package finishes downloading, run it.


6. On the first screen, click "Next" to start the Setup Wizard.


7. On the second screen, click the license agreement checkbox, and then click "Next".


8. On the third screen, select the components you want to install. If you only want the standard MariaDB Client tools:


* Deselect "Database instance".
* Deselect "Backup utilities".
* Deselect "Development Components".
* Deselect "Third party tools".
* When only "Client programs" is selected, click "Next".


9. On the next screen, click "Install".


10. When the installation process completes, click "Finish".


# Import Data


The procedure to import data depends on the operating system.


## Linux


1. Determine the connection parameters for your MariaDB Enterprise Server database.


2. Use MariaDB Import with the connection information to import the data from the TSV or CSV file into your MariaDB Enterprise Server database:


```
$ mariadb-import --host FULLY_QUALIFIED_DOMAIN_NAME --port TCP_PORT \
      --user DATABASE_USER --password \
      --ssl-verify-server-cert \
      --ssl-ca ~/PATH_TO_PEM_FILE \
      --local \
      --ignore-lines=1 \
      accounts contacts.tsv
```

**Replace `FULLY_QUALIFIED_DOMAIN_NAME` with the IP address or Fully Qualified Domain Name of your database** Replace `TCP_PORT` with the TCP port of your database
**Replace `DATABASE_USER` with the username for your database user account** If TLS is required, replace `/PATH_TO_PEM_FILE` with the path to the certificate authority chain (.pem) file
**If your file is a CSV file, rather than a TSV file, specify `--fields-terminated-by=`,** Specify the database name as the first argument (from above, accounts)
**The table name is extracted from the TSV or CSV file's basename (from above, contacts)**


3. After the command is executed, you will be prompted for the password of your database user account.


## Windows


1. Fix your executable search path.


On Windows, MariaDB Import is not typically found in the executable search path by default. You must find its installation path, and add that path to the executable search path:


```
$ SET "PATH=C:\Program Files\MariaDB 10.6\bin;%PATH%"
```

2. Determine the connection parameters for your MariaDB Enterprise Server database.


3. Use MariaDB Import with the connection information to import the data from the TSV or CSV file into your MariaDB Enterprise Server database:


```
$ mariadb-import --host FULLY_QUALIFIED_DOMAIN_NAME --port TCP_PORT \
      --user DATABASE_USER --password \
      --ssl-verify-server-cert \
      --ssl-ca ~/PATH_TO_PEM_FILE \
      --local \
      --ignore-lines=1 \
      accounts contacts.tsv
```

**Replace `FULLY_QUALIFIED_DOMAIN_NAME` with the IP address or Fully Qualified Domain Name of your database** Replace `TCP_PORT` with the TCP port of your database
**Replace `DATABASE_USER` with the username for your database user account** Replace `/PATH_TO_PEM_FILE` with the path to the certificate authority chain (.pem) file
**If your file is a CSV file, rather than a TSV file, specify --fields-terminated-by=,** Specify the database name as the first argument (from above, accounts)
**The table name is extracted from the TSV or CSV file's basename (from above, contacts)**


4. After the command is executed, you will be prompted for the password of your database user account.


## MariaDB Import 10.3 and Older


The instructions provided above are written for MariaDB Import 10.4 and later, which uses the binary filename of `mariadb-import`.


Copyright © 2025 MariaDB


{% @marketo/form formId="4316" %}
