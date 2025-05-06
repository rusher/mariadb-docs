
# MariaDB Plans - Replication

**Note:** This page is obsolete. The information is old, outdated, or otherwise currently incorrect. We are keeping the page for historical reasons only. **Do not** rely on the information in this article.



We are discussing points for the replication part of the MariaDB roadmap.


So far discussed:


* Replication filters, like --replicate-do-db and friends, need to be
 possible to change dynamically, without having to restart the
 server. Having to stop the slave should ideally also not be needed, but is
 less of a problem. (complete)


* Transactional storage of slave state, rather than file-based master.info 
 and relay-log.info . So the slave can recover consistently after a crash. (complete)


* Global transaction ID, so the slave state becomes recoverable, and
 facilitate automatic moving a slave to a new master across multi-level
 hierarchies. (complete)


* Support in global transaction ID for master_pos_wait() (complete)


* Hooks around rotation of the binlog, so user can configure shell commands
 when a new log is started and when it is ended. The command must be run
 asynchroneously, and get the old and new log file name as arguments.


* Sending of heartbeats from master to slaves, so slaves starting up can know
 in finite time where the master is.


* Replication APIs, as per [MWL#107](https://askmonty.org/worklog/?tid=107)

  * Most important [MWL#120](https://askmonty.org/worklog/?tid=120) and [MWL#133](https://askmonty.org/worklog/?tid=133), for obtaining and applying events.
  * Then a mechanism for prioritising transactions.


CC BY-SA / Gnu FDL

