
# Database Normalization: 4th Normal Form


This article is intended to be read after the [Boyce-Codd normal form](database-normalization-boyce-codd-normal-form.md) article.


Let's look at the situation where redundancies can creep in even though a table is in [Boyce-Codd normal form](database-normalization-boyce-codd-normal-form.md). Let's take the student / instructor / course example used in that article, but change one of the initial assumptions.


Assume that the following is true for the tables below:


* Each instructor takes only one course
* Each course can have one or more instructors
* Each student can have several instructors per course (this is different to the previous example)
* Each student can take one or more courses


### Student Course Instructor data, with several instructors per course


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
| Dingaan Fortune | Mathematics | Helen Ginwala |



The data is the same as before, except that Helen Ginwala is teaching science to Gerrie Jantjies as well as mathematics to Dingaan Fortune, and Dingaan Fortune is being taught by both Helen Ginwala and Kader Dlamini for mathematics.


The only possible key is a combination of all three attributes, as shown below. No other combination will uniquely identify a particular record.


### Three attributes as key



| Student Course Instructor table |
| --- |
| Student Course Instructor table |
| Student |
| Instructor |
| Course |



But this still has some potentially anomalous behavior. The fact that Kader Dlamini teaches mathematics is still stored more than once, as is the fact that Dingaan Thobela takes mathematics. The real problem is that the table stores more than one kind of fact: that of student-to-course relationship, as well as that of a student-to-instructor relationship. You can avoid this, as always, by separating the data into two tables, as shown below:


### Creating a table for the student to instructor relationship



| Student Instructor table |
| --- |
| Student Instructor table |
| Student |
| Instructor |



### Creating a table for the student to course relationship



| Student Instructor table |
| --- |
| Student Instructor table |
| Student |
| Course |



This situation exists when you have multiple multivalued dependencies. A multivalued dependency exists between two attributes when, for each value of the first attribute, there are one or more associated values of the second attribute. For each value of *student*, there were many values of *course*. This is the first multivalued dependency. Then, for each value of *student*, there are one or more associated values of *instructor*. This is the second multivalued dependency.


Thus, a table is in 4th normal form if:


* it is in Boyce-Codd normal form
* it does not contain more than one multivalued dependency


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
