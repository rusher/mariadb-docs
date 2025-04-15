
# myisamlog

`<code>myisamlog</code>` processes and returns the contents of a [MyISAM log file](../../server-management/server-monitoring-logs/myisam-log.md).


Invoke `<code>myisamlog</code>` like this:


```
shell> myisamlog [options] [log_file [tbl_name] ...]
shell> isamlog [options] [log_file [tbl_name] ...]
```

The default operation is update (`<code>-u</code>`). If a recovery is done (`<code>-r</code>`), all
writes and possibly updates and deletes are done and errors are only counted.
The default log file name is `<code>myisam.log</code>` for `<code>myisamlog</code>` and `<code>isam.log</code>`
for `<code>isamlog</code>` if no `<code>log_file</code>` argument is given. If tables are named on
the command line, only those tables are updated.


`<code>myisamlog</code>` supports the following options:



| Option | Description |
| --- | --- |
| Option | Description |
| -?, -I | Display a help message and exit. |
| -c N | Execute only N commands. |
| -f N | Specify the maximum number of open files. |
| -i | Display extra information before exiting. |
| -o offset | Specify the starting offset. |
| -p N | Remove N components from path. |
| -r | Perform a recovery operation. |
| -R record_pos_file record_pos | Specify record position file and record position. |
| -u | Displays update operations. |
| -v | Verbose mode. Print more output about what the program does. This option can be given multiple times (-vv, -vvv) to produce more and more output. |
| -w write_file | Specify the write file. |
| -V | Display version information. |


