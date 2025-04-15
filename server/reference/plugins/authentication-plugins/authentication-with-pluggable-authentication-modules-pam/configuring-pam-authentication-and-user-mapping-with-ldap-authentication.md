
# Configuring PAM Authentication and User Mapping with LDAP Authentication

In this article, we will walk through the configuration of PAM authentication using the `<code>[pam](authentication-plugin-pam.md)</code>` authentication plugin and user and group mapping with the `<code>[pam_user_map](user-and-group-mapping-with-pam.md)</code>` PAM module. The primary authentication will be handled by the `<code>[pam_ldap](https://linux.die.net/man/5/pam_ldap)</code>` PAM module, which performs LDAP authentication. We will also set up an OpenLDAP server.



## Hypothetical Requirements


In this walkthrough, we are going to assume the following hypothetical requirements:


* The LDAP user `<code>foo</code>` should be mapped to the MariaDB user `<code>bar</code>`. (`<code>foo: bar</code>`)
* Any LDAP user in the LDAP group `<code>dba</code>` should be mapped to the MariaDB user `<code>dba</code>`. (`<code>@dba: dba</code>`)


## Setting up the OpenLDAP Server


Before we can use LDAP authentication, we first need to set up our OpenLDAP Server. This is usually done on a server that is completely separate from the database server.


### Installing the OpenLDAP Server and Client Components


On the server acting as the OpenLDAP Server, first, we need to install the OpenLDAP components.


On RHEL, CentOS, and other similar Linux distributions that use [RPM packages](../../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/README.md), that would go like this:


```
sudo yum install openldap openldap-servers openldap-clients nss-pam-ldapd
```

### Configuring the OpenLDAP Server


Next, let's to configure the OpenLDAP Server. The easiest way to do that is to copy the template configuration file that is included with the installation. In many installations, that will be at `<code>/usr/share/openldap-servers/DB_CONFIG.example</code>`. For example:


```
sudo cp /usr/share/openldap-servers/DB_CONFIG.example /var/lib/ldap/DB_CONFIG
sudo chown ldap. /var/lib/ldap/DB_CONFIG
```

#### Configuring the OpenLDAP Port


Sometimes it is useful to change the port used by OpenLDAP. For example, some cloud environments block well-known authentication services, so they block the default LDAP port.


On some systems, the port can be changed by setting `<code>SLAPD_URLS</code>` in `<code>/etc/sysconfig/slapd</code>`:


```
SLAPD_URLS="ldapi:/// ldap://0.0.0.0:3306/"
```

I used `<code>3306</code>` because that is the port that is usually used by `<code>mysqld</code>`, so I know that it is not blocked.


### Starting the OpenLDAP Server


Next, let's start the OpenLDAP Server and configure it to start on reboot. On `<code>[systemd](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/systemd.md)</code>` systems, that would go like this:


```
sudo systemctl start slapd
sudo systemctl enable slapd
```

### Installing the Standard LDAP objectClasses


In order to use LDAP for authentication, we also need to install some standard `<code>objectClasses</code>`, such as `<code>posixAccount</code>` and `<code>posixGroup</code>`. In LDAP, things like `<code>objectClasses</code>` are defined in `<code>[LDIF](https://www.digitalocean.com/community/tutorials/how-to-use-ldif-files-to-make-changes-to-an-openldap-system)</code>` files. In many installations, these specific `<code>objectClasses</code>` are defined in `<code>/etc/openldap/schema/nis.ldif</code>`. `<code>nis.ldif</code>` also depends on `<code>core.ldif</code>` and `<code>cosine.ldif</code>`. However, `<code>core.ldif</code>` is usually installed by default.


We can install them with `<code>[ldapmodify](https://www.openldap.org/software/man.cgi?query=ldapmodify&sektion=1&apropos=0&manpath=OpenLDAP+2.4-Release)</code>`:


```
sudo ldapmodify -a -Y EXTERNAL -H ldapi:/// -f /etc/openldap/schema/cosine.ldif
sudo ldapmodify -a -Y EXTERNAL -H ldapi:/// -f /etc/openldap/schema/nis.ldif
```

### Creating the LDAP Directory Manager User


Next, let’s create a directory manager user. We can do this by using OpenLDAP's [olc](https://www.openldap.org/doc/admin24/slapdconf2.html) configuration system to change the `<code>[olcRootDN](https://www.openldap.org/doc/admin24/slapdconf2.html#olcRootDN:%20%3CDN%3E)</code>` directive to the DN of the directory manager user, which means that the user will be a privileged LDAP user that is not subject to access controls. We will also set the root password for the user by changing the `<code>[olcRootPW](https://www.openldap.org/doc/admin24/slapdconf2.html#olcRootPW:%20%3Cpassword%3E)</code>` directive.


