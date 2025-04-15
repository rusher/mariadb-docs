
# Stuff in MySQL 5.6

This is SergeyP's list of patches in MySQL 5.6 that he has found interesting. It is not a full list of interesting features or anything like that


[WL#6071](https://askmonty.org/worklog/?tid=6071): Inline tmp tables into the nested loops algorithm. (Evgen, 2012-05-31)


[WL#4443](https://askmonty.org/worklog/?tid=4443) - Prune partition locks (public WL) (April 2012)


[WL#4897](https://askmonty.org/worklog/?tid=4897): Add EXPLAIN INSERT/UPDATE/DELETE (2011)


* EXPLAIN EXTENDED UPDATE doesn't print warnings...


[WL#5906](https://askmonty.org/worklog/?tid=5906) read before write removal (RBWR) (2012-04)


* used by NDB only. (Bug#37153 NDB Cluster reports affected rows incorrectly, etc)
* but the SQL layer still does reads before doing writes. This code is not suitable for update-without-reads.
* The main idea is that we do [deleted|updated]= table->file->end_read_removal(); at the end. This only counts #of affected rows.

