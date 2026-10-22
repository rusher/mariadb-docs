---
description: >-
  How MariaDB Cloud AI Retrieval authenticates requests, connects to your
  database, and handles the region of your data.
icon: shield-check
hidden: true
---

<!-- DRAFT for DOCS-6592. Hidden until the Public Preview launch. Structure follows Egor Ustinov's call of 2026-10-20. Open items are marked TODO. -->

# Access and Security

This page explains who can use AI Retrieval, how your applications authenticate, how AI Retrieval connects to your MariaDB service, and where your data is processed. Document knowledge bases and database knowledge bases handle the database connection differently, so each has its own section.

## Roles and Permissions

Users with the Viewer role can view knowledge bases but cannot create or change them.

<!-- TODO: list the other roles and what each can do. Verify against the portal role checks in skysql-ui-client. -->

## API Keys and Authentication

Applications call a knowledge base through a REST API and authenticate with an API key. Send the key as a bearer token in the `Authorization` header, or in the `X-API-Key` header. An API key belongs to your user account, not to a single knowledge base.

To create, revoke, or delete a key, see [Connect Your Application](document-knowledge-bases.md#connect-your-application).

<!-- TODO: confirm the scope of a key and the roles that can create one. Egor, 2026-10-20: keys authenticate the same way as any MariaDB Cloud endpoint. -->

## Document Knowledge Bases

A document knowledge base stores its chunks and embeddings in a MariaDB service that you select or let MariaDB Cloud provision. AI Retrieval does not read any other data in that service.

### Objects That AI Retrieval Creates

For each document knowledge base, AI Retrieval creates these objects in the vector store service:

| Object | Name | Purpose |
| --- | --- | --- |
| Schema | `ai_retrieval_cloud_` followed by the last 7 characters of the knowledge base ID | Holds the chunks and embeddings of the knowledge base. |
| Database user | `mdb_ai_rag_` followed by the same 7 characters | The account that AI Retrieval uses to connect. It has privileges on this schema only. |

You do not supply credentials for a document knowledge base, and the portal does not offer an option to choose the user name.

{% hint style="warning" %}
Do not delete or change these objects, and do not change the password of the database user. A knowledge base cannot ingest or retrieve documents without them.
{% endhint %}

<!-- TODO: Egor said on 2026-10-20 that AI Retrieval connects with the service user shown in the Connect dialog and stops working when its password changes. The code (ai-retrieval-cloud packages/skysql-common dbprovision/user_provisioner.py, commit 5124e49a of 2026-09-15) provisions a dedicated mdb_ai_rag_<suffix> user per knowledge base with privileges on its own schema only, and customer_db.py ensures it on first ingestion. Ask Egor which is right before unhiding, then fix the table and the hint. -->

<!-- TODO: confirm that deleting the schema breaks the knowledge base and whether a service restored from a backup needs the objects recreated. See Known Limitations in the overview. -->

### Network Access

AI Retrieval connects to the vector store service over a private network inside MariaDB Cloud. You do not need to add AI Retrieval to the IP allowlist of the service.

<!-- TODO: Egor confirmed this for document knowledge bases on 2026-10-20 (the 0.0.0.0/0 allowlist requirement from MCDEV-2653 is fixed). He will check database knowledge bases. Not verified in code. -->

## Database Knowledge Bases

A database knowledge base reads from a MariaDB service that already holds your data. You enter the user name and password of the account that AI Retrieval uses. AI Retrieval builds its description of the database, called the semantic map, from the tables and columns that this account can see.

To control what a database knowledge base can read, create a dedicated user:

1. Create a view that exposes only the data that the knowledge base should use.
2. Create a user that has privileges on the view only.
3. Enter that user when you create the knowledge base.

<!-- TODO: Database knowledge bases are not documented yet. The source is on the unmerged branch feature/MCDEV-3646-DBKB of skysql-gen-ai and in skysql-microservices ai-service. Confirm this section against the merged code and the final create form, and ask about the IP allowlist (Egor will check). -->

## Data Residency

Document knowledge bases run in the cloud and region that you select. The vector store service must be in the same cloud and region, so the chunks and embeddings are stored there. You access a document knowledge base through the regional endpoint that the **Connect** dialog shows.

The create form marks where each embedding model runs. Text that is sent to a model is processed as follows:

| Provider | Models | Processing |
| --- | --- | --- |
| AWS Bedrock, in the region of the knowledge base | Cohere Embed 3 English, Cohere Embed 3 Multilingual, Cohere Embed 4 | Traffic stays in the region. |
| Google | Gemini Embedding 2 | Processed outside your cloud. |

<!-- TODO: the model list is from the test environment on 2026-10-20 and the processing labels come from the create form. Confirm the final model list and the wording on data residency with Egor. Model names are not published elsewhere yet. -->

<!-- TODO: Egor said document knowledge bases must be accessed through the regional endpoints. Replace the placeholder host in the guide with the production host once it is known. -->

<!-- Egor said on 2026-10-20 not to cover encryption or audit logging. Left out on purpose. -->

## Next Steps

{% content-ref url="document-knowledge-bases.md" %}
[document-knowledge-bases.md](document-knowledge-bases.md)
{% endcontent-ref %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
