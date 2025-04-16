
# Does the Password Prompt Appear Before or After Establishing a Connection?

**Question:** When I use the mysql client as in `mysql -u root -p -h <host>`, does the password-enter prompt popup before or after the client has established a connection with the server?


**Answer:** Before the client has established a connection to the server.


How do we derive the answer?


```
lovegood:~ byte$ mysql -uroot -p -hlocalhost
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 1
Server version: 5.2.8-MariaDB Source distribution

This software comes with ABSOLUTELY NO WARRANTY. This is free software,
and you are welcome to modify and redistribute it under the GPL v2 license

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> \q
Bye
lovegood:~ byte$ mysql.server stop
Shutting down MySQL
. SUCCESS! 
lovegood:~ byte$ mysql -uroot -p -hlocalhost
Enter password: 
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)
```
