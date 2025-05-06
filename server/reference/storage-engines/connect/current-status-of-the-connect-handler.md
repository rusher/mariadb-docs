
# Current Status of the CONNECT Handler

The current CONNECT handler is a GA (stable) release. It was written starting both from an aborted project written for MySQL in 2004 and from the “DBCONNECT” program. It was tested on all the examples described in this document, and is distributed with a set of 53 test cases. Here is a not limited list of future developments:


1. Adding more table types.
1. Make more tests files (53 are already made)
1. Adding more data types, in particular unsigned ones (done for unsigned).
1. Supporting indexing on nullable and decimal columns.
1. Adding more optimize tools (block indexing, dynamic indexing, etc.) (done)
1. Supporting MRR (done)
1. Supporting partitioning (done)
1. Getting NOSQL data from the Net as answers from REST queries (done)


No programs are bug free, especially new ones. Please [report all bugs](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/bug-tracking/reporting-bugs) or documentation errors using the means provided by MariaDB.


GPLv2

