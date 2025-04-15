# Information Schema FEEDBACK Table

The [Information Schema](/en/information_schema/) `FEEDBACK` table is created when the [Feedback Plugin](../../../../../../plugins/other-plugins/feedback-plugin.md) is enabled, and contains the complete contents submitted by the plugin.

It contains two columns:

| Column | Description |
| --- | --- |
| Column | Description |
| VARIABLE_NAME | Name of the item of information being collected. |
| VARIABLE_VALUE | Contents of the item of information being collected. |

It is possible to disable automatic collection, by setting the `[feedback_url](../../../../../../plugins/other-plugins/feedback-plugin.md#feedback_url)` variable to an empty string, and to submit the contents manually, as follows:

```
$ mysql -e 'SELECT * FROM information_schema.FEEDBACK' > report.txt
```

Then you can send it by opening `[https://mariadb.org/feedback_plugin/post](https://mariadb.org/feedback_plugin/post)` in your
browser, and uploading your generated `report.txt`. Or you can do it from the
command line with (for example):

```
$ curl -F data=@report.txt https://mariadb.org/feedback_plugin/post
```

Manual uploading allows you to be absolutely
sure that we receive only the data shown in the `information_schema.FEEDBACK`
table and that no private or sensitive information is being sent.

#

# Example

```
SELECT * FROM information_schema.FEEDBACK\G
...
*************************** 906. row ***************************
 VARIABLE_NAME: Uname_sysname
VARIABLE_VALUE: Linux
*************************** 907. row ***************************
 VARIABLE_NAME: Uname_release
VARIABLE_VALUE: 3.13.0-53-generic
*************************** 908. row ***************************
 VARIABLE_NAME: Uname_version
VARIABLE_VALUE: #89-Ubuntu SMP Wed May 20 10:34:39 UTC 2015
*************************** 909. row ***************************
 VARIABLE_NAME: Uname_machine
VARIABLE_VALUE: x86_64
*************************** 910. row ***************************
 VARIABLE_NAME: Uname_distribution
VARIABLE_VALUE: lsb: Ubuntu 14.04.2 LTS
*************************** 911. row ***************************
 VARIABLE_NAME: Collation used latin1_german1_ci
VARIABLE_VALUE: 1
*************************** 912. row ***************************
 VARIABLE_NAME: Collation used latin1_swedish_ci
VARIABLE_VALUE: 18
*************************** 913. row ***************************
 VARIABLE_NAME: Collation used utf8_general_ci
VARIABLE_VALUE: 567
*************************** 914. row ***************************
 VARIABLE_NAME: Collation used latin1_bin
VARIABLE_VALUE: 1
*************************** 915. row ***************************
 VARIABLE_NAME: Collation used binary
VARIABLE_VALUE: 16
*************************** 916. row ***************************
 VARIABLE_NAME: Collation used utf8_bin
VARIABLE_VALUE: 4044
```