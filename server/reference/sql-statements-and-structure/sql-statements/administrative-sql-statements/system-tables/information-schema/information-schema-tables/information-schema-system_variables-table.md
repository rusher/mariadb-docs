
# Information Schema SYSTEM_VARIABLES Table

The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>SYSTEM_VARIABLES</code>` table shows current values and various metadata of all [system variables](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md).


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| VARIABLE_NAME | System variable name. |
| SESSION_VALUE | Session value of the variable or NULL if the variable only has a global scope. |
| GLOBAL_VALUE | Global value of the variable or NULL if the variable only has a session scope. |
| GLOBAL_VALUE_ORIGIN | How the global value was set — a compile-time default, auto-configured by the server, configuration file (or a command line), with the SQL statement. |
| DEFAULT_VALUE | Compile-time default value of the variable. |
| VARIABLE_SCOPE | Global, session, or session-only. |
| VARIABLE_TYPE | Data type of the variable value. |
| VARIABLE_COMMENT | Help text, usually shown in mariadbd --help --verbose. |
| NUMERIC_MIN_VALUE | For numeric variables — minimal allowed value. |
| NUMERIC_MAX_VALUE | For numeric variables — maximal allowed value. |
| NUMERIC_BLOCK_SIZE | For numeric variables — a valid value must be a multiple of the "block size". |
| ENUM_VALUE_LIST | For ENUM, SET, and FLAGSET variables — the list of recognized values. |
| READ_ONLY | Whether a variable can be set with the SQL statement. Note that many "read only" variables can still be set on the command line. |
| COMMAND_LINE_ARGUMENT | Whether an argument is required when setting the variable on the command line. NULL when a variable can not be set on the command line. |
| GLOBAL_VALUE_PATH | Which config file the variable got its value from. NULL if not set in any config file. Added in [MariaDB 10.5.0](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md). |



## Example


```
SELECT * FROM information_schema.SYSTEM_VARIABLES 
  WHERE VARIABLE_NAME='JOIN_BUFFER_SIZE'\G
*************************** 1. row *****************************
        VARIABLE_NAME: JOIN_BUFFER_SIZE
        SESSION_VALUE: 131072
         GLOBAL_VALUE: 131072
  GLOBAL_VALUE_ORIGIN: COMPILE-TIME
        DEFAULT_VALUE: 131072
       VARIABLE_SCOPE: SESSION
        VARIABLE_TYPE: BIGINT UNSIGNED
     VARIABLE_COMMENT: The size of the buffer that is used for joins
    NUMERIC_MIN_VALUE: 128
    NUMERIC_MAX_VALUE: 18446744073709551615
   NUMERIC_BLOCK_SIZE: 128
      ENUM_VALUE_LIST: NULL
            READ_ONLY: NO
COMMAND_LINE_ARGUMENT: REQUIRED
```
