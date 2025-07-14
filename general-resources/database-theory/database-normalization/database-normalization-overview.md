
# Database Normalization Overview


Developed in the 1970's by E.F. Codd, database normalization is standard requirement of many database designs. Normalization is a technique that can help you avoid data anomalies and other problems with managing your data. It consists of transforming a table through various stages: *1st normal form*, *2nd normal form*, *3rd normal form*, and beyond.


It aims to:


* Eliminate data redundancies (and therefore use less space)
* Make it easier to make changes to data, and avoid anomalies when doing so
* Make referential integrity constraints easier to enforce
* Produce an easily comprehensible structure that closely resembles the situation the data represents, and allows for growth


Let's begin by creating a sample set of data. You'll walk through the process of normalization first without worrying about the theory, to get an understanding of the reasons you'd want to normalize. Once you've done that, we'll introduce the theory and the various stages of normalization, which will make the whole process described below much simpler the next time you do it.


Imagine you are working on a system that records plants placed in certain locations, and the soil descriptions associated with them.


The location:


* Location Code: 11
* Location name: Kirstenbosch Gardens


contains the following three plants:


* Plant code: 431
* Plant name: Leucadendron
* Soil category: A
* Soil description: Sandstone


* Plant code: 446
* Plant name: Protea
* Soil category: B
* Soil description: Sandstone/Limestone


* Plant code: 482
* Plant name: Erica
* Soil category: C
* Soil description: Limestone


The location:


* Location Code: 12
* Location name: Karbonkelberg Mountains


contains the following two plants:


* Plant code: 431
* Plant name: Leucadendron
* Soil category: A
* Soil description: Sandstone


* Plant code: 449
* Plant name: Restio
* Soil category: B
* Soil description: Sandstone/Limestone


Tables in a relational database are in a grid, or table format (MariaDB, like most modern DBMSs is a relational database), so let's rearrange this data in the form of a tabular report:


### Plant data displayed as a tabular report



| Location code | Location name | Plant code | Plant name | Soil category | Soil description |
| --- | --- | --- | --- | --- | --- |
| 11 | Kirstenbosch Gardens | 431 | Leaucadendron | A | Sandstone |
|  |  | 446 | Protea | B | Sandstone/limestone |
|  |  | 482 | Erica | C | Limestone |
| 12 | Karbonkelberg Mountains | 431 | Leucadendron | A | Sandstone |
|  |  | 449 | Restio | B | Sandstone/limestone |



How are you to enter this data into a table in the database? You could try to copy the layout you see above, resulting in a table something like the below. The null fields reflect the fields where no data was entered.


### Trying to create a table with plant data



| Location code | Location name | Plant code | Plant name | Soil category | Soil description |
| --- | --- | --- | --- | --- | --- |
| 11 | Kirstenbosch Gardens | 431 | Leucadendron | A | Sandstone |
| NULL | NULL | 446 | Protea | B | Sandstone/limestone |
| NULL | NULL | 482 | Erica | C | Limestone |
| 1 2 | Karbonkelberg Mountains | 431 | Leucadendron | A | Sandstone |
| NULL | NULL | 449 | Restio | B | Sandstone/limestone |



This table is not much use, though. The first three rows are actually a group, all belonging to the same location. If you take the third row by itself, the data is incomplete, as you cannot tell the location the Erica is to be found. Also, with the table as it stands, you cannot use the location code, or any other fields, as a primary key (remember, a primary key is a field, or list of fields, that uniquely identify one record). There is not much use in having a table if you can't uniquely identify each record in it.


So, the solution is to make sure each table row can stand alone, and is not part of a group, or set. To achieve this, remove the groups, or sets of data, and make each row a complete record in its own right, which results in the table below.


### Each record stands alone



| Location code | Location name | Plant code | Plant name | Soil category | Soil description |
| --- | --- | --- | --- | --- | --- |
| 11 | Kirstenbosch Gardens | 431 | Leucadendron | A | Sandstone |
| 11 | Kirstenbosch Gardens | 446 | Protea | B | Sandstone/limestone |
| 11 | Kirstenbosch Gardens | 482 | Erica | C | Limestone |
| 12 | Karbonkelberg Mountains | 431 | Leucadendron | A | Sandstone |
| 12 | Karbonkelberg Mountains | 449 | Restio | B | Sandstone/limestone |



Notice that the location code cannot be a primary key on its own. It does not uniquely identify a row of data. So, the primary key must be a combination of *location code* and *plant code*. Together these two fields uniquely identify a row of data. Think about it. You would never add the same plant type more than once to a particular location. Once you have the fact that it occurs in that location, that's enough. If you want to record quantities of plants at a location - for this example, you're just interested in the spread of plants - you don't need to add an entire new record for each plant; rather, just add a quantity field. If for some reason you would be adding more than one instance of a plant/location combination, you'd need to add something else to the key to make it unique.


So, now the data can go in table format, but there are still problems with it. The table stores the information that code *11* refers to *Kirstenbosch Gardens* three times! Besides the waste of space, there is another serious problem. Look carefully at the data below.


### Data anomaly



