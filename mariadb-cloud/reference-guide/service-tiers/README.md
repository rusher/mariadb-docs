# Service Tiers

The available service tiers are **Foundation** and **Power**. See the features of those service tiers in the following table, notable differences for Power Tier highlighted.

|                                                                               | Foundation Tier                                            | Power Tier                                                                   |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------- |
| <mark style="color:blue;">**Service Features**</mark>                         |                                                            |                                                                              |
| Database                                                                      | MariaDB Community                                          | MariaDB Enterprise                                                           |
| Supported Deployments                                                         | <p>Provisioned - Single Node, Replicated<br>Serverless</p> | <p>Provisioned - Single Node, Replicated<br>Serverless</p>                   |
| <p>Uptime SLA<br>% of time service is guaranteed to be available</p>          | <p>99.95% for multi-node<br>99.9% for single node</p>      | <p><strong>99.995% for multi-node</strong><br>99.9% for single node</p>      |
| Support                                                                       | <p>Basic Included<br>Standard, Premium available</p>       | <p>Basic Included<br>Standard, Premium, <strong>RDBA available</strong></p>  |
| <mark style="color:blue;">**Cloud Resources**</mark>                          |                                                            |                                                                              |
| <p>Cloud Availability<br>Cloud deployment options</p>                         | AWS, GCP, Azure, 40+ regions                               | AWS, GCP, Azure, 40+ regions                                                 |
| Compute                                                                       | Up to 16 vCPU, 128GB RAM                                   | **Up to 128 vCPU, 1024 GB RAM**                                              |
| <p>Compute Scaling<br>Ability to scale both horizontally and vertically</p>   | On-demand                                                  | <p>On-demand<br><strong>Autoscaling</strong></p>                             |
| Storage                                                                       | Up to 1000 GB                                              | **Up to 9000 GB**                                                            |
| Storage Scaling                                                               | On-demand                                                  | On-demand or **Autoscaling**                                                 |
| <p>Multi-node Configuration<br>Ability to launch and horizontally scale</p>   | Up to 1 read replica                                       | **Up to 4 read replicas**                                                    |
| <p>Redundant MaxScale<br>For improved higher availability</p>                 | No                                                         | Yes                                                                          |
| <mark style="color:blue;">**Backup and Recovery Features**</mark>             |                                                            |                                                                              |
| <p>Backup Types<br>Supported backup types</p>                                 | <p>Nightly<br>Self-service</p>                             | <p>Nightly<br>Self-service</p>                                               |
| Backup Storage                                                                | Managed                                                    | Managed or **External**                                                      |
| Recovery                                                                      | Backup restore                                             | <p>Backup restore and<br><strong>Point-in-time restore</strong></p>          |
| <mark style="color:blue;">**Observability Features**</mark>                   |                                                            |                                                                              |
| Metrics and Logs                                                              | Cloud Portal                                               | Cloud Portal                                                                 |
| Alerts                                                                        | <p>Preconfigured<br>Custom</p>                             | Preconfigured                                                                |
| <mark style="color:blue;">**Security**</mark>                                 |                                                            |                                                                              |
| Portal RBAC                                                                   | Yes                                                        | Yes                                                                          |
| <p>Data Encryption<br>In transit and at rest for data and backups</p>         | Yes                                                        | Yes                                                                          |
| <p>Secure Connectivity<br>How clients are able to connect to the database</p> | IP Allowlist                                               | <p>IP Allowlist<br><strong>PrivateLink, Private Service Connect</strong></p> |
