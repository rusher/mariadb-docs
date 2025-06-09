
# Performance Schema socket_instances Table

The `socket_instances` table lists active server connections, with each record being a Unix socket file or TCP/IP connection.


The `socket_instances` table contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| EVENT_NAME | NAME from the setup_instruments table, and the name of the wait/io/socket/* instrument that produced the event. |
| OBJECT_INSTANCE_BEGIN | Memory address of the object. |
| THREAD_ID | Thread identifier that the server assigns to each socket. |
| SOCKET_ID | The socket's internal file handle. |
| IP | Client IP address. Blank for Unix socket file, otherwise an IPv4 or IPv6 address. Together with the PORT identifies the connection. |
| PORT | TCP/IP port number, from 0 to 65535. Together with the IP identifies the connection. |
| STATE | Socket status, either IDLE if waiting to receive a request from a client, or ACTIVE |




CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
