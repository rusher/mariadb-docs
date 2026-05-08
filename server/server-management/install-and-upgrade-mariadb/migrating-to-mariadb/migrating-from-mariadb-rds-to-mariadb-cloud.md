---
description: >-
  Guide for migrating from MariaDB RDS to MariaDB Cloud using AWS Database
  Migration Service (DMS).
hidden: true
---

# Migrating From MariaDB RDS to MariaDB Cloud

This guide covers migrating from a self-managed or AWS MariaDB RDS instance to MariaDB Cloud using [AWS Database Migration Service (DMS)](https://aws.amazon.com/dms/), utilizing binary log streaming for [Change Data Capture (CDC)](#user-content-fn-1)[^1] to enable a near-zero downtime cutover.

## Phase 1: Preparing Your Source and Target Environments

DMS reads changes from MariaDB using binary log replication. These settings must be in place before creating DMS endpoints or starting any task.

{% stepper %}
{% step %}
### Source AWS MariaDB RDS Configuration.

* Enable Automated Backups: Set "Backup Retention Period" to at least 1 day.
* Create a Custom Parameter Group: Apply the following parameters to ensure DMS can read row-level changes:
* binlog\_format = ROW
* binlog\_row\_image = Full
* binlog\_checksum = NONE

The "DB instance parameter group" displays mariadb118custom (In sync).

* Apply and Reboot: Associate the custom parameter group with your RDS instance and Reboot to finalize the ROW mode.
* Set Log Retention: Provide a buffer for DMS to read the continuous logs.&#x20;

Execute CALL mysql.rds\_set\_configuration('binlog retention hours', 24);

* Verify Settings: Set  VARIABLES LIKE binlog\_format to ROW, Increase network tolerance parameter times.
{% endstep %}

{% step %}
###


{% endstep %}
{% endstepper %}

1:&#x20;

* Enable Automated Backups: Set "Backup Retention Period" to at least 1 day.
* Create a Custom Parameter Group: Apply the following parameters to ensure DMS can read row-level changes:
* binlog\_format = ROW
* binlog\_row\_image = Full
* binlog\_checksum = NONE

The "DB instance parameter group" displays mariadb118custom (In sync).

* Apply and Reboot: Associate the custom parameter group with your RDS instance and Reboot to finalize the ROW mode.
* Set Log Retention: Provide a buffer for DMS to read the continuous logs.&#x20;

Execute CALL mysql.rds\_set\_configuration('binlog retention hours', 24);

* Verify Settings: Set  VARIABLES LIKE binlog\_format to ROW, Increase network tolerance parameter times.

2: MariaDB Cloud Target Configuration

* Create Database: Log into MariaDB Cloud and run CREATE DATABASE \<DbName>;.
* Create User (Optional): Use the default user to create additional users with privileges (e.g., users in RDS, dms\_admin etc.), setting the Allowed Host to % or the specific IP of your DMS instance.
* Verify Settings: Set VARIABLES LIKE binlog\_format to ROW, Increase network tolerance parameter times.
* Enable Connectivity: Add 0.0.0.0/0 (temporarily), the DMS Public IP, or your NAT Gateway EIP to the MariaDB Cloud IP Allowlist.

Several IPs are whitelisted, including 13.205.232.134/32 labeled as "AWS DMS", and 172.168.55.21/32 labeled as "APP SERVER".

* Note on Serverless: Unlike Provisioned instances, MariaDB Serverless creates temporary Elastic Network Interfaces (ENIs) in your subnets. These ENIs lack default Public IPs and cannot reach the internet via an Internet Gateway. A NAT Gateway in your VPC is required.

***

#### Phase 2: Provisioning the AWS DMS Networking and Compute

The replication instance is the compute resource that handles the data migration.

* Instance Type: Using a "Provisioned" instance is highly recommended for static IP stability.
* VPC Architecture: Deploy resources within private subnets for enhanced security, utilizing a NAT Gateway to establish the required outbound internet connection to MariaDB Cloud.&#x20;
* Public Accessibility: Select Publicly Accessible: Yes if your traffic is routing over the internet. Note the allocated Public IP and add it to your MariaDB Cloud allowlist if you are not using an open 0.0.0.0/0 rule.

AWS DMS "Replication instances" list - A provisioned instance named dmsprovisionedinstance is shown with Status "Available", Publicly accessible "Yes", and an assigned Public IP address.

* Test Connections: Ensure both endpoints return a "Successful" status.

&#x20;Successful connection test results in the DMS console. The endpoint identifier mdbprovisioned successfully connected via the dmsprovisionedinstance replication instance.

* Serverless Limits: Similar to the target database, DMS Serverless relies on ENIs without Public IPs and inherently struggles to reach MariaDB Cloud over the internet without a properly configured NAT Gateway.

***

#### Phase 3: Migrating Schema Definitions and Secondary Objects

AWS DMS only migrates table data and basic primary keys. It does not migrate secondary objects such as views, stored procedures, or triggers.

Export Metadata from RDS Source: Use mariadb-dump from your terminal to grab all schema objects except the table data. Run this command:

mariadb-dump -h \[RDS\_HOST] -u \[USER] -p --no-data --no-create-info --routines --triggers --databases \<DBName> | sed -e 's/DEFINER=\`\[^\`]\*\`@\`\[^\`]\*\`//g'  > metadata.sql

***

#### Phase 4: Configuring Migration Endpoints and Sync Tasks

Before creating endpoints, establish secure CA certificate trust between AWS DMS and your database servers.

Source Endpoint (RDS):

1. Download the Global Bundle or Regional CA from the AWS RDS connection information section.

Under "Connect using > Code snippets", commands are provided:&#x20;

curl -o global-bundle.pem https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem and the corresponding mariadb connection string.

2. In the DMS Console, go to Certificates > Import Certificate. Upload the global-bundle.pem file and name it rds-source-ca.
3. In the Source Endpoint settings, select SSL mode: verify-ca and choose the rds-source-ca certificate. Point to your RDS endpoint using the MariaDB user.

&#x20;

<br>

The Source engine is MariaDB RDS. The Server name points to an RDS AWS domain.Secure Socket Layer (SSL) mode is set to verify-ca and the imported CA certificate is uploaded from AWS MariaDB RDS.

Target Endpoint (MariaDB Cloud):

1. Download the MariaDB Cloud CA Certificate from your MariaDB Cloud portal (found in the Security or Connect tab).

Primary Endpoint service details in MariaDB Cloud and a download link for the Certificate authority chain.

2. Import this into the DMS Console as MariaDB Cloud-target-ca.
3. Create the Target Endpoint, select SSL mode: verify-full, and point it to the MariaDB Cloud endpoint on Port 3306.

The target engine is MariaDB Cloud. The Server name points to a .skysql.com domain. SSL mode is set to verify-full with the appropriate CA certificate uploaded from MariaDB Cloud.

Create the DMS Migration Task:

* Migration type: Select Migrate existing data and replicate ongoing changes (enables Snapshot + Replica mode).
* Target table preparation mode: Choose Drop tables on target if you want DMS to build the structures, or Do nothing if you pre-created the tables.
* Stop task after full load completes: Select Don't stop so it transitions into CDC mode automatically.
* Include LOB columns in replication: Select Limited LOB mode.
* Table Mappings: Add a selection rule with Schema \<your Schema Name>, Table name %, and Action Include.
* Transformation Rules: Add rules here if you need to rename schemas (e.g., sakila to sakila\_prod).
* Premigration Assessment: Enable this to let AWS check for potential issues (unsupported data types, missing primary keys) before launching.

***

#### Phase 5: Live Replication, Target Cutover, and Decommissioning

1\. Executing the "Snapshot + Replica" Select Start on create to initiate the Full Load. Watch the Full load progress bar until it hits 100%. The task status will transition to Load complete, replication ongoing. From this point forward, any INSERT or UPDATE on the RDS source is replicated to MariaDB Cloud instantaneously.

A task named provisioned-cdc-snap-r has a Status of "Load completed, replication ongoing". The load progress reads 100% and CDC replication is active .&#x20;

2\. Post-Table Migration (Views, Triggers, & Procedures) AWS DMS does not migrate secondary objects. Once DMS shows the load is complete, apply the metadata you exported in Part 3 to your MariaDB Cloud Instance:

mariadb -h \[MariaDB Cloud\_HOST] -P 4000 -u \[USER] -p \<DBName> < metadata.sql

Important CDC Considerations for Triggers: If you have triggers on the Target (MariaDB Cloud) that update other tables, DMS might accidentally trigger them again while replicating CDC events, causing duplicate data. It is best practice to keep triggers disabled on the target until the final cutover.

3\. Cutover: Identify a low-traffic window, stop the application from writing to the RDS source, and wait for the CDC lag to hit zero. Update your connection strings to point to MariaDB Cloud, re-enable your triggers, and finally terminate the DMS task and infrastructure.

#### Phase 6: (Optional) Reverse Replication&#x20;

<br>

Switch Master Slave to make MariaDB Cloud the Master.

Established MariaDB SkySQL as the Primary (Master) and AWS RDS as the Replica (Slave).&#x20;

<br>

1\. Prepare MariaDB Cloud (New Master)&#x20;

<br>

Before RDS can follow MariaDB Cloud, the target environment must be configured to allow inbound replication.

* Add the AWS RDS Public IP (or NAT Gateway EIP) to the SkySQL Allowlist (Port 3306).
* Identity: Create a dedicated replication user on MariaDB Cloud (SkySQL):

CREATE USER 'repl\_user'@'%' IDENTIFIED BY 'YourSecurePassword';

GRANT REPLICATION SLAVE, REPLICATION CLIENT ON \*.\* TO 'repl\_user'@'%';

* Checkpoint: Capture the current Binary Log coordinates to tell RDS where to start:

SHOW MASTER STATUS; -- Note the File and Position

2\. Configure AWS RDS (New Slave) Because RDS is a managed service, standard CHANGE MASTER commands are restricted. You must use AWS stored procedures.

* Initialize: Clear old migration metadata and point RDS to the SkySQL endpoint using the file and position from step 1:

CALL mysql.rds\_set\_external\_master (

'skysql-hostname.net', 4000, 'repl\_user', 'YourSecurePassword',

'\[File\_from\_SkySQL]', \[Position\_from\_SkySQL], 1 );

* Activate: Start the replication threads:

CALL mysql.rds\_start\_replication;

3\. Monitoring & Verification The "Source of Truth" for the health of this link moves from the DMS Console to the database command line.

* Status Check on RDS: Run CALL mysql.rds\_replica\_status\G; to verify connectivity.
* Success Criteria: Ensure Slave\_IO\_Running is Yes, Slave\_SQL\_Running is Yes, and Seconds\_Behind\_Master is 0.
* Status Check on MariaDB Cloud: Run SHOW MASTER STATUS\G and SHOW SLAVE STATUS\G (this should return an Empty set).

Decommissioning Once Seconds\_Behind\_Master remains at 0, the AWS DMS infrastructure is redundant. To eliminate unnecessary costs:

1. Stop and Delete the AWS DMS Task.
2. Terminate the DMS Replication Instance.
3. Delete the NAT Gateway (if no longer required for outbound RDS traffic).

Note: The DMS Task Console will now show "Zero Activity" and may report "High Source Latency." This is expected, as the data flow has successfully moved from the DMS pipe to native MariaDB replication.

[^1]: In databases, change data capture (CDC) is a set of software design patterns used to determine and track the data that has changed (the "deltas") so that action can be taken using the changed data. The result is a delta-driven dataset.
