---
description: >-
  Learn about authentication in MariaDB MaxScale. This section covers
  configuring user authentication for clients connecting through MaxScale and
  securing access to your database instances.
---

# MaxScale Authentication

## Overview

In MariaDB MaxScale, authenticators perform the following tasks:

* Authenticating clients that connect to MaxScale
* Authenticating connections to back-end MariaDB Enterprise Server and MariaDB Xpand nodes
* Deciding how authentication should be performed

## Authenticators Supported by MaxScale

* [GSSAPI Authenticator](../../reference/maxscale-authenticators/maxscale-gssapi-client-authenticator.md)
* [Native Authenticator](../../reference/maxscale-authenticators/maxscale-mariadb-mysql-authenticator.md)
* [PAM Authenticator](../../reference/maxscale-authenticators/maxscale-pam-authenticator.md)
* [PARSEC Authenticator](../../reference/maxscale-authenticators/maxscale-parsec-authenticator.md)
* [ed25519 Authenticator](../../reference/maxscale-authenticators/maxscale-ed25519-authenticator.md)
