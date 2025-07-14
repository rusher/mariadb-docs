
# Database Normalization: 2nd Normal Form


This article follows on from [Database Normalization: 1st Normal Form](database-normalization-1st-normal-form.md).


After converting to first normal form, the following table structure was achieved:



| Plant location table |
| --- |
| Location code |
| Location name |
| Plant code |
| Plant name |
| Soil category |
| Soil description |



Is this in 2nd normal form?


A table is in 2nd normal form if:


* it is in 1st normal form
* it includes no partial dependencies (where an attribute is only dependent on part of a primary key)


For an attribute to be only dependent on part of the primary key, the primary key must consist of more than one field. If the primary key contains only one field, the table is automatically in 2nd normal form if it is in 1st normal form


Let's examine all the fields. *Location name* is only dependent on *location code*. *Plant name*, *soil category*, and *soil description* are only dependent on *plant code* (this assumes that each plant only occurs in one soil type, which is the case in this example). So you remove each of these fields and place them in a separate table, with the key being that part of the original key on which they are dependent. For example, with *plant name*, the key is *plant code*. This leaves you with the tables below:


### Plant location table with partial dependencies removed



| Plant location table |
| --- |
| Plant code |
| Location code |



### Table resulting from fields dependent on plant code



| Plant table |
| --- |
| Plant code |
| Plant name |
| Soil category |
| Soil description |



### Table resulting from fields dependent on location code



| Location table |
| --- |
| Location code |
| Location name |



The resulting tables are now in 2nd normal form. The process for turning a table into 3rd normal form is continued in the next article.


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