We will also set the DN suffix for our backend LDAP database by changing the `<code>[olcSuffix](https://www.openldap.org/doc/admin24/slapdconf2.html#olcSuffix:%20%3Cdn%20suffix%3E)</code>` directive.


Let’s use the `<code>[slappasswd](https://www.openldap.org/software/man.cgi?query=slappasswd&apropos=0&sektion=8&manpath=OpenLDAP+2.4-Release&format=html)</code>` utility to generate a password hash from a clear-text password. Simply execute:


```
slappasswd
```

This utility should provide a password hash that looks kind of like this: `<code>{SSHA}AwT4jrvmokeCkbDrFAnGvzzjCMb7bvEl</code>`


OpenLDAP's [olc](https://www.openldap.org/doc/admin24/slapdconf2.html) configuration system also uses `<code>[LDIF](https://www.digitalocean.com/community/tutorials/how-to-use-ldif-files-to-make-changes-to-an-openldap-system)</code>` files. Now that we have the password hash, let’s create an `<code>LDIF</code>` file to create the directory manager user:


```
tee ~/setupDirectoryManager.ldif <<EOF
dn: olcDatabase={1}monitor,cn=config
changetype: modify
replace: olcAccess
olcAccess: {0}to * 
    by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external,cn=auth" read 
    by dn.base="cn=Manager,dc=support,dc=mariadb,dc=com" read 
    by * none

dn: olcDatabase={2}hdb,cn=config
changetype: modify
replace: olcSuffix
olcSuffix: dc=support,dc=mariadb,dc=com

dn: olcDatabase={2}hdb,cn=config
changetype: modify
replace: olcRootDN
olcRootDN: cn=Manager,dc=support,dc=mariadb,dc=com

dn: olcDatabase={2}hdb,cn=config
changetype: modify
add: olcRootPW
olcRootPW: {SSHA}AwT4jrvmokeCkbDrFAnGvzzjCMb7bvEl

dn: olcDatabase={2}hdb,cn=config
changetype: modify
add: olcAccess
olcAccess: {0}to attrs=userPassword,shadowLastChange 
    by   dn="cn=Manager,dc=support,dc=mariadb,dc=com" write 
    by anonymous auth 
    by self write 
    by * none
olcAccess: {1}to dn.base="" 
    by * read
olcAccess: {2}to * 
    by dn="cn=Manager,dc=support,dc=mariadb,dc=com" write 
    by * read
EOF
```

Note that I am using the `<code>dc=support,dc=mariadb,dc=com</code>` domain for my directory. You can change this to whatever is relevant to you.


Now let’s run the ldif file with `<code>[ldapmodify](https://www.openldap.org/software/man.cgi?query=ldapmodify&sektion=1&apropos=0&manpath=OpenLDAP+2.4-Release)</code>`:


```
sudo ldapmodify -Y EXTERNAL -H ldapi:/// -f ~/setupDirectoryManager.ldif
```

We will use the new directory manager user to make changes to the LDAP directory after this step.


### Creating the Structure of the Directory


Next, let's create the structure of the directory by creating parts of our tree.


```
tee ~/setupDirectoryStructure.ldif <<EOF
dn: dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: dcObject
objectclass: organization
o: MariaDB Support Team
dc: support

dn: cn=Manager,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: organizationalRole
cn: Manager
description: Directory Manager

dn: ou=People,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: organizationalUnit
ou: People

dn: ou=Groups,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: organizationalUnit
ou: Groups

dn: ou=System Users,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: organizationalUnit
ou: System Users
EOF
```

Now let’s use our new directory manager user and run the `<code>[LDIF](https://www.digitalocean.com/community/tutorials/how-to-use-ldif-files-to-make-changes-to-an-openldap-system)</code>` file with `<code>[ldapmodify](https://www.openldap.org/software/man.cgi?query=ldapmodify&sektion=1&apropos=0&manpath=OpenLDAP+2.4-Release)</code>`:


```
ldapmodify -a -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -f ~/setupDirectoryStructure.ldif
```

### Creating the LDAP Users and Groups


Let's go ahead and create the LDAP users and groups that we are using for this hypothetical scenario.


First, let's create the the `<code>foo</code>` user:


```
tee ~/createFooUser.ldif <<EOF
dn: uid=foo,ou=People,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: account
objectClass: posixAccount
objectClass: shadowAccount
cn: foo
uid: foo
uidNumber: 16859
gidNumber: 100
homeDirectory: /home/foo
loginShell: /bin/bash
gecos: foo
userPassword: {crypt}x
shadowLastChange: -1
shadowMax: -1
shadowWarning: 0
EOF
ldapmodify -a -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -f ~/createFooUser.ldif
```

Then let's create a couple users to go into the `<code>dba</code>` group:


