
# MaxScale 21.06 Encrypting Passwords

# Encrypting Passwords


**Note**: The password encryption format changed in MaxScale 2.5. All
 encrypted passwords created with MaxScale 2.4 or older need to be
 re-encrypted.


There are two options for representing the password, either plain text or
encrypted passwords may be used. In order to use encrypted passwords a set of
keys must be generated that will be used by the encryption and decryption
process. To generate the keys, use the `<code>maxkeys</code>` command.



```
maxkeys
```



By default the key file will be generated in `<code>/var/lib/maxscale</code>`. If a different
directory is required, it can be given as the first argument to the program. For
more information, see `<code>maxkeys --help</code>`.


Once the keys have been created the `<code>maxpasswd</code>` command can be used to generate
the encrypted password.



```
maxpasswd plainpassword
96F99AA1315BDC3604B006F427DD9484
```



The username and password, either encrypted or plain text, are stored in the
service section using the `<code>user</code>` and `<code>password</code>` parameters.


If a custom location was used for the key file, give it as the first argument to
`<code>maxpasswd</code>` and pass the password to be encrypted as the second argument. For
more information, see `<code>maxkeys --help</code>`.


Here is an example configuration that uses an encrypted password.



```
[My-Service]
type=service
router=readconnroute
router_options=master
servers=dbserv1, dbserv2, dbserv3
user=maxscale
password=96F99AA1315BDC3604B006F427DD9484
```



If the key file is not in the default location, the
[datadir](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md) parameter must be
set to the directory that contains it.
