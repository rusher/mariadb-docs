
# API Reference

## Packages


* [enterprise.mariadb.com/v1alpha1](#enterprisemariadbcomv1alpha1)


## enterprise.mariadb.com/v1alpha1


Package v1alpha1 contains API Schema definitions for the v1alpha1 API group


### Resource Types


* [Backup](#backup)
* [Connection](#connection)
* [Database](#database)
* [Grant](#grant)
* [MariaDB](#mariadb)
* [MaxScale](#maxscale)
* [Restore](#restore)
* [SqlJob](#sqljob)
* [User](#user)


#### Affinity


Refer to the Kubernetes docs: [#affinity-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#affinity-v1-core).


*Appears in:*
- [AffinityConfig](#affinityconfig)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| podAntiAffinity [PodAntiAffinity](#podantiaffinity) |  |  |  |
| nodeAffinity [NodeAffinity](#nodeaffinity) |  |  |  |


#### AffinityConfig


AffinityConfig defines policies to schedule Pods in Nodes.


*Appears in:*
- [BackupSpec](#backupspec)
- [Exporter](#exporter)
- [Job](#job)
- [JobPodTemplate](#jobpodtemplate)
- [MariaDBSpec](#mariadbspec)
- [MaxScalePodTemplate](#maxscalepodtemplate)
- [MaxScaleSpec](#maxscalespec)
- [PodTemplate](#podtemplate)
- [RestoreSpec](#restorespec)
- [SqlJobSpec](#sqljobspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| podAntiAffinity [PodAntiAffinity](#podantiaffinity) |  |  |  |
| nodeAffinity [NodeAffinity](#nodeaffinity) |  |  |  |
| antiAffinityEnabled boolean | AntiAffinityEnabled configures PodAntiAffinity so each Pod is scheduled in a different Node, enabling HA.Make sure you have at least as many Nodes available as the replicas to not end up with unscheduled Pods. |  |  |


#### Backup


Backup is the Schema for the backups API. It is used to define backup jobs and its storage.


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| apiVersion string | enterprise.mariadb.com/v1alpha1 |  |  |
| kind string | Backup |  |  |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |  |  |
| spec [BackupSpec](#backupspec) |  |  |  |


#### BackupSpec


BackupSpec defines the desired state of Backup


*Appears in:*
- [Backup](#backup)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| args string array | Args to be used in the Container. |  |  |
| resources [ResourceRequirements](#resourcerequirements) | Resouces describes the compute resource requirements. |  |  |
| securityContext [SecurityContext](#securitycontext) | SecurityContext holds security configuration that will be applied to a container. |  |  |
| podMetadata [Metadata](#metadata) | PodMetadata defines extra metadata for the Pod. |  |  |
| imagePullSecrets [LocalObjectReference](#localobjectreference) array | ImagePullSecrets is the list of pull Secrets to be used to pull the image. |  |  |
| podSecurityContext [PodSecurityContext](#podsecuritycontext) | SecurityContext holds pod-level security attributes and common container settings. |  |  |
| serviceAccountName string | ServiceAccountName is the name of the ServiceAccount to be used by the Pods. |  |  |
| affinity [AffinityConfig](#affinityconfig) | Affinity to be used in the Pod. |  |  |
| nodeSelector object (keys:string, values:string) | NodeSelector to be used in the Pod. |  |  |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array | Tolerations to be used in the Pod. |  |  |
| priorityClassName string | PriorityClassName to be used in the Pod. |  |  |
| successfulJobsHistoryLimit integer | SuccessfulJobsHistoryLimit defines the maximum number of successful Jobs to be displayed. |  | Minimum: 0 |
| failedJobsHistoryLimit integer | FailedJobsHistoryLimit defines the maximum number of failed Jobs to be displayed. |  | Minimum: 0 |
| timeZone string | TimeZone defines the timezone associated with the cron expression. |  |  |
| mariaDbRef [MariaDBRef](#mariadbref) | MariaDBRef is a reference to a MariaDB object. |  | Required: {} |
| compression [CompressAlgorithm](#compressalgorithm) | Compression algorithm to be used in the Backup. |  | Enum: [none bzip2 gzip] |
| stagingStorage [BackupStagingStorage](#backupstagingstorage) | StagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.It defaults to an emptyDir volume, meaning that the backups will be temporarily stored in the node where the Backup Job is scheduled.The staging area gets cleaned up after each backup is completed, consider this for sizing it appropriately. |  |  |
| storage [BackupStorage](#backupstorage) | Storage defines the final storage for backups. |  | Required: {} |
| schedule [Schedule](#schedule) | Schedule defines when the Backup will be taken. |  |  |
| maxRetention [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | MaxRetention defines the retention policy for backups. Old backups will be cleaned up by the Backup Job.It defaults to 30 days. |  |  |
| databases string array | Databases defines the logical databases to be backed up. If not provided, all databases are backed up. |  |  |
| ignoreGlobalPriv boolean | IgnoreGlobalPriv indicates to ignore the mysql.global_priv in backups.If not provided, it will default to true when the referred MariaDB instance has Galera enabled and otherwise to false. |  |  |
| logLevel string | LogLevel to be used n the Backup Job. It defaults to 'info'. | info |  |
| backoffLimit integer | BackoffLimit defines the maximum number of attempts to successfully take a Backup. |  |  |
| restartPolicy [RestartPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#restartpolicy-v1-core) | RestartPolicy to be added to the Backup Pod. | OnFailure | Enum: [Always OnFailure Never] |
| inheritMetadata [Metadata](#metadata) | InheritMetadata defines the metadata to be inherited by children resources. |  |  |


#### BackupStagingStorage


BackupStagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.


*Appears in:*
- [BackupSpec](#backupspec)
- [BootstrapFrom](#bootstrapfrom)
- [RestoreSource](#restoresource)
- [RestoreSpec](#restorespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| persistentVolumeClaim [PersistentVolumeClaimSpec](#persistentvolumeclaimspec) | PersistentVolumeClaim is a Kubernetes PVC specification. |  |  |
| volume [StorageVolumeSource](#storagevolumesource) | Volume is a Kubernetes volume specification. |  |  |


#### BackupStorage


BackupStorage defines the final storage for backups.


*Appears in:*
- [BackupSpec](#backupspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| s3 [S3](#s3) | S3 defines the configuration to store backups in a S3 compatible storage. |  |  |
| persistentVolumeClaim [PersistentVolumeClaimSpec](#persistentvolumeclaimspec) | PersistentVolumeClaim is a Kubernetes PVC specification. |  |  |
| volume [StorageVolumeSource](#storagevolumesource) | Volume is a Kubernetes volume specification. |  |  |


#### BasicAuth


KubernetesAuth refers to the basic authentication mechanism utilized for establishing a connection from the operator to the agent.


*Appears in:*
- [GaleraAgent](#galeraagent)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| enabled boolean | Enabled is a flag to enable BasicAuth |  |  |
| username string | Username to be used for basic authentication |  |  |
| passwordSecretKeyRef [GeneratedSecretKeyRef](#generatedsecretkeyref) | PasswordSecretKeyRef to be used for basic authentication |  |  |


#### BootstrapFrom


BootstrapFrom defines a source to bootstrap MariaDB from.


*Appears in:*
- [MariaDBSpec](#mariadbspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| backupRef [LocalObjectReference](#localobjectreference) | BackupRef is a reference to a Backup object. It has priority over S3 and Volume. |  |  |
| s3 [S3](#s3) | S3 defines the configuration to restore backups from a S3 compatible storage. It has priority over Volume. |  |  |
| volume [StorageVolumeSource](#storagevolumesource) | Volume is a Kubernetes Volume object that contains a backup. |  |  |
| targetRecoveryTime [Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#time-v1-meta) | TargetRecoveryTime is a RFC3339 (1970-01-01T00:00:00Z) date and time that defines the point in time recovery objective.It is used to determine the closest restoration source in time. |  |  |
| stagingStorage [BackupStagingStorage](#backupstagingstorage) | StagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.It defaults to an emptyDir volume, meaning that the backups will be temporarily stored in the node where the Restore Job is scheduled. |  |  |
| restoreJob [Job](#job) | RestoreJob defines additional properties for the Job used to perform the Restore. |  |  |


#### CSIVolumeSource


Refer to the Kubernetes docs: [#csivolumesource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#csivolumesource-v1-core).


*Appears in:*
- [StorageVolumeSource](#storagevolumesource)
- [Volume](#volume)
- [VolumeSource](#volumesource)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| driver string |  |  |  |
| readOnly boolean |  |  |  |
| fsType string |  |  |  |
| volumeAttributes object (keys:string, values:string) |  |  |  |
| nodePublishSecretRef [LocalObjectReference](#localobjectreference) |  |  |  |


#### CleanupPolicy


*Underlying type:* *string*


CleanupPolicy defines the behavior for cleaning up a resource.


*Appears in:*
- [DatabaseSpec](#databasespec)
- [GrantSpec](#grantspec)
- [SQLTemplate](#sqltemplate)
- [UserSpec](#userspec)


| Field | Description |
| --- | --- |
| Field | Description |
| Skip | CleanupPolicySkip indicates that the resource will NOT be deleted from the database after the CR is deleted. |
| Delete | CleanupPolicyDelete indicates that the resource will be deleted from the database after the CR is deleted. |


#### CompressAlgorithm


*Underlying type:* *string*


CompressAlgorithm defines the compression algorithm for a Backup resource.


*Appears in:*
- [BackupSpec](#backupspec)


| Field | Description |
| --- | --- |
| Field | Description |
| none | No compression |
| bzip2 | Bzip2 compression. Good compression ratio, but slower compression/decompression speed compared to gzip. |
| gzip | Gzip compression. Good compression/decompression speed, but worse compression ratio compared to bzip2. |


#### ConfigMapKeySelector


Refer to the Kubernetes docs: [#configmapkeyselector-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#configmapkeyselector-v1-core).


*Appears in:*
- [EnvVarSource](#envvarsource)
- [MariaDBSpec](#mariadbspec)
- [SqlJobSpec](#sqljobspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| name string |  |  |  |
| key string |  |  |  |


#### ConfigMapVolumeSource


Refer to the Kubernetes docs: [#configmapvolumesource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#configmapvolumesource-v1-core).


*Appears in:*
- [Volume](#volume)
- [VolumeSource](#volumesource)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| name string |  |  |  |
| defaultMode integer |  |  |  |


#### Connection


Connection is the Schema for the connections API. It is used to configure connection strings for the applications connecting to MariaDB.


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| apiVersion string | enterprise.mariadb.com/v1alpha1 |  |  |
| kind string | Connection |  |  |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |  |  |
| spec [ConnectionSpec](#connectionspec) |  |  |  |


#### ConnectionSpec


ConnectionSpec defines the desired state of Connection


*Appears in:*
- [Connection](#connection)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| secretName string | SecretName to be used in the Connection. |  |  |
| secretTemplate [SecretTemplate](#secrettemplate) | SecretTemplate to be used in the Connection. |  |  |
| healthCheck [HealthCheck](#healthcheck) | HealthCheck to be used in the Connection. |  |  |
| params object (keys:string, values:string) | Params to be used in the Connection. |  |  |
| serviceName string | ServiceName to be used in the Connection. |  |  |
| port integer | Port to connect to. If not provided, it defaults to the MariaDB port or to the first MaxScale listener. |  |  |
| mariaDbRef [MariaDBRef](#mariadbref) | MariaDBRef is a reference to the MariaDB to connect to. Either MariaDBRef or MaxScaleRef must be provided. |  |  |
| maxScaleRef [ObjectReference](#objectreference) | MaxScaleRef is a reference to the MaxScale to connect to. Either MariaDBRef or MaxScaleRef must be provided. |  |  |
| username string | Username to use for configuring the Connection. |  | Required: {} |
| passwordSecretKeyRef [SecretKeySelector](#secretkeyselector) | PasswordSecretKeyRef is a reference to the password to use for configuring the Connection.Either passwordSecretKeyRef or tlsClientCertSecretRef must be provided as client credentials.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password. |  |  |
| tlsClientCertSecretRef [LocalObjectReference](#localobjectreference) | TLSClientCertSecretRef is a reference to a Kubernetes TLS Secret used as authentication when checking the connection health.Either passwordSecretKeyRef or tlsClientCertSecretRef must be provided as client credentials.If not provided, the client certificate provided by the referred MariaDB is used if TLS is enabled.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the client certificate. |  |  |
| host string | Host to connect to. If not provided, it defaults to the MariaDB host or to the MaxScale host. |  |  |
| database string | Database to use when configuring the Connection. |  |  |


#### ConnectionTemplate


ConnectionTemplate defines a template to customize Connection objects.


*Appears in:*
- [ConnectionSpec](#connectionspec)
- [MariaDBMaxScaleSpec](#mariadbmaxscalespec)
- [MariaDBSpec](#mariadbspec)
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| secretName string | SecretName to be used in the Connection. |  |  |
| secretTemplate [SecretTemplate](#secrettemplate) | SecretTemplate to be used in the Connection. |  |  |
| healthCheck [HealthCheck](#healthcheck) | HealthCheck to be used in the Connection. |  |  |
| params object (keys:string, values:string) | Params to be used in the Connection. |  |  |
| serviceName string | ServiceName to be used in the Connection. |  |  |
| port integer | Port to connect to. If not provided, it defaults to the MariaDB port or to the first MaxScale listener. |  |  |


#### Container


Container object definition.


*Appears in:*
- [MariaDBSpec](#mariadbspec)
- [PodTemplate](#podtemplate)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| name string | Name to be given to the container. |  |  |
| image string | Image name to be used by the container. The supported format is <image>:<tag>. |  | Required: {} |
| imagePullPolicy [PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#pullpolicy-v1-core) | ImagePullPolicy is the image pull policy. One of Always, Never or IfNotPresent. If not defined, it defaults to IfNotPresent. |  | Enum: [Always Never IfNotPresent] |
| command string array | Command to be used in the Container. |  |  |
| args string array | Args to be used in the Container. |  |  |
| env [EnvVar](#envvar) array | Env represents the environment variables to be injected in a container. |  |  |
| volumeMounts [VolumeMount](#volumemount) array | VolumeMounts to be used in the Container. |  |  |
| resources [ResourceRequirements](#resourcerequirements) | Resouces describes the compute resource requirements. |  |  |


#### ContainerTemplate


ContainerTemplate defines a template to configure Container objects.


*Appears in:*
- [GaleraAgent](#galeraagent)
- [GaleraInit](#galerainit)
- [MariaDBSpec](#mariadbspec)
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| command string array | Command to be used in the Container. |  |  |
| args string array | Args to be used in the Container. |  |  |
| env [EnvVar](#envvar) array | Env represents the environment variables to be injected in a container. |  |  |
| envFrom [EnvFromSource](#envfromsource) array | EnvFrom represents the references (via ConfigMap and Secrets) to environment variables to be injected in the container. |  |  |
| volumeMounts [VolumeMount](#volumemount) array | VolumeMounts to be used in the Container. |  |  |
| livenessProbe [Probe](#probe) | LivenessProbe to be used in the Container. |  |  |
| readinessProbe [Probe](#probe) | ReadinessProbe to be used in the Container. |  |  |
| startupProbe [Probe](#probe) | StartupProbe to be used in the Container. |  |  |
| resources [ResourceRequirements](#resourcerequirements) | Resouces describes the compute resource requirements. |  |  |
| securityContext [SecurityContext](#securitycontext) | SecurityContext holds security configuration that will be applied to a container. |  |  |


#### CooperativeMonitoring


*Underlying type:* *string*


CooperativeMonitoring enables coordination between multiple MaxScale instances running monitors.
See: [](https://mariadb.com/docs/server/architecture/components/maxscale/monitors/mariadbmon/use-cooperative-locking-ha-maxscale-mariadb-monitor/)


*Appears in:*
- [MaxScaleMonitor](#maxscalemonitor)


| Field | Description |
| --- | --- |
| Field | Description |
| majority_of_all | CooperativeMonitoringMajorityOfAll requires a lock from the majority of the MariaDB servers, even the ones that are down. |
| majority_of_running | CooperativeMonitoringMajorityOfRunning requires a lock from the majority of the MariaDB servers. |


#### CronJobTemplate


CronJobTemplate defines parameters for configuring CronJob objects.


*Appears in:*
- [BackupSpec](#backupspec)
- [SqlJobSpec](#sqljobspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| successfulJobsHistoryLimit integer | SuccessfulJobsHistoryLimit defines the maximum number of successful Jobs to be displayed. |  | Minimum: 0 |
| failedJobsHistoryLimit integer | FailedJobsHistoryLimit defines the maximum number of failed Jobs to be displayed. |  | Minimum: 0 |
| timeZone string | TimeZone defines the timezone associated with the cron expression. |  |  |


#### Database


Database is the Schema for the databases API. It is used to define a logical database as if you were running a 'CREATE DATABASE' statement.


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| apiVersion string | enterprise.mariadb.com/v1alpha1 |  |  |
| kind string | Database |  |  |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |  |  |
| spec [DatabaseSpec](#databasespec) |  |  |  |


#### DatabaseSpec


DatabaseSpec defines the desired state of Database


*Appears in:*
- [Database](#database)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| requeueInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | RequeueInterval is used to perform requeue reconciliations. |  |  |
| retryInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | RetryInterval is the interval used to perform retries. |  |  |
| cleanupPolicy [CleanupPolicy](#cleanuppolicy) | CleanupPolicy defines the behavior for cleaning up a SQL resource. |  | Enum: [Skip Delete] |
| mariaDbRef [MariaDBRef](#mariadbref) | MariaDBRef is a reference to a MariaDB object. |  | Required: {} |
| characterSet string | CharacterSet to use in the Database. | utf8 |  |
| collate string | Collate to use in the Database. | utf8_general_ci |  |
| name string | Name overrides the default Database name provided by metadata.name. |  | MaxLength: 80 |


#### EmptyDirVolumeSource


Refer to the Kubernetes docs: [#emptydirvolumesource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#emptydirvolumesource-v1-core).


*Appears in:*
- [StorageVolumeSource](#storagevolumesource)
- [Volume](#volume)
- [VolumeSource](#volumesource)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| medium [StorageMedium](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#storagemedium-v1-core) |  |  |  |
| sizeLimit [Quantity](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#quantity-resource-api) |  |  |  |


#### EnvFromSource


Refer to the Kubernetes docs: [#envfromsource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#envfromsource-v1-core).


*Appears in:*
- [ContainerTemplate](#containertemplate)
- [GaleraAgent](#galeraagent)
- [GaleraInit](#galerainit)
- [MariaDBSpec](#mariadbspec)
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| prefix string |  |  |  |
| configMapRef [LocalObjectReference](#localobjectreference) |  |  |  |
| secretRef [LocalObjectReference](#localobjectreference) |  |  |  |


#### EnvVar


Refer to the Kubernetes docs: [#envvarsource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#envvarsource-v1-core).


*Appears in:*
- [Container](#container)
- [ContainerTemplate](#containertemplate)
- [GaleraAgent](#galeraagent)
- [GaleraInit](#galerainit)
- [MariaDBSpec](#mariadbspec)
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| name string | Name of the environment variable. Must be a C_IDENTIFIER. |  |  |
| value string |  |  |  |
| valueFrom [EnvVarSource](#envvarsource) |  |  |  |


#### EnvVarSource


Refer to the Kubernetes docs: [#envvarsource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#envvarsource-v1-core).


*Appears in:*
- [EnvVar](#envvar)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| fieldRef [ObjectFieldSelector](#objectfieldselector) |  |  |  |
| configMapKeyRef [ConfigMapKeySelector](#configmapkeyselector) |  |  |  |
| secretKeyRef [SecretKeySelector](#secretkeyselector) |  |  |  |


#### ExecAction


Refer to the Kubernetes docs: [#execaction-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#execaction-v1-core).


*Appears in:*
- [Probe](#probe)
- [ProbeHandler](#probehandler)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| command string array |  |  |  |


#### Exporter


Exporter defines a metrics exporter container.


*Appears in:*
- [MariadbMetrics](#mariadbmetrics)
- [MaxScaleMetrics](#maxscalemetrics)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| image string | Image name to be used as metrics exporter. The supported format is <image>:<tag>. |  |  |
| imagePullPolicy [PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#pullpolicy-v1-core) | ImagePullPolicy is the image pull policy. One of Always, Never or IfNotPresent. If not defined, it defaults to IfNotPresent. |  | Enum: [Always Never IfNotPresent] |
| imagePullSecrets [LocalObjectReference](#localobjectreference) array | ImagePullSecrets is the list of pull Secrets to be used to pull the image. |  |  |
| args string array | Args to be used in the Container. |  |  |
| port integer | Port where the exporter will be listening for connections. |  |  |
| resources [ResourceRequirements](#resourcerequirements) | Resouces describes the compute resource requirements. |  |  |
| podMetadata [Metadata](#metadata) | PodMetadata defines extra metadata for the Pod. |  |  |
| securityContext [SecurityContext](#securitycontext) | SecurityContext holds container-level security attributes. |  |  |
| podSecurityContext [PodSecurityContext](#podsecuritycontext) | SecurityContext holds pod-level security attributes and common container settings. |  |  |
| affinity [AffinityConfig](#affinityconfig) | Affinity to be used in the Pod. |  |  |
| nodeSelector object (keys:string, values:string) | NodeSelector to be used in the Pod. |  |  |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array | Tolerations to be used in the Pod. |  |  |
| priorityClassName string | PriorityClassName to be used in the Pod. |  |  |


#### Galera


Galera allows you to enable multi-master HA via Galera in your MariaDB cluster.


*Appears in:*
- [MariaDBSpec](#mariadbspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| primary [PrimaryGalera](#primarygalera) | Primary is the Galera configuration for the primary node. |  |  |
| sst [SST](#sst) | SST is the Snapshot State Transfer used when new Pods join the cluster.More info: [sst.html](https://galeracluster.com/library/documentation/sst.html). |  | Enum: [rsync mariabackup mysqldump] |
| availableWhenDonor boolean | AvailableWhenDonor indicates whether a donor node should be responding to queries. It defaults to false. |  |  |
| galeraLibPath string | GaleraLibPath is a path inside the MariaDB image to the wsrep provider plugin. It is defaulted if not provided.More info: [mysql-wsrep-options.html#wsrep-provider](https://galeracluster.com/library/documentation/mysql-wsrep-options.html#wsrep-provider). |  |  |
| replicaThreads integer | ReplicaThreads is the number of replica threads used to apply Galera write sets in parallel.More info: [galera-cluster-system-variables#wsrep_slave_threads](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_slave_threads). |  |  |
| providerOptions object (keys:string, values:string) | ProviderOptions is map of Galera configuration parameters.More info: [galera-cluster-system-variables#wsrep_provider_options](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_provider_options). |  |  |
| agent [GaleraAgent](#galeraagent) | GaleraAgent is a sidecar agent that co-operates with mariadb-enterprise-operator. |  |  |
| recovery [GaleraRecovery](#galerarecovery) | GaleraRecovery is the recovery process performed by the operator whenever the Galera cluster is not healthy.More info: [crash-recovery.html](https://galeracluster.com/library/documentation/crash-recovery.html). |  |  |
| initContainer [GaleraInit](#galerainit) | InitContainer is an init container that runs in the MariaDB Pod and co-operates with mariadb-enterprise-operator. |  |  |
| initJob [GaleraInitJob](#galerainitjob) | InitJob defines a Job that co-operates with mariadb-enterprise-operator by performing initialization tasks. |  |  |
| config [GaleraConfig](#galeraconfig) | GaleraConfig defines storage options for the Galera configuration files. |  |  |
| clusterName string | ClusterName is the name of the cluster to be used in the Galera config file. |  |  |
| enabled boolean | Enabled is a flag to enable Galera. |  |  |


#### GaleraAgent


GaleraAgent is a sidecar agent that co-operates with mariadb-enterprise-operator.


*Appears in:*
- [Galera](#galera)
- [GaleraSpec](#galeraspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| command string array | Command to be used in the Container. |  |  |
| args string array | Args to be used in the Container. |  |  |
| env [EnvVar](#envvar) array | Env represents the environment variables to be injected in a container. |  |  |
| envFrom [EnvFromSource](#envfromsource) array | EnvFrom represents the references (via ConfigMap and Secrets) to environment variables to be injected in the container. |  |  |
| volumeMounts [VolumeMount](#volumemount) array | VolumeMounts to be used in the Container. |  |  |
| livenessProbe [Probe](#probe) | LivenessProbe to be used in the Container. |  |  |
| readinessProbe [Probe](#probe) | ReadinessProbe to be used in the Container. |  |  |
| startupProbe [Probe](#probe) | StartupProbe to be used in the Container. |  |  |
| resources [ResourceRequirements](#resourcerequirements) | Resouces describes the compute resource requirements. |  |  |
| securityContext [SecurityContext](#securitycontext) | SecurityContext holds security configuration that will be applied to a container. |  |  |
| image string | Image name to be used by the MariaDB instances. The supported format is <image>:<tag>. |  |  |
| imagePullPolicy [PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#pullpolicy-v1-core) | ImagePullPolicy is the image pull policy. One of Always, Never or IfNotPresent. If not defined, it defaults to IfNotPresent. |  | Enum: [Always Never IfNotPresent] |
| port integer | Port where the agent will be listening for API connections. |  |  |
| probePort integer | Port where the agent will be listening for probe connections. |  |  |
| kubernetesAuth [KubernetesAuth](#kubernetesauth) | KubernetesAuth to be used by the agent container |  |  |
| basicAuth [BasicAuth](#basicauth) | BasicAuth to be used by the agent container |  |  |
| gracefulShutdownTimeout [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | GracefulShutdownTimeout is the time we give to the agent container in order to gracefully terminate in-flight requests. |  |  |


#### GaleraConfig


GaleraConfig defines storage options for the Galera configuration files.


*Appears in:*
- [Galera](#galera)
- [GaleraSpec](#galeraspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| reuseStorageVolume boolean | ReuseStorageVolume indicates that storage volume used by MariaDB should be reused to store the Galera configuration files.It defaults to false, which implies that a dedicated volume for the Galera configuration files is provisioned. |  |  |
| volumeClaimTemplate [VolumeClaimTemplate](#volumeclaimtemplate) | VolumeClaimTemplate is a template for the PVC that will contain the Galera configuration files shared between the InitContainer, Agent and MariaDB. |  |  |


#### GaleraInit


GaleraInit is an init container that runs in the MariaDB Pod and co-operates with mariadb-enterprise-operator.


*Appears in:*
- [Galera](#galera)
- [GaleraSpec](#galeraspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| command string array | Command to be used in the Container. |  |  |
| args string array | Args to be used in the Container. |  |  |
| env [EnvVar](#envvar) array | Env represents the environment variables to be injected in a container. |  |  |
| envFrom [EnvFromSource](#envfromsource) array | EnvFrom represents the references (via ConfigMap and Secrets) to environment variables to be injected in the container. |  |  |
| volumeMounts [VolumeMount](#volumemount) array | VolumeMounts to be used in the Container. |  |  |
| livenessProbe [Probe](#probe) | LivenessProbe to be used in the Container. |  |  |
| readinessProbe [Probe](#probe) | ReadinessProbe to be used in the Container. |  |  |
| startupProbe [Probe](#probe) | StartupProbe to be used in the Container. |  |  |
| resources [ResourceRequirements](#resourcerequirements) | Resouces describes the compute resource requirements. |  |  |
| securityContext [SecurityContext](#securitycontext) | SecurityContext holds security configuration that will be applied to a container. |  |  |
| image string | Image name to be used by the MariaDB instances. The supported format is <image>:<tag>. |  | Required: {} |
| imagePullPolicy [PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#pullpolicy-v1-core) | ImagePullPolicy is the image pull policy. One of Always, Never or IfNotPresent. If not defined, it defaults to IfNotPresent. |  | Enum: [Always Never IfNotPresent] |


#### GaleraInitJob


GaleraInitJob defines a Job used to be used to initialize the Galera cluster.


*Appears in:*
- [Galera](#galera)
- [GaleraSpec](#galeraspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| metadata [Metadata](#metadata) | Refer to Kubernetes API documentation for fields of metadata. |  |  |
| resources [ResourceRequirements](#resourcerequirements) | Resouces describes the compute resource requirements. |  |  |


#### GaleraRecovery


GaleraRecovery is the recovery process performed by the operator whenever the Galera cluster is not healthy.
More info: [crash-recovery.html](https://galeracluster.com/library/documentation/crash-recovery.html).


*Appears in:*
- [Galera](#galera)
- [GaleraSpec](#galeraspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| enabled boolean | Enabled is a flag to enable GaleraRecovery. |  |  |
| minClusterSize [IntOrString](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#intorstring-intstr-util) | MinClusterSize is the minimum number of replicas to consider the cluster healthy. It can be either a number of replicas (1) or a percentage (50%).If Galera consistently reports less replicas than this value for the given 'ClusterHealthyTimeout' interval, a cluster recovery is iniated.It defaults to '1' replica, and it is highly recommendeded to keep this value at '1' in most cases.If set to more than one replica, the cluster recovery process may restart the healthy replicas as well. |  |  |
| clusterMonitorInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | ClusterMonitorInterval represents the interval used to monitor the Galera cluster health. |  |  |
| clusterHealthyTimeout [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | ClusterHealthyTimeout represents the duration at which a Galera cluster, that consistently failed health checks,is considered unhealthy, and consequently the Galera recovery process will be initiated by the operator. |  |  |
| clusterBootstrapTimeout [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | ClusterBootstrapTimeout is the time limit for bootstrapping a cluster.Once this timeout is reached, the Galera recovery state is reset and a new cluster bootstrap will be attempted. |  |  |
| clusterUpscaleTimeout [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | ClusterUpscaleTimeout represents the maximum duration for upscaling the cluster's StatefulSet during the recovery process. |  |  |
| clusterDownscaleTimeout [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | ClusterDownscaleTimeout represents the maximum duration for downscaling the cluster's StatefulSet during the recovery process. |  |  |
| podRecoveryTimeout [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | PodRecoveryTimeout is the time limit for recevorying the sequence of a Pod during the cluster recovery. |  |  |
| podSyncTimeout [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | PodSyncTimeout is the time limit for a Pod to join the cluster after having performed a cluster bootstrap during the cluster recovery. |  |  |
| forceClusterBootstrapInPod string | ForceClusterBootstrapInPod allows you to manually initiate the bootstrap process in a specific Pod.IMPORTANT: Use this option only in exceptional circumstances. Not selecting the Pod with the highest sequence number may result in data loss.IMPORTANT: Ensure you unset this field after completing the bootstrap to allow the operator to choose the appropriate Pod to bootstrap from in an event of cluster recovery. |  |  |
| job [GaleraRecoveryJob](#galerarecoveryjob) | Job defines a Job that co-operates with mariadb-enterprise-operator by performing the Galera cluster recovery . |  |  |


#### GaleraRecoveryJob


GaleraRecoveryJob defines a Job used to be used to recover the Galera cluster.


*Appears in:*
- [GaleraRecovery](#galerarecovery)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| metadata [Metadata](#metadata) | Refer to Kubernetes API documentation for fields of metadata. |  |  |
| resources [ResourceRequirements](#resourcerequirements) | Resouces describes the compute resource requirements. |  |  |
| podAffinity boolean | PodAffinity indicates whether the recovery Jobs should run in the same Node as the MariaDB Pods. It defaults to true. |  |  |


#### GaleraSpec


GaleraSpec is the Galera desired state specification.


*Appears in:*
- [Galera](#galera)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| primary [PrimaryGalera](#primarygalera) | Primary is the Galera configuration for the primary node. |  |  |
| sst [SST](#sst) | SST is the Snapshot State Transfer used when new Pods join the cluster.More info: [sst.html](https://galeracluster.com/library/documentation/sst.html). |  | Enum: [rsync mariabackup mysqldump] |
| availableWhenDonor boolean | AvailableWhenDonor indicates whether a donor node should be responding to queries. It defaults to false. |  |  |
| galeraLibPath string | GaleraLibPath is a path inside the MariaDB image to the wsrep provider plugin. It is defaulted if not provided.More info: [mysql-wsrep-options.html#wsrep-provider](https://galeracluster.com/library/documentation/mysql-wsrep-options.html#wsrep-provider). |  |  |
| replicaThreads integer | ReplicaThreads is the number of replica threads used to apply Galera write sets in parallel.More info: [galera-cluster-system-variables#wsrep_slave_threads](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_slave_threads). |  |  |
| providerOptions object (keys:string, values:string) | ProviderOptions is map of Galera configuration parameters.More info: [galera-cluster-system-variables#wsrep_provider_options](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_provider_options). |  |  |
| agent [GaleraAgent](#galeraagent) | GaleraAgent is a sidecar agent that co-operates with mariadb-enterprise-operator. |  |  |
| recovery [GaleraRecovery](#galerarecovery) | GaleraRecovery is the recovery process performed by the operator whenever the Galera cluster is not healthy.More info: [crash-recovery.html](https://galeracluster.com/library/documentation/crash-recovery.html). |  |  |
| initContainer [GaleraInit](#galerainit) | InitContainer is an init container that runs in the MariaDB Pod and co-operates with mariadb-enterprise-operator. |  |  |
| initJob [GaleraInitJob](#galerainitjob) | InitJob defines a Job that co-operates with mariadb-enterprise-operator by performing initialization tasks. |  |  |
| config [GaleraConfig](#galeraconfig) | GaleraConfig defines storage options for the Galera configuration files. |  |  |
| clusterName string | ClusterName is the name of the cluster to be used in the Galera config file. |  |  |


#### GeneratedSecretKeyRef


GeneratedSecretKeyRef defines a reference to a Secret that can be automatically generated by mariadb-enterprise-operator if needed.


*Appears in:*
- [BasicAuth](#basicauth)
- [MariaDBSpec](#mariadbspec)
- [MariadbMetrics](#mariadbmetrics)
- [MaxScaleAuth](#maxscaleauth)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| name string |  |  |  |
| key string |  |  |  |
| generate boolean | Generate indicates whether the Secret should be generated if the Secret referenced is not present. | false |  |


#### Grant


Grant is the Schema for the grants API. It is used to define grants as if you were running a 'GRANT' statement.


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| apiVersion string | enterprise.mariadb.com/v1alpha1 |  |  |
| kind string | Grant |  |  |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |  |  |
| spec [GrantSpec](#grantspec) |  |  |  |


#### GrantSpec


GrantSpec defines the desired state of Grant


*Appears in:*
- [Grant](#grant)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| requeueInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | RequeueInterval is used to perform requeue reconciliations. |  |  |
| retryInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | RetryInterval is the interval used to perform retries. |  |  |
| cleanupPolicy [CleanupPolicy](#cleanuppolicy) | CleanupPolicy defines the behavior for cleaning up a SQL resource. |  | Enum: [Skip Delete] |
| mariaDbRef [MariaDBRef](#mariadbref) | MariaDBRef is a reference to a MariaDB object. |  | Required: {} |
| privileges string array | Privileges to use in the Grant. |  | MinItems: 1 Required: {} |
| database string | Database to use in the Grant. | * |  |
| table string | Table to use in the Grant. | * |  |
| username string | Username to use in the Grant. |  | Required: {} |
| host string | Host to use in the Grant. It can be localhost, an IP or '%'. |  |  |
| grantOption boolean | GrantOption to use in the Grant. | false |  |


#### HTTPGetAction


Refer to the Kubernetes docs: [#httpgetaction-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#httpgetaction-v1-core).


*Appears in:*
- [Probe](#probe)
- [ProbeHandler](#probehandler)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| path string |  |  |  |
| port [IntOrString](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#intorstring-intstr-util) |  |  |  |
| host string |  |  |  |
| scheme [URIScheme](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#urischeme-v1-core) |  |  |  |


#### HealthCheck


HealthCheck defines intervals for performing health checks.


*Appears in:*
- [ConnectionSpec](#connectionspec)
- [ConnectionTemplate](#connectiontemplate)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| interval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | Interval used to perform health checks. |  |  |
| retryInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | RetryInterval is the interval used to perform health check retries. |  |  |


#### HostPathVolumeSource


Refer to the Kubernetes docs: [#hostpathvolumesource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#hostpathvolumesource-v1-core)


*Appears in:*
- [StorageVolumeSource](#storagevolumesource)
- [Volume](#volume)
- [VolumeSource](#volumesource)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| path string |  |  |  |
| type string |  |  |  |


#### Job


Job defines a Job used to be used with MariaDB.


*Appears in:*
- [BootstrapFrom](#bootstrapfrom)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| metadata [Metadata](#metadata) | Refer to Kubernetes API documentation for fields of metadata. |  |  |
| affinity [AffinityConfig](#affinityconfig) | Affinity to be used in the Pod. |  |  |
| resources [ResourceRequirements](#resourcerequirements) | Resouces describes the compute resource requirements. |  |  |
| args string array | Args to be used in the Container. |  |  |


#### JobContainerTemplate


JobContainerTemplate defines a template to configure Container objects that run in a Job.


*Appears in:*
- [BackupSpec](#backupspec)
- [RestoreSpec](#restorespec)
- [SqlJobSpec](#sqljobspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| args string array | Args to be used in the Container. |  |  |
| resources [ResourceRequirements](#resourcerequirements) | Resouces describes the compute resource requirements. |  |  |
| securityContext [SecurityContext](#securitycontext) | SecurityContext holds security configuration that will be applied to a container. |  |  |


#### JobPodTemplate


JobPodTemplate defines a template to configure Container objects that run in a Job.


*Appears in:*
- [BackupSpec](#backupspec)
- [RestoreSpec](#restorespec)
- [SqlJobSpec](#sqljobspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| podMetadata [Metadata](#metadata) | PodMetadata defines extra metadata for the Pod. |  |  |
| imagePullSecrets [LocalObjectReference](#localobjectreference) array | ImagePullSecrets is the list of pull Secrets to be used to pull the image. |  |  |
| podSecurityContext [PodSecurityContext](#podsecuritycontext) | SecurityContext holds pod-level security attributes and common container settings. |  |  |
| serviceAccountName string | ServiceAccountName is the name of the ServiceAccount to be used by the Pods. |  |  |
| affinity [AffinityConfig](#affinityconfig) | Affinity to be used in the Pod. |  |  |
| nodeSelector object (keys:string, values:string) | NodeSelector to be used in the Pod. |  |  |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array | Tolerations to be used in the Pod. |  |  |
| priorityClassName string | PriorityClassName to be used in the Pod. |  |  |


#### KubernetesAuth


KubernetesAuth refers to the Kubernetes authentication mechanism utilized for establishing a connection from the operator to the agent.
The agent validates the legitimacy of the service account token provided as an Authorization header by creating a TokenReview resource.


*Appears in:*
- [GaleraAgent](#galeraagent)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| enabled boolean | Enabled is a flag to enable KubernetesAuth |  |  |
| authDelegatorRoleName string | AuthDelegatorRoleName is the name of the ClusterRoleBinding that is associated with the "system:auth-delegator" ClusterRole.It is necessary for creating TokenReview objects in order for the agent to validate the service account token. |  |  |


#### LabelSelector


*Underlying type:* *[struct{MatchLabels map[string]string "json:\"matchLabels,omitempty\""; MatchExpressions []LabelSelectorRequirement "json:\"matchExpressions,omitempty\""}](#struct{matchlabels-map[string]string-"json:\"matchlabels,omitempty\"";-matchexpressions-[]labelselectorrequirement-"json:\"matchexpressions,omitempty\""})*


Refer to the Kubernetes docs: [#labelselector-v1-meta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#labelselector-v1-meta)


*Appears in:*
- [PodAffinityTerm](#podaffinityterm)


#### LocalObjectReference


Refer to the Kubernetes docs: [#localobjectreference-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#localobjectreference-v1-core).


*Appears in:*
- [BackupSpec](#backupspec)
- [BootstrapFrom](#bootstrapfrom)
- [CSIVolumeSource](#csivolumesource)
- [ConfigMapKeySelector](#configmapkeyselector)
- [ConfigMapVolumeSource](#configmapvolumesource)
- [ConnectionSpec](#connectionspec)
- [EnvFromSource](#envfromsource)
- [Exporter](#exporter)
- [GeneratedSecretKeyRef](#generatedsecretkeyref)
- [JobPodTemplate](#jobpodtemplate)
- [MariaDBSpec](#mariadbspec)
- [MaxScalePodTemplate](#maxscalepodtemplate)
- [MaxScaleSpec](#maxscalespec)
- [MaxScaleTLS](#maxscaletls)
- [PodTemplate](#podtemplate)
- [RestoreSource](#restoresource)
- [RestoreSpec](#restorespec)
- [SecretKeySelector](#secretkeyselector)
- [SqlJobSpec](#sqljobspec)
- [TLS](#tls)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| name string |  |  |  |


#### MariaDB


MariaDB is the Schema for the mariadbs API. It is used to define MariaDB clusters.


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| apiVersion string | enterprise.mariadb.com/v1alpha1 |  |  |
| kind string | MariaDB |  |  |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |  |  |
| spec [MariaDBSpec](#mariadbspec) |  |  |  |


#### MariaDBMaxScaleSpec


MariaDBMaxScaleSpec defines a reduced version of MaxScale to be used with the current MariaDB.


*Appears in:*
- [MariaDBSpec](#mariadbspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| enabled boolean | Enabled is a flag to enable a MaxScale instance to be used with the current MariaDB. |  |  |
| image string | Image name to be used by the MaxScale instances. The supported format is <image>:<tag>.Only MariaDB official images are supported. |  |  |
| imagePullPolicy [PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#pullpolicy-v1-core) | ImagePullPolicy is the image pull policy. One of Always, Never or IfNotPresent. If not defined, it defaults to IfNotPresent. |  | Enum: [Always Never IfNotPresent] |
| services [MaxScaleService](#maxscaleservice) array | Services define how the traffic is forwarded to the MariaDB servers. |  |  |
| monitor [MaxScaleMonitor](#maxscalemonitor) | Monitor monitors MariaDB server instances. |  |  |
| admin [MaxScaleAdmin](#maxscaleadmin) | Admin configures the admin REST API and GUI. |  |  |
| config [MaxScaleConfig](#maxscaleconfig) | Config defines the MaxScale configuration. |  |  |
| auth [MaxScaleAuth](#maxscaleauth) | Auth defines the credentials required for MaxScale to connect to MariaDB. |  |  |
| metrics [MaxScaleMetrics](#maxscalemetrics) | Metrics configures metrics and how to scrape them. |  |  |
| tls [MaxScaleTLS](#maxscaletls) | TLS defines the PKI to be used with MaxScale. |  |  |
| connection [ConnectionTemplate](#connectiontemplate) | Connection provides a template to define the Connection for MaxScale. |  |  |
| replicas integer | Replicas indicates the number of desired instances. |  |  |
| podDisruptionBudget [PodDisruptionBudget](#poddisruptionbudget) | PodDisruptionBudget defines the budget for replica availability. |  |  |
| updateStrategy [StatefulSetUpdateStrategy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#statefulsetupdatestrategy-v1-apps) | UpdateStrategy defines the update strategy for the StatefulSet object. |  |  |
| kubernetesService [ServiceTemplate](#servicetemplate) | KubernetesService defines a template for a Kubernetes Service object to connect to MaxScale. |  |  |
| guiKubernetesService [ServiceTemplate](#servicetemplate) | GuiKubernetesService define a template for a Kubernetes Service object to connect to MaxScale's GUI. |  |  |
| requeueInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | RequeueInterval is used to perform requeue reconciliations. |  |  |


#### MariaDBRef


MariaDBRef is a reference to a MariaDB object.


*Appears in:*
- [BackupSpec](#backupspec)
- [ConnectionSpec](#connectionspec)
- [DatabaseSpec](#databasespec)
- [GrantSpec](#grantspec)
- [MaxScaleSpec](#maxscalespec)
- [RestoreSpec](#restorespec)
- [SqlJobSpec](#sqljobspec)
- [UserSpec](#userspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| name string |  |  |  |
| namespace string |  |  |  |
| waitForIt boolean | WaitForIt indicates whether the controller using this reference should wait for MariaDB to be ready. | true |  |


#### MariaDBSpec


MariaDBSpec defines the desired state of MariaDB


*Appears in:*
- [MariaDB](#mariadb)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| command string array | Command to be used in the Container. |  |  |
| args string array | Args to be used in the Container. |  |  |
| env [EnvVar](#envvar) array | Env represents the environment variables to be injected in a container. |  |  |
| envFrom [EnvFromSource](#envfromsource) array | EnvFrom represents the references (via ConfigMap and Secrets) to environment variables to be injected in the container. |  |  |
| volumeMounts [VolumeMount](#volumemount) array | VolumeMounts to be used in the Container. |  |  |
| livenessProbe [Probe](#probe) | LivenessProbe to be used in the Container. |  |  |
| readinessProbe [Probe](#probe) | ReadinessProbe to be used in the Container. |  |  |
| startupProbe [Probe](#probe) | StartupProbe to be used in the Container. |  |  |
| resources [ResourceRequirements](#resourcerequirements) | Resouces describes the compute resource requirements. |  |  |
| securityContext [SecurityContext](#securitycontext) | SecurityContext holds security configuration that will be applied to a container. |  |  |
| podMetadata [Metadata](#metadata) | PodMetadata defines extra metadata for the Pod. |  |  |
| imagePullSecrets [LocalObjectReference](#localobjectreference) array | ImagePullSecrets is the list of pull Secrets to be used to pull the image. |  |  |
| initContainers [Container](#container) array | InitContainers to be used in the Pod. |  |  |
| sidecarContainers [Container](#container) array | SidecarContainers to be used in the Pod. |  |  |
| podSecurityContext [PodSecurityContext](#podsecuritycontext) | SecurityContext holds pod-level security attributes and common container settings. |  |  |
| serviceAccountName string | ServiceAccountName is the name of the ServiceAccount to be used by the Pods. |  |  |
| affinity [AffinityConfig](#affinityconfig) | Affinity to be used in the Pod. |  |  |
| nodeSelector object (keys:string, values:string) | NodeSelector to be used in the Pod. |  |  |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array | Tolerations to be used in the Pod. |  |  |
| volumes [Volume](#volume) array | Volumes to be used in the Pod. |  |  |
| priorityClassName string | PriorityClassName to be used in the Pod. |  |  |
| topologySpreadConstraints [TopologySpreadConstraint](#topologyspreadconstraint) array | TopologySpreadConstraints to be used in the Pod. |  |  |
| suspend boolean | Suspend indicates whether the current resource should be suspended or not.This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities. | false |  |
| image string | Image name to be used by the MariaDB instances. The supported format is <image>:<tag>.Only MariaDB official images are supported. |  |  |
| imagePullPolicy [PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#pullpolicy-v1-core) | ImagePullPolicy is the image pull policy. One of Always, Never or IfNotPresent. If not defined, it defaults to IfNotPresent. |  | Enum: [Always Never IfNotPresent] |
| inheritMetadata [Metadata](#metadata) | InheritMetadata defines the metadata to be inherited by children resources. |  |  |
| rootPasswordSecretKeyRef [GeneratedSecretKeyRef](#generatedsecretkeyref) | RootPasswordSecretKeyRef is a reference to a Secret key containing the root password. |  |  |
| rootEmptyPassword boolean | RootEmptyPassword indicates if the root password should be empty. Don't use this feature in production, it is only intended for development and test environments. |  |  |
| database string | Database is the name of the initial Database. |  |  |
| username string | Username is the initial username to be created by the operator once MariaDB is ready.The initial User will have ALL PRIVILEGES in the initial Database. |  |  |
| passwordSecretKeyRef [GeneratedSecretKeyRef](#generatedsecretkeyref) | PasswordSecretKeyRef is a reference to a Secret that contains the password to be used by the initial User.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password. |  |  |
| passwordHashSecretKeyRef [SecretKeySelector](#secretkeyselector) | PasswordHashSecretKeyRef is a reference to the password hash to be used by the initial User.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password hash.It requires the 'skip-strict-password-validation' option to be set. See: [](https://mariadb.com/docs/server/ref/mdb/cli/mariadbd/strict-password-validation/). |  |  |
| passwordPlugin [PasswordPlugin](#passwordplugin) | PasswordPlugin is a reference to the password plugin and arguments to be used by the initial User.It requires the 'skip-strict-password-validation' option to be set. See: [](https://mariadb.com/docs/server/ref/mdb/cli/mariadbd/strict-password-validation/). |  |  |
| myCnf string | MyCnf allows to specify the my.cnf file mounted by Mariadb.Updating this field will trigger an update to the Mariadb resource. |  |  |
| myCnfConfigMapKeyRef [ConfigMapKeySelector](#configmapkeyselector) | MyCnfConfigMapKeyRef is a reference to the my.cnf config file provided via a ConfigMap.If not provided, it will be defaulted with a reference to a ConfigMap containing the MyCnf field.If the referred ConfigMap is labeled with "enterprise.mariadb.com/watch", an update to the Mariadb resource will be triggered when the ConfigMap is updated. |  |  |
| timeZone string | TimeZone sets the default timezone. If not provided, it defaults to SYSTEM and the timezone data is not loaded. |  |  |
| bootstrapFrom [BootstrapFrom](#bootstrapfrom) | BootstrapFrom defines a source to bootstrap from. |  |  |
| storage [Storage](#storage) | Storage defines the storage options to be used for provisioning the PVCs mounted by MariaDB. |  |  |
| metrics [MariadbMetrics](#mariadbmetrics) | Metrics configures metrics and how to scrape them. |  |  |
| tls [TLS](#tls) | TLS defines the PKI to be used with MariaDB. |  |  |
| galera [Galera](#galera) | Galera configures high availability via Galera. |  |  |
| maxScaleRef [ObjectReference](#objectreference) | MaxScaleRef is a reference to a MaxScale resource to be used with the current MariaDB.Providing this field implies delegating high availability tasks such as primary failover to MaxScale. |  |  |
| maxScale [MariaDBMaxScaleSpec](#mariadbmaxscalespec) | MaxScale is the MaxScale specification that defines the MaxScale resource to be used with the current MariaDB.When enabling this field, MaxScaleRef is automatically set. |  |  |
| replicas integer | Replicas indicates the number of desired instances. | 1 |  |
| replicasAllowEvenNumber boolean | disables the validation check for an odd number of replicas. | false |  |
| port integer | Port where the instances will be listening for connections. | 3306 |  |
| servicePorts [ServicePort](#serviceport) array | ServicePorts is the list of additional named ports to be added to the Services created by the operator. |  |  |
| podDisruptionBudget [PodDisruptionBudget](#poddisruptionbudget) | PodDisruptionBudget defines the budget for replica availability. |  |  |
| updateStrategy [UpdateStrategy](#updatestrategy) | UpdateStrategy defines how a MariaDB resource is updated. |  |  |
| service [ServiceTemplate](#servicetemplate) | Service defines a template to configure the general Service object.The network traffic of this Service will be routed to all Pods. |  |  |
| connection [ConnectionTemplate](#connectiontemplate) | Connection defines a template to configure the general Connection object.This Connection provides the initial User access to the initial Database.It will make use of the Service to route network traffic to all Pods. |  |  |
| primaryService [ServiceTemplate](#servicetemplate) | PrimaryService defines a template to configure the primary Service object.The network traffic of this Service will be routed to the primary Pod. |  |  |
| primaryConnection [ConnectionTemplate](#connectiontemplate) | PrimaryConnection defines a template to configure the primary Connection object.This Connection provides the initial User access to the initial Database.It will make use of the PrimaryService to route network traffic to the primary Pod. |  |  |
| secondaryService [ServiceTemplate](#servicetemplate) | SecondaryService defines a template to configure the secondary Service object.The network traffic of this Service will be routed to the secondary Pods. |  |  |
| secondaryConnection [ConnectionTemplate](#connectiontemplate) | SecondaryConnection defines a template to configure the secondary Connection object.This Connection provides the initial User access to the initial Database.It will make use of the SecondaryService to route network traffic to the secondary Pods. |  |  |


#### MariadbMetrics


MariadbMetrics defines the metrics for a MariaDB.


*Appears in:*
- [MariaDBSpec](#mariadbspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| enabled boolean | Enabled is a flag to enable Metrics |  |  |
| exporter [Exporter](#exporter) | Exporter defines the metrics exporter container. |  |  |
| serviceMonitor [ServiceMonitor](#servicemonitor) | ServiceMonitor defines the ServiceMonior object. |  |  |
| username string | Username is the username of the monitoring user used by the exporter. |  |  |
| passwordSecretKeyRef [GeneratedSecretKeyRef](#generatedsecretkeyref) | PasswordSecretKeyRef is a reference to the password of the monitoring user used by the exporter.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password. |  |  |


#### MaxScale


MaxScale is the Schema for the maxscales API. It is used to define MaxScale clusters.


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| apiVersion string | enterprise.mariadb.com/v1alpha1 |  |  |
| kind string | MaxScale |  |  |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |  |  |
| spec [MaxScaleSpec](#maxscalespec) |  |  |  |


#### MaxScaleAdmin


MaxScaleAdmin configures the admin REST API and GUI.


*Appears in:*
- [MariaDBMaxScaleSpec](#mariadbmaxscalespec)
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| port integer | Port where the admin REST API and GUI will be exposed. |  |  |
| guiEnabled boolean | GuiEnabled indicates whether the admin GUI should be enabled. |  |  |


#### MaxScaleAuth


MaxScaleAuth defines the credentials required for MaxScale to connect to MariaDB.


*Appears in:*
- [MariaDBMaxScaleSpec](#mariadbmaxscalespec)
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| generate boolean | Generate defies whether the operator should generate users and grants for MaxScale to work.It only supports MariaDBs specified via spec.mariaDbRef. |  |  |
| adminUsername string | AdminUsername is an admin username to call the admin REST API. It is defaulted if not provided. |  |  |
| adminPasswordSecretKeyRef [GeneratedSecretKeyRef](#generatedsecretkeyref) | AdminPasswordSecretKeyRef is Secret key reference to the admin password to call the admin REST API. It is defaulted if not provided. |  |  |
| deleteDefaultAdmin boolean | DeleteDefaultAdmin determines whether the default admin user should be deleted after the initial configuration. If not provided, it defaults to true. |  |  |
| metricsUsername string | MetricsUsername is an metrics username to call the REST API. It is defaulted if metrics are enabled. |  |  |
| metricsPasswordSecretKeyRef [GeneratedSecretKeyRef](#generatedsecretkeyref) | MetricsPasswordSecretKeyRef is Secret key reference to the metrics password to call the admib REST API. It is defaulted if metrics are enabled.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password. |  |  |
| clientUsername string | ClientUsername is the user to connect to MaxScale. It is defaulted if not provided. |  |  |
| clientPasswordSecretKeyRef [GeneratedSecretKeyRef](#generatedsecretkeyref) | ClientPasswordSecretKeyRef is Secret key reference to the password to connect to MaxScale. It is defaulted if not provided.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password. |  |  |
| clientMaxConnections integer | ClientMaxConnections defines the maximum number of connections that the client can establish.If HA is enabled, make sure to increase this value, as more MaxScale replicas implies more connections.It defaults to 30 times the number of MaxScale replicas. |  |  |
| serverUsername string | ServerUsername is the user used by MaxScale to connect to MariaDB server. It is defaulted if not provided. |  |  |
| serverPasswordSecretKeyRef [GeneratedSecretKeyRef](#generatedsecretkeyref) | ServerPasswordSecretKeyRef is Secret key reference to the password used by MaxScale to connect to MariaDB server. It is defaulted if not provided.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password. |  |  |
| serverMaxConnections integer | ServerMaxConnections defines the maximum number of connections that the server can establish.If HA is enabled, make sure to increase this value, as more MaxScale replicas implies more connections.It defaults to 30 times the number of MaxScale replicas. |  |  |
| monitorUsername string | MonitorUsername is the user used by MaxScale monitor to connect to MariaDB server. It is defaulted if not provided. |  |  |
| monitorPasswordSecretKeyRef [GeneratedSecretKeyRef](#generatedsecretkeyref) | MonitorPasswordSecretKeyRef is Secret key reference to the password used by MaxScale monitor to connect to MariaDB server. It is defaulted if not provided.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password. |  |  |
| monitorMaxConnections integer | MonitorMaxConnections defines the maximum number of connections that the monitor can establish.If HA is enabled, make sure to increase this value, as more MaxScale replicas implies more connections.It defaults to 30 times the number of MaxScale replicas. |  |  |
| syncUsername string | MonitoSyncUsernamerUsername is the user used by MaxScale config sync to connect to MariaDB server. It is defaulted when HA is enabled. |  |  |
| syncPasswordSecretKeyRef [GeneratedSecretKeyRef](#generatedsecretkeyref) | SyncPasswordSecretKeyRef is Secret key reference to the password used by MaxScale config to connect to MariaDB server. It is defaulted when HA is enabled.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password. |  |  |
| syncMaxConnections integer | SyncMaxConnections defines the maximum number of connections that the sync can establish.If HA is enabled, make sure to increase this value, as more MaxScale replicas implies more connections.It defaults to 30 times the number of MaxScale replicas. |  |  |


#### MaxScaleConfig


MaxScaleConfig defines the MaxScale configuration.


*Appears in:*
- [MariaDBMaxScaleSpec](#mariadbmaxscalespec)
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| params object (keys:string, values:string) | Params is a key value pair of parameters to be used in the MaxScale static configuration file.Any parameter supported by MaxScale may be specified here. See reference:[#global-settings](https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-maxscale-configuration-guide/#global-settings). |  |  |
| volumeClaimTemplate [VolumeClaimTemplate](#volumeclaimtemplate) | VolumeClaimTemplate provides a template to define the PVCs for storing MaxScale runtime configuration files. It is defaulted if not provided. |  |  |
| sync [MaxScaleConfigSync](#maxscaleconfigsync) | Sync defines how to replicate configuration across MaxScale replicas. It is defaulted when HA is enabled. |  |  |


#### MaxScaleConfigSync


MaxScaleConfigSync defines how the config changes are replicated across replicas.


*Appears in:*
- [MaxScaleConfig](#maxscaleconfig)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| database string | Database is the MariaDB logical database where the 'maxscale_config' table will be created in order to persist and synchronize config changes. If not provided, it defaults to 'mysql'. |  |  |
| interval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | Interval defines the config synchronization interval. It is defaulted if not provided. |  |  |
| timeout [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | Interval defines the config synchronization timeout. It is defaulted if not provided. |  |  |


#### MaxScaleListener


MaxScaleListener defines how the MaxScale server will listen for connections.


*Appears in:*
- [MaxScaleService](#maxscaleservice)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| suspend boolean | Suspend indicates whether the current resource should be suspended or not.This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities. | false |  |
| name string | Name is the identifier of the listener. It is defaulted if not provided |  |  |
| port integer | Port is the network port where the MaxScale server will listen. |  | Required: {} |
| protocol string | Protocol is the MaxScale protocol to use when communicating with the client. If not provided, it defaults to MariaDBProtocol. |  |  |
| params object (keys:string, values:string) | Params defines extra parameters to pass to the listener.Any parameter supported by MaxScale may be specified here. See reference:[#listener_1](https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-maxscale-configuration-guide/#listener_1). |  |  |


#### MaxScaleMetrics


MaxScaleMetrics defines the metrics for a Maxscale.


*Appears in:*
- [MariaDBMaxScaleSpec](#mariadbmaxscalespec)
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| enabled boolean | Enabled is a flag to enable Metrics |  |  |
| exporter [Exporter](#exporter) | Exporter defines the metrics exporter container. |  |  |
| serviceMonitor [ServiceMonitor](#servicemonitor) | ServiceMonitor defines the ServiceMonior object. |  |  |


#### MaxScaleMonitor


MaxScaleMonitor monitors MariaDB server instances


*Appears in:*
- [MariaDBMaxScaleSpec](#mariadbmaxscalespec)
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| suspend boolean | Suspend indicates whether the current resource should be suspended or not.This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities. | false |  |
| name string | Name is the identifier of the monitor. It is defaulted if not provided. |  |  |
| module [MonitorModule](#monitormodule) | Module is the module to use to monitor MariaDB servers. It is mandatory when no MariaDB reference is provided. |  |  |
| interval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | Interval used to monitor MariaDB servers. It is defaulted if not provided. |  |  |
| cooperativeMonitoring [CooperativeMonitoring](#cooperativemonitoring) | CooperativeMonitoring enables coordination between multiple MaxScale instances running monitors. It is defaulted when HA is enabled. |  | Enum: [majority_of_all majority_of_running] |
| params object (keys:string, values:string) | Params defines extra parameters to pass to the monitor.Any parameter supported by MaxScale may be specified here. See reference:[https://mariadb.com/kb/en/mariadb-maxscale-2308-common-monitor-parameters/.Monitor](https://mariadb.com/kb/en/mariadb-maxscale-2308-common-monitor-parameters/.<br />Monitor) specific parameter are also suported:[https://mariadb.com/kb/en/mariadb-maxscale-2308-galera-monitor/#galera-monitor-optional-parameters.https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-monitor/#configuration](https://mariadb.com/kb/en/mariadb-maxscale-2308-galera-monitor/#galera-monitor-optional-parameters.<br />https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-monitor/#configuration). |  |  |


#### MaxScalePodTemplate


MaxScalePodTemplate defines a template for MaxScale Pods.


*Appears in:*
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| podMetadata [Metadata](#metadata) | PodMetadata defines extra metadata for the Pod. |  |  |
| imagePullSecrets [LocalObjectReference](#localobjectreference) array | ImagePullSecrets is the list of pull Secrets to be used to pull the image. |  |  |
| podSecurityContext [PodSecurityContext](#podsecuritycontext) | SecurityContext holds pod-level security attributes and common container settings. |  |  |
| serviceAccountName string | ServiceAccountName is the name of the ServiceAccount to be used by the Pods. |  |  |
| affinity [AffinityConfig](#affinityconfig) | Affinity to be used in the Pod. |  |  |
| nodeSelector object (keys:string, values:string) | NodeSelector to be used in the Pod. |  |  |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array | Tolerations to be used in the Pod. |  |  |
| priorityClassName string | PriorityClassName to be used in the Pod. |  |  |
| topologySpreadConstraints [TopologySpreadConstraint](#topologyspreadconstraint) array | TopologySpreadConstraints to be used in the Pod. |  |  |


#### MaxScaleServer


MaxScaleServer defines a MariaDB server to forward traffic to.


*Appears in:*
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| name string | Name is the identifier of the MariaDB server. |  | Required: {} |
| address string | Address is the network address of the MariaDB server. |  | Required: {} |
| port integer | Port is the network port of the MariaDB server. If not provided, it defaults to 3306. |  |  |
| protocol string | Protocol is the MaxScale protocol to use when communicating with this MariaDB server. If not provided, it defaults to MariaDBBackend. |  |  |
| maintenance boolean | Maintenance indicates whether the server is in maintenance mode. |  |  |
| params object (keys:string, values:string) | Params defines extra parameters to pass to the server.Any parameter supported by MaxScale may be specified here. See reference:[#server_1](https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-maxscale-configuration-guide/#server_1). |  |  |


#### MaxScaleService


Services define how the traffic is forwarded to the MariaDB servers.


*Appears in:*
- [MariaDBMaxScaleSpec](#mariadbmaxscalespec)
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| suspend boolean | Suspend indicates whether the current resource should be suspended or not.This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities. | false |  |
| name string | Name is the identifier of the MaxScale service. |  | Required: {} |
| router [ServiceRouter](#servicerouter) | Router is the type of router to use. |  | Enum: [readwritesplit readconnroute] Required: {} |
| listener [MaxScaleListener](#maxscalelistener) | MaxScaleListener defines how the MaxScale server will listen for connections. |  | Required: {} |
| params object (keys:string, values:string) | Params defines extra parameters to pass to the service.Any parameter supported by MaxScale may be specified here. See reference:[https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-maxscale-configuration-guide/#service_1.Router](https://mariadb.com/kb/en/mariadb-maxscale-2308-mariadb-maxscale-configuration-guide/#service_1.<br />Router) specific parameter are also suported:[https://mariadb.com/kb/en/mariadb-maxscale-2308-readwritesplit/#configuration.https://mariadb.com/kb/en/mariadb-maxscale-2308-readconnroute/#configuration](https://mariadb.com/kb/en/mariadb-maxscale-2308-readwritesplit/#configuration.<br />https://mariadb.com/kb/en/mariadb-maxscale-2308-readconnroute/#configuration). |  |  |


#### MaxScaleSpec


MaxScaleSpec defines the desired state of MaxScale.


*Appears in:*
- [MaxScale](#maxscale)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| command string array | Command to be used in the Container. |  |  |
| args string array | Args to be used in the Container. |  |  |
| env [EnvVar](#envvar) array | Env represents the environment variables to be injected in a container. |  |  |
| envFrom [EnvFromSource](#envfromsource) array | EnvFrom represents the references (via ConfigMap and Secrets) to environment variables to be injected in the container. |  |  |
| volumeMounts [VolumeMount](#volumemount) array | VolumeMounts to be used in the Container. |  |  |
| livenessProbe [Probe](#probe) | LivenessProbe to be used in the Container. |  |  |
| readinessProbe [Probe](#probe) | ReadinessProbe to be used in the Container. |  |  |
| startupProbe [Probe](#probe) | StartupProbe to be used in the Container. |  |  |
| resources [ResourceRequirements](#resourcerequirements) | Resouces describes the compute resource requirements. |  |  |
| securityContext [SecurityContext](#securitycontext) | SecurityContext holds security configuration that will be applied to a container. |  |  |
| podMetadata [Metadata](#metadata) | PodMetadata defines extra metadata for the Pod. |  |  |
| imagePullSecrets [LocalObjectReference](#localobjectreference) array | ImagePullSecrets is the list of pull Secrets to be used to pull the image. |  |  |
| podSecurityContext [PodSecurityContext](#podsecuritycontext) | SecurityContext holds pod-level security attributes and common container settings. |  |  |
| serviceAccountName string | ServiceAccountName is the name of the ServiceAccount to be used by the Pods. |  |  |
| affinity [AffinityConfig](#affinityconfig) | Affinity to be used in the Pod. |  |  |
| nodeSelector object (keys:string, values:string) | NodeSelector to be used in the Pod. |  |  |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array | Tolerations to be used in the Pod. |  |  |
| priorityClassName string | PriorityClassName to be used in the Pod. |  |  |
| topologySpreadConstraints [TopologySpreadConstraint](#topologyspreadconstraint) array | TopologySpreadConstraints to be used in the Pod. |  |  |
| suspend boolean | Suspend indicates whether the current resource should be suspended or not.This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities. | false |  |
| mariaDbRef [MariaDBRef](#mariadbref) | MariaDBRef is a reference to the MariaDB that MaxScale points to. It is used to initialize the servers field. |  |  |
| servers [MaxScaleServer](#maxscaleserver) array | Servers are the MariaDB servers to forward traffic to. It is required if 'spec.mariaDbRef' is not provided. |  |  |
| image string | Image name to be used by the MaxScale instances. The supported format is <image>:<tag>.Only MaxScale official images are supported. |  |  |
| imagePullPolicy [PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#pullpolicy-v1-core) | ImagePullPolicy is the image pull policy. One of Always, Never or IfNotPresent. If not defined, it defaults to IfNotPresent. |  | Enum: [Always Never IfNotPresent] |
| inheritMetadata [Metadata](#metadata) | InheritMetadata defines the metadata to be inherited by children resources. |  |  |
| services [MaxScaleService](#maxscaleservice) array | Services define how the traffic is forwarded to the MariaDB servers. It is defaulted if not provided. |  |  |
| monitor [MaxScaleMonitor](#maxscalemonitor) | Monitor monitors MariaDB server instances. It is required if 'spec.mariaDbRef' is not provided. |  |  |
| admin [MaxScaleAdmin](#maxscaleadmin) | Admin configures the admin REST API and GUI. |  |  |
| config [MaxScaleConfig](#maxscaleconfig) | Config defines the MaxScale configuration. |  |  |
| auth [MaxScaleAuth](#maxscaleauth) | Auth defines the credentials required for MaxScale to connect to MariaDB. |  |  |
| metrics [MaxScaleMetrics](#maxscalemetrics) | Metrics configures metrics and how to scrape them. |  |  |
| tls [MaxScaleTLS](#maxscaletls) | TLS defines the PKI to be used with MaxScale. |  |  |
| connection [ConnectionTemplate](#connectiontemplate) | Connection provides a template to define the Connection for MaxScale. |  |  |
| replicas integer | Replicas indicates the number of desired instances. | 1 |  |
| podDisruptionBudget [PodDisruptionBudget](#poddisruptionbudget) | PodDisruptionBudget defines the budget for replica availability. |  |  |
| updateStrategy [StatefulSetUpdateStrategy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#statefulsetupdatestrategy-v1-apps) | UpdateStrategy defines the update strategy for the StatefulSet object. |  |  |
| kubernetesService [ServiceTemplate](#servicetemplate) | KubernetesService defines a template for a Kubernetes Service object to connect to MaxScale. |  |  |
| guiKubernetesService [ServiceTemplate](#servicetemplate) | GuiKubernetesService defines a template for a Kubernetes Service object to connect to MaxScale's GUI. |  |  |
| requeueInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | RequeueInterval is used to perform requeue reconciliations. If not defined, it defaults to 10s. |  |  |


#### MaxScaleTLS


TLS defines the PKI to be used with MaxScale.


*Appears in:*
- [MariaDBMaxScaleSpec](#mariadbmaxscalespec)
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| enabled boolean | Enabled indicates whether TLS is enabled, determining if certificates should be issued and mounted to the MaxScale instance.It is enabled by default when the referred MariaDB instance (via mariaDbRef) has TLS enabled and enforced. |  |  |
| adminVersions string array | Versions specifies the supported TLS versions in the MaxScale REST API.By default, the MaxScale's default supported versions are used. See: [mariadb-maxscale-25-mariadb-maxscale-configuration-guide#admin_ssl_version](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-25/maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide#admin_ssl_version) |  |  |
| serverVersions string array | ServerVersions specifies the supported TLS versions in both the servers and listeners managed by this MaxScale instance.By default, the MaxScale's default supported versions are used. See: [mariadb-maxscale-25-mariadb-maxscale-configuration-guide#ssl_version](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-25/maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide#ssl_version). |  |  |
| adminCASecretRef [LocalObjectReference](#localobjectreference) | AdminCASecretRef is a reference to a Secret containing the admin certificate authority keypair. It is used to establish trust and issue certificates for the MaxScale's administrative REST API and GUI.One of:- Secret containing both the 'ca.crt' and 'ca.key' keys. This allows you to bring your own CA to Kubernetes to issue certificates.- Secret containing only the 'ca.crt' in order to establish trust. In this case, either adminCertSecretRef or adminCertIssuerRef fields must be provided.If not provided, a self-signed CA will be provisioned to issue the server certificate. |  |  |
| adminCertSecretRef [LocalObjectReference](#localobjectreference) | AdminCertSecretRef is a reference to a TLS Secret used by the MaxScale's administrative REST API and GUI. |  |  |
| adminCertIssuerRef [ObjectReference](#objectreference) | AdminCertIssuerRef is a reference to a cert-manager issuer object used to issue the MaxScale's administrative REST API and GUI certificate. cert-manager must be installed previously in the cluster.It is mutually exclusive with adminCertSecretRef.By default, the Secret field 'ca.crt' provisioned by cert-manager will be added to the trust chain. A custom trust bundle may be specified via adminCASecretRef. |  |  |
| adminCertConfig [TLSConfig](#tlsconfig) | AdminCertConfig allows configuring the admin certificates, either issued by the operator or cert-manager.If not set, the default settings will be used. |  |  |
| listenerCASecretRef [LocalObjectReference](#localobjectreference) | ListenerCASecretRef is a reference to a Secret containing the listener certificate authority keypair. It is used to establish trust and issue certificates for the MaxScale's listeners.One of:- Secret containing both the 'ca.crt' and 'ca.key' keys. This allows you to bring your own CA to Kubernetes to issue certificates.- Secret containing only the 'ca.crt' in order to establish trust. In this case, either listenerCertSecretRef or listenerCertIssuerRef fields must be provided.If not provided, a self-signed CA will be provisioned to issue the listener certificate. |  |  |
| listenerCertSecretRef [LocalObjectReference](#localobjectreference) | ListenerCertSecretRef is a reference to a TLS Secret used by the MaxScale's listeners. |  |  |
| listenerCertIssuerRef [ObjectReference](#objectreference) | ListenerCertIssuerRef is a reference to a cert-manager issuer object used to issue the MaxScale's listeners certificate. cert-manager must be installed previously in the cluster.It is mutually exclusive with listenerCertSecretRef.By default, the Secret field 'ca.crt' provisioned by cert-manager will be added to the trust chain. A custom trust bundle may be specified via listenerCASecretRef. |  |  |
| listenerCertConfig [TLSConfig](#tlsconfig) | ListenerCertConfig allows configuring the listener certificates, either issued by the operator or cert-manager.If not set, the default settings will be used. |  |  |
| serverCASecretRef [LocalObjectReference](#localobjectreference) | ServerCASecretRef is a reference to a Secret containing the MariaDB server CA certificates. It is used to establish trust with MariaDB servers.The Secret should contain a 'ca.crt' key in order to establish trust.If not provided, and the reference to a MariaDB resource is set (mariaDbRef), it will be defaulted to the referred MariaDB CA bundle. |  |  |
| serverCertSecretRef [LocalObjectReference](#localobjectreference) | ServerCertSecretRef is a reference to a TLS Secret used by MaxScale to connect to the MariaDB servers.If not provided, and the reference to a MariaDB resource is set (mariaDbRef), it will be defaulted to the referred MariaDB client certificate (clientCertSecretRef). |  |  |
| verifyPeerCertificate boolean | VerifyPeerCertificate specifies whether the peer certificate's signature should be validated against the CA.It is disabled by default. |  |  |
| verifyPeerHost boolean | VerifyPeerHost specifies whether the peer certificate's SANs should match the peer host.It is disabled by default. |  |  |
| replicationSSLEnabled boolean | ReplicationSSLEnabled specifies whether the replication SSL is enabled. If enabled, the SSL options will be added to the server configuration.It is enabled by default when the referred MariaDB instance (via mariaDbRef) has replication enabled.If the MariaDB servers are manually provided by the user via the 'servers' field, this must be set by the user as well. |  |  |


#### Metadata


Metadata defines the metadata to added to resources.


*Appears in:*
- [BackupSpec](#backupspec)
- [Exporter](#exporter)
- [GaleraInitJob](#galerainitjob)
- [GaleraRecoveryJob](#galerarecoveryjob)
- [Job](#job)
- [JobPodTemplate](#jobpodtemplate)
- [MariaDBSpec](#mariadbspec)
- [MaxScalePodTemplate](#maxscalepodtemplate)
- [MaxScaleSpec](#maxscalespec)
- [PodTemplate](#podtemplate)
- [RestoreSpec](#restorespec)
- [SecretTemplate](#secrettemplate)
- [ServiceTemplate](#servicetemplate)
- [SqlJobSpec](#sqljobspec)
- [VolumeClaimTemplate](#volumeclaimtemplate)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| labels object (keys:string, values:string) | Labels to be added to children resources. |  |  |
| annotations object (keys:string, values:string) | Annotations to be added to children resources. |  |  |


#### MonitorModule


*Underlying type:* *string*


MonitorModule defines the type of monitor module


*Appears in:*
- [MaxScaleMonitor](#maxscalemonitor)


| Field | Description |
| --- | --- |
| Field | Description |
| mariadbmon | MonitorModuleMariadb is a monitor to be used with MariaDB servers. |
| galeramon | MonitorModuleGalera is a monitor to be used with Galera servers. |


#### NFSVolumeSource


Refer to the Kubernetes docs: [#nfsvolumesource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#nfsvolumesource-v1-core).


*Appears in:*
- [StorageVolumeSource](#storagevolumesource)
- [Volume](#volume)
- [VolumeSource](#volumesource)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| server string |  |  |  |
| path string |  |  |  |
| readOnly boolean |  |  |  |


#### NodeAffinity


Refer to the Kubernetes docs: [#nodeaffinity-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#nodeaffinity-v1-core)


*Appears in:*
- [Affinity](#affinity)
- [AffinityConfig](#affinityconfig)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| requiredDuringSchedulingIgnoredDuringExecution [NodeSelector](#nodeselector) |  |  |  |
| preferredDuringSchedulingIgnoredDuringExecution [PreferredSchedulingTerm](#preferredschedulingterm) array |  |  |  |


#### NodeSelector


Refer to the Kubernetes docs: [#nodeselector-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#nodeselector-v1-core)


*Appears in:*
- [NodeAffinity](#nodeaffinity)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| nodeSelectorTerms [NodeSelectorTerm](#nodeselectorterm) array |  |  |  |


#### NodeSelectorTerm


*Underlying type:* *[struct{MatchExpressions []NodeSelectorRequirement "json:\"matchExpressions,omitempty\""; MatchFields []NodeSelectorRequirement "json:\"matchFields,omitempty\""}](#struct{matchexpressions-[]nodeselectorrequirement-"json:\"matchexpressions,omitempty\"";-matchfields-[]nodeselectorrequirement-"json:\"matchfields,omitempty\""})*


Refer to the Kubernetes docs: [#nodeselectorterm-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#nodeselectorterm-v1-core)


*Appears in:*
- [NodeSelector](#nodeselector)
- [PreferredSchedulingTerm](#preferredschedulingterm)


#### ObjectFieldSelector


Refer to the Kubernetes docs: [#objectfieldselector-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectfieldselector-v1-core).


*Appears in:*
- [EnvVarSource](#envvarsource)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| apiVersion string |  |  |  |
| fieldPath string |  |  |  |


#### ObjectReference


Refer to the Kubernetes docs: [#objectreference-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectreference-v1-core).


*Appears in:*
- [ConnectionSpec](#connectionspec)
- [MariaDBRef](#mariadbref)
- [MariaDBSpec](#mariadbspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| name string |  |  |  |
| namespace string |  |  |  |


#### PasswordPlugin


PasswordPlugin defines the password plugin and its arguments.


*Appears in:*
- [MariaDBSpec](#mariadbspec)
- [UserSpec](#userspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| pluginNameSecretKeyRef [SecretKeySelector](#secretkeyselector) | PluginNameSecretKeyRef is a reference to the authentication plugin to be used by the User.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the authentication plugin. |  |  |
| pluginArgSecretKeyRef [SecretKeySelector](#secretkeyselector) | PluginArgSecretKeyRef is a reference to the arguments to be provided to the authentication plugin for the User.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the authentication plugin arguments. |  |  |


#### PersistentVolumeClaimSpec


Refer to the Kubernetes docs: [#persistentvolumeclaimspec-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#persistentvolumeclaimspec-v1-core).


*Appears in:*
- [BackupStagingStorage](#backupstagingstorage)
- [BackupStorage](#backupstorage)
- [VolumeClaimTemplate](#volumeclaimtemplate)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| accessModes [PersistentVolumeAccessMode](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#persistentvolumeaccessmode-v1-core) array |  |  |  |
| selector [LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#labelselector-v1-meta) |  |  |  |
| resources [VolumeResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#volumeresourcerequirements-v1-core) |  |  |  |
| storageClassName string |  |  |  |


#### PersistentVolumeClaimVolumeSource


Refer to the Kubernetes docs: [#persistentvolumeclaimvolumesource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#persistentvolumeclaimvolumesource-v1-core).


*Appears in:*
- [StorageVolumeSource](#storagevolumesource)
- [Volume](#volume)
- [VolumeSource](#volumesource)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| claimName string |  |  |  |
| readOnly boolean |  |  |  |


#### PodAffinityTerm


Refer to the Kubernetes docs: [#podaffinityterm-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#podaffinityterm-v1-core).


*Appears in:*
- [PodAntiAffinity](#podantiaffinity)
- [WeightedPodAffinityTerm](#weightedpodaffinityterm)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| labelSelector [LabelSelector](#labelselector) |  |  |  |
| topologyKey string |  |  |  |


#### PodAntiAffinity


Refer to the Kubernetes docs: [#podantiaffinity-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#podantiaffinity-v1-core).


*Appears in:*
- [Affinity](#affinity)
- [AffinityConfig](#affinityconfig)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| requiredDuringSchedulingIgnoredDuringExecution [PodAffinityTerm](#podaffinityterm) array |  |  |  |
| preferredDuringSchedulingIgnoredDuringExecution [WeightedPodAffinityTerm](#weightedpodaffinityterm) array |  |  |  |


#### PodDisruptionBudget


PodDisruptionBudget is the Pod availability bundget for a MariaDB


*Appears in:*
- [MariaDBMaxScaleSpec](#mariadbmaxscalespec)
- [MariaDBSpec](#mariadbspec)
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| minAvailable [IntOrString](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#intorstring-intstr-util) | MinAvailable defines the number of minimum available Pods. |  |  |
| maxUnavailable [IntOrString](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#intorstring-intstr-util) | MaxUnavailable defines the number of maximum unavailable Pods. |  |  |


#### PodSecurityContext


Refer to the Kubernetes docs: [#podsecuritycontext-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#podsecuritycontext-v1-core)


*Appears in:*
- [BackupSpec](#backupspec)
- [Exporter](#exporter)
- [JobPodTemplate](#jobpodtemplate)
- [MariaDBSpec](#mariadbspec)
- [MaxScalePodTemplate](#maxscalepodtemplate)
- [MaxScaleSpec](#maxscalespec)
- [PodTemplate](#podtemplate)
- [RestoreSpec](#restorespec)
- [SqlJobSpec](#sqljobspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| seLinuxOptions [SELinuxOptions](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#selinuxoptions-v1-core) |  |  |  |
| runAsUser integer |  |  |  |
| runAsGroup integer |  |  |  |
| runAsNonRoot boolean |  |  |  |
| supplementalGroups integer array |  |  |  |
| fsGroup integer |  |  |  |
| fsGroupChangePolicy [PodFSGroupChangePolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#podfsgroupchangepolicy-v1-core) |  |  |  |
| seccompProfile [SeccompProfile](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#seccompprofile-v1-core) |  |  |  |
| appArmorProfile [AppArmorProfile](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#apparmorprofile-v1-core) |  |  |  |


#### PodTemplate


PodTemplate defines a template to configure Container objects.


*Appears in:*
- [MariaDBSpec](#mariadbspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| podMetadata [Metadata](#metadata) | PodMetadata defines extra metadata for the Pod. |  |  |
| imagePullSecrets [LocalObjectReference](#localobjectreference) array | ImagePullSecrets is the list of pull Secrets to be used to pull the image. |  |  |
| initContainers [Container](#container) array | InitContainers to be used in the Pod. |  |  |
| sidecarContainers [Container](#container) array | SidecarContainers to be used in the Pod. |  |  |
| podSecurityContext [PodSecurityContext](#podsecuritycontext) | SecurityContext holds pod-level security attributes and common container settings. |  |  |
| serviceAccountName string | ServiceAccountName is the name of the ServiceAccount to be used by the Pods. |  |  |
| affinity [AffinityConfig](#affinityconfig) | Affinity to be used in the Pod. |  |  |
| nodeSelector object (keys:string, values:string) | NodeSelector to be used in the Pod. |  |  |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array | Tolerations to be used in the Pod. |  |  |
| volumes [Volume](#volume) array | Volumes to be used in the Pod. |  |  |
| priorityClassName string | PriorityClassName to be used in the Pod. |  |  |
| topologySpreadConstraints [TopologySpreadConstraint](#topologyspreadconstraint) array | TopologySpreadConstraints to be used in the Pod. |  |  |


#### PreferredSchedulingTerm


Refer to the Kubernetes docs: [#preferredschedulingterm-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#preferredschedulingterm-v1-core)


*Appears in:*
- [NodeAffinity](#nodeaffinity)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| weight integer |  |  |  |
| preference [NodeSelectorTerm](#nodeselectorterm) |  |  |  |


#### PrimaryGalera


PrimaryGalera is the Galera configuration for the primary node.


*Appears in:*
- [Galera](#galera)
- [GaleraSpec](#galeraspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| podIndex integer | PodIndex is the StatefulSet index of the primary node. The user may change this field to perform a manual switchover. |  |  |
| automaticFailover boolean | AutomaticFailover indicates whether the operator should automatically update PodIndex to perform an automatic primary failover. |  |  |


#### Probe


Refer to the Kubernetes docs: [#probe-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#probe-v1-core).


*Appears in:*
- [ContainerTemplate](#containertemplate)
- [GaleraAgent](#galeraagent)
- [GaleraInit](#galerainit)
- [MariaDBSpec](#mariadbspec)
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| exec [ExecAction](#execaction) |  |  |  |
| httpGet [HTTPGetAction](#httpgetaction) |  |  |  |
| tcpSocket [TCPSocketAction](#tcpsocketaction) |  |  |  |
| initialDelaySeconds integer |  |  |  |
| timeoutSeconds integer |  |  |  |
| periodSeconds integer |  |  |  |
| successThreshold integer |  |  |  |
| failureThreshold integer |  |  |  |


#### ProbeHandler


Refer to the Kubernetes docs: [#probe-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#probe-v1-core).


*Appears in:*
- [Probe](#probe)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| exec [ExecAction](#execaction) |  |  |  |
| httpGet [HTTPGetAction](#httpgetaction) |  |  |  |
| tcpSocket [TCPSocketAction](#tcpsocketaction) |  |  |  |


#### ResourceRequirements


Refer to the Kubernetes docs: [#resourcerequirements-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcerequirements-v1-core).


*Appears in:*
- [BackupSpec](#backupspec)
- [Container](#container)
- [ContainerTemplate](#containertemplate)
- [Exporter](#exporter)
- [GaleraAgent](#galeraagent)
- [GaleraInit](#galerainit)
- [GaleraInitJob](#galerainitjob)
- [GaleraRecoveryJob](#galerarecoveryjob)
- [Job](#job)
- [JobContainerTemplate](#jobcontainertemplate)
- [MariaDBSpec](#mariadbspec)
- [MaxScaleSpec](#maxscalespec)
- [RestoreSpec](#restorespec)
- [SqlJobSpec](#sqljobspec)


#### Restore


Restore is the Schema for the restores API. It is used to define restore jobs and its restoration source.


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| apiVersion string | enterprise.mariadb.com/v1alpha1 |  |  |
| kind string | Restore |  |  |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |  |  |
| spec [RestoreSpec](#restorespec) |  |  |  |


#### RestoreSource


RestoreSource defines a source for restoring a MariaDB.


*Appears in:*
- [BootstrapFrom](#bootstrapfrom)
- [RestoreSpec](#restorespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| backupRef [LocalObjectReference](#localobjectreference) | BackupRef is a reference to a Backup object. It has priority over S3 and Volume. |  |  |
| s3 [S3](#s3) | S3 defines the configuration to restore backups from a S3 compatible storage. It has priority over Volume. |  |  |
| volume [StorageVolumeSource](#storagevolumesource) | Volume is a Kubernetes Volume object that contains a backup. |  |  |
| targetRecoveryTime [Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#time-v1-meta) | TargetRecoveryTime is a RFC3339 (1970-01-01T00:00:00Z) date and time that defines the point in time recovery objective.It is used to determine the closest restoration source in time. |  |  |
| stagingStorage [BackupStagingStorage](#backupstagingstorage) | StagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.It defaults to an emptyDir volume, meaning that the backups will be temporarily stored in the node where the Restore Job is scheduled. |  |  |


#### RestoreSpec


RestoreSpec defines the desired state of restore


*Appears in:*
- [Restore](#restore)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| args string array | Args to be used in the Container. |  |  |
| resources [ResourceRequirements](#resourcerequirements) | Resouces describes the compute resource requirements. |  |  |
| securityContext [SecurityContext](#securitycontext) | SecurityContext holds security configuration that will be applied to a container. |  |  |
| podMetadata [Metadata](#metadata) | PodMetadata defines extra metadata for the Pod. |  |  |
| imagePullSecrets [LocalObjectReference](#localobjectreference) array | ImagePullSecrets is the list of pull Secrets to be used to pull the image. |  |  |
| podSecurityContext [PodSecurityContext](#podsecuritycontext) | SecurityContext holds pod-level security attributes and common container settings. |  |  |
| serviceAccountName string | ServiceAccountName is the name of the ServiceAccount to be used by the Pods. |  |  |
| affinity [AffinityConfig](#affinityconfig) | Affinity to be used in the Pod. |  |  |
| nodeSelector object (keys:string, values:string) | NodeSelector to be used in the Pod. |  |  |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array | Tolerations to be used in the Pod. |  |  |
| priorityClassName string | PriorityClassName to be used in the Pod. |  |  |
| backupRef [LocalObjectReference](#localobjectreference) | BackupRef is a reference to a Backup object. It has priority over S3 and Volume. |  |  |
| s3 [S3](#s3) | S3 defines the configuration to restore backups from a S3 compatible storage. It has priority over Volume. |  |  |
| volume [StorageVolumeSource](#storagevolumesource) | Volume is a Kubernetes Volume object that contains a backup. |  |  |
| targetRecoveryTime [Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#time-v1-meta) | TargetRecoveryTime is a RFC3339 (1970-01-01T00:00:00Z) date and time that defines the point in time recovery objective.It is used to determine the closest restoration source in time. |  |  |
| stagingStorage [BackupStagingStorage](#backupstagingstorage) | StagingStorage defines the temporary storage used to keep external backups (i.e. S3) while they are being processed.It defaults to an emptyDir volume, meaning that the backups will be temporarily stored in the node where the Restore Job is scheduled. |  |  |
| mariaDbRef [MariaDBRef](#mariadbref) | MariaDBRef is a reference to a MariaDB object. |  | Required: {} |
| database string | Database defines the logical database to be restored. If not provided, all databases available in the backup are restored.IMPORTANT: The database must previously exist. |  |  |
| logLevel string | LogLevel to be used n the Backup Job. It defaults to 'info'. | info |  |
| backoffLimit integer | BackoffLimit defines the maximum number of attempts to successfully perform a Backup. | 5 |  |
| restartPolicy [RestartPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#restartpolicy-v1-core) | RestartPolicy to be added to the Backup Job. | OnFailure | Enum: [Always OnFailure Never] |
| inheritMetadata [Metadata](#metadata) | InheritMetadata defines the metadata to be inherited by children resources. |  |  |


#### S3


*Appears in:*
- [BackupStorage](#backupstorage)
- [BootstrapFrom](#bootstrapfrom)
- [RestoreSource](#restoresource)
- [RestoreSpec](#restorespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| bucket string | Bucket is the name Name of the bucket to store backups. |  | Required: {} |
| endpoint string | Endpoint is the S3 API endpoint without scheme. |  | Required: {} |
| region string | Region is the S3 region name to use. |  |  |
| prefix string | Prefix indicates a folder/subfolder in the bucket. For example: mariadb/ or mariadb/backups. A trailing slash '/' is added if not provided. |  |  |
| accessKeyIdSecretKeyRef [SecretKeySelector](#secretkeyselector) | AccessKeyIdSecretKeyRef is a reference to a Secret key containing the S3 access key id. |  |  |
| secretAccessKeySecretKeyRef [SecretKeySelector](#secretkeyselector) | AccessKeyIdSecretKeyRef is a reference to a Secret key containing the S3 secret key. |  |  |
| sessionTokenSecretKeyRef [SecretKeySelector](#secretkeyselector) | SessionTokenSecretKeyRef is a reference to a Secret key containing the S3 session token. |  |  |
| tls [TLSS3](#tlss3) | TLS provides the configuration required to establish TLS connections with S3. |  |  |


#### SQLTemplate


SQLTemplate defines a template to customize SQL objects.


*Appears in:*
- [DatabaseSpec](#databasespec)
- [GrantSpec](#grantspec)
- [UserSpec](#userspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| requeueInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | RequeueInterval is used to perform requeue reconciliations. |  |  |
| retryInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | RetryInterval is the interval used to perform retries. |  |  |
| cleanupPolicy [CleanupPolicy](#cleanuppolicy) | CleanupPolicy defines the behavior for cleaning up a SQL resource. |  | Enum: [Skip Delete] |


#### SST


*Underlying type:* *string*


SST is the Snapshot State Transfer used when new Pods join the cluster.
More info: [sst.html](https://galeracluster.com/library/documentation/sst.html).


*Appears in:*
- [Galera](#galera)
- [GaleraSpec](#galeraspec)


| Field | Description |
| --- | --- |
| Field | Description |
| rsync | SSTRsync is an SST based on rsync. |
| mariabackup | SSTMariaBackup is an SST based on mariabackup. It is the recommended SST. |
| mysqldump | SSTMysqldump is an SST based on mysqldump. |


#### Schedule


Schedule contains parameters to define a schedule


*Appears in:*
- [BackupSpec](#backupspec)
- [SqlJobSpec](#sqljobspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| cron string | Cron is a cron expression that defines the schedule. |  | Required: {} |
| suspend boolean | Suspend defines whether the schedule is active or not. | false |  |


#### SecretKeySelector


Refer to the Kubernetes docs: [#secretkeyselector-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#secretkeyselector-v1-core).


*Appears in:*
- [ConnectionSpec](#connectionspec)
- [EnvVarSource](#envvarsource)
- [GeneratedSecretKeyRef](#generatedsecretkeyref)
- [MariaDBSpec](#mariadbspec)
- [PasswordPlugin](#passwordplugin)
- [S3](#s3)
- [SqlJobSpec](#sqljobspec)
- [TLSS3](#tlss3)
- [UserSpec](#userspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| name string |  |  |  |
| key string |  |  |  |


#### SecretTemplate


SecretTemplate defines a template to customize Secret objects.


*Appears in:*
- [ConnectionSpec](#connectionspec)
- [ConnectionTemplate](#connectiontemplate)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| metadata [Metadata](#metadata) | Refer to Kubernetes API documentation for fields of metadata. |  |  |
| key string | Key to be used in the Secret. |  |  |
| format string | Format to be used in the Secret. |  |  |
| usernameKey string | UsernameKey to be used in the Secret. |  |  |
| passwordKey string | PasswordKey to be used in the Secret. |  |  |
| hostKey string | HostKey to be used in the Secret. |  |  |
| portKey string | PortKey to be used in the Secret. |  |  |
| databaseKey string | DatabaseKey to be used in the Secret. |  |  |


#### SecretVolumeSource


Refer to the Kubernetes docs: [#secretvolumesource-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#secretvolumesource-v1-core).


*Appears in:*
- [Volume](#volume)
- [VolumeSource](#volumesource)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| secretName string |  |  |  |
| defaultMode integer |  |  |  |


#### SecurityContext


Refer to the Kubernetes docs: [#securitycontext-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#securitycontext-v1-core).


*Appears in:*
- [BackupSpec](#backupspec)
- [ContainerTemplate](#containertemplate)
- [Exporter](#exporter)
- [GaleraAgent](#galeraagent)
- [GaleraInit](#galerainit)
- [JobContainerTemplate](#jobcontainertemplate)
- [MariaDBSpec](#mariadbspec)
- [MaxScaleSpec](#maxscalespec)
- [RestoreSpec](#restorespec)
- [SqlJobSpec](#sqljobspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| capabilities [Capabilities](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#capabilities-v1-core) |  |  |  |
| privileged boolean |  |  |  |
| runAsUser integer |  |  |  |
| runAsGroup integer |  |  |  |
| runAsNonRoot boolean |  |  |  |
| readOnlyRootFilesystem boolean |  |  |  |
| allowPrivilegeEscalation boolean |  |  |  |


#### ServiceMonitor


ServiceMonitor defines a prometheus ServiceMonitor object.


*Appears in:*
- [MariadbMetrics](#mariadbmetrics)
- [MaxScaleMetrics](#maxscalemetrics)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| prometheusRelease string | PrometheusRelease is the release label to add to the ServiceMonitor object. |  |  |
| jobLabel string | JobLabel to add to the ServiceMonitor object. |  |  |
| interval string | Interval for scraping metrics. |  |  |
| scrapeTimeout string | ScrapeTimeout defines the timeout for scraping metrics. |  |  |


#### ServicePort


Refer to the Kubernetes docs: [#serviceport-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#serviceport-v1-core)


*Appears in:*
- [MariaDBSpec](#mariadbspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| name string |  |  |  |
| port integer |  |  |  |


#### ServiceRouter


*Underlying type:* *string*


ServiceRouter defines the type of service router.


*Appears in:*
- [MaxScaleService](#maxscaleservice)


| Field | Description |
| --- | --- |
| Field | Description |
| readwritesplit | ServiceRouterReadWriteSplit splits the load based on the queries. Write queries are performed on master and read queries on the replicas. |
| readconnroute | ServiceRouterReadConnRoute splits the load based on the connections. Each connection is assigned to a server. |


#### ServiceTemplate


ServiceTemplate defines a template to customize Service objects.


*Appears in:*
- [MariaDBMaxScaleSpec](#mariadbmaxscalespec)
- [MariaDBSpec](#mariadbspec)
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| type [ServiceType](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#servicetype-v1-core) | Type is the Service type. One of ClusterIP, NodePort or LoadBalancer. If not defined, it defaults to ClusterIP. | ClusterIP | Enum: [ClusterIP NodePort LoadBalancer] |
| metadata [Metadata](#metadata) | Refer to Kubernetes API documentation for fields of metadata. |  |  |
| loadBalancerIP string | LoadBalancerIP Service field. |  |  |
| loadBalancerSourceRanges string array | LoadBalancerSourceRanges Service field. |  |  |
| externalTrafficPolicy [ServiceExternalTrafficPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#serviceexternaltrafficpolicy-v1-core) | ExternalTrafficPolicy Service field. |  |  |
| sessionAffinity [ServiceAffinity](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#serviceaffinity-v1-core) | SessionAffinity Service field. |  |  |
| allocateLoadBalancerNodePorts boolean | AllocateLoadBalancerNodePorts Service field. |  |  |


#### SqlJob


SqlJob is the Schema for the sqljobs API. It is used to run sql scripts as jobs.


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| apiVersion string | enterprise.mariadb.com/v1alpha1 |  |  |
| kind string | SqlJob |  |  |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |  |  |
| spec [SqlJobSpec](#sqljobspec) |  |  |  |


#### SqlJobSpec


SqlJobSpec defines the desired state of SqlJob


*Appears in:*
- [SqlJob](#sqljob)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| args string array | Args to be used in the Container. |  |  |
| resources [ResourceRequirements](#resourcerequirements) | Resouces describes the compute resource requirements. |  |  |
| securityContext [SecurityContext](#securitycontext) | SecurityContext holds security configuration that will be applied to a container. |  |  |
| podMetadata [Metadata](#metadata) | PodMetadata defines extra metadata for the Pod. |  |  |
| imagePullSecrets [LocalObjectReference](#localobjectreference) array | ImagePullSecrets is the list of pull Secrets to be used to pull the image. |  |  |
| podSecurityContext [PodSecurityContext](#podsecuritycontext) | SecurityContext holds pod-level security attributes and common container settings. |  |  |
| serviceAccountName string | ServiceAccountName is the name of the ServiceAccount to be used by the Pods. |  |  |
| affinity [AffinityConfig](#affinityconfig) | Affinity to be used in the Pod. |  |  |
| nodeSelector object (keys:string, values:string) | NodeSelector to be used in the Pod. |  |  |
| tolerations [Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) array | Tolerations to be used in the Pod. |  |  |
| priorityClassName string | PriorityClassName to be used in the Pod. |  |  |
| successfulJobsHistoryLimit integer | SuccessfulJobsHistoryLimit defines the maximum number of successful Jobs to be displayed. |  | Minimum: 0 |
| failedJobsHistoryLimit integer | FailedJobsHistoryLimit defines the maximum number of failed Jobs to be displayed. |  | Minimum: 0 |
| timeZone string | TimeZone defines the timezone associated with the cron expression. |  |  |
| mariaDbRef [MariaDBRef](#mariadbref) | MariaDBRef is a reference to a MariaDB object. |  | Required: {} |
| schedule [Schedule](#schedule) | Schedule defines when the SqlJob will be executed. |  |  |
| username string | Username to be impersonated when executing the SqlJob. |  | Required: {} |
| passwordSecretKeyRef [SecretKeySelector](#secretkeyselector) | UserPasswordSecretKeyRef is a reference to the impersonated user's password to be used when executing the SqlJob. |  | Required: {} |
| tlsCASecretRef [LocalObjectReference](#localobjectreference) | TLSCACertSecretRef is a reference toa CA Secret used to establish trust when executing the SqlJob.If not provided, the CA bundle provided by the referred MariaDB is used. |  |  |
| tlsClientCertSecretRef [LocalObjectReference](#localobjectreference) | TLSClientCertSecretRef is a reference to a Kubernetes TLS Secret used as authentication when executing the SqlJob.If not provided, the client certificate provided by the referred MariaDB is used. |  |  |
| database string | Username to be used when executing the SqlJob. |  |  |
| dependsOn [LocalObjectReference](#localobjectreference) array | DependsOn defines dependencies with other SqlJob objectecs. |  |  |
| sql string | Sql is the script to be executed by the SqlJob. |  |  |
| sqlConfigMapKeyRef [ConfigMapKeySelector](#configmapkeyselector) | SqlConfigMapKeyRef is a reference to a ConfigMap containing the Sql script.It is defaulted to a ConfigMap with the contents of the Sql field. |  |  |
| backoffLimit integer | BackoffLimit defines the maximum number of attempts to successfully execute a SqlJob. | 5 |  |
| restartPolicy [RestartPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#restartpolicy-v1-core) | RestartPolicy to be added to the SqlJob Pod. | OnFailure | Enum: [Always OnFailure Never] |
| inheritMetadata [Metadata](#metadata) | InheritMetadata defines the metadata to be inherited by children resources. |  |  |


#### Storage


Storage defines the storage options to be used for provisioning the PVCs mounted by MariaDB.


*Appears in:*
- [MariaDBSpec](#mariadbspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| ephemeral boolean | Ephemeral indicates whether to use ephemeral storage in the PVCs. It is only compatible with non HA MariaDBs. |  |  |
| size [Quantity](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#quantity-resource-api) | Size of the PVCs to be mounted by MariaDB. Required if not provided in 'VolumeClaimTemplate'. It supersedes the storage size specified in 'VolumeClaimTemplate'. |  |  |
| storageClassName string | StorageClassName to be used to provision the PVCS. It supersedes the 'StorageClassName' specified in 'VolumeClaimTemplate'.If not provided, the default 'StorageClass' configured in the cluster is used. |  |  |
| resizeInUseVolumes boolean | ResizeInUseVolumes indicates whether the PVCs can be resized. The 'StorageClassName' used should have 'allowVolumeExpansion' set to 'true' to allow resizing.It defaults to true. |  |  |
| waitForVolumeResize boolean | WaitForVolumeResize indicates whether to wait for the PVCs to be resized before marking the MariaDB object as ready. This will block other operations such as cluster recovery while the resize is in progress.It defaults to true. |  |  |
| volumeClaimTemplate [VolumeClaimTemplate](#volumeclaimtemplate) | VolumeClaimTemplate provides a template to define the PVCs. |  |  |


#### StorageVolumeSource


Refer to the Kubernetes docs: [#volume-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#volume-v1-core).


*Appears in:*
- [BackupStagingStorage](#backupstagingstorage)
- [BackupStorage](#backupstorage)
- [BootstrapFrom](#bootstrapfrom)
- [RestoreSource](#restoresource)
- [RestoreSpec](#restorespec)
- [Volume](#volume)
- [VolumeSource](#volumesource)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| emptyDir [EmptyDirVolumeSource](#emptydirvolumesource) |  |  |  |
| nfs [NFSVolumeSource](#nfsvolumesource) |  |  |  |
| csi [CSIVolumeSource](#csivolumesource) |  |  |  |
| hostPath [HostPathVolumeSource](#hostpathvolumesource) |  |  |  |
| persistentVolumeClaim [PersistentVolumeClaimVolumeSource](#persistentvolumeclaimvolumesource) |  |  |  |


#### SuspendTemplate


SuspendTemplate indicates whether the current resource should be suspended or not.


*Appears in:*
- [MariaDBSpec](#mariadbspec)
- [MaxScaleListener](#maxscalelistener)
- [MaxScaleMonitor](#maxscalemonitor)
- [MaxScaleService](#maxscaleservice)
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| suspend boolean | Suspend indicates whether the current resource should be suspended or not.This can be useful for maintenance, as disabling the reconciliation prevents the operator from interfering with user operations during maintenance activities. | false |  |


#### TCPSocketAction


Refer to the Kubernetes docs: [#tcpsocketaction-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#tcpsocketaction-v1-core).


*Appears in:*
- [Probe](#probe)
- [ProbeHandler](#probehandler)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| port [IntOrString](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#intorstring-intstr-util) |  |  |  |
| host string |  |  |  |


#### TLS


TLS defines the PKI to be used with MariaDB.


*Appears in:*
- [MariaDBSpec](#mariadbspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| enabled boolean | Enabled indicates whether TLS is enabled, determining if certificates should be issued and mounted to the MariaDB instance.It is enabled by default. |  |  |
| required boolean | Required specifies whether TLS must be enforced for all connections.User TLS requirements take precedence over this.It disabled by default. |  |  |
| versions string array | Versions specifies the supported TLS versions for this MariaDB instance.By default, the MariaDB's default supported versions are used. See: [ssltls-system-variables.md#tls_version](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#tls_version). |  |  |
| serverCASecretRef [LocalObjectReference](#localobjectreference) | ServerCASecretRef is a reference to a Secret containing the server certificate authority keypair. It is used to establish trust and issue server certificates.One of:- Secret containing both the 'ca.crt' and 'ca.key' keys. This allows you to bring your own CA to Kubernetes to issue certificates.- Secret containing only the 'ca.crt' in order to establish trust. In this case, either serverCertSecretRef or serverCertIssuerRef must be provided.If not provided, a self-signed CA will be provisioned to issue the server certificate. |  |  |
| serverCertSecretRef [LocalObjectReference](#localobjectreference) | ServerCertSecretRef is a reference to a TLS Secret containing the server certificate.It is mutually exclusive with serverCertIssuerRef. |  |  |
| serverCertIssuerRef [ObjectReference](#objectreference) | ServerCertIssuerRef is a reference to a cert-manager issuer object used to issue the server certificate. cert-manager must be installed previously in the cluster.It is mutually exclusive with serverCertSecretRef.By default, the Secret field 'ca.crt' provisioned by cert-manager will be added to the trust chain. A custom trust bundle may be specified via serverCASecretRef. |  |  |
| serverCertConfig [TLSConfig](#tlsconfig) | ServerCertConfig allows configuring the server certificates, either issued by the operator or cert-manager.If not set, the default settings will be used. |  |  |
| clientCASecretRef [LocalObjectReference](#localobjectreference) | ClientCASecretRef is a reference to a Secret containing the client certificate authority keypair. It is used to establish trust and issue client certificates.One of:- Secret containing both the 'ca.crt' and 'ca.key' keys. This allows you to bring your own CA to Kubernetes to issue certificates.- Secret containing only the 'ca.crt' in order to establish trust. In this case, either clientCertSecretRef or clientCertIssuerRef fields must be provided.If not provided, a self-signed CA will be provisioned to issue the client certificate. |  |  |
| clientCertSecretRef [LocalObjectReference](#localobjectreference) | ClientCertSecretRef is a reference to a TLS Secret containing the client certificate.It is mutually exclusive with clientCertIssuerRef. |  |  |
| clientCertIssuerRef [ObjectReference](#objectreference) | ClientCertIssuerRef is a reference to a cert-manager issuer object used to issue the client certificate. cert-manager must be installed previously in the cluster.It is mutually exclusive with clientCertSecretRef.By default, the Secret field 'ca.crt' provisioned by cert-manager will be added to the trust chain. A custom trust bundle may be specified via clientCASecretRef. |  |  |
| clientCertConfig [TLSConfig](#tlsconfig) | ClientCertConfig allows configuring the client certificates, either issued by the operator or cert-manager.If not set, the default settings will be used. |  |  |
| galeraSSTEnabled boolean | GaleraSSTEnabled determines whether Galera SST connections should use TLS.It disabled by default. |  |  |
| galeraServerSSLMode string | GaleraServerSSLMode defines the server SSL mode for a Galera Enterprise cluster.This field is only supported and applicable for Galera Enterprise >= 10.6 instances.Refer to the MariaDB Enterprise docs for more detail: [#WSREP_TLS_Modes](https://mariadb.com/docs/server/security/galera/#WSREP_TLS_Modes) |  | Enum: [PROVIDER SERVER SERVER_X509] |
| galeraClientSSLMode string | GaleraClientSSLMode defines the client SSL mode for a Galera Enterprise cluster.This field is only supported and applicable for Galera Enterprise >= 10.6 instances.Refer to the MariaDB Enterprise docs for more detail: [#SST_TLS_Modes](https://mariadb.com/docs/server/security/galera/#SST_TLS_Modes) |  | Enum: [DISABLED REQUIRED VERIFY_CA VERIFY_IDENTITY] |


#### TLSConfig


TLSConfig defines parameters to configure a certificate.


*Appears in:*
- [MaxScaleTLS](#maxscaletls)
- [TLS](#tls)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| caLifetime [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | CALifetime defines the CA certificate validity. |  |  |
| certLifetime [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | CertLifetime defines the certificate validity. |  |  |
| privateKeyAlgorithm string | PrivateKeyAlgorithm is the algorithm to be used for the CA and leaf certificate private keys.One of: ECDSA or RSA |  | Enum: [ECDSA RSA] |
| privateKeySize integer | PrivateKeyAlgorithm is the key size to be used for the CA and leaf certificate private keys.Supported values: ECDSA(256, 384, 521), RSA(2048, 3072, 4096) |  |  |


#### TLSRequirements


TLSRequirements specifies TLS requirements for the user to connect. See: [securing-connections-for-client-and-server.md#requiring-tls](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/securing-connections-for-client-and-server.md#requiring-tls).


*Appears in:*
- [UserSpec](#userspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| ssl boolean | SSL indicates that the user must connect via TLS. |  |  |
| x509 boolean | X509 indicates that the user must provide a valid x509 certificate to connect. |  |  |
| issuer string | Issuer indicates that the TLS certificate provided by the user must be issued by a specific issuer. |  |  |
| subject string | Subject indicates that the TLS certificate provided by the user must have a specific subject. |  |  |


#### TLSS3


*Appears in:*
- [S3](#s3)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| enabled boolean | Enabled is a flag to enable TLS. |  |  |
| caSecretKeyRef [SecretKeySelector](#secretkeyselector) | CASecretKeyRef is a reference to a Secret key containing a CA bundle in PEM format used to establish TLS connections with S3.By default, the system trust chain will be used, but you can use this field to add more CAs to the bundle. |  |  |


#### TopologySpreadConstraint


Refer to the Kubernetes docs: [#topologyspreadconstraint-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#topologyspreadconstraint-v1-core).


*Appears in:*
- [MariaDBSpec](#mariadbspec)
- [MaxScalePodTemplate](#maxscalepodtemplate)
- [MaxScaleSpec](#maxscalespec)
- [PodTemplate](#podtemplate)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| maxSkew integer |  |  |  |
| topologyKey string |  |  |  |
| whenUnsatisfiable [UnsatisfiableConstraintAction](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#unsatisfiableconstraintaction-v1-core) |  |  |  |
| labelSelector [LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#labelselector-v1-meta) |  |  |  |
| minDomains integer |  |  |  |
| nodeAffinityPolicy [NodeInclusionPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#nodeinclusionpolicy-v1-core) |  |  |  |
| nodeTaintsPolicy [NodeInclusionPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#nodeinclusionpolicy-v1-core) |  |  |  |
| matchLabelKeys string array |  |  |  |


#### UpdateStrategy


UpdateStrategy defines how a MariaDB resource is updated.


*Appears in:*
- [MariaDBSpec](#mariadbspec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| type [UpdateType](#updatetype) | Type defines the type of updates. One of ReplicasFirstPrimaryLast, RollingUpdate or OnDelete. If not defined, it defaults to ReplicasFirstPrimaryLast. | ReplicasFirstPrimaryLast | Enum: [ReplicasFirstPrimaryLast RollingUpdate OnDelete Never] |
| rollingUpdate [RollingUpdateStatefulSetStrategy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#rollingupdatestatefulsetstrategy-v1-apps) | RollingUpdate defines parameters for the RollingUpdate type. |  |  |
| autoUpdateDataPlane boolean | AutoUpdateDataPlane indicates whether the Galera data-plane version (agent and init containers) should be automatically updated based on the operator version. It defaults to false.Updating the operator will trigger updates on all the MariaDB instances that have this flag set to true. Thus, it is recommended to progressively set this flag after having updated the operator. |  |  |


#### UpdateType


*Underlying type:* *string*


UpdateType defines the type of update for a MariaDB resource.


*Appears in:*
- [UpdateStrategy](#updatestrategy)


| Field | Description |
| --- | --- |
| Field | Description |
| ReplicasFirstPrimaryLast | ReplicasFirstPrimaryLastUpdateType indicates that the update will be applied to all replica Pods first and later on to the primary Pod.The updates are applied one by one waiting until each Pod passes the readiness probei.e. the Pod gets synced and it is ready to receive traffic. |
| RollingUpdate | RollingUpdateUpdateType indicates that the update will be applied by the StatefulSet controller using the RollingUpdate strategy.This strategy is unaware of the roles that the Pod have (primary or replica) and it willperform the update following the StatefulSet ordinal, from higher to lower. |
| OnDelete | OnDeleteUpdateType indicates that the update will be applied by the StatefulSet controller using the OnDelete strategy.The update will be done when the Pods get manually deleted by the user. |
| Never | NeverUpdateType indicates that the StatefulSet will never be updated.This can be used to roll out updates progressively to a fleet of instances. |


#### User


User is the Schema for the users API. It is used to define grants as if you were running a 'CREATE USER' statement.


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| apiVersion string | enterprise.mariadb.com/v1alpha1 |  |  |
| kind string | User |  |  |
| metadata [ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for fields of metadata. |  |  |
| spec [UserSpec](#userspec) |  |  |  |


#### UserSpec


UserSpec defines the desired state of User


*Appears in:*
- [User](#user)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| requeueInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | RequeueInterval is used to perform requeue reconciliations. |  |  |
| retryInterval [Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#duration-v1-meta) | RetryInterval is the interval used to perform retries. |  |  |
| cleanupPolicy [CleanupPolicy](#cleanuppolicy) | CleanupPolicy defines the behavior for cleaning up a SQL resource. |  | Enum: [Skip Delete] |
| mariaDbRef [MariaDBRef](#mariadbref) | MariaDBRef is a reference to a MariaDB object. |  | Required: {} |
| passwordSecretKeyRef [SecretKeySelector](#secretkeyselector) | PasswordSecretKeyRef is a reference to the password to be used by the User.If not provided, the account will be locked and the password will expire.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password. |  |  |
| passwordHashSecretKeyRef [SecretKeySelector](#secretkeyselector) | PasswordHashSecretKeyRef is a reference to the password hash to be used by the User.If the referred Secret is labeled with "enterprise.mariadb.com/watch", updates may be performed to the Secret in order to update the password hash.It requires the 'skip-strict-password-validation' option to be set. See: [](https://mariadb.com/docs/server/ref/mdb/cli/mariadbd/strict-password-validation/). |  |  |
| passwordPlugin [PasswordPlugin](#passwordplugin) | PasswordPlugin is a reference to the password plugin and arguments to be used by the User.It requires the 'skip-strict-password-validation' option to be set. See: [](https://mariadb.com/docs/server/ref/mdb/cli/mariadbd/strict-password-validation/). |  |  |
| require [TLSRequirements](#tlsrequirements) | Require specifies TLS requirements for the user to connect. See: [securing-connections-for-client-and-server.md#requiring-tls](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/securing-connections-for-client-and-server.md#requiring-tls). |  |  |
| maxUserConnections integer | MaxUserConnections defines the maximum number of simultaneous connections that the User can establish. | 10 |  |
| name string | Name overrides the default name provided by metadata.name. |  | MaxLength: 80 |
| host string | Host related to the User. |  | MaxLength: 255 |


#### Volume


Refer to the Kubernetes docs: [#volume-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#volume-v1-core).


*Appears in:*
- [MariaDBSpec](#mariadbspec)
- [PodTemplate](#podtemplate)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| name string |  |  |  |
| emptyDir [EmptyDirVolumeSource](#emptydirvolumesource) |  |  |  |
| nfs [NFSVolumeSource](#nfsvolumesource) |  |  |  |
| csi [CSIVolumeSource](#csivolumesource) |  |  |  |
| hostPath [HostPathVolumeSource](#hostpathvolumesource) |  |  |  |
| persistentVolumeClaim [PersistentVolumeClaimVolumeSource](#persistentvolumeclaimvolumesource) |  |  |  |
| secret [SecretVolumeSource](#secretvolumesource) |  |  |  |
| configMap [ConfigMapVolumeSource](#configmapvolumesource) |  |  |  |


#### VolumeClaimTemplate


VolumeClaimTemplate defines a template to customize PVC objects.


*Appears in:*
- [GaleraConfig](#galeraconfig)
- [MaxScaleConfig](#maxscaleconfig)
- [Storage](#storage)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| accessModes [PersistentVolumeAccessMode](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#persistentvolumeaccessmode-v1-core) array |  |  |  |
| selector [LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#labelselector-v1-meta) |  |  |  |
| resources [VolumeResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#volumeresourcerequirements-v1-core) |  |  |  |
| storageClassName string |  |  |  |
| metadata [Metadata](#metadata) | Refer to Kubernetes API documentation for fields of metadata. |  |  |


#### VolumeMount


Refer to the Kubernetes docs: [#volumemount-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#volumemount-v1-core).


*Appears in:*
- [Container](#container)
- [ContainerTemplate](#containertemplate)
- [GaleraAgent](#galeraagent)
- [GaleraInit](#galerainit)
- [MariaDBSpec](#mariadbspec)
- [MaxScaleSpec](#maxscalespec)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| name string | This must match the Name of a Volume. |  |  |
| readOnly boolean |  |  |  |
| mountPath string |  |  |  |
| subPath string |  |  |  |


#### VolumeSource


Refer to the Kubernetes docs: [#volume-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#volume-v1-core).


*Appears in:*
- [Volume](#volume)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| emptyDir [EmptyDirVolumeSource](#emptydirvolumesource) |  |  |  |
| nfs [NFSVolumeSource](#nfsvolumesource) |  |  |  |
| csi [CSIVolumeSource](#csivolumesource) |  |  |  |
| hostPath [HostPathVolumeSource](#hostpathvolumesource) |  |  |  |
| persistentVolumeClaim [PersistentVolumeClaimVolumeSource](#persistentvolumeclaimvolumesource) |  |  |  |
| secret [SecretVolumeSource](#secretvolumesource) |  |  |  |
| configMap [ConfigMapVolumeSource](#configmapvolumesource) |  |  |  |


#### WeightedPodAffinityTerm


Refer to the Kubernetes docs: [#weightedpodaffinityterm-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#weightedpodaffinityterm-v1-core).


*Appears in:*
- [PodAntiAffinity](#podantiaffinity)


| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| Field | Description | Default | Validation |
| weight integer |  |  |  |
| podAffinityTerm [PodAffinityTerm](#podaffinityterm) |  |  |  |


CC BY-SA / Gnu FDL

