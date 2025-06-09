
# Backup/Restore + Data Export/Import via dbForge Studio

dbForge Studio is a proprietary third-party tool, not included with MariaDB Server. Content contributed by devart.


Without a doubt, you want your backup/restore and export/import operations to be fast, easy, and automated wherever possible. You can have it all that way with [dbForge Studio for MySQL](https://www.devart.com/dbforge/mysql/studio/). As the name implies, it is an IDE for MySQL development, management, and administration, yet it works just as perfectly as a [MariaDB GUI client](https://www.devart.com/dbforge/mysql/studio/mariadb-gui-client.html). Now, let's see how it tackles routine database backups.


## Create a MariaDB backup


1. On the **Database** menu, go to **Backup and Restore**, and click **Backup Database** to open **Database Backup Wizard**.


2. On the **General** page, specify the required connection and database, the path for the backup file to be saved to, and the output file name in the respective fields. Optionally, you can append a timestamp to the file name, enable the auto-deletion of old files, and compress your backup into an archive. After you set it all up, click **Next**.


![b1](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/b1.png "b1")


3. On the **Backup content** page, select the content for your backup and click **Next**.


![b2](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/b2.png "b2")


4. On the **Options** page, configure your detailed backup options—there are quite a few of those to match your requirements most precisely. Then click **Next**.


![b3](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/b3.png "b3")


5. On the **Errors handling** page, configure the **Errors handling** and **Log settings** options. Afterwards, click **Backup** to run the backup process.


Note that you have two more options here: you can select **Save Project** to save your current backup project with all the settings—or you can select **Save Command Line** to save a backup script that you can execute from the command line whenever you need.


![b4](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/b4.png "b4")


6. After you click **Backup**, wait for the backup process to be completed.


Note that you don't have to go through every wizard page to click **Backup**. You can do it whenever you've finished configuring your settings.


![b5](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/b5.png "b5")


7. Finally, confirm the successful completion by clicking **Finish**.


![b6](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/b6.png "b6")


As you can see, it's very easy. Furthermore, you can schedule to run regular backups using **Action > Create Basic Task** in **Windows Task Scheduler**.


## Restore a MariaDB backup


This is an even faster task, done in half as many steps.


1. On the **Database** menu, go to ***Backup and Restore**, and click **Restore Database** to open the **Database Restore Wizard**.


2. On the **Database Script File** page, specify the required connection and database, as well as the path to the previously saved backup file.


![r1](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/r1.png "r1")


3. After that, click **Restore**, and let the Studio do the rest for you.


And when it's done, click **Finish**, and there you have it.


![r2](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/r2.png "r2")


You can learn more about this functionality on the dedicated [backup/restore page](https://www.devart.com/dbforge/mysql/studio/mysql-backup.html). Please note: while the page focuses on MySQL databases, everything that's described there is just as perfectly applicable to MariaDB from the same Studio with the same workflow.


## Export data from MariaDB


With dbForge Studio, you can export data to 14 most popular formats: HTML, TXT, XLS, XLSX, MDB, RTF, PDF, JSON, XML, CSV, OBSC, DBF, SQL, and Google Sheets. You can do it with an easy-to-follow wizard that guides you through the entire process and delivers quite a few customization options.


Let's see how it works. And before we start, note that different formats may have slightly different wizard pages. In our walkthrough, we'll take the HTML format as an example.


1. To open the export wizard, on the **Database** menu, click **Export Data**.


2. On the **Export format** page, pick the required format and click **Next**.


![e1](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/e1.png "e1")


3. On the **Source** page, select the required connection, database, as well as tables and views to be exported. Then click **Next**.


![e2](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/e2.png "e2")


4. On the **Output settings** page, specify the path for the output, select to export data into a single or several separate files, and configure a few other settings, such as timestamps and compression. Then click **Next**.


![e3](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/e3.png "e3")


5. On the **Options** page, configure and preview table grid options for exported data. Click **Next**.


![e4](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/e4.png "e4")


6. On the **Data formats** page, you have two tabs. On the **Columns** tab, you can check the list of columns to be exported.


![e5](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/e5.png "e5")


Then, on the **Formats** tab, you can adjust the default format settings for Date, Time, Date Time, Currency, Float, Integer, Boolean, Null String, as well as select the required binary encoding.


![e6](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/e6.png "e6")


Once you make sure everything is correct, click **Next**.


7. On the **Exported rows** page, select to export all rows or define a certain range of rows, and then click *Next**.**


![e7](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/e7.png "e7")


8. On the **Errors handling** page, configure the errors handling behavior and select to keep a log file, if necessary.


![e8](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/e8.png "e8")


But before you click **Export**, note that you can save templates with your settings for recurring export operations. To do that, click **Save** in the lower left corner of the wizard, specify a name and a destination for the template file to be saved to, and then click **Save**.


![e9](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/e9.png "e9")


Also note that you don't have to go through every wizard page to click **Export**. You can do it whenever you've finished configuring your settings.


9. Finally, after you click **Export**, watch the progress and click **Finish** upon completion.


![e10](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/e10.png "e10")


Done! Now, if you want, you can open the folder with the output file right away.


## Import data into MariaDB


dbForge Studio supports 10 data formats for import, including TXT, XLS, XLSX, MDB, XML, JSON, CSV, ODBC, DBF, and Google Sheets. Just like with export, you have a helpful wizard at hand, whose pages may have differences, depending on the format. And let's pick a different format this time, say, the Microsoft Excel format (XLS).


1. To open the wizard, on the **Database** menu, click **Import Data**.


2. On the **Source file** page, choose the required format, select the file to import data from, and click **Next**.


![i1](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/i1.png "i1")


3. On the **Destination** page, select the target connection and database. Then you can select to import data either to a new table or to an existing table. Click **Next**.


![i2](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/i2.png "i2")


4. On the **Options** page, configure and preview table grid options for imported data. Click **Next**.


![i3](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/i3.png "i3")


5. On the **Data formats** page, you have two tabs. The first tab is called **Common Formats**, where you can specify the required formats for null strings, thousand and decimal separators, boolean variables, date and time.


![i4](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/i4.png "i4")


The second tab is called **Column Settings**, where you can configure format settings for separate columns.


![i5](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/i5.png "i5")


Once you make sure everything is correct, click **Next**.


6. On the **Mapping** page, you can map the source columns to the target ones and preview the results. If you're importing data into a new table, the Studio will automatically create and map all the columns, so you will only have to make adjustments if you wish. Then click **Next**.


![i6](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/i6.png "i6")


7. On the **Modes** page, select one of the 5 available import modes and click **Next**.


![i7](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/i7.png "i7")


8. On the **Output** page, select the preferred output option and click **Next**.


![i8](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/i8.png "i8")


9. On the **Errors handling** page, configure the errors handling behavior and select to keep a log file, if necessary.


![i9](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/i9.png "i9")


Similarly to export, you can save templates with your settings for recurring import operations. To do that, click **Save** in the lower left corner of the wizard, specify a name and a destination for the template file to be saved to, and then click **Save**.


![i10](../../.gitbook/assets/backup-restore-and-import-clients-backuprestore-data-exportimport-via-dbfor/+image/i10.png "i10")


Also note that you don't have to go through every wizard page to click **Import**. You can do it whenever you've finished configuring your settings.


10. After you click **Import**, wait for the process to be completed. Then click **Finish** to confirm the successful completion, and check the results if you wish. That's it!


You can learn more about this functionality on the dedicated [data export/import page](https://www.devart.com/dbforge/mysql/studio/data-export-import.html). Please note: while the page focuses on MySQL databases, everything that's described there is just as perfectly applicable to MariaDB from the same Studio with the same workflow.


There is much more to dbForge Studio when it comes to MariaDB development and management. You can have a brief overview of its features and capabilities on [the Features page](https://www.devart.com/dbforge/mysql/studio/features.html).


That said, if you'd love to have a single IDE that doesn't need any 3rd-party extensions because it can perfectly deal with nearly any task on its own, feel free to [download dbForge Studio for a free 30-day trial](https://www.devart.com/dbforge/mysql/studio/download.html) and give it a go in your daily work.


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
