
# Fake GTID_LIST event

This event is sent by master server to the registering slave and it's sent only once, after 
[Format Description Event](format_description_event.md)


**Note**: the fake GTID_LIST event is not written in the binlog file.
It's created by the master and sent to new connected slave before any "real" binlog event.


#### Header


* Event type is set to 163 (0xa3)
* Time stamp set to 0
* NextPos tells which is the binlog position of next event
* Flags are set to ARTIFICIAL (0x20)


#### Content


The content is the same as the "real" [GTID_LIST](gtid_list_event.md).


* # of GTIDs
* domain_id
* server_id
* sequence
* ...

