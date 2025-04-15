
# Building MariaDB on Windows


## Build Requirements


To build MariaDB you need the following:


* [Visual C++](https://www.microsoft.com/visualstudio): We currently support Visual Studio 2019 and 2022. Generally we try to support the two most recent VS versions, but build ourselves using the last one. Community editions will work fine; we only use them in our builds.
While installing Visual Studio, make sure to [add "Desktop Development with C++"](https://mariadb.com/kb/en/Building_MariaDB_on_Windows/+image/vs2019_workloads).
Also, make sure to use [recent enough Windows SDK](https://learn.microsoft.com/en-us/cpp/overview/install-c17-support?view=msvc-170) - latest Windows 11 SDK is recommended.


* [CMake](https://cmake.org/download): We recommend the latest release. Older releases might not support your version of Visual Studio. Visual Studio 2019 requires cmake 3.14 at least.


* [Git](https://git-scm.com/download): Required to
 build newer versions from the source tree. 

  * NOTE: run


```
git config --global core.autocrlf input
```

after the installation, otherwise some mtr tests will fail


In the "Adjusting your PATH" dialog, choose "Use Git from Windows command prompt", otherwise wrong (mingw64) git and perl will be in your PATH


* [Bison from GnuWin32](https://gnuwin32.sourceforge.net/packages/bison.htm):
 Bison creates parts of the SQL parser. Choose "Complete package except
 sources" when downloading.

  * NOTE: Do not install this into your default path with spaces
 (e.g. under `<code>C:\Program Files\GnuWin32</code>`); the build will break due to
 [this bison bug](https://sourceforge.net/tracker/index.php?func=detail&aid=2788969&group_id=23617&atid=379173).
 Instead, install into `<code>C:\GnuWin32</code>`.
  * Add `<code>C:\GnuWin32\bin</code>` to your system `<code>PATH</code>` after installation.
* [Strawberry perl](https://strawberryperl.com): Used to run the test suite.
 [ActiveState Perl](https://www.activestate.com/activeperl/downloads) is
 another Win32 Perl distribution and should work as well (but it is not as
 well tested). NOTE: Cygwin or mingw Perl versions will not work for testing. Use Windows native Perl, please.
* Optional: If you intend to build the MSI packages, install
 [Windows Installer XML](https://wixtoolset.org/releases/) . If you build MSI with 10.4, 
 also modify your Visual Studio installation, add "Redistributable MSMs" (see [MDEV-22555](https://jira.mariadb.org/browse/MDEV-22555))


* [Gnu Diff](https://gnuwin32.sourceforge.net/packages/diffutils.htm), needed if you run mysql-test-run.pl tests.


Verify that bison.exe, or git.exe, cmake.exe and perl.exe can be found in the PATH
environment variable with "`<code>where bison</code>`", "`<code>where git</code>`", "`<code>where perl</code>`" etc. from
the command line prompt.


## Building Windows Binaries


The above instructions assume [MariaDB 10.2](../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md) or higher.


Branch the MariaDB repository, or unpack the source archive. On the command
prompt, switch to your source directory, then execute:


```
mkdir bld
cd bld
cmake ..
cmake --build . --config RelWithDebInfo
```

The above example builds a release configured for 64 bit systems in a
subdirectory named `<code>bld</code>`. "`<code>cmake ...</code>`" is the configuration step,
"`<code>cmake --build . --config Relwithdebinfo</code>`" is the build step.


## Build Variations


### Debug Builds


Building Debug version is done with:


```
cmake --build . --config Debug
```

### 32bit and 64 bit Builds


#### Build 64 bit binary


Visual Studio 2019-2022 cmake generator will use host architecture by default, that is, with the steps above, cmake will build x64 binaries on x64 machine.


#### Build 32 bit binary


pass -A Win32 parameter for CMake, like this


```
cmake .. -A Win32
```

Historical note:
With Visual Studio 2017 and earlier, one had to pass the name of 32bit generator ,e.g
cmake .. -G "Visual Studio 15 2017"


For a complete list of available generators, call "cmake" without any parameters.


### IDE Builds


Instead of calling "`<code>cmake --build</code>`" as above, open solution file `<code>MariaDB.sln</code>` (in older versions, prior to 11.0, `<code>MySQL.sln</code>` ). When Visual Studio starts, choose Build/Compile.


## Building the ZIP Package


```
cmake --build . --config relwithdebinfo --target package
```

This is how it is "done by the book", standard cmake target.


MariaDB however uses non-standard target "win_package" for the packaging for its releases, it generates 2 ZIPs, a slim one with executables, and another one with debuginfo (.PDB files). The debuginfo is important to be able to debug released binaries, and to analyze crashes.


```
cmake --build . --config relwithdebinfo --target win_package
```

## Building the MSI Package


```
cmake --build . --config relwithdebinfo 
cmake --build . --config relwithdebinfo --target MSI
```

## Including HeidiSQL in the MSI Installer


Starting with [MariaDB 5.2.7](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-2-series/mariadb-527-release-notes.md), it is possible to build an installer which
includes 3rd party products, as described in
[MWL#200](https://askmonty.org/worklog/Other/?tid=200). Currently only
[HeidiSQL](https://www.heidisql.com) support is implemented; it is also
included in the official builds. Use the CMake parameter
`<code>-DWITH_THIRD_PARTY=HeidiSQL</code>` to include it in the installer.


## Code Signing


MariaDB builds optionally support authenticode code signing with an optional
parameter `<code>SIGNCODE</code>`. Use `<code class="fixed" style="white-space:pre-wrap">cmake -DSIGNCODE=1</code>` during the
configuration step to sign the binaries in the `<code>ZIP</code>` and `<code>MSI</code>` packages.


**Important:** for `<code>SIGNCODE=1</code>` to work, the user that runs the build needs to
install a valid authenticode digital certificate into their certificate store,
otherwise the packaging step will fail.


## Building Packages for MariaDB Releases


The full script to create the release in an out-of-source build with Visual
Studio with signed binaries might look like:


```
mkdir bld
cd bld
cmake .. -DSIGNCODE=1 -DWITH_THIRD_PARTY=HeidiSQL
cmake --build . --config relwithdebinfo --target win_package
cmake --build . --config relwithdebinfo  --target MSI
```

This command sequence will produce a ZIP package (e.g mariadb-5.2.6-win32.zip)
and MSI package (e.g mariadb-5.2.6-win32.msi) in the `<code>bld</code>` directory.


## Running Tests


* Important: Do not use Cygwin bash, MinGW bash, Git bash, WSL bash, or any other bash when running the test suite. You will then very likely use the wrong version of Perl too (a "Unix-flavoured" one on Windows), and spend a lot of time trying to figure out why this version of Perl does not work for the test suite. Use native perl, in cmd.exe , or powershell instead,


* Switch mysql-test subdirectory of the build directory


```
cd C:\server\bld\mysql-test
```

* Run the test suite


```
perl mysql-test-run.pl --suite=main --parallel=auto
```

### Running a Test Under Debugger


Assuming VS is installed on the machine


```
perl mysql-test-run.pl  <test_name> --vsjitdebugger
```

If vsjitdebugger does not start, you can edit AeDebug registry key as mentioned in


[debug-using-the-just-in-time-debugger?view=vs-2019#jit_errors](https://docs.microsoft.com/en-us/visualstudio/debugger/debug-using-the-just-in-time-debugger?view=vs-2019#jit_errors)


Alternatively:


```
perl mysql-test-run.pl  <test_name> --devenv
```

(devenv.exe needs to be in PATH)


or, if you prefer WinDBG


```
perl mysql-test-run.pl  <test_name> --windbg
```
