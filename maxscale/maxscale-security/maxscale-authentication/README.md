---
description: >-
  Learn about authentication in MariaDB MaxScale. This section covers
  configuring user authentication for clients connecting through MaxScale and
  securing access to your database instances.
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
---

# MaxScale Authentication

## Overview

In MariaDB MaxScale, authenticators perform the following tasks:

* Authenticating clients that connect to MaxScale
* Authenticating connections to back-end MariaDB Enterprise Server and MariaDB Xpand nodes
* Deciding how authentication should be performed

## Authenticators Supported by MaxScale

* [GSSAPI Authenticator](../../maxscale-archive/archive-of-2x.xx-versions/mariadb-maxscale-23-02/mariadb-maxscale-23-02-authenticators/mariadb-maxscale-2302-gssapi-client-authenticator.md)
* [Native Authenticator](native-authenticator.md)
* [PAM Authenticator](../../maxscale-archive/archive-of-2x.xx-versions/mariadb-maxscale-23-02/mariadb-maxscale-23-02-authenticators/mariadb-maxscale-2302-pam-authenticator.md)
