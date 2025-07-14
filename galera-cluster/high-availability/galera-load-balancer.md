# Galera Load Balancer

Galera Load Balancer is a simple load balancer specifically designed for [Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/). Like Galera, it only runs on Linux. Galera Load Balancer is developed and maintained by Codership. Documentation is available [on fromdual.com](https://www.fromdual.com/galera-load-balancer-documentation).

Galera Load Balancer is inspired by Pen, which is a generic TCP load balancer. However, since Pen is a generic TCP connection load balancer, the techniques it uses are not well-suited to the particular use case of database servers. Galera Load Balancer is optimized for this type of workload.

Several balancing policies are supported. Each node can be assigned a different weight. Nodes with a higher weight are preferred. Depending on the selected policy, other nodes can even be ignored until the preferred nodes crash.

A lightweight daemon called glbd receives the connections from clients, and it redirects them to nodes. No specific client exists for this demo: a generic TCP client, such as nc, can be used to send administrative commands and read the usage statistics.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
