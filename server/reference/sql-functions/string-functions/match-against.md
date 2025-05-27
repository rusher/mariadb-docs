# MATCH AGAINST

## Syntax

```
MATCH (col1,col2,...) AGAINST (expr [search_modifier])
```

## Description

A special construct used to perform a fulltext search on a fulltext index.

See [Fulltext Index Overview](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/full-text-index-overview.md) for a full description, and [Full-text Indexes](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) for more articles on the topic.

## Examples

```
CREATE TABLE ft_myisam(copy TEXT,FULLTEXT(copy)) ENGINE=MyISAM;

INSERT INTO ft_myisam(copy) VALUES ('Once upon a time'), ('There was a wicked witch'), 
 ('Who ate everybody up');

SELECT * FROM ft_myisam WHERE MATCH(copy) AGAINST('wicked');
+--------------------------+
| copy                     |
+--------------------------+
| There was a wicked witch |
+--------------------------+
```

```
SELECT id, body, MATCH (title,body) AGAINST
    ('Security implications of running MySQL as root'
    IN NATURAL LANGUAGE MODE) AS score
    FROM articles WHERE MATCH (title,body) AGAINST
    ('Security implications of running MySQL as root'
    IN NATURAL LANGUAGE MODE);
+----+-------------------------------------+-----------------+
| id | body                                | score           |
+----+-------------------------------------+-----------------+
|  4 | 1. Never run mysqld as root. 2. ... | 1.5219271183014 |
|  6 | When configured properly, MySQL ... | 1.3114095926285 |
+----+-------------------------------------+-----------------+
```

GPLv2 fill\_help\_tables.sql
