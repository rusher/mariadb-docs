# DOUBLE PRECISION

#

# Syntax

```
DOUBLE PRECISION[(M,D)] [SIGNED | UNSIGNED | ZEROFILL]
REAL[(M,D)] [SIGNED | UNSIGNED | ZEROFILL]
```

#

# Description

REAL and DOUBLE PRECISION are synonyms for [DOUBLE](double.md).

Exception: If the REAL_AS_FLOAT [SQL mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/sql_modemssql) is enabled, 
REAL is a synonym for [FLOAT](floating-point-accuracy.md) rather than 
[DOUBLE](double.md).