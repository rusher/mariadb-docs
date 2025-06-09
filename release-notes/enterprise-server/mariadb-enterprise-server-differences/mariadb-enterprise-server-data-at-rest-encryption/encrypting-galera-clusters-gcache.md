# Encrypting Galera Cluster's GCache

##

## Overview

[MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) and MariaDB Community Server support data-at-rest encryption, which secures data on the file system. The server and storage engines encrypt data before writes and decrypt it during reads, ensuring that the data is only unencrypted when accessed directly through the server.

In many versions of MariaDB Server, the GCache used by [Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) does not support data-at-rest encryption.

However, [MariaDB Enterprise Server 10.4](../../10-4/) and later support an enterprise version of Galera 4, which adds support for encrypting the GCache.

In those versions, the GCache supports the following data-at-rest encryption features:

* The GCache can be automatically encrypted.

For more information, see the following resources:

* Enabling GCache Encryption
* Disabling GCache Encryption

Copyright © 2025 MariaDB
