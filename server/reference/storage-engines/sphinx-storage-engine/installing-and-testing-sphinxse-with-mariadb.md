
# Installing and Testing SphinxSE with MariaDB

To use [SphinxSE](README.md) with MariaDB you need to first [download and install Sphinx](installing-sphinx.md).


Complete Sphinx documentation is available on the [Sphinx website](https://sphinxsearch.com/docs/).


## Tips for Installing Sphinx


### libexpat


One library we know you will need on Linux before you can install Sphinx is `<code>libexpat</code>`. If it is not installed, you will get the 
warning `<code class="fixed" style="white-space:pre-wrap">checking for libexpat... not found</code>`.
On Suse the package is called `<code>libexpat-devel</code>`,
on Ubuntu the package is called `<code>libexpat1-dev</code>`.


### MariaDB detection


If you run into problems with MariaDB not being detected, use the
following options:


```
--with-mysql            compile with MySQL support (default is enabled)
 --with-mysql-includes   path to MySQL header files
 --with-mysql-libs       path to MySQL libraries
```

The above will tell the `<code>configure</code>` script where your MySQL/MariaDB
installation is.


## Testing Sphinx


After installing Sphinx, you can check that things are working in MariaDB by
doing the following:


```
cd installation-dir/mysql-test
./mysql-test-run --suite=sphinx
```

If the above test doesn't pass, check the logs in the `<code>'var'</code>` directory.
If there is a problem with the sphinx installation, the reason can probably
be found in the log file at: `<code>var/log/sphinx.sphinx/searchd/sphinx.log</code>`.