| Location code | Location name | Plant code | Plant name | Soil category | Soil description |
| --- | --- | --- | --- | --- | --- |
| 11 | Kirstenbosch Gardens | 431 | Leucadendron | A | Sandstone |
| 11 | Kirstenbosh Gardens | 446 | Protea | B | Sandstone/limestone |
| 11 | Kirstenbosch Gardens | 482 | Erica | C | Limestone |
| 12 | Karbonkelberg Mountains | 431 | Leucadendron | A | Sandstone |
| 12 | Karbonkelberg Mountains | 449 | Restio | B | Sandstone/limestone |



Did you notice anything strange? Congratulations if you did! *Kirstenbosch* is misspelled in the second record. Now imagine trying to spot this error in a table with thousands of records! By using the structure in the table above, the chances of data anomalies increases dramatically.


The solution is simple. You remove the duplication. What you are doing is looking for partial dependencies - in other words, fields that are dependent on a part of a key and not the entire key. Because both the location code and the plant code make up the key, you look for fields that are dependent only on location code or on plant name.


There are quite a few fields where this is the case. Location name is dependent on location code (plant code is irrelevant in determining project name), and plant name, soil code, and soil name are all dependent on plant number. So, take out all these fields, as shown in the table below:


### Removing the fields not dependent on the entire key



| Location code | Plant code |
| --- | --- |
| 11 | 431 |
| 11 | 446 |
| 11 | 482 |
| 12 | 431 |
| 12 | 449 |



Clearly you can't remove the data and leave it out of your database completely. You take it out, and put it into a new table, consisting of the fields that have the partial dependency and the fields on which they are dependent. For each of the *key* fields in the partial dependency, you create a new table (in this case, both are already part of the primary key, but this doesn't always have to be the case). So, you identified *plant name*, *soil description* and *soil category* as being dependent on *plant code*. The new table will consist of *plant code*, as a key, as well as plant name, soil category and soil description, as shown below:


### Creating a new table with location data



| Plant code | Plant name | Soil category | Soil description |
| --- | --- | --- | --- |
| 431 | Leucadendron | A | Sandstone |
| 446 | Protea | B | Sandstone/limestone |
| 482 | Erica | C | Limestone |
| 431 | Leucadendron | A | Sandstone |
| 449 | Restio | B | Sandstone/limestone |



You do the same process with the location data, shown below:


### Creating a new table with location data



| Location code | Location name |
| --- | --- |
| 11 | Kirstenbosch Gardens |
| 12 | Karbonkelberg Mountains |



See how these tables remove the earlier duplication problem? There is only one record that contains *Kirstenbosch Gardens*, so the chances of noticing a misspelling are much higher. And you aren't wasting space storing the name in many different records. Notice that the location code and plant code fields are repeated in two tables. These are the fields that create the relation, allowing you to associate the various plants with the various locations. Obviously there is no way to remove the duplication of these fields without losing the relation altogether, but it is far more efficient storing a small code repeatedly than a large piece of text.


But the table is still not perfect. There is still a chance for anomalies to slip in. Examine the table below carefully:


### Another anomaly



| Plant code | Plant name | Soil category | Soil description |
| --- | --- | --- | --- |
| 431 | Leucadendron | A | Sandstone |
| 446 | Protea | B | Sandstone/limestone |
| 482 | Erica | C | Limestone |
| 431 | Leucadendron | A | Sandstone |
| 449 | Restio | B | Sandstone |



The problem in the table above is that the Restio has been associated with Sandstone, when in fact, having a soil category of B, it should be a mix of sandstone and limestone (the soil category determines the soil description in this example). Once again you're storing data redundantly. The *soil category* to *soil description* relationship is being stored in its entirety for each plant. As before, the solution is to take out this excess data and place it in its own table. What you are in fact doing at this stage is looking for transitive relationships, or relationships where a nonkey field is dependent on another nonkey field. *Soil description*, although in one sense dependent on plant code (it did seem to be a partial dependency when we looked at it in the previous step), is actually dependent on *soil category*. So, *soil description* must be removed. Once again, take it out and place it in a new table, along with its actual key (*soil category*) as shown in the tables below:


### Plant data after removing the soil description



| Plant code | Plant name | Soil category |
| --- | --- | --- |
| 431 | Leucadendron | A |
| 446 | Protea | B |
| 482 | Erica | C |
| 449 | Restio | B |



### Creating a new table with the soil description



| Soil category | Soil description |
| --- | --- |
| A | Sandstone |
| B | Sandstone/limestone |
| C | Limestone |



You've cut down on the chances of anomalies once again. It is now impossible to mistakenly assume soil category B is associated with anything but a mix of sandstone and limestone. The soil description to soil category relationships are stored in only one place - the new *soil* table, where you can be much more certain they are accurate.


Often, when you're designing a system you don't yet have a complete set of test data available, and it's not necessary if you understand how the data relates. This article has used the tables and their data to demonstrate the consequences of storing data in tables that were not normalized, but without them you have to rely on dependencies between fields, which is the key to database normalization.


The following articles will describe the process more formally, starting with moving from unnormalized data (or zero normal form) to first normal form.


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
