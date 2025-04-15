
# Running mariadb-tzinfo-to-sql with Ansible

For documentation about the `<code>mariadb-tzinfo-to-sql</code>` utility, see [mysql_tzinfo_to_sql](../../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_tzinfo_to_sql.md). This page is about running it using Ansible.


## Installing or Upgrading the Package


First, we should install `<code>mariadb-tzinfo-to-sql</code>` if it is available on our system. For example, to install it on Ubuntu, we can use this task. For other systems, use the proper module and package name.


```
- name: Update timezone info
  tags: [ timezone-update ]
  apt:
    name: tzdata
    state: latest
    install_recommends: no
  register: timezone_info
```

This task installs the latest version of the `<code>tzdata</code>`, unless it is already installed and up to date. We register the `<code>timezone_info</code>` variables, so we can only run the next task if the package was installed or updated.


We also specify a `<code>timezone-update</code>` tag, so we can apply the role to only update the timezone tables.


## Running the Script


The next task runs `<code>mariadb-tzinfo-to-sql</code>`.


```
- name: Move system timezone info into MariaDB
  tags: [ timezone-update ]
  shell: >
    mysql_tzinfo_to_sql /usr/share/zoneinfo \
      | grep -v "^Warning" \
      | mysql --database=mysql
  when: timezone_info.changed
```

We use the `<code>shell</code>` module to run the command. Running a command in this way is not idempotent, so we specify `<code>when: timezone_info.changed</code>` to only run it when necessary. Some warnings may be generated, so we pipe the output of `<code>mysql_tzinfo_to_sql</code>` to `<code>grep</code>` to filter warnings out.


## Using Galera


If we're using [MariaDB Galera Cluster](../../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-status-variables.md) we'll want to only update the timezone tables in one node, because the other nodes will replicate the changes. For our convenience, we can run this operation on the first node. If the nodes hostnames are defined in a list called `<code>cluster_hosts</code>`, we can check if the current node is the first in this way:


```
when: timezone_info.changed and inventory_hostname == cluster_hosts[0].hostname
```


Content initially contributed by [Vettabase Ltd](https://vettabase.com/).

