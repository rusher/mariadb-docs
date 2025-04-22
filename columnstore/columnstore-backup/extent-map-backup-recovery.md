
# Extent Map Backup & Recovery

The extent map is a critical component of MariaDB Enterprise ColumnStore. It provides a logical range for partitioning, eliminating the need for traditional database performance optimizations like indexing, manual table partitioning, materialized views, and summary tables. Therefore, regular backups of the extent map are crucial for system recovery. This document outlines the purpose, backup, and restore procedures for the extent map files when using shared local storage.


## Purpose


ColumnStore's extent map is a smart structure that underpins its performance. By providing a logical partitioning scheme, it avoids the overhead associated with indexing and other common row-based database optimizations.


The primary node in a ColumnStore cluster holds the master copy of the extent map. Upon system startup, this master copy is read into memory and then replicated to all other participating nodes for high availability and disaster recovery. Nodes keep the extent map in memory for rapid access during query processing. As data within extents is modified, these updates are broadcast to all participating nodes to maintain consistency.


If the master copy of the extent map becomes corrupted, the entire system could become unusable, potentially leading to data loss. Having a recent backup of the extent map allows for a much faster recovery compared to reloading the entire database in such a scenario.


## Backup


**Note**: MariaDB recommends implementing regular backups to ensure data integrity and recovery. A common default is to back up every 3 hours and retain backups for at least 10 days.


To backup the extent map files:


1. Stop ColumnStore:
```
$ mcs cluster stop
```
1. Copy the files:
```
$ rsync -av /var/lib/columnstore/data1/systemFiles/dbrm/ /BACKUP_PATH/extent_map/
```
1. Restart ColumnStore:
```
$ mcs cluster start
```


## Restore


To restore the extent map files:


1. Find the active BRM file version by checking the `BRM_saves_current` file:



```
$ cat /var/lib/columnstore/data1systemFiled/dbrm/BRM_saves_current
```

```
BRM_saves
```


If the output above is not `BRM_saves`, then it might have a suffix of `A` or `B`, which means that an alternate extent map file is being used.

2. Compare the file sizes of each BRM file version:



```
$ ls -la /var/lib/columnstore/data1/systemFiles/dbrm/
```


```
-rwxr-xr-t. 1 mysql mysql    4748 Dec 10 16:14 BRM_savesA_em
-rwxr-xr-t. 1 mysql mysql      12 Dec 10 16:14 BRM_savesA_vbbm
-rwxr-xr-t. 1 mysql mysql       8 Dec 10 16:14 BRM_savesA_vss
-rwxr-xr-t. 1 mysql mysql    4652 Dec 10 16:14 BRM_savesB_em
-rwxr-xr-t. 1 mysql mysql      12 Dec 10 16:14 BRM_savesB_vbbm
-rwxr-xr-t. 1 mysql mysql       8 Dec 10 16:14 BRM_savesB_vss
-rwxr-xr-t. 1 mysql mysql      10 Dec 30 15:34 BRM_saves_current
-rwxr-xr-t. 1 mysql mysql   33644 Dec 30 15:34 BRM_saves_em
-rwxr-xr-t. 1 mysql mysql     261 Dec 30 19:20 BRM_saves_journal
-rwxr-xr-t. 1 mysql mysql      36 Dec 30 15:34 BRM_saves_vbbm
-rwxr-xr.t. 1 mysql mysql       8 Dec 30 15:34 BRM_saves_vss
-rwxr-xr-t. 1 mysql mysql 2099204 Dec 28 16:21 oidbitmap
-rwxr-xr.t. 1 mysql mysql      12 Dec 30 19:20 SMTxnID
-rwxr-xr-t. 1 mysql mysql       4 Dec 30 19:20 tablelocks
```

If you compare the sizes of the three `_em` files (`BRM_saves_em, BRM_savesA_em, and BRM_savesB_em`), you can see that the base version (`BRM_saves_em`) is largest. This is also the version that was shown in the `BRM_saves_current` file, so this is the active one. This is what we expect as its being appended to with new object and summary information. If the A or B version is larger, then the system might have been using a backup copy of the extent map for some time.

3. Determine which BRM file to restore:
This depends on a lot of factors, such as the file sizes, file modification timestamps, and the specific issue being troubleshooted.
Usually, you want to restore the active BRM files. If `BRM_saves_journal` is larger than 0 bytes and the `BRM_saves_current` file includes the `A` or `B` suffix, you might want to restore an alternate BRM file version. Ask MariaDB Support for assistance.


4. Stop ColumnStore:



```
$ mcs cluster stop
```


5. Clear Shared Memory



```
$clearShm
```


6. Restore the BRM files:



```
$ rsync -av /BACKUP_PATH/extent_map/BRM_saves_em /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_em
$ rysnc -av /BACKUP_PATH/extent_map/BRM_saves_vbbm /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_vbbm
$ rysnc -av /BACKUP_PATH/extent_map/BRM_saves_vss /var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves_vss
```

If you are restoring the A or B versions of the BRM files, remove the suffix during the restore.

7. If the `BRM_saves_current` file contains the `A` or `B``suffix after ``BRM_saves`, edit the file so that it no longer has the suffix:



```
BRM_saves
```


8. Restart ColumnStore:



```
$ mcs cluster start
```

