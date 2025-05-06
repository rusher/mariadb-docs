
# Exploring Early Database Models

Before the advent of databases, the only way to store data was from unrelated files. Programmers had to go to great lengths to extract the data, and their programs had to perform complex parsing and relating.


Languages such as Perl, with its powerful regular expressions ideal for processing text, have made the job a lot easier than before; however, accessing the data from files is still a challenging task. Without a standard way to access data, systems are more prone to errors, are slower to develop, and are more difficult to maintain. Data redundancy (where data is duplicated unnecessarily) and poor data integrity (where data is not changed in all locations, leading to wrong or outdated data being supplied) are frequent consequences of the file access method of data storage. For these reasons, database management systems (DBMSs) were developed to provide a standard and reliable way to access and update data. They provide an intermediary layer between the application and the data, and the programmer is able to concentrate on developing the application, rather than worrying about data access issues.


A *database model* is a logical model concerned with how the data is represented. Instead of database designers worrying about the physical storage of data, the database model allows them to look at a higher, more conceptual level, reducing the gap between the real-world problem for which the application is being developed and the technical implementation.


There are a number of database models. The next two articles cover two common models; the [hierarchical database model](understanding-the-hierarchical-database-model.md) and the [network database model](understanding-the-network-database-model.md). After that comes the one MariaDB, along with most modern DBMSs uses, the relational model.


CC BY-SA / Gnu FDL

