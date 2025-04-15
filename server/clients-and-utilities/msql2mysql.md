
# msql2mysql

## Description


Initially, the MySQL C API was developed to be very similar to that of the
mSQL database system.


Because of this, mSQL programs often can be converted relatively easily for use
with MySQL by changing the names of their C API functions.


The `<code>msql2mysql</code>` utility performs the conversion of mSQL C API
function calls to their MySQL equivalents.


**Warning:** `<code>msql2mysql</code>` converts the input
file in place, so make a copy of the original before converting it.


## Example


```
shell> cp client-prog.c client-prog.c.orig
shell> msql2mysql client-prog.c
client-prog.c converted
```

After conversion, examine `<code>client-prog.c</code>` and make any necessary
post-conversion revisions.


`<code>msql2mysql</code>` uses the `<code>[replace](replace-utility.md)</code>` utility to make the function name
substitutions.

