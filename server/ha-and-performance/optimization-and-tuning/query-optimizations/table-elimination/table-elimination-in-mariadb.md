# Table Elimination in MariaDB

The first thing the MariaDB optimizer does is to merge the `VIEW`\
definition into the query to obtain:

```sql
select ACRAT_rating
from
  ac_anchor
  left join ac_name on ac_anchor.AC_ID=ac_name.AC_ID
  left join ac_dob on ac_anchor.AC_ID=ac_dob.AC_ID
  left join ac_rating on (ac_anchor.AC_ID=ac_rating.AC_ID and
                          ac_rating.ACRAT_fromdate = 
                            (select max(sub.ACRAT_fromdate)
                             from ac_rating sub where sub.AC_ID = ac_rating.AC_ID))
where
 ACNAM_name='Gary Oldman'
```

It's important to realize that the obtained query has a useless part:

* `left join ac_dob on ac_dob.AC_ID=...` will produce exactly\
  one matching record:
  * `primary key(ac_dob.AC_ID)` guarantees that there will be\
    at most one match for any value of `ac_anchor.AC_ID`,
  * and if there won't be a match, `LEFT JOIN` will generate a\
    NULL-complemented “row”
* and we don't care what the matching record is, as table`ac_dob` is not used anywhere else in the query.

This means that the `left join ac_dob on ...` part can be\
removed from the query and this is what Table Elimination module does. The\
detection logic is rather smart, for example it would be able to remove the`left join ac_rating on ...` part as well, together with the\
subquery (in the above example it won't be removed because ac\_rating used in\
the selection list of the query). The Table Elimination module can also handle\
nested outer joins and multi-table outer joins.

## See Also

* This page is based on the following blog post about table elimination:[?p=58](https://petrunia.net/blog/?p=58)

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
