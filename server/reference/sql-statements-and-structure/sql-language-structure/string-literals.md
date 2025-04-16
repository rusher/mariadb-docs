
# String Literals

Strings are sequences of characters and are enclosed with quotes.


The syntax is:


```
[_charset_name]'string' [COLLATE collation_name]
```

For example:


```
'The MariaDB Foundation'
_utf8 'Foundation' COLLATE utf8_unicode_ci;
```

Strings can either be enclosed in single quotes or in double quotes (the same character must be used to both open and close the string).


The ANSI SQL-standard does not permit double quotes for enclosing strings, and although MariaDB does by default, if the MariaDB server has enabled the [ANSI_QUOTES_SQL](../../../server-management/variables-and-modes/sql-mode.md#ansi_quotes) [SQL_MODE](../../../server-management/variables-and-modes/sql-mode.md), double quotes will be treated as being used for [identifiers](identifier-names.md) instead of strings.


Strings that are next to each other are automatically concatenated. For example:


```
'The ' 'MariaDB ' 'Foundation'
```

and


```
'The MariaDB Foundation'
```

are equivalent.


The `\` (backslash character) is used to escape characters (unless the [SQL_MODE](../../../server-management/variables-and-modes/sql-mode.md) hasn't been set to [NO_BACKSLASH_ESCAPES](../../../server-management/variables-and-modes/sql-mode.md#no_backslash_escapes)). For example:


```
'MariaDB's new features'
```

is not a valid string because of the single quote in the middle of the string, which is treated as if it closes the string, but is actually meant as part of the string, an apostrophe. The backslash character helps in situations like this:


```
'MariaDB\'s new features'
```

is now a valid string, and if displayed, will appear without the backslash.


```
SELECT 'MariaDB\'s new features';
+------------------------+
| MariaDB's new features |
+------------------------+
| MariaDB's new features |
+------------------------+
```

Another way to escape the quoting character is repeating it twice:


```
SELECT 'I''m here', """Double""";
+----------+----------+
| I'm here | "Double" |
+----------+----------+
| I'm here | "Double" |
+----------+----------+
```

## Escape Sequences


There are other escape sequences also. Here is a full list:



| Escape sequence | Character |
| --- | --- |
| Escape sequence | Character |
| \0 | ASCII NUL (0x00). |
| \' | Single quote (“'”). |
| \" | Double quote (“"”). |
| \b | Backspace. |
| \n | Newline, or linefeed,. |
| \r | Carriage return. |
| \t | Tab. |
| \Z | ASCII 26 (Control+Z). See note following the table. |
| \\ | Backslash (“\”). |
| \% | “%” character. See note following the table. |
| \_ | A “_” character. See note following the table. |



Escaping the `%` and `_` characters can be necessary when using the [LIKE](../sql-statements/built-in-functions/string-functions/like.md) operator, which treats them as special characters.


The ASCII 26 character (`\Z`) needs to be escaped when included in a batch file which needs to be executed in Windows. The reason is that ASCII 26, in Windows, is the end of file (EOF).


Backslash (`\`), if not used as an escape character, must always be escaped. When followed by a character that is not in the above table, backslashes will simply be ignored.

