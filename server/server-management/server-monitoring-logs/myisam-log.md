
# MyISAM Log

The MyISAM log records all changes to [MyISAM](../../ref/storage-engines/myisam-storage-engine/myisam-system-variables.md) tables. It is not enabled by default. To enable it, start the server with the [--log-isam](../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) option, for example:


```
--log-isam=myisam.log
```

The *isam* instead of *myisam* above is not a typo - it's a legacy from when the predecessor to the MyISAM format, called ISAM. The option can be used without specifying a filename, in which case the default, *myisam.log* is used.


To process the contents of the log file, use the [myisamlog](../../clients-and-utilities/myisam-clients-and-utilities/myisamlog.md) utility.

