---
title: Untitled
---

<details>

<summary>Disable AWS PrivateLink via the MariaDB Cloud DBaaS API</summary>

\\

To disable AWS PrivateLink on an existing service, you will need to update the service endpoints with a payload similar to the following:

```json
[
  {
    "mechanism": "nlb"
  }
]
```

This payload should then be sent to the API `PATCH` https://api.skysql.com/provisioning/v1/services/{SERVICE\_ID}/endpoints where `{SERVICE_ID}` is the ID of the service you are updating. For more information on using the MariaDB Cloud DBaaS API, see ["MariaDB Cloud DBaaS API"](https://apidocs.skysql.com/#/Services/patch_provisioning_v1_services__service_id__endpoints).

</details>
