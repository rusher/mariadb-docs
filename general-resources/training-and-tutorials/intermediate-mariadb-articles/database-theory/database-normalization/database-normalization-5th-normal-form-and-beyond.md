
# Database Normalization: 5th Normal Form and Beyond


This article follows on from the [4th normal form](database-normalization-4th-normal-form.md) article.


There are normal forms beyond 4th that are mainly of academic interest, as the problems they exist to solve rarely appear in practice. This series won't discuss then in detail, but for those interested, the following example provides a taste.


### The sales rep example



| Sales rep | Company | Product |
| --- | --- | --- |
| Sales rep | Company | Product |
| Felicia Powers | Exclusive | Books |
| Afzal Ignesund | Wordsworth | Magazines |
| Felicia Powers | Exclusive | Magazines |



Usually you would store this data in one table, as you need all three records to see which combinations are valid. *Afzal Ignesund* sells magazines for *Wordsworth*, but not necessarily books. *Felicia Powers* happens to sell both books and magazines for *Exclusive*. However, let's add another condition. If a sales rep sells a certain product, and they sell it for a particular company, then they must sell that product for that company.


Let's look at a larger data set adhering to this condition:


### Looking at a larger set of data



| Sales rep | Company | Product |
| --- | --- | --- |
| Sales rep | Company | Product |
| Felicia Powers | Exclusive | Books |
| Felicia Powers | Exclusive | Magazines |
| Afzal Ignesund | Wordsworth | Books |
| Felicia Powers | Wordsworth | Books |
| Felicia Powers | Wordsworth | Magazines |



Now, with this extra dependency, you could normalize the table above into three separate tables without losing any facts, as shown below:


### Creating a table with Sales rep and Product



| Sales rep | Product |
| --- | --- |
| Sales rep | Product |
| Felicia Powers | Books |
| Felicia Powers | Magazines |
| Afzal Ignesund | Books |



### Creating a table with Sales rep and Company



| Sales rep | Company |
| --- | --- |
| Sales rep | Company |
| Felicia Powers | Exclusive |
| Felicia Powers | Wordsworth |
| Afzal Ignesund | Wordsworth |



### Creating a table with Company and Product



| Company | Product |
| --- | --- |
| Company | Product |
| Exclusive | Books |
| Exclusive | Magazines |
| Wordsworth | Books |
| Wordsworth | Magazines |



Basically, a table is in 5th normal form if it cannot be made into any smaller tables with different keys (most tables can obviously be made into smaller tables with the same key!).


Beyond 5th normal form you enter the heady realms of domain key normal form, a kind of theoretical ideal. Its practical use to a database designer os similar to that of infinity to a bookkeeper - i.e. it exists in theory but is not going to be used in practice. Even the most demanding owner is not going to expect that of the bookkeeper!


For those interested in pursuing this academic and highly theoretical topic further, I suggest obtaining a copy of *An Introduction to Database Systems* by C.J. Date, at the time of writing in its 8th edition, or *Relational Theory for Computer Professionals* by the same author.


CC BY-SA / Gnu FDL

