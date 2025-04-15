# How do I migrate a MySQL database to Amazon RDS?

[Amazon Relational Database Service (Amazon RDS)](http://aws.amazon.com/rds/) is part of the Amazon Web Services, that allows one to setup and run a relational database in the cloud. It supports running MariaDB in addition to MySQL, PostgreSQL, and other common relational databases.

Gee-Hwan Chuang of Listia has written a guide titled [Moving a Production MySQL Database to Amazon RDS with Minimal Downtime](http://geehwan.posterous.com/moving-a-production-mysql-database-to-amazon). He recommends using [mysqldump](../../../clients-and-utilities/legacy-clients-and-utilities/mysqldumpslow.md).