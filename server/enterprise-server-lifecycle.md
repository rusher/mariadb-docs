# Enterprise Server Lifecycle

[MariaDB Enterprise Server](https://mariadb.com/docs/server/products/mariadb-enterprise-server/) enables a predictable development and operations experience through an _enterprise lifecycle_. This enterprise lifecycle incorporates optimized builds, predictable release behavior, and vendor support.

### Enterprise Server Builds

MariaDB Enterprise Server incorporates enhancements that are not present in MariaDB Community Server including:

* Premium features to meet enterprise scaling and operations requirements.
* Priority bug fixes that are available first to enterprise customers.
* Increased code stability through restricted release of new functionality.
* Reduction of risk from untested or incompatible features, through inclusion of only features with level 3 support (Engineering code-level support) from MariaDB Corporation.
* Optimized configuration defaults.

For details on features added to enhance, harden, and secure MariaDB Enterprise Server, see [What's New in MariaDB Enterprise Server 10.6?](https://mariadb.com/docs/server/whats-new/mariadb-enterprise-server-11-4/).

### Enterprise Server Releases

Releases of MariaDB Enterprise Server are predictable because:

* Major releases are delivered on a schedule.
* Minor releases are focused on small, incremental defect remediation.
* Critical fixes from newer release series are selectively backported.
* Enterprise-grade testing drives a low defect rate.
* Specific changes present in each release are clearly communicated.

Additional information on the release cycle for MariaDB Enterprise Server can be found in [MariaDB Corporation Engineering Policy](https://mariadb.com/engineering-policies/).

#### Upcoming Minor and Maintenance Releases

Planned releases of MariaDB Enterprise Server are [scheduled](https://mariadb.com/docs/server/products/mariadb-enterprise-server/release-schedule/).

#### Obtaining MariaDB Enterprise Server

MariaDB Enterprise Server is available to MariaDB subscription customers via the [MariaDB Customer Portal](https://customers.mariadb.com/).

If you are not yet a MariaDB subscription customer, [contact MariaDB Corporation](https://mariadb.com/contact/) for more information.

MariaDB Enterprise Server binary and source code is delivered over secure protocols from MariaDB Corporation-maintained infrastructure as detailed in the [Deployment Guide](https://mariadb.com/docs/server/deploy/).

#### Enterprise Server Release Identifiers

Releases of MariaDB Enterprise Server are given an identifier such as 'MariaDB Enterprise Server 10.5.8-5', whose components are:

* The product name (MariaDB Enterprise Server).
* The release series (10.5, spoken "ten-five").
* The point release of MariaDB Community Server used as the base of this Enterprise Server release (.8, spoken "ten-five-eight").
* The release postfix of MariaDB Enterprise Server, starting with '-1' and incremented for subsequent releases on that _release series_ (-5, spoken "ten-five-eight-dash-five").
* On the Debian and Ubuntu platforms, the release postfix contains a period instead of a dash, such that release postfixes start with .1 and increment for subsequent releases on that _release series_ (.5, spoken "ten-five-eight-dot-five").

Additional information on the release numbering for MariaDB Enterprise Server can be found in [MariaDB Corporation Engineering Policy](https://mariadb.com/engineering-policies/).

### Enterprise Server Support

MariaDB Corporation offers vendor support for MariaDB Enterprise Server including:

* [Customer Support](support.md) as detailed in [Subscription Services Policy](https://mariadb.com/subscription-services-policies/).
* [Professional Services](https://mariadb.com/services/) including Migration Services, Remote DBA Services, and consulting.
* Customer communications, managed via the [MariaDB Customer Portal](https://customers.mariadb.com/).
* [Training](https://mariadb.com/services/training/)
* [Documentation](https://mariadb.com/docs/)

Copyright © 2025 MariaDB
