
# UPDATEXML

## Syntax


```
UpdateXML(xml_target, xpath_expr, new_xml)
```

## Description


This function replaces a single portion of a given fragment of XML markup
`<code>xml_target</code>` with a new XML fragment `<code>new_xml</code>`, and then returns the
changed XML. The portion of `<code>xml_target</code>` that is replaced matches an XPath
expression `<code>xpath_expr</code>` supplied by the user. If no expression matching
`<code>xpath_expr</code>` is found, or if multiple matches are found, the function returns
the original `<code>xml_target</code>` XML fragment. All three arguments should be
strings.


## Examples


```
SELECT
    UpdateXML('<a><b>ccc</b><d></d></a>', '/a', '<e>fff</e>') AS val1,
    UpdateXML('<a><b>ccc</b><d></d></a>', '/b', '<e>fff</e>') AS val2,
    UpdateXML('<a><b>ccc</b><d></d></a>', '//b', '<e>fff</e>') AS val3,
    UpdateXML('<a><b>ccc</b><d></d></a>', '/a/d', '<e>fff</e>') AS val4,
    UpdateXML('<a><d></d><b>ccc</b><d></d></a>', '/a/d', '<e>fff</e>') AS val5
    \G
*************************** 1. row ***************************
val1: <e>fff</e>
val2: <a><b>ccc</b><d></d></a>
val3: <a><e>fff</e><d></d></a>
val4: <a><b>ccc</b><e>fff</e></a>
val5: <a><d></d><b>ccc</b><d></d></a>
1 row in set (0.00 sec)
```
