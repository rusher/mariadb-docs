# wsrep\_sst\_common

The `wsrep_sst_common` script parses the following options:

```bash
~/myh/instances/10622$ cat bin/wsrep_sst_common | grep "parse_cnf" | grep sst
    WSREP_SST_OPT_AUTH=$(parse_cnf 'sst' 'wsrep-sst-auth')
    tcert=$(parse_cnf 'sst' 'tca')
    tcap=$(parse_cnf 'sst' 'tcapath')
    tpem=$(parse_cnf 'sst' 'tcert')
    tkey=$(parse_cnf 'sst' 'tkey')
```

