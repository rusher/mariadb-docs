# Full-Text Index Stopwords

Stopwords are used to provide a list of commonly-used words that can be ignored for the purposes of [Full-text-indexes](./).

Full-text indexes built in [MyISAM](../../../../reference/storage-engines/myisam-storage-engine/) and [InnoDB](../../../../reference/storage-engines/innodb/) have different stopword lists by default.

## MyISAM Stopwords

For full-text indexes on MyISAM tables, by default, the list is built from the file `storage/myisam/ft_static.c`, and searched using the server's character set and collation. The [ft\_stopword\_file](../../system-variables/server-system-variables.md#ft_stopword_file) system variable allows the default list to be overridden with words from another file, or for stopwords to be ignored altogether.

If the stopword list is changed, any existing full-text indexes need to be rebuilt

The following table shows the default list of stopwords, although you should always treat `storage/myisam/ft_static.c` as the definitive list. See the [Fulltext Index Overview](full-text-index-overview.md) for more details, and [Full-text-indexes](./) for related articles.

|               |               |              |              |
| ------------- | ------------- | ------------ | ------------ |
| a's           | able          | about        | above        |
| according     | accordingly   | across       | actually     |
| after         | afterwards    | again        | against      |
| ain't         | all           | allow        | allows       |
| almost        | alone         | along        | already      |
| also          | although      | always       | am           |
| among         | amongst       | an           | and          |
| another       | any           | anybody      | anyhow       |
| anyone        | anything      | anyway       | anyways      |
| anywhere      | apart         | appear       | appreciate   |
| appropriate   | are           | aren't       | around       |
| as            | aside         | ask          | asking       |
| associated    | at            | available    | away         |
| awfully       | be            | became       | because      |
| become        | becomes       | becoming     | been         |
| before        | beforehand    | behind       | being        |
| believe       | below         | beside       | besides      |
| best          | better        | between      | beyond       |
| both          | brief         | but          | by           |
| c'mon         | c's           | came         | can          |
| can't         | cannot        | cant         | cause        |
| causes        | certain       | certainly    | changes      |
| clearly       | co            | com          | come         |
| comes         | concerning    | consequently | consider     |
| considering   | contain       | containing   | contains     |
| corresponding | could         | couldn't     | course       |
| currently     | definitely    | described    | despite      |
| did           | didn't        | different    | do           |
| does          | doesn't       | doing        | don't        |
| done          | down          | downwards    | during       |
| each          | edu           | eg           | eight        |
| either        | else          | elsewhere    | enough       |
| entirely      | especially    | et           | etc          |
| even          | ever          | every        | everybody    |
| everyone      | everything    | everywhere   | ex           |
| exactly       | example       | except       | far          |
| few           | fifth         | first        | five         |
| followed      | following     | follows      | for          |
| former        | formerly      | forth        | four         |
| from          | further       | furthermore  | get          |
| gets          | getting       | given        | gives        |
| go            | goes          | going        | gone         |
| got           | gotten        | greetings    | had          |
| hadn't        | happens       | hardly       | has          |
| hasn't        | have          | haven't      | having       |
| he            | he's          | hello        | help         |
| hence         | her           | here         | here's       |
| hereafter     | hereby        | herein       | hereupon     |
| hers          | herself       | hi           | him          |
| himself       | his           | hither       | hopefully    |
| how           | howbeit       | however      | i'd          |
| i'll          | i'm           | i've         | ie           |
| if            | ignored       | immediate    | in           |
| inasmuch      | inc           | indeed       | indicate     |
| indicated     | indicates     | inner        | insofar      |
| instead       | into          | inward       | is           |
| isn't         | it            | it'd         | it'll        |
| it's          | its           | itself       | just         |
| keep          | keeps         | kept         | know         |
| knows         | known         | last         | lately       |
| later         | latter        | latterly     | least        |
| less          | lest          | let          | let's        |
| like          | liked         | likely       | little       |
| look          | looking       | looks        | ltd          |
| mainly        | many          | may          | maybe        |
| me            | mean          | meanwhile    | merely       |
| might         | more          | moreover     | most         |
| mostly        | much          | must         | my           |
| myself        | name          | namely       | nd           |
| near          | nearly        | necessary    | need         |
| needs         | neither       | never        | nevertheless |
| new           | next          | nine         | no           |
| nobody        | non           | none         | noone        |
| nor           | normally      | not          | nothing      |
| novel         | now           | nowhere      | obviously    |
| of            | off           | often        | oh           |
| ok            | okay          | old          | on           |
| once          | one           | ones         | only         |
| onto          | or            | other        | others       |
| otherwise     | ought         | our          | ours         |
| ourselves     | out           | outside      | over         |
| overall       | own           | particular   | particularly |
| per           | perhaps       | placed       | please       |
| plus          | possible      | presumably   | probably     |
| provides      | que           | quite        | qv           |
| rather        | rd            | re           | really       |
| reasonably    | regarding     | regardless   | regards      |
| relatively    | respectively  | right        | said         |
| same          | saw           | say          | saying       |
| says          | second        | secondly     | see          |
| seeing        | seem          | seemed       | seeming      |
| seems         | seen          | self         | selves       |
| sensible      | sent          | serious      | seriously    |
| seven         | several       | shall        | she          |
| should        | shouldn't     | since        | six          |
| so            | some          | somebody     | somehow      |
| someone       | something     | sometime     | sometimes    |
| somewhat      | somewhere     | soon         | sorry        |
| specified     | specify       | specifying   | still        |
| sub           | such          | sup          | sure         |
| t's           | take          | taken        | tell         |
| tends         | th            | than         | thank        |
| thanks        | thanx         | that         | that's       |
| thats         | the           | their        | theirs       |
| them          | themselves    | then         | thence       |
| there         | there's       | thereafter   | thereby      |
| therefore     | therein       | theres       | thereupon    |
| these         | they          | they'd       | they'll      |
| they're       | they've       | think        | third        |
| this          | thorough      | thoroughly   | those        |
| though        | three         | through      | throughout   |
| thru          | thus          | to           | together     |
| too           | took          | toward       | towards      |
| tried         | tries         | truly        | try          |
| trying        | twice         | two          | un           |
| under         | unfortunately | unless       | unlikely     |
| until         | unto          | up           | upon         |
| us            | use           | used         | useful       |
| uses          | using         | usually      | value        |
| various       | very          | via          | viz          |
| vs            | want          | wants        | was          |
| wasn't        | way           | we           | we'd         |
| we'll         | we're         | we've        | welcome      |
| well          | went          | were         | weren't      |
| what          | what's        | whatever     | when         |
| whence        | whenever      | where        | where's      |
| whereafter    | whereas       | whereby      | wherein      |
| whereupon     | wherever      | whether      | which        |
| while         | whither       | who          | who's        |
| whoever       | whole         | whom         | whose        |
| why           | will          | willing      | wish         |
| with          | within        | without      | won't        |
| wonder        | would         | wouldn't     | yes          |
| yet           | you           | you'd        | you'll       |
| you're        | you've        | your         | yours        |
| yourself      | yourselves    | zero         |              |

