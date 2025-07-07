# SET SESSION AUTHORIZATION

From MariaDB 12.0, certain users can perform server actions as another user:

* This is implemented through the SET SESSION AUTHORIZATION statement.
* This permits everything that can be done in a stored procedure  with an arbitrary definer.
* &#x20;In particular, this bypasses account lock, expired password, authentication, REQUIRE SSL checks, and so on.
* &#x20;Users are required to have the SET USER privilege
* Does not work inside transactions, the Performance Scheme and Stored Procedures

