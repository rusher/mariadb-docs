# Restoring Data

If you lose your data in MariaDB, but have been using [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) (previously called mysqldump) to make regular backups of your data in MariaDB, you can use the dump files to restore your data. This is the point of the back-ups, after all. To restore a dump file, it's just a matter of having the mariadb client execute all of the SQL statements that the file contains. There are some things to consider before restoring from a dump file, so read this section all of the way through before restoring. One simple and perhaps clumsy method to restore from a dump file is to enter something like the following:

```bash
mariadb --user admin_restore --password < /data/backup/db1.sql
```

Again, this is not using [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md). The [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) utility is only for making back-up copies, not restoring databases. Instead, you would use the mariadb client, which will read the dump file's content in order to batch execute the SQL statements that it contains. Notice that the redirect for `STDOUT` is not used here, but the redirect for the standard input (`STDIN`); the less-than sign is used since the dump file is an input source. Also, notice that in this example a database isn't specified. That's given within the dump file.

#### Restoring One Table

The problem with restoring from a dump file is that you may overwrite tables or databases that you wish you hadn't. For instance, your dump file might be a few days old and only one table may have been lost. If you restore all of the databases or all of the tables in a database, you would be restoring the data back to it's state at the time of the backup, a few days before. This could be quite a disaster. This is why dumping by database and table can be handy. However, that could be cumbersome.

A simple and easy method of limiting a restoration would be to create temporarily a user who only has privileges for the table you want to restore. You would enter a [GRANT](../../reference/sql-statements/account-management-sql-statements/grant.md) statement like this:

```sql
GRANT SELECT
ON db1.* TO 'admin_restore_temp'@'localhost' 
IDENTIFIED BY 'its_pwd';

GRANT ALL ON db1.table1
TO 'admin_restore_temp'@'localhost';
```

These two SQL statements allow the temporary user to have the needed [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) privileges on all of the tables of `db1` and `ALL` privileges for the `table1` table. Now when you restore the dump file containing the whole `db1` database, only `table1` will be replaced with the back-up copy. Of course, MariaDB will generate errors. To overlook the errors and to proceed with the restoration of data where no errors are generated (i.e., `table1`), use the `--force` option. Here's what you would enter at the command-line for this situation:

```bash
mariadb --user admin_restore_temp --password --force < /data/backup/db1.sql
```

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
