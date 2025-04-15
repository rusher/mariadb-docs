
# Merging New XtraDB Releases (obsolete)

**Note:** This page is obsolete. The information is old, outdated, or otherwise currently incorrect. We are keeping the page for historical reasons only. **Do not** rely on the information in this article.



### Background


Percona used to maintain XtraDB as a patch series against the InnoDB plugin. This affected how we started merging XtraDB in.


Now Percona maintains a normal source repository on launchpad (`<code class="highlight fixed" style="white-space:pre-wrap">lp:percona-server</code>`). But we continue to merge the old way to preserve the history of our changes.


### Merging


There used to be a `<code class="highlight fixed" style="white-space:pre-wrap">lp:percona-xtradb</code>` tree, that we were merging from as:


```
bzr merge lp:percona-xtradb
```

Now we have to maintain our own XtraDB-5.5 repository to merge from. It is `<code class="highlight fixed" style="white-space:pre-wrap">lp:~maria-captains/maria/xtradb-mergetree-5.5</code>`. Follow the procedures as described in [Merging with a merge tree](merging-with-a-merge-tree.md) to merge from it.

