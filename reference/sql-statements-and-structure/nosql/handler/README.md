# HANDLER

The `HANDLER` statements give you direct access to reading rows from the storage engine. This is much faster than normal access through [SELECT](../../../../server-usage/replication-cluster-multi-master/standard-replication/selectively-skipping-replication-of-binlog-events.md) as there is less parsing involved and no optimizer involved.

You can use [prepared statements](/en/prepared-statements/) for `HANDLER READ`, which should give you a speed comparable to [HandlerSocket](../handlersocket/handlersocket-external-resources.md). Also see Yoshinori Matsunobu's blog post [Using MySQL as a NoSQL - A story for exceeding 750,000 qps on a commodity server](http://yoshinorimatsunobu.blogspot.com/2010/10/using-mysql-as-nosql-story-for.html).