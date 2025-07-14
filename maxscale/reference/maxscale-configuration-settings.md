# MaxScale Configuration Settings

## Configuration Settings

### General

#### [MaxScale](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

**Global Settings**

[**admin\_audit**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**admin\_audit\_exclude\_methods**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `GET`, `PUT`, `POST`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`, `CONNECT`, `TRACE`
* Default: No exclusions

[**admin\_audit\_file**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `/var/log/maxscale/admin_audit.csv`

[**admin\_auth**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**admin\_enabled**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**admin\_gui**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**admin\_host**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `"127.0.0.1"`

[**admin\_jwt\_algorithm**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `auto`, `HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`, `PS256`, `PS384`, `PS512`, `ES256`, `ES384`, `ES512`, `ED25519`, `ED448`
* Default: `auto`

[**admin\_jwt\_issuer**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `maxscale`

[**admin\_jwt\_key**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_jwt\_max\_age**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `24h`

[**admin\_log\_auth\_failures**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**admin\_oidc\_url**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_pam\_readonly\_service**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_pam\_readwrite\_service**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_port**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `8989`

[**admin\_readwrite\_hosts**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `%`

[**admin\_secure\_gui**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**admin\_ssl\_ca**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_ssl\_cert**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_ssl\_cipher**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No

[**admin\_ssl\_key**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_ssl\_version**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum\_mask](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`

[**admin\_verify\_url**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**auth\_connect\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**auto\_tune**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string list
* Values: `all` or list of auto tunable parameters, separated by `,`
* Default: No
* Mandatory: No
* Dynamic: No

[**cachedir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/cache/maxscale`

[**config\_sync\_cluster**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None

[**config\_sync\_db**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mysql`

[**config\_sync\_interval**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `5s`

[**config\_sync\_password**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: password
* Mandatory: No
* Dynamic: Yes
* Default: None

[**config\_sync\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**config\_sync\_user**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**connector\_plugindir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent

[**core\_file**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: true
* Dynamic: No

[**datadir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale`

[**debug**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**dump\_last\_statements**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `on_close`, `on_error`, `never`
* Default: `never`

[**execdir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/usr/bin`

[**host\_cache\_size**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: integer
* Default: 128
* Dynamic: Yes

[**key\_manager**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Dynamic: Yes
* Values: `none`, `file`, `kmip`, `vault`
* Default: `none`

[**language**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/`

[**libdir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent

[**load\_persisted\_configs**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**local\_address**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**log\_augmentation**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**log\_debug**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_info**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_notice**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**log\_throttling**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number, [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md), [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10, 1000ms, 10000ms`

[**log\_warn\_super\_user**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**log\_warning**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**logdir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/log/maxscale`

[**max\_auth\_errors\_until\_block**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`

[**maxlog**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**module\_configdir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/etc/maxscale.modules.d/`

[**ms\_timestamp**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**passive**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**persist\_runtime\_changes**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: true
* Dynamic: No

[**persistdir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/maxscale.cnf.d/`

[**piddir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/run/maxscale`

[**query\_classifier\_cache\_size**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [size](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: System Dependent

[**query\_retries**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1`

[**query\_retry\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**rebalance\_period**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

[**rebalance\_threshold**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `20`

[**rebalance\_window**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`

[**retain\_last\_statements**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**secretsdir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**session\_trace**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**session\_trace\_match**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**sharedir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/usr/share/maxscale`

[**skip\_name\_resolve**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**sql\_mode**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `default`, `oracle`
* Default: `default`

[**substitute\_variables**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**syslog**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**threads**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number or `auto`
* Mandatory: No
* Dynamic: No
* Default: `auto`

[**threads\_max**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: positive integer
* Default: 256
* Dynamic: No

[**trace\_file\_dir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No

[**trace\_file\_size**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [size](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes

[**users\_refresh\_interval**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

[**users\_refresh\_time**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `30s`

[**writeq\_high\_water**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [size](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `65536`

[**writeq\_low\_water**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [size](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `1024`

**Listener**

[**address**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `"::"`

[**authenticator**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**authenticator\_options**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**connection\_init\_sql\_file**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**connection\_metadata**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: stringlist
* Default: `character_set_client=auto,character_set_connection=auto,character_set_results=auto,max_allowed_packet=auto,system_time_zone=auto,time_zone=auto,tx_isolation=auto,maxscale=auto`
* Dynamic: Yes
* Mandatory: No

[**port**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: Yes, if `socket` is not provided.
* Dynamic: No
* Default: `0`

[**protocol**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: protocol
* Mandatory: No
* Dynamic: No
* Default: `mariadb`

[**service**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: service
* Mandatory: Yes
* Dynamic: No

[**socket**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes, if `port` is not provided.
* Dynamic: No
* Default: `""`

[**sql\_mode**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `default`, `oracle`
* Default: `default`

[**user\_mapping\_file**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

**Server**

[**address**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes, if `socket` is not provided.
* Dynamic: Yes
* Default: `""`

[**disk\_space\_threshold**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: Custom
* Mandatory: No
* Dynamic: No
* Default: None

[**extra\_port**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**max\_routing\_connections**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**monitorpw**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**monitoruser**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**persistmaxtime**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

[**persistpoolmax**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**port**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `3306`

[**priority**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0

[**private\_address**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**proxy\_protocol**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**rank**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `primary`, `secondary`
* Default: `primary`

[**replication\_custom\_options**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Default: None
* Dynamic: Yes

[**socket**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes, if `address` is not provided.
* Dynamic: Yes
* Default: `""`

**Service**

[**auth\_all\_servers**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**cluster**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None

[**connection\_keepalive**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `300s`
* Auto tune: [Yes](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

[**disable\_sescmd\_history**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**enable\_root\_user**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**filters**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: filter list
* Mandatory: No
* Dynamic: Yes
* Default: None

[**force\_connection\_keepalive**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: boolean
* Mandatory No
* Dynamic: Yes
* Default: `false`

[**idle\_session\_pool\_time**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `-1s`

[**log\_auth\_warnings**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**log\_debug**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_info**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_notice**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_warning**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**max\_connections**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**max\_sescmd\_history**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `50`

[**multiplex\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`

[**net\_write\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [durations](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory No
* Dynamic: Yes
* Default: `0s`

[**password**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**prune\_sescmd\_history**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**retain\_last\_statements**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `-1`

[**router**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: router
* Mandatory: Yes
* Dynamic: No

[**servers**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: server list
* Mandatory: No
* Dynamic: Yes
* Default: None

[**session\_track\_trx\_state**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**strip\_db\_esc**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**targets**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: target list
* Mandatory: No
* Dynamic: Yes
* Default: None

[**user**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**user\_accounts\_file**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**user\_accounts\_file\_usage**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `add_when_load_ok`, `file_only_always`
* Default: `add_when_load_ok`

[**version\_string**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: None

[**wait\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`
* Auto tune: [Yes](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

**Settings for File-based Key Manager**

[**file.keyfile**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: Yes
* Dynamic: Yes

**Settings for HashiCorp Vault Key Manager**

[**vault.ca**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Default: `""`
* Dynamic: Yes

[**vault.host**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Default: `localhost`
* Dynamic: Yes

[**vault.mount**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Default: `secret`
* Dynamic: Yes

[**vault.port**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: integer
* Default: `8200`
* Dynamic: Yes

[**vault.timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: 30s
* Dynamic: Yes

[**vault.tls**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: true
* Dynamic: Yes

[**vault.token**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: password
* Mandatory: Yes
* Dynamic: Yes

**Settings for KMIP Key Manager**

[**kmip.ca**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Default: `""`
* Dynamic: Yes

[**kmip.cert**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: Yes
* Dynamic: Yes

[**kmip.host**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**kmip.key**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: Yes
* Dynamic: Yes

[**kmip.port**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: integer
* Mandatory: Yes
* Dynamic: Yes

**Settings for TLS/SSL Encryption**

[**ssl**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**ssl\_ca**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_cert**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_cert\_verify\_depth**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `9`

[**ssl\_cipher**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_crl**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_key**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_verify\_peer\_certificate**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**ssl\_verify\_peer\_host**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory No
* Dynamic: Yes
* Default: `false`

[**ssl\_version**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum\_mask](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`

### Authenticators

#### [Authentication-Modules](https://github.com/mariadb-corporation/docs-server/blob/test/en/maxscale-25-01-authentication-modules/README.md)

**Settings**

[**lower\_case\_table\_names**](https://mariadb.com/kb/en/maxscale-25-01-authentication-modules/#lower_case_table_names)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `0`

[**match\_host**](https://mariadb.com/kb/en/maxscale-25-01-authentication-modules/#match_host)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**skip\_authentication**](https://mariadb.com/kb/en/maxscale-25-01-authentication-modules/#skip_authentication)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

#### [GSSAPI-Authenticator](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-gssapi-client-authenticator.md)

**Settings**

[**gssapi\_keytab\_path**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-gssapi-client-authenticator.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: Kerberos Default

[**principal\_name**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-gssapi-client-authenticator.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mariadb/localhost.localdomain`

#### [MySQL-Authenticator](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-mariadbmysql-authenticator.md)

**Settings**

[**log\_password\_mismatch**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-mariadbmysql-authenticator.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

#### [PAM-Authenticator](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)

**Settings**

[**pam\_backend\_mapping**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)

* Type: [enumeration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `none`, `mariadb`
* Default: `none`

[**pam\_mapped\_pw\_file**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: None

[**pam\_mode**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)

* Type: [enumeration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `password`, `password_2FA`, `suid`
* Default: `password`

[**pam\_use\_cleartext\_plugin**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

### Filters

#### [BinlogFilter](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-binlog-filter.md)

**Settings**

[**exclude**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-binlog-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**match**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-binlog-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**rewrite\_dest**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-binlog-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**rewrite\_src**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-binlog-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [CCRFilter](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)

**Settings**

[**count**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**global**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**ignore**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `""`

[**match**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `""`

[**options**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

[**time**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`

#### [Cache](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

**Settings**

[**cache\_in\_transactions**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `never`, `read_only_transactions`, `all_transactions`
* Default: `all_transactions`

[**cached\_data**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `shared`, `thread_specific`
* Default: `thread_specific`

[**clear\_cache\_on\_parse\_errors**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**debug**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**enabled**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**hard\_ttl**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)

[**invalidate**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `never`, `current`
* Default: `never`

[**max\_count**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

[**max\_resultset\_rows**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

[**max\_resultset\_size**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [size](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

[**max\_size**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [size](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

[**rules**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""` (no rules)

[**selects**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `assume_cacheable`, `verify_cacheable`
* Default: `assume_cacheable`

[**soft\_ttl**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)

[**storage**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `storage_inmemory`

[**storage\_options**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default:

[**timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `5s`

[**users**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `mixed`, `isolated`
* Default: `mixed`

**`storage_memcached`**

[**max\_value\_size**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [size](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: 1Mi

[**server**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: The Memcached server address specified as `host[:port]`
* Mandatory: Yes
* Dynamic: No

**`storage_redis`**

[**password**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**server**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: The Redis server address specified as `host[:port]`
* Mandatory: Yes
* Dynamic: No

[**ssl**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**ssl\_ca**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`

[**ssl\_cert**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`

[**ssl\_key**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`

[**username**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

#### [Comment](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-comment-filter.md)

**Settings**

[**inject**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-comment-filter.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

#### [LDIFilter](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

**Settings**

[**host**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `s3.amazonaws.com`

[**key**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes

[**no\_verify**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**port**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 0

[**protocol\_version**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 0
* Values: 0, 1, 2

[**region**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `us-east-1`

[**secret**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes

[**use\_http**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

#### [Masking](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

**Settings**

[**check\_subqueries**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: [bool](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**check\_unions**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: [bool](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**check\_user\_variables**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: [bool](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**large\_payload**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `ignore`, `abort`
* Default: `abort`

[**prevent\_function\_usage**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: [bool](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**require\_fully\_parsed**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: [bool](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**rules**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: path
* Mandatory: Yes
* Dynamic: Yes

[**treat\_string\_arg\_as\_field**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: [bool](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**warn\_type\_mismatch**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `never`, `always`
* Default: `never`

#### [Maxrows](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)

**Settings**

[**debug**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**max\_resultset\_return**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `empty`, `error`, `ok`
* Default: `empty`

[**max\_resultset\_rows**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: (no limit)

[**max\_resultset\_size**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)

* Type: [size](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `64Ki`

#### [Named-Server-Filter](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)

**Settings**

[**matchXY**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**options**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

[**source**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**targetXY**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**user**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [Query-Log-All-Filter](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

**Settings**

[**append**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [bool](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**duration\_unit**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `milliseconds`

[**exclude**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**filebase**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: string
* Mandatory: Yes
* Dynamic: No

[**flush**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [bool](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_data**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [enum\_mask](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `service`, `session`, `date`, `user`, `reply_time`, `total_reply_time`, `query`, `default_db`, `num_rows`, `reply_size`, `transaction`, `transaction_time`, `num_warnings`, `error_msg`
* Default: `date, user, query`

[**log\_type**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [enum\_mask](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `session`, `unified`, `stdout`
* Default: `session`

[**match**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**newline\_replacement**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `" "`

[**options**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [enum\_mask](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `case`, `ignorecase`, `extended`
* Default: `case`

[**separator**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `","`

[**source**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**source\_exclude**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes

[**source\_match**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes

[**use\_canonical\_form**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [bool](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**user**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**user\_exclude**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes

[**user\_match**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes

#### [Regex-Filter](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)

**Settings**

[**log\_file**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**log\_trace**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**match**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: Yes
* Dynamic: Yes

[**options**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

[**replace**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**source**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**user**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [RewriteFilter](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

**Settings**

[**case\_sensitive**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: boolean
* Mandatory: No
* Dynamic: Yes
* Default: true

[**log\_replacement**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: boolean
* Mandatory: No
* Dynamic: Yes
* Default: false

[**regex\_grammar**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: Native
* Values: `Native`, `ECMAScript`, `Posix`, `EPosix`, `Awk`, `Grep`, `EGrep`

[**template\_file**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Default: No default value

**Settings per template in the template file**

[**case\_sensitive**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: boolean
* Default: From maxscale.cnf

[**continue\_if\_matched**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: boolean
* Default: false

[**ignore\_whitespace**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: boolean
* Default: true

[**regex\_grammar**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: string
* Values: `Native`, `ECMAScript`, `Posix`, `EPosix`, `Awk`, `Grep`, `EGrep`
* Default: From maxscale.cnf

[**what\_if**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: boolean
* Default: false

#### [Tee-Filter](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

**Settings**

[**exclude**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**match**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**options**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

[**service**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

* Type: service
* Mandatory: No
* Dynamic: Yes
* Default: none

[**source**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**sync**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**target**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

* Type: target
* Mandatory: No
* Dynamic: Yes
* Default: none

[**user**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [Throttle](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-throttle.md)

**Settings**

[**continuous\_duration**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-throttle.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 2s

[**max\_qps**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-throttle.md)

* Type: number
* Mandatory: Yes
* Dynamic: Yes

[**sampling\_duration**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-throttle.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 250ms

[**throttling\_duration**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-throttle.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: Yes
* Dynamic: Yes

#### [Top-N-Filter](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)

**Settings**

[**count**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`

[**exclude**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**filebase**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**match**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**options**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `ignorecase`, `case`, `extended`
* Default: `case`

[**source**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**user**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [Wcar](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md)

**Settings**

[**capture\_dir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md)

* Type: path
* Default: /var/lib/maxscale/wcar/
* Mandatory: No
* Dynamic: No

[**capture\_duration**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: 0s
* Mandatory: No
* Dynamic: No

[**capture\_size**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md)

* Type: [size](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: 0
* Mandatory: No
* Dynamic: No

[**start\_capture**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md)

* Type: boolean
* Default: false
* Mandatory: No
* Dynamic: No

### Monitors

#### [Galera-Monitor](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)

**Settings**

[**available\_when\_donor**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)

* Type: boolean
* Default: false
* Dynamic: Yes

[**disable\_master\_failback**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)

* Type: boolean
* Default: false
* Dynamic: Yes

[**disable\_master\_role\_setting**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)

* Type: boolean
* Default: false
* Dynamic: Yes

[**root\_node\_as\_master**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)

* Type: boolean
* Default: false
* Dynamic: Yes

[**set\_donor\_nodes**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)

* Type: boolean
* Default: false
* Dynamic: Yes

[**use\_priority**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)

* Type: boolean
* Default: false
* Dynamic: Yes

#### [MariaDB-Monitor](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

**Settings**

[**assume\_unique\_hostnames**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**cooperative\_monitoring\_locks**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `majority_of_all`, `majority_of_running`
* Default: `none`

[**enforce\_read\_only\_servers**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**enforce\_read\_only\_slaves**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**enforce\_writable\_master**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**failcount**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `5`

[**maintenance\_on\_low\_disk\_space**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**master\_conditions**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [enum\_mask](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `connecting_slave`, `connected_slave`, `running_slave`, `primary_monitor_master`, `disk_space_ok`
* Default: `primary_monitor_master, disk_space_ok`

[**script\_max\_replication\_lag**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `-1`

[**slave\_conditions**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [enum\_mask](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `linked_master`, `running_master`, `writable_master`, `primary_monitor_master`
* Default: `none`

**Settings for Backup operations**

[**backup\_storage\_address**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**backup\_storage\_path**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None

[**rebuild\_port**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `4444`

[**ssh\_check\_host\_key**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**ssh\_keyfile**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None

[**ssh\_port**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `22`

[**ssh\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**ssh\_user**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

**Settings for Cluster manipulation operations**

[**auto\_failover**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `true`, `on`, `yes`, `1`, `false`, `off`, `no`, `0`, `safe`
* Default: `false`

[**auto\_rejoin**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**demotion\_sql\_file**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**enforce\_simple\_topology**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**failover\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`

[**handle\_events**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**master\_failure\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**promotion\_sql\_file**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**replication\_master\_ssl**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**replication\_password**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**replication\_user**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**servers\_no\_promotion**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**switchover\_on\_low\_disk\_space**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**switchover\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`

[**verify\_master\_failure**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

**Settings for Primary server write test**

[**write\_test\_fail\_action**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: `log`
* Values: `log`, `failover`
* Dynamic: Yes

[**write\_test\_interval**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Dynamic: Yes
* Default: 0s

[**write\_test\_table**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: string
* Dynamic: Yes
* Default: `mxs.maxscale_write_test`

#### [Monitor-Common](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

**Settings**

[**backend\_connect\_attempts**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `1`

[**backend\_connect\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

[**backend\_read\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

[**backend\_write\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

[**disk\_space\_check\_interval**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

[**disk\_space\_threshold**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**events**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: enum
* Mandatory: No
* Dynamic: Yes
* Values: `master_down`, `master_up`, `slave_down`, `slave_up`, `server_down`, `server_up`, `lost_master`, `lost_slave`, `new_master`, `new_slave`
* Default: All events

[**journal\_max\_age**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `28800s`

[**module**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: string
* Mandatory: Yes
* Dynamic: No

[**monitor\_interval**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `2s`

[**password**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**script**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**script\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`

[**servers**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**user**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

### Protocols

#### [MariaDB](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-mariadb-protocol-module.md)

**Settings**

[**allow\_replication**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-mariadb-protocol-module.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true

#### [NoSQL](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

**Settings**

[**authentication\_db**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `"NoSQL"`

[**authentication\_key\_id**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `""`

[**authentication\_password**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `""`

[**authentication\_required**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `false`

[**authentication\_shared**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `false`

[**authentication\_user**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: string
* Mandatory: Yes, if `authentication_shared` is true.

[**authorization\_enabled**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `false`

[**auto\_create\_databases**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `true`

[**auto\_create\_tables**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `true`

[**cursor\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `60s`

[**debug**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [enum\_mask](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Values: `none`, `in`, `out`, `back`
* Default: `none`

[**host**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `"%"`

[**id\_length**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: count
* Mandatory: No
* Range: `[35, 2048]`
* \*Default: `35`

[**internal\_cache**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: ''

[**log\_unknown\_command**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `false`

[**on\_unknown\_command**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Values: `return_error`, `return_empty`
* Default: `return_error`

[**ordered\_insert\_behavior**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Values: `atomic`, `default`
* Default: `default`

[**password**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `""`

[**user**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `""`

### Routers

#### [Avrorouter](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

**Settings**

[**avrodir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/`

[**binlogdir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/`

[**codec**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `null`, `deflate`
* Default: `null`

[**cooperative\_replication**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**exclude**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `""`

[**filestem**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mysql-bin`

[**gtid\_start\_pos**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**match**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `""`

[**server\_id**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1234`

[**start\_index**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1`

**Settings for Avro File**

[**block\_size**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: [size](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `16KiB`

[**group\_rows**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1000`

[**group\_trx**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1`

[**max\_data\_age**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: 0s

[**max\_file\_size**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: [size](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: 0

#### [Binlogrouter](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

**Settings**

[**archivedir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: string
* Mandatory: Yes
* Default: No
* Dynamic: No

[**compression\_algorithm**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `none`, `zstandard`
* Default: `none`

[**datadir**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/binlogs`

[**ddl\_only**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: boolean
* Mandatory: No
* Dynamic: No
* Default: false

[**encryption\_cipher**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `AES_CBC`, `AES_CTR`, `AES_GCM`
* Default: `AES_GCM`

[**encryption\_key\_id**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**expiration\_mode**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Dynamic: No
* Values: `purge`, `archive`
* Default: `purge`

[**expire\_log\_duration**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `0s`

[**expire\_log\_minimum\_files**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `2`

[**net\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `10s`

[**number\_of\_noncompressed\_files**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `2`

[**rpl\_semi\_sync\_slave\_enabled**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: false
* Dynamic: Yes

[**select\_master**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**server\_id**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `1234`

#### [Diff](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

**Settings**

[**explain**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `other`, \`both'
* Default: `both`

[**explain\_entries**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 2

[**explain\_period**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 15m

[**main**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: server
* Mandatory: Yes
* Dynamic: No

[**max\_request\_lag**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 10

[**on\_error**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `close`, `ignore`
* Default: `ignore`

[**percentile**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Min: 1
* Max: 100
* Default: 99

[**qps\_window**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: 15m

[**report**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `always`, `on_discrepancy`, `never`
* Default: `on_discrepancy`

[**reset\_replication**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**retain\_faster\_statements**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

[**retain\_slower\_statements**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

[**samples**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Min: 100
* Default: 1000

[**service**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: service
* Mandatory: Yes
* Dynamic: No

#### [KafkaCDC](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

**Settings**

[**bootstrap\_servers**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: string
* Mandatory: Yes
* Dynamic: No

[**cooperative\_replication**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**enable\_idempotence**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**exclude**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**gtid**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_sasl\_mechanism**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `PLAIN`, `SCRAM-SHA-256`, `SCRAM-SHA-512`
* Default: `PLAIN`

[**kafka\_sasl\_password**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_sasl\_user**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_ssl**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**kafka\_ssl\_ca**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_ssl\_cert**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_ssl\_key**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**match**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**read\_gtid\_from\_kafka**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**send\_schema**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**server\_id**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1234`

[**timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**topic**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: string
* Mandatory: Yes
* Dynamic: No

#### [KafkaImporter](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

**Settings**

[**batch\_size**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `100`

[**bootstrap\_servers**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**engine**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: string
* Default: `InnoDB`
* Mandatory: No
* Dynamic: Yes

[**kafka\_sasl\_mechanism**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `PLAIN`, `SCRAM-SHA-256`, `SCRAM-SHA-512`
* Default: `PLAIN`

[**kafka\_sasl\_password**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**kafka\_sasl\_user**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**kafka\_ssl**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**kafka\_ssl\_ca**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**kafka\_ssl\_cert**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**kafka\_ssl\_key**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**table\_name\_in**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `topic`, `key`
* Default: `topic`

[**timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `5000ms`

[**topics**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: stringlist
* Mandatory: Yes
* Dynamic: Yes

#### [Mirror](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)

**Settings**

[**exporter**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: Yes
* Dynamic: Yes
* Values: `log`, `file`, `kafka`

[**file**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)

* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes

[**kafka\_broker**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)

* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes

[**kafka\_topic**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)

* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes

[**main**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)

* Type: target
* Mandatory: Yes
* Dynamic: Yes

[**on\_error**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: `ignore`
* Mandatory: No
* Dynamic: Yes
* Values: `ignore`, `close`

[**report**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: `always`
* Mandatory: No
* Dynamic: Yes
* Values: `always`, `on_conflict`

#### [ReadConnRoute](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readconnroute.md)

**Settings**

[**master\_accept\_reads**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readconnroute.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**max\_replication\_lag**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readconnroute.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 0s

[**router\_options**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readconnroute.md)

* Type: [enum\_mask](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `master`, `slave`, `synced`, `running`
* Default: `running`

#### [ReadWriteSplit](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

**Settings**

[**causal\_reads**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `local`, `global`, `fast`, `fast_global`, `universal`, `fast_universal`
* Default: `none`

[**causal\_reads\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 10s

[**delayed\_retry**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**delayed\_retry\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 10s

[**lazy\_connect**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**master\_accept\_reads**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**master\_failure\_mode**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `fail_instantly`, `fail_on_write`, `error_on_write`
* Default: `fail_on_write` (MaxScale 23.08: `fail_instantly`)

[**master\_reconnection**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true (>= MaxScale 24.02), false(<= MaxScale 23.08)

[**max\_replication\_lag**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 0s

[**max\_slave\_connections**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 255

[**retry\_failed\_reads**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**slave\_connections**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 255

[**slave\_selection\_criteria**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `least_current_operations`, `adaptive_routing`, `least_behind_master`, `least_router_connections`, `least_global_connections`
* Default: `least_current_operations`

[**strict\_multi\_stmt**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**strict\_sp\_calls**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**strict\_tmp\_tables**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true (>= MaxScale 24.02), false (<= MaxScale 23.08)

[**transaction\_replay**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**transaction\_replay\_attempts**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

[**transaction\_replay\_checksum**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `full`, `result_only`, `no_insert_id`
* Default: `full`

[**transaction\_replay\_max\_size**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [size](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 1 MiB

[**transaction\_replay\_retry\_on\_deadlock**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**transaction\_replay\_retry\_on\_mismatch**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**transaction\_replay\_safe\_commit**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**transaction\_replay\_timeout**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 30s (>= MaxScale 24.02), 0s (<= MaxScale 23.08)

[**use\_sql\_variables\_in**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [enum](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `master`, `all`
* Default: `all`

#### [SchemaRouter](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)

**Settings**

[**allow\_duplicates**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**ignore\_tables**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)

* Type: stringlist
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ignore\_tables\_regex**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)

* Type: [regex](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `""`

[**max\_staleness**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 150s

[**refresh\_databases**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**refresh\_interval**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)

* Type: [duration](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `300s`

#### [SmartRouter](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-smartrouter.md)

**Settings**

[**master**](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-smartrouter.md)

* Type: target
* Mandatory: Yes
* Dynamic: No

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
