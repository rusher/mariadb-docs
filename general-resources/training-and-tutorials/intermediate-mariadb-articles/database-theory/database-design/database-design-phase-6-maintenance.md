
# Database Design Phase 6: Maintenance

This article follows on from [Database Design Phase 5: Operation](database-design-phase-5-operation.md).


The database maintenance phase incorporates general maintenance, such as maintaining the indexes, optimizing the tables, adding and removing users, and changing passwords, as well as backups and restoration of backups in case of a failure. New requirements also start to be requested, and this may result in new fields, or new tables, being created.


As the new system and organization changes, the existing database becomes less and less sufficient to meet the organization's needs. For example, the media organization may be amalgamated with media bodies from other countries, requiring integration of many data sources, or the volumes and staff may expand (or reduce) dramatically. Eventually, there comes a time, whether it's 10 months after completion or 10 years, when the database system needs to be replaced. The maintenance of the existing database begins to drain more and more resources, and the effort to create a new design is matched by the current maintenance effort. As this point, the database is coming to the end of its life, and a new project begins life in the Analysis phase.


The following are the steps in the maintenance phase:


1. Maintain the indexes
1. Maintain the tables
1. Maintain the users
1. Change passwords
1. Backup
1. Restore backups
1. Change the design to meet new requirements

