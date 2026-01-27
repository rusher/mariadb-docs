---
hidden: true
---

# Bring Your Own Account (BYOA)

Bring Your Own Account (BYOA) allows large enterprises to deploy fully managed MariaDB Cloud databases directly within their own public cloud infrastructure. This deployment model offers the operational simplicity of a managed service while satisfying strict requirements for data sovereignty, compliance, and cloud cost optimization.

With BYOA, the Control Plane (UI, API, Monitoring) remains in MariaDB Cloud, while the Data Plane (Compute, Storage, Backups) resides entirely in your cloud account.

## How it works

A BYOA environment is a secure, isolated set of resources within your own cloud provider account (Azure, AWS, or Google Cloud) that is managed by MariaDB Cloud.

```mermaid
flowchart LR
    %% Simplified diagram focusing on the 4 steps
    classDef step fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#0d47a1
    classDef resource fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c

    subgraph Steps ["Operational Workflow"]
        direction LR
        S1["1. Account Linking<br/>(IAM Handshake)"]:::step
        S2["2. Provisioning<br/>(VM Creation)"]:::step
        S3["3. Management<br/>(Patching/Health)"]:::step
        S4["4. Connectivity<br/>(Private Access)"]:::step
    end
    
    S1 --> S2
    S2 --> S3
    S3 --> S4
```

1. Account Linking: You authorize MariaDB Cloud to access your specific cloud subscription via a secure IAM role or Service Principal with least-privilege permissions.
2. Resource Provisioning: When you create a service, MariaDB Cloud orchestrates the deployment of Virtual Machines, Storage, and Networking directly into your account.
3. Management: MariaDB Cloud monitors health, performs backups, and applies patches automatically, just like a standard managed service.
4. Connectivity: Your applications connect to the database locally within your cloud network (VPC/VNet), ensuring low latency and high security without exposing data to the public internet.

#### Architecture Diagram

The following diagram illustrates how the MariaDB Control Plane securely manages resources inside your cloud account without ever extracting your data.

```mermaid
flowchart LR
    %% Global Graph Settings: Bold styles for "Aiven-like" readability
    classDef control fill:#e3f2fd,stroke:#1565c0,stroke-width:3px,color:#0d47a1,font-size:16px,font-weight:bold;
    classDef data fill:#fff3e0,stroke:#ef6c00,stroke-width:3px,color:#e65100,font-size:16px,font-weight:bold;
    classDef external fill:#f5f5f5,stroke:#616161,stroke-width:2px,font-size:15px;

    %% Actors
    User([Customer DevOps]):::external
    App([Your Application]):::external

    %% MariaDB Cloud Control Plane
    subgraph CP ["MariaDB Control Plane"]
        direction TB
        Portal["Portal & API"]:::control
        Orch["Orchestrator"]:::control
        Mon["Monitoring"]:::control
    end

    %% Customer Cloud Account
    subgraph Cloud ["Your Cloud Account (AWS/Azure)"]
        direction TB
        IAM["IAM Role / SP"]:::data
        
        subgraph VPC ["Your Private VPC"]
            direction TB
            Bastion["Secure Bastion"]:::data
            DB["Database Node"]:::data
            Storage[("Storage")]:::data
        end
    end

    %% Connections - Using thick lines for visibility
    User ==>|"1. Manage"| Portal
    Portal ==> Orch
    Orch ==>|"2. Provision"| IAM
    IAM -.->|"Creates"| VPC
    
    %% Secure Tunnel
    Orch ===>|"3. Manage (TLS)"| Bastion
    Bastion <==> DB
    DB -.->|"Metrics"| Mon
    DB <==> Storage

    App ==>|"4. Connect"| DB
    
    %% Subgraph Styling for clarity
    style CP fill:#f0f8ff,stroke:#1565c0,stroke-width:2px,color:#0d47a1
    style Cloud fill:#fff8e1,stroke:#ef6c00,stroke-width:2px,color:#e65100
    style VPC fill:#ffffff,stroke:#ef6c00,stroke-width:2px,stroke-dasharray: 5 5
```

### Why use BYOA?

BYOA is designed for enterprise organizations with specific regulatory or infrastructure requirements:

* Compliance & Data Sovereignty: Since data never leaves your cloud account, you maintain absolute control over data residency. This simplifies meeting strict regulatory standards such as HIPAA, PCI-DSS, and GDPR.
* Cloud Cost Optimization: You pay your cloud provider directly for the underlying infrastructure. This allows you to burn down existing committed spend (e.g., Azure MACC, AWS EDP) and leverage your negotiated enterprise discounts.
* Network Security: Database nodes are deployed into a private VPC/VNet. You can enforce your own security group rules, routing policies, and network isolation without complex peering arrangements.
* Advanced Workloads (PowerPlus): Enables the PowerPlus tier, allowing for advanced topologies like Galera Clusters to run in your own environment.

