# MariaDB Enterprise Cluster Security

{% hint style="info" %}
The features described on this page are available from MariaDB Enterprise Server 10.6.
{% endhint %}

MariaDB Enterprise Cluster, powered by Galera, adds some security features:

* New TLS Modes have been implemented, which can be used to configure mandatory TLS and X.509 certificate verification for Enterprise Cluster:
  * [WSREP TLS Modes](mariadb-enterprise-cluster-security.md#wsrep-tls-modes) have been implemented for Enterprise Cluster replication traffic.
  * [SST TLS Modes](mariadb-enterprise-cluster-security.md#sst-tls-modes) have been implemented for SSTs that use MariaDB Enterprise Backup or Rsync.
* [Cluster name verification](mariadb-enterprise-cluster-security.md#cluster-name-verification) checks that a Joiner node belongs to the cluster prior to performing a State Snapshot Transfer (SST) or an Incremental State Transfer (IST).
* [Certificate expiration warnings](mariadb-enterprise-cluster-security.md#certificate-expiration-warnings) are written to the MariaDB error log when the node's X.509 certificate is close to expiration.
* TLS can be [enabled without downtime](mariadb-enterprise-cluster-security.md#enable-tls-without-downtime) for Enterprise Cluster replication traffic.

### WSREP TLS Modes

MariaDB Enterprise Cluster, powered by Galera, adds the [wsrep\_ssl\_mode](../reference/wsrep_ssl_mode.md) system variable, which configures the WSREP TLS Mode used for Enterprise Cluster replication traffic.

The following WSREP TLS Modes are supported:

| **WSREP TLS Mode**                                                                             | **Values**                                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Provider](mariadb-enterprise-cluster-security.md#wsrep-tls-modes-provider)                    | <ul><li><code>PROVIDER</code></li></ul>    | <ul><li>TLS is optional for Enterprise Cluster replication traffic.</li><li>Each node obtains its TLS configuration from the <a href="../reference/wsrep_provider_options.md">wsrep_provider_options</a> system variable. When the provider is not configured to use TLS on a node, the node will connect to the cluster without TLS.</li><li>The Provider WSREP TLS Mode is backward compatible with ES 10.5 and earlier. When performing a rolling upgrade from ES 10.5 and earlier, the Provider WSREP TLS Mode can be configured on the upgraded nodes.</li></ul> |
| [Server](mariadb-enterprise-cluster-security.md#wsrep-tls-modes-server-and-server-x.509)       | <ul><li><code>SERVER</code></li></ul>      | <ul><li>TLS is mandatory for Enterprise Cluster replication traffic, but X.509 certificate verification is not performed.</li><li>Each node obtains its TLS configuration from the node's MariaDB Enterprise Server configuration. When MariaDB Enterprise Server is not configured to use TLS on a node, the node will fail to connect to the cluster.</li><li>The Server WSREP TLS Mode is the default in ES 10.6.</li></ul>                                                                                                                                        |
| [Server X.509](mariadb-enterprise-cluster-security.md#wsrep-tls-modes-server-and-server-x.509) | <ul><li><code>SERVER_X509</code></li></ul> | <ul><li>TLS and X.509 certificate verification are mandatory for Enterprise Cluster replication traffic.</li><li>Each node obtains its TLS configuration from the node's MariaDB Enterprise Server configuration. When MariaDB Enterprise Server is not configured to use TLS on a node, the node will fail to connect to the cluster.</li></ul>                                                                                                                                                                                                                      |

#### WSREP TLS Modes: Provider

MariaDB Enterprise Cluster supports the Provider `WSREP TLS` Mode, which is equivalent to Enterprise Cluster's TLS implementation in earlier versions of MariaDB Server. The Provider `WSREP TLS` Mode is primarily intended for backward compatibility, and it is most useful for users who need to perform a rolling upgrade to Enterprise Server 10.6.

The Provider `WSREP TLS` Mode can be configured by setting the [wsrep\_ssl\_mode](../reference/wsrep_ssl_mode.md) system variable to `PROVIDER`.

TLS is optional in the Provider `WSREP TLS` Mode. When the provider is not configured to use TLS on a node, the node will connect to the cluster without TLS.

Each node obtains its TLS configuration from the [wsrep\_provider\_options](../reference/wsrep_provider_options.md) system variable. The following options are used:

|                                                     |                                                                   |
| --------------------------------------------------- | ----------------------------------------------------------------- |
| [socket.ssl](../reference/socket.ssl.md)            | Set this option to `true` to enable TLS.                          |
| [socket.ssl\_ca](../reference/socket.ssl_ca.md)     | Set this option to the path of the CA chain file.                 |
| [socket.ssl\_cert](../reference/socket.ssl_cert.md) | Set this option to the path of the node's X.509 certificate file. |
| [socket.ssl\_key](../reference/socket.ssl_key.md)   | Set this option to the path of the node's private key file.       |

For example:

```ini
[mariadb]
...
wsrep_ssl_mode = PROVIDER
wsrep_provider_options = "socket.ssl=true;socket.ssl_cert=/certs/server-cert.pem;socket.ssl_ca=/certs/ca-cert.pem;socket.ssl_key=/certs/server-key.pem"
```

#### WSREP TLS Modes: Server and Server X.509

MariaDB Enterprise Cluster adds the Server and Server X.509 `WSREP TLS` Modes for users who require mandatory TLS.

The Server `WSREP TLS` Mode can be configured by setting the [wsrep\_ssl\_mode](../reference/wsrep_ssl_mode.md) system variable to `SERVER`. In the Server `WSREP TLS` Mode, TLS is mandatory, but X.509 certificate verification is not performed. The Server `WSREP TLS` Mode is the default.

The Server X.509 `WSREP TLS` Mode can be configured by setting the [wsrep\_ssl\_mode](../reference/wsrep_ssl_mode.md) system variable to `SERVER_X509`. In the Server X.509 `WSREP TLS` Mode, TLS and X.509 certification verification are mandatory.

TLS is mandatory in both the Server and Server X.509 `WSREP TLS` Modes. When MariaDB Enterprise Server is not configured to use TLS on a node, the node will fail to connect to the cluster.

Each node obtains its TLS configuration from the node's MariaDB Enterprise Server configuration. The following system variables are used:

| **System Variable**                       | **Description**                                                                                                                                                                                                                                           |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ssl\_ca](../reference/ssl_ca.md)         | Set this system variables to the path of the CA chain file.                                                                                                                                                                                               |
| [ssl\_capath](../reference/ssl_capath.md) | Optionally set this system variables to the path of the CA chain directory. The directory must have been processed by `openssl rehash`. When your CA chain is stored in a single file, use the [ssl\_ca](../reference/ssl_ca.md) system variable instead. |
| [ssl\_cert](../reference/ssl_cert.md)     | Set this system variable to the path of the node's X.509 certificate file.                                                                                                                                                                                |
| [ssl\_key](../reference/ssl_key.md)       | Set this system variable to the path of the node's private key file.                                                                                                                                                                                      |

For example:

```ini
[mariadb]
...
wsrep_ssl_mode = SERVER_X509

ssl_ca = /certs/ca-cert.pem
ssl_cert = /certs/server-cert.pem
ssl_key = /certs/server-key.pem
```

### SST TLS Modes

MariaDB Enterprise Cluster, powered by Galera, adds the `ssl-mode` option, which configures the SST TLS Mode for State Snapshot Transfers (SSTs). The `ssl-mode` option is supported by the following SST methods, which can be configured using the [wsrep\_sst\_method](../reference/wsrep_sst_method.md) system variable:

| **SST Method**            | [wsrep\_sst\_method](../reference/wsrep_sst_method.md) |
| ------------------------- | ------------------------------------------------------ |
| MariaDB Enterprise Backup | `mariabackup`                                          |
| Rsync                     | `rsync`                                                |

The following SST TLS Modes are supported:

| **SST TLS Mode**                                                                                | **Values**                                                                    | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Backward Compatible](mariadb-enterprise-cluster-security.md#sst-tls-modes-backward-compatible) | <ul><li><code>DISABLED</code></li><li>Not set</li></ul>                       | <ul><li>TLS is optional for SST traffic.</li><li>Each node obtains its TLS configuration from the <code>tca</code>, <code>tcert</code>, and <code>tkey</code> options. When the SST is not configured to use TLS on a node, the node will connect during the SST without TLS.</li><li>The Backward Compatible SST TLS Mode is backward compatible with ES 10.5 and earlier, so it is suitable for rolling upgrades.</li><li>The Backward Compatible SST TLS Mode is the default in ES 10.6.</li></ul> |
| [Server](mariadb-enterprise-cluster-security.md#sst-tls-modes-server-and-server-x.509)          | <ul><li><code>REQUIRED</code></li></ul>                                       | <ul><li>TLS is mandatory for SST traffic, but X.509 certificate verification is not performed.</li><li>Each node obtains its TLS configuration from the node's MariaDB Enterprise Server configuration. When MariaDB Enterprise Server is not configured to use TLS on a node, the node will fail to connect during an SST.</li></ul>                                                                                                                                                                 |
| [Server X.509](mariadb-enterprise-cluster-security.md#sst-tls-modes-server-and-server-x.509)    | <ul><li><code>VERIFY_CA</code></li><li><code>VERIFY_IDENTITY</code></li></ul> | <ul><li>TLS and X.509 certification verification are mandatory for SST traffic.</li><li>Each node obtains its TLS configuration from the node's MariaDB Enterprise Server configuration. When MariaDB Enterprise Server is not configured to use TLS on a node, the node will fail to connect during an SST.</li><li>Prior to the state transfer, the Donor node will verify the Joiner node's X.509 certificate, and the Joiner node will verify the Donor node's X.509 certificate.</li></ul>       |

#### SST TLS Modes: Backward Compatible

In MariaDB Enterprise Server 10.6, MariaDB Enterprise Cluster adds the Backward Compatible SST TLS Mode for SSTs that use MariaDB Enterprise Backup or Rsync. The Backward Compatible SST TLS Mode is primarily intended for backward compatibility with ES 10.5 and earlier, and it is most useful for users who need to perform a rolling upgrade to ES 10.6.

The Backward Compatible SST TLS Mode is the default, but it can also be configured by setting the `ssl_mode` option to `DISABLED` in a configuration file in the `[sst]` group.

TLS is optional in the Backward Compatible SST TLS Mode. When the SST is not configured to use TLS, the SST will occur without TLS.

Each node obtains its TLS configuration from a configuration file in the `[sst]` group. The following options are used:

| **Option** | **Description**                                                   |
| ---------- | ----------------------------------------------------------------- |
| `tca`      | Set this option to the path of the CA chain file.                 |
| `tcert`    | Set this option to the path of the node's X.509 certificate file. |
| `tkey`     | Set this option to the path of the node's private key file.       |

For example:

```ini
[mariadb]
...
wsrep_sst_method = mariabackup
wsrep_sst_auth = mariabackup:mypassword

[sst]
ssl_mode = DISABLED

tca = /certs/ca-cert.pem
tcert = /certs/server-cert.pem
tkey = /certs/server-key.pem
```

#### SST TLS Modes: Server and Server X.509

MariaDB Enterprise Cluster adds the Server and Server X.509 SST TLS Modes for SSTs that use MariaDB Enterprise Backup or Rsync. The Server and Server X.509 `SST TLS` Modes are intended for users who require mandatory TLS.

The Server `SST TLS` Mode can be configured by setting the `ssl_mode` option to `REQUIRED` in a configuration file in the `[sst]` group. In the Server SST TLS Mode, TLS is mandatory, but X.509 certificate verification is not performed.

The Server X.509 SST TLS Mode can be configured by setting the `ssl_mode` option to `VERIFY_CA` or `VERIFY_IDENTITY` in a configuration file in the `[sst]` group. In the Server X.509 SST TLS Mode, TLS and X.509 certification verification are mandatory. Prior to the state transfer, the Donor node will verify the Joiner node's X.509 certificate, and the Joiner node will verify the Donor node's X.509 certificate.

TLS is mandatory in both the Server and Server X.509 `SST TLS` Modes. When MariaDB Enterprise Server is not configured to use TLS on a node, the node will fail to connect during an SST.

Each node obtains its TLS configuration from the node's MariaDB Enterprise Server configuration. The following system variables are used:

| **System Variable**                                                                     | **Description**                                                            |
| --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| [ssl\_ca](https://docs-archive.mariadb.net/server/ref/mdb/system-variables/ssl_ca/)     | Set this system variables to the path of the CA chain file.                |
| [ssl\_cert](https://docs-archive.mariadb.net/server/ref/mdb/system-variables/ssl_cert/) | Set this system variable to the path of the node's X.509 certificate file. |
| [ssl\_key](https://docs-archive.mariadb.net/server/ref/mdb/system-variables/ssl_key/)   | Set this system variable to the path of the node's private key file.       |

For example:

```ini
[mariadb]
...
wsrep_sst_method = mariabackup
wsrep_sst_auth = mariabackup:mypassword

ssl_ca = /certs/ca-cert.pem
ssl_cert = /certs/server-cert.pem
ssl_key = /certs/server-key.pem

[sst]
ssl_mode = VERIFY_CA
```

When the [backward-compatible TLS parameters in the \[sst\] group](mariadb-enterprise-cluster-security.md#sst-tls-modes-backward-compatible) are configured, the Server and Server X.509 SST TLS Modes use those parameters instead of the MariaDB Enterprise Server system variables. In that case, the following message will be written to the [MariaDB error log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log):

```
new ssl configuration options (ssl-ca, ssl-cert and ssl-key) are ignored by SST due to presence of the tca, tcert and/or tkey in the [sst] section
```

### Cluster Name Verification

MariaDB Enterprise Cluster, powered by Galera, adds cluster name verification for Joiner nodes, which ensures that the Joiner node does not perform a State Snapshot Transfer (SST) or an Incremental State Transfer (IST) for the wrong cluster.

Prior to performing a State Snapshot Transfer (SST) or Incremental State Transfer (IST), the Donor node verifies the [wsrep\_cluster\_name](https://docs-archive.mariadb.net/server/ref/mdb/system-variables/wsrep_cluster_name/) value configured by the Joiner node to verify that the node belongs to the cluster.

### Certificate Expiration Warnings

MariaDB Enterprise Cluster, powered by Galera, can be configured to write certificate expiration warnings to the [MariaDB Error Log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log) when the node's X.509 certificate is close to expiration.

Certificate expiration warnings can be configured using the [wsrep\_certificate\_expiration\_hours\_warning](../reference/wsrep_certificate_expiration_hours_warning.md) system variable:

* When the `wsrep_certificate_expiration_hours_warning` system variable is set to `0`, certificate expiration warnings are not printed to the MariaDB Error Log.
* When the `wsrep_certificate_expiration_hours_warning` system variable is set to a value `N`, which is greater than `0`, certificate expiration warnings are printed to the MariaDB Error Log when the node's certificate expires in `N` hours or less.

For example:

```ini
[mariadb]
...
# warn 3 days before certificate expiration
wsrep_certificate_expiration_hours_warning=72
```

### Enable TLS without Downtime

MariaDB Enterprise Cluster, powered by Galera, adds new capabilities that allow TLS to be enabled for Enterprise Cluster replication traffic without downtime.

Enabling TLS without downtime relies on two new options implemented for the [wsrep\_provider\_options](../reference/wsrep_provider_options.md) system variable:

| **Option**          | **Dynamic?** | **Default** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------- | ------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `socket.dynamic`    | No           | `false`     | <ul><li>When set to <code>true</code>, the node will allow TLS and non-TLS communications at the same time.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `socket.ssl_reload` | Yes          | N/A         | <ul><li>When set to <code>true</code> with the <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set#global-session">SET GLOBAL</a> statement, Enterprise Cluster dynamically re-initializes its TLS context.</li><li>This is most useful if you need to replace a certificate that is about to expire without restarting the server.</li><li>The paths to the certificate and key files cannot be changed dynamically, so the updated certificates and keys must be placed at the same paths defined by the relevant TLS variables.</li></ul> |

\
