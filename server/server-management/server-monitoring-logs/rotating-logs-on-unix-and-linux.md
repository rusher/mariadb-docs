
# Rotating Logs on Unix and Linux


Unix and Linux distributions offer the `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` utility, which makes it very easy to rotate log files. This page will describe how to configure log rotation for the [error log](error-log.md), [general query log](general-query-log.md), and the [slow query log](slow-query-log/slow-query-log-overview.md).


## Configuring Locations and File Names of Logs


The first step is to configure the locations and file names of logs. To make the log rotation configuration easier, it can be best to put these logs in a dedicated log directory.


We will need to configure the following:


* The [error log](error-log.md) location and file name is configured with the `<code>[log_error](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_error)</code>` system variable.
* The [general query log](general-query-log.md) location and file name is configured with the `<code>[general_log_file](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#general_log_file)</code>` system variable.
* The [slow query log](slow-query-log/slow-query-log-overview.md) location and file name is configured with the `<code>[slow_query_log_file](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log_file)</code>` system variable.


If you want to enable the [general query log](general-query-log.md) and [slow query log](slow-query-log/slow-query-log-overview.md) immediately, then you will also have to configure the following:


* The [general query log](general-query-log.md) is enabled with the `<code>[general_log](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#general_log)</code>` system variable.
* The [slow query log](slow-query-log/slow-query-log-overview.md) is enabled with the `<code>[slow_query_log](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log)</code>` system variable.