#### Galera Cluster Topology (PowerPlus Exclusive)

Customers on the PowerPlus tier can deploy Galera Clusters for synchronous multi-primary replication and zero data loss failover.

```mermaid
graph TD
    %% Styles
    classDef node fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef sync fill:#ffffff,stroke:#01579b,stroke-width:2px,stroke-dasharray: 5 5;

    App[Customer Application]

    subgraph Galera_Cluster ["MariaDB Galera Cluster (PowerPlus)"]
        direction TB
        N1[("Node 1<br/>(Primary)")]:::node
        N2[("Node 2<br/>(Primary)")]:::node
        N3[("Node 3<br/>(Primary)")]:::node
        
        %% Synchronous Replication
        N1 <==>|Sync Repl| N2
        N2 <==>|Sync Repl| N3
        N3 <==>|Sync Repl| N1
    end

    App -->|Writes| N1
    App -.->|Failover Write| N2
    
    %% Note
    style Galera_Cluster fill:#f3e5f5,stroke:#4a148c,stroke-dasharray: 5 5
```

### Who is eligible for BYOA?

BYOA is an enterprise-grade feature with specific commercial and technical prerequisites:

* Service Tier: Your organization must be on the Power or PowerPlus tier.
* Support Plan: You must have Standard Support with the Remote DBA add-on enabled.
* Contract: Available to customers with annual contracts or minimum spend commitments.

{% hint style="info" %}
For the initial release (Jan 2026), BYOA is available as a Tech Preview on Microsoft Azure. AWS and Google Cloud support will follow in subsequent phases.
{% endhint %}

### BYOA Pricing and Billing

The BYOA setup splits your costs into two separate components. This model ensures transparency and allows you to apply your own cloud credits or reserved instance savings to the infrastructure portion of the cost.

```mermaid
flowchart LR
    %% Styles
    classDef money fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef invoice fill:#fff9c4,stroke:#fbc02d,stroke-width:2px,stroke-dasharray: 5 5;

    Customer((Customer Organization))

    subgraph MariaDB_Bill ["Invoice 1: MariaDB Cloud"]
        direction TB
        M_Fees[("Management Fees<br/>Support (Remote DBA)<br/>Software Licenses")]:::invoice
    end

    subgraph Cloud_Bill ["Invoice 2: Cloud Provider (AWS/Azure)"]
        direction TB
        C_Infra[("Compute (VMs)<br/>Storage (IOPS/Disk)<br/>Data Transfer")]:::invoice
    end

    %% Flows
    Customer -->|Pays Service Fees| MariaDB_Bill
    Customer -->|Pays Infrastructure Costs| Cloud_Bill

    %% Benefit Annotation - Fixed Syntax Here (Added quotes around label)
    Cloud_Bill -.->|"Apply committed spend<br/>(e.g., EDP / MACC)"| Customer
```

1. MariaDB Cloud Invoice: You receive a bill from MariaDB for the management fee, software licensing, and support.
2. Cloud Provider Invoice: You receive a bill directly from your cloud provider (e.g., Microsoft Azure) for the consumed infrastructure resources (Compute, Storage, Network).

### Get Started

For the Tech Preview (Jan 2026), onboarding is a guided process.

1. Contact Sales: Submit a request via the MariaDB Cloud Portal or contact your account representative to validate eligibility.
2. Onboarding: Our support team will provide the necessary IAM/Service Principal templates and guide you through the account linking process.
3. Deploy: Once linked, "Bring Your Own Account" will appear as a deployment target in your Create Service wizard.

```mermaid
sequenceDiagram
    participant Admin as Customer Admin
    participant Portal as MariaDB Portal
    participant Cloud as Customer Azure/AWS
    participant Sales as MariaDB Sales

    Admin->>Portal: Request BYOA Enablement
    Portal->>Sales: Notify for Qualification (Tier Check)
    Sales-->>Portal: Approve Request
    
    rect rgb(240, 248, 255)
    note right of Admin: Account Linking Phase
    Portal->>Admin: Generate IaC Template (Terraform/ARM)
    Admin->>Cloud: Apply Template (Create Role/SP)
    Cloud-->>Portal: Validate Permissions & Establish Trust
    end
    
    rect rgb(255, 250, 240)
    note right of Admin: Deployment Phase
    Admin->>Portal: Create Service (Select BYOA Region)
    Portal->>Cloud: Provision VPC, VMs, Storage
    Cloud-->>Admin: Resources Ready
    end
```
