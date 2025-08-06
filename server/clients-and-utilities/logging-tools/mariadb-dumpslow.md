# mariadb-dumpslow

{% hint style="info" %}
Previously, the client was called `mysqldumpslow`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.
{% endhint %}

`mariadb-dumpslow` is a tool to examine the [slow query log](../../server-management/server-monitoring-logs/slow-query-log/).

It parses the slow query log files, printing a summary result. Normally, mariadb-dumpslow groups queries that are similar except for the particular values of number and string data values. It “abstracts” these values to N and ´S´ when displaying summary output. The `-a` and `-n` options can be used to modify value abstracting behavior.

## Usage

```bash
mariadb-dumpslow [ options... ] [ logs... ]
```

## Options

| Option        | Description                                                                                                                                                                                                                                                                        |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -a            | Don't abstract all numbers to N and strings to 'S'                                                                                                                                                                                                                                 |
| -d, --debug   | Debug                                                                                                                                                                                                                                                                              |
| -g _PATTERN_  | Grep: only consider statements that include this string                                                                                                                                                                                                                            |
| --help        | Display help                                                                                                                                                                                                                                                                       |
| -h HOSTNAME   | Hostname of db server for _-slow.log filename (can be wildcard), default is '_', i.e. match all                                                                                                                                                                                    |
| -i NAME       | Name of server instance (if using mysql.server startup script)                                                                                                                                                                                                                     |
| -l            | Don't subtract lock time from total time                                                                                                                                                                                                                                           |
| -n _NUM_      | Abstract numbers with at least _NUM_ digits within names                                                                                                                                                                                                                           |
| -r            | Reverse the sort order (largest last instead of first)                                                                                                                                                                                                                             |
| -s _ORDER_    | What to sort by (aa, ae, al, ar, at, a, c, e, l, r, t). at is default. aa average rows affected ae aggregated number of rows examined al average lock time ar average rows sent at average query time a rows affected c count e rows examined l lock time r rows sent t query time |
| -t _NUM_      | Just show the top NUM queries.                                                                                                                                                                                                                                                     |
| -v, --verbose | Verbose mode.                                                                                                                                                                                                                                                                      |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
