
# Cracklib Password Check Plugin

`<code>cracklib_password_check</code>` is a [password validation](README.md) plugin. It uses the [CrackLib](https://github.com/cracklib/cracklib) library to check the strength of new passwords. CrackLib is installed by default in many Linux distributions, since the system's [Pluggable Authentication Module (PAM)](https://en.wikipedia.org/wiki/Pluggable_authentication_module) authentication framework is usually configured to check the strength of new passwords with the `<code>[pam_cracklib](https://linux.die.net/man/8/pam_cracklib)</code>` PAM module.


Note that passwords can be directly set as a hash, bypassing the password validation, if the [strict_password_validation](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#strict_password_validation) variable is `<code>OFF</code>` (it is `<code>ON</code>` by default).


The plugin requires at least cracklib 2.9.0, so it is not available on Debian/Ubuntu builds before Debian 8 Jessie/Ubuntu 14.04 Trusty, RedHat Enterprise Linux / CentOS 6.


## Installing the Plugin's Package


The `<code>cracklib_password_check</code>` plugin's shared library is included in MariaDB packages as the `<code>cracklib_password_check.so</code>` or `<code>cracklib_password_check.dll</code>` shared library on systems where it can be built.


### Installing on Linux


The `<code>cracklib_password_check</code>` plugin is included in `<code>systemd</code>` [binary tarballs](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/installing-mariadb-binary-tarballs.md) on Linux, but not in the older generic and `<code>glibc_214</code>` tarballs.


#### Installing with a Package Manager


The `<code>cracklib_password_check</code>` plugin can also be installed via a package manager on Linux. In order to do so, your system needs to be configured to install from one of the MariaDB repositories.


You can configure your package manager to install it from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md).


You can also configure your package manager to install it from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/).


##### Installing with yum/dnf


On RHEL, CentOS, Fedora, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/README.md) from MariaDB's
repository using `<code>[yum](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/yum.md)</code>` or `<code>[dnf](https://en.wikipedia.org/wiki/DNF_(software))</code>`. Starting with RHEL 8 and Fedora 22, `<code>yum</code>` has been replaced by `<code>dnf</code>`, which is the next major version of `<code>yum</code>`. However, `<code>yum</code>` commands still work on many systems that use `<code>dnf</code>`. For example:


```
sudo yum install MariaDB-cracklib-password-check
```

##### Installing with apt-get


On Debian, Ubuntu, and other similar Linux distributions, it is highly recommended to install the relevant [DEB package](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md) from MariaDB's
repository using `<code>[apt-get](https://wiki.debian.org/apt-get)</code>`. For example:


```
sudo apt-get install mariadb-plugin-cracklib-password-check
```

##### Installing with zypper


On SLES, OpenSUSE, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/README.md) from MariaDB's repository using `<code>[zypper](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md)</code>`. For example:


```
sudo zypper install MariaDB-cracklib-password-check
```

## Installing the Plugin


Once the shared library is in place, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.


The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing `<code>[INSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md)</code>` or `<code>[INSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md)</code>`. For example:


