# MariaDB Connector/C 2.1.0 Changelog

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-c/2.1.0)[Release Notes](../mariadb-connector-c-210-release-notes.md)[Changelog](mariadb-connector-c-210-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 29 Jan 2015

For the highlights of this release, see the[release notes](../mariadb-connector-c-210-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #199](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/199)\
  Wed 2015-01-28 18:25:27 +0100
  * Updated ignore file list
* [Revision #198](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/198)\
  Wed 2015-01-21 19:32:04 +0100
  * Generate files for exported symbols, so we don't have to keep 2 different files up to date. Symbols should be added (or removed) now in libmariadb/CMakeLists.txt
* [Revision #197](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/197)\
  Wed 2015-01-21 12:41:29 +0100
  * changed banner for msi installation
* [Revision #196](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/196)\
  Wed 2015-01-21 12:03:12 +0100
  * Added a global variable mariadb\_deinitialize\_ssl which controls if SSL will be deinitialized in mysql\_server\_end (see [MDEV-6671](https://jira.mariadb.org/browse/MDEV-6671))
* [Revision #195](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/195)\
  Wed 2015-01-21 11:47:34 +0100
  * We now build an object library which prevents compiling sources twice (for shared and static libraries) Fixed test cases
* [Revision #194](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/194)\
  Fri 2015-01-16 13:17:51 +0100
  * Fixed hardcoded path for default locations
* [Revision #193](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/193)\
  Wed 2015-01-14 20:53:13 +0100
  * Fixed name for source package
* [Revision #192](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/192)\
  Wed 2015-01-14 15:29:27 +0100
  * (Corrected) Fix for [CONC-118](https://jira.mariadb.org/browse/CONC-118): memory leak when reconnecting
* [Revision #191](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/191)\
  Wed 2015-01-07 20:20:04 +0100
  * Fix string for hex\_symbols in mysql\_hex\_string function
* [Revision #190](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/190)\
  Wed 2015-01-07 14:06:49 +0100
  * Fixed filenames for include lists (msi packaging)
* [Revision #189](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/189)\
  Wed 2015-01-07 11:16:53 +0100
  * Added plugin dependencies for msi build
* [Revision #188](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/188)\
  Wed 2015-01-07 10:43:18 +0100
  * Codesigning for cleartext plugin (MSI package)
* [Revision #187](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/187)\
  Tue 2014-12-23 13:05:13 +0100
  * More build fixes Added new option for position independent code: WITH\_PIC=ON/OFF
* [Revision #186](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/186)\
  Sun 2014-12-21 22:11:37 +0100
  * Static library fixes
* [Revision #185](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/185)\
  Sun 2014-12-21 17:43:38 +0100
  * Fix for [CONC-117](https://jira.mariadb.org/browse/CONC-117):
* [Revision #184](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/184)\
  Fri 2014-12-19 17:42:33 +0100
  * avoid compiling objects twice: shared and static library now can be build in one step
* [Revision #183](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/183)\
  Thu 2014-12-18 18:02:50 +0100
  * Added support for MYSQL\_ENABLE\_CLEARtEXT\_PLUGIN in mysql\_options. However we don't take any actions - plugins are always enabled.
* [Revision #182](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/182)\
  Thu 2014-12-18 12:59:28 +0100
  * Fix include path in mariadb\_config
* [Revision #181](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/181)\
  Thu 2014-12-18 12:03:38 +0100
  * fixed typo in plugins/auth/CMakeLists.txt
* [Revision #180](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/180)\
  Tue 2014-12-16 19:42:17 +0100
  * Added missing mysql\_clear\_password for msi
* [Revision #179](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/179)\
  Sat 2014-12-13 17:37:52 +0100
  * Fixes for include/mysql folder in msi
* [Revision #178](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/178)\
  Sat 2014-12-13 15:29:32 +0100
  * More msi fixes
* [Revision #177](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/177)\
  Sat 2014-12-13 11:14:02 +0100
  * Added missing include files in include/mysqlh Fixed id's in msi packager
* [Revision #176](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/176)\
  Fri 2014-12-12 18:00:43 +0100
  * Fixed package name for windows
* [Revision #175](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/175)\
  Fri 2014-12-12 15:40:35 +0100
  * Fixed package\_file\_name for cpack
* [Revision #174](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/174)\
  Fri 2014-12-12 08:23:30 +0100
  * Buildbot fix: Lowered required cmake version for non windows latforms to 2.6.4 removed get\_tty\_password from list of exported functions
* [Revision #173](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/173)\
  Fri 2014-12-12 08:10:41 +0100
  * removed obsolete getpass() stuff from get\_password.c
* [Revision #172](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/172)\
  Thu 2014-12-11 12:41:15 +0100
  * msi fixex for authentication plugins
* [Revision #171](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/171)\
  Thu 2014-12-11 11:35:41 +0100
  * Fixed include directories for windows build
* [Revision #170](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/170)\
  Thu 2014-12-11 11:20:32 +0100
  * Fix for cleartext plugin: We need to send also terminating zero character for password
* [Revision #169](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/169)\
  Thu 2014-12-11 11:17:58 +0100
  * Added clear\_text plugin for pam authentication. To use the clear text plugin pam-use-cleartext-plugin setting must be enabled in MariaDB server.
* [Revision #168](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/168)\
  Thu 2014-12-11 09:47:49 +0100
  *
    * mysql\_load\_plugin\_v supports now the environment variable MARIADB\_PLUGIN\_DIR to load plugins from a different destination than PLUGINDIR.
* [Revision #167](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/167)\
  Tue 2014-12-09 20:11:54 +0100
  * Fixed misc.c (was test case for [CONC-114](https://jira.mariadb.org/browse/CONC-114))
* [Revision #166](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/166)\
  Thu 2014-11-13 13:54:45 +0100
  * Fix for [CONC-114](https://jira.mariadb.org/browse/CONC-114): Windows version of libmariadb doesn't export all symbols
* [Revision #165](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/165)\
  Thu 2014-11-13 10:27:59 +0100
  * Build fixes for MacOSX
* [Revision #164](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/164)\
  Thu 2014-11-13 09:02:44 +0100
  * Fixed product name for msi build
* [Revision #163](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/163)\
  Wed 2014-11-12 19:40:14 +0100
  * another revert and repush for msi/buildbot
* [Revision #162](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/162)\
  Wed 2014-11-12 18:30:33 +0100
  * Reverted last patch and added more windows build fixes
* [Revision #161](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/161)\
  Wed 2014-11-12 18:10:22 +0100
  * Fixed vio for non-blocking API calls
* [Revision #160](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/160)\
  Fri 2014-11-07 07:09:24 +0100
  * Fix for [CONC-111](https://jira.mariadb.org/browse/CONC-111): export missing symbols for plugin api
* [Revision #159](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/159)\
  Tue 2014-11-04 16:30:41 +0100
  * More dynamic solution for [CONC-107](https://jira.mariadb.org/browse/CONC-107). Cmake now supports the following options: -DINSTALL\_LAYOUT=DEFAULT or RPM -DINSTALL\_LIB\_DIR -DINSTALL\_INCLUDE\_DIR -DINSTALL\_DOCS\_DIR -DINSTALL\_PLUGINS\_DIR -DINSTALL\_BIN\_DIR
* [Revision #158](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/158)\
  Sun 2014-11-02 05:54:30 +0100
  * Fix for OS-X build (Thanks to Eric Trinh) test case fixes: removed obsolete DBUG\_\* stuff
* [Revision #157](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/157)\
  Mon 2014-10-27 14:18:35 +0100
  * Since CRYPTO\_THREADID is not supported by OpenSSL versions prior to 1.0.0, we need still provide support for old (deprecated) thread\_id functions.
* [Revision #156](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/156)\
  Thu 2014-10-23 18:48:42 +0200
  * Removed docs. Documentation is in a separate github repository
* [Revision #155](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/155)\
  Thu 2014-10-23 18:45:18 +0200
  * Build fixes for MacOS and Windows
* [Revision #154](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/154)\
  Wed 2014-10-22 17:36:33 +0200
  * Windows fix: remove inclusion of global.h in str helper functions
* [Revision #153](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/153)\
  Wed 2014-10-22 17:16:27 +0200
  * renoved unused include added some status information
* [Revision #152](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/152)\
  Tue 2014-10-21 16:55:04 +0200
  * Fix for [CONC-107](https://jira.mariadb.org/browse/CONC-107), [CONC-108](https://jira.mariadb.org/browse/CONC-108) and [CONC-109](https://jira.mariadb.org/browse/CONC-109)
* [Revision #151](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/151)\
  Sun 2014-10-12 05:35:43 +0200
  * Fix for [CONC-102](https://jira.mariadb.org/browse/CONC-102): Since we use one SSL context per library instance (which might be shared by several threads) we need to protect certification loading by a mutex.
* [Revision #150](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/150)\
  Wed 2014-09-17 19:14:09 +0200
  * Fix for [CONC-105](https://jira.mariadb.org/browse/CONC-105): remove longlong definition from mysql.h to prevent collides with other projects
* [Revision #149](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/149)\
  Mon 2014-09-15 15:47:17 +0200
  * Fix for [CONC-104](https://jira.mariadb.org/browse/CONC-104): mysql\_options doesn't support MYSQL\_SECURE\_AUTH option
* [Revision #148](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/148)\
  Mon 2014-07-14 11:50:16 +0200
  * Fix for [CONC-101](https://jira.mariadb.org/browse/CONC-101): redefinition of dlerror
* [Revision #147](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/147)\
  Fri 2014-06-27 06:48:43 +0200
  *
    * Removed unused \_PC macrofrom my\_global.h: it clashes with \_PC macro in tchar.h (windows) - removed unused global.h file
* [Revision #146](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/146)\
  Tue 2014-06-24 08:13:43 +0200
  * Fix for asynchronous api (windows): Context iitialization didn't work, since client library doesn't use WIN definition (instead we use \_WIN32).
* [Revision #145](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/145)\
  Mon 2014-06-23 09:23:14 +0200
  * Fix for [CONC-95](https://jira.mariadb.org/browse/CONC-95): SSL connection with require X509 privilege doesn't work. - all pems and ciphers are now stored in global context - create new ssl instance after loading pems into global context
* [Revision #144](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/144)\
  Fri 2014-06-20 12:23:14 +0200
  * Fix for [CONC-99](https://jira.mariadb.org/browse/CONC-99): memory corruption In case a connection fails and vio was already created the socket needs to be closed only via vio\_close. A 2nd close may lead to corruption in a threaded evironment in case the handle was opened by a nother thread.
* [Revision #143](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/143)\
  Tue 2014-06-10 09:48:05 +0200
  * Fix for [CONC-97](https://jira.mariadb.org/browse/CONC-97) and [CONC-98](https://jira.mariadb.org/browse/CONC-98): - Check if the connection is valid before resetting statement - Fix windows compile error (mingw)
* [Revision #142](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/142)\
  Thu 2014-05-15 08:34:31 +0200
  * We create the include files twice now, to prevent problems with MSI installer
* [Revision #141](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/141)\
  Wed 2014-05-14 15:31:58 +0200
  * Fix for [CONC-92](https://jira.mariadb.org/browse/CONC-92): Since NULL values in a binary result packet are represented in a bitmap, the packet length might be smaller than the number of result set NULL values, so we need to allocate additional bytes (=Number of fields) to prevent a possible memory corruption
* [Revision #140](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/140)\
  Wed 2014-05-14 14:49:25 +0200
  * Fixed ssl test (running ssl tests now under different user)
* [Revision #139](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/139)\
  Wed 2014-05-14 12:20:47 +0200
  * Added delay/sleep after mysql\_kill
* [Revision #138](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/138)\
  Fri 2014-05-09 09:46:53 +0200
  * Throw error in case OpenSSL was not found
* [Revision #137](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/137)\
  Mon 2014-05-05 15:04:39 +0200
  * Fixed prototype for mysql\_hex\_string from ulong to unsigned long
* [Revision #136](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/136)\
  Sun 2014-05-04 17:30:54 +0200
  * Fix for [CONC-94](https://jira.mariadb.org/browse/CONC-94): Segmentation fault when using named pipes - disabled read-ahead cache for named pipe connections
* [Revision #135](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/135)\
  Fri 2014-05-02 16:13:21 +0200
  * Fix for [CONC-90](https://jira.mariadb.org/browse/CONC-90): Incorrect output for mariadb\_config - When linking against external zlib the linker options are - added missing space for CMAKE\_C\_FLAGS
* [Revision #134](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/134)\
  Thu 2014-04-10 10:17:45 +0200
  *
    * Windows build fixes for async API
* [Revision #133](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/133)\
  Tue 2014-04-08 12:18:08 +0200
  * Added MariaDB's asnychronous client API. For more information please visit [non-blocking-api-reference](broken-reference)
* [Revision #132](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/132)\
  Fri 2014-04-04 12:43:00 +0200
  * Fix for [CONC-88](https://jira.mariadb.org/browse/CONC-88): Out-of-source build touches files in source dir removed duplicate CONFIGURE\_FILE directives
* [Revision #131](https://bazaar.launchpad.net/~maria-captains/mariadb-native-client/trunk/revision/131)\
  Fri 2014-04-04 12:26:06 +0200
  * Fix for [CONC-86](https://jira.mariadb.org/browse/CONC-86): mysql.h doesn't include the API function mysql\_hex\_string
