
# Database Normalization: 3rd Normal Form

This article follows on from [Database Normalization: 2nd Normal Form](database-normalization-2nd-normal-form.md).


After converting to second normal form, the following table structure was achieved:



| Plant location table |
| --- |
| Plant location table |
| Plant code |
| Location code |




| Plant table |
| --- |
| Plant table |
| Plant code |
| Plant name |
| Soil category |
| Soil description |




| Location table |
| --- |
| Location table |
| Location code |
| Location name |



Are these tables in 3rd normal form?


A table is in 3rd normal form if:


* it is in 2nd normal form
* it contains no transitive dependencies (where a non-key attribute is dependent on the primary key through another non-key attribute)


If a table only contains one non-key attribute, it is obviously impossible for a non-key attribute to be dependent on another non-key attribute. Any tables where this is the case that are in 2nd normal form are then therefore also in 3rd normal form.


As only the plant table has more than one non-key attribute, you can ignore the others because they are in 3rd normal form already. All fields are dependent on the primary key in some way, since the tables are in second normal form. But is this dependency on another non-key field? *Plant name* is not dependent on either *soil category* or *soil description*. Nor is *soil category* dependent on either *soil description* or *plant name*.


However, *soil description* is dependent on *soil category*. You use the same procedure as before, removing it, and placing it in its own table with the attribute that it was dependent on as the key. You are left with the tables below:


### Plant location table remains unchanged



| Plant location table |
| --- |
| Plant location table |
| Plant code |
| Location code |



### Plant table with soil description removed



| Plant table |
| --- |
| Plant table |
| Plant code |
| Plant name |
| Soil category |



### The new soil table



| Soil table |
| --- |
| Soil table |
| Soil category |
| Soil description |



### Location table remains unchanged



| Location table |
| --- |
| Location table |
| Location code |
| Location name |



All of these tables are now in 3rd normal form. 3rd normal form is usually sufficient for most tables because it avoids the most common kind of data anomalies. It's suggested getting most tables you work with to 3rd normal form before you implement them, as this will achieve the aims of normalization listed in [Database Normalization Overview](database-normalization-overview.md) in the vast majority of cases.


The normal forms beyond this, such as Boyce-Codd normal form and 4th normal form, are rarely useful for business applications. In most cases, tables in 3rd normal form are already in these normal forms anyway. But any skilful database practitioner should know the exceptions, and be able to normalize to the higher levels when required.


The next article covers Boyce-Codd normal form.


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
