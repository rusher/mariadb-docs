# Remote connection work but often get error HY000/2002 connection timed out

Hi all,

I have create a remote connection between two linux server running mariadb.
One run centos stream 9 with 10.5.16-MariaDB and the second run centos 7 with 5.5.68-MariaDB.
Through php script automated with cron I run queries and it work.

The problem is that often i get the error HY000/2002 connection timed out. 
The error occurs at random times either using cron or launching it manually. 
For example, the script work for 10 times and on the 11th time I receive the error (HY000/2002 connection timed out) which can occur one or more times consecutively and then return to work on the umpteenth execution.
The number of times the script works or not is always different.

I can't find the cause of the error.
Any suggestions?

Thanks