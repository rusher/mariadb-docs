# Building MariaDB on Solaris and OpenSolaris

The following two articles should help you get your Solaris machine prepared to build MariaDB (just ignore the parts about installing buildbot):

* [Buildbot Setup for Solaris Sparc](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/general-info/tools/buildbot/setup/buildbot-setup-for-solaris-sparc)
* [Buildbot Setup for Solaris x86](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/general-info/tools/buildbot/setup/buildbot-setup-for-solaris-x86)

## Notes

* The BUILD dir contains various scripts for compiling MariaDB on Solaris. The `BUILD/compile-solaris-amd64` and `BUILD/compile-solaris-amd64-debug` are probably the most useful.
* The scripts do not play nice with non-bash shells such as the Korn Shell (ksh). So if your `/bin/sh` is pointing at `ksh` or `ksh93`, you'll want to change it so that it points at bash.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
