
# WHILE

## Syntax


```
[begin_label:] WHILE search_condition DO
    statement_list
END WHILE [end_label]
```

## Description


The statement list within a `<code>WHILE</code>` statement is repeated as long as the
`<code>search_condition</code>` is true. statement_list consists of one or more
statements. If the loop must be executed at least once, `<code>[REPEAT ... LOOP](repeat-loop.md)</code>` can be used instead.


A `<code>WHILE</code>` statement can be [labeled](labels.md). end_label cannot be given unless
begin_label also is present. If both are present, they must be the
same.


## Examples


```
CREATE PROCEDURE dowhile()
BEGIN
  DECLARE v1 INT DEFAULT 5;

  WHILE v1 > 0 DO
    ...
    SET v1 = v1 - 1;
  END WHILE;
END
```
