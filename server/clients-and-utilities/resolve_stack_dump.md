
# resolve_stack_dump

resolve_stack_dump is a tool that resolves numeric stack strace dumps into symbols.


## Usage


```
resolve_stack_dump [OPTIONS] symbols-file [numeric-dump-file]
```

The symbols-file should include the output from: `<code>nm --numeric-sort mariadbd</code>`.
The numeric-dump-file should contain a numeric stack trace from mariadbd.
If the numeric-dump-file is not given, the stack trace is read from stdin.


## Options



| Option | Description |
| --- | --- |
| Option | Description |
| -h, --help | Display this help and exit. |
| -V, --version | Output version information and exit. |
| -s, --symbols-file=name | Use specified symbols file. |
| -n, --numeric-dump-file=name | Read the dump from specified file. |


