
# Server Locale

The [lc_time_names](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lc_time_names) server system variable sets the language used by the date and time functions [DAYNAME()](../../../../sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/dayname.md), [MONTHNAME()](../../../../sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/monthname.md) and [DATE_FORMAT()](../../../../sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/date_format.md) and [lc_messages](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lc_messages) sets the language for error messages.


The list of the locales supported by the current MariaDB installation can be obtained via the [LOCALES](locales-plugin.md) plugin.


MariaDB supports the following locale values:



| Locale | Language | Territory |
| --- | --- | --- |
| Locale | Language | Territory |
| ar_AE | Arabic | United Arab Emirates |
| ar_BH | Arabic | Bahrain |
| ar_DZ | Arabic | Algeria |
| ar_EG | Arabic | Egypt |
| ar_IN | Arabic | Iran |
| ar_IQ | Arabic | Iraq |
| ar_JO | Arabic | Jordan |
| ar_KW | Arabic | Kuwait |
| ar_LB | Arabic | Lebanon |
| ar_LY | Arabic | Libya |
| ar_MA | Arabic | Morocco |
| ar_OM | Arabic | Oman |
| ar_QA | Arabic | Qatar |
| ar_SA | Arabic | Saudi Arabia |
| ar_SD | Arabic | Sudan |
| ar_SY | Arabic | Syria |
| ar_TN | Arabic | Tunisia |
| ar_YE | Arabic | Yemen |
| be_BY | Belarusian | Belarus |
| bg_BG | Bulgarian | Bulgaria |
| ca_ES | Catalan | Catalan |
| cs_CZ | Czech | Czech Republic |
| da_DK | Danish | Denmark |
| de_AT | German | Austria |
| de_BE | German | Belgium |
| de_CH | German | Switzerland |
| de_DE | German | Germany |
| de_LU | German | Luxembourg |
| el_GR | Greek | Greece |
| en_AU | English | Australia |
| en_CA | English | Canada |
| en_GB | English | United Kingdom |
| en_IN | English | India |
| en_NZ | English | New Zealand |
| en_PH | English | Philippines |
| en_US | English | United States |
| en_ZA | English | South Africa |
| en_ZW | English | Zimbabwe |
| es_AR | Spanish | Argentina |
| es_BO | Spanish | Bolivia |
| es_CL | Spanish | Chile |
| es_CO | Spanish | Columbia |
| es_CR | Spanish | Costa Rica |
| es_DO | Spanish | Dominican Republic |
| es_EC | Spanish | Ecuador |
| es_ES | Spanish | Spain |
| es_GT | Spanish | Guatemala |
| es_HN | Spanish | Honduras |
| es_MX | Spanish | Mexico |
| es_NI | Spanish | Nicaragua |
| es_PA | Spanish | Panama |
| es_PE | Spanish | Peru |
| es_PR | Spanish | Puerto Rico |
| es_PY | Spanish | Paraguay |
| es_SV | Spanish | El Salvador |
| es_US | Spanish | United States |
| es_UY | Spanish | Uruguay |
| es_VE | Spanish | Venezuela |
| et_EE | Estonian | Estonia |
| eu_ES | Basque | Basque |
| fi_FI | Finnish | Finland |
| fo_FO | Faroese | Faroe Islands |
| fr_BE | French | Belgium |
| fr_CA | French | Canada |
| fr_CH | French | Switzerland |
| fr_FR | French | France |
| fr_LU | French | Luxembourg |
| gl_ES | Galician | Galician |
| gu_IN | Gujarati | India |
| he_IL | Hebrew | Israel |
| hi_IN | Hindi | India |
| hr_HR | Croatian | Croatia |
| hu_HU | Hungarian | Hungary |
| id_ID | Indonesian | Indonesia |
| is_IS | Icelandic | Iceland |
| it_CH | Italian | Switzerland |
| it_IT | Italian | Italy |
| ja_JP | Japanese | Japan |
| ka_GE | Georgian | Georgia (From [MariaDB 10.11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-11-series/mariadb-10-11-3-release-notes)) |
| ko_KR | Korean | Republic of Korea |
| lt_LT | Lithuanian | Lithuania |
| lv_LV | Latvian | Latvia |
| mk_MK | Macedonian | FYROM |
| mn_MN | Mongolia | Mongolian |
| ms_MY | Malay | Malaysia |
| nb_NO | Norwegian(Bokmål) | Norway |
| nl_BE | Dutch | Belgium |
| nl_NL | Dutch | The Netherlands |
| no_NO | Norwegian | Norway |
| pl_PL | Polish | Poland |
| pt_BR | Portugese | Brazil |
| pt_PT | Portugese | Portugal |
| rm_CH | Romansh | Switzerland |
| ro_RO | Romanian | Romania |
| ru_RU | Russian | Russia |
| ru_UA | Russian | Ukraine |
| sk_SK | Slovak | Slovakia |
| sl_SI | Slovenian | Slovenia |
| sq_AL | Albanian | Albania |
| sr_YU | Serbian | Serbia (Deprecated in [MariaDB 10.0.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10011-release-notes) and removed in [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)) |
| sv_FI | Swedish | Finland |
| sv_SE | Swedish | Sweden |
| sw_KE | Swahili | Kenya (from [MariaDB 11.1.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-2-release-notes)) |
| ta_IN | Tamil | India |
| te_IN | Telugu | India |
| th_TH | Thai | Thailand |
| tr_TR | Turkish | Turkey |
| uk_UA | Ukrainian | Ukraine |
| ur_PK | Urdu | Pakistan |
| vi_VN | Vietnamese | Viet Nam |
| zh_CN | Chinese | China |
| zh_HK | Chinese | Hong Kong |
| zh_TW | Chinese | Taiwan Province of China |



## Examples


Setting the [lc_time_names](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lc_time_names) and [lc_messages](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lc_messages) variables to localize the units of date and time, and the server error messages.


```
SELECT DAYNAME('2013-04-01'), MONTHNAME('2013-04-01');
+-----------------------+-------------------------+
| DAYNAME('2013-04-01') | MONTHNAME('2013-04-01') |
+-----------------------+-------------------------+
| Monday                | April                   |
+-----------------------+-------------------------+

SET lc_time_names = 'fr_CA';

SELECT DAYNAME('2013-04-01'), MONTHNAME('2013-04-01');
+-----------------------+-------------------------+
| DAYNAME('2013-04-01') | MONTHNAME('2013-04-01') |
+-----------------------+-------------------------+
| lundi                 | avril                   |
+-----------------------+-------------------------+

SELECT blah;
ERROR 1054 (42S22): Unknown column 'blah' in 'field' list'

SET lc_messages = 'nl_NL';

SELECT blah;
ERROR 1054 (42S22): Onbekende kolom 'blah' in field list
```
