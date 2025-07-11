# Relational Databases: Views

Views are virtual tables. They are only a structure, and contain no data. Their purpose is to allow a user to see a subset of the actual data. A view can consist of a subset of one table. For example, the _student view_, below, is a subset of the _student table_.

| Student View |
| ------------ |
| First name   |
| Surname      |
| Grade        |

| Student Table |
| ------------- |
| Student\_id   |
| First name    |
| Surname       |
| Grade         |
| Address       |
| Telephone     |

This view could be used to allow other students to see their fellow student's marks but not allow them access to personal information.

Alternatively, a view could be a combination of a number of tables, such as the view below:

| Student View |
| ------------ |
| First name   |
| Surname      |
| Grade        |

| Student Table |
| ------------- |
| Student\_id   |
| First name    |
| Surname       |
| Address       |
| Telephone     |

| Course Table       |
| ------------------ |
| Course\_id         |
| Course description |

| Grade Table | Student\_id |
| ----------- | ----------- |
| Student\_id |             |
| Course\_id  |             |
| Grade       |             |

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

For more use cases, see the [Views Tutorial](../tutorials.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
