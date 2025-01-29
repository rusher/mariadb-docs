# Get, Build and Test Latest MariaDB the Lazy Way

The intention of this documentation is show all the steps of getting, building and testing the latest MariaDB server (10.5 at time of writing) from GitHub. Each stage links to the full documentation for that step if you need to find out more.

### [Install all tools needed to build MariaDB](https://mariadb.com/kb/en/Build_Environment_Setup_for_Linux/) <a href="#build_environment_setup_for_linuxinstall-all-tools-needed-to-build-mariadb" id="build_environment_setup_for_linuxinstall-all-tools-needed-to-build-mariadb"></a>

#### OpenSuse <a href="#opensuse" id="opensuse"></a>

```
sudo zypper install git gcc gcc-c++ make bison ncurses ncurses-devel zlib-devel libevent-devel cmake openssl
```

#### Debian <a href="#debian" id="debian"></a>

```
apt install -y build-essential bison libgnutls28-dev
apt build-dep mariadb-server 
```

### [Set Up git](https://mariadb.com/kb/en/using-git/) <a href="#using-gitset-up-git" id="using-gitset-up-git"></a>

Fetch and checkout the MariaDB source to a subdirectory of the current directory

```
git clone https://github.com/MariaDB/server.git mariadb
cd mariadb
git checkout 11.4
```

### [Build It](https://mariadb.com/kb/en/generic-build-instructions/) <a href="#generic-build-instructionsbuild-it" id="generic-build-instructionsbuild-it"></a>

The following command builds a server the same way that is used for building releases. Use `cmake . -DCMAKE_BUILD_TYPE=Debug` to build for debugging.

```
cmake . -DBUILD_CONFIG=mysql_release && cmake --build . --parallel=8
```

### [Check the Server (If You Want To)](https://mariadb.com/kb/en/mysql-test/) <a href="#mysql-testcheck-the-server-if-you-want-to" id="mysql-testcheck-the-server-if-you-want-to"></a>

```
mysql-test/mtr --parallel=8 --force
```

### [Install the Default Databases](https://mariadb.com/kb/en/mariadb-install-db/) <a href="#mariadb-install-dbinstall-the-default-databases" id="mariadb-install-dbinstall-the-default-databases"></a>

```
./scripts/mariadb-install-db --srcdir=.
```

(Older MariaDB version use [mysql\_install\_db](https://mariadb.com/kb/en/mysql_install_db/))

### Install the Server (If needed) <a href="#install-the-server-if-needed" id="install-the-server-if-needed"></a>

You can also [run and test mariadb directly from the build directory](https://mariadb.com/kb/en/running-mariadb-from-the-build-directory/), in which case you can skip the rest of the steps below.

```
cmake --install .
```

#### [Start the Server](https://mariadb.com/kb/en/starting-and-stopping-mariadb-automatically/) <a href="#starting-and-stopping-mariadb-automaticallystart-the-server" id="starting-and-stopping-mariadb-automaticallystart-the-server"></a>

Start the server in it's own terminal window for testing. Note that the directory depends on your system!

```
/usr/sbin/mariadbd
```
