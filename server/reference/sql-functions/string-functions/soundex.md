
# SOUNDEX

## Syntax


```
SOUNDEX(str)
```

## Description


Returns a soundex string from *`str`*. Two strings that sound almost the
same should have identical soundex strings. A standard soundex string is four
characters long, but the `SOUNDEX()` function returns an arbitrarily long
string. You can use `SUBSTRING()` on the result to get a standard soundex
string. All non-alphabetic characters in *`str`* are ignored. All
international alphabetic characters outside the A-Z range are treated as
vowels.


**Important:** When using SOUNDEX(), you should be aware of the
following details:


* This function, as currently implemented, is intended to work well with
 strings that are in the English language only. Strings in other languages may
 not produce reasonable results.


* This function implements the original Soundex algorithm, not the more popular enhanced version (also described by D. Knuth). The difference is that original version discards vowels first and duplicates second, whereas the enhanced version discards duplicates first and vowels second.


## Examples


```
SOUNDEX('Hello');
+------------------+
| SOUNDEX('Hello') |
+------------------+
| H400             |
+------------------+
```

```
SELECT SOUNDEX('MariaDB');
+--------------------+
| SOUNDEX('MariaDB') |
+--------------------+
| M631               |
+--------------------+
```

```
SELECT SOUNDEX('Knowledgebase');
+--------------------------+
| SOUNDEX('Knowledgebase') |
+--------------------------+
| K543212                  |
+--------------------------+
```

```
SELECT givenname, surname FROM users WHERE SOUNDEX(givenname) = SOUNDEX("robert");
+-----------+---------+
| givenname | surname |
+-----------+---------+
| Roberto   | Castro  |
+-----------+---------+
```

## See Also


* [SOUNDS LIKE](sounds-like.md)()


GPLv2 fill_help_tables.sql


{% @marketo/form formId="4316" %}
