# Running MariaDB from the Build Directory

You can run mariadbd directly from the build directory (without doing
`make install`).

#

# Starting mariadbd After Build on Windows

On Windows, the data directory is produced during the build.

The simplest way to start database from the command line is:
1. Go to the directory where mariadbd.exe is located (subdirectory sql\Debug or sql\Relwithdebinfo of the build directory)
1. From here, execute, if you are using [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-105) or newer, 
```
mariadbd.exe --console
```
 else 
```
mariadbd.exe --console
```

As usual, you can pass other server parameters on the command line, or store them in a my.ini configuraton file and pass `--defaults-file=path\to\my.ini`

The default search path on Windows for the my.ini file is:

* GetSystemWindowsDirectory()
* GetWindowsDirectory()
* C:\
* Directory where the executable is located

#

# Starting mariadbd After Build on Unix

Copy the following to your '`~/.my.cnf`' file.

There are two lines you have to edit: '`datadir=`' and '`language=`'. Be sure to change them to match your environment.

```
# Example MariadB config file.

# You can copy this to one of:
# /etc/my.cnf to set global options,

# /mysql-data-dir/my.cnf to get server specific options or
# ~/my.cnf for user specific options.

# 
# One can use all long options that the program supports.

# Run the program with --help to get a list of available options

# This will be passed to all MariaDB clients

[client]
#password=my_password
#port=3306
#socket=/tmp/mysql.sock

# Here is entries for some specific programs

# The following values assume you have at least 32M ram

# The mariadb server (both [mysqld] and [mariadb] works here)

[mariadb]
#port=3306
#socket=/tmp/mysql.sock

# The following three entries caused mysqld 10.0.1-MariaDB (and possibly other versions) to abort...

# skip-locking
# set-variable = key_buffer=16M

loose-innodb_data_file_path = ibdata1:1000M
loose-mutex-deadlock-detector
gdb

#

######## Fix the two following paths

# Where you want to have your database

datadir=/path/to/data/dir

# Where you have your mysql/MariaDB source + sql/share/english

language=/path/to/src/dir/sql/share/english

#

######### One can also have a different path for different versions, to simplify development.

[mariadb-10.1]
lc-messages-dir=/my/maria-10.1/sql/share

[mariadb-10.2]
lc-messages-dir=/my/maria-10.2/sql/share

[mysqldump]
quick
set-variable = max_allowed_packet=16M

[mysql]
no-auto-rehash

[myisamchk]
set-variable= key_buffer=128M
```

With the above file in place, go to your MariaDB source directory and execute:

```
./scripts/mariadb-install-db --srcdir=$PWD --datadir=/path/to/data/dir --user=$LOGNAME
```

Above '$PWD' is the environment variable that points to your current directory.
If you added `datadir` to your `my.cnf`, you don't have to give this option above.
Also above, --user=$LOGNAME is necessary when using msqyld 10.0.1-MariaDB (and possibly other versions)

Now you can start `mariadbd` (or `mysqld` if you are using a version older than [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-105)) in the debugger:

```
cd sql
ddd ./mariadbd &
```

Or start mariadbd on its own:

```
cd sql
./mariadbd &
```

After starting up `mariadbd` using one of the above methods (with the debugger or without), launch the client (as root if you don't have any users setup yet).

```
../client/mariadb
```

#

# Using a Storage Engine Plugin

The simplest case is to compile the storage engine into MariaDB:

```
cmake -DWITH_PLUGIN_<plugin_name>=1` .
```

Another option is to point `mariadbd` to the storage engine directory:

```
./mariadbd --plugin-dir={build-dir-path}/storage/connect/.libs
```