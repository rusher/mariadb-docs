
# ACID: Concurrency Control with Transactions

Database requests happen in linear fashion, one after another. When many users are accessing a database, or one user has a related set of requests to run, it becomes important to ensure that the results remain consistent. To achieve this, you use *transactions*, which are groups of database requests that are processed as a whole. Put another way, they are logical units of work.


To ensure data integrity, transactions need to adhere to four conditions: atomicity, consistency, isolation and durability (ACID).


### Atomicity


*Atomicity* means the entire transaction must complete. If this is not the case, the entire transaction is aborted. This ensures that the database is never left with partially completed transactions, which would lead to data integrity issues. For example, if money is debited from one bank account but an error occurs before it can be credited to another account, the entire transaction must fail. The money cannot be lost or taken from one account without being successfully deposited into the other.


### Consistency


*Consistency* ensures that data adheres to predefined rules or constraints. For example, a rule might state that each invoice in the invoices table must be linked to a customer in the customers table. During a transaction, these rules can be temporarily violated—such as inserting an invoice before adding the related customer—but only within the transaction itself. These temporary violations are not visible outside the transaction and are always resolved before the transaction is finalized.


### Isolation


*Isolation* ensures that data being used by one transaction is inaccessible to other transactions until the first transaction is complete. For example, if two people deposit $100 each into an account with a balance of $900, the first transaction must update the balance to $1,000, and the second must then update it to $1,100. If the second transaction reads the $900 balance before the first transaction finishes, both transactions will appear successful, but $100 will be lost. The second transaction must wait until the first completes to access the correct balance.


### Durability


*Durability* guarantees that once a transaction is committed, its effects are permanent, even in the event of a system failure. While a transaction is in progress, its changes are not yet permanent. If the database crashes before the transaction is committed, the system can be restored to a consistent state using backups, which reflect the state before the transaction started. A committed transaction cannot be undone by a failure.


CC BY-SA / Gnu FDL