## InnoDB Stopwords

Stopwords on full-text indexes are only enabled if the [innodb\_ft\_enable\_stopword](../../../../reference/storage-engines/innodb/innodb-system-variables.md) system variable is set (by default it is) at the time the index was created.

The stopword list is determined as follows:

* If the [innodb\_ft\_user\_stopword\_table](../../../../reference/storage-engines/innodb/innodb-system-variables.md) system variable is set, that table is used as a stopword list.
* If `innodb_ft_user_stopword_table` is not set, the table set by [innodb\_ft\_server\_stopword\_table](../../../../reference/storage-engines/innodb/innodb-system-variables.md) is used.
* If neither variable is set, the built-in list is used, which can be viewed by querying the [INNODB\_FT\_DEFAULT\_STOPWORD table](../../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_ft_default_stopword-table.md) in the [Information Schema](../../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/).

In the first two cases, the specified table must exist at the time the system variable is set and the full-text index created. It must be an InnoDB table with a single column, a [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md) named VALUE.

The default InnoDB stopword list differs from the default MyISAM list, being much shorter, and contains the following words:

|      |       |      |      |
| ---- | ----- | ---- | ---- |
| a    | about | an   | are  |
| as   | at    | be   | by   |
| com  | de    | en   | for  |
| from | how   | i    | in   |
| is   | it    | la   | of   |
| on   | or    | that | the  |
| this | to    | was  | what |
| when | where | who  | will |
| with | und   | the  | www  |

CC BY-SA / Gnu FDL
