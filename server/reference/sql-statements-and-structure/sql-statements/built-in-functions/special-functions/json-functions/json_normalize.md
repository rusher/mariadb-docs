
# JSON_NORMALIZE


##### MariaDB starting with [10.7.0](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1070-release-notes.md)
JSON_NORMALIZE was added in [MariaDB 10.7.0](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1070-release-notes.md).


## Syntax


```
JSON_NORMALIZE(json)
```

## Description


Recursively sorts keys and removes spaces, allowing comparison of json documents for equality.


## Examples


We may wish our application to use the database to enforce a unique constraint on the JSON contents, and we can do so using the JSON_NORMALIZE function in combination with a unique key.


For example, if we have a table with a JSON column:


```
CREATE TABLE t1 (
 id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
 val JSON,
 /* other columns here */
 PRIMARY KEY (id)
);
```

Add a unique constraint using JSON_NORMALIZE like this:


```
ALTER TABLE t1
   ADD COLUMN jnorm JSON AS (JSON_NORMALIZE(val)) VIRTUAL,
   ADD UNIQUE KEY (jnorm);
```

We can test this by first inserting a row as normal:


```
INSERT INTO t1 (val) VALUES ('{"name":"alice","color":"blue"}');
```

And then seeing what happens with a different string which would produce the same JSON object:


```
INSERT INTO t1 (val) VALUES ('{ "color": "blue", "name": "alice" }');
ERROR 1062 (23000): Duplicate entry '{"color":"blue","name":"alice"}' for key 'jnorm'
```

## See Also


* [JSON_EQUALS](json_equals.md)

