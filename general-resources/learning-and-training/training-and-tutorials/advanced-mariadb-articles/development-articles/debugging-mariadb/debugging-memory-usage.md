
# Debugging Memory Usage

Debugging memory usage on CentOS 7.


This page describes how to debug MariaDB's memory usage. It uses CentOS 7 but can be applied to other systems as well.


The idea is to employ Google PerfTools: [heapprofile.html](https://gperftools.github.io/gperftools/heapprofile.html)


On CentOS :


```
sudo yum install gperftools 
service mariadb stop
systemctl edit mariadb
```

This will open an editor.


Add this content and close the file:


```
[Service]
Environment="HEAPPROFILE=/tmp/heap-prof-1"
Environment="HEAP_PROFILE_ALLOCATION_INTERVAL=10737418240"
Environment="HEAP_PROFILE_INUSE_INTERVAL=1073741824"
Environment="LD_PRELOAD=/usr/lib64/libtcmalloc.so.4"
```

Then run


```
service mariadb start
```

Then, run the workload. When memory consumption becomes large enough, ruh


```
ls -la /tmp/heap-prof-*
```

This should show several files.


Copy away the last one of them:


```
cp /tmp/heap-prof-1.0007.heap .
```

Then, run


```
pprof --dot /usr/sbin/mysqld heap-prof-1.0007.heap  > 7.dot
```

(Note: this produces a lot of statements like `<code>/bin/addr2line: Dwarf Error: ... </code>`. Is this because it cannot find locations from the plugin .so files in mariadbd? Anyhow, this is not a showstopper at the moment)


Then, please send us the 7.dot file.

