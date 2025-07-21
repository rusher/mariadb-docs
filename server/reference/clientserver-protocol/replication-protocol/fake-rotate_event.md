# Fake ROTATE\_EVENT

When a slave server connects to a MariaDB 10 master server, the first binlog event sent is Fake ROTATE\_EVENT.\
This event is similar to [ROTATE\_EVENT](rotate_event.md) but it's artificial and its purpose is to tell the slave server which is the binlog file name of the master.\
This matters of course when the slave connects with the GTID option (no filename is given) or when using file and pos with empty file name (usually file='' and pos = 4).

The Event Type is set ROTATE\_EVENT (0x4)

{% hint style="info" %}
**Note**: the fake ROTATE\_EVENT event is not written in the binlog file. It's created by the master and sent to new connected slave before [FORMAT\_DESCRIPTION\_EVENT](format_description_event.md)
{% endhint %}

#### Header

* Timestamp set to 0
* Event Tye is ROTATE\_EVENT
* Next Pos is set to 0
* Flags are set to LOG\_ARTIFICIAL\_F (0x20)

#### Content

The content is the same as [ROTATE\_EVENT](rotate_event.md).

* pos = the requested pos from slave, usually 4
* filename = the master binlog filename

If it is the first fake rotate event and global server variable @@binlog\_checksum was set to CRC32:

* crc32\_checksum (4 Bytes)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
