# Information Schema APPLICABLE_ROLES Table

The [Information Schema](/en/information_schema/) `APPLICABLE_ROLES` table shows the [role authorizations](../../../../../../../security/user-account-management/roles/roles_overview.md) that the current user may use.

It contains the following columns:

| Column | Description | Added |
| --- | --- | --- |
| Column | Description | Added |
| GRANTEE | Account that the role was granted to. | |
| ROLE_NAME | Name of the role. | |
| IS_GRANTABLE | Whether the role can be granted or not. | |
| IS_DEFAULT | Whether the role is the user's default role or not | [MariaDB 10.1.3](/en/mariadb-1013-release-notes/) |

The current role is in the [ENABLED_ROLES](information-schema-enabled_roles-table.md) Information Schema table.

#

# Example

```
SELECT * FROM information_schema.APPLICABLE_ROLES;
+----------------+-------------+--------------+------------+
| GRANTEE | ROLE_NAME | IS_GRANTABLE | IS_DEFAULT |
+----------------+-------------+--------------+------------+
| root@localhost | journalist | YES | NO |
| root@localhost | staff | YES | NO |
| root@localhost | dd | YES | NO |
| root@localhost | dog | YES | NO |
+----------------+-------------+--------------+------------+
```