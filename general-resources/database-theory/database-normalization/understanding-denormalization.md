
# Understanding Denormalization

*Denormalization* is the process of reversing the transformations made during [normalization](README.md) for performance reasons. It's a topic that stirs controversy among database experts; there are those who claim the cost is too high and never denormalize, and there are those that tout its benefits and routinely denormalize.


For proponents of denormalization, the thinking is as follows: normalization creates more tables as you proceed towards higher normal forms, but more tables mean there are more joins to be made when data is retrieved, which in turn slows down your queries. For that reason, to improve the performance of certain queries, you can override the advantages to data integrity and return the data structure to a lower normal form.


A practical approach makes sense, taking into account the limitations of SQL and MariaDB in particular, but being cautious not to needless denormalize. Here are some suggestions:


* if your performance with a normalized structure is acceptable, you should not denormalize.
* if your performance is unacceptable, make sure normalizing will cause it to become acceptable. There are very likely to be other alternatives, such as better hardware, load balancing, etc. It's hard to undo structural changes later.
* be sure you are willing to trade decreased data integrity for the increase in performance.
* consider possible future scenario, where applications may place different requirements on the data. Denormalizing to enhance performance of a specific application makes your data structure dependent on that application, when in an ideal situation it will be application-independent.


The table below introduces a common structure where it may not be in your best interests to denormalize. Which normal form is it in?



| Customer table |
| --- |
| Customer table |
| ID |
| First name |
| Surname |
| Address line 1 |
| Address line 2 |
| Town |
| Zip code |



It must be in [1st normal form](database-normalization-1st-normal-form.md) because it has a primary key and there are no repeating groups. It must be in [2nd normal form](database-normalization-2nd-normal-form.md) because there's only one key, so there cannot be any partial dependencies. And [3rd normal form](database-normalization-3rd-normal-form.md)? Are there any transitive dependencies? It looks like it. *Zip Code* is probably determined by the town attribute. To transform it into [3rd normal form](database-normalization-3rd-normal-form.md), you should take out *Zi..p code*, putting it in a separate table with town as the key. In most cases, though, this is not worth doing. So although this table is not in 3rd normal form, separating the table is not worth the trouble. The more tables you have, the more joins you need to do, which slows the system down. The reason you normalize at all is to reduce the size of the tables by removing redundant data, and doing do can often speed up the system.


But you also need to look at how your tables are used. *Town* and *Zip code* would almost always be returned together, as part of the address. In most cases, the small amount of space you save by removing the duplicate town/zip code combinations would not offset the slowing down of the system because of the extra joins. In some situations, this may be useful, perhaps where you need to sort addresses according to zip codes or towns for many thousands of customers, and the distribution of data means that a query to the new, smaller table can return the results substantially quicker. In the end, experienced database designers can go beyond rigidly following the steps, as they understand how the data will be used. And that is something only experience can teach you. Normalization is just a helpful set of steps that most often produces an efficient table structure, and not a rule for database design.


There are some scary database designs out there, almost always because of not normalizing rather than too much normalization. So if you're unsure, normalize!



<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
