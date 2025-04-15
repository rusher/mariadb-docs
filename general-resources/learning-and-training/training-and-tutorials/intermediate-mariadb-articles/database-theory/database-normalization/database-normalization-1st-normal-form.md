
# Database Normalization: 1st Normal Form

This article follows on from the [Database Normalization Overview](database-normalization-overview.md).


At first, the data structure was as follows:


* Location code
* Location name
* 1-n plant numbers (1-n is a shorthand for saying there are many occurrences of this field. In other words, it is a repeating group).
* 1-n plant names
* 1-n soil categories
* 1-n soil descriptions


This is a completely unnormalized structure - in other words, it is in *zero normal form* So, to begin the normalization process, you start by moving from zero normal form to 1st normal form.


Tables are in 1st normal form if they follow these rules:


* There are no repeating groups.
* All the key attributes are defined.
* All attributes are dependent on the primary key.


What this means is that data must be able to fit into a tabular format, where each field contains one value. This is also the stage where the primary key is defined. Some sources claim that defining the primary key is not necessary for a table to be in first normal form, but usually it's done at this stage and is necessary before we can progress to the next stage. Theoretical debates aside, you'll have to define your primary keys at this point.


Although not always seen as part of the definition of 1st normal form, the principle of atomicity is usually applied at this stage as well. This means that all columns must contain their smallest parts, or be indivisible. A common example of this is where someone creates a *name* field, rather than *first name* and *surname* fields. They usually regret it later.


So far, the plant example has no keys, and there are repeating groups. To get it into 1st normal form, you'll need to define a primary key and change the structure so that there are no repeating groups; in other words, each row / column intersection contains one, and only one, value. Without this, you cannot put the data into the ordinary two-dimensional table that most databases require. You define location code and plant code as the primary key together (neither on its own can uniquely identify a record), and replace the repeating groups with a single-value attribute. After doing this, you are left with the structure shown in the table below (the primary key is in italics):



| Plant location table |
| --- |
| Plant location table |
| Location code |
| Location name |
| Plant code |
| Plant name |
| Soil category |
| Soil description |



This table is now in 1st normal formal. The process for turning a table into 2nd normal form is continued in the next article.

