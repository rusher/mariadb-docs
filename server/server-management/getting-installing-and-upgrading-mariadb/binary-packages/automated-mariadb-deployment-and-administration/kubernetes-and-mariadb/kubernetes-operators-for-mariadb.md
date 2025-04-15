# Kubernetes Operators for MariaDB

Operators basically instruct Kubernetes about how to manage a certain technology. Kubernetes comes with some default operators, but it is possible to create custom operators. Operators created by the community can be found on [OperatorHub.io](https://operatorhub.io/).

#

# Custom Operators

Kubernetes provides a declarative API. To support a specific (i.e. MariaDB) technology or implement a desired behavior (i.e. provisioning a [replica](/kb/en/standard-replication/)), we extend Kubernetes API. This involves creating two main components:

* A custom resource.
* A custom controller.

A custom resource adds an API endpoint, so the resource can be managed via the API server. It includes functionality to get information about the resource, like a list of the existing servers.

A custom controller implements the checks that must be performed against the resource to check if its state should be corrected using the API. In the case of MariaDB, some reasonable checks would be verifying that it accepts connections, replication is running, and a server is (or is not) read only.

#

# MariaDB Operator

[mariadb-operator](https://github.com/mariadb-operator/mariadb-operator) is a Kubernetes operator that allows you to run and operate MariaDB in a cloud native way. It aims to declaratively manage MariaDB instances using Kubernetes CRDs instead of imperative commands.

It's available in both [Artifact Hub](https://artifacthub.io/packages/helm/mariadb-operator/mariadb-operator) and [Operator Hub](https://operatorhub.io/operator/mariadb-operator) and supports the following features:

* [Easily provision](https://github.com/mariadb-operator/mariadb-operator/blob/main/examples/manifests/mariadb_minimal.yaml) and [configure](https://github.com/mariadb-operator/mariadb-operator/blob/main/examples/manifests/mariadb_full.yaml) MariaDB servers in Kubernetes.
* Multiple [HA modes](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/HA.md): Galera Cluster or MariaDB Replication.
* Automated [primary failover](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/HA.md) and [cluster recovery](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/GALERA.md#galera-cluster-recovery).
* Advanced HA with [MaxScale](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/MAXSCALE.md): a sophisticated database proxy, router, and load balancer for MariaDB.
* Flexible [storage](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/STORAGE.md) configuration. [Volume expansion](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/STORAGE.md#volume-resize).
* Take, restore, and schedule [backups](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/BACKUP.md).
* Multiple [backup storage types](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/BACKUP.md#storage-types): S3 compatible, PVCs, and Kubernetes volumes.
* Policy-driven [backup retention](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/BACKUP.md#retention-policy) with [compression options](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/BACKUP.md#compression): bzip2 and gzip.
* [Target recovery time](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/BACKUP.md#target-recovery-time): restore the closest available backup to the specified time.
* [Bootstrap new instances](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/BACKUP.md#bootstrap-new-mariadb-instances-from-backups) from: backups, S3, PVCs...
* [Cluster-aware rolling update](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/UPDATES.md#replicasfirstprimarylast): roll out replica Pods one by one, wait for each of them to become ready, and then proceed with the primary Pod.
* Multiple [update strategies](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/UPDATES.md#update-strategies): `ReplicasFirstPrimaryLast`, `OnDelete`, and `Never`.
* Automated [data-plane updates](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/UPDATES.md#auto-update-data-plane).
* [my.cnf change detection](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/CONFIGURATION.md#mycnf): automatically trigger [updates](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/UPDATES.md) when my.cnf changes.
* [Suspend](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/SUSPEND.md) operator reconciliation for maintenance operations.
* Issue, configure, and rotate [TLS certificates](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/TLS.md) and CAs.
* Native integration with [cert-manager](https://github.com/cert-manager/cert-manager): automatically create `Certificate` resources.
* [Prometheus metrics](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/METRICS.md) via [mysqld-exporter](https://github.com/prometheus/mysqld_exporter) and maxscale-exporter.
* Native integration with [prometheus-operator](https://github.com/prometheus-operator/prometheus-operator): automatically create `ServiceMonitor` resources.
* Declaratively manage [SQL resources](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/SQL_RESOURCES.md): [users](https://github.com/mariadb-operator/mariadb-operator/blob/main/examples/manifests/user.yaml), [grants](https://github.com/mariadb-operator/mariadb-operator/blob/main/examples/manifests/grant.yaml), and logical [databases](https://github.com/mariadb-operator/mariadb-operator/blob/main/examples/manifests/database.yaml).
* Configure [connections](https://github.com/mariadb-operator/mariadb-operator/blob/main/examples/manifests/connection.yaml) for your applications.
* Orchestrate and schedule [SQL scripts](https://github.com/mariadb-operator/mariadb-operator/blob/main/examples/manifests/sqljobs).
* Validation webhooks to provide CRD immutability.
* Additional printer columns to report the current CRD status.
* CRDs designed according to the Kubernetes [API conventions](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md).
* Install it using [helm](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/HELM.md), [OLM](https://operatorhub.io/operator/mariadb-operator), or [static manifests](https://github.com/mariadb-operator/mariadb-operator/tree/main/deploy/manifests).
* Multiple [deployment modes](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/HELM.md#deployment-modes): cluster-wide and single namespace.
* Multi-arch distroless [image](https://github.com/orgs/mariadb-operator/packages/container/package/mariadb-operator).
* [GitOps](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/GITOPS.md) friendly.

Please, refer to the [documentation](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/), the [API reference](https://github.com/mariadb-operator/mariadb-operator/tree/main/docs/API_REFERENCE.md) and the [example suite](https://github.com/mariadb-operator/mariadb-operator/blob/main/examples/) for further detail.

Content initially contributed by [Vettabase Ltd](https://vettabase.com/). Updated 11/6/24 by MariaDB.