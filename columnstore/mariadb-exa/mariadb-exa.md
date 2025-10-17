---
description: This section documents MariaDB Exa for Analytics workloads.
icon: chart-pie-simple-circle-currency
---

# MariaDB Exa

## Overview

MariaDB Exa is powered by [Exasol](https://www.exasol.com/analytics-engine/). MariaDB Exa is a high-performance, in-memory, MPP (Massively Parallel Processing) analytical database designed for fast, large-scale SQL analytics.\
\
MariaDB Exa is optimized for columnar storage, vectorized execution, and distributed query processing, making it an excellent complement to MariaDB Enterprise Server and MariaDB MaxScale in modern analytic architectures.

This guide describes how to integrate MariaDB Exa for analytical workloads, data pipelines, and change data capture (CDC) scenarios. It also introduces common configuration patterns, performance considerations, and validation techniques used in production and benchmarking environments.

## Why Exasol?

Exasol offers:

* Extreme performance for complex aggregations and joins, even on billions of rows.
* SQL compatibility with ANSI SQL and support for many advanced analytic functions.
* Elastic scalability, allowing nodes to be added for horizontal growth.&#x20;
* High Availability through multimode deployments, standby nodes, data redistribution and data redundancy.&#x20;
* Separation of compute and storage allowing for effective scaling for resource intensive workloads.
* Simple connectivity through standard JDBC and ODBC drivers.&#x20;

When paired with MariaDB Enterprise Server and MaxScale, MariaDB Exa can act as a real-time analytical sink for data replicated or streamed from operational systems.

\