```
INSTALL SONAME 'cracklib_password_check';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the `<code>[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or the `<code>[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` options. This can be specified as a command-line argument to `<code>[mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
plugin_load_add = cracklib_password_check
```

## Uninstalling the Plugin


You can uninstall the plugin dynamically by executing `<code>[UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)</code>` or `<code>[UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)</code>`. For example:


```
UNINSTALL SONAME 'cracklib_password_check';
```

If you installed the plugin by providing the `<code>[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or the `<code>[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` options in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.


## Viewing CrackLib Errors


If password validation fails, then the original CrackLib error message can be viewed by executing `<code>[SHOW WARNINGS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-warnings.md)</code>`.


## Example


When creating a new password, if the criteria are not met, the following error is returned:


```
SET PASSWORD FOR 'bob'@'%.loc.gov' = PASSWORD('abc');
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
```

## Known Issues


### Issues with PAM Authentication Plugin


Prior to [MariaDB 10.4.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1040-release-notes.md), all [password validation plugins](README.md) are incompatible with the `<code>[pam](../authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md)</code>` authentication plugin. See [Authentication Plugin - PAM: Conflicts with Password Validation](../authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md#conflicts-with-password-validation) for more information.


### SELinux


When using the standard [SELinux](../../../security/securing-mariadb/selinux.md) policy with the [mode](../../../security/securing-mariadb/selinux.md#changing-selinuxs-mode) set to `<code>enforcing</code>`, `<code>mysqld</code>` does not have access to `<code>/usr/share/cracklib</code>`, and you may see the following error when attempting to use the `<code>cracklib_password_check</code>` plugin:


```
CREATE USER `user`@`hostname` IDENTIFIED BY 's0mePwd123.';
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements

SHOW WARNINGS;
+---------+------+----------------------------------------------------------------+
| Level   | Code | Message                                                        |
+---------+------+----------------------------------------------------------------+
| Warning | 1819 | cracklib: error loading dictionary                             |
| Error   | 1819 | Your password does not satisfy the current policy requirements |
| Error   | 1396 | Operation CREATE USER failed for 'user'@'hostname'             |
+---------+------+----------------------------------------------------------------+
```

And the SELinux `<code>audit.log</code>` will contain errors like the following:


```
type=AVC msg=audit(1548371977.821:66): avc:  denied  { read } for  pid=3537 comm="mysqld" name="pw_dict.pwd" dev="xvda2" ino=564747 scontext=system_u:system_r:mysqld_t:s0 tcontext=system_u:object_r:crack_db_t:s0 tclass=file
type=SYSCALL msg=audit(1548371977.821:66): arch=c000003e syscall=2 success=no exit=-13 a0=7fdd2a674580 a1=0 a2=1b6 a3=1b items=0 ppid=1 pid=3537 auid=4294967295 uid=995 gid=992 euid=995 suid=995 fsuid=995 egid=992 sgid=992 fsgid=992 tty=(none) ses=4294967295 comm="mysqld" exe="/usr/sbin/mysqld" subj=system_u:system_r:mysqld_t:s0 key=(null)
```

This can be fixed by creating an SELinux policy that allows `<code>mysqld</code>` to load the CrackLib dictionary. For example:


```
cd /usr/share/mysql/policy/selinux/
tee ./mariadb-plugin-cracklib-password-check.te <<EOF

module mariadb-plugin-cracklib-password-check 1.0;

require {
        type mysqld_t;
        type crack_db_t;
        class file { execute setattr read create getattr execute_no_trans write ioctl open append unlink };
        class dir { write search getattr add_name read remove_name open };
}

allow mysqld_t crack_db_t:dir { search read open };
allow mysqld_t crack_db_t:file { getattr read open };
EOF
sudo yum install selinux-policy-devel
make -f /usr/share/selinux/devel/Makefile mariadb-plugin-cracklib-password-check.pp
sudo semodule -i mariadb-plugin-cracklib-password-check.pp
```

See [MDEV-18374](https://jira.mariadb.org/browse/MDEV-18374) for more information.


## Versions



| Version | Status | Introduced |
| --- | --- | --- |
| Version | Status | Introduced |
| 1.0 | Stable | [MariaDB 10.1.18](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10118-release-notes.md) |
| 1.0 | Gamma | [MariaDB 10.1.13](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10113-release-notes.md) |
| 1.0 | Alpha | [MariaDB 10.1.2](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-2-release-notes.md) |



## System Variables


#### `<code>cracklib_password_check_dictionary</code>`


* Description: Sets the path to the CrackLib dictionary. If not set, the default CrackLib dictionary path is used. The parameter expects the base name of a cracklib dictionary (a set of three files with endings `<code>.hwm</code>`, `<code>.pwd</code>`, `<code>.pwi</code>`), not a directory path.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--cracklib-password-check-dictionary=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: Depends on the system. Often `<code>/usr/share/cracklib/pw_dict</code>`



## Options


#### `<code>cracklib_password_check</code>`


* Description: Controls how the server should treat the plugin when the server starts up.

  * Valid values are:

    * `<code>OFF</code>` - Disables the plugin without removing it from the `<code>[mysql.plugins](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md)</code>` table.
    * `<code>ON</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `<code>FORCE</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `<code>FORCE_PLUS_PERMANENT</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with `<code>[UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)</code>` or `<code>[UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)</code>` while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--cracklib-password-check=value</code>`
* Data Type: `<code>enumerated</code>`
* Default Value: `<code>ON</code>`
* Valid Values: `<code>OFF</code>`, `<code>ON</code>`, `<code>FORCE</code>`, `<code>FORCE_PLUS_PERMANENT</code>`



## See Also


* [Password Validation](README.md)
* [simple_password_check plugin](simple-password-check-plugin.md) - permits the setting of basic criteria for passwords