```
tee ~/createDbaUsers.ldif <<EOF
dn: uid=gmontee,ou=People,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: account
objectClass: posixAccount
objectClass: shadowAccount
cn: gmontee
uid: gmontee
uidNumber: 16860
gidNumber: 100
homeDirectory: /home/gmontee
loginShell: /bin/bash
gecos: gmontee
userPassword: {crypt}x
shadowLastChange: -1
shadowMax: -1
shadowWarning: 0

dn: uid=bstillman,ou=People,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: account
objectClass: posixAccount
objectClass: shadowAccount
cn: bstillman
uid: bstillman
uidNumber: 16861
gidNumber: 100
homeDirectory: /home/bstillman
loginShell: /bin/bash
gecos: bstillman
userPassword: {crypt}x
shadowLastChange: -1
shadowMax: -1
shadowWarning: 0
EOF
ldapmodify -a -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -f ~/createDbaUsers.ldif
```

Note that each of these users needs a password, so we can set it for each user with `<code>[ldappasswd](https://www.openldap.org/software/man.cgi?query=ldappasswd&apropos=0&sektion=1&manpath=OpenLDAP+2.4-Release&format=html)</code>`:


```
ldappasswd -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -S uid=foo,ou=People,dc=support,dc=mariadb,dc=com
ldappasswd -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -S uid=gmontee,ou=People,dc=support,dc=mariadb,dc=com
ldappasswd -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -S uid=bstillman,ou=People,dc=support,dc=mariadb,dc=com
```

And then let's create our `<code>dba</code>` group


```
tee ~/createDbaGroup.ldif <<EOF
dn: cn=dba,ou=Groups,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: posixGroup
gidNumber: 678
EOF
ldapmodify -a -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -f ~/createDbaGroup.ldif
```

And then let's add our two users to it:


```
tee ~/addUsersToDbaGroup.ldif <<EOF
dn: cn=dba,ou=Groups,dc=support,dc=mariadb,dc=com
changetype: modify
add: memberuid
memberuid: gmontee

dn: cn=dba,ou=Groups,dc=support,dc=mariadb,dc=com
changetype: modify
add: memberuid
memberuid: bstillman
EOF
ldapmodify -a -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -f ~/addUsersToDbaGroup.ldif
```

