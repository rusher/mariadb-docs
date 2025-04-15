
# Numeric Literals

Numeric literals are written as a sequence of digits from `<code>0</code>` to `<code>9</code>`. Initial zeros are ignored. A sign can always precede the digits, but it is optional for positive numbers. In decimal numbers, the integer part and the decimal part are divided with a dot (`<code>.</code>`).


If the integer part is zero, it can be omitted, but the literal must begin with a dot.


The notation with exponent can be used. The exponent is preceded by an `<code>E</code>` or `<code>e</code>` character. The exponent can be preceded by a sign and must be an integer. A number `<code>N</code>` with an exponent part `<code>X</code>`, is calculated as `<code>N * POW(10, X)</code>`.


In some cases, adding zeroes at the end of a decimal number can increment the precision of the expression where the number is used. For example, `<code>[PI()](../sql-statements/built-in-functions/numeric-functions/pi.md)</code>` by default returns a number with 6 decimal digits. But the `<code>PI()+0.0000000000</code>` expression (with 10 zeroes) returns a number with 10 decimal digits.


[Hexadecimal literals](hexadecimal-literals.md) are interpreted as numbers when used in numeric contexts.


## Examples


```
10
+10
-10
```

All these literals are equivalent:


```
0.1
.1
+0.1
+.1
```

With exponents:


```
0.2E3 -- 0.2 * POW(10, 3) = 200
.2e3
.2e+2
1.1e-10 -- 0.00000000011
-1.1e10 -- -11000000000
```
