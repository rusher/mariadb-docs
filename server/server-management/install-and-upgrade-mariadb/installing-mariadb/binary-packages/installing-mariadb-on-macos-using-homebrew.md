---
description: >-
  How to install MariaDB Server on macOS using the Homebrew package manager,
  including starting the service and securing the installation.
---

# Installing MariaDB on macOS

MariaDB Server is available for installation on macOS via the [Homebrew](https://brew.sh/) package manager. MariaDB Server (together with many client programs and helper tools) is available as a Homebrew "bottle", a precompiled package. If you haven't yet installed Homebrew, [see this section](installing-mariadb-on-macos-using-homebrew.md#homebrew-installation).

Install MariaDB Server like this:

```bash
brew install mariadb
```

Start MariaDB Server:

```bash
mysql.server start
```

To autostart MariaDB Server, use Homebrew's services functionality, which configures autostart with the `launchctl` utility from [launchd](../../../starting-and-stopping-mariadb/launchd.md):

```bash
brew services start mariadb
```

After MariaDB Server is started, you can log in like this, using the shell user name (for instance, _`myuser`_):

```bash
mariadb
```

Or log in as root:

```bash
sudo mysql -u root
```

## Upgrading MariaDB

Update your brew installation:

```bash
brew update
```

Then upgrade MariaDB Server:

```bash
brew upgrade mariadb
```

## Notes About Homebrew

### Installation

Install Homebrew like this:

1. Open a Terminal (<kbd>⌘ + Space</kbd> to open _Spotlight_, type _Terminal_).
2. Issue this command:\
   `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`&#x20;
   1. Alternatively, use the package installer (`.pkg`; at the time of writing this, [https://github.com/Homebrew/brew/releases/download/5.0.4/Homebrew-5.0.4.pkg](https://github.com/Homebrew/brew/releases/download/5.0.4/Homebrew-5.0.4.pkg))
3. Refer to the [Homebrew website](https://brew.sh/) for more information, particularly to the [Homebrew documentation](https://docs.brew.sh/).

### MariaDB Configuration

In Homebrew, the configuration file for MariaDB is located at:

* &#x20;`/usr/local/etc/my.cnf` for Intel-based Macs.
* `/opt/homebrew/etc/my.cnf` for Apple Silicon Macs (ARM architecture).

### MariaDB Information

Find information about the MariaDB version, analytics, and more, using the `brew info` command:

```shellscript
~> brew info mariadb
==> mariadb: stable 12.1.2 (bottled)
Drop-in replacement for MySQL
https://mariadb.org/
...
To restart mariadb after an upgrade:
  brew services restart mariadb
Or, if you don't want/need a background service you can just run:
  /opt/homebrew/opt/mariadb/bin/mariadbd-safe --datadir\=/opt/homebrew/var/mysql
==> Analytics
install: 6,319 (30 days), 12,735 (90 days), 62,444 (365 days)
install-on-request: 6,291 (30 days), 12,670 (90 days), 62,137 (365 days)
build-error: 8 (30 days)
```

### MariaDB Programs

MariaDB Server (`mariadbd`), the MariaDB command-line client (`mariadb`), and many more clients and tools are installed in `/opt/homebrew/Cellar/mariadb` (for Apple Silicon Macs). Find the location for your machine, as well as the MariaDB programs installed, with these commands:

```shellscript
~> which mariadb
/opt/homebrew/bin/mariadb # in the next command, use this location to cd to
~> cd /opt/homebrew/bin/; ls -1 maria*
mariabackup
mariadb
mariadb-access
...
mariadbd
mariadbd-multi
mariadbd-safe
mariadbd-safe-helper
```

### Terminal User & MariaDB User

To find out which user is used, issue these commands in a shell like _Terminal_:

```shellscript
~> users
myuser
~> mariadb -e "SELECT USER()"
+------------------+
| USER()           |
+------------------+
| myuser@localhost |
+------------------+
```

## Building MariaDB Server from source

In addition to the "bottled" MariaDB Server package available from Homebrew, you can use Homebrew to build MariaDB from source. This is useful if you want to use a different version of the server or enable some different capabilities that are not included in the bottle package.

Two components not included in the bottle package are the CONNECT and OQGRAPH engines, because they have non-standard dependencies. To build MariaDB Server with these engines, you must first install `boost` and `judy`. Follow these steps to install the dependencies and build the server:

```bash
brew install boost judy
brew install mariadb --build-from-source
```

You can also use Homebrew to build and install a pre-release version of MariaDB Server. Use this command to build and install a "development" version of MariaDB Server:

```bash
brew install mariadb --devel
```

## Other resources

* [mariadb.rb on github](https://github.com/Homebrew/homebrew-core/blob/master/Formula/m/mariadb.rb)
* [MariaDB Server on macOS: Does it even make sense to try?](https://www.youtube.com/watch?v=VoAPP6GDyYw) (video)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
