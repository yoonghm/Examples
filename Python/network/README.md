## UDP Broadcast Text Message

Test UDP broadcast command with **`UDP_broadcast_server.py`** and **`UDP_broadcast_client.py`**.

- You may need to enable filewall rules to allow python to send and receive UDP packets at all ports.
- Start one or more `UDP_broadcast_server.py` which listens at port `12345` in all addresses 
- Start one `UDP_broadcast_client.py`
- One the `UDB_broadcast_server.py` has received the message from `UDB_broadcast_client.py`, it will close.

## UDB Broadcast Tuple

Test UDP broadcast command with **`UDP_broadcast_tuple_server.py`** and **`UDP_broadcast_tuple_client.py`**.

- You may need to enable filewall rules to allow python to send and receive UDP packets at all ports.
- Start one or more `UDP_broadcast_tuple_server.py` which listens at port `12345` in all addresses 
- Start one `UDP_broadcast_tuple_client.py`

