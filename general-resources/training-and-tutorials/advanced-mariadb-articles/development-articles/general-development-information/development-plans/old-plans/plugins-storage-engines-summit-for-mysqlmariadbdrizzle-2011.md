
# Plugins & Storage Engines Summit for MySQL/MariaDB/Drizzle 2011

**Note:** This page is obsolete. The information is old, outdated, or otherwise currently incorrect. We are keeping the page for historical reasons only. **Do not** rely on the information in this article.



Continuing the tradition of having a storage engine summit (see notes from [2010](storage-engine-summit-2010.md)) after the [O'Reilly MySQL Conference](https://en.oreilly.com/mysql2011), this year it has been decided that the focus of the summit to be expanded.


# Location


The Facebook Campus, 1601 S. California Ave. Palo Alto, CA 94304.


For directions, use Google Maps. However, if you're at the O'Reilly MySQL Conference, you can take the light rail from the conference center to Mountain View and then Caltrain from Mountain View to the California Ave exit and then walk 1 mile to the Facebook campus.


# Date and Time


April 15 2011, from 10am - 4pm. Lunch will be served, courtesy of Facebook.


# Target Audience


Developers who are writing storage engines and plugins, knowing the plugin architecture of either MySQL, the extensions in MariaDB as well as the differences in Drizzle. User defined function (UDF) writers are welcome too.


Its expanded from just an invited audience of MySQL storage engine vendors this year.


Seats are limited to **twenty-four (24)** attendees.


# Who's Attending


If you're attending, **this is the signup form!** Please fill up your name, email address, company, and any other contact information you may have (like Facebook, Twitter). You will need to login to the Knowledgebase (OpenID login is available).


1. Michael "Monty" Widenius, monty at askmonty dot org, Monty Program Ab
1. Sergei Golubchik, serg at askmonty dot org, Monty Program Ab
1. Colin Charles, colin at montyprogram dot com, Monty Program Ab, [@bytebot](https://twitter.com/bytebot), [fb:bytebot](https://www.facebook.com/bytebot)
1. Zardosht Kasheff, zardosht at gmail dot com, Tokutek
1. Mark Callaghan, mdcallag at gmail dot com, Facebook
1. Paul McCullagh, paul dot mccullagh at primebase dot org, PrimeBase
1. Konstantin Osipov, kostja dot osipov at gmail dot com, Mail.Ru
1. Oleksandr "Sanja" Byelkin, sanja at askmonty dot org, Monty Program Ab
1. Bradley C. Kuszmaul, bradley@tokutek.com, Tokutek
1. Felix Schupp, felix.schupp@softmethod.de, BlackRay Data Engine, [fb:fschupp](https://facebook.com/fschupp)
1. Hartmut Holzgraefe, hartmut@php,net
1. Timour Katchaounov, timour at askmonty dot org, Monty Program Ab
1. praburam upendran, ramu@scaledb.com, scaledb
1. Rich Kelm, richard at sphinxsearch dot com, Sphinx Search
1. Antony T Curtis, atcurtis at gmail dot com, [Blizzard Entertainment](https://blizzard.com/) and [Open Query](https://openquery.com).
1. Daijiro MORI, morita at razil dot jp, Brazil Inc.
1. Tasuku SUENAGA, a at razil dot jp, Brazil Inc.
1. Kentoku SHIBA, kentokushiba at gmail dot com, WildGrowth
1. Peter Zaitsev, peter at percona dot com, Percona
1. Vadim Tkachenko, vadim at percona dot com, Percona
1. Louis Fahrberger, louis.fahrberger at infobright dot com, Infobright
1. Sergey Petrunya, psergey at askmonty.org, Monty Program Ab
1. Serge Frezefond
1. Igor Babaev, igor at askmonty.org Monty Program Ab
1. Volker Oboda, PrimeBase
1. Jeff Rothschild, Facebook
1. Rasmus Johansson, Monty Program Ab
1. Moshe Shadmon, ScaleDB
1. Chip Turner, Facebook
1. Domas Mituzas, Facebook/Wikipedia


# Notes


# Linking with the Storage Engine Advisory Board at Oracle


Volker Odoba - member of the storage engine advisory board at Oracle


* an explanation from Oracle as to why/if/when Oracle will take patches to extend the storage engine layer from the community
* its been mentioned that you might have to pay to be on the advisory board (i.e. you must be a customer)
* next meeting is at Oracle OpenWorld in October
* Schooner, Primebase, InnoDB, Infobright, Kickfire was there (now no longer since they do not exist)


# Topics


* HBase storage engine layer to work with dynamic columns
* Discovery (Shared metadata)
* Materialised views
* Online ALTER TABLE
* Parallel replication (not SE, but a related topic)
* Group commit
* Parallel execution
* Fulltext search for every storage engine
* Cross-engine Online Backup
* Finish off server definition interface for FederatedX. Make it generic enough so that Spider can also use it.
* Pluggable data types
* Indexing/Dynamic Functions
* Fast load


## HBase by Chip Turner


Distributed key value store. Single index on a given table. Distributed servers each serving a row, multiple rows. Lexicographically sorted. No C API, there's a proxy API and Chip is fixing that now. Current protocol is serialized Java. Eventually each HBase server will speak Thrift. See [ThriftApi](https://wiki.apache.org/hadoop/Hbase/ThriftApi) and [](https://incubator.apache.org/thrift/)


Index Condition Pushdown and MRR are useful here.


Messages is a HBase application.


## Index Condition Pushdown


* idx_cond_push()
* opt_index_condition_pushdown.cc
* EXPLAIN will say Using index condition
* Don't copy HA_NDBCLUSTER::COND_PUSH() since it is not done in a seinsble way. Much smarter implementations are possible with easy code - psergey
* This will be continued in discussion via email (sphinx, infobright, tokutek, spider, oqgraph)

  * TODO: Timour will create a Worklog entry and involve appropriate attendees


## Discovery


Cluster with many MySQL servers connected to it. It was originally designed for MySQL Cluster.


* TODO: Serg to write an explanation here. Session led by him.


## Loadable Indexes


* TODO: Paul, Kentoku, Richard, and Serg to discuss further
* Fulltext search
* Dynamic indexing method to existing storage engines are required. Do you want to store the data and index in the engine? It is not necessary (Kentoku). Want to implement just an index, not a storage engine. Storage format might be completely different.
* Practical use of having indexes for all engines? GIS.


## Parallel Execution


* Read in two threads, will that be a problem for the storage engine? Two handlers within the same transaction ID calling in. Could just be a switch for the storage engine. Same THD in two different threads.


## Online Backup


* Status hasn't changed since last year after Oracle cancelled it. No work has been done on this.
* Needs about 6 months sponsorship of one person's salary to get such a feature enabled
* Mark doesn't like running hot backup in the server and thinks its not generally a good idea. He prefers using xtrabackup, a separate process from the server. xtrabackup is a transactional log reader (Domas has joined us and is now enlightening everyone on xtrabackup features).

  * Replication team and this meeting are the only folk that ask for this
* MyISAM has implemented backups twice now, and it has never made it outside
* Focus on what will gain you traction. Look on Percona Server. It just focuses on what customers want.


## Pluggable/abstract data types


* UUID, IPv4/IPv6 address, complex numbers, etc.


## Online ALTER


* Zardosht has an example from MySQL Cluster. He likes the implementation in MySQL Cluster 7.1. They have a different alter table API, and they've ported this to TokuDB with support for MySQL 5.1 and [MariaDB 5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1)/5.2.
* Wait and see the work that Oracle is doing?
* Old 6.0.3 - online alter and metadata alter - serg checked
* Zardosht's patch will work with [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3), but once there's [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) based on MySQL 5.5 he's terribly worried about porting


## Group commit


* See slides for Monty+Kristian's talk


CC BY-SA / Gnu FDL

