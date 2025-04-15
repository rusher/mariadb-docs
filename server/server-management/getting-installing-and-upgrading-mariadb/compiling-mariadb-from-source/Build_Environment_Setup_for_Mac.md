
# Build Environment Setup for Mac

## XCode


* Install Xcode from Apple (free registration required): [](https://developer.apple.com/xcode/) or from your Mac OS X installation disk (macports needs XCode >= 3.1, so if you do not have that version or greater you will need to download the latest version, which is 900+ MB)


You can install the necessary dependencies using either MacPorts or Homebrew.


## Using MacPorts


* [Download](https://svn.macports.org/repository/macports/downloads/) and install the MacPorts dmg image from [www.macports.org](https://www.macports.org)


* After installing, update it from the terminal: `<code class="fixed" style="white-space:pre-wrap">sudo port -v selfupdate
</code>`


`<code class="fixed" style="white-space:pre-wrap">sudo port install cmake jemalloc judy openssl boost gnutls</code>`


## Using Homebrew


* Download and install Homebrew from [https:brew.sh](https://brew.sh/)


`<code class="fixed" style="white-space:pre-wrap">brew install cmake jemalloc traildb/judy/judy openssl boost gnutls</code>`


Your Mac should now have everything it needs to get, compile, and otherwise work with the MariaDB source code. The next step is to actually get a copy of the code. For help with this see the [Getting the MariaDB Source Code](../../../clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md) page.


When building with Mac, you'll need `<code class="fixed" style="white-space:pre-wrap">-DOPENSSL_ROOT_DIR=/usr/local/openssl</code>` passed as a `<code class="fixed" style="white-space:pre-wrap">cmake</code>` argument to build against openssl correctly.

