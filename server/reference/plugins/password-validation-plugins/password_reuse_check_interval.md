
# password_reuse_check_interval

The password_reuse_check_interval system variable is available when the [password_reuse_check plugin](password-reuse-check-plugin.md) is installed. It determines the retention period for the password history in days. Zero, the default, means passwords are never discarded.


* Commandline: `--password_reuse_check_interval=#`
* Scope: Global
* Read-only: No
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `36500`



CC BY-SA / Gnu FDL

