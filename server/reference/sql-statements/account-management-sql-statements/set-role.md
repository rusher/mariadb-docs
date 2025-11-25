---
description: >-
  Activate the role for the current session. Learn how to enable none, or a
  specific role to change your active privileges dynamically.
---

# SET ROLE

## Syntax

```
SET ROLE { role | NONE }
```

## Description

{% hint style="info" %}
Only one role can be active at a time. Executing `SET ROLE` replaces the currently active role; it does not add to a list of active roles. This differs from MySQL, where you may activate several roles at a time.
{% endhint %}

The `SET ROLE` statement switches the active role for the current session, enabling its associated permissions. To unset a role, use `NONE`.

If a role that doesn't exist, or to which the user has not been assigned, is specified, an `ERROR 1959 (OP000): Invalid role specification` error occurs.

An automatic SET ROLE is implicitly performed when a user connects if that user has been assigned a default role. See [SET DEFAULT ROLE](set-default-role.md).

## Example

```sql
--Checking the current role status
SELECT CURRENT_ROLE;
```

{% code title="No role active" %}
```
+--------------+
| CURRENT_ROLE |
+--------------+
| NULL         |
+--------------+
```
{% endcode %}

```sql
--Setting the staff role, and verifying the switch
SET ROLE staff;
SELECT CURRENT_ROLE;
```

{% code title="'staff' role is active for the session" %}
```
+--------------+
| CURRENT_ROLE |
+--------------+
| staff        |
+--------------+
```
{% endcode %}

```sql
--switching to 'admin' role, and verifying the switch
SET ROLE admin;
SELECT CURRENT_ROLE;
```

{% code title="'staff' role is no longer active" %}
```
+--------------+
| CURRENT_ROLE |
+--------------+
| admin        |
+--------------+
```
{% endcode %}

```sql
--Removing the active role
SET ROLE NONE;
SELECT CURRENT_ROLE();
```

```
+----------------+
| CURRENT_ROLE() |
+----------------+
| NULL           |
+----------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
