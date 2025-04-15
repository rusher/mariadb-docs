
# Configuring PAM Authentication and User Mapping with Unix Authentication

In this article, we will walk through the configuration of PAM authentication using the `<code>[pam](authentication-plugin-pam.md)</code>` authentication plugin and user and group mapping with the `<code>[pam_user_map](user-and-group-mapping-with-pam.md)</code>` PAM module. The primary authentication will be handled by the `<code>[pam_unix](https://linux.die.net/man/8/pam_unix)</code>` PAM module, which performs standard Unix password authentication.



## Hypothetical Requirements


In this walkthrough, we are going to assume the following hypothetical requirements:


* The Unix user `<code>foo</code>` should be mapped to the MariaDB user `<code>bar</code>`. (`<code>foo: bar</code>`)
* Any Unix user in the Unix group `<code>dba</code>` should be mapped to the MariaDB user `<code>dba</code>`. (`<code>@dba: dba</code>`)


## Creating Our Unix Users and Groups


Let's go ahead and create the Unix users and groups that we are using for this hypothetical scenario.


First, let's create the the `<code>foo</code>` user and a couple users to go into the `<code>dba</code>` group. Note that each of these users needs a password.


```
sudo useradd foo
sudo passwd foo
sudo useradd alice
sudo passwd alice
sudo useradd bob
sudo passwd bob
```

And then let's create our `<code>dba</code>` group and add our two users to it:


```
sudo groupadd dba
sudo usermod -a -G dba alice 
sudo usermod -a -G dba bob
```

