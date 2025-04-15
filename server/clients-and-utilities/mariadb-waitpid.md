
# mariadb-waitpid

`<code>mariadb_waitpid</code>` is a utility for terminating processes. It runs on Unix-like systems, making use of the `<code>kill()</code>` system call.


Prior to [MariaDB 10.5](../../release-notes/mariadb-community-server/what-is-mariadb-105.md), the client was called `<code>mysql_waitpid</code>`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.


## Usage


```
mariadb-waitpid [options] pid time
```

## Description


`<code>mariadb-waitpid</code>` sends signal 0 to the process *pid* and waits up to *time* seconds for the process to terminate. *pid* and *time* must be positive integers.


Returns 0 if the process terminates in time, or does not exist, and 1 otherwise.


Signal 1 is used if the kill() system call cannot handle signal 0


## Options



| Option | Description |
| --- | --- |
| Option | Description |
| -?, --help | Display help and exit |
| -I, --help | Synonym for -? |
| -v, --verbose | Be more verbose. Give a warning, if kill can't handle signal 0 |
| -V, --version | Print version information and exit |


