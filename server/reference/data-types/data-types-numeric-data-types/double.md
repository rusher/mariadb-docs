
# DOUBLE

## Syntax


```
DOUBLE[(M,D)] [SIGNED | UNSIGNED | ZEROFILL]
DOUBLE PRECISION[(M,D)] [SIGNED | UNSIGNED | ZEROFILL]
REAL[(M,D)] [SIGNED | UNSIGNED | ZEROFILL]
```


## Description


A normal-size (double-precision) floating-point number (see [FLOAT](float.md) for a single-precision floating-point number).


Allowable values are:


* `<code>-1.7976931348623157E+308</code>` to `<code>-2.2250738585072014E-308</code>`
* `<code>0</code>`
* `<code>2.2250738585072014E-308</code>` to `<code>1.7976931348623157E+308</code>`


These are the theoretical limits, based on the IEEE standard. The actual range
might be slightly smaller depending on your hardware or operating system.


`<code>M</code>` is the total number of digits and `<code>D</code>` is the number of digits
following the decimal point. If `<code>M</code>` and `<code>D</code>` are omitted, values are stored
to the limits allowed by the hardware. A double-precision
floating-point number is accurate to approximately 15 decimal places.


`<code>UNSIGNED</code>`, if specified, disallows negative values.


`<code>ZEROFILL</code>`, if specified, pads the number with zeros, up to the total number
of digits specified by `<code>M</code>`.


REAL and DOUBLE PRECISION are synonyms, unless the REAL_AS_FLOAT [SQL mode](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modemssql.md) is enabled, in which case REAL is a synonym for [FLOAT](float.md) rather than DOUBLE.


See [Floating Point Accuracy](floating-point-accuracy.md) for issues when using floating-point numbers.


For more details on the attributes, see [Numeric Data Type Overview](numeric-data-type-overview.md).


## Examples


```
CREATE TABLE t1 (d DOUBLE(5,0) zerofill);

INSERT INTO t1 VALUES (1),(2),(3),(4);

SELECT * FROM t1;
+-------+
| d     |
+-------+
| 00001 |
| 00002 |
| 00003 |
| 00004 |
+-------+
```
