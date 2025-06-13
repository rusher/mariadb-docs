
# Understanding the Relational Database Model

The relational database model was a huge leap forward from the [network database model](understanding-the-network-database-model.md). Instead of relying on a parent-child or owner-member relationship, the relational model allows any file to be related to any other by means of a common field. Suddenly, the complexity of the design was greatly reduced because changes could be made to the database schema without affecting the system's ability to access data. And because access was not by means of paths to and from files, but from a direct relationship between files, new relations between these files could easily be added.


In 1970, when E.F. Codd developed the model, it was thought to be impractical. The increased ease of use comes at a large performance penalty, and the hardware in those days was not able to implement the model. Since then, of course, hardware has taken huge strides to where today, even the simplest computers can run sophisticated relational database management systems.


Relational databases go hand-in-hand with the development of SQL. The simplicity of SQL - where even a novice can learn to perform basic queries in a short period of time - is a large part of the reason for the popularity of the relational model.


The two tables below relate to each other through the *product_code* field. Any two tables can relate to each other simply by creating a field they have in common.


### Table 1



| Product_code | Description | Price |
| --- | --- | --- |
| Product_code | Description | Price |
| A416 | Nails, box | $0.14 |
| C923 | Drawing pins, box | $0.08 |



### Table 2



| Invoice_code | Invoice_line | Product_code | Quantity |
| --- | --- | --- | --- |
| Invoice_code | Invoice_line | Product_code | Quantity |
| 3804 | 1 | A416 | 10 |
| 3804 | 2 | C923 | 15 |




<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
