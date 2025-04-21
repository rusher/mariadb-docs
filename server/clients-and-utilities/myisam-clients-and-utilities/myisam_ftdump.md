
# myisam_ftdump

myisam_ftdump is a utility for displaying information about [MyISAM](../../reference/storage-engines/myisam-storage-engine/README.md) [FULLTEXT](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md) indexes. It will scan and dump the entire index, and can be a lengthy process.


If the server is running, make sure you run a [FLUSH TABLES](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush.md) statement first.


## Usage


```
myisam_ftdump <table_name> <index_num>
```

The table_name can be specified with or without the .MYI index extension.


The index number refers to the number of the index when the table was defined, starting at zero. For example, take the following table definition:


```
CREATE TABLE IF NOT EXISTS `employees_example` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(40) NOT NULL,
  `position` varchar(25) NOT NULL,
  `home_address` varchar(50) NOT NULL,
  `home_phone` varchar(12) NOT NULL,
  `employee_code` varchar(25) NOT NULL,
  `bio` text NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `employee_code` (`employee_code`),
  FULLTEXT (`bio`)
) ENGINE=MyISAM;
```

The fulltext index will be `2`. The primary key is index `0`, and the unique key index `1`.


You can use *myisam_ftdump* to generate a list of index entries in order of frequency of occurrence as follows:


```
myisam_ftdump -c mytexttable 1 | sort -r
```

## Options



| Option | Description |
| --- | --- |
| Option | Description |
| -h, --help | Display help and exit. |
| -?, --help | Synonym for -h. |
| -c, --count | Calculate per-word stats (counts and global weights). |
| -d, --dump | Dump index (incl. data offsets and word weights). |
| -l, --length | Report length distribution. |
| -s, --stats | Report global stats. |
| -v, --verbose | Be verbose. |


