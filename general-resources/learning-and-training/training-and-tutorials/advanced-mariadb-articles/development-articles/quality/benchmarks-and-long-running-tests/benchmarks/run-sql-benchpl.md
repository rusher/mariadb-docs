
# run-sql-bench.pl

`<code>run-sql-bench.pl</code>` is a perl script for automating runs of sql-bench
(You can find sql-bench in the [MariaDB source code](../../../../../../../../server/clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md).)


`<code>run-sql-bench.pl</code>` can be found in the
[mariadb-tools](mariadb-tools.md) project on Launchpad. Once you have a copy of mariadb-tools,
you'll find the script, and its configuration directories, in the `<code>sql-bench</code>` directory. For the purposes of this
article, wherever you located your local branch of `<code>mariadb-tools</code>` will be called `<code>${BASE_DIR}</code>`.


The `<code>run-sql-bench.pl</code>` script is located at
'`<code>${BASE_DIR}/sql-bench/run-sql-bench.pl</code>`'.


Example configuration scripts used for different runs can be found in the various subdirectories of `<code>${BASE_DIR}/sql-bench/</code>`.


To run the `<code>run-sql-bench.pl</code>` script, do the following:


1. [Branch a MariaDB or MySQL tree](../../../../../../../../server/clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md)
1. Optionally do some code changes in that tree and commit your changes
1. Edit `<code>run-sql-bench.pl</code>` to set internal options, especially the "`<code class="fixed" style="white-space:pre-wrap"><span class="k">my</span> <span class="nv">$path</span>
</code>`" variable.
1. Create a `<code>${BASE_DIR}/sql-bench/conf/host.cnf</code>` file for your system. An
 easy way to do this is by duplicating one of the example `<code>host.cnf</code>` files:
```
cp -avi ${BASE_DIR}/sql-bench/conf/pitbull.cnf ${BASE_DIR}/sql-bench/conf/${HOSTNAME}.cnf
```
Edit the file to customize it for your system.
1. Create `<code>${HOSTNAME}.cnf</code>` files under the `<code>${BASE_DIR}/sql-bench/basic</code>`, `<code>${BASE_DIR}/sql-bench/debug</code>`, `<code>${BASE_DIR}/sql-bench/debug-full</code>`,
 and `<code>${BASE_DIR}/sql-bench/O2</code>` directories, depending on which automated
 tests you want to run. Use the example files as a base and customize them for
 your system.
1. Run the `<code>run-sql-bench.pl</code>` script:
```
cd ${BASE_DIR}/sql-bench/; ./run-sql-bench.pl --repository=[/path/to/bzr/repository] --sql-bench-options=[additional sql-bench-options] --debug=[yes|no]
```


  * `<code><code>--</code>repository</code>` is the MariaDB tree to use and compile, the script will also look here for sql-bench.
  * `<code><code>--</code>sql-bench-options</code>` is mostly used in testing and debugging cases where
 we want to have short run times. For instance, using `<code><code>--</code>small-test</code>`
 or `<code><code>--</code>small-table</code>`.
  * You can separate several sql-bench options with spaces like so:
```
--sql-bench-options="--small-test --small-table"
```


## The results


Results are stored at the location specified by the `<code class="fixed" style="white-space:pre-wrap"><span class="nv">$sql_bench_results</span>
</code>` variable in the `<code>${BASE_DIR}/sql-bench/conf/hostname.cnf</code>` file for your host.
Results are organized in sub directories with the following schema:


```
sql-bench-results-dir/${HOSTNAME}/YYYY-MM-DD
```

## Future plans


* Crash and error detection and reporting.
* One should be able to specify a test name for each file (`<code>run-all-tests</code>` `<code><code>--</code>suffix='_xxxx'</code>`)

