# SET SESSION AUTHORIZATION

From [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120), certain users can perform server actions as another user:

* This is implemented through the SET SESSION AUTHORIZATION statement.
* This permits everything that can be done in a [stored procedure](server-usage/stored-routines/stored-procedures/)  with an arbitrary definer.
* &#x20;In particular, this bypasses [account lock](security/user-account-management/account-locking.md), [expired password](security/user-account-management/user-password-expiry.md), authentication, REQUIRE SSL checks, and so on.
* &#x20;Users are required to have the [SET USER](reference/sql-statements/account-management-sql-statements/grant.md#set-user) privilege
* Does not work inside [transactions](reference/sql-statements/transactions/), the [Performance Schema](server-usage/storage-engines/performance_schema-storage-engine.md) and [stored procedures](server-usage/stored-routines/stored-procedures/).

