
# DBT3 Automation Scripts

DBT-3 (OSDL Database Test 3) is a workload tool for the Linux kernel that OSDL (Open Source Development Labs, inc) developed based on TPC-H which is provided by the Transaction Performance Processing Council (TPC).

DBT-3, like TPC-H, simulates an actual decision-making support system and models complex business analysis applications that perform data processing jobs for making better business decisions. By running the workload that DBT-3 simulates, it is possible to verify and measure the performances of the Linux kernel in an actual decision-making support system.

DBT-3 uses the "scale factor (SF)" as a stress indicator of the system. By varying the SF, it becomes possible to make the size of a database the SF times its size.

The tests performed by DBT-3 comprise the three tests listed below. DBT-3 obtains the execution times of these three tests as well as the system status information and database statistics information.

1.  **Load test**
      * Enters the data to be used for the Power and Throughput tests into the database. Makes a bulk insert of the huge CSV data corresponding to the scale factor into the database.
2.  **Power test**
      * Performs 22 complex queries.
3.  **Throughput test**
      * Performs the same 22 queries as in the Power test simultaneously in more than one process.

For the purpose of this task, only the Power test is performed over a preliminary prepared database with various Scale factors. The time for each query execution will be measured and stored into a database. Later the results of one whole test with all 22 queries will be rendered into a histogram graphics comparing it to different configurations.

## Benchmark environment preparation

### sudo rights

The user that will run the benchmark must have sudo rights on the machine. For clearing the system caches between query runs, the automation script uses the following command:

```
sudo /sbin/sysctl vm.drop_caches=3
```

This command must be run with superuser rights. Even if a user supplies a password to sudo, this password expires after some timeout. In order for this command to be run without requiring a password, the following line should be added to the sudoers file (edit it with the `"sudo visudo"` command):

```
'your_username' ALL=NOPASSWD:/sbin/sysctl
```

...where `'your_username'` is the user that will run the benchmark.

### Required software

