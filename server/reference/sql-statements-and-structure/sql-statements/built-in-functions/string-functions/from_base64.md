
# FROM_BASE64

## Syntax


```
FROM_BASE64(str)
```

## Description


Decodes the given base-64 encode string, returning the result as a binary string. Returns `<code>NULL</code>` if the given string is `<code>NULL</code>` or if it's invalid.


It is the reverse of the `<code>[TO_BASE64](to_base64.md)</code>` function.


There are numerous methods to base-64 encode a string. MariaDB uses the following:


* It encodes alphabet value 64 as '`<code>+</code>`'.
* It encodes alphabet value 63 as '`<code>/</code>`'.
* It codes output in groups of four printable characters. Each three byte of data encoded uses four characters. If the final group is incomplete, it pads the difference with the '`<code>=</code>`' character.
* It divides long output, adding a new line very 76 characters.
* In decoding, it recognizes and ignores newlines, carriage returns, tabs and space whitespace characters.


```
SELECT TO_BASE64('Maria') AS 'Input';
+-----------+
| Input     |
+-----------+
| TWFyaWE=  |
+-----------+

SELECT FROM_BASE64('TWFyaWE=') AS 'Output';
+--------+
| Output |
+--------+
| Maria  |
+--------+
```
