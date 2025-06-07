# MariaDB Audit Plugin

MariaDB and MySQL are used in a broad range of environments, but if you needed to record user access to be in compliance with auditing regulations for your organization, you would previously have had to use other database solutions. To meet this need, though, MariaDB has developed the MariaDB Audit Plugin. Although the MariaDB Audit Plugin has some unique features available only for MariaDB, it can be used also with MySQL.

Basically, the purpose of the MariaDB Audit Plugin is to log the server's activity. For each client session, it records who connected to the server (i.e., user name and host), what queries were executed, and which tables were accessed and server variables that were changed. This information is stored in a rotating log file or it may be sent to the local `syslogd`.

The MariaDB Audit Plugin works with MariaDB, MySQL (as of, version 5.5.34 and 10.0.7) and Percona Server. MariaDB started including by default the Audit Plugin from versions 10.0.10 and 5.5.37, and it can be installed in any version from [MariaDB 5.5.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/mariadb-5520-release-notes).

#### Additional documentation

Below are links to additional documentation on the MariaDB Audit Plugin. They explain in detail how to install, configure and use the Audit Plugin.

* [Installation](mariadb-audit-plugin-installation.md)
* [Configuration](mariadb-audit-plugin-configuration.md)
* [Log Settings](mariadb-audit-plugin-log-settings.md)
* [Log Location & Rotation](mariadb-audit-plugin-location-and-rotation-of-logs.md)
* [Log Format](mariadb-audit-plugin-log-format.md)
* [Status Variables](mariadb-audit-plugin-status-variables.md)
* [System Variables](mariadb-audit-plugin-options-and-system-variables.md)
* [Release Notes](release-notes-mariadb-audit-plugin/)

#### Tutorials

Below are links to some tutorials on MariaDB's site and other sites. They may help you to get more out of the MariaDB Audit Plugin.

* [Introducing the MariaDB Audit Plugin](https://mariadb.com/kb/en/resources/blog/introducing-mariadb-audit-plugin)\
  by Anatoliy Dimitrov, September 2, 2014
* [Activating MariaDB Audit Log](https://tunnelix.com/activating-mariadb-audit-log/)\
  by Jaykishan Mutkawoa, May 30, 2016
* [Installing MariaDB Audit Plugin on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Options.AuditPlugin.html)\
  Amazon RDS supports using the MariaDB Audit Plugin on MySQL and MariaDB database instances.

#### Blog Articles

Below are links to web log articles on the MariaDB Audit Plugin. You may find them useful in understanding better how to use the Audit Plugin. Since some of these articles are older, they won't include changes and improvements in newer versions. You can rely on the documentation pages listed above for the most current information.

* [Activating Auditing for MariaDB in 5 Minutes](https://mariadb.com/kb/en/resources/blog/activating-auditing-mariadb-and-mysql-5-minutes)\
  by Ralf Gebhardt, September 29, 2013
* [Query and Password Filtering with the MariaDB Audit Plugin](https://mariadb.com/kb/en/resources/blog/query-and-password-filtering-mariadb-audit-plugin)\
  by Ralf Gebhardt, May 4, 2015
* [Set Up a Remote Log File using rsyslog](https://mariadb.com/kb/en/resources/blog/mariadb-audit-plugin-set-remote-log-file-using-rsyslog)\
  by Ralf Gebhardt, December 16, 2013
* [MySQL Auditing with MariaDB Auditing Plugin](https://planet.mysql.com/entry/?id=5994184)\
  by Peter Zeitsev, February 15, 2016

#### Sub-Documents
