# About the MariaDB Jupyter Kernel

The MariaDB Jupyter Kernel is an Open Source kernel for [Jupyter](https://jupyter.org) which enables users to run MariaDB in a [Jupyter](https://jupyter.org) notebook.

Notebooks can be run in a variety of environments, ranging from your local computer for testing purposes via [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) to complex [Zero To JupyterHub Kubernetes systems](https://zero-to-jupyterhub.readthedocs.io/en/latest/) running in the cloud.

The [mariadb\_kernel](https://github.com/MariaDB/mariadb_kernel) project is agnostic about the complexity of your [Jupyter](https://jupyter.org) infrastructure, it can run on any of them thanks to the way [Jupyter](https://jupyter.org) designed its kernel machinery. As long as MariaDB is installed on the host running the kernel and there is MariaDB Server running somewhere, things should work out as expected.

## Motivation

We created the [mariadb\_kernel](https://github.com/MariaDB/mariadb_kernel) project with some simple goals in mind:

* Help existing MariaDB users have an alternative to the classical [mariadb command-line client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mysql-command-line-client) based on Jupyter.
* Bring MariaDB Server to Jupyter and Python users who would like to use our Open Source database for handling their datasets.

If you would love to be able to run SQL against MariaDB data from Jupyter notebooks\
or you want to run a training program and help your employees learn SQL,\
if you are a teacher and you’d love to use Jupyter for your SQL classes or\
you are a data scientist trying to quickly chart or explore your datasets,\
you should take a look at this project.

## Contents

### [Installation](../other/mariadb-jupyter-kernel/mariadb-jupyter-kernel-installation.md)

* [Quick Installation Steps](../other/mariadb-jupyter-kernel/mariadb-jupyter-kernel-installation.md#quick-installation-steps)
* [Complete Installation Steps](../other/mariadb-jupyter-kernel/mariadb-jupyter-kernel-installation.md#complete-installation-steps)
* [Platforms Coverage](../other/mariadb-jupyter-kernel/mariadb-jupyter-kernel-installation.md#platforms-coverage)

### [Configuring the kernel](../other/mariadb-jupyter-kernel/configuring-the-mariadb-jupyter-kernel.md)

* [Config File Location](../other/mariadb-jupyter-kernel/configuring-the-mariadb-jupyter-kernel.md#config-file-location)
* [Config Example](../other/mariadb-jupyter-kernel/configuring-the-mariadb-jupyter-kernel.md#config-example)
* [The Full List of JSON Options](../other/mariadb-jupyter-kernel/configuring-the-mariadb-jupyter-kernel.md#the-full-list-of-json-options)

### [Using the Kernel](https://mariadb.com/kb/en/using-the-mariadb-jupyter-kernel/)

* [General Usage Information](../other/mariadb-jupyter-kernel/using-the-kernel/general-mariadb-jupyter-kernel-usage-information.md)
* [SQL Autocompletion and Introspection](../other/mariadb-jupyter-kernel/using-the-kernel/sql-autocompletion-and-introspection.md)
* [Magic Commands](../other/mariadb-jupyter-kernel/using-the-kernel/mariadb-jupyter-kernel-magic-commands.md)
* [Restrictions and Limitations](https://mariadb.com/kb/en/using-the-mariadb-jupyter-kernel/#restrictions-and-limitations)

### [Main Components and Architecture](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md)

* [Architecture](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#architecture)
* [Components](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#components)
  * [MariaDBKernel](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#mariadbkernel)
  * [ClientConfig](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#clientconfig)
  * [MariaDBClient](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#mariadbclient)
  * [MariaDBServer](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#mariadbserver)
  * [CodeParser](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#codeparser)
  * [MagicFactory](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#magicfactory)
  * [MariaMagic](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#mariamagic)
  * [LineMagic](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#linemagic)
  * [CellMagic](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#cellmagic)
  * [LSMagic](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#lsmagic)
  * [Line](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#line)
  * [DF](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#df)
  * [Bar](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#bar)
  * [Pie](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#pie)
  * [Delimiter](../other/mariadb-jupyter-kernel/the-mariadb-jupyter-kernel-main-components-and-architecture.md#delimiter)

### [Extending the Kernel](../other/mariadb-jupyter-kernel/contributing-to-the-mariadb-jupyter-kernel-project.md)

### [Changelog](../other/mariadb-jupyter-kernel/changes-in-mariadb-jupyter-kernel.md)

* [v0.2.2](../other/mariadb-jupyter-kernel/changes-in-mariadb-jupyter-kernel.md#v020-02-november-2021)
* [v0.1.1](../other/mariadb-jupyter-kernel/changes-in-mariadb-jupyter-kernel.md#v011-29-march-2021)
* [v0.1.0 First release!](../other/mariadb-jupyter-kernel/changes-in-mariadb-jupyter-kernel.md#v010-11-january-2021)


{% @marketo/form formid="4316" %}
