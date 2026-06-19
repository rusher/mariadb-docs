---
description: >-
  Maintenance windows and scheduling policies for MariaDB Cloud — every service
  has an assigned weekly 1-hour window defined in UTC, auto-assigned per region
  and configurable per service.
---

# Maintenance Windows and Scheduling Policies

Every MariaDB Cloud database operates with an assigned weekly maintenance window. You can configure a different preferred maintenance period for each of your services.

## Window Configuration Details

* Each maintenance window is a block of **1 hour**.
* Windows are defined in **UTC** to provide consistency across global time zones and daylight saving time (DST) changes.
* If you don't select a window during or after launch, a default window is automatically assigned for your service, scheduled during off-peak hours for the deployed region's local time.

You can view and change your assigned window at any time from the **Maintenance** pane on the Service detail page. See [Maintenance Management](../cloud-usage/maintenance-management.md) for the full workflow.

## Default Global Schedules

If you don't select a window, your service is assigned a default scheduled outside critical business hours in the deployed region's local time. Default windows are shown in UTC. Entries marked **TBD** will be published once finalized.

### Americas

| UTC | Regions | Default window |
| :-- | :-- | :-- |
| UTC-8 (PT) | AWS: us-west-2, Azure: westus2, GCP: us-west1<br>AWS: us-west-1, Azure: westus, GCP: us-west2 | TBD |
| UTC-5 (ET) | AWS: us-east-1, Azure: eastus, GCP: us-east1<br>AWS: us-east-2, Azure: eastus2, GCP: us-east4<br>AWS: ca-central-1, Azure: canadacentral, GCP: northamerica-northeast1 | TBD |
| UTC-3 | AWS: sa-east-1, Azure: brazilsouth, GCP: southamerica-east1 | TBD |

### Europe

| UTC | Regions | Default window |
| :-- | :-- | :-- |
| UTC | AWS: eu-west-1, Azure: northeurope, GCP: europe-west1<br>AWS: eu-west-2, Azure: uksouth, GCP: europe-west2 | 09:00 UTC – 17:00 UTC |
| UTC+1 | AWS: eu-central-1, Azure: westeurope, GCP: europe-west3<br>AWS: eu-west-3, Azure: francecentral, GCP: europe-west9<br>Azure: westeurope, GCP: europe-west4<br>AWS: eu-north-1, Azure: swedencentral, GCP: europe-north1 | 09:00 UTC – 17:00 UTC |

### Middle East & Africa

| UTC | Regions | Default window |
| :-- | :-- | :-- |
| UTC+2 | AWS: af-south-1, Azure: southafricanorth, GCP: africa-south1 | 09:00 UTC – 17:00 UTC |
| UTC+4 | AWS: me-central-1, Azure: uaenorth, GCP: me-central2 | 09:00 UTC – 17:00 UTC |

### Asia Pacific

| UTC | Regions | Default window |
| :-- | :-- | :-- |
| UTC+5:30 | AWS: ap-south-1, Azure: centralindia, GCP: asia-south1 | TBD |
| UTC+8 | AWS: ap-southeast-1, Azure: southeastasia, GCP: asia-southeast1 | TBD |
| UTC+9 | AWS: ap-northeast-1, Azure: japaneast, GCP: asia-northeast1<br>AWS: ap-northeast-2, Azure: koreacentral, GCP: asia-northeast3 | TBD |
| UTC+10 | AWS: ap-southeast-2, Azure: australiaeast, GCP: australia-southeast1 | TBD |

## Auditability and Compliance

MariaDB Cloud maintains a comprehensive, auditable history of all maintenance activities for each service. This history records when maintenance was scheduled, executed, and completed. Customer actions — including manual application, window changes, and deferrals — are permanently recorded to provide a complete audit trail for compliance and troubleshooting.
