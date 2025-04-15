
# Table Discovery (before 10.0.2)

This page describes the **old** discovery API, created in MySQL for NDB Cluster. It no longer works in MariaDB. New table discovery API is documented [here](table-discovery.md).


There are four parts of it.


First, when a server finds that a table (for example, mentioned in the `<code>SELECT</code>` query) does not exist, it asks every engine whether it knows anything about this table. For this it uses **discover()** method of the handlerton. The method is defined as


```
int discover(handlerton *hton, THD* thd, const char *db, const char *name,
             unsigned char **frmblob, size_t *frmlen);
```

It takes the database and a table name as arguments and is returns 0 if the table exists in the engine and 1 otherwise. If it returned 0, it is supposed to allocate (with `<code>my_malloc()</code>`) a buffer and store the complete binary image of the `<code>.frm</code>` file of that table. The server will write it down to disk, creating table's `<code>.frm</code>`. The output parameters `<code>frmblob</code>` and `<code>frmlen</code>` are used to return the information about the buffer to the caller. The caller is responsible for freeing the buffer with `<code>my_free()</code>`.


Second, in some cases the server only wants to know if the table exists, but it does not really need to open it and will not use its `<code>.frm</code>` file image. Then using the `<code>discover()</code>` method would be an overkill, and the server uses a lightweight **table_exists_in_engine()** method. This method is defined as


```
int table_exists_in_engine(handlerton *hton, THD* thd,
                           const char *db, const char *name);
```

and it returns one of the `<code>HA_ERR_</code>` codes, typically `<code>HA_ERR_NO_SUCH_TABLE</code>` or `<code>
HA_ERR_TABLE_EXIST</code>`.


Third, there can be a situation when the server thinks that the table exists (it found and successfully read the `<code>.frm</code>` file), but from the engine point of view the `<code>.frm</code>` file is incorrect. For example, the table was already deleted from the engine, or its definition was modified (again, modified only in the engine). In this case the `<code>.frm</code>` file is outdated, and the server needs to re-discover the table. The engine conveys this to the server by returning `<code>HA_ERR_TABLE_DEF_CHANGED</code>` error code from the handler's **open()** method. On receiving this error the server will use the `<code>discover()</code>` method to get the new `<code>.frm</code>` image. This also means that *after* the table is opened, the server does not expect its metadata to change. The engine thus should ensure (with some kind of locking, perhaps) that a table metadata cannot be modified, as long as the table stays opened.


And fourth, a user might want to retrieve a list of tables in a specific database. With `<code>SHOW TABLES</code>` or by quering `<code>INFORMATION_SCHEMA</code>` tables. The user expects to see all tables, but the server cannot discover them one by one, because it doesnt know table names. In this case, the server uses a special discovery technique. It is **find_files()** method in the handlerton, defines as


```
int find_files(handlerton *hton, THD *thd,
               const char *db, const char *path,
               const char *wild, bool dir, List<LEX_STRING> *files);
```

and it, typically for Storage Engine API, returns 0 on success and 1 on failure. The arguments mean `<code>db</code>` - the name of the database, `<code>path</code>` - the path to it, `<code>wild</code>` an SQL wildcard pattern (for example, from `<code>SHOW TABLES LIKE '...'</code>`, and `<code>dir</code>`, if set, means to discover *databases* instead of *tables*.

