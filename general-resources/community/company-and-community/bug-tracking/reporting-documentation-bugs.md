# Reporting Documentation Bugs

Documentation bugs and feature requests should be reported at [jira.mariadb.org](https://jira.mariadb.org).

This page contains general guidelines for the community for reporting documentation bugs.

## Known Bugs

First, check that the bug isn't already filed in the[MariaDB bugs database](https://jira.mariadb.org/browse/MDEV).

For the MariaDB bugs database, use JIRA search to check if a report you are going to submit already exists. You are not expected to be a JIRA search guru, but please at least make some effort.

* Choose `Issues => Search for issues`;
* If the form opens for you with a long blank line at top, press `Basic` on the right to switch to a simpler mode;
* In the `Project` field, choose the related project, (`MDEV` for generic MariaDB server and clients);
* In the `Contains text` text field, enter the most significant key words from your future report;
* Press `Enter` or the magnifying glass icon to search.

If you see bug reports which are already closed, but you still see the error, please confirm that the issue still exists in the Knowledge Base.

If you find an open bug report, please vote/add a comment that the bug also affects you along with any additional information you have that may help us to find and fix the bug.

If the bug is not in the MariaDB bugs database yet, then it's time to file a bug report.

## Reporting a Bug

Bugs and feature requests are reported to the [MariaDB bugs database](https://jira.mariadb.org/browse/MDEV).

### JIRA Privacy

Please note that our JIRA entries are public, and JIRA is very good at keeping a record of everything that has been done. What this means is that if you ever include confidential information in the description there will be a log containing it, even after you've deleted it. The only way to get rid of it will be removing the JIRA entry completely.

Attachments in JIRA are also public.

Access to a comment can be restricted to a certain group (e.g. Developers only), but the existing groups are rather wide, so you should not rely on it either.

### JIRA Fields

The section below describes which JIRA fields need to be populated while filing reports, and what should be put there.\
Apart from what's mentioned below, you don't have to fill or change any fields while creating a new bug report.

#### Project

If you are filing a report for documentation about MariaDB server, client programs, or MariaDB Galera Cluster, the target project is `MDEV`. Connectors and MaxScale have separate projects with corresponding names. If you choose a wrong project, bug processing can be delayed, but there is no reason to panic -- we'll correct it. If you inform us about the mistake, we'll change it faster.

Some project names include:

* CONC - MariaDB Connector/C
* CONJ - MariaDB Connector/J
* CONJS - MariaDB Connector/node.js
* CONPY - MariaDB Connector/Python
* MCOL - ColumnStore
* MDBF - MariaDB Foundation Development (anything related to the [mariadb.org domain](https://mariadb.org))
* MDEV - MariaDB server, client programs, or MariaDB Galera Cluster
* MXS - MaxScale
* ODBC - MariaDB Connector/ODBC

#### Type

Feature requests are not the same as bug reports. Specify a `Task` type for feature requests in [Jira](../../../development-articles/general-development-information/tools/jira.md), and a `Bug` type for bug reports. Like with the project field, choosing a wrong type will put the request to the wrong queue and can delay its processing, but eventually it will be noticed and amended.

#### Summary

Please make sure the summary line is informative and distinctive. It should always be easy to recognize your report among other similar ones, otherwise a reasonable question arises -- why are they not duplicates?

Examples:

* good summary: SELECT max\_statement\_time clause example gives incorrect results
* not a good summary: code example doesn't work

Generally, we try not to change the original summary without a good reason to do it, so that you can always recognize your own reports easily.

#### Priority

We do not have separate Severity/Priority fields in JIRA, so this Priority field serves a double purpose. For original reports, it indicates the importance of the problem from the reporter's point of view. The default is 'Major'; there are two lower and two higher values. Please set the value accurately. While we do take it into account during initial processing, increasing the value above reasonable won't do any good, the only effect will be the waste of time while somebody will be trying to understand why a trivial problem got such a high priority. After that, the value will be changed, and the report will be processed in its due time anyway.

#### Component/s

Documentation bugs should have "Documentation" added as a component in order to be correctly assigned.

#### Affected Version/s

Since the documentation is not version-dependent, you can put N/A in this field.

#### Environment

Usually this can be left empty, but if applicable, put any environment-related information that might be important for reproducing or analyzing the problem.

#### Description

The most important part of the description are the steps to reproduce the problem. Link to the page on the Knowledge Base with the error/s. Where applicable, provide a sample structure and results clearly demonstrating the problem.

_Use {noformat}...{noformat} and {code}...{code} blocks for code and console output in the description._

#### Links

If the documentation error relates to an existing bug/feature request in JIRA (for example an undocumented new feature), you should link it here. Alternatively, you can just mention them in the description or comments.

#### Tags

You don't have to set any tags, but if you want to use any for your convenience, feel free to do so. However, please don't put too generic values -- for example, the tag `mariadb` is meaningless, because everything there is `mariadb`. Don't be surprised if some tags are removed later during report processing.

CC BY-SA / Gnu FDL
