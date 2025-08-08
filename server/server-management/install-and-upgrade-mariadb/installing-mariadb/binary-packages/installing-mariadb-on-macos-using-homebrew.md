# Installing MariaDB Server on macOS Using Homebrew

MariaDB Server is available for installation on macOS (formerly Mac OS X) via the [Homebrew](https://brew.sh/) package manager.

MariaDB Server is available as a Homebrew "bottle", a pre-compiled package. This means you can install it without having to build from source yourself. This saves time.

After installing Homebrew, MariaDB Server can be installed with this command:

```bash
brew install mariadb
```

After installation, start MariaDB Server:

```bash
mysql.server start
```

To auto-start MariaDB Server, use Homebrew's services functionality, which configures auto-start with the launchctl utility from [launchd](../../../starting-and-stopping-mariadb/launchd.md):

```bash
brew services start mariadb
```

After MariaDB Server is started, you can log in as your user:

```bash
mysql
```

Or log in as root:

```bash
sudo mysql -u root
```

## Upgrading MariaDB

First you may need to update your brew installation:

```bash
brew update
```

Then, to upgrade MariaDB Server:

```bash
brew upgrade mariadb
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
