# Compiling with the InnoDB Plugin from Oracle

From [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102), MariaDB uses InnoDB as the default storage engine. Before [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102), MariaDB came by default with [XtraDB](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/README.md), an enhanced version of the InnoDB plugin that comes from Oracle.

If you want to use Oracle's InnoDB plugin, then you need to compile MariaDB and**not** specify `--without-plugin-innodb_plugin` when\
configuring. For example, a simple `./configure` without\
any options will do.

When the InnoDB plugin is compiled, the innodb\_plugin test suite will test the\
InnoDB plugin in addition to xtradb:

```
./mysql-test-run --suite=innodb_plugin
```

To use the innodb\_plugin instead of xtradb you can do (for [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)):

```
mysqld --ignore-builtin-innodb --plugin-load=innodb=ha_innodb.so \
--plugin_dir=/usr/local/mysql/lib/mysql/plugin
```

## See Also

[replacing-builtin-innodb.html](https://dev.mysql.com/doc/refman/5.1/en/replacing-builtin-innodb.html)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
