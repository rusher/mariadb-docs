
# PCRE - Perl Compatible Regular Expressions


## PCRE Versions



| PCRE Version | Introduced | Maturity |
| --- | --- | --- |
| PCRE Version | Introduced | Maturity |
| [PCRE2](https://www.pcre.org/) 10.34 | [MariaDB 10.5.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md) | Stable |
| PCRE 8.43 | [MariaDB 10.1.39](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10139-release-notes.md) | Stable |
| PCRE 8.42 | [MariaDB 10.2.15](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.1.33](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10133-release-notes.md), [MariaDB 10.0.35](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10035-release-notes.md) | Stable |
| PCRE 8.41 | [MariaDB 10.2.8](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md), [MariaDB 10.1.26](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10126-release-notes.md), [MariaDB 10.0.32](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10032-release-notes.md) | Stable |
| PCRE 8.40 | [MariaDB 10.2.5](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1025-release-notes.md), [MariaDB 10.1.22](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10122-release-notes.md), [MariaDB 10.0.30](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10030-release-notes.md) | Stable |
| PCRE 8.39 | [MariaDB 10.1.15](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10115-release-notes.md), [MariaDB 10.0.26](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10026-release-notes.md) | Stable |
| PCRE 8.38 | [MariaDB 10.1.10](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10110-release-notes.md), [MariaDB 10.0.23](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10023-release-notes.md) | Stable |
| PCRE 8.37 | [MariaDB 10.1.5](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-5-release-notes.md), [MariaDB 10.0.18](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10018-release-notes.md) | Stable |
| PCRE 8.36 | [MariaDB 10.1.2](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-2-release-notes.md), [MariaDB 10.0.15](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10015-release-notes.md) | Stable |
| PCRE 8.35 | [MariaDB 10.1.0](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-0-release-notes.md), [MariaDB 10.0.12](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10012-release-notes.md) | Stable |
| PCRE 8.34 | [MariaDB 10.0.8](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1008-release-notes.md) | Stable |




## PCRE Enhancements


[MariaDB 10.0.5](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes.md) switched to the PCRE library, which significantly improved the power of the [REGEXP/RLIKE](regexp.md) operator.


The switch to PCRE added a number of features, including recursive patterns, named capture, look-ahead and look-behind assertions, non-capturing groups, non-greedy quantifiers, Unicode character properties, extended syntax for characters and character classes, multi-line matching, and many other.


Additionally, [MariaDB 10.0.5](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes.md) introduced three new functions that work with regular expressions: [REGEXP_REPLACE()](regexp_replace.md), [REGEXP_INSTR()](regexp_instr.md) and [REGEXP_SUBSTR()](regexp_substr.md).


Also, REGEXP/RLIKE, and the new functions, now work correctly with all multi-byte [character sets](../../../../../data-types/string-data-types/character-sets/README.md) supported by MariaDB, including East-Asian character sets (big5, gb2313, gbk, eucjp, eucjpms, cp932, ujis, euckr), and Unicode character sets (utf8, utf8mb4, ucs2, utf16, utf16le, utf32). In earlier versions of MariaDB (and all MySQL versions) REGEXP/RLIKE works correctly only with 8-bit character sets.


## New Regular Expression Functions


* [REGEXP_REPLACE(subject, pattern, replace)](regexp_replace.md) - Replaces all occurrences of a pattern.
* [REGEXP_INSTR(subject, pattern)](regexp_instr.md) - Position of the first appearance of a regex .
* [REGEXP_SUBSTR(subject,pattern)](regexp_substr.md) - Returns the matching part of a string.


See the individual articles for more details and examples.


## PCRE Syntax


In most cases PCRE is backward compatible with the old POSIX 1003.2 compliant regexp library (see [Regular Expressions Overview](regular-expressions-overview.md)), so you won't need to change your applications that use SQL queries with the REGEXP/RLIKE predicate.


[MariaDB 10.0.11](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10011-release-notes.md) introduced the [default_regex_flags](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_regex_flags) variable to address the remaining compatibilities between PCRE and the old regex library.


This section briefly describes the most important extended PCRE features. For more details please refer to the documentation on the [PCRE site](https://www.pcre.org/), or to the documentation which is bundled in the /pcre/doc/html/ directory of a MariaDB sources distribution. The pages pcresyntax.html and pcrepattern.html should be a good start. [Regular-Expressions.Info](https://www.regular-expressions.info/tutorial.html) is another good resource to learn about PCRE and regular expressions generally.


### Special Characters


PCRE supports the following escape sequences to match special characters:



| Sequence | Description |
| --- | --- |
| Sequence | Description |
| \a | 0x07 (BEL) |
| \cx | "control-x", where x is any ASCII character |
| \e | 0x1B (escape) |
| \f | 0x0C (form feed) |
| \n | 0x0A (newline) |
| \r | 0x0D (carriage return) |
| \t | 0x09 (TAB) |
| \ddd | character with octal code ddd |
| \xhh | character with hex code hh |
| \x{hhh..} | character with hex code hhh.. |



Note, the backslash characters (here, and in all examples in the sections below) must be escaped with another backslash, unless you're using the [SQL_MODE](../../../../../../server-management/variables-and-modes/sql-mode.md) `<code>NO_BACKSLASH_ESCAPES</code>`.


This example tests if a character has hex code 0x61:


```
SELECT 'a' RLIKE '\\x{61}';
-> 1
```

### Character Classes


PCRE supports the standard POSIX character classes such as `<code>alnum</code>`, `<code>alpha</code>`, `<code>blank</code>`, `<code>cntrl</code>`, `<code>digit</code>`, `<code>graph</code>`, `<code>lower</code>`, `<code>print</code>`, `<code>punct</code>`, `<code>space</code>`, `<code>upper</code>`, `<code>xdigit</code>`, with the following additional classes:



| Class | Description |
| --- | --- |
| Class | Description |
| ascii | any ASCII character (0x00..0x7F) |
| word | any "word" character (a letter, a digit, or an underscore) |



This example checks if the string consists of ASCII characters only:


```
SELECT 'abc' RLIKE '^[[:ascii:]]+$';
-> 1
```

### Generic Character Types


Generic character types complement the POSIX character classes and serve to simplify writing patterns:



| Class | Description |
| --- | --- |
| Class | Description |
| \d | a decimal digit (same as [:digit:]) |
| \D | a character that is not a decimal digit |
| \h | a horizontal white space character |
| \H | a character that is not a horizontal white space character |
| \N | a character that is not a new line |
| \R | a newline sequence |
| \s | a white space character |
| \S | a character that is not a white space character |
| \v | a vertical white space character |
| \V | a character that is not a vertical white space character |
| \w | a "word" character (same as [:word:]) |
| \W | a "non-word" character |



This example checks if the string consists of "word" characters only:


```
SELECT 'abc' RLIKE '^\\w+$';
-> 1
```

### Unicode Character Properties


`<code>\p{xx}</code>` is a character with the `<code>xx</code>` property, and `<code>\P{xx}</code>` is a character without the `<code>xx</code>` property.


The property names represented by `<code>xx</code>` above are limited to the Unicode script names, the general category properties, and "Any", which matches any character (including newline). Those that are not part of an identified script are lumped together as "Common".


#### General Category Properties For \p and \P



| Property | Description |
| --- | --- |
| Property | Description |
| C | Other |
| Cc | Control |
| Cf | Format |
| Cn | Unassigned |
| Co | Private use |
| Cs | Surrogate |
| L | Letter |
| Ll | Lower case letter |
| Lm | Modifier letter |
| Lo | Other letter |
| Lt | Title case letter |
| Lu | Upper case letter |
| L& | Ll, Lu, or Lt |
| M | Mark |
| Mc | Spacing mark |
| Me | Enclosing mark |
| Mn | Non-spacing mark |
| N | Number |
| Nd | Decimal number |
| Nl | Letter number |
| No | Other number |
| P | Punctuation |
| Pc | Connector punctuation |
| Pd | Dash punctuation |
| Pe | Close punctuation |
| Pf | Final punctuation |
| Pi | Initial punctuation |
| Po | Other punctuation |
| Ps | Open punctuation |
| S | Symbol |
| Sc | Currency symbol |
| Sk | Modifier symbol |
| Sm | Mathematical symbol |
| So | Other symbol |
| Z | Separator |
| Zl | Line separator |
| Zp | Paragraph separator |
| Zs | Space separator |



This example checks if the string consists only of characters with property N (number):


```
SELECT '1¼①' RLIKE '^\\p{N}+$';
-> 1
```

#### Special Category Properties For \p and \P



| Property | Description |
| --- | --- |
| Property | Description |
| Xan | Alphanumeric: union of properties L and N |
| Xps | POSIX space: property Z or tab, NL, VT, FF, CR |
| Xsp | Perl space: property Z or tab, NL, FF, CR |
| Xuc | A character than can be represented by a Universal Character Name |
| Xwd | Perl word: property Xan or underscore |



The property `<code>Xuc</code>` matches any character that can be represented by a Universal Character Name (in C++ and other programming languages). These include `<code>$</code>`, `<code>@</code>`, `<code>`</code>`, and all characters with Unicode code points greater than `<code>U+00A0</code>`, excluding the surrogates `<code>U+D800</code>`..`<code>U+DFFF</code>`.


#### Script Names For \p and \P


Arabic, Armenian, Avestan, Balinese, Bamum, Batak, Bengali, Bopomofo, Brahmi, Braille, Buginese, Buhid, Canadian_Aboriginal, Carian, Chakma, Cham, Cherokee, Common, Coptic, Cuneiform, Cypriot, Cyrillic, Deseret, Devanagari, Egyptian_Hieroglyphs, Ethiopic, Georgian, Glagolitic, Gothic, Greek, Gujarati, Gurmukhi, Han, Hangul, Hanunoo, Hebrew, Hiragana, Imperial_Aramaic, Inherited, Inscriptional_Pahlavi, Inscriptional_Parthian, Javanese, Kaithi, Kannada, Katakana, Kayah_Li, Kharoshthi, Khmer, Lao, Latin, Lepcha, Limbu, Linear_B, Lisu, Lycian, Lydian, Malayalam, Mandaic, Meetei_Mayek, Meroitic_Cursive, Meroitic_Hieroglyphs, Miao, Mongolian, Myanmar, New_Tai_Lue, Nko, Ogham, Old_Italic, Old_Persian, Old_South_Arabian, Old_Turkic, Ol_Chiki, Oriya, Osmanya, Phags_Pa, Phoenician, Rejang, Runic, Samaritan, Saurashtra, Sharada, Shavian, Sinhala, Sora_Sompeng, Sundanese, Syloti_Nagri, Syriac, Tagalog, Tagbanwa, Tai_Le, Tai_Tham, Tai_Viet, Takri, Tamil, Telugu, Thaana, Thai, Tibetan, Tifinagh, Ugaritic, Vai, Yi.


This example checks if the string consists only of Greek characters:


```
SELECT 'ΣΦΩ' RLIKE '^\\p{Greek}+$';
-> 1
```

### Extended Unicode Grapheme Sequence


The `<code>\X</code>` escape sequence matches a character sequence that makes an "extended grapheme cluster", i.e. a composite character that consists of multiple Unicode code points.


One of the examples of a composite character can be a letter followed by non-spacing accent marks. This example demonstrates that `<code>U+0045 LATIN CAPITAL LETTER E</code>` followed by `<code>U+0302 COMBINING CIRCUMFLEX ACCENT</code>` followed by `<code>U+0323 COMBINING DOT BELOW</code>` together form an extended grapheme cluster:


```
SELECT _ucs2 0x004503020323 RLIKE '^\\X$';
-> 1
```

See the [PCRE documentation](https://www.pcre.org) for the other types of extended grapheme clusters.


### Simple Assertions


An assertion specifies a certain condition that must match at a particular point, but without consuming characters from the subject string. In addition to the standard POSIX simple assertions `<code>^</code>` (that matches at the beginning of a line) and `<code>$</code>` (that matches at the end of a line), PCRE supports a number of other assertions:



| Assertion | Description |
| --- | --- |
| Assertion | Description |
| \b | matches at a word boundary |
| \B | matches when not at a word boundary |
| \A | matches at the start of the subject |
| \Z | matches at the end of the subject, also matches before a newline at the end of the subject |
| \z | matches only at the end of the subject |
| \G | matches at the first matching position in the subject |



This example cuts a word that consists only of 3 characters from a string:


```
SELECT REGEXP_SUBSTR('---abcd---xyz---', '\\b\\w{3}\\b');
-> xyz
```

Notice that the two `<code>\b</code>` assertions checked the word boundaries but did not get into the matching pattern.


The `<code>\b</code>` assertions work well in the beginning and the end of the subject string:


```
SELECT REGEXP_SUBSTR('xyz', '\\b\\w{3}\\b');
-> xyz
```

By default, the `<code>^</code>` and `<code>$</code>` assertions have the same meaning with `<code>\A</code>`, `<code>\Z</code>`, and `<code>\z</code>`. However, the meanings of `<code>^</code>` and `<code>$</code>` can change in multiline mode (see below). By contrast, the meanings of `<code>\A</code>`, `<code>\Z</code>`, and `<code>\z</code>` are always the same; they are independent of the multiline mode.


### Option Setting


A number of options that control the default match behavior can be changed within the pattern by a sequence of option letters enclosed between `<code>(?</code>` and `<code>)</code>`.



| Option | Description |
| --- | --- |
| Option | Description |
| (?i) | case insensitive match |
| (?m) | multiline mode |
| (?s) | dotall mode (dot matches newline characters) |
| (?x) | extended (ignore white space) |
| (?U) | ungreedy (lazy) match |
| (?J) | allow named subpatterns with duplicate names |
| (?X) | extra PCRE functionality (e.g. force error on unknown escaped character) |
| (?-...) | unset option(s) |



For example, `<code>(?im)</code>` sets case insensitive multiline matching.


A hyphen followed by the option letters unset the options. For example, `<code>(?-im)</code>` means case sensitive single line match.


A combined setting and unsetting is also possible, e.g. `<code>(?im-sx)</code>`.


If an option is set outside of subpattern parentheses, the option applies to the remainder of the pattern that follows the option. If an option is set inside a subpattern, it applies to the part of this subpattern that follows the option.


In this example the pattern `<code>(?i)m((?-i)aria)db</code>` matches the words `<code>MariaDB</code>`, `<code>Mariadb</code>`, `<code>mariadb</code>`, but not `<code>MARIADB</code>`:


```
SELECT 'MariaDB' RLIKE '(?i)m((?-i)aria)db';
-> 1

SELECT 'mariaDB' RLIKE '(?i)m((?-i)aria)db';
-> 1

SELECT 'Mariadb' RLIKE '(?i)m((?-i)aria)db';
-> 1

SELECT 'MARIADB' RLIKE '(?i)m((?-i)aria)db';
-> 0
```

This example demonstrates that the `<code>(?x)</code>` option makes the regexp engine ignore all white spaces in the pattern (other than in a class).


```
SELECT 'ab' RLIKE '(?x)a b';
-> 1
```

Note, putting spaces into a pattern in combination with the (?x) option can be useful to split different logical parts of a complex pattern, to make it more readable.


### Multiline Matching


Multiline matching changes the meaning of `<code>^</code>` and `<code>$</code>` from "the beginning of the subject string" and "the end of the subject string" to "the beginning of any line in the subject string" and "the end of any line in the subject string" respectively.


This example checks if the subject string contains two consequent lines that fully consist of digits:


```
SELECT 'abc\n123\n456\nxyz\n' RLIKE '(?m)^\\d+\\R\\d+$';
-> 1
```

Notice the `<code>(?m)</code>` option in the beginning of the pattern, which switches to the multiline matching mode.


### Newline Conventions


PCRE supports five line break conventions:


* `<code>CR (\r)</code>` - a single carriage return character
* `<code>LF (\n)</code>` - a single linefeed character
* `<code>CRLF (\r\n)</code>` - a carriage return followed by a linefeed
* any of the previous three
* any Unicode newline sequence


By default, the newline convention is set to any Unicode newline sequence, which includes:



| Sequence | Description |
| --- | --- |
| Sequence | Description |
| LF | (U+000A, carriage return) |
| CR | (U+000D, carriage return) |
| CRLF | (a carriage return followed by a linefeed) |
| VT | (U+000B, vertical tab) |
| FF | (U+000C, form feed) |
| NEL | (U+0085, next line) |
| LS | (U+2028, line separator) |
| PS | (U+2029, paragraph separator) |



The newline convention can be set by starting a pattern with one of the following sequences:



| Sequence | Description |
| --- | --- |
| Sequence | Description |
| (*CR) | carriage return |
| (*LF) | linefeed |
| (*CRLF) | carriage return followed by linefeed |
| (*ANYCRLF) | any of the previous three |
| (*ANY) | all Unicode newline sequences |



The newline conversion affects the `<code>^</code>` and `<code>$</code>` assertions, the interpretation of the dot metacharacter, and the behavior of `<code>\N</code>`.


Note, the new line convention does not affect the meaning of `<code>\R</code>`.


This example demonstrates that the dot metacharacter matches `<code>\n</code>`, because it is not a newline sequence anymore:


```
SELECT 'a\nb' RLIKE '(*CR)a.b';
-> 1
```

### Newline Sequences


By default, the escape sequence `<code>\R</code>` matches any Unicode newline sequences.


The meaning of `<code>\R</code>` can be set by starting a pattern with one of the following sequences:



| Sequence | Description |
| --- | --- |
| Sequence | Description |
| (*BSR_ANYCRLF) | any of CR, LF or CRLF |
| (*BSR_UNICODE) | any Unicode newline sequence |



### Comments


It's possible to include comments inside a pattern. Comments do not participate in the pattern matching. Comments start at the `<code>(?</code>`

# sequence and continue up to the next closing parenthesis:


```
SELECT 'ab12' RLIKE 'ab(?#expect digits)12';
-> 1
```

### Quoting


POSIX uses the backslash to remove a special meaning from a character. PCRE introduces a syntax to remove special meaning from a sequence of characters. The characters inside `<code>\Q</code>` ... `<code>\E</code>` are treated literally, without their special meaning.


This example checks if the string matches a dollar sign followed by a parenthesized name (a variable reference in some languages):


```
SELECT '$(abc)' RLIKE '^\\Q$(\\E\\w+\\Q)\\E$';
-> 1
```

Note that the leftmost dollar sign and the parentheses are used literally, while the rightmost dollar sign is still used to match the end of the string.


### Resetting the Match Start


The escape sequence `<code>\K</code>` causes any previously matched characters to be excluded from the final matched sequence. For example, the pattern: `<code>(foo)\Kbar</code>` matches `<code>foobar</code>`, but reports that it has matched `<code>bar</code>`. This feature is similar to a look-behind assertion. However, in this case, the part of the subject before the real match does not have to be of fixed length:


```
SELECT REGEXP_SUBSTR('aaa123', '[a-z]*\\K[0-9]*');
-> 123
```

### Non-Capturing Groups


The question mark and the colon after the opening parenthesis create a non-capturing group: `<code>(?:...)</code>`.


This example removes an optional article from a word, for example for better sorting of the results.


```
SELECT REGEXP_REPLACE('The King','(?:the|an|a)[^a-z]([a-z]+)','\\1');
-> King
```

Note that the articles are listed inside the left parentheses using the alternation operator `<code>|</code>` but they do not produce a captured subpattern, so the word followed by the article is referenced by `<code>'<br/>1'</code>` in the third argument to the function. Using non-capturing groups can be useful to save numbers on the sup-patterns that won't be used in the third argument of [REGEXP_REPLACE()](regexp_replace.md), as well as for performance purposes.


### Non-Greedy Quantifiers


By default, the repetition quantifiers `<code>?</code>`, `<code>*</code>`, `<code>+</code>` and `<code>{n,m}</code>` are "greedy", that is, they try to match as much as possible. Adding a question mark after a repetition quantifier makes it "non-greedy", so the pattern matches the minimum number of times possible.


This example cuts C comments from a line:


```
SELECT REGEXP_REPLACE('/* Comment1 */ i+= 1; /* Comment2 */', '/[*].*?[*]/','');
->  i+= 1;
```

The pattern without the non-greedy flag to the quantifier `<code>/[*].*[*]/</code>` would match the entire string between the leftmost `<code>/*</code>` and the rightmost `<code>*/</code>`.


### Atomic Groups


A sequence inside `<code>(?></code>`...`<code>)</code>` makes an atomic group. Backtracking inside an atomic group is prevented once it has matched; however, backtracking past to the previous items works normally.


Consider the pattern `<code>\d+foo</code>` applied to the subject string `<code>123bar</code>`. Once the engine scans `<code>123</code>` and fails on the letter `<code>b</code>`, it would normally backtrack to `<code>2</code>` and try to match again, then fail and backtrack to `<code>1</code>` and try to match and fail again, and finally fail the entire pattern. In case of an atomic group `<code>(?>\d+)foo</code>` with the same subject string `<code>123bar</code>`, the engine gives up immediately after the first failure to match `<code>foo</code>`. An atomic group with a quantifier can match all or nothing.


Atomic groups produce faster false results (i.e. in case when a long subject string does not match the pattern), because the regexp engine saves performance on backtracking. However, don't hurry to put everything into atomic groups. This example demonstrates the difference between atomic and non-atomic match:


```
SELECT 'abcc' RLIKE 'a(?>bc|b)c' AS atomic1;
-> 1

SELECT 'abc' RLIKE 'a(?>bc|b)c' AS atomic2;
-> 0
 
SELECT 'abcc' RLIKE 'a(bc|b)c' AS non_atomic1;
-> 1

SELECT 'abc' RLIKE 'a(bc|b)c' AS non_atomic2;
-> 1
```

The non-atomic pattern matches both `<code>abbc</code>` and `<code>abc</code>`, while the atomic pattern matches `<code>abbc</code>` only.


The atomic group `<code>(?>bc|b)</code>` in the above example can be "translated" as "if there is `<code>bc</code>`, then don't try to match as `<code>b</code>`". So `<code>b</code>` can match only if `<code>bc</code>` is not found.


Atomic groups are not capturing. To make an atomic group capturing, put it into parentheses:


```
SELECT REGEXP_REPLACE('abcc','a((?>bc|b))c','\\1');
-> bc
```

### Possessive quantifiers


An atomic group which ends with a quantifier can be rewritten using a so called "possessive quantifier" syntax by putting an additional `<code>+</code>` sign following the quantifier.


The pattern `<code>(?>\d+)foo</code>` from the previous section's example can be rewritten as `<code>\d++foo</code>`.


### Absolute and Relative Numeric Backreferences


Backreferences match the same text as previously matched by a capturing group. Backreferences can be written using:


* a backslash followed by a digit
* the `<code>\g</code>` escape sequence followed by a positive or negative number
* the `<code>\g</code>` escape sequence followed by a positive or negative number enclosed in braces


The following backreferences are identical and refer to the first capturing group:


* `<code>\1</code>`
* `<code>\g1</code>`
* `<code>\g{1}</code>`


This example demonstrates a pattern that matches "sense and sensibility" and "response and responsibility", but not "sense and responsibility":


```
SELECT 'sense and sensibility' RLIKE '(sens|respons)e and \\1ibility';
-> 1
```

This example removes doubled words that can unintentionally creep in when you edit a text in a text editor:


```
SELECT REGEXP_REPLACE('using using the the regexp regexp',
 '\\b(\\w+)\\s+\\1\\b','\\1');
-> using the regexp
```

Note that all double words were removed, in the beginning, in the middle and in the end of the subject string.


A negative number in a `<code>\g</code>` sequence means a relative reference. Relative references can be helpful in long patterns, and also in patterns that are created by joining fragments together that contain references within themselves. The sequence `<code>\g{-1}</code>` is a reference to the most recently started capturing subpattern before `<code>\g</code>`.


In this example `<code>\g{-1}</code>` is equivalent to `<code>\2</code>`:


```
SELECT 'abc123def123' RLIKE '(abc(123)def)\\g{-1}';     
-> 1

SELECT 'abc123def123' RLIKE '(abc(123)def)\\2';
-> 1
```

### Named Subpatterns and Backreferences


Using numeric backreferences for capturing groups can be hard to track in a complicated regular expression. Also, the numbers can change if an expression is modified. To overcome these difficulties, PCRE supports named subpatterns.


A subpattern can be named in one of three ways: `<code>(?<name></code>`...`<code>)</code>` or `<code>(?'name'</code>`...`<code>)</code>` as in Perl, or `<code>(?P<name></code>`...`<code>)</code>` as in Python. References to capturing subpatterns from other parts of the pattern, can be made by name as well as by number.


Backreferences to a named subpattern can be written using the .NET syntax `<code>\k{name}</code>`, the Perl syntax `<code>\k<name></code>` or `<code>\k'name'</code>` or `<code>\g{name}</code>`, or the Python syntax `<code>(?P=name)</code>`.


This example tests if the string is a correct HTML tag:


```
SELECT '<a href="../">Up</a>' RLIKE '<(?<tag>[a-z][a-z0-9]*)[^>]*>[^<]*</(?P=tag)>';
-> 1
```

### Positive and Negative Look-Ahead and Look-Behind Assertions


Look-ahead and look-behind assertions serve to specify the context for the searched regular expression pattern. Note that the assertions only check the context, they do not capture anything themselves!


This example finds the letter which is not followed by another letter (negative look-ahead):


```
SELECT REGEXP_SUBSTR('ab1','[a-z](?![a-z])');
-> b
```

This example finds the letter which is followed by a digit (positive look-ahead):


```
SELECT REGEXP_SUBSTR('ab1','[a-z](?=[0-9])');
-> b
```

This example finds the letter which does not follow a digit character (negative look-behind):


```
SELECT REGEXP_SUBSTR('1ab','(?<![0-9])[a-z]');
-> b
```

This example finds the letter which follows another letter character (positive look-behind):


```
SELECT REGEXP_SUBSTR('1ab','(?<=[a-z])[a-z]');
-> b
```

Note that look-behind assertions can only be of fixed length; you cannot have repetition operators or alternations with different lengths:


```
SELECT 'aaa' RLIKE '(?<=(a|bc))a';
ERROR 1139 (42000): Got error 'lookbehind assertion is not fixed length at offset 10' from regexp
```

### Subroutine Reference and Recursive Patterns


PCRE supports a special syntax to recourse the entire pattern or its individual subpatterns:



| Syntax | Description |
| --- | --- |
| Syntax | Description |
| (?R) | Recourse the entire pattern |
| (?n) | call subpattern by absolute number |
| (?+n) | call subpattern by relative number |
| (?-n) | call subpattern by relative number |
| (?&name) | call subpattern by name (Perl) |
| (?P>name) | call subpattern by name (Python) |
| \g<name> | call subpattern by name (Oniguruma) |
| \g'name' | call subpattern by name (Oniguruma) |
| \g<n> | call subpattern by absolute number (Oniguruma) |
| \g'n' | call subpattern by absolute number (Oniguruma) |
| \g<+n> | call subpattern by relative number |
| \g<-n> | call subpattern by relative number |
| \g'+n' | call subpattern by relative number |
| \g'-n' | call subpattern by relative number |



This example checks for a correct additive arithmetic expression consisting of numbers, unary plus and minus, binary plus and minus, and parentheses:


```
SELECT '1+2-3+(+(4-1)+(-2)+(+1))' RLIKE  '^(([+-]?(\\d+|[(](?1)[)]))(([+-](?1))*))$';
-> 1
```

The recursion is done using `<code>(?1)</code>` to call for the first parenthesized subpattern, which includes everything except the leading `<code>^</code>` and the trailing `<code>$</code>`.


The regular expression in the above example implements the following BNF grammar:


1. `<code class="fixed" style="white-space:pre-wrap"><expression> ::= <term> [(<sign> <term>)...]</code>`
1. `<code class="fixed" style="white-space:pre-wrap"><term> ::= [ <sign> ] <primary></code>`
1. `<code class="fixed" style="white-space:pre-wrap"><primary> ::= <number> | <left paren> <expression> <right paren></code>`
1. `<code class="fixed" style="white-space:pre-wrap"><sign> ::= <plus sign> | <minus sign></code>`


### Defining Subpatterns For Use By Reference


Use the `<code>(?(DEFINE)</code>`...`<code>)</code>` syntax to define subpatterns that can be referenced from elsewhere.


This example defines a subpattern with the name `<code>letters</code>` that matches one or more letters, which is further reused two times:


```
SELECT 'abc123xyz' RLIKE '^(?(DEFINE)(?<letters>[a-z]+))(?&letters)[0-9]+(?&letters)$';
-> 1
```

The above example can also be rewritten to define the digit part as a subpattern as well:


```
SELECT 'abc123xyz' RLIKE
 '^(?(DEFINE)(?<letters>[a-z]+)(?<digits>[0-9]+))(?&letters)(?&digits)(?&letters)$';
-> 1
```

### Conditional Subpatterns


There are two forms of conditional subpatterns:


```
(?(condition)yes-pattern)
(?(condition)yes-pattern|no-pattern)
```

The `<code>yes-pattern</code>` is used if the condition is satisfied, otherwise the `<code>no-pattern</code>` (if any) is used.


#### Conditions With Subpattern References


If a condition consists of a number, it makes a condition with a subpattern reference. Such a condition is true if a capturing subpattern corresponding to the number has previously matched.


This example finds an optionally parenthesized number in a string:


```
SELECT REGEXP_SUBSTR('a(123)b', '([(])?[0-9]+(?(1)[)])');
-> (123)
```

The `<code>([(])?</code>` part makes a capturing subpattern that matches an optional opening parenthesis; the `<code>[0-9]+</code>` part matches a number, and the `<code>(?(1)[)])</code>` part matches a closing parenthesis, but only if the opening parenthesis has been previously found.


#### Other Kinds of Conditions


The other possible condition kinds are: recursion references and assertions. See the [PCRE documentation](https://www.pcre.org) for details.


### Matching Zero Bytes (0x00)


PCRE correctly works with zero bytes in the subject strings:


```
SELECT 'a\0b' RLIKE '^a.b$';
-> 1
```

Zero bytes, however, are not supported literally in the pattern strings and should be escaped using the `<code>\xhh</code>` or `<code>\x{hh}</code>` syntax:


```
SELECT 'a\0b' RLIKE '^a\\x{00}b$';
-> 1
```

### Other PCRE Features


PCRE provides other extended features that were not covered in this document,
such as duplicate subpattern numbers, backtracking control, breaking utf-8
sequences into individual bytes, setting the match limit, setting the recursion
limit, optimization control, recursion conditions, assertion conditions and
more types of extended grapheme clusters. Please refer to the
[PCRE documentation](https://www.pcre.org) for details.


Enhanced regex was implemented as a GSoC 2013 project by Sudheera Palihakkara.


### default_regex_flags Examples


The [default_regex_flags](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_regex_flags) variable was introduced to address the remaining incompatibilities between PCRE and the old regex library. Here are some examples of its usage:


The default behaviour (multiline match is off)


```
SELECT 'a\nb\nc' RLIKE '^b$';
+---------------------------+
| '(?m)a\nb\nc' RLIKE '^b$' |
+---------------------------+
|                         0 |
+---------------------------+
```

Enabling the multiline option using the PCRE option syntax:


```
SELECT 'a\nb\nc' RLIKE '(?m)^b$';
+---------------------------+
| 'a\nb\nc' RLIKE '(?m)^b$' |
+---------------------------+
|                         1 |
+---------------------------+
```

Enabling the miltiline option using default_regex_flags


```
SET default_regex_flags='MULTILINE';
SELECT 'a\nb\nc' RLIKE '^b$';
+-----------------------+
| 'a\nb\nc' RLIKE '^b$' |
+-----------------------+
|                     1 |
+-----------------------+
```

### See Also


* [MariaDB upgrades to PCRE-8.34](https://blog.mariadb.org/mariadb-upgrades-to-pcre-8-34/)

