
# Merging with a Merge Tree

If you have a [merge tree](creating-a-new-merge-tree.md), you merge into MariaDB as follows:


1. MariaDB merge trees are in the [mergetrees](https://github.com/MariaDB/mergetrees) repository. Add it as a new remote:

```
git remote add merge https://github.com/MariaDB/mergetrees
```
1. Check out the branch you want to update and merge, for example:

```
git checkout merge-innodb-5.6
```
1. delete everything in the branch
1. download the latest released source tarball, unpack it, copy files into the repository:

  * for InnoDB-5.6: use the content of the `<code>storage/innobase/</code>` of the latest MySQL 5.6 source release tarball.
  * for performance schema 5.6: use `<code>storage/perfschema</code>`, `<code>include/mysql/psi</code>`, `<code>mysql-test/suite/perfschema</code>`, and `<code>mysql-test/suite/perfschema_stress</code>` from the latest MySQL 5.6 source release tarball.
  * for SphinxSE: use `<code>mysqlse/</code>` subdirectory from the latest Sphinx source release tarball.
  * for XtraDB: use the content of the `<code>storage/innobase/</code>` of the latest Percona-Server source release tarball (5.5 or 5.6 as appropriate).
  * for pcre: simply unpack the latest pcre release source tarball into the repository, rename `<code>pcre-X-XX/</code>` to `<code>pcre</code>`.
1. Now `<code>git add .</code>`, `<code>git commit</code>` (use the tarball version as a comment), `<code>git push</code>`
1. merge this branch into MariaDB
1. Sometimes after a merge, some changes may be needed:

  * for performance schema 5.6: update `<code>storage/perfschema/ha_perfschema.cc</code>`, plugin version under `<code>maria_declare_plugin</code>`.
  * for InnoDB-5.6: update `<code>storage/innobase/include/univ.i</code>`, setting `<code>INNODB_VERSION_MAJOR</code>`, `<code>INNODB_VERSION_MINOR</code>`, `<code>INNODB_VERSION_BUGFIX</code>` to whatever MySQL version you were merging from.
  * for XtraDB-5.5: update `<code>storage/xtradb/include/univ.i</code>`, setting `<code>PERCONA_INNODB_VERSION</code>`, `<code>INNODB_VERSION_STR</code>` to whatever Percona-Server version you were merging from.
  * for XtraDB-5.6: update `<code>storage/xtradb/include/univ.i</code>`, setting `<code>PERCONA_INNODB_VERSION</code>`, `<code>INNODB_VERSION_MAJOR</code>`, `<code>INNODB_VERSION_MINOR</code>`, `<code>INNODB_VERSION_BUGFIX</code>` to whatever Percona-Server version you were merging from.

