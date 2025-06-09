
# LOCAL_INFILE Packet

### LOCAL_INFILE Packet


If the client sends a LOAD DATA LOCAL INFILE command via [com_query](../2-text-protocol/com_query.md), the server responds with LOCAL_INFILE_Packet to tell the client to send a specified file to the server.


#### Fields



* [int<1>](../protocol-data-types.md#fixed-length-integers) 0xFB : LOCAL_INFILE header
* [string<EOF>](../protocol-data-types.md#end-of-file-length-strings) filename






#### Client response


The client sends the file as the packet body. If the file is large, the contents are sent in multiple separate packets.
After the file is sent, the client must send an empty packet to indicate that no more data will follow.


Once the client has finished sending the file, the server will respond with an [OK_packet](ok_packet.md) or an [ERR_packet](err_packet.md).


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
