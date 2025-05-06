
# Kubernetes Overview for MariaDB Users

Kubernetes, or K8s, is software to orchestrate containers. It is released under the terms of an open source license, Apache License 2.0.


Kubernetes was originally developed by Google. Currently it is maintained by the Cloud Native Computing Foundation (CNCF), with the status of Graduated Project.


For information about how to setup a learning environment or a production environment, see [Getting started](https://kubernetes.io/docs/setup/) in Kubernetes documentation.



## Architecture


Kubernetes runs in a **cluster**. A cluster runs a **workload**: a set of servers that are meant to work together (web servers, database servers, etc).


A Kubernetes cluster consists of the following components:


* Nodes run containers with the servers needed by our applications.
* Controllersconstantly check the cluster nodes current state, and compare it with the desired state.
* A Control Plane is a set of different components that store the cluster desired state and take decisions about the nodes. The Control Plane provides an API that is used by the controllers.


For more information on Kubernetes architecture, see [Concepts](https://kubernetes.io/docs/concepts/) and [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/) in Kubernetes documentation.


### Nodes


A node is a system that is responsible to run one or more pods. A pod is a set of containers that run a Kubernetes workload or part of it. All containers that run in the same pod are also located on the same node. Usually identical pods run on different nodes for fault tolerance.


For more details, see [Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/) in the Kubernetes documentation.


Every node must necessarily have the following components:


* kubelet
* kube-proxy
* A container runtime


#### kubelet


kubelet has a set of **PodSpecs** which describe the desired state of pods. It checks that the current state of the pods matches the desired state. It especially takes care that containers don't crash.


#### kube-proxy


In a typical Kubernetes cluster, several containers located in different pods need to connect to other containers, located in the same pods (for performance and fault tolerance reasons). Therefore, when we develop and deploy an application, we can't know in advance the IPs of the containers to which it will have to connect. For example, an application server may need to connect to MariaDB, but the MariaDB IP will be different for every pod.


The main purpose of kube-proxy is to implement the concept of Kubernetes **services**. When an application needs to connect to MariaDB, it will connect to the MariaDB service. kube-proxy will receive the request and will redirect it to a running MariaDB container in the same pod.


#### Container Runtime


Kubernetes manages the containers in a pod via a container runtime, or container manager, that supports the Kubernetes Container Runtime Interface (CRI). Container runtimes that meet this requisite are listed in the [Container runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/) page in the Kubernetes documentation. More information about the Container Runtime Interface can be found [on GitHub](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-node/container-runtime-interface).


Originally, Kubernetes used Docker as a container runtime. This was later deprecated, but Docker images can still be used using any container runtime.


### Controllers


Controllers constantly check if there are differences between the pod's current state and their desired state. When differences are found, controllers try to fix them. Each node type controls one or more resource types. Several types of controllers are needed to run a cluster.


Most of the actions taken by the controllers user the API server in the Control Plane. However, this is not necessarily true for custom controllers. Also, some actions cannot be performed via the Control Plane. For example, if some nodes crashed, adding new nodes involves taking actions outside of the Kubernetes cluster, and controllers will have to do this themselves.


It is possible to write custom controllers to perform checks that require knowledge about a specific technology. For example, a MariaDB custom controller may want to check if [replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/README.md) is working by issuing [SHOW REPLICA STATUS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-replica-status.md) commands. This logic is specific to the way MariaDB works, and can only be implemented in a customer controller. Custom controllers are usually part of operators.


For more information, see [Controllers](https://kubernetes.io/docs/concepts/architecture/controller/) in the Kubernetes documentation.


### Control Plane


The control plane consists of the following components.


For more information about the control plane, see [Control Plane Components](https://kubernetes.io/docs/concepts/overview/components/) in Kubernetes documentation.


#### API Server


An API Server exposes API functions both internally and externally. It is essential to coordinate Kubernetes components so that they react to node's change of state, and it allows the user to send commands.


The default implementation of the API Server is kube-apiserver. It is able to scale horizontally and to balance the load between its instances.


#### kube-controller-manager


Most controllers run in this component.


#### etcd


etcd contains all data used by a Kubernetes cluster. It is a good idea to take regular backups of etcd data.


#### kube-scheduler


When a new pod is created, kube-scheduler decides which node should host it. The decision is made based on several criteria, like the resource requirements for the pod.


#### cloud-controller-manager


cloud-controller-manager implements the logic and API of a cloud provider. It receives requests from the API Server and performs specific actions, like creating an instance in AWS. It also runs controllers that are specific to a cloud vendor.


### Clients and Tools


Kubernetes comes with a set of tools that allow us to communicate with the API server and test a cluster.


#### kubectl


kubectl allows communication with the API server and run commands on a Kubernetes cluster.


#### kubeadm


kubeadm allows creating a Kubernetes cluster that is ready to receive commands from kubectl.


#### kind and minikube


These tools are meant to create and manage test clusters on a personal machine. They work on Linux, MacOS and Windows. kind creates a cluster that consists of Docker containers, therefore it requires Docker to be installed. minikube runs a single-node cluster on the local machine.


## Kubernetes Resources and References


* [Kubernetes website](https://kubernetes.io/).
* [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) on Wikipedia.
* [Kubernetes organization](https://github.com/kubernetes) on GitHub.
* [The Official MariaDB Operator](https://github.com/mariadb-operator/mariadb-operator)
* [OperatorHub.io](https://operatorhub.io/)
* [Kubernetes Community Forums](https://discuss.kubernetes.io/).
* (video) [MariaDB database clusters on Kubernetes](https://mariadb.org/fest2020/kubernetes/), by Pengfei Ma, at MariaDB Server Fest 2020.
* Series of posts by Anel Husakovic on the MariaDB Foundation blog:

  * [Start MariaDB in K8s](https://mariadb.org/start-mariadb-in-k8s/)
  * [MariaDB & K8s: Communication between containers/Deployments](https://mariadb.org/mariadb-k8s-communication-between-containers-deployments/)
  * [MariaDB & K8s: Create a Secret and use it in MariaDB deployment](https://mariadb.org/mariadb-k8s-create-a-secret-and-use-it-in-mariadb-deployment/)
  * [MariaDB & K8s: Deploy MariaDB and WordPress using Persistent Volumes](https://mariadb.org/mariadb-k8s-deploy-mariadb-and-wordpress-using-persistent-volumes/)
  * [Create statefulset MariaDB application in K8s](https://mariadb.org/create-statefulset-mariadb-application-in-k8s/)
  * [MariaDB replication using containers](https://mariadb.org/mariadb-replication-using-containers/)
  * [MariaDB & K8s: How to replicate MariaDB in K8s](https://mariadb.org/mariadb-k8s-how-to-replicate-mariadb-in-k8s/)



Content initially contributed by [Vettabase Ltd](https://vettabase.com/).


CC BY-SA / Gnu FDL

