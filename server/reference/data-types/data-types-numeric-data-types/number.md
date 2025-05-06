
# NUMBER

```
NUMBER[(M[,D])] [SIGNED | UNSIGNED | ZEROFILL]
```

In [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/sql_modeoracle#synonyms-for-basic-sql-types), `NUMBER` is a synonym for [DECIMAL](decimal.md).


## EXAMPLES


Number_Example


```
SET sql_mode='oracle';
```

```
CREATE TABLE number_example (
  example NUMBER
);
```

```
SHOW CREATE TABLE number_example\G
```

```
*************************** 1. row ***************************
       Table: number_example
Create Table: CREATE TABLE "number_example" (
  "example" double DEFAULT NULL
)
```


CC BY-SA / Gnu FDL

