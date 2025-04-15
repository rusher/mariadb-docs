
# password_reuse_check_interval

The password_reuse_check_interval system variable is available when the [password_reuse_check plugin](password-reuse-check-plugin.md) is installed. It determines the retention period for the password history in days. Zero, the default, means passwords are never discarded.


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--password_reuse_check_interval=#</code>`
* Scope: Global
* Read-only: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>36500</code>`