We also need to create LDAP users with the same name as the `<code>bar</code>` and `<code>dba</code>` MariaDB users. See [here](user-and-group-mapping-with-pam.md#pam-user-with-same-name-as-mapped-mariadb-user-must-exist) to read more about why. No one will be logging in as these users, so they do not need passwords. Instead of the `<code>People</code>` `<code>organizationalUnit</code>`, we will create them in the `<code>System Users</code>` `<code>organizationalUnit</code>`.


```
tee ~/createSystemUsers.ldif <<EOF
dn: uid=bar,ou=System Users,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: account
objectClass: posixAccount
objectClass: shadowAccount
cn: bar
uid: bar
uidNumber: 16862
gidNumber: 100
homeDirectory: /home/bar
loginShell: /bin/bash
gecos: bar
userPassword: {crypt}x
shadowLastChange: -1
shadowMax: -1
shadowWarning: 0

dn: uid=dba,ou=System Users,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: account
objectClass: posixAccount
objectClass: shadowAccount
cn: dba
uid: dba
uidNumber: 16863
gidNumber: 100
homeDirectory: /home/dba
loginShell: /bin/bash
gecos: dba
userPassword: {crypt}x
shadowLastChange: -1
shadowMax: -1
shadowWarning: 0
EOF
ldapmodify -a -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -f ~/createSystemUsers.ldif
```

## Setting up the MariaDB Server


At this point, we can move onto setting up the MariaDB Server.


### Installing LDAP and PAM Libraries


First, we need to make sure that the LDAP and PAM libraries are installed.


On RHEL, CentOS, and other similar Linux distributions that use [RPM packages](../../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/README.md), we need to install the following packages:


```
sudo yum install openldap-clients nss-pam-ldapd pam pam-devel
```

### Configuring LDAP


Next, let's configure LDAP on the system. We can use `<code>[authconfig](https://linux.die.net/man/8/authconfig)</code>` for this:


```
sudo authconfig --enableldap \
   --enableldapauth \
   --ldapserver="ldap://172.30.0.238:3306" \
   --ldapbasedn="dc=support,dc=mariadb,dc=com" \
   --enablemkhomedir \
   --update
```

Be sure to replace `<code>-–ldapserver</code>` and `<code>-–ldapbasedn</code>` with values that are relevant for your environment.


### Installing the pam_user_map PAM Module


The following steps apply to MariaDB Server in versions 10.2.32.7, 10.3.23., 10.4.13.6, 10.5.2 and earlier. In later releases, the pam_user_map PAM module is now included in the base install.


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

### Configuring the pam_user_map PAM Module


Next, let's [configure the pam_user_map PAM module](user-and-group-mapping-with-pam.md#configuring-the-pam_user_map-pam-module) based on our hypothetical requirements.


The configuration file for the `<code>pam_user_map</code>` PAM module is `<code>/etc/security/user_map.conf</code>`. Based on our hypothetical requirements, ours would look like:


```
foo: bar
@dba:dba
```

### Installing the PAM Authentication Plugin


Next, let's [install the pam authentication plugin](authentication-plugin-pam.md#installing-the-plugin).


Log into the MariaDB Server and execute the following:


```
INSTALL SONAME 'auth_pam';
```

### Configuring the PAM Service


Next, let's [configure the PAM service](authentication-plugin-pam.md#configuring-the-pam-service). We will call our service `<code>mariadb</code>`, so our PAM service configuration file will be located at `<code>/etc/pam.d/mariadb</code>` on most systems.


#### Configuring PAM to Allow Only LDAP Authentication


Since we are only doing LDAP authentication with the `<code>[pam_ldap](https://linux.die.net/man/5/pam_ldap)</code>` PAM module and group mapping with the `<code>pam_user_map</code>` PAM module, our configuration file would look like this:


```
auth required pam_ldap.so
auth required pam_user_map.so
account required pam_ldap.so
```

#### Configuring PAM to Allow LDAP and Local Unix Authentication


If we want to allow authentication from LDAP users **and** from local Unix users through `<code>[pam_unix](https://linux.die.net/man/8/pam_unix)</code>`, while giving priority to the local users, then we could do this instead:


```
auth [success=1 new_authtok_reqd=1 default=ignore] pam_unix.so audit
auth required pam_ldap.so try_first_pass
auth required pam_user_map.so
account sufficient pam_unix.so audit
account required pam_ldap.so
```

##### Configuring the pam_unix PAM Module


If you also want to allow authentication from local Unix users, the `<code>pam_unix</code>` PAM module adds [some additional configuration steps](authentication-plugin-pam.md#configuring-the-pam-service) on a lot of systems. We basically have to give the user that runs `<code>mysqld</code>` access to `<code>/etc/shadow</code>`.


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


### Testing LDAP Authentication


First, let's test out our `<code>foo</code>` user:


```
$ mysql -u foo -h 172.30.0.198
[mariadb] Password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 134
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

We can verify that our `<code>foo</code>` LDAP user was properly mapped to the `<code>bar</code>` MariaDB user by looking at the return value of `<code>[CURRENT_USER()](../../../sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/current_user.md)</code>`.


Then let's test out our `<code>gmontee</code>` user in the `<code>dba</code>` group:


```
$ mysql -u gmontee -h 172.30.0.198
[mariadb] Password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 135
Server version: 10.3.10-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT USER(), CURRENT_USER();
+----------------------------------------------------+----------------+
| USER()                                             | CURRENT_USER() |
+----------------------------------------------------+----------------+
| gmontee@ip-172-30-0-198.us-west-2.compute.internal | dba@%          |
+----------------------------------------------------+----------------+
1 row in set (0.000 sec)
```

And then let's test out our `<code>bstillman</code>` user in the `<code>dba</code>` group:


```
$ mysql -u bstillman -h 172.30.0.198
[mariadb] Password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 136
Server version: 10.3.10-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT USER(), CURRENT_USER();
+------------------------------------------------------+----------------+
| USER()                                               | CURRENT_USER() |
+------------------------------------------------------+----------------+
| bstillman@ip-172-30-0-198.us-west-2.compute.internal | dba@%          |
+------------------------------------------------------+----------------+
1 row in set (0.000 sec)
```

We can verify that our `<code>gmontee</code>` and `<code>bstillman</code>` LDAP users in the `<code>dba</code>` LDAP group were properly mapped to the `<code>dba</code>` MariaDB user by looking at the return values of `<code>[CURRENT_USER()](../../../sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/current_user.md)</code>`.


### Testing Local Unix Authentication


If you chose the option that also allowed local Unix authentication, then let's test that out. Let's create a Unix user and give the user a password real quick:


```
sudo useradd alice
sudo passwd alice
```

And let's also map this user to `<code>dba</code>`:


```
@dba:dba
foo: bar
alice: dba
```

And we know that the existing anonymous user already has the `<code>PROXY</code>` privilege granted to the `<code>dba</code>` user, so this should just work without any other configuration. Let's test it out:


```
$ mysql -u alice -h 172.30.0.198
[mariadb] Password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 141
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

We can verify that our `<code>alice</code>` Unix user was properly mapped to the `<code>dba</code>` MariaDB user by looking at the return values of `<code>[CURRENT_USER()](../../../sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/current_user.md)</code>`.

