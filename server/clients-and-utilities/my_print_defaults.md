# my\_print\_defaults

## my\_print\_defaults

`my_print_defaults` displays the options from option groups of option files. It is useful to see which options a particular tool will use.

Output is one option per line, displayed in the form in which they would be specified on the command line.

### Usage

```
my_print_defaults [OPTIONS] [groups]
```

### Options

| Option                 | Description                                                                                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Option                 | Description                                                                                                                                                  |
| -c, --config-file=name | Deprecated, please use --defaults-file instead. Name of config file to read; if no extension is given, default extension (e.g., .ini or .cnf) will be added. |
| -                      |                                                                                                                                                              |

## ,--debug\[=#] | In debug versions, write a debugging log. A typical debug\_options string is d:t:o,file\_name. The default is d:t:o,/tmp/my\_print\_defaults.trace. |

\| -c, --defaults-file=name | Like --config-file, except: if first option, then read this file only, do not read global or per-user config files; should be the first option. Removed in [MariaDB 10.8.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes). |\
\| -e, --defaults-extra-file=name | Read this file after the global config file and before the config file in the users home directory; should be the first option. Removed in [MariaDB 10.8.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes). |\
\| -g, --defaults-group-suffix=name | In addition to the given groups, read also groups with this suffix. Removed in [MariaDB 10.8.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes). |\
\| -e, --extra-file=name | Deprecated. Synonym for --defaults-extra-file. |\
\| --mariadbd | Read the same set of groups that the [mariadbd](../server-management/install-and-upgrade-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) binary does. From [MariaDB 10.11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-3-release-notes). |\
\| --mysqld | Read the same set of groups that the [mysqld](../server-management/install-and-upgrade-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) binary does. |\
\| -n, --no-defaults | Return an empty string (useful for scripts). |\
\| ?, --help | Display this help message and exit. |\
\| -v, --verbose | Increase the output level. |\
\| -V, --version | Output version information and exit. |

### Examples

```
my_print_defaults --defaults-file=example.cnf client client-server mysql
```

[mariadb-check](mariadb-check.md) reads from the \[mariadb-check] and \[client] sections, so the following would display the mariadb-check options.

```
my_print_defaults mariadb-check client
```

CC BY-SA / Gnu FDL
