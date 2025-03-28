# Installing MariaDB on IBM Cloud

Get MariaDB on IBM Cloud

You should have an IBM Cloud account, otherwise you can [register here](https://cloud.ibm.com/registration).
At the end of the tutorial you will have a cluster with MariaDB up and running. IBM Cloud uses Bitnami charts to deploy MariaDB on with helm
1. We will provision a new Kubernetes Cluster for you if, you already have one skip to step **2**
2. We will deploy the IBM Cloud Block Storage plug-in, if already have it skip to step **3**
3. MariaDB deployment

#

# Step 1 provision Kubernetes Cluster

* Click the Catalog button on the top
* Select Service from the catalog
* Search for Kubernetes Service and click on it

![kubernetes-select](/en/installing-mariadb-on-ibm-cloud/+image/kubernetes-select "kubernetes-select")

* You are now at the Kubernetes deployment page, you need to specify some details about the cluster
* Choose a plan standard or free, the free plan only has one worker node and no subnet, to provision a standard cluster, you will need to upgrade you account to Pay-As-You-Go
* To upgrade to a Pay-As-You-Go account, complete the following steps:

* In the console, go to Manage > Account.
* Select Account settings, and click Add credit card.
* Enter your payment information, click Next, and submit your information
* Choose classic or VPC, read the [docs](https://cloud.ibm.com/docs/containers?topic=containers-infrastructure_providers) and choose the most suitable type for yourself

![infra-select](/en/installing-mariadb-on-ibm-cloud/+image/infra-select "infra-select")

* Now choose your location settings, for more information please visit [Locations](https://cloud.ibm.com/docs/containers?topic=containers-regions-and-zones#zones)
* Choose Geography (continent)

![location-geo](/en/installing-mariadb-on-ibm-cloud/+image/location-geo "location-geo")

* Choose Single or Multizone, in single zone your data is only kept in on datacenter, on the other hand with Multizone it is distributed to multiple zones, thus safer in an unforseen zone failure

![location-avail](/en/installing-mariadb-on-ibm-cloud/+image/location-avail "location-avail")

* Choose a Worker Zone if using Single zones or Metro if Multizone

![location-worker](/en/installing-mariadb-on-ibm-cloud/+image/location-worker "location-worker")

* If you wish to use Multizone please set up your account with [VRF](https://cloud.ibm.com/docs/dl?topic=dl-overview-of-virtual-routing-and-forwarding-vrf-on-ibm-cloud) or [enable Vlan spanning](https://cloud.ibm.com/docs/vlans?topic=vlans-vlan-spanning#vlan-spanning)
* If at your current location selection, there is no available Virtual LAN, a new Vlan will be created for you

* Choose a Worker node setup or use the preselected one, set Worker node amount per zone

![worker-pool](/en/installing-mariadb-on-ibm-cloud/+image/worker-pool "worker-pool")

* Choose Master Service Endpoint, In VRF-enabled accounts, you can choose private-only to make your master accessible on the private network or via VPN tunnel. Choose public-only to make your master publicly accessible. When you have a VRF-enabled account, your cluster is set up by default to use both private and public endpoints. For more information visit [endpoints](https://cloud.ibm.com/docs/account?topic=account-service-endpoints-overview).

![endpoints](/en/installing-mariadb-on-ibm-cloud/+image/endpoints "endpoints")

* Give cluster a name

![name-new](/en/installing-mariadb-on-ibm-cloud/+image/name-new "name-new")

* Give desired tags to your cluster, for more information visit [tags](https://cloud.ibm.com/docs/account?topic=account-tag)

![tasg-new](/en/installing-mariadb-on-ibm-cloud/+image/tasg-new "tasg-new")

* Click create

![create-new](/en/installing-mariadb-on-ibm-cloud/+image/create-new "create-new")

* Wait for you cluster to be provisioned

![cluster-prepare](/en/installing-mariadb-on-ibm-cloud/+image/cluster-prepare "cluster-prepare")

* Your cluster is ready for usage

![cluster-done](/en/installing-mariadb-on-ibm-cloud/+image/cluster-done "cluster-done")

#

# Step 2 deploy IBM Cloud Block Storage plug-in

The Block Storage plug-in is a persistent, high-performance iSCSI storage that you can add to your apps by using Kubernetes Persistent Volumes (PVs).

* Click the Catalog button on the top
* Select Software from the catalog
* Search for IBM Cloud Block Storage plug-in and click on it

![block-search](/en/installing-mariadb-on-ibm-cloud/+image/block-search "block-search")

* On the application page Click in the dot next to the cluster, you wish to use
* Click on Enter or Select Namespace and choose the default Namespace or use a custom one (if you get error please wait 30 minutes for the cluster to finalize)

![block-cluster](/en/installing-mariadb-on-ibm-cloud/+image/block-cluster "block-cluster")

* Give a name to this workspace
* Click install and wait for the deployment

![block-storage-create](/en/installing-mariadb-on-ibm-cloud/+image/block-storage-create "block-storage-create")

#

# Step 3 deploy MariaDB

We will deploy MariaDB on our cluster

* Click the Catalog button on the top
* Select Software from the catalog
* Search for MariaDB and click on it

![search](/en/installing-mariadb-on-ibm-cloud/+image/search "search")

* Please select IBM Kubernetes Service

![target-select](/en/installing-mariadb-on-ibm-cloud/+image/target-select "target-select")

* On the application page Click in the dot next to the cluster, you wish to use

![cluster-select](/en/installing-mariadb-on-ibm-cloud/+image/cluster-select "cluster-select")

* Click on Enter or Select Namespace and choose the default Namespace or use a custom one

![details-namespace](/en/installing-mariadb-on-ibm-cloud/+image/details-namespace "details-namespace")

* Give a unique name to workspace, which you can easily recognize

![details-name](/en/installing-mariadb-on-ibm-cloud/+image/details-name "details-name")

* Select which resource group you want to use, it's for access controll and billing purposes. For more information please visit [resource groups](https://cloud.ibm.com/docs/account?topic=account-account_setup#bp_resourcegroups)

![details-resource](/en/installing-mariadb-on-ibm-cloud/+image/details-resource "details-resource")

* Give tags to your MariaDB, for more information visit [tags](https://cloud.ibm.com/docs/account?topic=account-tag)

![details-tags](/en/installing-mariadb-on-ibm-cloud/+image/details-tags "details-tags")

* Click on Parameters with default values, You can set deployment values or use the default ones

![parameters](/en/installing-mariadb-on-ibm-cloud/+image/parameters "parameters")

* Please set the MariaDB root password in the parameters

![root-password](/en/installing-mariadb-on-ibm-cloud/+image/root-password "root-password")

* After finishing everything, tick the box next to the agreements and click install

![aggreement-create](/en/installing-mariadb-on-ibm-cloud/+image/aggreement-create "aggreement-create")

* The MariaDB workspace will start installing, wait a couple of minutes

![in-progress](/en/installing-mariadb-on-ibm-cloud/+image/in-progress "in-progress")

* Your MariaDB workspace has been successfully deployed

![done](/en/installing-mariadb-on-ibm-cloud/+image/done "done")

#

# Verify MariaDB installation

* Go to [Resources](http://cloud.ibm.com/resources) in your browser
* Click on Clusters
* Click on your Cluster

![resource-select](/en/installing-mariadb-on-ibm-cloud/+image/resource-select "resource-select")

* Now you are at you clusters overview, here Click on Actions and Web terminal from the dropdown menu

![cluster-main](/en/installing-mariadb-on-ibm-cloud/+image/cluster-main "cluster-main")

* Click install - wait couple of minutes

![terminal-install](/en/installing-mariadb-on-ibm-cloud/+image/terminal-install "terminal-install")

* Click on Actions
* Click Web terminal --> a terminal will open up

* Type in the terminal, please change NAMESPACE to the namespace you choose at the deployment setup:

```
$ kubectl get ns
```

![get-ns](/en/installing-mariadb-on-ibm-cloud/+image/get-ns "get-ns")

```
$ kubectl get pod -n NAMESPACE -o wide
```

![get-pods](/en/installing-mariadb-on-ibm-cloud/+image/get-pods "get-pods")

```
$ kubectl get service -n NAMESPACE
```

![get-service](/en/installing-mariadb-on-ibm-cloud/+image/get-service "get-service")

* Enter your pod with bash , please replace PODNAME with your mariadb pod's name

```
$ kubectl exec --stdin --tty PODNAME -n NAMESPACE -- /bin/bash
```

![bash](/en/installing-mariadb-on-ibm-cloud/+image/bash "bash")

* After you are in your pod please enter enter Mariadb and enter your root password after the prompt

```
$ mysql -u root -p
```

![welcome](/en/installing-mariadb-on-ibm-cloud/+image/welcome "welcome")

You have succesfully deployed MariaDB IBM Cloud!