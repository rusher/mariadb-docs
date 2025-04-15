
# Google Season of Docs 2020

MariaDB is applying to participate in the 2020 Google Season of Docs.



# Where to Start


Please join us on [Zulip](https://mariadb.com/kb/en/irc-chat-servers-and-zulip-instance/) to mingle with the community. You can also subscribe to [maria-docs@lists.launchpad.net](https://launchpad.net/~maria-docs), the documentation mailing list.


# List of Tasks


## Migration Documentation


You will choose a major relational DBMS, and, focusing on the most recent stable releases, document the process to migrate to MariaDB, including MariaDB equivalents to features in that system, and a detailed list of features that exist in one but not the other, as well as possible workarounds. For an example, see the work-in-progress [Migrating from SQL Server to MariaDB](../../../../server/server-management/getting-installing-and-upgrading-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-sql-server/README.md) as well as the documentation on [migrating from MySQL to MariaDB](../../../../server/server-management/getting-installing-and-upgrading-mariadb/migrating-to-mariadb/moving-from-mysql/migrating-to-mariadb-from-mysql-obsolete-articles/README.md) (bearing that MariaDB is a MySQL fork, and is substantially more similar to MySQL than to other systems).


## Stored Procedures Documentation


The [Stored Procedures](../../../../server/server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md) capabilities of MariaDB Server are critical to producing large-scale applications. The current documentation lacks sufficient examples, and the examples warrant testing. Getting Started content would make this easier to adopt. MariaDB's implementation is based on ISO SQL/PSM.


## Getting Started with Connector/C and Connector/J


[MariaDB Connector/C](../../../../connectors/mariadb-connector-cpp/mariadb-connector-cpp-sample-application.md) and [MariaDB Connector/J](../../../../connectors/mariadb-connector-j/mariadb-connector-j-releases.md) provide the ability to access a MariaDB Server from applications built in C/C++ and Java, respectively. The current documentation for these connectors lacks Getting Started guides.


## Spider Documentation


The [Spider](../../../../server/reference/storage-engines/spider/spider-functions/spider_copy_tables.md) Storage Engine uses partitioning to provide data sharding through multiple servers. This task involves greatly expanding the existing documentation, including more detail about when to use Spider, basic usage tutorials, updating the [Spider Feature Matrix](../../../../server/reference/storage-engines/spider/spider-feature-matrix.md), detailed examples of the effects of the [server system variables](../../../../server/reference/storage-engines/spider/spider-system-variables.md) and [table system variables](../../../../server/reference/storage-engines/spider/spider-table-parameters.md), as well as the [Spider functions](../../../../server/reference/storage-engines/spider/spider-functions/README.md). You will also ensure changes in the most recent Spider releases are properly documented.


## Mroonga Documentation


[Mroonga](../../../../server/reference/storage-engines/mroonga/mroonga-user-defined-functions/mroonga_snippet_html.md) is a full text search storage engine based on Groonga, which is an open-source CJK-ready fulltext search engine using column base. This project involves greatly expanding the existing MariaDB documentation on the use of this storage engine.
A detailed tutorial and user guide, including examples of the various Mroonga [user-defined functions](../../../../server/reference/storage-engines/mroonga/mroonga-user-defined-functions/README.md), [system variables](../../../../server/reference/storage-engines/mroonga/mroonga-system-variables.md) and the effects of changing their settings, as well as the parser and [parser settings](../../../../server/reference/storage-engines/mroonga/mroonga-overview.md).


## Translation


You will choose a major language and ensure that a substantial subsection of the documentation is translated into that language. See [translations](https://mariadb.com/kb/en/translations/).


*Loaded from the [MariaDB issue tracker](https://jira.mariadb.org/issues/?jql=labels=gsdocs19)*
Loading Issues from [Jira](https://jira.mariadb.org/issues/?jql=labels=gsdocs19 and project=mdev order by key)
### %fields.summary%

%renderedFields.description%

| Details: | Mentor: |
| --- | --- |
| Details: | [%key%](https://jira.mariadb.org/browse/%key%) |
| Mentor: | %fields.assignee.displayName% |


<</style>>


# Suggest a Task


Do you have an idea of your own, not listed above? Do let us know!

