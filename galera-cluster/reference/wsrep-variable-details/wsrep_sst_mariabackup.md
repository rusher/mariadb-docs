# wsrep\_sst\_mariabackup

The `wsrep_sst_mariabackup` script parses the following options:

```bash
~/myh/instances/10622$ cat bin/wsrep_sst_mariabackup | grep "parse_cnf sst"
    sfmt=$(parse_cnf sst streamfmt 'mbstream')
    tfmt=$(parse_cnf sst transferfmt 'socat')
    sockopt=$(parse_cnf sst sockopt)
    progress=$(parse_cnf sst progress)
    ttime=$(parse_cnf sst time 0)
    cpat=$(parse_cnf sst cpat "$cpat")
    scomp=$(parse_cnf sst compressor)
    sdecomp=$(parse_cnf sst decompressor)
    rlimit=$(parse_cnf sst rlimit)
    uextra=$(parse_cnf sst use-extra 0)
    speciald=$(parse_cnf sst 'sst-special-dirs' 1)
    stimeout=$(parse_cnf sst 'sst-initial-timeout' 300)
    ssyslog=$(parse_cnf sst 'sst-syslog' 0)
    sstlogarchive=$(parse_cnf sst 'sst-log-archive' 1)
    sstlogarchivedir=$(parse_cnf sst sst-log-archive-dir \
```
