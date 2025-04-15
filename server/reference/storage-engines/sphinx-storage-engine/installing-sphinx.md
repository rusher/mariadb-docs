
# Installing Sphinx

In order to use the [Sphinx Storage Engine](README.md), it is necessary to install the Sphinx daemon.


Many Linux distributions have Sphinx in their repositories. These can be used to install Sphinx instead of following the instructions below, but these are usually quite old versions and don't all include API's for easy integration. Ubuntu users can use the updated repository at [sphinxsearch-rel21](https://launchpad.net/~builds/+archive/sphinxsearch-rel21) (see instructions below). Alternatively, download from [](https://sphinxsearch.com/downloads/release/)


## Debian and Ubuntu


Ubuntu users can make use of the repository, as follows:


```
sudo add-apt-repository ppa:builds/sphinxsearch-rel21
sudo apt-get update
sudo apt-get install sphinxsearch
```

Alternatively, install as follows:


* The Sphinx package and daemon are named `<code>sphinxsearch</code>`.
* `<code>sudo apt-get install unixodbc libpq5 mariadb-client</code>`
* `<code>sudo dpkg -i sphinxsearch*.deb</code>`
* [Configure Sphinx](configuring-sphinx.md) as required
* You may need to check `<code>/etc/default/sphinxsearch</code>` to see that `<code>START=yes</code>`
* Start with `<code>sudo service sphinxsearch start</code>` (and stop with `<code>sudo service sphinxsearch stop</code>`)


## Red Hat and CentOS


* The package name is `<code>sphinx</code>` and the daemon `<code>searchd</code>`.
* `<code>sudo yum install postgresql-libs unixODBC</code>`
* `<code>sudo rpm -Uhv sphinx*.rpm</code>`
* [Configure Sphinx](configuring-sphinx.md) as required
* `<code>service searchd start</code>`


## Windows


* Unzip and extract the downloaded zip file
* Move the extracted directory to `<code>C:\Sphinx</code>`
* [Configure Sphinx](configuring-sphinx.md) as required
* Install as a service: 

  * `<code>C:\Sphinx\bin> C:\Sphinx\bin\searchd --install --config C:\Sphinx\sphinx.conf.in --servicename SphinxSearch</code>`


Once Sphinx has been installed, it will need to be [configured](configuring-sphinx.md).


Full instructions, including details on compiling Sphinx yourself, are available at [current.html](https://sphinxsearch.com/docs/current.html).

