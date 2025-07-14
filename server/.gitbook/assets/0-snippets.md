
# Snippets for Markdown

This file is for snippets ready to copy & paste into Markdown files, handy when working on Markdown level, e.g. in GitHub.

## Classical Markdown

## GitBook Extensions

### Admonitions

The most-used types of admonitions in GitBook are `ìnfo` and `warning`.
```
{% hint style="info" %}
Text here
{% endhint %}
```

### Page Headers

This is a template for README.md pages (or folders in GitHub), although you can use it for any kind of page.

To turn on page navigation (previous/next), set pagination visibility to true.

```
---
description: >-
Page description (200 characters maximum)
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
---
```

### Tabs

Put version-specific information in tabs. The first tab should have a title of `Current`, while other tabs usually hold information about previous Server versions.

```
{% tabs %}
{% tab title="Current" %}
Text here
{% endtab %}
{% tab title="< 10.5.1" %}
Text here
{% endtab %}
{% endtabs %}
```

