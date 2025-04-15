
# Database Design Phase 4: Testing

This article follows on from [Database Design Phase 3: Implementation](database-design-phase-3-implementation.md).


The testing phase is where the performance, security, and integrity of the data are tested. Usually this will occur in conjunctions with the applications that have been developed. You test the performance under various loads conditions to see how the database handles multiple concurrent connections or high volumes of updating and reading. Are the reports generated quickly enough? For example, an application designed with the old [MyISAM](../../../../../../server/reference/storage-engines/myisam-storage-engine/myisam-system-variables.md) storage engine may prove to be too slow because the impact of the updates was underestimated. The storage engine may have to be changed to [XtraDB](../../../advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) in response.


Data integrity also needs to be tested, as the application may have logical flaws that result in transactions being lost or other inaccuracies. Further, security needs to be tested to ensure that users can access and change only the data they should.


The logical or physical designs may have to be modified. Perhaps new indexes are required (which the tester may discover after careful use of MariaDB's [EXPLAIN](../../../advanced-mariadb-articles/development-articles/outdated-pages/explain-formatjson-in-mysql.md) statement, for example).


The testing and fine-tuning process is an iterative one, with multiple tests performed and changes implemented.


The following are the steps in the testing phase:


1. Test the performance
1. Test the security
1. Test the data integrity
1. Fine-tune the parameters or modify the logical or physical designs in response to the tests.

