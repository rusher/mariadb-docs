---
title: With both READ UNCOMMITTED ...
---

{% hint style="warning" %}
With both `READ UNCOMMITTED` and `READ COMMITTED` isolation levels, you can’t expect results to be deterministic between successive statements of the same transaction.
{% endhint %}
