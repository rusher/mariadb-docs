
# Using Encryption and Compression Tools With Mariabackup

[Mariabackup](mariabackup-and-backup-stage-commands.md) supports streaming to stdout with the `--stream=xbstream` option. This option allows easy integration with popular encryption and compression tools. Below are several examples.


## Encrypting and Decrypting Backup With openssl


The following example creates an AES-encrypted backup, protected with the password "mypass" and stores it in a file "backup.xb.enc":


```
mariabackup --user=root --backup --stream=xbstream  | openssl  enc -aes-256-cbc -k mypass > backup.xb.enc
```

To decrypt and unpack this backup into the current directory, the following command can be used:


```
openssl  enc -d -aes-256-cbc -k mypass -in backup.xb.enc | mbstream -x
```

## Compressing and Decompressing Backup With gzip


This example compresses the backup without encrypting:


```
mariabackup --user=root --backup --stream=xbstream | gzip > backupstream.gz
```

We can decompress and unpack the backup as follows:


```
gunzip -c backupstream.gz | mbstream -x
```

## Compressing and Encrypting Backup, Using gzip and openssl


This example adds a compression step before the encryption, otherwise looks almost identical to the previous example:


```
mariabackup --user=root --backup --stream=xbstream | gzip | openssl  enc -aes-256-cbc -k mypass > backup.xb.gz.enc
```

We can decrypt, decompress and unpack the backup as follow (note `gzip -d` in the pipeline):


```
openssl  enc -d -aes-256-cbc -k mypass -in backup.xb.gz.enc |gzip -d| mbstream -x
```

## Compressing and Encrypting with 7Zip


7zip archiver is a popular utility (especially on Windows) that supports reading from standard output, with the -`-si` option, and writing to stdout with the `-so` option, and can thus be used together with Mariabackup.


Compressing backup with the 7z command line utility works as follows:


```
mariabackup --user=root --backup --stream=xbstream | 7z a -si backup.xb.7z
```

Uncompress and unpack the archive with


```
7z e backup.xb.7z -so |mbstream -x
```

7z also has builtin AES-256 encryption. To encrypt the backup from the previous example using password SECRET, add `-pSECRET` to the 7z command line.


## Compressing with zstd


Compress


```
mariabackup --user=root --backup --stream=xbstream  | zstd - -o backup.xb.zst -f -1
```

Decompress , unpack


```
zstd -d backup.xbstream.zst -c | mbstream -x
```

## Encrypting With GPG


Encryption


```
mariabackup --user=root --backup --stream=xbstream | gpg -c --passphrase SECRET --batch --yes -o backup.xb.gpg
```

Decrypt, unpack


```
gpg --decrypt --passphrase SECRET --batch --yes  backup.xb.gpg | mbstream -x
```

## Interactive Input for Passphrases


Most of the described tools also provide a way to enter a passphrase interactively (although 7zip does not seem to work well when reading input from stdin). Please consult documentation of the tools for more info.


## Writing extra status files


By default files like `[xtrabackup_checkpoints](files-created-by-mariabackup.md#xtrabackup_checkpoints)` are also written to the output stream only, and so would not be available for taking further incremental backups without prior extraction from the compressed or encrypted stream output file.


To avoid this these files can additionally be written to a directory that can then be used as input for further incremental backups using the `[--extra-lsndir=...](mariabackup-options.md#-extra-lsndir)` option.


See also e.g: [Combining incremental backups with streaming output](incremental-backup-and-restore-with-mariabackup.md#combining-with-stream-output)

