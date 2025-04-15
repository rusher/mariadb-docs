
# S3 Storage Engine System Variables


##### MariaDB starting with [10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)
The [S3 storage engine](s3-storage-engine-status-variables.md) has been available since [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md).



This page documents system variables related to the [S3 storage engine](s3-storage-engine-status-variables.md).


See [Server System Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting system variables.


Also see the [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md)


## Variables


#### `<code>s3_access_key</code>`


* Description: The AWS access key to access your data. See [mariadbd startup options for S3](using-the-s3-storage-engine.md#mariadbd-startup-options-for-s3).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-access-key=val</code>`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: (Empty)
* Introduced: [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)



#### `<code>s3_block_size</code>`


* Description: The default block size for a table, if not specified in [CREATE TABLE](../../sql-statements-and-structure/vectors/create-table-with-vectors.md). Set to 4M as default. See [mysqld startup options for S3](using-the-s3-storage-engine.md#mysqld-startup-options-for-s3).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-block-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Numeric
* Default Value: `<code>4194304</code>`
* Range: `<code>4194304</code>` to `<code>16777216</code>`
* Introduced: [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)



#### `<code>s3_bucket</code>`


* Description: The AWS bucket where your data should be stored. All MariaDB table data is stored in this bucket. See [mysqld startup options for S3](using-the-s3-storage-engine.md#mysqld-startup-options-for-s3).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-bucket=val</code>`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: `<code>MariaDB</code>`
* Introduced: [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)



#### `<code>s3_debug</code>`


* Description: Generates a trace file from libmarias3 on stderr (mysqld.err) for debugging the S3 protocol.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-debug=[0|1]</code>`
* Scope: Global
* Dynamic:

  * Yes (>= [MariaDB 10.6.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md), [MariaDB 10.11.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md), [MariaDB 11.0.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes.md), [MariaDB 11.1.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes.md), [MariaDB 11.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes.md), [MariaDB 11.3.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes.md), [MariaDB 11.4.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-1-release-notes.md))
  * No (<= [MariaDB 10.6.16](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md), [MariaDB 10.11.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-6-release-notes.md), [MariaDB 11.0.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes.md), [MariaDB 11.1.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes.md), [MariaDB 11.2.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes.md), [MariaDB 11.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-1-release-notes.md))
* Data Type: Boolean
* Valid Values: 0 or 1
* Default Value: `<code>0</code>`
* Introduced: [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)



#### `<code>s3_host_name</code>`


* Description: Hostname for the S3 service. "s3.amazonaws.com", Amazon S3 service, by default
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-host-name=val</code>`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: `<code>s3.amazonaws.com</code>`
* Introduced: [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)



#### `<code>s3_no_content_type</code>`


* Description: If true (false is default), disables the Content-Type header, required for some providers.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-no-content-type=[0|1]</code>`
* Scope: Global
* Dynamic: No
* Data Type: Boolean
* Default Value: `<code>0</code>`
* Introduced: [MariaDB 11.6.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes.md)



#### `<code>s3_pagecache_age_threshold</code>`


* Description: This characterizes the number of hits a hot block has to be untouched until it is considered aged enough to be downgraded to a warm block. This specifies the percentage ratio of that number of hits to the total number of blocks in the page cache.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-pagecache-age-threshold=val</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Numeric
* Default Value: `<code>300</code>`
* Range: `<code>100</code>` to `<code>18446744073709551615</code>`
* Introduced: [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)



#### `<code>s3_pagecache_buffer_size</code>`


* Description: The size of the buffer used for index blocks for S3 tables. Increase this to get better index handling (for all reads and multiple writes) to as much as you can afford. Size can be adjusted in blocks of `<code>8192</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-pagecache-buffer-size=val</code>`
* Scope: Global
* Dynamic: No
* Data Type: Numeric
* Default Value: `<code>134217728</code>` (128M)
* Range: `<code>33554432</code>` to `<code>18446744073709551615</code>`
* Introduced: [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)



#### `<code>s3_pagecache_division_limit</code>`


* Description: The minimum percentage of warm blocks in key cache.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-pagecache-division-limit=val</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Numeric
* Default Value: `<code>100</code>`
* Range: `<code>1</code>` to `<code>100</code>`
* Introduced: [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)



#### `<code>s3_pagecache_file_hash_size</code>`


* Description: Number of hash buckets for open files. Default 512. If you have a lot of S3 files open you should increase this for faster flush of changes. A good value is probably 1/10 of number of possible open S3 files.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-pagecache-file-hash-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: Numeric
* Default Value: `<code>512</code>`
* Range: `<code>32</code>` to `<code>16384</code>`
* Introduced: [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)



#### `<code>s3_port</code>`


* Description: The TCP port number on the S3 host to connect to. A values of 0 means determine automatically.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-port=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: Numeric
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>65535</code>`
* Introduced: [MariaDB 10.5.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1057-release-notes.md)



#### `<code>s3_protocol_version</code>`


* Description: Protocol used to communication with S3. "Auto" is the default. If you get errors like "8 Access Denied" when you are connecting to another service provider, then try to change this option. The reason for this variable is that Amazon has changed some parts of the S3 protocol since they originally introduced it but other service providers are still using the original protocol. Can also be set numerically.

  * `<code>Auto</code>` (`<code>0</code>`):
  * `<code>Original</code>` or (`<code>1</code>`): Same as "Auto". Deprecated from [MariaDB 10.6.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md), [MariaDB 10.11.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md), [MariaDB 11.0.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes.md), [MariaDB 11.1.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes.md), [MariaDB 11.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes.md), [MariaDB 11.3.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes.md), [MariaDB 11.4.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-1-release-notes.md).
  * `<code>Amazon</code>` (`<code>2</code>`) Same as "Auto". Deprecated from [MariaDB 10.6.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md), [MariaDB 10.11.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md), [MariaDB 11.0.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes.md), [MariaDB 11.1.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes.md), [MariaDB 11.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes.md), [MariaDB 11.3.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes.md), [MariaDB 11.4.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-1-release-notes.md).
  * `<code>Legacy</code>` (`<code>3</code>`): v1 protocol. From [MariaDB 10.6.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md), [MariaDB 10.11.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md), [MariaDB 11.0.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes.md), [MariaDB 11.1.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes.md), [MariaDB 11.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes.md), [MariaDB 11.3.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes.md), [MariaDB 11.4.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-1-release-notes.md)
  * `<code>Path</code>` (`<code>4</code>`): From [MariaDB 10.6.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md), [MariaDB 10.11.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md), [MariaDB 11.0.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes.md), [MariaDB 11.1.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes.md), [MariaDB 11.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes.md), [MariaDB 11.3.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes.md), [MariaDB 11.4.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-1-release-notes.md)
  * `<code>Domain</code>` (`<code>5</code>`): From [MariaDB 10.6.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md), [MariaDB 10.11.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md), [MariaDB 11.0.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes.md), [MariaDB 11.1.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes.md), [MariaDB 11.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes.md), [MariaDB 11.3.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes.md), [MariaDB 11.4.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-1-release-notes.md)
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-protocol-version=val</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Enum
* Valid Values:

  * `<code>Auto</code>`(`<code>0</code>`) , `<code>Original</code>` (`<code>1</code>`), `<code>Amazon</code>` (`<code>2</code>`), `<code>Legacy</code>` (`<code>3</code>`), `<code>Path</code>` (`<code>4</code>`), `<code>Domain</code>` (`<code>5</code>`) (>= [MariaDB 10.6.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md), [MariaDB 10.11.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md), [MariaDB 11.0.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes.md), [MariaDB 11.1.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes.md), [MariaDB 11.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes.md), [MariaDB 11.3.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes.md), [MariaDB 11.4.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-1-release-notes.md))
  * `<code>Auto</code>`, `<code>Original</code>`, `<code>Amazon</code>` (<= [MariaDB 10.6.16](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md), [MariaDB 10.11.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-6-release-notes.md), [MariaDB 11.0.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes.md), [MariaDB 11.1.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes.md), [MariaDB 11.2.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes.md), [MariaDB 11.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-1-release-notes.md))
* Default Value: `<code>Auto</code>`
* Introduced: [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)



#### `<code>s3_provider</code>`


* Description: Enable S3 provider specific compatibility tweaks. "Default", "Amazon", or "Huawei".

  * `<code>Default</code>`:
  * `<code>Amazon</code>`: Effectively sets [s3_protocol_version](s3-storage-engine-system-variables.md#s3_protocol_version) to `<code>5</code>` (`<code>Domain</code>`), overriding any other setting it may have.
  * `<code>Huawei</code>`: Effectively sets [s3_no_content_type](s3-storage-engine-system-variables.md#s3_no_content_type) to 1, overriding any other setting it may have.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-provider=val</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: enum
* Valid Values: `<code>Default</code>`, `<code>Amazon</code>`, `<code>Huawei</code>`
* Default Value: `<code>Default</code>`
* Introduced: [MariaDB 10.6.20](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-20-release-notes.md), [MariaDB 10.11.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-10-release-notes.md), [MariaDB 11.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes.md), [MariaDB 11.4.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-4-release-notes.md), [MariaDB 11.6.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes.md)



#### `<code>s3_region</code>`


* Description: The AWS region where your data should be stored. See [mysqld startup options for S3](using-the-s3-storage-engine.md#mysqld-startup-options-for-s3).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-region=val</code>`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: (Empty)
* Introduced: [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)



#### `<code>s3_replicate_alter_as_create_select</code>`


* Description: When converting S3 table to local table, log all rows in binary log. This allows the slave to replicate `<code class="fixed" style="white-space:pre-wrap">CREATE TABLE .. SELECT FROM s3_table</code>` even it the slave doesn't have access to the original `<code class="fixed" style="white-space:pre-wrap">s3_table</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-replicate-alter-as-create-select=[0|1]</code>`
* Scope: Global
* Dynamic: No
* Data Type: Boolean
* Default Value: `<code>1</code>`
* Introduced: [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)



#### `<code>s3_secret_key</code>`


* Description: The AWS secret key to access your data. See [mysqld startup options for S3](using-the-s3-storage-engine.md#mysqld-startup-options-for-s3).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-secret-key=val</code>`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: (Empty)
* Introduced: [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)



#### `<code>s3_slave_ignore_updates</code>`


* Description: Should be set if master and slave share the same S3 instance. This tells the slave that it can ignore any updates to the S3 tables as they are already applied on the master.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-slave-ignore-updates=[0|1]</code>`
* Scope: Global
* Dynamic: No
* Data Type: Boolean
* Default Value: `<code>0</code>`
* Introduced: [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)



#### `<code>s3_ssl_no_verify</code>`


* Description: If true, SSL certificate verification for the S3 endpoint is disabled
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-ssl-no-verify=[0|1]</code>`
* Scope: Global
* Dynamic: No
* Data Type: Boolean
* Default Value: `<code>0</code>`
* Introduced: [MariaDB 10.6.20](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-20-release-notes.md), [MariaDB 10.11.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-10-release-notes.md), [MariaDB 11.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes.md), [MariaDB 11.4.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-4-release-notes.md), [MariaDB 11.6.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes.md)



#### `<code>s3_use_http</code>`


* Description: If enabled, HTTP will be used instead of HTTPS.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--s3-use-http=[0|1]</code>`
* Scope: Global
* Dynamic: No
* Data Type: Boolean
* Default Value: `<code>0</code>`
* Introduced: [MariaDB 10.5.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1057-release-notes.md)



## See Also


[Using the S3 Storage Engine](using-the-s3-storage-engine.md)

