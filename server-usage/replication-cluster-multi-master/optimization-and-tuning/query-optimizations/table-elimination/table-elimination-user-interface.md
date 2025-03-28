# Table Elimination User Interface

One can check that table elimination is working by looking at the
output of `EXPLAIN [EXTENDED]` and not finding there the
tables that were eliminated:

```
explain select ACRAT_rating from actors where ACNAM_name=’Gary Oldman’;
+----+--------------------+-----------+--------+---------------+---------+---------+----------------------+------+-------------+
| id | select_type | table | type | possible_keys | key | key_len | ref | rows | Extra |
+----+--------------------+-----------+--------+---------------+---------+---------+----------------------+------+-------------+
| 1 | PRIMARY | ac_anchor | index | PRIMARY | PRIMARY | 4 | NULL | 2 | Using index |
| 1 | PRIMARY | ac_name | eq_ref | PRIMARY | PRIMARY | 4 | test.ac_anchor.AC_ID | 1 | Using where |
| 1 | PRIMARY | ac_rating | ref | PRIMARY | PRIMARY | 4 | test.ac_anchor.AC_ID | 1 | |
| 3 | DEPENDENT SUBQUERY | sub | ref | PRIMARY | PRIMARY | 4 | test.ac_rating.AC_ID | 1 | Using index |
+----+--------------------+-----------+--------+---------------+---------+---------+----------------------+------+-------------+
```

Note that `ac_dob` table is not in the output. Now let's try
getting birthdate instead:

```
explain select ACDOB_birthdate from actors where ACNAM_name=’Gary Oldman’;
+----+-------------+-----------+--------+---------------+---------+---------+----------------------+------+-------------+
| id | select_type | table | type | possible_keys | key | key_len | ref | rows | Extra |
+----+-------------+-----------+--------+---------------+---------+---------+----------------------+------+-------------+
| 1 | PRIMARY | ac_anchor | index | PRIMARY | PRIMARY | 4 | NULL | 2 | Using index |
| 1 | PRIMARY | ac_name | eq_ref | PRIMARY | PRIMARY | 4 | test.ac_anchor.AC_ID | 1 | Using where |
| 1 | PRIMARY | ac_dob | eq_ref | PRIMARY | PRIMARY | 4 | test.ac_anchor.AC_ID | 1 | |
+----+-------------+-----------+--------+---------------+---------+---------+----------------------+------+-------------+
3 rows in set (0.01 sec)
```

The `ac_dob` table is there while `ac_rating`
and the subquery are gone. Now, if we just want to check the name of the actor:

```
explain select count(*) from actors where ACNAM_name=’Gary Oldman’;
+----+-------------+-----------+--------+---------------+---------+---------+----------------------+------+-------------+
| id | select_type | table | type | possible_keys | key | key_len | ref | rows | Extra |
+----+-------------+-----------+--------+---------------+---------+---------+----------------------+------+-------------+
| 1 | PRIMARY | ac_anchor | index | PRIMARY | PRIMARY | 4 | NULL | 2 | Using index |
| 1 | PRIMARY | ac_name | eq_ref | PRIMARY | PRIMARY | 4 | test.ac_anchor.AC_ID | 1 | Using where |
+----+-------------+-----------+--------+---------------+---------+---------+----------------------+------+-------------+
2 rows in set (0.01 sec)
```

In this case it will eliminate both the `ac_dob` and
`ac_rating` tables.

Removing tables from a query does not make the query slower, and it does not
cut off any optimization opportunities, so table elimination is unconditional
and there are no plans on having any kind of query hints for it.

For debugging purposes there is a `table_elimination=on|off`
switch in debug builds of the server.

#

# See Also

* This page is based on the following blog post about table elimination:
 [http://s.petrunia.net/blog/?p=58](http://s.petrunia.net/blog/?p=58)