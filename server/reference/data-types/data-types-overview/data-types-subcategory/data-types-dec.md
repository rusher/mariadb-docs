
# DEC


See [DECIMAL](https://mariadb.com/kb/en/data-types-decimal).


## EXAMPLES


```
CREATE TABLE dec_example (
  example DEC
);
```

```
SHOW CREATE TABLE dec_example\G
```

```
*************************** 1. row ***************************
       Table: dec_example
Create Table: CREATE TABLE `dec_example` (
  `example` decimal(10,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```
