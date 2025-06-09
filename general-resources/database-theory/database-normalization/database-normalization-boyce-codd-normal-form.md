
# Database Normalization: Boyce-Codd Normal Form


This article follows on from [Database Normalization: 3rd Normal Form](database-normalization-3rd-normal-form.md)


E.F. Codd and R.F. Boyce, two of the people instrumental in the development of the database model, have been honored by the name of this normal form. E.F. Codd developed and expanded the relational model, and also developed normalization for relational models in 1970, while R.F. Boyce was one of the creators of Structured Query Language (then called SEQUEL).


In spite of some resources stating the contrary, Boyce-Codd normal form is not the same as 4th normal form. Let's look at an example of data anomalies, which are presented in 3rd normal form and solved by transforming into Boyce-Codd normal form, before defining it.


### Table containing data about the student, course, and instructor relationship



| Student Course Instructor table |
| --- |
| Student Course Instructor table |
| Student |
| Course |
| Instructor |



Assume that the following is true for the table above:


* Each instructor takes only one course
* Each course can have one or more instructors
* Each student only has one instructor per course
* Each student can take one or more courses


What would the key be? None of the fields on their own would be sufficient to uniquely identify a records, so you have to use two fields. Which two should you use?


Perhaps *student* and *instructor* seem like the best choice, as that would allow you to determine the *course*. Or you could use *student* and *course*, which would determine the *instructor*. For now, let's use *student* and *course* as the key:


### Using student and course as the key



| Student Course Instructor table |
| --- |
| Student Course Instructor table |
| Student |
| Course |
| Instructor |



What normal form is this table in? It's in [1st normal form](database-normalization-1st-normal-form.md), as it has a key and no repeating groups. It's also in [2nd normal form](database-normalization-2nd-normal-form.md), as the instructor is dependent on both other fields (students have many courses, and therefore instructors, and courses have many instructors). Finally, it's also in [3rd normal form](database-normalization-3rd-normal-form.md), as there is only one non-key attribute.


But there are still some data anomalies. Look at the data sample below:


### More data anomalies



| Student | Course | Instructor |
| --- | --- | --- |
| Student | Course | Instructor |
| Conrad Pienaar | Biology | Nkosizana Asmal |
| Dingaan Fortune | Mathematics | Kader Dlamini |
| Gerrie Jantjies | Science | Helen Ginwala |
| Mark Thobela | Biology | Nkosizana Asmal |
| Conrad Pienaar | Science | Peter Leon |
| Alicia Ncita | Science | Peter Leon |
| Quinton Andrews | Mathematics | Kader Dlamini |



The fact that Peter Leon teaches science is stored redundantly, as are Kader Dlamini with mathematics and Nkosizana Asmal with biology. The problem is that the *instructor* determines the *course*. Or put another, *course* is determined by *instructor*. The table conforms to [3rd normal form](database-normalization-3rd-normal-form.md) rules because no non-key attribute is dependent upon a non-key attribute! Again, you use the familiar method of removing this field and placing it into another table, along with its key:


### Student Instructor table after removing Course



| Student Course Instructor table |
| --- |
| Student Course Instructor table |
| Student |
| Instructor |



After removing the *course* field, the primary key needs to include both remaining fields to uniquely identify a record.


### Resulting Instructor table



| Student Course Instructor table |
| --- |
| Student Course Instructor table |
| Instructor |
| Course |



Although we had chosen course as part of the primary key in the original table, the instructor determines the course, which is why we make it the primary key in this table. As you can see, the redundancy problem has been solved.


Thus, a table is in Boyce-Codd normal form if:


* it is in 3rd normal form
* each determinant is a candidate key


That sounds scary! For most people new to database design, these are new terms. If you followed along with the example above, however, the terms will soon become clear:


* a determinant is an attribute that determines the value of another attribute.
* a candidate key is either the key or an alternate key (in other words, the attribute could be a key for that table)


In the initial table, *instructor* is not a candidate key (alone it cannot uniquely identify the record), yet it determines the course, so the table is not in Boyce-Codd normal form.


Let's look at the example again, and see what happens if you chose student and instructor as the key. What normal form is the table in this time?


### Using student and instructor as the key



| Student Course Instructor table |
| --- |
| Student Course Instructor table |
| Student |
| Instructor |
| Course |



Once again it's in 1st normal form because there is a primary key and there are no repeating groups. This time, though, it's not in 2nd normal form because *course* is determined by only part of the key: the instructor. By removing *course* and its key, instructor, you get the structure shown below:


### Removing course



| Student Instructor table |
| --- |
| Student Instructor table |
| Student |
| Instructor |



### Creating a new table with course



| Student Course Instructor table |
| --- |
| Student Course Instructor table |
| Instructor |
| Course |



Either way you do it, by making sure the tables are normalized into Boyce-Codd normal form, you get the same two resulting tables. It's usually the case that when there are alternate fields to choose as a key, it doesn't matter which ones you choose initially because after normalizing you get the same results either way.


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
