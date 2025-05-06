
# Plans for 10.3


No new features will be added to [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103). If you wish to contribute new features to the latest development release, see [Plans for MariaDB 10.5](plans-for-mariadb-105.md).


"[What is MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)" shows all features implemented for 10.3.


## [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)


The following features were discussed at the 2016 MariaDB Developer's Meeting for consideration in [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103). See [Thoughts on MariaDB Server 10.3 from MariaDB Developers Meeting in Amsterdam, part 1](https://mariadb.org/thoughts-mariadb-server-10-3-mariadb-developers-meeting-amsterdam-part-1/).


* Hidden Columns
* Long unique constraints
* SQL based CREATE AGGREGATE FUNCTION
* Now it looks like one step ahead has been made with the implementation of a Pluggable Data Type API. It still exists in a separate branch, but it is now planned for inclusion in MariaDB Server 10.3. On top of the API the idea is to build User Defined Types according to the SQL Standard.
* Better support for CJK (Chinese, Japanese, and Korean) languages. The idea is to include the ngram full-text parser and MeCab full-text parser plugins. Also the GB 18030 standard for Chinese charsets is on the radar for 10.3.
* On the storage engine side MyRocks will be included in 10.2, which will open MyRocks to a wider audience. It’s obvious that it will need work during 10.3 timeframe to grow in maturity. Another interesting storage engine discussed during the last few years is Spider, an engine that provides a sharding solution for databases. Although Spider already exists in MariaDB Server, there is a set of patches that needs to be incorporated on the server side to improve functionality and performance. These patches can be found in [MDEV-7698](https://jira.mariadb.org/browse/MDEV-7698).


### InnoDB


* In MySQL 8.0 there are a couple of interesting new features for InnoDB that are interesting for MariaDB as well. The timelines of 10.3 and 8.0 will partially determine whether these will be in 10.3.
* InnoDB deadlock detect
* The new information schema table.
* Lock wait policy
* Persistent autoincrement


### Compatibility


* Support for SEQUENCE
* Addition of a PL/SQL parser
* Support for INTERSECT
* Support for EXCEPT


### JIRA


We manage our development plans in JIRA, so the definitive list will be there. [This search](https://jira.mariadb.org/issues/?jql=project+%3D+MDEV+AND+issuetype+%3D+Task+AND+fixVersion+in+%2810.3.0%2C+10.3%29+ORDER+BY+priority+DESC) shows what we **currently** plan for 10.3. It shows all tasks with the **Fix-Version** being 10.3. Not all these tasks will really end up in 10.3, but tasks with the "red" priorities have a much higher chance of being done in time for 10.3. Practically, you can think of these tasks as "features that **will** be in 10.3". Tasks with the "green" priorities probably won't be in 10.3. Think of them as "bonus features that would be **nice to have** in 10.3".


## See Also


* [Current tasks for 10.3](https://jira.mariadb.org/issues/?jql=project%20%3D%20MDEV%20AND%20issuetype%20%3D%20Task%20AND%20fixVersion%20in%20(10.3.0%2C%2010.3)%20ORDER%20BY%20priority%20DESC)
* [10.3 Features/fixes by vote](https://jira.mariadb.org/issues/?jql=project%20%3D%20MDEV%20AND%20fixVersion%20%3D%2010.3%20ORDER%20BY%20votes%20DESC)
* [What is MariaDB 10.3?](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)
* [What is MariaDB 10.2?](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102)
* [What is MariaDB 10.1?](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1)
* [What is MariaDB 10.0?](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