We also need to create Unix users with the same name as the `<code>bar</code>` and `<code>dba</code>` MariaDB users. See [here](user-and-group-mapping-with-pam.md#pam-user-with-same-name-as-mapped-mariadb-user-must-exist) to read more about why. No one will be logging in as these users, so they do not need passwords.


```
sudo useradd bar
sudo useradd dba -g dba
```

## Installing the pam_user_map PAM Module


Next, let's [install the pam_user_map PAM module](user-and-group-mapping-with-pam.md#installing-the-pam_user_map-pam-module).


Before the module can be compiled from source, we may need to install some dependencies.


On RHEL, CentOS, and other similar Linux distributions that use [RPM packages](../../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/README.md), we need to install `<code>gcc</code>` and `<code>pam-devel</code>`:


```
sudo yum install gcc pam-devel
```

On Debian, Ubuntu, and other similar Linux distributions that use [DEB packages](../../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md), we need to install `<code>gcc</code>` and `<code>libpam0g-dev</code>`:


```
sudo apt-get install gcc libpam0g-dev
```

And then we can build and install the library with the following:


```
wget https://raw.githubusercontent.com/MariaDB/server/10.4/plugin/auth_pam/mapper/pam_user_map.c 
gcc pam_user_map.c -shared -lpam -fPIC -o pam_user_map.so 
sudo install --mode=0755 pam_user_map.so /lib64/security/
```

## Configuring the pam_user_map PAM Module


Next, let's [configure the pam_user_map PAM module](user-and-group-mapping-with-pam.md#configuring-the-pam_user_map-pam-module) based on our hypothetical requirements.


The configuration file for the `<code>pam_user_map</code>` PAM module is `<code>/etc/security/user_map.conf</code>`. Based on our hypothetical requirements, ours would look like:


```
foo: bar
@dba:dba
```

## Installing the PAM Authentication Plugin


Next, let's [install the pam authentication plugin](authentication-plugin-pam.md#installing-the-plugin).


Log into the MariaDB Server and execute the following:


```
INSTALL SONAME 'auth_pam';
```

## Configuring the PAM Service


Next, let's [configure the PAM service](authentication-plugin-pam.md#configuring-the-pam-service). We will call our service `<code>mariadb</code>`, so our PAM service configuration file will be located at `<code>/etc/pam.d/mariadb</code>` on most systems.


Since we are only doing Unix authentication with the `<code>pam_unix</code>` PAM module and group mapping with the `<code>pam_user_map</code>` PAM module, our configuration file would look like this:


```
auth required pam_unix.so audit
auth required pam_user_map.so
account required pam_unix.so audit
```

## Configuring the pam_unix PAM Module


The `<code>pam_unix</code>` PAM module adds [some additional configuration steps](authentication-plugin-pam.md#configuring-the-pam-service) on a lot of systems. We basically have to give the user that runs `<code>mysqld</code>` access to `<code>/etc/shadow</code>`.


If the `<code>mysql</code>` user is running `<code>mysqld</code>`, then we can do that by executing the following:


```
sudo groupadd shadow
sudo usermod -a -G shadow mysql
sudo chown root:shadow /etc/shadow
sudo chmod g+r /etc/shadow
```

The [server needs to be restarted](https://mariadb.com/kb/en/) for this change to take affect.


## Creating MariaDB Users


Next, let's [create the MariaDB users](authentication-plugin-pam.md#creating-users). Remember that our PAM service is called `<code>mariadb</code>`.


First, let's create the MariaDB user for the user mapping: `<code>foo: bar</code>`


That means that we need to create a `<code>bar</code>` user:


```
CREATE USER 'bar'@'%' IDENTIFIED BY 'strongpassword';
GRANT ALL PRIVILEGES ON *.* TO 'bar'@'%' ;
```

And then let's create the MariaDB user for the group mapping: `<code>@dba: dba</code>`


That means that we need to create a `<code>dba</code>` user:


```
CREATE USER 'dba'@'%' IDENTIFIED BY 'strongpassword';
GRANT ALL PRIVILEGES ON *.* TO 'dba'@'%' ;
```

And then to allow for the user and group mapping, we need to [create an anonymous user that authenticates with the pam authentication plugin](user-and-group-mapping-with-pam.md#creating-users) that is also able to `<code>PROXY</code>` as the `<code>bar</code>` and `<code>dba</code>` users. Before we can create the proxy user, we might need to [clean up some defaults](../../../sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user.md#fixing-a-legacy-default-anonymous-account):


```
DELETE FROM mysql.db WHERE User='' AND Host='%';
FLUSH PRIVILEGES;
```

And then let's create the anonymous proxy user:


```
CREATE USER ''@'%' IDENTIFIED VIA pam USING 'mariadb';
GRANT PROXY ON 'bar'@'%' TO ''@'%';
GRANT PROXY ON 'dba'@'%' TO ''@'%';
```

## Testing our Configuration


Next, let's test out our configuration by [verifying that mapping is occurring](user-and-group-mapping-with-pam.md#verifying-that-mapping-is-occurring). We can verify this by logging in as each of our users and comparing the return value of `<code>[USER()](../../other-plugins/user-variables-plugin.md)</code>`, which is the original user name and the return value of `<code>[CURRENT_USER()](../../../sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/current_user.md)</code>`, which is the authenticated user name.


First, let's test out our `<code>foo</code>` user:


```
$ mysql -u foo -h 172.30.0.198
[mariadb] Password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 22
Server version: 10.3.10-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT USER(), CURRENT_USER();
+------------------------------------------------+----------------+
| USER()                                         | CURRENT_USER() |
+------------------------------------------------+----------------+
| foo@ip-172-30-0-198.us-west-2.compute.internal | bar@%          |
+------------------------------------------------+----------------+
1 row in set (0.000 sec)
```

We can verify that our `<code>foo</code>` Unix user was properly mapped to the `<code>bar</code>` MariaDB user by looking at the return value of `<code>[CURRENT_USER()](../../../sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/current_user.md)</code>`.


Then let's test out our `<code>alice</code>` user in the `<code>dba</code>` group:


```
$ mysql -u alice -h 172.30.0.198
[mariadb] Password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 19
Server version: 10.3.10-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT USER(), CURRENT_USER();
+--------------------------------------------------+----------------+
| USER()                                           | CURRENT_USER() |
+--------------------------------------------------+----------------+
| alice@ip-172-30-0-198.us-west-2.compute.internal | dba@%          |
+--------------------------------------------------+----------------+
1 row in set (0.000 sec)
```

And then let's test out our `<code>bob</code>` user in the `<code>dba</code>` group:


```
$ mysql -u bob -h 172.30.0.198
[mariadb] Password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 20
Server version: 10.3.10-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT USER(), CURRENT_USER();
+------------------------------------------------+----------------+
| USER()                                         | CURRENT_USER() |
+------------------------------------------------+----------------+
| bob@ip-172-30-0-198.us-west-2.compute.internal | dba@%          |
+------------------------------------------------+----------------+
1 row in set (0.000 sec)
```

We can verify that our `<code>alice</code>` and `<code>bob</code>` Unix users in the `<code>dba</code>` Unix group were properly mapped to the `<code>dba</code>` MariaDB user by looking at the return values of `<code>[CURRENT_USER()](../../../sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/current_user.md)</code>`.

