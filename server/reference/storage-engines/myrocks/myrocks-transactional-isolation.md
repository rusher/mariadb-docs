
# MyRocks Transactional Isolation

TODO:


* MyRocks uses snapshot isolation
* Support do READ-COMMITTED and REPEATABLE-READ
* SERIALIZABLE is not supported

  * There is no "Gap Locking" which makes Statement Based Replication unsafe (See MyRocks and Replication).

