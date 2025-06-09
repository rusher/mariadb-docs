
# Relational Databases: Views

Views are virtual tables. They are only a structure, and contain no data. Their purpose is to allow a user to see a subset of the actual data. A view can consist of a subset of one table. For example, the *student view*, below, is a subset of the *student table*.



| Student View |
| --- |
| Student View |
| First name |
| Surname |
| Grade |




| Student Table |
| --- |
| Student Table |
| Student_id |
| First name |
| Surname |
| Grade |
| Address |
| Telephone |



This view could be used to allow other students to see their fellow student's marks but not allow them access to personal information.


Alternatively, a view could be a combination of a number of tables, such as the view below:



| Student View |
| --- |
| Student View |
| First name |
| Surname |
| Grade |




| Student Table |
| --- |
| Student Table |
| Student_id |
| First name |
| Surname |
| Address |
| Telephone |




| Course Table |
| --- |
| Course Table |
| Course_id |
| Course description |




| Grade Table | Student_id |
| --- | --- |
| Grade Table |
| Student_id |
| Course_id |
| Grade |



Views are also useful for security. In larger organizations, where many developers may be working on a project, views allow developers to access only the data they need. What they don't need, even if it is in the same table, is hidden from them, safe from being seen or manipulated. It also allows queries to be simplified for developers. For example, without the view, a developer would have to retrieve the fields in the view with the following sort of query


```
SELECT first_name, surname, course_description, grade FROM student, grade, course 
  WHERE grade.student_id = student.student_id AND grade.course_id = course.course_id
```

With the view, a developer could do the same with the following:


```
SELECT first_name, surname, course_description, grade FROM student_grade_view
```

Much simpler for a junior developer who hasn't yet learned to do joins, and it's just less hassle for a senior developer too!


For more use cases, see the [Views Tutorial](https://mariadb.com/kb/en/views-tutorial/).


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
