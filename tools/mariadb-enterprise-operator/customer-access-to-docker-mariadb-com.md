
# Customer access to docker.mariadb.com

This documentation aims to provide guidance on how to configure access to `docker.mariadb.com` in your MariaDB Enterprise Operator resources.


## Table of contents


* [Customer credentials](#customer-credentials)
* [Openshift](#openshift)
* [MariaDB](#mariadb)
* [MaxScale](#maxscale)
* [Backup, Restore and SqlJob](#backup-restore-and-sqljob)


## Customer credentials


MariaDB Corporation requires customers to authenticate when logging in to the MariaDB Enterprise Docker Registry. A Customer Download Token must be provided as the password. Customer Download Tokens are available through the MariaDB Customer Portal. To retrieve the customer download token for your account:


* Navigate to the [Customer Download Token at the MariaDB Customer Portal](https://customers.mariadb.com/downloads/token/).
* Log in using your [MariaDB ID](https://id.mariadb.com/).
* Copy the Customer Download Token to use as the password when logging in to the MariaDB Enterprise Docker Registry.


Then, configure a Kubernetes [kubernetes.io/dockerconfigjson Secret](https://kubernetes.io/docs/concepts/configuration/secret/#docker-config-secrets) to authenticate:



```
kubectl create secret docker-registry mariadb-enterprise \
   --docker-server=docker.mariadb.com \
   --docker-username=<email> \
   --docker-password=<customer-download-token>
```



## Openshift


If you are running in Openshift, it is recommended to use the [global pull secret](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/images/managing-images#images-update-global-pull-secret_using-image-pull-secrets) to configure [customer credentials](#customer-credentials). The global pull secret is automatically used by all `Pods` in the cluster, without having to specify `imagePullSecrets` explicitly.


To configure the global pull secret, you can use the following commands:


* Extract your [Openshift global pull secret](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/images/managing-images#images-update-global-pull-secret_using-image-pull-secrets):



```
oc extract secret/pull-secret -n openshift-config --confirm
```



* Login in the MariaDB registry providing the customer download token as password:



```
oc registry login \
  --registry="docker.mariadb.com" \
  --auth-basic="<email>:<customer-download-token>" \
  --to=.dockerconfigjson
```



* Update the global pull secret:



```
oc set data secret/pull-secret -n openshift-config --from-file=.dockerconfigjson
```



Alternatively, you can also create a dedicated `Secret` for authenticating:



```
oc create secret docker-registry mariadb-enterprise \
   --docker-server=docker.mariadb.com \
   --docker-username=<email> \
   --docker-password=<customer-download-token>
```



## `MariaDB`


In order to configure access to `docker.mariadb.com` in your `MariaDB` resources, you can use the `imagePullSecrets` field to specify your [customer credentials](#customer-credentials):



```
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
  ...
  image: docker.mariadb.com/enterprise-server:11.4.4-2
  imagePullPolicy: IfNotPresent
  imagePullSecrets:
    - name: mariadb-enterprise
```



As a result, the `Pods` created as part of the reconciliation process will have the `imagePullSecrets`.


## `MaxScale`


Similarly to `MariaDB`, you are able to configure access to `docker.mariadb.com` in your `MaxScale` resources:



```
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale
spec:
  ...
  image: docker.mariadb.com/maxscale-enterprise:25.01.1
  imagePullPolicy: IfNotPresent
  imagePullSecrets:
    - name: mariadb-enterprise
```



## `Backup`, `Restore` and `SqlJob`


The batch `Job` resources will inherit the `imagePullSecrets` from the referred `MariaDB`, as they also make use of its `image`. However, you are also able to provide dedicated `imagePullSecrets` for these resources:



```
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
  ...
  image: docker.mariadb.com/enterprise-server:11.4.4-2
  imagePullPolicy: IfNotPresent
  imagePullSecrets:
    - name: mariadb-enterprise
```




```
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Backup
metadata:
  name: backup
spec:
  ...
  mariaDbRef:
    name: mariadb
  imagePullSecrets:
    - name: backup-registry
```



When the resources from the previous examples are created, a `Job` with both `mariadb-enterprise` and `backup-registry` `imagePullSecrets` will be reconciled.


CC BY-SA / Gnu FDL


{% @marketo/form formid="4316" formId="4316" %}
