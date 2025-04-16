
# HANDLER

The `HANDLER` statements give you direct access to reading rows from the storage engine. This is much faster than normal access through [SELECT](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) as there is less parsing involved and no optimizer involved.


You can use [prepared statements](../../sql-statements/prepared-statements/README.md) for `HANDLER READ`, which should give you a speed comparable to [HandlerSocket](../handlersocket/handlersocket-external-resources.md). Also see Yoshinori Matsunobu's blog post [Using MySQL as a NoSQL - A story for exceeding 750,000 qps on a commodity server](https://yoshinorimatsunobu.blogspot.com/2010/10/using-mysql-as-nosql-story-for.html).