These options can be set in a server [option group](../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example, if we wanted to put our log files in `<code>/var/log/mysql/</code>`, then we could configure the following:


```
[mariadb]
...
log_error=/var/log/mysql/mariadb.err
general_log
general_log_file=/var/log/mysql/mariadb.log
slow_query_log
slow_query_log_file=/var/log/mysql/mariadb-slow.log
long_query_time=5
```

We will also need to create the relevant directory:


```
sudo mkdir /var/log/mysql/
sudo chown mysql:mysql /var/log/mysql/
sudo chmod 0770 /var/log/mysql/
```

If you are using [SELinux](../../security/securing-mariadb/selinux.md), then you may also need to set the SELinux context for the directory. See [SELinux: Setting the File Context for Log Files](../../security/securing-mariadb/selinux.md#setting-the-file-context-for-log-files) for more information. For example:


```
sudo semanage fcontext -a -t mysqld_log_t "/var/log/mysql(/.*)?"
sudo restorecon -Rv /var/log/mysql
```

After MariaDB is [restarted](https://mariadb.com/kb/en/), it will use the new log locations and file names.


## Configuring Authentication for Logrotate


The `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` utility needs to be able to authenticate with MariaDB in order to flush the log files.


The easiest way to allow the `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` utility to authenticate with MariaDB is to configure the `<code>root@localhost</code>` user account.



#### Note

The `<code>root@localhost</code>` user account is configured to use unix_socket authentication by default


The `<code>root@localhost</code>` user account can be altered to use [unix_socket](../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) authentication with the [ALTER USER](../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/alter-user.md) statement. For example:


```
ALTER USER 'root'@'localhost' IDENTIFIED VIA unix_socket;
```

<</product>>


## Configuring Logrotate


At this point, we can configure the `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` utility to rotate the log files.


On many systems, the primary `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` configuration file is located at the following path:


* `<code>/etc/logrotate.conf</code>`


And the `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` configuration files for individual services are located in the following directory:


* `<code>/etc/logrotate.d/</code>`


We can create a `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` configuration file for MariaDB by executing the following command in a shell:


```
$ sudo tee /etc/logrotate.d/mariadb <<EOF
/var/log/mysql/* {
        su mysql mysql
        missingok
        create 660 mysql mysql
        notifempty
        daily
        minsize 1M # only use with logrotate >= 3.7.4
        maxsize 100M # only use with logrotate >= 3.8.1
        rotate 30
        # dateext # only use if your logrotate version is compatible with below dateformat
        # dateformat .%Y-%m-%d-%H-%M-%S # only use with logrotate >= 3.9.2
        compress
        delaycompress
        sharedscripts 
        olddir archive/
        createolddir 770 mysql mysql # only use with logrotate >= 3.8.9
    postrotate
        # just if mysqld is really running
        if test -x /usr/bin/mysqladmin && \
           /usr/bin/mysqladmin ping &>/dev/null
        then
           /usr/bin/mysqladmin --local flush-error-log \
              flush-engine-log flush-general-log flush-slow-log
        fi
    endscript
}
EOF
```

You may have to modify this configuration file to use it on your system, depending on the specific version of the `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` utility that is installed. See the description of each configuration directive below to determine which `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` versions support that configuration directive.


Each specific configuration directive does the following:


* `<code>missingok</code>`: This directive configures it to ignore missing files, rather than failing with an error.
* `<code>create 660 mysql mysql</code>`: This directive configures it to recreate the log files after log rotation with the specified permissions and owner.
* `<code>notifempty</code>`: This directive configures it to skip a log file during log rotation if it is empty.
* `<code>daily</code>`: This directive configures it to rotate each log file once per day.
* `<code>minsize 1M</code>`: This directive configures it to skip a log file during log rotation if it is smaller than 1 MB. This directive is only available with `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` 3.7.4 and later.
* `<code>maxsize 100M</code>`: This directive configures it to rotate a log file more frequently than daily if it grows larger than 100 MB. This directive is only available with `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` 3.8.1 and later.
* `<code>rotate 30</code>`: This directive configures it to keep 30 old copies of each log file.
* `<code>dateext</code>`: This directive configures it to use the date as an extension, rather than just a number. This directive is only available with `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` 3.7.6 and later.
* `<code>dateformat .%Y-%m-%d-%H-%M-%S</code>`: This directive configures it to use this date format string (as defined by the format specification for `<code>[strftime](https://linux.die.net/man/3/strftime)</code>`) for the date extension configured by the `<code>dateext</code>` directive. This directive is only available with `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` 3.7.7 and later. Support for `<code>%H</code>` is only available with `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` 3.9.0 and later. Support for `<code>%M</code>` and `<code>%S</code>` is only available with `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` 3.9.2 and later.
* `<code>compress</code>`: This directive configures it to compress the log files with `<code>[gzip](https://linux.die.net/man/1/gzip)</code>`.
* `<code>delaycompress</code>`: This directive configures it to delay compression of each log file until the next log rotation. If the log file is compressed at the same time that it is rotated, then there may be cases where a log file is being compressed while the MariaDB server is still writing to the log file. Delaying compression of a log file until the next log rotation can prevent race conditions such as these that can happen between the compression operation and the MariaDB server's log flush operation.
* `<code>olddir archive/</code>`: This directive configures it to archive the rotated log files in `<code>/var/log/mysql/archive/</code>`.
* `<code>createolddir 770 mysql mysql</code>`: This directive configures it to create the directory specified by the `<code>olddir</code>` directive with the specified permissions and owner, if the directory does not already exist. This directive is only available with `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` 3.8.9 and later.
* `<code>sharedscripts</code>`: This directive configures it to run the `<code>postrotate</code>` script just once, rather than once for each rotated log file.
* `<code>postrotate</code>`: This directive configures it to execute a script after log rotation. This particular script executes the [mariadb-admin](../../clients-and-utilities/mariadb-admin.md) utility, which executes the [FLUSH](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) statement, which tells the MariaDB server to flush its various log files. When MariaDB server flushes a log file, it closes its existing file handle and reopens a new one. This ensure that MariaDB server does not continue writing to a log file after it has been rotated. This is an important component of the log rotation process.


If our system does not have `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` 3.8.9 or later, which is needed to support the `<code>createolddir</code>` directive, then we will also need to create the relevant directory specified by the `<code>olddir</code>` directive:


```
sudo mkdir /var/log/mysql/archive/
sudo chown mysql:mysql /var/log/mysql/archive/
sudo chmod 0770 /var/log/mysql/archive/
```

## Testing Log Rotation


We can test log rotation by executing the `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` utility with the `<code>--force</code>` option. For example:


```
sudo logrotate --force /etc/logrotate.d/mariadb
```

Keep in mind that under normal operation, the `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` utility may skip a log file during log rotation if the utility does not believe that the log file needs to be rotated yet. For example:


* If you set the `<code>notifempty</code>` directive mentioned above, then it will be configured to skip a log file during log rotation if the log file is empty.
* If you set the `<code>daily</code>` directive mentioned above, then it will be configured to only rotate each log file once per day.
* If you set the `<code>minsize 1M</code>` directive mentioned above, then it will be configured to skip a log file during log rotation if the log file size is smaller than 1 MB.


However, when running tests with the `<code>--force</code>` option, the `<code>[logrotate](https://linux.die.net/man/8/logrotate)</code>` utility does not take these options into consideration.


After a few tests, we can see that the log rotation is indeed working:


```
$ sudo ls -l /var/log/mysql/archive/
total 48
-rw-rw---- 1 mysql mysql  440 Mar 31 15:31 mariadb.err.1
-rw-rw---- 1 mysql mysql  138 Mar 31 15:30 mariadb.err.2.gz
-rw-rw---- 1 mysql mysql  145 Mar 31 15:28 mariadb.err.3.gz
-rw-rw---- 1 mysql mysql 1007 Mar 31 15:27 mariadb.err.4.gz
-rw-rw---- 1 mysql mysql 1437 Mar 31 15:32 mariadb.log.1
-rw-rw---- 1 mysql mysql  429 Mar 31 15:31 mariadb.log.2.gz
-rw-rw---- 1 mysql mysql  439 Mar 31 15:28 mariadb.log.3.gz
-rw-rw---- 1 mysql mysql  370 Mar 31 15:27 mariadb.log.4.gz
-rw-rw---- 1 mysql mysql 3915 Mar 31 15:32 mariadb-slow.log.1
-rw-rw---- 1 mysql mysql  554 Mar 31 15:31 mariadb-slow.log.2.gz
-rw-rw---- 1 mysql mysql  569 Mar 31 15:28 mariadb-slow.log.3.gz
-rw-rw---- 1 mysql mysql  487 Mar 31 15:27 mariadb-slow.log.4.gz
```

## Logrotate in Ansible


Let's see an example of how to configure logrotate in Ansible.


First, we'll create a couple of tasks in our playbook:


```
- name: Create mariadb_logrotate_old_dir
  file:
    path: "{{ mariadb_logrotate_old_dir }}"
    owner: mysql
    group: mysql
    mode: '770'
    state: directory

- name: Configure logrotate
  template:
    src: "../templates/logrotate.j2"
    dest: "/etc/logrotate.d/mysql"
```

The first task creates a directory to store the old, compressed logs, and set proper permissions.


The second task uploads logrotate configuration file into the proper directory, and calls it `<code>mysql</code>`. As you can see the original name is different, and it ends with the `<code>.j2</code>` extension, because it is a Jinja 2 template.


The file will look like the following:


```
{{ mariadb_log_dir }}/* {
        su mysql mysql
        missingok
        create 660 mysql mysql
        notifempty
        daily
        minsize 1M {{ mariadb_logrotate_min_size }}
        maxsize 100M {{ mariadb_logrotate_max_size }}
        rotate {{ mariadb_logrotate_old_dir }}
        dateformat .%Y-%m-%d-%H-%M-%S # only use with logrotate >= 3.9.2
        compress
        delaycompress
        sharedscripts 
        olddir archive/
        createolddir 770 mysql mysql # only use with logrotate >= 3.8.9
    postrotate
        # just if mysqld is really running
        if test -x /usr/bin/mysqladmin && \
           /usr/bin/mysqladmin ping &>/dev/null
        then
           /usr/bin/mysqladmin --local flush-error-log \
              flush-engine-log flush-general-log flush-slow-log
        fi
    endscript
}
```

The file is very similar to the file shown above, which is obvious because we're still uploading a logrotate configuration file. Ansible is just a tool we've chosen to do this.


However, both in the tasks and in the template, we used some variables. This allows to use different paths and rotation parameters for different hosts, or host groups.


If we have a group host called `<code>mariadb</code>` that contains the default configuration for all our MariaDB servers, we can define these variables in a file called `<code>group_vars/mariadb.yml</code>`:


```
# MariaDB writes its logs here
mariadb_log_dir: /var/lib/mysql/logs

# logrotate configuration

mariadb_logrotate_min_size: 500M
mariadb_logrotate_max_size: 1G
mariadb_logrotate_old_files: 7
mariadb_logrotate_old_dir: /var/mysql/old-logs
```

After setting up logrotate in Ansible, you may want to deploy it to a non-production server and test it manually as explained above. Once you're sure that it works fine on one server, you can be confident in the new Ansible tasks and deploy them on all servers.


For more information on how to use Ansible to automate MariaDB configuration, see [Ansible and MariaDB](../getting-installing-and-upgrading-mariadb/binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/README.md).

