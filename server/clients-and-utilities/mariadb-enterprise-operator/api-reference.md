# API Reference

## Packages

* [enterprise.mariadb.com/v1alpha1](api-reference.md#enterprisemariadbcomv1alpha1)

## enterprise.mariadb.com/v1alpha1

Package v1alpha1 contains API Schema definitions for the v1alpha1 API group

### Resource Types

* [Backup](api-reference.md#backup)
* [Connection](api-reference.md#connection)
* [Database](api-reference.md#database)
* [Grant](api-reference.md#grant)
* [MariaDB](api-reference.md#mariadb)
* [MaxScale](api-reference.md#maxscale)
* [Restore](api-reference.md#restore)
* [SqlJob](api-reference.md#sqljob)
* [User](api-reference.md#user)

#### Affinity

Refer to the Kubernetes docs: [#affinity-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#affinity-v1-core).

_Appears in:_

* [AffinityConfig](api-reference.md#affinityconfig)

| Field                                                               | Description | Default | Validation |
| ------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                               | Description | Default | Validation |
| podAntiAffinity [PodAntiAffinity](api-reference.md#podantiaffinity) |             |         |            |
| nodeAffinity [NodeAffinity](api-reference.md#nodeaffinity)          |             |         |            |

#### AffinityConfig

AffinityConfig defines policies to schedule Pods in Nodes.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [Exporter](api-reference.md#exporter)
* [Job](api-reference.md#job)
* [JobPodTemplate](api-reference.md#jobpodtemplate)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScalePodTemplate](api-reference.md#maxscalepodtemplate)
* [MaxScaleSpec](api-reference.md#maxscalespec)
* [PodTemplate](api-reference.md#podtemplate)
* [RestoreSpec](api-reference.md#restorespec)
* [SqlJobSpec](api-reference.md#sqljobspec)

| Field                                                               | Description                                                                                                                                                                                                       | Default | Validation |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                               | Description                                                                                                                                                                                                       | Default | Validation |
| podAntiAffinity [PodAntiAffinity](api-reference.md#podantiaffinity) |                                                                                                                                                                                                                   |         |            |
| nodeAffinity [NodeAffinity](api-reference.md#nodeaffinity)          |                                                                                                                                                                                                                   |         |            |
| antiAffinityEnabled boolean                                         | AntiAffinityEnabled configures PodAntiAffinity so each Pod is scheduled in a different Node, enabling HA.Make sure you have at least as many Nodes available as the replicas to not end up with unscheduled Pods. |         |            |

#### Backup

Backup is the Schema for the backups API. It is used to define backup jobs and its storage.

| Field                                                                                                          | Description                                                   | Default | Validation |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                          | Description                                                   | Default | Validation |
| apiVersion string                                                                                              | enterprise.mariadb.com/v1alpha1                               |         |            |
| kind string                                                                                                    | Backup                                                        |         |            |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |         |            |
| spec [BackupSpec](api-reference.md#backupspec)                                                                 |                                                               |         |            |

#### BackupSpec

BackupSpec defines the desired state of Backup

_Appears in:_

* [Backup](api-reference.md#backup)

| Field                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                          | Default   | Validation                      |
| ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------- |
| Field                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                          | Default   | Validation                      |
| args string array                                                                                                         | Args to be used in the Container.                                                                                                                                                                                                                                                                                                                                    |           |                                 |
| resources [ResourceRequirements](api-reference.md#resourcerequirements)                                                   | Resouces describes the compute resource requirements.                                                                                                                                                                                                                                                                                                                |           |                                 |
| securityContext [SecurityContext](api-reference.md#securitycontext)                                                       | SecurityContext holds security configuration that will be applied to a container.                                                                                                                                                                                                                                                                                    |           |                                 |
| podMetadata [Metadata](api-reference.md#metadata)                                                                         | PodMetadata defines extra metadata for the Pod.                                                                                                                                                                                                                                                                                                                      |           |                                 |
| imagePullSecrets [LocalObjectReference](api-reference.md#localobjectreference) array                                      | ImagePullSecrets is the list of pull Secrets to be used to pull the image.                                                                                                                                                                                                                                                                                           |           |                                 |
| podSecurityContext [PodSecurityContext](api-reference.md#podsecuritycontext)                                              | SecurityContext holds pod-level security attributes and common container settings.                                                                                                                                                                                                                                                                                   |           |                                 |
| serviceAccountName string                                                                                                 | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.                                                                                                                                                                                                                                                                                         |           |                                 |
| affinity [AffinityConfig](api-reference.md#affinityconfig)                                                                | Affinity to be used in the Pod.                                                                                                                                                                                                                                                                                                                                      |           |                                 |
| nodeSelector object (keys:string, values:string)                                                                          | NodeSelector to be used in the Pod.                                                                                                                                                                                                                                                                                                                                  |           |                                 |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array   | Tolerations to be used in the Pod.                                                                                                                                                                                                                                                                                                                                   |           |                                 |
| priorityClassName string                                                                                                  | PriorityClassName to be used in the Pod.                                                                                                                                                                                                                                                                                                                             |           |                                 |
| successfulJobsHistoryLimit integer                                                                                        | SuccessfulJobsHistoryLimit defines the maximum number of successful Jobs to be displayed.                                                                                                                                                                                                                                                                            |           | Minimum: 0                      |
| failedJobsHistoryLimit integer                                                                                            | FailedJobsHistoryLimit defines the maximum number of failed Jobs to be displayed.                                                                                                                                                                                                                                                                                    |           | Minimum: 0                      |
| timeZone string                                                                                                           | TimeZone defines the timezone associated with the cron expression.                                                                                                                                                                                                                                                                                                   |           |                                 |
| mariaDbRef [MariaDBRef](api-reference.md#mariadbref)                                                                      | MariaDBRef is a reference to a MariaDB object.                                                                                                                                                                                                                                                                                                                       |           | Required: {}                    |
| compression [CompressAlgorithm](api-reference.md#compressalgorithm)                                                       | Compression algorithm to be used in the Backup.                                                                                                                                                                                                                                                                                                                      |           | Enum: \[none bzip2 gzip]        |
| stagingStorage [BackupStagingStorage](api-reference.md#backupstagingstorage)                                              | StagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.It defaults to an emptyDir volume, meaning that the backups will be temporarily stored in the node where the Backup Job is scheduled.The staging area gets cleaned up after each backup is completed, consider this for sizing it appropriately. |           |                                 |
| storage [BackupStorage](api-reference.md#backupstorage)                                                                   | Storage defines the final storage for backups.                                                                                                                                                                                                                                                                                                                       |           | Required: {}                    |
| schedule [Schedule](api-reference.md#schedule)                                                                            | Schedule defines when the Backup will be taken.                                                                                                                                                                                                                                                                                                                      |           |                                 |
| maxRetention [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)            | MaxRetention defines the retention policy for backups. Old backups will be cleaned up by the Backup Job.It defaults to 30 days.                                                                                                                                                                                                                                      |           |                                 |
| databases string array                                                                                                    | Databases defines the logical databases to be backed up. If not provided, all databases are backed up.                                                                                                                                                                                                                                                               |           |                                 |
| ignoreGlobalPriv boolean                                                                                                  | IgnoreGlobalPriv indicates to ignore the mysql.global\_priv in backups.If not provided, it will default to true when the referred MariaDB instance has Galera enabled and otherwise to false.                                                                                                                                                                        |           |                                 |
| logLevel string                                                                                                           | LogLevel to be used n the Backup Job. It defaults to 'info'.                                                                                                                                                                                                                                                                                                         | info      |                                 |
| backoffLimit integer                                                                                                      | BackoffLimit defines the maximum number of attempts to successfully take a Backup.                                                                                                                                                                                                                                                                                   |           |                                 |
| restartPolicy [RestartPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#restartpolicy-v1-core) | RestartPolicy to be added to the Backup Pod.                                                                                                                                                                                                                                                                                                                         | OnFailure | Enum: \[Always OnFailure Never] |
| inheritMetadata [Metadata](api-reference.md#metadata)                                                                     | InheritMetadata defines the metadata to be inherited by children resources.                                                                                                                                                                                                                                                                                          |           |                                 |

#### BackupStagingStorage

BackupStagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [BootstrapFrom](api-reference.md#bootstrapfrom)
* [RestoreSource](api-reference.md#restoresource)
* [RestoreSpec](api-reference.md#restorespec)

| Field                                                                                         | Description                                              | Default | Validation |
| --------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------- | ---------- |
| Field                                                                                         | Description                                              | Default | Validation |
| persistentVolumeClaim [PersistentVolumeClaimSpec](api-reference.md#persistentvolumeclaimspec) | PersistentVolumeClaim is a Kubernetes PVC specification. |         |            |
| volume [StorageVolumeSource](api-reference.md#storagevolumesource)                            | Volume is a Kubernetes volume specification.             |         |            |

#### BackupStorage

BackupStorage defines the final storage for backups.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)

| Field                                                                                         | Description                                                               | Default | Validation |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                         | Description                                                               | Default | Validation |
| s3 [S3](api-reference.md#s3)                                                                  | S3 defines the configuration to store backups in a S3 compatible storage. |         |            |
| persistentVolumeClaim [PersistentVolumeClaimSpec](api-reference.md#persistentvolumeclaimspec) | PersistentVolumeClaim is a Kubernetes PVC specification.                  |         |            |
| volume [StorageVolumeSource](api-reference.md#storagevolumesource)                            | Volume is a Kubernetes volume specification.                              |         |            |

#### BasicAuth

KubernetesAuth refers to the basic authentication mechanism utilized for establishing a connection from the operator to the agent.

_Appears in:_

* [GaleraAgent](api-reference.md#galeraagent)

| Field                                                                                | Description                                              | Default | Validation |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------- | ------- | ---------- |
| Field                                                                                | Description                                              | Default | Validation |
| enabled boolean                                                                      | Enabled is a flag to enable BasicAuth                    |         |            |
| username string                                                                      | Username to be used for basic authentication             |         |            |
| passwordSecretKeyRef [GeneratedSecretKeyRef](api-reference.md#generatedsecretkeyref) | PasswordSecretKeyRef to be used for basic authentication |         |            |

#### BootstrapFrom

BootstrapFrom defines a source to bootstrap MariaDB from.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                                                                        | Description                                                                                                                                                                                                                                                | Default | Validation |
| ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                        | Description                                                                                                                                                                                                                                                | Default | Validation |
| backupRef [LocalObjectReference](api-reference.md#localobjectreference)                                      | BackupRef is a reference to a Backup object. It has priority over S3 and Volume.                                                                                                                                                                           |         |            |
| s3 [S3](api-reference.md#s3)                                                                                 | S3 defines the configuration to restore backups from a S3 compatible storage. It has priority over Volume.                                                                                                                                                 |         |            |
| volume [StorageVolumeSource](api-reference.md#storagevolumesource)                                           | Volume is a Kubernetes Volume object that contains a backup.                                                                                                                                                                                               |         |            |
| targetRecoveryTime [Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#time-v1-meta) | TargetRecoveryTime is a RFC3339 (1970-01-01T00:00:00Z) date and time that defines the point in time recovery objective.It is used to determine the closest restoration source in time.                                                                     |         |            |
| stagingStorage [BackupStagingStorage](api-reference.md#backupstagingstorage)                                 | StagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.It defaults to an emptyDir volume, meaning that the backups will be temporarily stored in the node where the Restore Job is scheduled. |         |            |
| restoreJob [Job](api-reference.md#job)                                                                       | RestoreJob defines additional properties for the Job used to perform the Restore.                                                                                                                                                                          |         |            |

#### CSIVolumeSource

Refer to the Kubernetes docs: [#csivolumesource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#csivolumesource-v1-core).

_Appears in:_

* [StorageVolumeSource](api-reference.md#storagevolumesource)
* [Volume](api-reference.md#volume)
* [VolumeSource](api-reference.md#volumesource)

| Field                                                                              | Description | Default | Validation |
| ---------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                                              | Description | Default | Validation |
| driver string                                                                      |             |         |            |
| readOnly boolean                                                                   |             |         |            |
| fsType string                                                                      |             |         |            |
| volumeAttributes object (keys:string, values:string)                               |             |         |            |
| nodePublishSecretRef [LocalObjectReference](api-reference.md#localobjectreference) |             |         |            |

#### CleanupPolicy

_Underlying type:_ _string_

CleanupPolicy defines the behavior for cleaning up a resource.

_Appears in:_

* [DatabaseSpec](api-reference.md#databasespec)
* [GrantSpec](api-reference.md#grantspec)
* [SQLTemplate](api-reference.md#sqltemplate)
* [UserSpec](api-reference.md#userspec)

| Field  | Description                                                                                                  |
| ------ | ------------------------------------------------------------------------------------------------------------ |
| Field  | Description                                                                                                  |
| Skip   | CleanupPolicySkip indicates that the resource will NOT be deleted from the database after the CR is deleted. |
| Delete | CleanupPolicyDelete indicates that the resource will be deleted from the database after the CR is deleted.   |

#### CompressAlgorithm

_Underlying type:_ _string_

CompressAlgorithm defines the compression algorithm for a Backup resource.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)

| Field | Description                                                                                             |
| ----- | ------------------------------------------------------------------------------------------------------- |
| Field | Description                                                                                             |
| none  | No compression                                                                                          |
| bzip2 | Bzip2 compression. Good compression ratio, but slower compression/decompression speed compared to gzip. |
| gzip  | Gzip compression. Good compression/decompression speed, but worse compression ratio compared to bzip2.  |

#### ConfigMapKeySelector

Refer to the Kubernetes docs: [#configmapkeyselector-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#configmapkeyselector-v1-core).

_Appears in:_

* [EnvVarSource](api-reference.md#envvarsource)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [SqlJobSpec](api-reference.md#sqljobspec)

| Field       | Description | Default | Validation |
| ----------- | ----------- | ------- | ---------- |
| Field       | Description | Default | Validation |
| name string |             |         |            |
| key string  |             |         |            |

#### ConfigMapVolumeSource

Refer to the Kubernetes docs: [#configmapvolumesource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#configmapvolumesource-v1-core).

_Appears in:_

* [Volume](api-reference.md#volume)
* [VolumeSource](api-reference.md#volumesource)

| Field               | Description | Default | Validation |
| ------------------- | ----------- | ------- | ---------- |
| Field               | Description | Default | Validation |
| name string         |             |         |            |
| defaultMode integer |             |         |            |

#### Connection

Connection is the Schema for the connections API. It is used to configure connection strings for the applications connecting to MariaDB.

| Field                                                                                                          | Description                                                   | Default | Validation |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                          | Description                                                   | Default | Validation |
| apiVersion string                                                                                              | enterprise.mariadb.com/v1alpha1                               |         |            |
| kind string                                                                                                    | Connection                                                    |         |            |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |         |            |
| spec [ConnectionSpec](api-reference.md#connectionspec)                                                         |                                                               |         |            |

#### ConnectionSpec

ConnectionSpec defines the desired state of Connection

_Appears in:_

* [Connection](api-reference.md#connection)

| Field                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Default | Validation   |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ------------ |
| Field                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Default | Validation   |
| secretName string                                                                    | SecretName to be used in the Connection.                                                                                                                                                                                                                                                                                                                                                                                                                                             |         |              |
| secretTemplate [SecretTemplate](api-reference.md#secrettemplate)                     | SecretTemplate to be used in the Connection.                                                                                                                                                                                                                                                                                                                                                                                                                                         |         |              |
| healthCheck [HealthCheck](api-reference.md#healthcheck)                              | HealthCheck to be used in the Connection.                                                                                                                                                                                                                                                                                                                                                                                                                                            |         |              |
| params object (keys:string, values:string)                                           | Params to be used in the Connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |         |              |
| serviceName string                                                                   | ServiceName to be used in the Connection.                                                                                                                                                                                                                                                                                                                                                                                                                                            |         |              |
| port integer                                                                         | Port to connect to. If not provided, it defaults to the MariaDB port or to the first MaxScale listener.                                                                                                                                                                                                                                                                                                                                                                              |         |              |
| mariaDbRef [MariaDBRef](api-reference.md#mariadbref)                                 | MariaDBRef is a reference to the MariaDB to connect to. Either MariaDBRef or MaxScaleRef must be provided.                                                                                                                                                                                                                                                                                                                                                                           |         |              |
| maxScaleRef [ObjectReference](api-reference.md#objectreference)                      | MaxScaleRef is a reference to the MaxScale to connect to. Either MariaDBRef or MaxScaleRef must be provided.                                                                                                                                                                                                                                                                                                                                                                         |         |              |
| username string                                                                      | Username to use for configuring the Connection.                                                                                                                                                                                                                                                                                                                                                                                                                                      |         | Required: {} |
| passwordSecretKeyRef [SecretKeySelector](api-reference.md#secretkeyselector)         | PasswordSecretKeyRef is a reference to the password to use for configuring the Connection.Either passwordSecretKeyRef or tlsClientCertSecretRef must be provided as client credentials.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password.                                                                                                                                                |         |              |
| tlsClientCertSecretRef [LocalObjectReference](api-reference.md#localobjectreference) | TLSClientCertSecretRef is a reference to a Kubernetes TLS Secret used as authentication when checking the connection health.Either passwordSecretKeyRef or tlsClientCertSecretRef must be provided as client credentials.If not provided, the client certificate provided by the referred MariaDB is used if TLS is enabled.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the client certificate. |         |              |
| host string                                                                          | Host to connect to. If not provided, it defaults to the MariaDB host or to the MaxScale host.                                                                                                                                                                                                                                                                                                                                                                                        |         |              |
| database string                                                                      | Database to use when configuring the Connection.                                                                                                                                                                                                                                                                                                                                                                                                                                     |         |              |

#### ConnectionTemplate

ConnectionTemplate defines a template to customize Connection objects.

_Appears in:_

* [ConnectionSpec](api-reference.md#connectionspec)
* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                            | Description                                                                                             | Default | Validation |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                            | Description                                                                                             | Default | Validation |
| secretName string                                                | SecretName to be used in the Connection.                                                                |         |            |
| secretTemplate [SecretTemplate](api-reference.md#secrettemplate) | SecretTemplate to be used in the Connection.                                                            |         |            |
| healthCheck [HealthCheck](api-reference.md#healthcheck)          | HealthCheck to be used in the Connection.                                                               |         |            |
| params object (keys:string, values:string)                       | Params to be used in the Connection.                                                                    |         |            |
| serviceName string                                               | ServiceName to be used in the Connection.                                                               |         |            |
| port integer                                                     | Port to connect to. If not provided, it defaults to the MariaDB port or to the first MaxScale listener. |         |            |

#### Container

Container object definition.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)
* [PodTemplate](api-reference.md#podtemplate)

| Field                                                                                                                 | Description                                                                                                                  | Default | Validation                         |
| --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------- |
| Field                                                                                                                 | Description                                                                                                                  | Default | Validation                         |
| name string                                                                                                           | Name to be given to the container.                                                                                           |         |                                    |
| image string                                                                                                          | Image name to be used by the container. The supported format is :.                                                           |         | Required: {}                       |
| imagePullPolicy [PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#pullpolicy-v1-core) | ImagePullPolicy is the image pull policy. One of Always, Never or IfNotPresent. If not defined, it defaults to IfNotPresent. |         | Enum: \[Always Never IfNotPresent] |
| command string array                                                                                                  | Command to be used in the Container.                                                                                         |         |                                    |
| args string array                                                                                                     | Args to be used in the Container.                                                                                            |         |                                    |
| env [EnvVar](api-reference.md#envvar) array                                                                           | Env represents the environment variables to be injected in a container.                                                      |         |                                    |
| volumeMounts [VolumeMount](api-reference.md#volumemount) array                                                        | VolumeMounts to be used in the Container.                                                                                    |         |                                    |
| resources [ResourceRequirements](api-reference.md#resourcerequirements)                                               | Resouces describes the compute resource requirements.                                                                        |         |                                    |

#### ContainerTemplate

ContainerTemplate defines a template to configure Container objects.

_Appears in:_

* [GaleraAgent](api-reference.md#galeraagent)
* [GaleraInit](api-reference.md#galerainit)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                   | Description                                                                                                             | Default | Validation |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                   | Description                                                                                                             | Default | Validation |
| command string array                                                    | Command to be used in the Container.                                                                                    |         |            |
| args string array                                                       | Args to be used in the Container.                                                                                       |         |            |
| env [EnvVar](api-reference.md#envvar) array                             | Env represents the environment variables to be injected in a container.                                                 |         |            |
| envFrom [EnvFromSource](api-reference.md#envfromsource) array           | EnvFrom represents the references (via ConfigMap and Secrets) to environment variables to be injected in the container. |         |            |
| volumeMounts [VolumeMount](api-reference.md#volumemount) array          | VolumeMounts to be used in the Container.                                                                               |         |            |
| livenessProbe [Probe](api-reference.md#probe)                           | LivenessProbe to be used in the Container.                                                                              |         |            |
| readinessProbe [Probe](api-reference.md#probe)                          | ReadinessProbe to be used in the Container.                                                                             |         |            |
| startupProbe [Probe](api-reference.md#probe)                            | StartupProbe to be used in the Container.                                                                               |         |            |
| resources [ResourceRequirements](api-reference.md#resourcerequirements) | Resouces describes the compute resource requirements.                                                                   |         |            |
| securityContext [SecurityContext](api-reference.md#securitycontext)     | SecurityContext holds security configuration that will be applied to a container.                                       |         |            |

#### CooperativeMonitoring

_Underlying type:_ _string_

CooperativeMonitoring enables coordination between multiple MaxScale instances running monitors.\
See:

_Appears in:_

* [MaxScaleMonitor](api-reference.md#maxscalemonitor)

| Field                 | Description                                                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Field                 | Description                                                                                                               |
| majority\_of\_all     | CooperativeMonitoringMajorityOfAll requires a lock from the majority of the MariaDB servers, even the ones that are down. |
| majority\_of\_running | CooperativeMonitoringMajorityOfRunning requires a lock from the majority of the MariaDB servers.                          |

#### CronJobTemplate

CronJobTemplate defines parameters for configuring CronJob objects.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [SqlJobSpec](api-reference.md#sqljobspec)

| Field                              | Description                                                                               | Default | Validation |
| ---------------------------------- | ----------------------------------------------------------------------------------------- | ------- | ---------- |
| Field                              | Description                                                                               | Default | Validation |
| successfulJobsHistoryLimit integer | SuccessfulJobsHistoryLimit defines the maximum number of successful Jobs to be displayed. |         | Minimum: 0 |
| failedJobsHistoryLimit integer     | FailedJobsHistoryLimit defines the maximum number of failed Jobs to be displayed.         |         | Minimum: 0 |
| timeZone string                    | TimeZone defines the timezone associated with the cron expression.                        |         |            |

#### Database

Database is the Schema for the databases API. It is used to define a logical database as if you were running a 'CREATE DATABASE' statement.

| Field                                                                                                          | Description                                                   | Default | Validation |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                          | Description                                                   | Default | Validation |
| apiVersion string                                                                                              | enterprise.mariadb.com/v1alpha1                               |         |            |
| kind string                                                                                                    | Database                                                      |         |            |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |         |            |
| spec [DatabaseSpec](api-reference.md#databasespec)                                                             |                                                               |         |            |

#### DatabaseSpec

DatabaseSpec defines the desired state of Database

_Appears in:_

* [Database](api-reference.md#database)

| Field                                                                                                             | Description                                                         | Default           | Validation           |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------- | -------------------- |
| Field                                                                                                             | Description                                                         | Default           | Validation           |
| requeueInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | RequeueInterval is used to perform requeue reconciliations.         |                   |                      |
| retryInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)   | RetryInterval is the interval used to perform retries.              |                   |                      |
| cleanupPolicy [CleanupPolicy](api-reference.md#cleanuppolicy)                                                     | CleanupPolicy defines the behavior for cleaning up a SQL resource.  |                   | Enum: \[Skip Delete] |
| mariaDbRef [MariaDBRef](api-reference.md#mariadbref)                                                              | MariaDBRef is a reference to a MariaDB object.                      |                   | Required: {}         |
| characterSet string                                                                                               | CharacterSet to use in the Database.                                | utf8              |                      |
| collate string                                                                                                    | Collate to use in the Database.                                     | utf8\_general\_ci |                      |
| name string                                                                                                       | Name overrides the default Database name provided by metadata.name. |                   | MaxLength: 80        |

#### EmptyDirVolumeSource

Refer to the Kubernetes docs: [#emptydirvolumesource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#emptydirvolumesource-v1-core).

_Appears in:_

* [StorageVolumeSource](api-reference.md#storagevolumesource)
* [Volume](api-reference.md#volume)
* [VolumeSource](api-reference.md#volumesource)

| Field                                                                                                              | Description | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------ | ----------- | ------- | ---------- |
| Field                                                                                                              | Description | Default | Validation |
| medium [StorageMedium](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#storagemedium-v1-core) |             |         |            |
| sizeLimit [Quantity](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#quantity-resource-api)   |             |         |            |

#### EnvFromSource

Refer to the Kubernetes docs: [#envfromsource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#envfromsource-v1-core).

_Appears in:_

* [ContainerTemplate](api-reference.md#containertemplate)
* [GaleraAgent](api-reference.md#galeraagent)
* [GaleraInit](api-reference.md#galerainit)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                      | Description | Default | Validation |
| -------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                                      | Description | Default | Validation |
| prefix string                                                              |             |         |            |
| configMapRef [LocalObjectReference](api-reference.md#localobjectreference) |             |         |            |
| secretRef [LocalObjectReference](api-reference.md#localobjectreference)    |             |         |            |

#### EnvVar

Refer to the Kubernetes docs: [#envvarsource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#envvarsource-v1-core).

_Appears in:_

* [Container](api-reference.md#container)
* [ContainerTemplate](api-reference.md#containertemplate)
* [GaleraAgent](api-reference.md#galeraagent)
* [GaleraInit](api-reference.md#galerainit)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                   | Description                                                | Default | Validation |
| ------------------------------------------------------- | ---------------------------------------------------------- | ------- | ---------- |
| Field                                                   | Description                                                | Default | Validation |
| name string                                             | Name of the environment variable. Must be a C\_IDENTIFIER. |         |            |
| value string                                            |                                                            |         |            |
| valueFrom [EnvVarSource](api-reference.md#envvarsource) |                                                            |         |            |

#### EnvVarSource

Refer to the Kubernetes docs: [#envvarsource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#envvarsource-v1-core).

_Appears in:_

* [EnvVar](api-reference.md#envvar)

| Field                                                                         | Description | Default | Validation |
| ----------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                                         | Description | Default | Validation |
| fieldRef [ObjectFieldSelector](api-reference.md#objectfieldselector)          |             |         |            |
| configMapKeyRef [ConfigMapKeySelector](api-reference.md#configmapkeyselector) |             |         |            |
| secretKeyRef [SecretKeySelector](api-reference.md#secretkeyselector)          |             |         |            |

#### ExecAction

Refer to the Kubernetes docs: [#execaction-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#execaction-v1-core).

_Appears in:_

* [Probe](api-reference.md#probe)
* [ProbeHandler](api-reference.md#probehandler)

| Field                | Description | Default | Validation |
| -------------------- | ----------- | ------- | ---------- |
| Field                | Description | Default | Validation |
| command string array |             |         |            |

#### Exporter

Exporter defines a metrics exporter container.

_Appears in:_

* [MariadbMetrics](api-reference.md#mariadbmetrics)
* [MaxScaleMetrics](api-reference.md#maxscalemetrics)

| Field                                                                                                                   | Description                                                                                                                  | Default | Validation                         |
| ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------- |
| Field                                                                                                                   | Description                                                                                                                  | Default | Validation                         |
| image string                                                                                                            | Image name to be used as metrics exporter. The supported format is :.                                                        |         |                                    |
| imagePullPolicy [PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#pullpolicy-v1-core)   | ImagePullPolicy is the image pull policy. One of Always, Never or IfNotPresent. If not defined, it defaults to IfNotPresent. |         | Enum: \[Always Never IfNotPresent] |
| imagePullSecrets [LocalObjectReference](api-reference.md#localobjectreference) array                                    | ImagePullSecrets is the list of pull Secrets to be used to pull the image.                                                   |         |                                    |
| args string array                                                                                                       | Args to be used in the Container.                                                                                            |         |                                    |
| port integer                                                                                                            | Port where the exporter will be listening for connections.                                                                   |         |                                    |
| resources [ResourceRequirements](api-reference.md#resourcerequirements)                                                 | Resouces describes the compute resource requirements.                                                                        |         |                                    |
| podMetadata [Metadata](api-reference.md#metadata)                                                                       | PodMetadata defines extra metadata for the Pod.                                                                              |         |                                    |
| securityContext [SecurityContext](api-reference.md#securitycontext)                                                     | SecurityContext holds container-level security attributes.                                                                   |         |                                    |
| podSecurityContext [PodSecurityContext](api-reference.md#podsecuritycontext)                                            | SecurityContext holds pod-level security attributes and common container settings.                                           |         |                                    |
| affinity [AffinityConfig](api-reference.md#affinityconfig)                                                              | Affinity to be used in the Pod.                                                                                              |         |                                    |
| nodeSelector object (keys:string, values:string)                                                                        | NodeSelector to be used in the Pod.                                                                                          |         |                                    |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array | Tolerations to be used in the Pod.                                                                                           |         |                                    |
| priorityClassName string                                                                                                | PriorityClassName to be used in the Pod.                                                                                     |         |                                    |

#### Galera

Galera allows you to enable multi-master HA via Galera in your MariaDB cluster.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                      | Description                                                                                                                                                                                                                                                                                   | Default | Validation                           |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------ |
| Field                                                      | Description                                                                                                                                                                                                                                                                                   | Default | Validation                           |
| primary [PrimaryGalera](api-reference.md#primarygalera)    | Primary is the Galera configuration for the primary node.                                                                                                                                                                                                                                     |         |                                      |
| sst [SST](api-reference.md#sst)                            | SST is the Snapshot State Transfer used when new Pods join the cluster.More info: [sst.html](https://galeracluster.com/library/documentation/sst.html).                                                                                                                                       |         | Enum: \[rsync mariabackup mysqldump] |
| availableWhenDonor boolean                                 | AvailableWhenDonor indicates whether a donor node should be responding to queries. It defaults to false.                                                                                                                                                                                      |         |                                      |
| galeraLibPath string                                       | GaleraLibPath is a path inside the MariaDB image to the wsrep provider plugin. It is defaulted if not provided.More info: [mysql-wsrep-options.html#wsrep-provider](https://galeracluster.com/library/documentation/mysql-wsrep-options.html#wsrep-provider).                                 |         |                                      |
| replicaThreads integer                                     | ReplicaThreads is the number of replica threads used to apply Galera write sets in parallel.More info: [galera-cluster-system-variables.md#wsrep\_slave\_threads](../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_slave_threads). |         |                                      |
| providerOptions object (keys:string, values:string)        | ProviderOptions is map of Galera configuration parameters.More info: [galera-cluster-system-variables.md#wsrep\_provider\_options](../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_provider_options).                             |         |                                      |
| agent [GaleraAgent](api-reference.md#galeraagent)          | GaleraAgent is a sidecar agent that co-operates with mariadb-enterprise-operator.                                                                                                                                                                                                             |         |                                      |
| recovery [GaleraRecovery](api-reference.md#galerarecovery) | GaleraRecovery is the recovery process performed by the operator whenever the Galera cluster is not healthy.More info: [crash-recovery.html](https://galeracluster.com/library/documentation/crash-recovery.html).                                                                            |         |                                      |
| initContainer [GaleraInit](api-reference.md#galerainit)    | InitContainer is an init container that runs in the MariaDB Pod and co-operates with mariadb-enterprise-operator.                                                                                                                                                                             |         |                                      |
| initJob [GaleraInitJob](api-reference.md#galerainitjob)    | InitJob defines a Job that co-operates with mariadb-enterprise-operator by performing initialization tasks.                                                                                                                                                                                   |         |                                      |
| config [GaleraConfig](api-reference.md#galeraconfig)       | GaleraConfig defines storage options for the Galera configuration files.                                                                                                                                                                                                                      |         |                                      |
| clusterName string                                         | ClusterName is the name of the cluster to be used in the Galera config file.                                                                                                                                                                                                                  |         |                                      |
| enabled boolean                                            | Enabled is a flag to enable Galera.                                                                                                                                                                                                                                                           |         |                                      |

#### GaleraAgent

GaleraAgent is a sidecar agent that co-operates with mariadb-enterprise-operator.

_Appears in:_

* [Galera](api-reference.md#galera)
* [GaleraSpec](api-reference.md#galeraspec)

| Field                                                                                                                     | Description                                                                                                                  | Default | Validation                         |
| ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------- |
| Field                                                                                                                     | Description                                                                                                                  | Default | Validation                         |
| command string array                                                                                                      | Command to be used in the Container.                                                                                         |         |                                    |
| args string array                                                                                                         | Args to be used in the Container.                                                                                            |         |                                    |
| env [EnvVar](api-reference.md#envvar) array                                                                               | Env represents the environment variables to be injected in a container.                                                      |         |                                    |
| envFrom [EnvFromSource](api-reference.md#envfromsource) array                                                             | EnvFrom represents the references (via ConfigMap and Secrets) to environment variables to be injected in the container.      |         |                                    |
| volumeMounts [VolumeMount](api-reference.md#volumemount) array                                                            | VolumeMounts to be used in the Container.                                                                                    |         |                                    |
| livenessProbe [Probe](api-reference.md#probe)                                                                             | LivenessProbe to be used in the Container.                                                                                   |         |                                    |
| readinessProbe [Probe](api-reference.md#probe)                                                                            | ReadinessProbe to be used in the Container.                                                                                  |         |                                    |
| startupProbe [Probe](api-reference.md#probe)                                                                              | StartupProbe to be used in the Container.                                                                                    |         |                                    |
| resources [ResourceRequirements](api-reference.md#resourcerequirements)                                                   | Resouces describes the compute resource requirements.                                                                        |         |                                    |
| securityContext [SecurityContext](api-reference.md#securitycontext)                                                       | SecurityContext holds security configuration that will be applied to a container.                                            |         |                                    |
| image string                                                                                                              | Image name to be used by the MariaDB instances. The supported format is :.                                                   |         |                                    |
| imagePullPolicy [PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#pullpolicy-v1-core)     | ImagePullPolicy is the image pull policy. One of Always, Never or IfNotPresent. If not defined, it defaults to IfNotPresent. |         | Enum: \[Always Never IfNotPresent] |
| port integer                                                                                                              | Port where the agent will be listening for API connections.                                                                  |         |                                    |
| probePort integer                                                                                                         | Port where the agent will be listening for probe connections.                                                                |         |                                    |
| kubernetesAuth [KubernetesAuth](api-reference.md#kubernetesauth)                                                          | KubernetesAuth to be used by the agent container                                                                             |         |                                    |
| basicAuth [BasicAuth](api-reference.md#basicauth)                                                                         | BasicAuth to be used by the agent container                                                                                  |         |                                    |
| gracefulShutdownTimeout [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | GracefulShutdownTimeout is the time we give to the agent container in order to gracefully terminate in-flight requests.      |         |                                    |

#### GaleraConfig

GaleraConfig defines storage options for the Galera configuration files.

_Appears in:_

* [Galera](api-reference.md#galera)
* [GaleraSpec](api-reference.md#galeraspec)

| Field                                                                           | Description                                                                                                                                                                                                                              | Default | Validation |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                           | Description                                                                                                                                                                                                                              | Default | Validation |
| reuseStorageVolume boolean                                                      | ReuseStorageVolume indicates that storage volume used by MariaDB should be reused to store the Galera configuration files.It defaults to false, which implies that a dedicated volume for the Galera configuration files is provisioned. |         |            |
| volumeClaimTemplate [VolumeClaimTemplate](api-reference.md#volumeclaimtemplate) | VolumeClaimTemplate is a template for the PVC that will contain the Galera configuration files shared between the InitContainer, Agent and MariaDB.                                                                                      |         |            |

#### GaleraInit

GaleraInit is an init container that runs in the MariaDB Pod and co-operates with mariadb-enterprise-operator.

_Appears in:_

* [Galera](api-reference.md#galera)
* [GaleraSpec](api-reference.md#galeraspec)

| Field                                                                                                                 | Description                                                                                                                  | Default | Validation                         |
| --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------- |
| Field                                                                                                                 | Description                                                                                                                  | Default | Validation                         |
| command string array                                                                                                  | Command to be used in the Container.                                                                                         |         |                                    |
| args string array                                                                                                     | Args to be used in the Container.                                                                                            |         |                                    |
| env [EnvVar](api-reference.md#envvar) array                                                                           | Env represents the environment variables to be injected in a container.                                                      |         |                                    |
| envFrom [EnvFromSource](api-reference.md#envfromsource) array                                                         | EnvFrom represents the references (via ConfigMap and Secrets) to environment variables to be injected in the container.      |         |                                    |
| volumeMounts [VolumeMount](api-reference.md#volumemount) array                                                        | VolumeMounts to be used in the Container.                                                                                    |         |                                    |
| livenessProbe [Probe](api-reference.md#probe)                                                                         | LivenessProbe to be used in the Container.                                                                                   |         |                                    |
| readinessProbe [Probe](api-reference.md#probe)                                                                        | ReadinessProbe to be used in the Container.                                                                                  |         |                                    |
| startupProbe [Probe](api-reference.md#probe)                                                                          | StartupProbe to be used in the Container.                                                                                    |         |                                    |
| resources [ResourceRequirements](api-reference.md#resourcerequirements)                                               | Resouces describes the compute resource requirements.                                                                        |         |                                    |
| securityContext [SecurityContext](api-reference.md#securitycontext)                                                   | SecurityContext holds security configuration that will be applied to a container.                                            |         |                                    |
| image string                                                                                                          | Image name to be used by the MariaDB instances. The supported format is :.                                                   |         | Required: {}                       |
| imagePullPolicy [PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#pullpolicy-v1-core) | ImagePullPolicy is the image pull policy. One of Always, Never or IfNotPresent. If not defined, it defaults to IfNotPresent. |         | Enum: \[Always Never IfNotPresent] |

#### GaleraInitJob

GaleraInitJob defines a Job used to be used to initialize the Galera cluster.

_Appears in:_

* [Galera](api-reference.md#galera)
* [GaleraSpec](api-reference.md#galeraspec)

| Field                                                                   | Description                                                   | Default | Validation |
| ----------------------------------------------------------------------- | ------------------------------------------------------------- | ------- | ---------- |
| Field                                                                   | Description                                                   | Default | Validation |
| metadata [Metadata](api-reference.md#metadata)                          | Refer to Kubernetes API documentation for fields of metadata. |         |            |
| resources [ResourceRequirements](api-reference.md#resourcerequirements) | Resouces describes the compute resource requirements.         |         |            |

#### GaleraRecovery

GaleraRecovery is the recovery process performed by the operator whenever the Galera cluster is not healthy.\
More info: [crash-recovery.html](https://galeracluster.com/library/documentation/crash-recovery.html).

_Appears in:_

* [Galera](api-reference.md#galera)
* [GaleraSpec](api-reference.md#galeraspec)

| Field                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Default | Validation |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Default | Validation |
| enabled boolean                                                                                                            | Enabled is a flag to enable GaleraRecovery.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |         |            |
| minClusterSize [IntOrString](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#intorstring-intstr-util) | MinClusterSize is the minimum number of replicas to consider the cluster healthy. It can be either a number of replicas (1) or a percentage (50%).If Galera consistently reports less replicas than this value for the given 'ClusterHealthyTimeout' interval, a cluster recovery is iniated.It defaults to '1' replica, and it is highly recommendeded to keep this value at '1' in most cases.If set to more than one replica, the cluster recovery process may restart the healthy replicas as well. |         |            |
| clusterMonitorInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)   | ClusterMonitorInterval represents the interval used to monitor the Galera cluster health.                                                                                                                                                                                                                                                                                                                                                                                                               |         |            |
| clusterHealthyTimeout [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)    | ClusterHealthyTimeout represents the duration at which a Galera cluster, that consistently failed health checks,is considered unhealthy, and consequently the Galera recovery process will be initiated by the operator.                                                                                                                                                                                                                                                                                |         |            |
| clusterBootstrapTimeout [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)  | ClusterBootstrapTimeout is the time limit for bootstrapping a cluster.Once this timeout is reached, the Galera recovery state is reset and a new cluster bootstrap will be attempted.                                                                                                                                                                                                                                                                                                                   |         |            |
| clusterUpscaleTimeout [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)    | ClusterUpscaleTimeout represents the maximum duration for upscaling the cluster's StatefulSet during the recovery process.                                                                                                                                                                                                                                                                                                                                                                              |         |            |
| clusterDownscaleTimeout [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)  | ClusterDownscaleTimeout represents the maximum duration for downscaling the cluster's StatefulSet during the recovery process.                                                                                                                                                                                                                                                                                                                                                                          |         |            |
| podRecoveryTimeout [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)       | PodRecoveryTimeout is the time limit for recevorying the sequence of a Pod during the cluster recovery.                                                                                                                                                                                                                                                                                                                                                                                                 |         |            |
| podSyncTimeout [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)           | PodSyncTimeout is the time limit for a Pod to join the cluster after having performed a cluster bootstrap during the cluster recovery.                                                                                                                                                                                                                                                                                                                                                                  |         |            |
| forceClusterBootstrapInPod string                                                                                          | ForceClusterBootstrapInPod allows you to manually initiate the bootstrap process in a specific Pod.IMPORTANT: Use this option only in exceptional circumstances. Not selecting the Pod with the highest sequence number may result in data loss.IMPORTANT: Ensure you unset this field after completing the bootstrap to allow the operator to choose the appropriate Pod to bootstrap from in an event of cluster recovery.                                                                            |         |            |
| job [GaleraRecoveryJob](api-reference.md#galerarecoveryjob)                                                                | Job defines a Job that co-operates with mariadb-enterprise-operator by performing the Galera cluster recovery .                                                                                                                                                                                                                                                                                                                                                                                         |         |            |

#### GaleraRecoveryJob

GaleraRecoveryJob defines a Job used to be used to recover the Galera cluster.

_Appears in:_

* [GaleraRecovery](api-reference.md#galerarecovery)

| Field                                                                   | Description                                                                                                           | Default | Validation |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                   | Description                                                                                                           | Default | Validation |
| metadata [Metadata](api-reference.md#metadata)                          | Refer to Kubernetes API documentation for fields of metadata.                                                         |         |            |
| resources [ResourceRequirements](api-reference.md#resourcerequirements) | Resouces describes the compute resource requirements.                                                                 |         |            |
| podAffinity boolean                                                     | PodAffinity indicates whether the recovery Jobs should run in the same Node as the MariaDB Pods. It defaults to true. |         |            |

#### GaleraSpec

GaleraSpec is the Galera desired state specification.

_Appears in:_

* [Galera](api-reference.md#galera)

| Field                                                      | Description                                                                                                                                                                                                                                                                                   | Default | Validation                           |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------ |
| Field                                                      | Description                                                                                                                                                                                                                                                                                   | Default | Validation                           |
| primary [PrimaryGalera](api-reference.md#primarygalera)    | Primary is the Galera configuration for the primary node.                                                                                                                                                                                                                                     |         |                                      |
| sst [SST](api-reference.md#sst)                            | SST is the Snapshot State Transfer used when new Pods join the cluster.More info: [sst.html](https://galeracluster.com/library/documentation/sst.html).                                                                                                                                       |         | Enum: \[rsync mariabackup mysqldump] |
| availableWhenDonor boolean                                 | AvailableWhenDonor indicates whether a donor node should be responding to queries. It defaults to false.                                                                                                                                                                                      |         |                                      |
| galeraLibPath string                                       | GaleraLibPath is a path inside the MariaDB image to the wsrep provider plugin. It is defaulted if not provided.More info: [mysql-wsrep-options.html#wsrep-provider](https://galeracluster.com/library/documentation/mysql-wsrep-options.html#wsrep-provider).                                 |         |                                      |
| replicaThreads integer                                     | ReplicaThreads is the number of replica threads used to apply Galera write sets in parallel.More info: [galera-cluster-system-variables.md#wsrep\_slave\_threads](../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_slave_threads). |         |                                      |
| providerOptions object (keys:string, values:string)        | ProviderOptions is map of Galera configuration parameters.More info: [galera-cluster-system-variables.md#wsrep\_provider\_options](../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_provider_options).                             |         |                                      |
| agent [GaleraAgent](api-reference.md#galeraagent)          | GaleraAgent is a sidecar agent that co-operates with mariadb-enterprise-operator.                                                                                                                                                                                                             |         |                                      |
| recovery [GaleraRecovery](api-reference.md#galerarecovery) | GaleraRecovery is the recovery process performed by the operator whenever the Galera cluster is not healthy.More info: [crash-recovery.html](https://galeracluster.com/library/documentation/crash-recovery.html).                                                                            |         |                                      |
| initContainer [GaleraInit](api-reference.md#galerainit)    | InitContainer is an init container that runs in the MariaDB Pod and co-operates with mariadb-enterprise-operator.                                                                                                                                                                             |         |                                      |
| initJob [GaleraInitJob](api-reference.md#galerainitjob)    | InitJob defines a Job that co-operates with mariadb-enterprise-operator by performing initialization tasks.                                                                                                                                                                                   |         |                                      |
| config [GaleraConfig](api-reference.md#galeraconfig)       | GaleraConfig defines storage options for the Galera configuration files.                                                                                                                                                                                                                      |         |                                      |
| clusterName string                                         | ClusterName is the name of the cluster to be used in the Galera config file.                                                                                                                                                                                                                  |         |                                      |

#### GeneratedSecretKeyRef

GeneratedSecretKeyRef defines a reference to a Secret that can be automatically generated by mariadb-enterprise-operator if needed.

_Appears in:_

* [BasicAuth](api-reference.md#basicauth)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MariadbMetrics](api-reference.md#mariadbmetrics)
* [MaxScaleAuth](api-reference.md#maxscaleauth)

| Field            | Description                                                                                        | Default | Validation |
| ---------------- | -------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field            | Description                                                                                        | Default | Validation |
| name string      |                                                                                                    |         |            |
| key string       |                                                                                                    |         |            |
| generate boolean | Generate indicates whether the Secret should be generated if the Secret referenced is not present. | false   |            |

#### Grant

Grant is the Schema for the grants API. It is used to define grants as if you were running a 'GRANT' statement.

| Field                                                                                                          | Description                                                   | Default | Validation |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                          | Description                                                   | Default | Validation |
| apiVersion string                                                                                              | enterprise.mariadb.com/v1alpha1                               |         |            |
| kind string                                                                                                    | Grant                                                         |         |            |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |         |            |
| spec [GrantSpec](api-reference.md#grantspec)                                                                   |                                                               |         |            |

#### GrantSpec

GrantSpec defines the desired state of Grant

_Appears in:_

* [Grant](api-reference.md#grant)

| Field                                                                                                             | Description                                                        | Default | Validation               |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------- | ------------------------ |
| Field                                                                                                             | Description                                                        | Default | Validation               |
| requeueInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | RequeueInterval is used to perform requeue reconciliations.        |         |                          |
| retryInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)   | RetryInterval is the interval used to perform retries.             |         |                          |
| cleanupPolicy [CleanupPolicy](api-reference.md#cleanuppolicy)                                                     | CleanupPolicy defines the behavior for cleaning up a SQL resource. |         | Enum: \[Skip Delete]     |
| mariaDbRef [MariaDBRef](api-reference.md#mariadbref)                                                              | MariaDBRef is a reference to a MariaDB object.                     |         | Required: {}             |
| privileges string array                                                                                           | Privileges to use in the Grant.                                    |         | MinItems: 1 Required: {} |
| database string                                                                                                   | Database to use in the Grant.                                      | \*      |                          |
| table string                                                                                                      | Table to use in the Grant.                                         | \*      |                          |
| username string                                                                                                   | Username to use in the Grant.                                      |         | Required: {}             |
| host string                                                                                                       | Host to use in the Grant. It can be localhost, an IP or '%'.       |         |                          |
| grantOption boolean                                                                                               | GrantOption to use in the Grant.                                   | false   |                          |

#### HTTPGetAction

Refer to the Kubernetes docs: [#httpgetaction-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#httpgetaction-v1-core).

_Appears in:_

* [Probe](api-reference.md#probe)
* [ProbeHandler](api-reference.md#probehandler)

| Field                                                                                                            | Description | Default | Validation |
| ---------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                                                                            | Description | Default | Validation |
| path string                                                                                                      |             |         |            |
| port [IntOrString](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#intorstring-intstr-util) |             |         |            |
| host string                                                                                                      |             |         |            |
| scheme [URIScheme](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#urischeme-v1-core)       |             |         |            |

#### HealthCheck

HealthCheck defines intervals for performing health checks.

_Appears in:_

* [ConnectionSpec](api-reference.md#connectionspec)
* [ConnectionTemplate](api-reference.md#connectiontemplate)

| Field                                                                                                           | Description                                                         | Default | Validation |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                           | Description                                                         | Default | Validation |
| interval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)      | Interval used to perform health checks.                             |         |            |
| retryInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | RetryInterval is the interval used to perform health check retries. |         |            |

#### HostPathVolumeSource

Refer to the Kubernetes docs: [#hostpathvolumesource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#hostpathvolumesource-v1-core)

_Appears in:_

* [StorageVolumeSource](api-reference.md#storagevolumesource)
* [Volume](api-reference.md#volume)
* [VolumeSource](api-reference.md#volumesource)

| Field       | Description | Default | Validation |
| ----------- | ----------- | ------- | ---------- |
| Field       | Description | Default | Validation |
| path string |             |         |            |
| type string |             |         |            |

#### Job

Job defines a Job used to be used with MariaDB.

_Appears in:_

* [BootstrapFrom](api-reference.md#bootstrapfrom)

| Field                                                                   | Description                                                   | Default | Validation |
| ----------------------------------------------------------------------- | ------------------------------------------------------------- | ------- | ---------- |
| Field                                                                   | Description                                                   | Default | Validation |
| metadata [Metadata](api-reference.md#metadata)                          | Refer to Kubernetes API documentation for fields of metadata. |         |            |
| affinity [AffinityConfig](api-reference.md#affinityconfig)              | Affinity to be used in the Pod.                               |         |            |
| resources [ResourceRequirements](api-reference.md#resourcerequirements) | Resouces describes the compute resource requirements.         |         |            |
| args string array                                                       | Args to be used in the Container.                             |         |            |

#### JobContainerTemplate

JobContainerTemplate defines a template to configure Container objects that run in a Job.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [RestoreSpec](api-reference.md#restorespec)
* [SqlJobSpec](api-reference.md#sqljobspec)

| Field                                                                   | Description                                                                       | Default | Validation |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                   | Description                                                                       | Default | Validation |
| args string array                                                       | Args to be used in the Container.                                                 |         |            |
| resources [ResourceRequirements](api-reference.md#resourcerequirements) | Resouces describes the compute resource requirements.                             |         |            |
| securityContext [SecurityContext](api-reference.md#securitycontext)     | SecurityContext holds security configuration that will be applied to a container. |         |            |

#### JobPodTemplate

JobPodTemplate defines a template to configure Container objects that run in a Job.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [RestoreSpec](api-reference.md#restorespec)
* [SqlJobSpec](api-reference.md#sqljobspec)

| Field                                                                                                                   | Description                                                                        | Default | Validation |
| ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                                   | Description                                                                        | Default | Validation |
| podMetadata [Metadata](api-reference.md#metadata)                                                                       | PodMetadata defines extra metadata for the Pod.                                    |         |            |
| imagePullSecrets [LocalObjectReference](api-reference.md#localobjectreference) array                                    | ImagePullSecrets is the list of pull Secrets to be used to pull the image.         |         |            |
| podSecurityContext [PodSecurityContext](api-reference.md#podsecuritycontext)                                            | SecurityContext holds pod-level security attributes and common container settings. |         |            |
| serviceAccountName string                                                                                               | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.       |         |            |
| affinity [AffinityConfig](api-reference.md#affinityconfig)                                                              | Affinity to be used in the Pod.                                                    |         |            |
| nodeSelector object (keys:string, values:string)                                                                        | NodeSelector to be used in the Pod.                                                |         |            |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array | Tolerations to be used in the Pod.                                                 |         |            |
| priorityClassName string                                                                                                | PriorityClassName to be used in the Pod.                                           |         |            |

#### KubernetesAuth

KubernetesAuth refers to the Kubernetes authentication mechanism utilized for establishing a connection from the operator to the agent.\
The agent validates the legitimacy of the service account token provided as an Authorization header by creating a TokenReview resource.

_Appears in:_

* [GaleraAgent](api-reference.md#galeraagent)

| Field                        | Description                                                                                                                                                                                                                                | Default | Validation |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ---------- |
| Field                        | Description                                                                                                                                                                                                                                | Default | Validation |
| enabled boolean              | Enabled is a flag to enable KubernetesAuth                                                                                                                                                                                                 |         |            |
| authDelegatorRoleName string | AuthDelegatorRoleName is the name of the ClusterRoleBinding that is associated with the "system:auth-delegator" ClusterRole.It is necessary for creating TokenReview objects in order for the agent to validate the service account token. |         |            |

#### LabelSelector

_Underlying type:_ [_struct{MatchLabels map\[string\]string "json:"matchLabels,omitempty""; MatchExpressions \[\]LabelSelectorRequirement "json:"matchExpressions,omitempty""}_](api-reference.md#struct{matchlabels-map\[string]string-"json:"matchlabels,omitempty"";-matchexpressions-\[]labelselectorrequirement-"json:"matchexpressions,omitempty""})

Refer to the Kubernetes docs: [#labelselector-v1-meta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#labelselector-v1-meta)

_Appears in:_

* [PodAffinityTerm](api-reference.md#podaffinityterm)

#### LocalObjectReference

Refer to the Kubernetes docs: [#localobjectreference-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#localobjectreference-v1-core).

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [BootstrapFrom](api-reference.md#bootstrapfrom)
* [CSIVolumeSource](api-reference.md#csivolumesource)
* [ConfigMapKeySelector](api-reference.md#configmapkeyselector)
* [ConfigMapVolumeSource](api-reference.md#configmapvolumesource)
* [ConnectionSpec](api-reference.md#connectionspec)
* [EnvFromSource](api-reference.md#envfromsource)
* [Exporter](api-reference.md#exporter)
* [GeneratedSecretKeyRef](api-reference.md#generatedsecretkeyref)
* [JobPodTemplate](api-reference.md#jobpodtemplate)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScalePodTemplate](api-reference.md#maxscalepodtemplate)
* [MaxScaleSpec](api-reference.md#maxscalespec)
* [MaxScaleTLS](api-reference.md#maxscaletls)
* [PodTemplate](api-reference.md#podtemplate)
* [RestoreSource](api-reference.md#restoresource)
* [RestoreSpec](api-reference.md#restorespec)
* [SecretKeySelector](api-reference.md#secretkeyselector)
* [SqlJobSpec](api-reference.md#sqljobspec)
* [TLS](api-reference.md#tls)

| Field       | Description | Default | Validation |
| ----------- | ----------- | ------- | ---------- |
| Field       | Description | Default | Validation |
| name string |             |         |            |

#### MariaDB

MariaDB is the Schema for the mariadbs API. It is used to define MariaDB clusters.

| Field                                                                                                          | Description                                                   | Default | Validation |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                          | Description                                                   | Default | Validation |
| apiVersion string                                                                                              | enterprise.mariadb.com/v1alpha1                               |         |            |
| kind string                                                                                                    | MariaDB                                                       |         |            |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |         |            |
| spec [MariaDBSpec](api-reference.md#mariadbspec)                                                               |                                                               |         |            |

#### MariaDBMaxScaleSpec

MariaDBMaxScaleSpec defines a reduced version of MaxScale to be used with the current MariaDB.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                                                                                                              | Description                                                                                                                  | Default | Validation                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------- |
| Field                                                                                                                                              | Description                                                                                                                  | Default | Validation                         |
| enabled boolean                                                                                                                                    | Enabled is a flag to enable a MaxScale instance to be used with the current MariaDB.                                         |         |                                    |
| image string                                                                                                                                       | Image name to be used by the MaxScale instances. The supported format is :.Only MariaDB official images are supported.       |         |                                    |
| imagePullPolicy [PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#pullpolicy-v1-core)                              | ImagePullPolicy is the image pull policy. One of Always, Never or IfNotPresent. If not defined, it defaults to IfNotPresent. |         | Enum: \[Always Never IfNotPresent] |
| services [MaxScaleService](api-reference.md#maxscaleservice) array                                                                                 | Services define how the traffic is forwarded to the MariaDB servers.                                                         |         |                                    |
| monitor [MaxScaleMonitor](api-reference.md#maxscalemonitor)                                                                                        | Monitor monitors MariaDB server instances.                                                                                   |         |                                    |
| admin [MaxScaleAdmin](api-reference.md#maxscaleadmin)                                                                                              | Admin configures the admin REST API and GUI.                                                                                 |         |                                    |
| config [MaxScaleConfig](api-reference.md#maxscaleconfig)                                                                                           | Config defines the MaxScale configuration.                                                                                   |         |                                    |
| auth [MaxScaleAuth](api-reference.md#maxscaleauth)                                                                                                 | Auth defines the credentials required for MaxScale to connect to MariaDB.                                                    |         |                                    |
| metrics [MaxScaleMetrics](api-reference.md#maxscalemetrics)                                                                                        | Metrics configures metrics and how to scrape them.                                                                           |         |                                    |
| tls [MaxScaleTLS](api-reference.md#maxscaletls)                                                                                                    | TLS defines the PKI to be used with MaxScale.                                                                                |         |                                    |
| connection [ConnectionTemplate](api-reference.md#connectiontemplate)                                                                               | Connection provides a template to define the Connection for MaxScale.                                                        |         |                                    |
| replicas integer                                                                                                                                   | Replicas indicates the number of desired instances.                                                                          |         |                                    |
| podDisruptionBudget [PodDisruptionBudget](api-reference.md#poddisruptionbudget)                                                                    | PodDisruptionBudget defines the budget for replica availability.                                                             |         |                                    |
| updateStrategy [StatefulSetUpdateStrategy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#statefulsetupdatestrategy-v1-apps) | UpdateStrategy defines the update strategy for the StatefulSet object.                                                       |         |                                    |
| kubernetesService [ServiceTemplate](api-reference.md#servicetemplate)                                                                              | KubernetesService defines a template for a Kubernetes Service object to connect to MaxScale.                                 |         |                                    |
| guiKubernetesService [ServiceTemplate](api-reference.md#servicetemplate)                                                                           | GuiKubernetesService define a template for a Kubernetes Service object to connect to MaxScale's GUI.                         |         |                                    |
| requeueInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)                                  | RequeueInterval is used to perform requeue reconciliations.                                                                  |         |                                    |

#### MariaDBRef

MariaDBRef is a reference to a MariaDB object.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [ConnectionSpec](api-reference.md#connectionspec)
* [DatabaseSpec](api-reference.md#databasespec)
* [GrantSpec](api-reference.md#grantspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)
* [RestoreSpec](api-reference.md#restorespec)
* [SqlJobSpec](api-reference.md#sqljobspec)
* [UserSpec](api-reference.md#userspec)

| Field             | Description                                                                                          | Default | Validation |
| ----------------- | ---------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field             | Description                                                                                          | Default | Validation |
| name string       |                                                                                                      |         |            |
| namespace string  |                                                                                                      |         |            |
| waitForIt boolean | WaitForIt indicates whether the controller using this reference should wait for MariaDB to be ready. | true    |            |

#### MariaDBSpec

MariaDBSpec defines the desired state of MariaDB

_Appears in:_

* [MariaDB](api-reference.md#mariadb)

| Field                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                          | Default | Validation                         |
| ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------- |
| Field                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                          | Default | Validation                         |
| command string array                                                                                                    | Command to be used in the Container.                                                                                                                                                                                                                                                                                                                 |         |                                    |
| args string array                                                                                                       | Args to be used in the Container.                                                                                                                                                                                                                                                                                                                    |         |                                    |
| env [EnvVar](api-reference.md#envvar) array                                                                             | Env represents the environment variables to be injected in a container.                                                                                                                                                                                                                                                                              |         |                                    |
| envFrom [EnvFromSource](api-reference.md#envfromsource) array                                                           | EnvFrom represents the references (via ConfigMap and Secrets) to environment variables to be injected in the container.                                                                                                                                                                                                                              |         |                                    |
| volumeMounts [VolumeMount](api-reference.md#volumemount) array                                                          | VolumeMounts to be used in the Container.                                                                                                                                                                                                                                                                                                            |         |                                    |
| livenessProbe [Probe](api-reference.md#probe)                                                                           | LivenessProbe to be used in the Container.                                                                                                                                                                                                                                                                                                           |         |                                    |
| readinessProbe [Probe](api-reference.md#probe)                                                                          | ReadinessProbe to be used in the Container.                                                                                                                                                                                                                                                                                                          |         |                                    |
| startupProbe [Probe](api-reference.md#probe)                                                                            | StartupProbe to be used in the Container.                                                                                                                                                                                                                                                                                                            |         |                                    |
| resources [ResourceRequirements](api-reference.md#resourcerequirements)                                                 | Resouces describes the compute resource requirements.                                                                                                                                                                                                                                                                                                |         |                                    |
| securityContext [SecurityContext](api-reference.md#securitycontext)                                                     | SecurityContext holds security configuration that will be applied to a container.                                                                                                                                                                                                                                                                    |         |                                    |
| podMetadata [Metadata](api-reference.md#metadata)                                                                       | PodMetadata defines extra metadata for the Pod.                                                                                                                                                                                                                                                                                                      |         |                                    |
| imagePullSecrets [LocalObjectReference](api-reference.md#localobjectreference) array                                    | ImagePullSecrets is the list of pull Secrets to be used to pull the image.                                                                                                                                                                                                                                                                           |         |                                    |
| initContainers [Container](api-reference.md#container) array                                                            | InitContainers to be used in the Pod.                                                                                                                                                                                                                                                                                                                |         |                                    |
| sidecarContainers [Container](api-reference.md#container) array                                                         | SidecarContainers to be used in the Pod.                                                                                                                                                                                                                                                                                                             |         |                                    |
| podSecurityContext [PodSecurityContext](api-reference.md#podsecuritycontext)                                            | SecurityContext holds pod-level security attributes and common container settings.                                                                                                                                                                                                                                                                   |         |                                    |
| serviceAccountName string                                                                                               | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.                                                                                                                                                                                                                                                                         |         |                                    |
| affinity [AffinityConfig](api-reference.md#affinityconfig)                                                              | Affinity to be used in the Pod.                                                                                                                                                                                                                                                                                                                      |         |                                    |
| nodeSelector object (keys:string, values:string)                                                                        | NodeSelector to be used in the Pod.                                                                                                                                                                                                                                                                                                                  |         |                                    |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array | Tolerations to be used in the Pod.                                                                                                                                                                                                                                                                                                                   |         |                                    |
| volumes [Volume](api-reference.md#volume) array                                                                         | Volumes to be used in the Pod.                                                                                                                                                                                                                                                                                                                       |         |                                    |
| priorityClassName string                                                                                                | PriorityClassName to be used in the Pod.                                                                                                                                                                                                                                                                                                             |         |                                    |
| topologySpreadConstraints [TopologySpreadConstraint](api-reference.md#topologyspreadconstraint) array                   | TopologySpreadConstraints to be used in the Pod.                                                                                                                                                                                                                                                                                                     |         |                                    |
| suspend boolean                                                                                                         | Suspend indicates whether the current resource should be suspended or not.This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities.                                                                                                             | false   |                                    |
| image string                                                                                                            | Image name to be used by the MariaDB instances. The supported format is :.Only MariaDB official images are supported.                                                                                                                                                                                                                                |         |                                    |
| imagePullPolicy [PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#pullpolicy-v1-core)   | ImagePullPolicy is the image pull policy. One of Always, Never or IfNotPresent. If not defined, it defaults to IfNotPresent.                                                                                                                                                                                                                         |         | Enum: \[Always Never IfNotPresent] |
| inheritMetadata [Metadata](api-reference.md#metadata)                                                                   | InheritMetadata defines the metadata to be inherited by children resources.                                                                                                                                                                                                                                                                          |         |                                    |
| rootPasswordSecretKeyRef [GeneratedSecretKeyRef](api-reference.md#generatedsecretkeyref)                                | RootPasswordSecretKeyRef is a reference to a Secret key containing the root password.                                                                                                                                                                                                                                                                |         |                                    |
| rootEmptyPassword boolean                                                                                               | RootEmptyPassword indicates if the root password should be empty. Don't use this feature in production, it is only intended for development and test environments.                                                                                                                                                                                   |         |                                    |
| database string                                                                                                         | Database is the name of the initial Database.                                                                                                                                                                                                                                                                                                        |         |                                    |
| username string                                                                                                         | Username is the initial username to be created by the operator once MariaDB is ready.The initial User will have ALL PRIVILEGES in the initial Database.                                                                                                                                                                                              |         |                                    |
| passwordSecretKeyRef [GeneratedSecretKeyRef](api-reference.md#generatedsecretkeyref)                                    | PasswordSecretKeyRef is a reference to a Secret that contains the password to be used by the initial User.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password.                                                                                             |         |                                    |
| passwordHashSecretKeyRef [SecretKeySelector](api-reference.md#secretkeyselector)                                        | PasswordHashSecretKeyRef is a reference to the password hash to be used by the initial User.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password hash.It requires the 'skip-strict-password-validation' option to be set. See:.                             |         |                                    |
| passwordPlugin [PasswordPlugin](api-reference.md#passwordplugin)                                                        | PasswordPlugin is a reference to the password plugin and arguments to be used by the initial User.It requires the 'skip-strict-password-validation' option to be set. See:.                                                                                                                                                                          |         |                                    |
| myCnf string                                                                                                            | MyCnf allows to specify the my.cnf file mounted by Mariadb.Updating this field will trigger an update to the Mariadb resource.                                                                                                                                                                                                                       |         |                                    |
| myCnfConfigMapKeyRef [ConfigMapKeySelector](api-reference.md#configmapkeyselector)                                      | MyCnfConfigMapKeyRef is a reference to the my.cnf config file provided via a ConfigMap.If not provided, it will be defaulted with a reference to a ConfigMap containing the MyCnf field.If the referred ConfigMap is labeled with "enterprise.mariadb.com/watch", an update to the Mariadb resource will be triggered when the ConfigMap is updated. |         |                                    |
| timeZone string                                                                                                         | TimeZone sets the default timezone. If not provided, it defaults to SYSTEM and the timezone data is not loaded.                                                                                                                                                                                                                                      |         |                                    |
| bootstrapFrom [BootstrapFrom](api-reference.md#bootstrapfrom)                                                           | BootstrapFrom defines a source to bootstrap from.                                                                                                                                                                                                                                                                                                    |         |                                    |
| storage [Storage](api-reference.md#storage)                                                                             | Storage defines the storage options to be used for provisioning the PVCs mounted by MariaDB.                                                                                                                                                                                                                                                         |         |                                    |
| metrics [MariadbMetrics](api-reference.md#mariadbmetrics)                                                               | Metrics configures metrics and how to scrape them.                                                                                                                                                                                                                                                                                                   |         |                                    |
| tls [TLS](api-reference.md#tls)                                                                                         | TLS defines the PKI to be used with MariaDB.                                                                                                                                                                                                                                                                                                         |         |                                    |
| galera [Galera](api-reference.md#galera)                                                                                | Galera configures high availability via Galera.                                                                                                                                                                                                                                                                                                      |         |                                    |
| maxScaleRef [ObjectReference](api-reference.md#objectreference)                                                         | MaxScaleRef is a reference to a MaxScale resource to be used with the current MariaDB.Providing this field implies delegating high availability tasks such as primary failover to MaxScale.                                                                                                                                                          |         |                                    |
| maxScale [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)                                                    | MaxScale is the MaxScale specification that defines the MaxScale resource to be used with the current MariaDB.When enabling this field, MaxScaleRef is automatically set.                                                                                                                                                                            |         |                                    |
| replicas integer                                                                                                        | Replicas indicates the number of desired instances.                                                                                                                                                                                                                                                                                                  | 1       |                                    |
| replicasAllowEvenNumber boolean                                                                                         | disables the validation check for an odd number of replicas.                                                                                                                                                                                                                                                                                         | false   |                                    |
| port integer                                                                                                            | Port where the instances will be listening for connections.                                                                                                                                                                                                                                                                                          | 3306    |                                    |
| servicePorts [ServicePort](api-reference.md#serviceport) array                                                          | ServicePorts is the list of additional named ports to be added to the Services created by the operator.                                                                                                                                                                                                                                              |         |                                    |
| podDisruptionBudget [PodDisruptionBudget](api-reference.md#poddisruptionbudget)                                         | PodDisruptionBudget defines the budget for replica availability.                                                                                                                                                                                                                                                                                     |         |                                    |
| updateStrategy [UpdateStrategy](api-reference.md#updatestrategy)                                                        | UpdateStrategy defines how a MariaDB resource is updated.                                                                                                                                                                                                                                                                                            |         |                                    |
| service [ServiceTemplate](api-reference.md#servicetemplate)                                                             | Service defines a template to configure the general Service object.The network traffic of this Service will be routed to all Pods.                                                                                                                                                                                                                   |         |                                    |
| connection [ConnectionTemplate](api-reference.md#connectiontemplate)                                                    | Connection defines a template to configure the general Connection object.This Connection provides the initial User access to the initial Database.It will make use of the Service to route network traffic to all Pods.                                                                                                                              |         |                                    |
| primaryService [ServiceTemplate](api-reference.md#servicetemplate)                                                      | PrimaryService defines a template to configure the primary Service object.The network traffic of this Service will be routed to the primary Pod.                                                                                                                                                                                                     |         |                                    |
| primaryConnection [ConnectionTemplate](api-reference.md#connectiontemplate)                                             | PrimaryConnection defines a template to configure the primary Connection object.This Connection provides the initial User access to the initial Database.It will make use of the PrimaryService to route network traffic to the primary Pod.                                                                                                         |         |                                    |
| secondaryService [ServiceTemplate](api-reference.md#servicetemplate)                                                    | SecondaryService defines a template to configure the secondary Service object.The network traffic of this Service will be routed to the secondary Pods.                                                                                                                                                                                              |         |                                    |
| secondaryConnection [ConnectionTemplate](api-reference.md#connectiontemplate)                                           | SecondaryConnection defines a template to configure the secondary Connection object.This Connection provides the initial User access to the initial Database.It will make use of the SecondaryService to route network traffic to the secondary Pods.                                                                                                |         |                                    |

#### MariadbMetrics

MariadbMetrics defines the metrics for a MariaDB.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                                                | Description                                                                                                                                                                                                                                    | Default | Validation |
| ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                | Description                                                                                                                                                                                                                                    | Default | Validation |
| enabled boolean                                                                      | Enabled is a flag to enable Metrics                                                                                                                                                                                                            |         |            |
| exporter [Exporter](api-reference.md#exporter)                                       | Exporter defines the metrics exporter container.                                                                                                                                                                                               |         |            |
| serviceMonitor [ServiceMonitor](api-reference.md#servicemonitor)                     | ServiceMonitor defines the ServiceMonior object.                                                                                                                                                                                               |         |            |
| username string                                                                      | Username is the username of the monitoring user used by the exporter.                                                                                                                                                                          |         |            |
| passwordSecretKeyRef [GeneratedSecretKeyRef](api-reference.md#generatedsecretkeyref) | PasswordSecretKeyRef is a reference to the password of the monitoring user used by the exporter.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password. |         |            |

#### MaxScale

MaxScale is the Schema for the maxscales API. It is used to define MaxScale clusters.

| Field                                                                                                          | Description                                                   | Default | Validation |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                          | Description                                                   | Default | Validation |
| apiVersion string                                                                                              | enterprise.mariadb.com/v1alpha1                               |         |            |
| kind string                                                                                                    | MaxScale                                                      |         |            |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |         |            |
| spec [MaxScaleSpec](api-reference.md#maxscalespec)                                                             |                                                               |         |            |

#### MaxScaleAdmin

MaxScaleAdmin configures the admin REST API and GUI.

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field              | Description                                                   | Default | Validation |
| ------------------ | ------------------------------------------------------------- | ------- | ---------- |
| Field              | Description                                                   | Default | Validation |
| port integer       | Port where the admin REST API and GUI will be exposed.        |         |            |
| guiEnabled boolean | GuiEnabled indicates whether the admin GUI should be enabled. |         |            |

#### MaxScaleAuth

MaxScaleAuth defines the credentials required for MaxScale to connect to MariaDB.

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                                       | Description                                                                                                                                                                                                                                                                                               | Default | Validation |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                       | Description                                                                                                                                                                                                                                                                                               | Default | Validation |
| generate boolean                                                                            | Generate defies whether the operator should generate users and grants for MaxScale to work.It only supports MariaDBs specified via spec.mariaDbRef.                                                                                                                                                       |         |            |
| adminUsername string                                                                        | AdminUsername is an admin username to call the admin REST API. It is defaulted if not provided.                                                                                                                                                                                                           |         |            |
| adminPasswordSecretKeyRef [GeneratedSecretKeyRef](api-reference.md#generatedsecretkeyref)   | AdminPasswordSecretKeyRef is Secret key reference to the admin password to call the admin REST API. It is defaulted if not provided.                                                                                                                                                                      |         |            |
| deleteDefaultAdmin boolean                                                                  | DeleteDefaultAdmin determines whether the default admin user should be deleted after the initial configuration. If not provided, it defaults to true.                                                                                                                                                     |         |            |
| metricsUsername string                                                                      | MetricsUsername is an metrics username to call the REST API. It is defaulted if metrics are enabled.                                                                                                                                                                                                      |         |            |
| metricsPasswordSecretKeyRef [GeneratedSecretKeyRef](api-reference.md#generatedsecretkeyref) | MetricsPasswordSecretKeyRef is Secret key reference to the metrics password to call the admib REST API. It is defaulted if metrics are enabled.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password.             |         |            |
| clientUsername string                                                                       | ClientUsername is the user to connect to MaxScale. It is defaulted if not provided.                                                                                                                                                                                                                       |         |            |
| clientPasswordSecretKeyRef [GeneratedSecretKeyRef](api-reference.md#generatedsecretkeyref)  | ClientPasswordSecretKeyRef is Secret key reference to the password to connect to MaxScale. It is defaulted if not provided.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password.                                 |         |            |
| clientMaxConnections integer                                                                | ClientMaxConnections defines the maximum number of connections that the client can establish.If HA is enabled, make sure to increase this value, as more MaxScale replicas implies more connections.It defaults to 30 times the number of MaxScale replicas.                                              |         |            |
| serverUsername string                                                                       | ServerUsername is the user used by MaxScale to connect to MariaDB server. It is defaulted if not provided.                                                                                                                                                                                                |         |            |
| serverPasswordSecretKeyRef [GeneratedSecretKeyRef](api-reference.md#generatedsecretkeyref)  | ServerPasswordSecretKeyRef is Secret key reference to the password used by MaxScale to connect to MariaDB server. It is defaulted if not provided.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password.          |         |            |
| serverMaxConnections integer                                                                | ServerMaxConnections defines the maximum number of connections that the server can establish.If HA is enabled, make sure to increase this value, as more MaxScale replicas implies more connections.It defaults to 30 times the number of MaxScale replicas.                                              |         |            |
| monitorUsername string                                                                      | MonitorUsername is the user used by MaxScale monitor to connect to MariaDB server. It is defaulted if not provided.                                                                                                                                                                                       |         |            |
| monitorPasswordSecretKeyRef [GeneratedSecretKeyRef](api-reference.md#generatedsecretkeyref) | MonitorPasswordSecretKeyRef is Secret key reference to the password used by MaxScale monitor to connect to MariaDB server. It is defaulted if not provided.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password. |         |            |
| monitorMaxConnections integer                                                               | MonitorMaxConnections defines the maximum number of connections that the monitor can establish.If HA is enabled, make sure to increase this value, as more MaxScale replicas implies more connections.It defaults to 30 times the number of MaxScale replicas.                                            |         |            |
| syncUsername string                                                                         | MonitoSyncUsernamerUsername is the user used by MaxScale config sync to connect to MariaDB server. It is defaulted when HA is enabled.                                                                                                                                                                    |         |            |
| syncPasswordSecretKeyRef [GeneratedSecretKeyRef](api-reference.md#generatedsecretkeyref)    | SyncPasswordSecretKeyRef is Secret key reference to the password used by MaxScale config to connect to MariaDB server. It is defaulted when HA is enabled.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password.  |         |            |
| syncMaxConnections integer                                                                  | SyncMaxConnections defines the maximum number of connections that the sync can establish.If HA is enabled, make sure to increase this value, as more MaxScale replicas implies more connections.It defaults to 30 times the number of MaxScale replicas.                                                  |         |            |

#### MaxScaleConfig

MaxScaleConfig defines the MaxScale configuration.

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                           | Description                                                                                                                                                                                                                                                                                       | Default | Validation |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                           | Description                                                                                                                                                                                                                                                                                       | Default | Validation |
| params object (keys:string, values:string)                                      | Params is a key value pair of parameters to be used in the MaxScale static configuration file.Any parameter supported by MaxScale may be specified here. See reference:[#global-settings](https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-maxscale-configuration-guide/#global-settings). |         |            |
| volumeClaimTemplate [VolumeClaimTemplate](api-reference.md#volumeclaimtemplate) | VolumeClaimTemplate provides a template to define the PVCs for storing MaxScale runtime configuration files. It is defaulted if not provided.                                                                                                                                                     |         |            |
| sync [MaxScaleConfigSync](api-reference.md#maxscaleconfigsync)                  | Sync defines how to replicate configuration across MaxScale replicas. It is defaulted when HA is enabled.                                                                                                                                                                                         |         |            |

#### MaxScaleConfigSync

MaxScaleConfigSync defines how the config changes are replicated across replicas.

_Appears in:_

* [MaxScaleConfig](api-reference.md#maxscaleconfig)

| Field                                                                                                      | Description                                                                                                                                                                              | Default | Validation |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                      | Description                                                                                                                                                                              | Default | Validation |
| database string                                                                                            | Database is the MariaDB logical database where the 'maxscale\_config' table will be created in order to persist and synchronize config changes. If not provided, it defaults to 'mysql'. |         |            |
| interval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | Interval defines the config synchronization interval. It is defaulted if not provided.                                                                                                   |         |            |
| timeout [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)  | Interval defines the config synchronization timeout. It is defaulted if not provided.                                                                                                    |         |            |

#### MaxScaleListener

MaxScaleListener defines how the MaxScale server will listen for connections.

_Appears in:_

* [MaxScaleService](api-reference.md#maxscaleservice)

| Field                                      | Description                                                                                                                                                                                                                                        | Default | Validation   |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------ |
| Field                                      | Description                                                                                                                                                                                                                                        | Default | Validation   |
| suspend boolean                            | Suspend indicates whether the current resource should be suspended or not.This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities.           | false   |              |
| name string                                | Name is the identifier of the listener. It is defaulted if not provided                                                                                                                                                                            |         |              |
| port integer                               | Port is the network port where the MaxScale server will listen.                                                                                                                                                                                    |         | Required: {} |
| protocol string                            | Protocol is the MaxScale protocol to use when communicating with the client. If not provided, it defaults to MariaDBProtocol.                                                                                                                      |         |              |
| params object (keys:string, values:string) | Params defines extra parameters to pass to the listener.Any parameter supported by MaxScale may be specified here. See reference:[#listener\_1](https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-maxscale-configuration-guide/#listener_1). |         |              |

#### MaxScaleMetrics

MaxScaleMetrics defines the metrics for a Maxscale.

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                            | Description                                      | Default | Validation |
| ---------------------------------------------------------------- | ------------------------------------------------ | ------- | ---------- |
| Field                                                            | Description                                      | Default | Validation |
| enabled boolean                                                  | Enabled is a flag to enable Metrics              |         |            |
| exporter [Exporter](api-reference.md#exporter)                   | Exporter defines the metrics exporter container. |         |            |
| serviceMonitor [ServiceMonitor](api-reference.md#servicemonitor) | ServiceMonitor defines the ServiceMonior object. |         |            |

#### MaxScaleMonitor

MaxScaleMonitor monitors MariaDB server instances

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Default | Validation                                       |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ------------------------------------------------ |
| Field                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Default | Validation                                       |
| suspend boolean                                                                                            | Suspend indicates whether the current resource should be suspended or not.This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | false   |                                                  |
| name string                                                                                                | Name is the identifier of the monitor. It is defaulted if not provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |         |                                                  |
| module [MonitorModule](api-reference.md#monitormodule)                                                     | Module is the module to use to monitor MariaDB servers. It is mandatory when no MariaDB reference is provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |         |                                                  |
| interval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | Interval used to monitor MariaDB servers. It is defaulted if not provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |         |                                                  |
| cooperativeMonitoring [CooperativeMonitoring](api-reference.md#cooperativemonitoring)                      | CooperativeMonitoring enables coordination between multiple MaxScale instances running monitors. It is defaulted when HA is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |         | Enum: \[majority\_of\_all majority\_of\_running] |
| params object (keys:string, values:string)                                                                 | <p>Params defines extra parameters to pass to the monitor.Any parameter supported by MaxScale may be specified here. See reference:[https://mariadb.com/kb/en/mariadb-maxscale-2308-common-monitor-parameters/.Monitor](https://mariadb.com/kb/en/mariadb-maxscale-2308-common-monitor-parameters/.<br>Monitor) specific parameter are also suported:[https://mariadb.com/kb/en/mariadb-maxscale-2308-galera-monitor/#galera-monitor-optional-parameters.https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-monitor/#configuration](https://mariadb.com/kb/en/mariadb-maxscale-2308-galera-monitor/#galera-monitor-optional-parameters.<br>https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-monitor/#configuration).</p> |         |                                                  |

#### MaxScalePodTemplate

MaxScalePodTemplate defines a template for MaxScale Pods.

_Appears in:_

* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                                                                   | Description                                                                        | Default | Validation |
| ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                                   | Description                                                                        | Default | Validation |
| podMetadata [Metadata](api-reference.md#metadata)                                                                       | PodMetadata defines extra metadata for the Pod.                                    |         |            |
| imagePullSecrets [LocalObjectReference](api-reference.md#localobjectreference) array                                    | ImagePullSecrets is the list of pull Secrets to be used to pull the image.         |         |            |
| podSecurityContext [PodSecurityContext](api-reference.md#podsecuritycontext)                                            | SecurityContext holds pod-level security attributes and common container settings. |         |            |
| serviceAccountName string                                                                                               | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.       |         |            |
| affinity [AffinityConfig](api-reference.md#affinityconfig)                                                              | Affinity to be used in the Pod.                                                    |         |            |
| nodeSelector object (keys:string, values:string)                                                                        | NodeSelector to be used in the Pod.                                                |         |            |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array | Tolerations to be used in the Pod.                                                 |         |            |
| priorityClassName string                                                                                                | PriorityClassName to be used in the Pod.                                           |         |            |
| topologySpreadConstraints [TopologySpreadConstraint](api-reference.md#topologyspreadconstraint) array                   | TopologySpreadConstraints to be used in the Pod.                                   |         |            |

#### MaxScaleServer

MaxScaleServer defines a MariaDB server to forward traffic to.

_Appears in:_

* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                      | Description                                                                                                                                                                                                                                  | Default | Validation   |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------ |
| Field                                      | Description                                                                                                                                                                                                                                  | Default | Validation   |
| name string                                | Name is the identifier of the MariaDB server.                                                                                                                                                                                                |         | Required: {} |
| address string                             | Address is the network address of the MariaDB server.                                                                                                                                                                                        |         | Required: {} |
| port integer                               | Port is the network port of the MariaDB server. If not provided, it defaults to 3306.                                                                                                                                                        |         |              |
| protocol string                            | Protocol is the MaxScale protocol to use when communicating with this MariaDB server. If not provided, it defaults to MariaDBBackend.                                                                                                        |         |              |
| maintenance boolean                        | Maintenance indicates whether the server is in maintenance mode.                                                                                                                                                                             |         |              |
| params object (keys:string, values:string) | Params defines extra parameters to pass to the server.Any parameter supported by MaxScale may be specified here. See reference:[#server\_1](https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-maxscale-configuration-guide/#server_1). |         |              |

#### MaxScaleService

Services define how the traffic is forwarded to the MariaDB servers.

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Default | Validation                                         |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | -------------------------------------------------- |
| Field                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Default | Validation                                         |
| suspend boolean                                                | Suspend indicates whether the current resource should be suspended or not.This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | false   |                                                    |
| name string                                                    | Name is the identifier of the MaxScale service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |         | Required: {}                                       |
| router [ServiceRouter](api-reference.md#servicerouter)         | Router is the type of router to use.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |         | Enum: \[readwritesplit readconnroute] Required: {} |
| listener [MaxScaleListener](api-reference.md#maxscalelistener) | MaxScaleListener defines how the MaxScale server will listen for connections.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |         | Required: {}                                       |
| params object (keys:string, values:string)                     | <p>Params defines extra parameters to pass to the service.Any parameter supported by MaxScale may be specified here. See reference:[https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-maxscale-configuration-guide/#service_1.Router](https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-maxscale-configuration-guide/#service_1.<br>Router) specific parameter are also suported:[https://mariadb.com/kb/en/mariadb-maxscale-2308-readwritesplit/#configuration.https://mariadb.com/kb/en/mariadb-maxscale-2308-readconnroute/#configuration](https://mariadb.com/kb/en/mariadb-maxscale-2308-readwritesplit/#configuration.<br>https://mariadb.com/kb/en/mariadb-maxscale-2308-readconnroute/#configuration).</p> |         |                                                    |

#### MaxScaleSpec

MaxScaleSpec defines the desired state of MaxScale.

_Appears in:_

* [MaxScale](api-reference.md#maxscale)

| Field                                                                                                                                              | Description                                                                                                                                                                                                                              | Default | Validation                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------- |
| Field                                                                                                                                              | Description                                                                                                                                                                                                                              | Default | Validation                         |
| command string array                                                                                                                               | Command to be used in the Container.                                                                                                                                                                                                     |         |                                    |
| args string array                                                                                                                                  | Args to be used in the Container.                                                                                                                                                                                                        |         |                                    |
| env [EnvVar](api-reference.md#envvar) array                                                                                                        | Env represents the environment variables to be injected in a container.                                                                                                                                                                  |         |                                    |
| envFrom [EnvFromSource](api-reference.md#envfromsource) array                                                                                      | EnvFrom represents the references (via ConfigMap and Secrets) to environment variables to be injected in the container.                                                                                                                  |         |                                    |
| volumeMounts [VolumeMount](api-reference.md#volumemount) array                                                                                     | VolumeMounts to be used in the Container.                                                                                                                                                                                                |         |                                    |
| livenessProbe [Probe](api-reference.md#probe)                                                                                                      | LivenessProbe to be used in the Container.                                                                                                                                                                                               |         |                                    |
| readinessProbe [Probe](api-reference.md#probe)                                                                                                     | ReadinessProbe to be used in the Container.                                                                                                                                                                                              |         |                                    |
| startupProbe [Probe](api-reference.md#probe)                                                                                                       | StartupProbe to be used in the Container.                                                                                                                                                                                                |         |                                    |
| resources [ResourceRequirements](api-reference.md#resourcerequirements)                                                                            | Resouces describes the compute resource requirements.                                                                                                                                                                                    |         |                                    |
| securityContext [SecurityContext](api-reference.md#securitycontext)                                                                                | SecurityContext holds security configuration that will be applied to a container.                                                                                                                                                        |         |                                    |
| podMetadata [Metadata](api-reference.md#metadata)                                                                                                  | PodMetadata defines extra metadata for the Pod.                                                                                                                                                                                          |         |                                    |
| imagePullSecrets [LocalObjectReference](api-reference.md#localobjectreference) array                                                               | ImagePullSecrets is the list of pull Secrets to be used to pull the image.                                                                                                                                                               |         |                                    |
| podSecurityContext [PodSecurityContext](api-reference.md#podsecuritycontext)                                                                       | SecurityContext holds pod-level security attributes and common container settings.                                                                                                                                                       |         |                                    |
| serviceAccountName string                                                                                                                          | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.                                                                                                                                                             |         |                                    |
| affinity [AffinityConfig](api-reference.md#affinityconfig)                                                                                         | Affinity to be used in the Pod.                                                                                                                                                                                                          |         |                                    |
| nodeSelector object (keys:string, values:string)                                                                                                   | NodeSelector to be used in the Pod.                                                                                                                                                                                                      |         |                                    |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array                            | Tolerations to be used in the Pod.                                                                                                                                                                                                       |         |                                    |
| priorityClassName string                                                                                                                           | PriorityClassName to be used in the Pod.                                                                                                                                                                                                 |         |                                    |
| topologySpreadConstraints [TopologySpreadConstraint](api-reference.md#topologyspreadconstraint) array                                              | TopologySpreadConstraints to be used in the Pod.                                                                                                                                                                                         |         |                                    |
| suspend boolean                                                                                                                                    | Suspend indicates whether the current resource should be suspended or not.This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities. | false   |                                    |
| mariaDbRef [MariaDBRef](api-reference.md#mariadbref)                                                                                               | MariaDBRef is a reference to the MariaDB that MaxScale points to. It is used to initialize the servers field.                                                                                                                            |         |                                    |
| servers [MaxScaleServer](api-reference.md#maxscaleserver) array                                                                                    | Servers are the MariaDB servers to forward traffic to. It is required if 'spec.mariaDbRef' is not provided.                                                                                                                              |         |                                    |
| image string                                                                                                                                       | Image name to be used by the MaxScale instances. The supported format is :.Only MaxScale official images are supported.                                                                                                                  |         |                                    |
| imagePullPolicy [PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#pullpolicy-v1-core)                              | ImagePullPolicy is the image pull policy. One of Always, Never or IfNotPresent. If not defined, it defaults to IfNotPresent.                                                                                                             |         | Enum: \[Always Never IfNotPresent] |
| inheritMetadata [Metadata](api-reference.md#metadata)                                                                                              | InheritMetadata defines the metadata to be inherited by children resources.                                                                                                                                                              |         |                                    |
| services [MaxScaleService](api-reference.md#maxscaleservice) array                                                                                 | Services define how the traffic is forwarded to the MariaDB servers. It is defaulted if not provided.                                                                                                                                    |         |                                    |
| monitor [MaxScaleMonitor](api-reference.md#maxscalemonitor)                                                                                        | Monitor monitors MariaDB server instances. It is required if 'spec.mariaDbRef' is not provided.                                                                                                                                          |         |                                    |
| admin [MaxScaleAdmin](api-reference.md#maxscaleadmin)                                                                                              | Admin configures the admin REST API and GUI.                                                                                                                                                                                             |         |                                    |
| config [MaxScaleConfig](api-reference.md#maxscaleconfig)                                                                                           | Config defines the MaxScale configuration.                                                                                                                                                                                               |         |                                    |
| auth [MaxScaleAuth](api-reference.md#maxscaleauth)                                                                                                 | Auth defines the credentials required for MaxScale to connect to MariaDB.                                                                                                                                                                |         |                                    |
| metrics [MaxScaleMetrics](api-reference.md#maxscalemetrics)                                                                                        | Metrics configures metrics and how to scrape them.                                                                                                                                                                                       |         |                                    |
| tls [MaxScaleTLS](api-reference.md#maxscaletls)                                                                                                    | TLS defines the PKI to be used with MaxScale.                                                                                                                                                                                            |         |                                    |
| connection [ConnectionTemplate](api-reference.md#connectiontemplate)                                                                               | Connection provides a template to define the Connection for MaxScale.                                                                                                                                                                    |         |                                    |
| replicas integer                                                                                                                                   | Replicas indicates the number of desired instances.                                                                                                                                                                                      | 1       |                                    |
| podDisruptionBudget [PodDisruptionBudget](api-reference.md#poddisruptionbudget)                                                                    | PodDisruptionBudget defines the budget for replica availability.                                                                                                                                                                         |         |                                    |
| updateStrategy [StatefulSetUpdateStrategy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#statefulsetupdatestrategy-v1-apps) | UpdateStrategy defines the update strategy for the StatefulSet object.                                                                                                                                                                   |         |                                    |
| kubernetesService [ServiceTemplate](api-reference.md#servicetemplate)                                                                              | KubernetesService defines a template for a Kubernetes Service object to connect to MaxScale.                                                                                                                                             |         |                                    |
| guiKubernetesService [ServiceTemplate](api-reference.md#servicetemplate)                                                                           | GuiKubernetesService defines a template for a Kubernetes Service object to connect to MaxScale's GUI.                                                                                                                                    |         |                                    |
| requeueInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)                                  | RequeueInterval is used to perform requeue reconciliations. If not defined, it defaults to 10s.                                                                                                                                          |         |                                    |

#### MaxScaleTLS

TLS defines the PKI to be used with MaxScale.

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Default | Validation |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ---------- |
| Field                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Default | Validation |
| enabled boolean                                                                     | Enabled indicates whether TLS is enabled, determining if certificates should be issued and mounted to the MaxScale instance.It is enabled by default when the referred MariaDB instance (via mariaDbRef) has TLS enabled and enforced.                                                                                                                                                                                                                                                                                                                                                           |         |            |
| adminVersions string array                                                          | Versions specifies the supported TLS versions in the MaxScale REST API.By default, the MaxScale's default supported versions are used. See: [mariadb-maxscale-25-mariadb-maxscale-configuration-guide#admin\_ssl\_version](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-25/maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide#admin_ssl_version)                                                                                                                                                                                            |         |            |
| serverVersions string array                                                         | ServerVersions specifies the supported TLS versions in both the servers and listeners managed by this MaxScale instance.By default, the MaxScale's default supported versions are used. See: [mariadb-maxscale-25-mariadb-maxscale-configuration-guide#ssl\_version](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-25/maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide#ssl_version).                                                                                                                                                       |         |            |
| adminCASecretRef [LocalObjectReference](api-reference.md#localobjectreference)      | AdminCASecretRef is a reference to a Secret containing the admin certificate authority keypair. It is used to establish trust and issue certificates for the MaxScale's administrative REST API and GUI.One of:- Secret containing both the 'ca.crt' and 'ca.key' keys. This allows you to bring your own CA to Kubernetes to issue certificates.- Secret containing only the 'ca.crt' in order to establish trust. In this case, either adminCertSecretRef or adminCertIssuerRef fields must be provided.If not provided, a self-signed CA will be provisioned to issue the server certificate. |         |            |
| adminCertSecretRef [LocalObjectReference](api-reference.md#localobjectreference)    | AdminCertSecretRef is a reference to a TLS Secret used by the MaxScale's administrative REST API and GUI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |         |            |
| adminCertIssuerRef [ObjectReference](api-reference.md#objectreference)              | AdminCertIssuerRef is a reference to a cert-manager issuer object used to issue the MaxScale's administrative REST API and GUI certificate. cert-manager must be installed previously in the cluster.It is mutually exclusive with adminCertSecretRef.By default, the Secret field 'ca.crt' provisioned by cert-manager will be added to the trust chain. A custom trust bundle may be specified via adminCASecretRef.                                                                                                                                                                           |         |            |
| adminCertConfig [TLSConfig](api-reference.md#tlsconfig)                             | AdminCertConfig allows configuring the admin certificates, either issued by the operator or cert-manager.If not set, the default settings will be used.                                                                                                                                                                                                                                                                                                                                                                                                                                          |         |            |
| listenerCASecretRef [LocalObjectReference](api-reference.md#localobjectreference)   | ListenerCASecretRef is a reference to a Secret containing the listener certificate authority keypair. It is used to establish trust and issue certificates for the MaxScale's listeners.One of:- Secret containing both the 'ca.crt' and 'ca.key' keys. This allows you to bring your own CA to Kubernetes to issue certificates.- Secret containing only the 'ca.crt' in order to establish trust. In this case, either listenerCertSecretRef or listenerCertIssuerRef fields must be provided.If not provided, a self-signed CA will be provisioned to issue the listener certificate.         |         |            |
| listenerCertSecretRef [LocalObjectReference](api-reference.md#localobjectreference) | ListenerCertSecretRef is a reference to a TLS Secret used by the MaxScale's listeners.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |         |            |
| listenerCertIssuerRef [ObjectReference](api-reference.md#objectreference)           | ListenerCertIssuerRef is a reference to a cert-manager issuer object used to issue the MaxScale's listeners certificate. cert-manager must be installed previously in the cluster.It is mutually exclusive with listenerCertSecretRef.By default, the Secret field 'ca.crt' provisioned by cert-manager will be added to the trust chain. A custom trust bundle may be specified via listenerCASecretRef.                                                                                                                                                                                        |         |            |
| listenerCertConfig [TLSConfig](api-reference.md#tlsconfig)                          | ListenerCertConfig allows configuring the listener certificates, either issued by the operator or cert-manager.If not set, the default settings will be used.                                                                                                                                                                                                                                                                                                                                                                                                                                    |         |            |
| serverCASecretRef [LocalObjectReference](api-reference.md#localobjectreference)     | ServerCASecretRef is a reference to a Secret containing the MariaDB server CA certificates. It is used to establish trust with MariaDB servers.The Secret should contain a 'ca.crt' key in order to establish trust.If not provided, and the reference to a MariaDB resource is set (mariaDbRef), it will be defaulted to the referred MariaDB CA bundle.                                                                                                                                                                                                                                        |         |            |
| serverCertSecretRef [LocalObjectReference](api-reference.md#localobjectreference)   | ServerCertSecretRef is a reference to a TLS Secret used by MaxScale to connect to the MariaDB servers.If not provided, and the reference to a MariaDB resource is set (mariaDbRef), it will be defaulted to the referred MariaDB client certificate (clientCertSecretRef).                                                                                                                                                                                                                                                                                                                       |         |            |
| verifyPeerCertificate boolean                                                       | VerifyPeerCertificate specifies whether the peer certificate's signature should be validated against the CA.It is disabled by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |         |            |
| verifyPeerHost boolean                                                              | VerifyPeerHost specifies whether the peer certificate's SANs should match the peer host.It is disabled by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |         |            |
| replicationSSLEnabled boolean                                                       | ReplicationSSLEnabled specifies whether the replication SSL is enabled. If enabled, the SSL options will be added to the server configuration.It is enabled by default when the referred MariaDB instance (via mariaDbRef) has replication enabled.If the MariaDB servers are manually provided by the user via the 'servers' field, this must be set by the user as well.                                                                                                                                                                                                                       |         |            |

#### Metadata

Metadata defines the metadata to added to resources.

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [Exporter](api-reference.md#exporter)
* [GaleraInitJob](api-reference.md#galerainitjob)
* [GaleraRecoveryJob](api-reference.md#galerarecoveryjob)
* [Job](api-reference.md#job)
* [JobPodTemplate](api-reference.md#jobpodtemplate)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScalePodTemplate](api-reference.md#maxscalepodtemplate)
* [MaxScaleSpec](api-reference.md#maxscalespec)
* [PodTemplate](api-reference.md#podtemplate)
* [RestoreSpec](api-reference.md#restorespec)
* [SecretTemplate](api-reference.md#secrettemplate)
* [ServiceTemplate](api-reference.md#servicetemplate)
* [SqlJobSpec](api-reference.md#sqljobspec)
* [VolumeClaimTemplate](api-reference.md#volumeclaimtemplate)

| Field                                           | Description                                    | Default | Validation |
| ----------------------------------------------- | ---------------------------------------------- | ------- | ---------- |
| Field                                           | Description                                    | Default | Validation |
| labels object (keys:string, values:string)      | Labels to be added to children resources.      |         |            |
| annotations object (keys:string, values:string) | Annotations to be added to children resources. |         |            |

#### MonitorModule

_Underlying type:_ _string_

MonitorModule defines the type of monitor module

_Appears in:_

* [MaxScaleMonitor](api-reference.md#maxscalemonitor)

| Field      | Description                                                        |
| ---------- | ------------------------------------------------------------------ |
| Field      | Description                                                        |
| mariadbmon | MonitorModuleMariadb is a monitor to be used with MariaDB servers. |
| galeramon  | MonitorModuleGalera is a monitor to be used with Galera servers.   |

#### NFSVolumeSource

Refer to the Kubernetes docs: [#nfsvolumesource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#nfsvolumesource-v1-core).

_Appears in:_

* [StorageVolumeSource](api-reference.md#storagevolumesource)
* [Volume](api-reference.md#volume)
* [VolumeSource](api-reference.md#volumesource)

| Field            | Description | Default | Validation |
| ---------------- | ----------- | ------- | ---------- |
| Field            | Description | Default | Validation |
| server string    |             |         |            |
| path string      |             |         |            |
| readOnly boolean |             |         |            |

#### NodeAffinity

Refer to the Kubernetes docs: [#nodeaffinity-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#nodeaffinity-v1-core)

_Appears in:_

* [Affinity](api-reference.md#affinity)
* [AffinityConfig](api-reference.md#affinityconfig)

| Field                                                                                                                     | Description | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                                                                                     | Description | Default | Validation |
| requiredDuringSchedulingIgnoredDuringExecution [NodeSelector](api-reference.md#nodeselector)                              |             |         |            |
| preferredDuringSchedulingIgnoredDuringExecution [PreferredSchedulingTerm](api-reference.md#preferredschedulingterm) array |             |         |            |

#### NodeSelector

Refer to the Kubernetes docs: [#nodeselector-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#nodeselector-v1-core)

_Appears in:_

* [NodeAffinity](api-reference.md#nodeaffinity)

| Field                                                                         | Description | Default | Validation |
| ----------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                                         | Description | Default | Validation |
| nodeSelectorTerms [NodeSelectorTerm](api-reference.md#nodeselectorterm) array |             |         |            |

#### NodeSelectorTerm

_Underlying type:_ [_struct{MatchExpressions \[\]NodeSelectorRequirement "json:"matchExpressions,omitempty""; MatchFields \[\]NodeSelectorRequirement "json:"matchFields,omitempty""}_](api-reference.md#struct{matchexpressions-\[]nodeselectorrequirement-"json:"matchexpressions,omitempty"";-matchfields-\[]nodeselectorrequirement-"json:"matchfields,omitempty""})

Refer to the Kubernetes docs: [#nodeselectorterm-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#nodeselectorterm-v1-core)

_Appears in:_

* [NodeSelector](api-reference.md#nodeselector)
* [PreferredSchedulingTerm](api-reference.md#preferredschedulingterm)

#### ObjectFieldSelector

Refer to the Kubernetes docs: [#objectfieldselector-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectfieldselector-v1-core).

_Appears in:_

* [EnvVarSource](api-reference.md#envvarsource)

| Field             | Description | Default | Validation |
| ----------------- | ----------- | ------- | ---------- |
| Field             | Description | Default | Validation |
| apiVersion string |             |         |            |
| fieldPath string  |             |         |            |

#### ObjectReference

Refer to the Kubernetes docs: [#objectreference-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectreference-v1-core).

_Appears in:_

* [ConnectionSpec](api-reference.md#connectionspec)
* [MariaDBRef](api-reference.md#mariadbref)
* [MariaDBSpec](api-reference.md#mariadbspec)

| Field            | Description | Default | Validation |
| ---------------- | ----------- | ------- | ---------- |
| Field            | Description | Default | Validation |
| name string      |             |         |            |
| namespace string |             |         |            |

#### PasswordPlugin

PasswordPlugin defines the password plugin and its arguments.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)
* [UserSpec](api-reference.md#userspec)

| Field                                                                          | Description                                                                                                                                                                                                                                                                          | Default | Validation |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ---------- |
| Field                                                                          | Description                                                                                                                                                                                                                                                                          | Default | Validation |
| pluginNameSecretKeyRef [SecretKeySelector](api-reference.md#secretkeyselector) | PluginNameSecretKeyRef is a reference to the authentication plugin to be used by the User.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the authentication plugin.                                |         |            |
| pluginArgSecretKeyRef [SecretKeySelector](api-reference.md#secretkeyselector)  | PluginArgSecretKeyRef is a reference to the arguments to be provided to the authentication plugin for the User.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the authentication plugin arguments. |         |            |

#### PersistentVolumeClaimSpec

Refer to the Kubernetes docs: [#persistentvolumeclaimspec-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#persistentvolumeclaimspec-v1-core).

_Appears in:_

* [BackupStagingStorage](api-reference.md#backupstagingstorage)
* [BackupStorage](api-reference.md#backupstorage)
* [VolumeClaimTemplate](api-reference.md#volumeclaimtemplate)

| Field                                                                                                                                                   | Description | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                                                                                                                   | Description | Default | Validation |
| accessModes [PersistentVolumeAccessMode](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#persistentvolumeaccessmode-v1-core) array |             |         |            |
| selector [LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#labelselector-v1-meta)                                    |             |         |            |
| resources [VolumeResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#volumeresourcerequirements-v1-core)         |             |         |            |
| storageClassName string                                                                                                                                 |             |         |            |

#### PersistentVolumeClaimVolumeSource

Refer to the Kubernetes docs: [#persistentvolumeclaimvolumesource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#persistentvolumeclaimvolumesource-v1-core).

_Appears in:_

* [StorageVolumeSource](api-reference.md#storagevolumesource)
* [Volume](api-reference.md#volume)
* [VolumeSource](api-reference.md#volumesource)

| Field            | Description | Default | Validation |
| ---------------- | ----------- | ------- | ---------- |
| Field            | Description | Default | Validation |
| claimName string |             |         |            |
| readOnly boolean |             |         |            |

#### PodAffinityTerm

Refer to the Kubernetes docs: [#podaffinityterm-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#podaffinityterm-v1-core).

_Appears in:_

* [PodAntiAffinity](api-reference.md#podantiaffinity)
* [WeightedPodAffinityTerm](api-reference.md#weightedpodaffinityterm)

| Field                                                         | Description | Default | Validation |
| ------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                         | Description | Default | Validation |
| labelSelector [LabelSelector](api-reference.md#labelselector) |             |         |            |
| topologyKey string                                            |             |         |            |

#### PodAntiAffinity

Refer to the Kubernetes docs: [#podantiaffinity-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#podantiaffinity-v1-core).

_Appears in:_

* [Affinity](api-reference.md#affinity)
* [AffinityConfig](api-reference.md#affinityconfig)

| Field                                                                                                                     | Description | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                                                                                     | Description | Default | Validation |
| requiredDuringSchedulingIgnoredDuringExecution [PodAffinityTerm](api-reference.md#podaffinityterm) array                  |             |         |            |
| preferredDuringSchedulingIgnoredDuringExecution [WeightedPodAffinityTerm](api-reference.md#weightedpodaffinityterm) array |             |         |            |

#### PodDisruptionBudget

PodDisruptionBudget is the Pod availability bundget for a MariaDB

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                                                                      | Description                                                    | Default | Validation |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                                      | Description                                                    | Default | Validation |
| minAvailable [IntOrString](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#intorstring-intstr-util)   | MinAvailable defines the number of minimum available Pods.     |         |            |
| maxUnavailable [IntOrString](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#intorstring-intstr-util) | MaxUnavailable defines the number of maximum unavailable Pods. |         |            |

#### PodSecurityContext

Refer to the Kubernetes docs: [#podsecuritycontext-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#podsecuritycontext-v1-core)

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [Exporter](api-reference.md#exporter)
* [JobPodTemplate](api-reference.md#jobpodtemplate)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScalePodTemplate](api-reference.md#maxscalepodtemplate)
* [MaxScaleSpec](api-reference.md#maxscalespec)
* [PodTemplate](api-reference.md#podtemplate)
* [RestoreSpec](api-reference.md#restorespec)
* [SqlJobSpec](api-reference.md#sqljobspec)

| Field                                                                                                                                             | Description | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                                                                                                             | Description | Default | Validation |
| seLinuxOptions [SELinuxOptions](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#selinuxoptions-v1-core)                      |             |         |            |
| runAsUser integer                                                                                                                                 |             |         |            |
| runAsGroup integer                                                                                                                                |             |         |            |
| runAsNonRoot boolean                                                                                                                              |             |         |            |
| supplementalGroups integer array                                                                                                                  |             |         |            |
| fsGroup integer                                                                                                                                   |             |         |            |
| fsGroupChangePolicy [PodFSGroupChangePolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#podfsgroupchangepolicy-v1-core) |             |         |            |
| seccompProfile [SeccompProfile](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#seccompprofile-v1-core)                      |             |         |            |
| appArmorProfile [AppArmorProfile](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#apparmorprofile-v1-core)                   |             |         |            |

#### PodTemplate

PodTemplate defines a template to configure Container objects.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                                                                                   | Description                                                                        | Default | Validation |
| ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                                   | Description                                                                        | Default | Validation |
| podMetadata [Metadata](api-reference.md#metadata)                                                                       | PodMetadata defines extra metadata for the Pod.                                    |         |            |
| imagePullSecrets [LocalObjectReference](api-reference.md#localobjectreference) array                                    | ImagePullSecrets is the list of pull Secrets to be used to pull the image.         |         |            |
| initContainers [Container](api-reference.md#container) array                                                            | InitContainers to be used in the Pod.                                              |         |            |
| sidecarContainers [Container](api-reference.md#container) array                                                         | SidecarContainers to be used in the Pod.                                           |         |            |
| podSecurityContext [PodSecurityContext](api-reference.md#podsecuritycontext)                                            | SecurityContext holds pod-level security attributes and common container settings. |         |            |
| serviceAccountName string                                                                                               | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.       |         |            |
| affinity [AffinityConfig](api-reference.md#affinityconfig)                                                              | Affinity to be used in the Pod.                                                    |         |            |
| nodeSelector object (keys:string, values:string)                                                                        | NodeSelector to be used in the Pod.                                                |         |            |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array | Tolerations to be used in the Pod.                                                 |         |            |
| volumes [Volume](api-reference.md#volume) array                                                                         | Volumes to be used in the Pod.                                                     |         |            |
| priorityClassName string                                                                                                | PriorityClassName to be used in the Pod.                                           |         |            |
| topologySpreadConstraints [TopologySpreadConstraint](api-reference.md#topologyspreadconstraint) array                   | TopologySpreadConstraints to be used in the Pod.                                   |         |            |

#### PreferredSchedulingTerm

Refer to the Kubernetes docs: [#preferredschedulingterm-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#preferredschedulingterm-v1-core)

_Appears in:_

* [NodeAffinity](api-reference.md#nodeaffinity)

| Field                                                            | Description | Default | Validation |
| ---------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                            | Description | Default | Validation |
| weight integer                                                   |             |         |            |
| preference [NodeSelectorTerm](api-reference.md#nodeselectorterm) |             |         |            |

#### PrimaryGalera

PrimaryGalera is the Galera configuration for the primary node.

_Appears in:_

* [Galera](api-reference.md#galera)
* [GaleraSpec](api-reference.md#galeraspec)

| Field                     | Description                                                                                                                     | Default | Validation |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field                     | Description                                                                                                                     | Default | Validation |
| podIndex integer          | PodIndex is the StatefulSet index of the primary node. The user may change this field to perform a manual switchover.           |         |            |
| automaticFailover boolean | AutomaticFailover indicates whether the operator should automatically update PodIndex to perform an automatic primary failover. |         |            |

#### Probe

Refer to the Kubernetes docs: [#probe-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#probe-v1-core).

_Appears in:_

* [ContainerTemplate](api-reference.md#containertemplate)
* [GaleraAgent](api-reference.md#galeraagent)
* [GaleraInit](api-reference.md#galerainit)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                         | Description | Default | Validation |
| ------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                         | Description | Default | Validation |
| exec [ExecAction](api-reference.md#execaction)                |             |         |            |
| httpGet [HTTPGetAction](api-reference.md#httpgetaction)       |             |         |            |
| tcpSocket [TCPSocketAction](api-reference.md#tcpsocketaction) |             |         |            |
| initialDelaySeconds integer                                   |             |         |            |
| timeoutSeconds integer                                        |             |         |            |
| periodSeconds integer                                         |             |         |            |
| successThreshold integer                                      |             |         |            |
| failureThreshold integer                                      |             |         |            |

#### ProbeHandler

Refer to the Kubernetes docs: [#probe-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#probe-v1-core).

_Appears in:_

* [Probe](api-reference.md#probe)

| Field                                                         | Description | Default | Validation |
| ------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                         | Description | Default | Validation |
| exec [ExecAction](api-reference.md#execaction)                |             |         |            |
| httpGet [HTTPGetAction](api-reference.md#httpgetaction)       |             |         |            |
| tcpSocket [TCPSocketAction](api-reference.md#tcpsocketaction) |             |         |            |

#### ResourceRequirements

Refer to the Kubernetes docs: [#resourcerequirements-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcerequirements-v1-core).

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [Container](api-reference.md#container)
* [ContainerTemplate](api-reference.md#containertemplate)
* [Exporter](api-reference.md#exporter)
* [GaleraAgent](api-reference.md#galeraagent)
* [GaleraInit](api-reference.md#galerainit)
* [GaleraInitJob](api-reference.md#galerainitjob)
* [GaleraRecoveryJob](api-reference.md#galerarecoveryjob)
* [Job](api-reference.md#job)
* [JobContainerTemplate](api-reference.md#jobcontainertemplate)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)
* [RestoreSpec](api-reference.md#restorespec)
* [SqlJobSpec](api-reference.md#sqljobspec)

#### Restore

Restore is the Schema for the restores API. It is used to define restore jobs and its restoration source.

| Field                                                                                                          | Description                                                   | Default | Validation |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                          | Description                                                   | Default | Validation |
| apiVersion string                                                                                              | enterprise.mariadb.com/v1alpha1                               |         |            |
| kind string                                                                                                    | Restore                                                       |         |            |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |         |            |
| spec [RestoreSpec](api-reference.md#restorespec)                                                               |                                                               |         |            |

#### RestoreSource

RestoreSource defines a source for restoring a MariaDB.

_Appears in:_

* [BootstrapFrom](api-reference.md#bootstrapfrom)
* [RestoreSpec](api-reference.md#restorespec)

| Field                                                                                                        | Description                                                                                                                                                                                                                                                | Default | Validation |
| ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                        | Description                                                                                                                                                                                                                                                | Default | Validation |
| backupRef [LocalObjectReference](api-reference.md#localobjectreference)                                      | BackupRef is a reference to a Backup object. It has priority over S3 and Volume.                                                                                                                                                                           |         |            |
| s3 [S3](api-reference.md#s3)                                                                                 | S3 defines the configuration to restore backups from a S3 compatible storage. It has priority over Volume.                                                                                                                                                 |         |            |
| volume [StorageVolumeSource](api-reference.md#storagevolumesource)                                           | Volume is a Kubernetes Volume object that contains a backup.                                                                                                                                                                                               |         |            |
| targetRecoveryTime [Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#time-v1-meta) | TargetRecoveryTime is a RFC3339 (1970-01-01T00:00:00Z) date and time that defines the point in time recovery objective.It is used to determine the closest restoration source in time.                                                                     |         |            |
| stagingStorage [BackupStagingStorage](api-reference.md#backupstagingstorage)                                 | StagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.It defaults to an emptyDir volume, meaning that the backups will be temporarily stored in the node where the Restore Job is scheduled. |         |            |

#### RestoreSpec

RestoreSpec defines the desired state of restore

_Appears in:_

* [Restore](api-reference.md#restore)

| Field                                                                                                                     | Description                                                                                                                                                                                                                                                | Default   | Validation                      |
| ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------- |
| Field                                                                                                                     | Description                                                                                                                                                                                                                                                | Default   | Validation                      |
| args string array                                                                                                         | Args to be used in the Container.                                                                                                                                                                                                                          |           |                                 |
| resources [ResourceRequirements](api-reference.md#resourcerequirements)                                                   | Resouces describes the compute resource requirements.                                                                                                                                                                                                      |           |                                 |
| securityContext [SecurityContext](api-reference.md#securitycontext)                                                       | SecurityContext holds security configuration that will be applied to a container.                                                                                                                                                                          |           |                                 |
| podMetadata [Metadata](api-reference.md#metadata)                                                                         | PodMetadata defines extra metadata for the Pod.                                                                                                                                                                                                            |           |                                 |
| imagePullSecrets [LocalObjectReference](api-reference.md#localobjectreference) array                                      | ImagePullSecrets is the list of pull Secrets to be used to pull the image.                                                                                                                                                                                 |           |                                 |
| podSecurityContext [PodSecurityContext](api-reference.md#podsecuritycontext)                                              | SecurityContext holds pod-level security attributes and common container settings.                                                                                                                                                                         |           |                                 |
| serviceAccountName string                                                                                                 | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.                                                                                                                                                                               |           |                                 |
| affinity [AffinityConfig](api-reference.md#affinityconfig)                                                                | Affinity to be used in the Pod.                                                                                                                                                                                                                            |           |                                 |
| nodeSelector object (keys:string, values:string)                                                                          | NodeSelector to be used in the Pod.                                                                                                                                                                                                                        |           |                                 |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array   | Tolerations to be used in the Pod.                                                                                                                                                                                                                         |           |                                 |
| priorityClassName string                                                                                                  | PriorityClassName to be used in the Pod.                                                                                                                                                                                                                   |           |                                 |
| backupRef [LocalObjectReference](api-reference.md#localobjectreference)                                                   | BackupRef is a reference to a Backup object. It has priority over S3 and Volume.                                                                                                                                                                           |           |                                 |
| s3 [S3](api-reference.md#s3)                                                                                              | S3 defines the configuration to restore backups from a S3 compatible storage. It has priority over Volume.                                                                                                                                                 |           |                                 |
| volume [StorageVolumeSource](api-reference.md#storagevolumesource)                                                        | Volume is a Kubernetes Volume object that contains a backup.                                                                                                                                                                                               |           |                                 |
| targetRecoveryTime [Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#time-v1-meta)              | TargetRecoveryTime is a RFC3339 (1970-01-01T00:00:00Z) date and time that defines the point in time recovery objective.It is used to determine the closest restoration source in time.                                                                     |           |                                 |
| stagingStorage [BackupStagingStorage](api-reference.md#backupstagingstorage)                                              | StagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.It defaults to an emptyDir volume, meaning that the backups will be temporarily stored in the node where the Restore Job is scheduled. |           |                                 |
| mariaDbRef [MariaDBRef](api-reference.md#mariadbref)                                                                      | MariaDBRef is a reference to a MariaDB object.                                                                                                                                                                                                             |           | Required: {}                    |
| database string                                                                                                           | Database defines the logical database to be restored. If not provided, all databases available in the backup are restored.IMPORTANT: The database must previously exist.                                                                                   |           |                                 |
| logLevel string                                                                                                           | LogLevel to be used n the Backup Job. It defaults to 'info'.                                                                                                                                                                                               | info      |                                 |
| backoffLimit integer                                                                                                      | BackoffLimit defines the maximum number of attempts to successfully perform a Backup.                                                                                                                                                                      | 5         |                                 |
| restartPolicy [RestartPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#restartpolicy-v1-core) | RestartPolicy to be added to the Backup Job.                                                                                                                                                                                                               | OnFailure | Enum: \[Always OnFailure Never] |
| inheritMetadata [Metadata](api-reference.md#metadata)                                                                     | InheritMetadata defines the metadata to be inherited by children resources.                                                                                                                                                                                |           |                                 |

#### S3

_Appears in:_

* [BackupStorage](api-reference.md#backupstorage)
* [BootstrapFrom](api-reference.md#bootstrapfrom)
* [RestoreSource](api-reference.md#restoresource)
* [RestoreSpec](api-reference.md#restorespec)

| Field                                                                               | Description                                                                                                                                 | Default | Validation   |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------ |
| Field                                                                               | Description                                                                                                                                 | Default | Validation   |
| bucket string                                                                       | Bucket is the name Name of the bucket to store backups.                                                                                     |         | Required: {} |
| endpoint string                                                                     | Endpoint is the S3 API endpoint without scheme.                                                                                             |         | Required: {} |
| region string                                                                       | Region is the S3 region name to use.                                                                                                        |         |              |
| prefix string                                                                       | Prefix indicates a folder/subfolder in the bucket. For example: mariadb/ or mariadb/backups. A trailing slash '/' is added if not provided. |         |              |
| accessKeyIdSecretKeyRef [SecretKeySelector](api-reference.md#secretkeyselector)     | AccessKeyIdSecretKeyRef is a reference to a Secret key containing the S3 access key id.                                                     |         |              |
| secretAccessKeySecretKeyRef [SecretKeySelector](api-reference.md#secretkeyselector) | AccessKeyIdSecretKeyRef is a reference to a Secret key containing the S3 secret key.                                                        |         |              |
| sessionTokenSecretKeyRef [SecretKeySelector](api-reference.md#secretkeyselector)    | SessionTokenSecretKeyRef is a reference to a Secret key containing the S3 session token.                                                    |         |              |
| tls [TLSS3](api-reference.md#tlss3)                                                 | TLS provides the configuration required to establish TLS connections with S3.                                                               |         |              |

#### SQLTemplate

SQLTemplate defines a template to customize SQL objects.

_Appears in:_

* [DatabaseSpec](api-reference.md#databasespec)
* [GrantSpec](api-reference.md#grantspec)
* [UserSpec](api-reference.md#userspec)

| Field                                                                                                             | Description                                                        | Default | Validation           |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------- | -------------------- |
| Field                                                                                                             | Description                                                        | Default | Validation           |
| requeueInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | RequeueInterval is used to perform requeue reconciliations.        |         |                      |
| retryInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)   | RetryInterval is the interval used to perform retries.             |         |                      |
| cleanupPolicy [CleanupPolicy](api-reference.md#cleanuppolicy)                                                     | CleanupPolicy defines the behavior for cleaning up a SQL resource. |         | Enum: \[Skip Delete] |

#### SST

_Underlying type:_ _string_

SST is the Snapshot State Transfer used when new Pods join the cluster.\
More info: [sst.html](https://galeracluster.com/library/documentation/sst.html).

_Appears in:_

* [Galera](api-reference.md#galera)
* [GaleraSpec](api-reference.md#galeraspec)

| Field       | Description                                                               |
| ----------- | ------------------------------------------------------------------------- |
| Field       | Description                                                               |
| rsync       | SSTRsync is an SST based on rsync.                                        |
| mariabackup | SSTMariaBackup is an SST based on mariabackup. It is the recommended SST. |
| mysqldump   | SSTMysqldump is an SST based on mysqldump.                                |

#### Schedule

Schedule contains parameters to define a schedule

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [SqlJobSpec](api-reference.md#sqljobspec)

| Field           | Description                                            | Default | Validation   |
| --------------- | ------------------------------------------------------ | ------- | ------------ |
| Field           | Description                                            | Default | Validation   |
| cron string     | Cron is a cron expression that defines the schedule.   |         | Required: {} |
| suspend boolean | Suspend defines whether the schedule is active or not. | false   |              |

#### SecretKeySelector

Refer to the Kubernetes docs: [#secretkeyselector-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#secretkeyselector-v1-core).

_Appears in:_

* [ConnectionSpec](api-reference.md#connectionspec)
* [EnvVarSource](api-reference.md#envvarsource)
* [GeneratedSecretKeyRef](api-reference.md#generatedsecretkeyref)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [PasswordPlugin](api-reference.md#passwordplugin)
* [S3](api-reference.md#s3)
* [SqlJobSpec](api-reference.md#sqljobspec)
* [TLSS3](api-reference.md#tlss3)
* [UserSpec](api-reference.md#userspec)

| Field       | Description | Default | Validation |
| ----------- | ----------- | ------- | ---------- |
| Field       | Description | Default | Validation |
| name string |             |         |            |
| key string  |             |         |            |

#### SecretTemplate

SecretTemplate defines a template to customize Secret objects.

_Appears in:_

* [ConnectionSpec](api-reference.md#connectionspec)
* [ConnectionTemplate](api-reference.md#connectiontemplate)

| Field                                          | Description                                                   | Default | Validation |
| ---------------------------------------------- | ------------------------------------------------------------- | ------- | ---------- |
| Field                                          | Description                                                   | Default | Validation |
| metadata [Metadata](api-reference.md#metadata) | Refer to Kubernetes API documentation for fields of metadata. |         |            |
| key string                                     | Key to be used in the Secret.                                 |         |            |
| format string                                  | Format to be used in the Secret.                              |         |            |
| usernameKey string                             | UsernameKey to be used in the Secret.                         |         |            |
| passwordKey string                             | PasswordKey to be used in the Secret.                         |         |            |
| hostKey string                                 | HostKey to be used in the Secret.                             |         |            |
| portKey string                                 | PortKey to be used in the Secret.                             |         |            |
| databaseKey string                             | DatabaseKey to be used in the Secret.                         |         |            |

#### SecretVolumeSource

Refer to the Kubernetes docs: [#secretvolumesource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#secretvolumesource-v1-core).

_Appears in:_

* [Volume](api-reference.md#volume)
* [VolumeSource](api-reference.md#volumesource)

| Field               | Description | Default | Validation |
| ------------------- | ----------- | ------- | ---------- |
| Field               | Description | Default | Validation |
| secretName string   |             |         |            |
| defaultMode integer |             |         |            |

#### SecurityContext

Refer to the Kubernetes docs: [#securitycontext-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#securitycontext-v1-core).

_Appears in:_

* [BackupSpec](api-reference.md#backupspec)
* [ContainerTemplate](api-reference.md#containertemplate)
* [Exporter](api-reference.md#exporter)
* [GaleraAgent](api-reference.md#galeraagent)
* [GaleraInit](api-reference.md#galerainit)
* [JobContainerTemplate](api-reference.md#jobcontainertemplate)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)
* [RestoreSpec](api-reference.md#restorespec)
* [SqlJobSpec](api-reference.md#sqljobspec)

| Field                                                                                                                  | Description | Default | Validation |
| ---------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                                                                                  | Description | Default | Validation |
| capabilities [Capabilities](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#capabilities-v1-core) |             |         |            |
| privileged boolean                                                                                                     |             |         |            |
| runAsUser integer                                                                                                      |             |         |            |
| runAsGroup integer                                                                                                     |             |         |            |
| runAsNonRoot boolean                                                                                                   |             |         |            |
| readOnlyRootFilesystem boolean                                                                                         |             |         |            |
| allowPrivilegeEscalation boolean                                                                                       |             |         |            |

#### ServiceMonitor

ServiceMonitor defines a prometheus ServiceMonitor object.

_Appears in:_

* [MariadbMetrics](api-reference.md#mariadbmetrics)
* [MaxScaleMetrics](api-reference.md#maxscalemetrics)

| Field                    | Description                                                                 | Default | Validation |
| ------------------------ | --------------------------------------------------------------------------- | ------- | ---------- |
| Field                    | Description                                                                 | Default | Validation |
| prometheusRelease string | PrometheusRelease is the release label to add to the ServiceMonitor object. |         |            |
| jobLabel string          | JobLabel to add to the ServiceMonitor object.                               |         |            |
| interval string          | Interval for scraping metrics.                                              |         |            |
| scrapeTimeout string     | ScrapeTimeout defines the timeout for scraping metrics.                     |         |            |

#### ServicePort

Refer to the Kubernetes docs: [#serviceport-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#serviceport-v1-core)

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field        | Description | Default | Validation |
| ------------ | ----------- | ------- | ---------- |
| Field        | Description | Default | Validation |
| name string  |             |         |            |
| port integer |             |         |            |

#### ServiceRouter

_Underlying type:_ _string_

ServiceRouter defines the type of service router.

_Appears in:_

* [MaxScaleService](api-reference.md#maxscaleservice)

| Field          | Description                                                                                                                               |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Field          | Description                                                                                                                               |
| readwritesplit | ServiceRouterReadWriteSplit splits the load based on the queries. Write queries are performed on master and read queries on the replicas. |
| readconnroute  | ServiceRouterReadConnRoute splits the load based on the connections. Each connection is assigned to a server.                             |

#### ServiceTemplate

ServiceTemplate defines a template to customize Service objects.

_Appears in:_

* [MariaDBMaxScaleSpec](api-reference.md#mariadbmaxscalespec)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field                                                                                                                                                           | Description                                                                                                     | Default   | Validation                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------- | ---------------------------------------- |
| Field                                                                                                                                                           | Description                                                                                                     | Default   | Validation                               |
| type [ServiceType](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#servicetype-v1-core)                                                    | Type is the Service type. One of ClusterIP, NodePort or LoadBalancer. If not defined, it defaults to ClusterIP. | ClusterIP | Enum: \[ClusterIP NodePort LoadBalancer] |
| metadata [Metadata](api-reference.md#metadata)                                                                                                                  | Refer to Kubernetes API documentation for fields of metadata.                                                   |           |                                          |
| loadBalancerIP string                                                                                                                                           | LoadBalancerIP Service field.                                                                                   |           |                                          |
| loadBalancerSourceRanges string array                                                                                                                           | LoadBalancerSourceRanges Service field.                                                                         |           |                                          |
| externalTrafficPolicy [ServiceExternalTrafficPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#serviceexternaltrafficpolicy-v1-core) | ExternalTrafficPolicy Service field.                                                                            |           |                                          |
| sessionAffinity [ServiceAffinity](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#serviceaffinity-v1-core)                                 | SessionAffinity Service field.                                                                                  |           |                                          |
| allocateLoadBalancerNodePorts boolean                                                                                                                           | AllocateLoadBalancerNodePorts Service field.                                                                    |           |                                          |

#### SqlJob

SqlJob is the Schema for the sqljobs API. It is used to run sql scripts as jobs.

| Field                                                                                                          | Description                                                   | Default | Validation |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                          | Description                                                   | Default | Validation |
| apiVersion string                                                                                              | enterprise.mariadb.com/v1alpha1                               |         |            |
| kind string                                                                                                    | SqlJob                                                        |         |            |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |         |            |
| spec [SqlJobSpec](api-reference.md#sqljobspec)                                                                 |                                                               |         |            |

#### SqlJobSpec

SqlJobSpec defines the desired state of SqlJob

_Appears in:_

* [SqlJob](api-reference.md#sqljob)

| Field                                                                                                                     | Description                                                                                                                                                                                         | Default   | Validation                      |
| ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------- |
| Field                                                                                                                     | Description                                                                                                                                                                                         | Default   | Validation                      |
| args string array                                                                                                         | Args to be used in the Container.                                                                                                                                                                   |           |                                 |
| resources [ResourceRequirements](api-reference.md#resourcerequirements)                                                   | Resouces describes the compute resource requirements.                                                                                                                                               |           |                                 |
| securityContext [SecurityContext](api-reference.md#securitycontext)                                                       | SecurityContext holds security configuration that will be applied to a container.                                                                                                                   |           |                                 |
| podMetadata [Metadata](api-reference.md#metadata)                                                                         | PodMetadata defines extra metadata for the Pod.                                                                                                                                                     |           |                                 |
| imagePullSecrets [LocalObjectReference](api-reference.md#localobjectreference) array                                      | ImagePullSecrets is the list of pull Secrets to be used to pull the image.                                                                                                                          |           |                                 |
| podSecurityContext [PodSecurityContext](api-reference.md#podsecuritycontext)                                              | SecurityContext holds pod-level security attributes and common container settings.                                                                                                                  |           |                                 |
| serviceAccountName string                                                                                                 | ServiceAccountName is the name of the ServiceAccount to be used by the Pods.                                                                                                                        |           |                                 |
| affinity [AffinityConfig](api-reference.md#affinityconfig)                                                                | Affinity to be used in the Pod.                                                                                                                                                                     |           |                                 |
| nodeSelector object (keys:string, values:string)                                                                          | NodeSelector to be used in the Pod.                                                                                                                                                                 |           |                                 |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array   | Tolerations to be used in the Pod.                                                                                                                                                                  |           |                                 |
| priorityClassName string                                                                                                  | PriorityClassName to be used in the Pod.                                                                                                                                                            |           |                                 |
| successfulJobsHistoryLimit integer                                                                                        | SuccessfulJobsHistoryLimit defines the maximum number of successful Jobs to be displayed.                                                                                                           |           | Minimum: 0                      |
| failedJobsHistoryLimit integer                                                                                            | FailedJobsHistoryLimit defines the maximum number of failed Jobs to be displayed.                                                                                                                   |           | Minimum: 0                      |
| timeZone string                                                                                                           | TimeZone defines the timezone associated with the cron expression.                                                                                                                                  |           |                                 |
| mariaDbRef [MariaDBRef](api-reference.md#mariadbref)                                                                      | MariaDBRef is a reference to a MariaDB object.                                                                                                                                                      |           | Required: {}                    |
| schedule [Schedule](api-reference.md#schedule)                                                                            | Schedule defines when the SqlJob will be executed.                                                                                                                                                  |           |                                 |
| username string                                                                                                           | Username to be impersonated when executing the SqlJob.                                                                                                                                              |           | Required: {}                    |
| passwordSecretKeyRef [SecretKeySelector](api-reference.md#secretkeyselector)                                              | UserPasswordSecretKeyRef is a reference to the impersonated user's password to be used when executing the SqlJob.                                                                                   |           | Required: {}                    |
| tlsCASecretRef [LocalObjectReference](api-reference.md#localobjectreference)                                              | TLSCACertSecretRef is a reference toa CA Secret used to establish trust when executing the SqlJob.If not provided, the CA bundle provided by the referred MariaDB is used.                          |           |                                 |
| tlsClientCertSecretRef [LocalObjectReference](api-reference.md#localobjectreference)                                      | TLSClientCertSecretRef is a reference to a Kubernetes TLS Secret used as authentication when executing the SqlJob.If not provided, the client certificate provided by the referred MariaDB is used. |           |                                 |
| database string                                                                                                           | Username to be used when executing the SqlJob.                                                                                                                                                      |           |                                 |
| dependsOn [LocalObjectReference](api-reference.md#localobjectreference) array                                             | DependsOn defines dependencies with other SqlJob objectecs.                                                                                                                                         |           |                                 |
| sql string                                                                                                                | Sql is the script to be executed by the SqlJob.                                                                                                                                                     |           |                                 |
| sqlConfigMapKeyRef [ConfigMapKeySelector](api-reference.md#configmapkeyselector)                                          | SqlConfigMapKeyRef is a reference to a ConfigMap containing the Sql script.It is defaulted to a ConfigMap with the contents of the Sql field.                                                       |           |                                 |
| backoffLimit integer                                                                                                      | BackoffLimit defines the maximum number of attempts to successfully execute a SqlJob.                                                                                                               | 5         |                                 |
| restartPolicy [RestartPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#restartpolicy-v1-core) | RestartPolicy to be added to the SqlJob Pod.                                                                                                                                                        | OnFailure | Enum: \[Always OnFailure Never] |
| inheritMetadata [Metadata](api-reference.md#metadata)                                                                     | InheritMetadata defines the metadata to be inherited by children resources.                                                                                                                         |           |                                 |

#### Storage

Storage defines the storage options to be used for provisioning the PVCs mounted by MariaDB.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                                                                       | Description                                                                                                                                                                                                                         | Default | Validation |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                       | Description                                                                                                                                                                                                                         | Default | Validation |
| ephemeral boolean                                                                                           | Ephemeral indicates whether to use ephemeral storage in the PVCs. It is only compatible with non HA MariaDBs.                                                                                                                       |         |            |
| size [Quantity](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#quantity-resource-api) | Size of the PVCs to be mounted by MariaDB. Required if not provided in 'VolumeClaimTemplate'. It supersedes the storage size specified in 'VolumeClaimTemplate'.                                                                    |         |            |
| storageClassName string                                                                                     | StorageClassName to be used to provision the PVCS. It supersedes the 'StorageClassName' specified in 'VolumeClaimTemplate'.If not provided, the default 'StorageClass' configured in the cluster is used.                           |         |            |
| resizeInUseVolumes boolean                                                                                  | ResizeInUseVolumes indicates whether the PVCs can be resized. The 'StorageClassName' used should have 'allowVolumeExpansion' set to 'true' to allow resizing.It defaults to true.                                                   |         |            |
| waitForVolumeResize boolean                                                                                 | WaitForVolumeResize indicates whether to wait for the PVCs to be resized before marking the MariaDB object as ready. This will block other operations such as cluster recovery while the resize is in progress.It defaults to true. |         |            |
| volumeClaimTemplate [VolumeClaimTemplate](api-reference.md#volumeclaimtemplate)                             | VolumeClaimTemplate provides a template to define the PVCs.                                                                                                                                                                         |         |            |

#### StorageVolumeSource

Refer to the Kubernetes docs: [#volume-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#volume-v1-core).

_Appears in:_

* [BackupStagingStorage](api-reference.md#backupstagingstorage)
* [BackupStorage](api-reference.md#backupstorage)
* [BootstrapFrom](api-reference.md#bootstrapfrom)
* [RestoreSource](api-reference.md#restoresource)
* [RestoreSpec](api-reference.md#restorespec)
* [Volume](api-reference.md#volume)
* [VolumeSource](api-reference.md#volumesource)

| Field                                                                                                         | Description | Default | Validation |
| ------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                                                                         | Description | Default | Validation |
| emptyDir [EmptyDirVolumeSource](api-reference.md#emptydirvolumesource)                                        |             |         |            |
| nfs [NFSVolumeSource](api-reference.md#nfsvolumesource)                                                       |             |         |            |
| csi [CSIVolumeSource](api-reference.md#csivolumesource)                                                       |             |         |            |
| hostPath [HostPathVolumeSource](api-reference.md#hostpathvolumesource)                                        |             |         |            |
| persistentVolumeClaim [PersistentVolumeClaimVolumeSource](api-reference.md#persistentvolumeclaimvolumesource) |             |         |            |

#### SuspendTemplate

SuspendTemplate indicates whether the current resource should be suspended or not.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleListener](api-reference.md#maxscalelistener)
* [MaxScaleMonitor](api-reference.md#maxscalemonitor)
* [MaxScaleService](api-reference.md#maxscaleservice)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field           | Description                                                                                                                                                                                                                              | Default | Validation |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field           | Description                                                                                                                                                                                                                              | Default | Validation |
| suspend boolean | Suspend indicates whether the current resource should be suspended or not.This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities. | false   |            |

#### TCPSocketAction

Refer to the Kubernetes docs: [#tcpsocketaction-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#tcpsocketaction-v1-core).

_Appears in:_

* [Probe](api-reference.md#probe)
* [ProbeHandler](api-reference.md#probehandler)

| Field                                                                                                            | Description | Default | Validation |
| ---------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                                                                            | Description | Default | Validation |
| port [IntOrString](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#intorstring-intstr-util) |             |         |            |
| host string                                                                                                      |             |         |            |

#### TLS

TLS defines the PKI to be used with MariaDB.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Default | Validation                                             |
| --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------ |
| Field                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Default | Validation                                             |
| enabled boolean                                                                   | Enabled indicates whether TLS is enabled, determining if certificates should be issued and mounted to the MariaDB instance.It is enabled by default.                                                                                                                                                                                                                                                                                                                                                                                                     |         |                                                        |
| required boolean                                                                  | Required specifies whether TLS must be enforced for all connections.User TLS requirements take precedence over this.It disabled by default.                                                                                                                                                                                                                                                                                                                                                                                                              |         |                                                        |
| versions string array                                                             | Versions specifies the supported TLS versions for this MariaDB instance.By default, the MariaDB's default supported versions are used. See: [ssltls-system-variables.md#tls\_version](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#tls_version).                                                                                                                                                                                                                                    |         |                                                        |
| serverCASecretRef [LocalObjectReference](api-reference.md#localobjectreference)   | ServerCASecretRef is a reference to a Secret containing the server certificate authority keypair. It is used to establish trust and issue server certificates.One of:- Secret containing both the 'ca.crt' and 'ca.key' keys. This allows you to bring your own CA to Kubernetes to issue certificates.- Secret containing only the 'ca.crt' in order to establish trust. In this case, either serverCertSecretRef or serverCertIssuerRef must be provided.If not provided, a self-signed CA will be provisioned to issue the server certificate.        |         |                                                        |
| serverCertSecretRef [LocalObjectReference](api-reference.md#localobjectreference) | ServerCertSecretRef is a reference to a TLS Secret containing the server certificate.It is mutually exclusive with serverCertIssuerRef.                                                                                                                                                                                                                                                                                                                                                                                                                  |         |                                                        |
| serverCertIssuerRef [ObjectReference](api-reference.md#objectreference)           | ServerCertIssuerRef is a reference to a cert-manager issuer object used to issue the server certificate. cert-manager must be installed previously in the cluster.It is mutually exclusive with serverCertSecretRef.By default, the Secret field 'ca.crt' provisioned by cert-manager will be added to the trust chain. A custom trust bundle may be specified via serverCASecretRef.                                                                                                                                                                    |         |                                                        |
| serverCertConfig [TLSConfig](api-reference.md#tlsconfig)                          | ServerCertConfig allows configuring the server certificates, either issued by the operator or cert-manager.If not set, the default settings will be used.                                                                                                                                                                                                                                                                                                                                                                                                |         |                                                        |
| clientCASecretRef [LocalObjectReference](api-reference.md#localobjectreference)   | ClientCASecretRef is a reference to a Secret containing the client certificate authority keypair. It is used to establish trust and issue client certificates.One of:- Secret containing both the 'ca.crt' and 'ca.key' keys. This allows you to bring your own CA to Kubernetes to issue certificates.- Secret containing only the 'ca.crt' in order to establish trust. In this case, either clientCertSecretRef or clientCertIssuerRef fields must be provided.If not provided, a self-signed CA will be provisioned to issue the client certificate. |         |                                                        |
| clientCertSecretRef [LocalObjectReference](api-reference.md#localobjectreference) | ClientCertSecretRef is a reference to a TLS Secret containing the client certificate.It is mutually exclusive with clientCertIssuerRef.                                                                                                                                                                                                                                                                                                                                                                                                                  |         |                                                        |
| clientCertIssuerRef [ObjectReference](api-reference.md#objectreference)           | ClientCertIssuerRef is a reference to a cert-manager issuer object used to issue the client certificate. cert-manager must be installed previously in the cluster.It is mutually exclusive with clientCertSecretRef.By default, the Secret field 'ca.crt' provisioned by cert-manager will be added to the trust chain. A custom trust bundle may be specified via clientCASecretRef.                                                                                                                                                                    |         |                                                        |
| clientCertConfig [TLSConfig](api-reference.md#tlsconfig)                          | ClientCertConfig allows configuring the client certificates, either issued by the operator or cert-manager.If not set, the default settings will be used.                                                                                                                                                                                                                                                                                                                                                                                                |         |                                                        |
| galeraSSTEnabled boolean                                                          | GaleraSSTEnabled determines whether Galera SST connections should use TLS.It disabled by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |         |                                                        |
| galeraServerSSLMode string                                                        | GaleraServerSSLMode defines the server SSL mode for a Galera Enterprise cluster.This field is only supported and applicable for Galera Enterprise >= 10.6 instances.Refer to the MariaDB Enterprise docs for more detail: [#WSREP\_TLS\_Modes](https://mariadb.com/docs/server/security/galera/#WSREP_TLS_Modes)                                                                                                                                                                                                                                         |         | Enum: \[PROVIDER SERVER SERVER\_X509]                  |
| galeraClientSSLMode string                                                        | GaleraClientSSLMode defines the client SSL mode for a Galera Enterprise cluster.This field is only supported and applicable for Galera Enterprise >= 10.6 instances.Refer to the MariaDB Enterprise docs for more detail: [#SST\_TLS\_Modes](https://mariadb.com/docs/server/security/galera/#SST_TLS_Modes)                                                                                                                                                                                                                                             |         | Enum: \[DISABLED REQUIRED VERIFY\_CA VERIFY\_IDENTITY] |

#### TLSConfig

TLSConfig defines parameters to configure a certificate.

_Appears in:_

* [MaxScaleTLS](api-reference.md#maxscaletls)
* [TLS](api-reference.md#tls)

| Field                                                                                                          | Description                                                                                                                                               | Default | Validation         |
| -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------ |
| Field                                                                                                          | Description                                                                                                                                               | Default | Validation         |
| caLifetime [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)   | CALifetime defines the CA certificate validity.                                                                                                           |         |                    |
| certLifetime [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | CertLifetime defines the certificate validity.                                                                                                            |         |                    |
| privateKeyAlgorithm string                                                                                     | PrivateKeyAlgorithm is the algorithm to be used for the CA and leaf certificate private keys.One of: ECDSA or RSA                                         |         | Enum: \[ECDSA RSA] |
| privateKeySize integer                                                                                         | PrivateKeyAlgorithm is the key size to be used for the CA and leaf certificate private keys.Supported values: ECDSA(256, 384, 521), RSA(2048, 3072, 4096) |         |                    |

#### TLSRequirements

TLSRequirements specifies TLS requirements for the user to connect. See: [securing-connections-for-client-and-server.md#requiring-tls](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/securing-connections-for-client-and-server.md#requiring-tls).

_Appears in:_

* [UserSpec](api-reference.md#userspec)

| Field          | Description                                                                                         | Default | Validation |
| -------------- | --------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field          | Description                                                                                         | Default | Validation |
| ssl boolean    | SSL indicates that the user must connect via TLS.                                                   |         |            |
| x509 boolean   | X509 indicates that the user must provide a valid x509 certificate to connect.                      |         |            |
| issuer string  | Issuer indicates that the TLS certificate provided by the user must be issued by a specific issuer. |         |            |
| subject string | Subject indicates that the TLS certificate provided by the user must have a specific subject.       |         |            |

#### TLSS3

_Appears in:_

* [S3](api-reference.md#s3)

| Field                                                                  | Description                                                                                                                                                                                                                             | Default | Validation |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Field                                                                  | Description                                                                                                                                                                                                                             | Default | Validation |
| enabled boolean                                                        | Enabled is a flag to enable TLS.                                                                                                                                                                                                        |         |            |
| caSecretKeyRef [SecretKeySelector](api-reference.md#secretkeyselector) | CASecretKeyRef is a reference to a Secret key containing a CA bundle in PEM format used to establish TLS connections with S3.By default, the system trust chain will be used, but you can use this field to add more CAs to the bundle. |         |            |

#### TopologySpreadConstraint

Refer to the Kubernetes docs: [#topologyspreadconstraint-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#topologyspreadconstraint-v1-core).

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScalePodTemplate](api-reference.md#maxscalepodtemplate)
* [MaxScaleSpec](api-reference.md#maxscalespec)
* [PodTemplate](api-reference.md#podtemplate)

| Field                                                                                                                                                         | Description | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                                                                                                                         | Description | Default | Validation |
| maxSkew integer                                                                                                                                               |             |         |            |
| topologyKey string                                                                                                                                            |             |         |            |
| whenUnsatisfiable [UnsatisfiableConstraintAction](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#unsatisfiableconstraintaction-v1-core) |             |         |            |
| labelSelector [LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#labelselector-v1-meta)                                     |             |         |            |
| minDomains integer                                                                                                                                            |             |         |            |
| nodeAffinityPolicy [NodeInclusionPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#nodeinclusionpolicy-v1-core)                    |             |         |            |
| nodeTaintsPolicy [NodeInclusionPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#nodeinclusionpolicy-v1-core)                      |             |         |            |
| matchLabelKeys string array                                                                                                                                   |             |         |            |

#### UpdateStrategy

UpdateStrategy defines how a MariaDB resource is updated.

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)

| Field                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                            | Default                  | Validation                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | -------------------------------------------------------------- |
| Field                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                            | Default                  | Validation                                                     |
| type [UpdateType](api-reference.md#updatetype)                                                                                                                  | Type defines the type of updates. One of ReplicasFirstPrimaryLast, RollingUpdate or OnDelete. If not defined, it defaults to ReplicasFirstPrimaryLast.                                                                                                                                                                                                                                 | ReplicasFirstPrimaryLast | Enum: \[ReplicasFirstPrimaryLast RollingUpdate OnDelete Never] |
| rollingUpdate [RollingUpdateStatefulSetStrategy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#rollingupdatestatefulsetstrategy-v1-apps) | RollingUpdate defines parameters for the RollingUpdate type.                                                                                                                                                                                                                                                                                                                           |                          |                                                                |
| autoUpdateDataPlane boolean                                                                                                                                     | AutoUpdateDataPlane indicates whether the Galera data-plane version (agent and init containers) should be automatically updated based on the operator version. It defaults to false.Updating the operator will trigger updates on all the MariaDB instances that have this flag set to true. Thus, it is recommended to progressively set this flag after having updated the operator. |                          |                                                                |

#### UpdateType

_Underlying type:_ _string_

UpdateType defines the type of update for a MariaDB resource.

_Appears in:_

* [UpdateStrategy](api-reference.md#updatestrategy)

| Field                    | Description                                                                                                                                                                                                                                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Field                    | Description                                                                                                                                                                                                                                                                                          |
| ReplicasFirstPrimaryLast | ReplicasFirstPrimaryLastUpdateType indicates that the update will be applied to all replica Pods first and later on to the primary Pod.The updates are applied one by one waiting until each Pod passes the readiness probei.e. the Pod gets synced and it is ready to receive traffic.              |
| RollingUpdate            | RollingUpdateUpdateType indicates that the update will be applied by the StatefulSet controller using the RollingUpdate strategy.This strategy is unaware of the roles that the Pod have (primary or replica) and it willperform the update following the StatefulSet ordinal, from higher to lower. |
| OnDelete                 | OnDeleteUpdateType indicates that the update will be applied by the StatefulSet controller using the OnDelete strategy.The update will be done when the Pods get manually deleted by the user.                                                                                                       |
| Never                    | NeverUpdateType indicates that the StatefulSet will never be updated.This can be used to roll out updates progressively to a fleet of instances.                                                                                                                                                     |

#### User

User is the Schema for the users API. It is used to define grants as if you were running a 'CREATE USER' statement.

| Field                                                                                                          | Description                                                   | Default | Validation |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                          | Description                                                   | Default | Validation |
| apiVersion string                                                                                              | enterprise.mariadb.com/v1alpha1                               |         |            |
| kind string                                                                                                    | User                                                          |         |            |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |         |            |
| spec [UserSpec](api-reference.md#userspec)                                                                     |                                                               |         |            |

#### UserSpec

UserSpec defines the desired state of User

_Appears in:_

* [User](api-reference.md#user)

| Field                                                                                                             | Description                                                                                                                                                                                                                                                                                                      | Default | Validation           |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------- |
| Field                                                                                                             | Description                                                                                                                                                                                                                                                                                                      | Default | Validation           |
| requeueInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | RequeueInterval is used to perform requeue reconciliations.                                                                                                                                                                                                                                                      |         |                      |
| retryInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta)   | RetryInterval is the interval used to perform retries.                                                                                                                                                                                                                                                           |         |                      |
| cleanupPolicy [CleanupPolicy](api-reference.md#cleanuppolicy)                                                     | CleanupPolicy defines the behavior for cleaning up a SQL resource.                                                                                                                                                                                                                                               |         | Enum: \[Skip Delete] |
| mariaDbRef [MariaDBRef](api-reference.md#mariadbref)                                                              | MariaDBRef is a reference to a MariaDB object.                                                                                                                                                                                                                                                                   |         | Required: {}         |
| passwordSecretKeyRef [SecretKeySelector](api-reference.md#secretkeyselector)                                      | PasswordSecretKeyRef is a reference to the password to be used by the User.If not provided, the account will be locked and the password will expire.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password.               |         |                      |
| passwordHashSecretKeyRef [SecretKeySelector](api-reference.md#secretkeyselector)                                  | PasswordHashSecretKeyRef is a reference to the password hash to be used by the User.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password hash.It requires the 'skip-strict-password-validation' option to be set. See:. |         |                      |
| passwordPlugin [PasswordPlugin](api-reference.md#passwordplugin)                                                  | PasswordPlugin is a reference to the password plugin and arguments to be used by the User.It requires the 'skip-strict-password-validation' option to be set. See:.                                                                                                                                              |         |                      |
| require [TLSRequirements](api-reference.md#tlsrequirements)                                                       | Require specifies TLS requirements for the user to connect. See: [securing-connections-for-client-and-server.md#requiring-tls](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/securing-connections-for-client-and-server.md#requiring-tls).                              |         |                      |
| maxUserConnections integer                                                                                        | MaxUserConnections defines the maximum number of simultaneous connections that the User can establish.                                                                                                                                                                                                           | 10      |                      |
| name string                                                                                                       | Name overrides the default name provided by metadata.name.                                                                                                                                                                                                                                                       |         | MaxLength: 80        |
| host string                                                                                                       | Host related to the User.                                                                                                                                                                                                                                                                                        |         | MaxLength: 255       |

#### Volume

Refer to the Kubernetes docs: [#volume-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#volume-v1-core).

_Appears in:_

* [MariaDBSpec](api-reference.md#mariadbspec)
* [PodTemplate](api-reference.md#podtemplate)

| Field                                                                                                         | Description | Default | Validation |
| ------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                                                                         | Description | Default | Validation |
| name string                                                                                                   |             |         |            |
| emptyDir [EmptyDirVolumeSource](api-reference.md#emptydirvolumesource)                                        |             |         |            |
| nfs [NFSVolumeSource](api-reference.md#nfsvolumesource)                                                       |             |         |            |
| csi [CSIVolumeSource](api-reference.md#csivolumesource)                                                       |             |         |            |
| hostPath [HostPathVolumeSource](api-reference.md#hostpathvolumesource)                                        |             |         |            |
| persistentVolumeClaim [PersistentVolumeClaimVolumeSource](api-reference.md#persistentvolumeclaimvolumesource) |             |         |            |
| secret [SecretVolumeSource](api-reference.md#secretvolumesource)                                              |             |         |            |
| configMap [ConfigMapVolumeSource](api-reference.md#configmapvolumesource)                                     |             |         |            |

#### VolumeClaimTemplate

VolumeClaimTemplate defines a template to customize PVC objects.

_Appears in:_

* [GaleraConfig](api-reference.md#galeraconfig)
* [MaxScaleConfig](api-reference.md#maxscaleconfig)
* [Storage](api-reference.md#storage)

| Field                                                                                                                                                   | Description                                                   | Default | Validation |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------- | ---------- |
| Field                                                                                                                                                   | Description                                                   | Default | Validation |
| accessModes [PersistentVolumeAccessMode](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#persistentvolumeaccessmode-v1-core) array |                                                               |         |            |
| selector [LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#labelselector-v1-meta)                                    |                                                               |         |            |
| resources [VolumeResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#volumeresourcerequirements-v1-core)         |                                                               |         |            |
| storageClassName string                                                                                                                                 |                                                               |         |            |
| metadata [Metadata](api-reference.md#metadata)                                                                                                          | Refer to Kubernetes API documentation for fields of metadata. |         |            |

#### VolumeMount

Refer to the Kubernetes docs: [#volumemount-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#volumemount-v1-core).

_Appears in:_

* [Container](api-reference.md#container)
* [ContainerTemplate](api-reference.md#containertemplate)
* [GaleraAgent](api-reference.md#galeraagent)
* [GaleraInit](api-reference.md#galerainit)
* [MariaDBSpec](api-reference.md#mariadbspec)
* [MaxScaleSpec](api-reference.md#maxscalespec)

| Field            | Description                           | Default | Validation |
| ---------------- | ------------------------------------- | ------- | ---------- |
| Field            | Description                           | Default | Validation |
| name string      | This must match the Name of a Volume. |         |            |
| readOnly boolean |                                       |         |            |
| mountPath string |                                       |         |            |
| subPath string   |                                       |         |            |

#### VolumeSource

Refer to the Kubernetes docs: [#volume-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#volume-v1-core).

_Appears in:_

* [Volume](api-reference.md#volume)

| Field                                                                                                         | Description | Default | Validation |
| ------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                                                                         | Description | Default | Validation |
| emptyDir [EmptyDirVolumeSource](api-reference.md#emptydirvolumesource)                                        |             |         |            |
| nfs [NFSVolumeSource](api-reference.md#nfsvolumesource)                                                       |             |         |            |
| csi [CSIVolumeSource](api-reference.md#csivolumesource)                                                       |             |         |            |
| hostPath [HostPathVolumeSource](api-reference.md#hostpathvolumesource)                                        |             |         |            |
| persistentVolumeClaim [PersistentVolumeClaimVolumeSource](api-reference.md#persistentvolumeclaimvolumesource) |             |         |            |
| secret [SecretVolumeSource](api-reference.md#secretvolumesource)                                              |             |         |            |
| configMap [ConfigMapVolumeSource](api-reference.md#configmapvolumesource)                                     |             |         |            |

#### WeightedPodAffinityTerm

Refer to the Kubernetes docs: [#weightedpodaffinityterm-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#weightedpodaffinityterm-v1-core).

_Appears in:_

* [PodAntiAffinity](api-reference.md#podantiaffinity)

| Field                                                               | Description | Default | Validation |
| ------------------------------------------------------------------- | ----------- | ------- | ---------- |
| Field                                                               | Description | Default | Validation |
| weight integer                                                      |             |         |            |
| podAffinityTerm [PodAffinityTerm](api-reference.md#podaffinityterm) |             |         |            |
