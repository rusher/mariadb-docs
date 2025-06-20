
# Database Design: Overview

Databases exist because of the need to change data into information. Data are the raw and unprocessed facts. Information is obtained by processing the data into something useful. For example, millions of names and telephone numbers in a phone book are data. Information is the telephone number of the fire department when your house is burning down.


A database is a large repository of facts, designed in such a way that processing the facts into information is easy. If the phone book was structured in a less convenient way, such as with names and numbers placed in chronological order according to when the numbers were issued, converting the data into information would be much more difficult. Not knowing when the fire department was issued their latest number, you could search for days, and by the time you find the number your house would be a charred pile of ash. So, it's a good thing the phone book was designed as it was.


A database is much more flexible; a similar set of data to what's in a phone book could be ordered by MariaDB according to name, telephone number, address as well as chronologically. But databases are of course more complex, containing many different kinds of information. People, job titles and a company's products can all mingle to provide complex information. But this complexity makes the design of databases more complex as well. Poor design could make for slow queries, or it could even make certain kinds of information impossible to reach. This section of the documentation features articles about good database design, specifically:


* The database lifecycle
* Entity-relationship modeling
* Common mistakes in database design
* Real-world example: creating a publishing tracking system
* Concurrency control with transactions


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
