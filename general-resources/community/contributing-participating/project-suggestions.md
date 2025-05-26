---
description: Discuss with Max - is this page up to date? Should we mention developer names?
icon: question
---

# Project Suggestions

If you want to contribute to MariaDB but have a doubt about what to work on,\
this page lists possible projects. The projects are picked to be

* features that are considered to be needed/relevant (so, there will be\
  interest to accept the code into MariaDB)
* features that will not require the implementer to work in "difficult" parts\
  of the code and/or make high-risk changes that could be rejected out of\
  concern that they could destabilize the codebase

This list is by no means complete. You can find more open tasks in [our project planning tool, JIRA](../../development-articles/general-development-information/tools/jira.md). You can also ask for tasks on the[MariaDB mailing list/IRC](broken-reference).

## Progress reporting for ALTER TABLE ... ADD INDEX

* Description: MariaDB has support for[progress reporting](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting) during DDL statements. In some\
  scenarios, progress reporting actually works. In\
  others (`ALTER TABLE ... ADD INDEX` being the most important of them) it\
  has not been implemented. The task is to place progress reporting statements\
  at appropriate places in the code, so that `ALTER TABLE ... ADD INDEX`\
  provides some clues about which fraction of work it has done/has left. The[progress reporting](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting) page has a section which gives\
  clues what kind of statements will need to be inserted. Finding where to put\
  them is left as an exercise for the implementer :)
* Background required: C, C++
* Mentors: Sergei Petrunia

### MacOSX Installer

* Description: To create a MacOSX installer for MariaDB. Make the build\
  scripts work, and integrate it with BuildBot so we get automated MacOSX\
  builds for MariaDB.
* Background required: Knowledge of Apple toolchain, plus the GNU\
  toolchain. PackageMaker knowledge useful, as is some Perl knowledge.\
  Understanding shell scripting also.

### MariaDB management console snapin and WMI Provider (Windows)

* Description: Since Windows 2000, the standard/recommended/integrated solution for implementing software management tools on Windows has been Microsoft Management Console. Another system mechanism known as WMI (Windows management instrumentation) adds the ability to manage software remotely.\
  In MariaDB, we would like to have a management console to handle different database instances - create /remove /upgrade /start /stop MariaDB services, show and analyze error log, modify configuration parameters. It should be able to work with local database instances, as well as remote ones, using WMI.\
  The task would be to implement WMI provider and MMC snapin.
* Background required: C++/COM or .NET, WMI, MMC. Powershell knowlegde is a plus.

### Keystone authentication plugin

Keystone is the OpenStack Identity Service. The idea would be to ensure that MariaDB can authenticate to Keystone directly.

* Skills: Python, C/C++

CC BY-SA / Gnu FDL