The automated DBT3 benchmark requires the following software:

  * [Perl](https://www.perl.org/)
  * [mariadb-tools](https://launchpad.net/mariadb-tools)
      * The project folder is called "`dbt3_benchmark`" and is under `mariadb-tools`.
  * [dbt3-1.9](https://sourceforge.net/projects/osdldbt/files/dbt3/)
  * [Gnuplot 4.4](https://www.gnuplot.info/) — graphics output program.
  * [Config::Auto](https://search.cpan.org/~simon/Config-Auto-0.03/Auto.pm) — a Perl module that reads configuration files. To install it use the following command:
    ```
    sudo cpan Config::Auto
    ```
  * [DBD::mysql](https://search.cpan.org/~capttofu/DBD-mysql-4.020/lib/DBD/mysql.pm) — a Perl module to connect to MariaDB/MySQL and PostgreSQL. To install it use the following command:
    ```
    sudo cpan DBD::mysql
    ```
    **NOTE:** You may receive an error saying that CPAN could not find `mysql_config`. In this case you have to install the mysql client development library. In OpenSuse the command is:
    ```
    sudo zypper install libmysqlclient-devel
    ```
    Alternatively this module can be installed manually by following these steps:
    1.  Download DBD-mysql-4.020.tar.gz from [search.cpan.org](https://search.cpan.org/~capttofu/DBD-mysql-4.020/lib/DBD/mysql.pm) and unpack it
    2.  Run the perl script PerlMake.pl under the unzipped dir:
        ```
        perl Makefile.PL --mysql_config=/path/to/some/mysql_binary_distribution/bin/mysql_config
        ```
    3.  Run `make` to compile `DBD::mysql`:
        ```
        make
        ```
    4.  Add the necessary paths in order to run `DBD::mysql`:
        ```
        export PERL5LIB="/path/to/unzipped_DBD_mysql/DBD-mysql-4.020/lib"
        export LD_LIBRARY_PATH="/path/to/unzipped_DBD_mysql/DBD-mysql-4.020/blib/arch/auto/DBD/mysql/:/path/to/some/mysql_binary_distribution/lib/"
        ```

### Tested DBMS

  * [MySQL 5.5.x](https://dev.mysql.com/downloads/mysql/#downloads)
  * [MySQL 5.6.x](https://dev.mysql.com/downloads/mysql/#downloads)
  * [MariaDB 5.3.x](https://launchpad.net/maria/5.3)
      * Download with Bazaar: `bzr branch lp:maria/5.3`
  * [MariaDB 5.5.x](https://launchpad.net/maria/5.5)
      * Download with Bazaar: `bzr branch lp:maria/5.5`
  * [PostgreSQL](https://www.postgresql.org/ftp/source/v9.1rc1/)

**NOTE:** The DBT3 benchmark requires a lot of disk space (for example MySQL 5.5.x + MyISAM database with scale factor 30 takes about 50 GB). Also some queries require the utilization of temp tables under the directory set by the `--tmpdir` startup parameter passed to `mysqld`. In the prepared configuration files the temp directory is pointed to the `mysql` system directory of the binary distribution, but one should reassure that there is enough free space available for the temp directory.

-----

## Installation instructions

**NOTE:** The directory where all the files will be downloaded or installed will be referred as `$PROJECT_HOME`. This could be for example `~/benchmark/dbt3`.

### Download mariadb-tools

1.  Go to your project folder
    ```
    cd $PROJECT_HOME
    ```
2.  Get the latest branch from LaunchPad with Bazaar:
    ```
    bzr branch lp:mariadb-tools
    ```
    Now the project for the dbt3 benchmark test will be in the following dir:
    ```
    $PROJECT_HOME/mariadb-tools/dbt3_benchmark/
    ```
    The project `dbt3_benchmark` has the following directories and files:
      * `config` — a folder where the configuration files for MariaDB, MySQL and PostgreSQL are stored. They are divided into subfolders named '`sXX`', where `XX` is the scale factor.
      * `dbt3_mysql` — a folder with all the necessary files for preparing DBT3 databases and queries for the tests with MySQL and MariaDB
      * `tests` — a folder where the different test configurations are stored. It contains the following directories:
          * `db_conf` — here are stored the database configuration files
          * `queries_conf` — here are stored the different queries configuration files
          * `results_db_conf` — here is stored the configuration of the results database
          * `test_conf` — here are the test configurations
          * `launcher.pl` — a perl script that automates the test. Details about calling and functionality of this file are listed later on this page.

### Prepare benchmark workload and queries

For the purpose of the benchmark from [DBT3-1.9](https://sourceforge.net/projects/osdldbt/files/dbt3/) we will only need **DBGEN** and **QGEN**. DBGEN is a tool that generates a workload for the test and QGEN is a tool that generates the queries used for the test.

1.  Download the archive for DBT3 1.9 into your project folder `$PROJECT_HOME`
2.  Unzip the archive into your project folder
    ```
    cd $PROJECT_HOME
    tar -zxf dbt3-1.9.tar.gz
    ```
3.  Copy the file `tpcd.h` into the dbt3 folder. This step includes the necessary labels for MySQL/MariaDB when building queries.
    ```
    cp $PROJECT_HOME/mariadb-tools/dbt3_benchmark/dbt3_mysql/tpcd.h $PROJECT_HOME/dbt3-1.9/src/dbgen/
    ```
4.  Copy the file `Makefile` under `$PROJECT_HOME/mariadb-tools/dbt3_benchmark/dbt3_mysql/` into the dbt3 folder
      * NOTE: This step is executed only if you want to overwrite the default behavior of PostgreSQL settings. After copying this Makefile and building the project, QGEN will be set to generate queries for MariaDB/MySQL. If you skip this step, QGEN will generate queries for PostgreSQL by default.
    <!-- end list -->
    ```
    cp $PROJECT_HOME/mariadb-tools/dbt3_benchmark/dbt3_mysql/Makefile $PROJECT_HOME/dbt3-1.9/src/dbgen/
    ```
5.  Go to `$PROJECT_HOME/dbt3-1.9/src/dbgen` and build the project
    ```
    cd $PROJECT_HOME/dbt3-1.9/src/dbgen
    make
    ```
6.  Set the variable `DSS_QUERY` to the folder with template queries for MariaDB/MySQL or for PostgreSQL
      * If you want to build the queries that fit MariaDB/MySQL dialect execute the following command:
        ```
        export DSS_QUERY=$PROJECT_HOME/mariadb-tools/dbt3_benchmark/dbt3_mysql/mysql_queries/
        ```
      * If you want to use the default PostgreSQL templates, execute the following command:
        ```
        export DSS_QUERY=$PROJECT_HOME/dbt3-1.9/queries/pgsql/
        ```
7.  Create a directory to store the generated queries in
    ```
    mkdir $PROJECT_HOME/gen_query
    ```
8.  Generate the queries (Example for scale factor 30)
    ```
    cd $PROJECT_HOME/dbt3-1.9/src/dbgen
    ./qgen -s 30 1 > $PROJECT_HOME/gen_query/s30-m/1.sql
    # ... repeat for all 22 queries
    ./qgen -s 30 22 > $PROJECT_HOME/gen_query/s30-m/22.sql
    ```
9.  Generate the explain queries
    ```
    ./qgen -s 30 -x 1 > $PROJECT_HOME/gen_query/s30-m/1_explain.sql
    # ... repeat for all 22 queries
    ./qgen -s 30 -x 22 > $PROJECT_HOME/gen_query/s30-m/22_explain.sql
    ```
    Now the generated queries for MariaDB/MySQL test are ready and are stored into the folder `$PROJECT_HOME/gen_query/s30-m/`
10. Create a directory for the generated workload
    ```
    mkdir $PROJECT_HOME/gen_data/s30
    ```
11. Set the variable `DSS_PATH` to the folder with the generated table data.
    ```
    export DSS_PATH=$PROJECT_HOME/gen_data/s30/
    ```
12. Generate the table data (Example for scale factor 30)
    ```
    ./dbgen -vfF -s 30
    ```
    Now the generated data load is stored into the folder set in `$DSS_PATH`. See [DBT3 example preparation time](https://www.google.com/search?q=dbt3-example-preparation-time.md) to see how long it would take you to prepare the databases for the test.

### Download & Build Instructions

Follow the specific download and build instructions for your chosen DBMS.

#### [MySQL 5.5.x](https://dev.mysql.com/downloads/mysql/#downloads) / [MySQL 5.6.x](https://dev.mysql.com/downloads/mysql/#downloads)

1.  Download the tar.gz file into your project folder (e.g., `$PROJECT_HOME/bin/`)
2.  Unzip the archive: `gunzip < mysql-version.tar.gz | tar xf -`
3.  The server can be started with:
    ```
    $PROJECT_HOME/bin/mysql-version/bin/mysqld_safe --datadir=some/data/dir &
    ```

#### [MariaDB 5.3.x](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3) / [MariaDB 5.5.x](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

1.  Download with Bazaar: `bzr branch lp:maria/5.x`
2.  Build MariaDB:
    ```
    cd mariadb-5.x/
    ./BUILD/compile-amd64-max
    ```
3.  Create a binary distribution: `./scripts/make_binary_distribution`
4.  Move and unzip the generated tar.gz to `$PROJECT_HOME/bin`

#### [PostgreSQL](https://www.postgresql.org/ftp/source/v9.1rc1/)

1.  Download and unzip the source tar.gz
2.  Configure, build, and install:
    ```
    ./configure --prefix=$PROJECT_HOME/bin/PostgreSQL_bin
    make
    make install
    ```

### Prepare the databases for the benchmark

1.  **Edit SQL Load Script**: Open the appropriate `.sql` file (e.g., `make-dbt3-db_innodb.sql`) and replace the placeholder paths in the `LOAD DATA INFILE` commands with the correct path to your generated data.
2.  **Create Database**: Create an empty database for the benchmark.
3.  **Start Server**: Start the `mysqld` or `postgres` process with the correct configuration.
4.  **Load Data**: Execute the `.sql` script to load the data into the database.
5.  **Shutdown Server**: Shut down the database server.

-----

## Automation script

The benchmark is run using the `launcher.pl` script, which is configured by a set of `.conf` files.

### Configuration

  * **Top-level configuration**: Combines paths to Test, DBMS, Queries, and Results DB config files.
  * **DBMS server configuration**: Describes the benchmarked DBMS (paths, user, config files, etc.).
  * **Test configuration**: Describes the test itself (warmups, number of runs, timeouts, etc.).
  * **Queries configuration**: Lists the queries to be benchmarked and allows overriding of global settings.
  * **Results database configuration**: Settings for the database where results will be stored.

### Script startup parameters

`launcher.pl` accepts startup parameters like `--test`, `--results-output-dir`, and others to define the test environment and override settings in the config files.

### Results extraction mechanisms

There are three mechanisms for extracting results:

  * **`ANALYZE_EXPLAIN`**: For InnoDB, runs the query only with the fastest execution plan.
  * **`MIN_MAX_OUT_OF_N`**: For InnoDB, stores the fastest and slowest run times.
  * **`SIMPLE_AVERAGE`**: For MyISAM, calculates the average execution time.

-----

## Results

The script generates various output files, including:

  * **`results.dat`**: Raw data for plotting.
  * **`graphics.jpeg`**: A Gnuplot-generated graph of the results.
  * Detailed logs and statistics for each test run.

### Benchmark Results Pages

  * [DBT3 benchmark results MyISAM](https://www.google.com/search?q=dbt3-benchmark-results-myisam.md)
  * [DBT3 benchmark results InnoDB](https://www.google.com/search?q=dbt3-benchmark-results-innodb.md)

\<sub\>*This page is licensed: CC BY-SA / Gnu FDL*\</sub\>