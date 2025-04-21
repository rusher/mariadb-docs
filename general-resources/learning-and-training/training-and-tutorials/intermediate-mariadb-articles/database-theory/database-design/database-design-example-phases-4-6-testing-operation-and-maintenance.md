
# Database Design Example Phases 4-6: Testing, Operation and Maintenance

This article follows on from [Database Design Example Phase 3: Implementation](database-design-example-phase-3-implementation.md).


Once the database is ready the application programs have been rolled out, it's time for the testing to begin. While the other phases of the database lifecycle can occur reasonably independently of the systems development process, part of the testing phase is how all the components run together.


Load testing may indicate that MariaDB has not been set up to handle the expected 600 concurrent connections, and the configuration file needs to be changed. Other tests may indicate that in certain circumstances, duplicate key errors are received, as the locking mechanism is not uniformly implemented, and the application does not handle locking correctly. The application needs to be fixed. Backups also need to be tested, as well as the ability to smoothly restore from backup with a minimum of downtime.


Testing is one of the most neglected and critical phases. A designer or manager who does not properly account for testing is simply incompetent. No matter how tiny your system, make sure you allocate time for thorough testing, and time for fixing the inevitable bugs.


Once testing is complete, the system can be rolled out. You decide on a low-key rollout and give a few selected poets access to the website to upload their poems. You discover other problems. Some poets upload poems using [character sets](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets/) you haven't catered for, and you need to make a few tweaks to ensure these are handled correctly.


Soon enough, the system is rolled out completely. Maintenance, though, is a never-ending task, and with the immense popularity of the system, and with large numbers of updates and deletes, the system tends to become fragmented. The administrator regularly needs to take care of this, and, of course, the inevitable disk failure leads to an all-night restore session, and much thankfulness for the ease of use of [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump).

