
# Aria Group Commit

Since [MariaDB 5.2](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md), the [Aria storage engine](../s3-storage-engine/aria_s3_copy.md) has included a feature to group commits to speed up concurrent threads doing many inserts into the same or different Aria tables.


By default, group commit for Aria is turned off. It is controlled by the 
[aria_group_commit](aria-system-variables.md) and [aria_group_commit_interval](aria-system-variables.md) system variables.


Information on setting server variables can be found on the [Server System Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) page.


## Terminology


* A `<code>commit</code>` is `<code>flush of logs</code>` followed by a sync.
* `<code>sent to disk</code>` means written to disk but not sync()ed,
* `<code>flushed</code>` mean sent to disk and synced().
* `<code>LSN</code>` means log serial number. It's refers to the position in the transaction log.


## Non Group commit logic (aria_group_commit="none")


The thread which first started the `<code>commit</code>` is performing the actual flush of logs. Other threads set the new goal (LSN)
of the next pass (if it is maximum) and wait for the pass end or just wait for the pass end.


The effect of this is that a flush (write of logs + sync) will save all data for all threads/transactions that have been waiting since the last flush.


## If hard group commit is enabled (aria_group_commit="hard")


### If hard commit and aria_group_commit_interval=0


The first thread sends all changed buffers to disk. This is repeated as long as there are new LSNs added. The process can not loop
forever because we have a limited number of threads and they will wait for the data to be synced.


Pseudo code:


```
do
   send changed buffers to disk
 while new_goal
sync
```

### If hard commit and aria_group_commit_interval > 0


If less than rate microseconds has passed since the last sync, then after buffers have been sent to disk, wait until rate microseconds has passed since last sync, do sync and return.
This ensures that if we call sync infrequently we don't do any waits.


## If soft group commit is enabled (aria_group_commit="soft")


Note that soft group commit should only be used if you can afford to lose a few rows if your machine shuts down hard (as in the case of a power failure).


Works like in `<code>non group commit'</code>` but the thread doesn't do any real sync(). If aria_group_commit_interval is not zero, the sync() will be performed by a service thread with the given rate when needed (new LSN appears). If aria_group_commit_interval is zero, there will be no sync() calls.


## Code


The code for this can be found in storage/maria/ma_loghandler.c::translog_flush()

