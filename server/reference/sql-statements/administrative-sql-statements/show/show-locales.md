# SHOW LOCALES

`SHOW LOCALES` was introduced as part of the [Information Schema plugin extension](broken-reference).

`SHOW LOCALES` is used to return [locales](../../../data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) information as part of the [Locales](../../../data-types/string-data-types/character-sets/internationalization-and-localization/locales-plugin.md) plugin. It requires this plugin to be installed to work.

While the [information\_schema.LOCALES](../system-tables/information-schema/information-schema-tables/information-schema-locales-table.md) table has 8 columns, the `SHOW LOCALES` statement will only display 4 of them:

## Example

```
SHOW LOCALES;
+-----+-------+-------------------------------------+------------------------+
| Id  | Name  | Description                         | Error_Message_Language |
+-----+-------+-------------------------------------+------------------------+
|   0 | en_US | English - United States             | english                |
|   1 | en_GB | English - United Kingdom            | english                |
|   2 | ja_JP | Japanese - Japan                    | japanese               |
|   3 | sv_SE | Swedish - Sweden                    | swedish                |
...
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
