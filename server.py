#!/usr/bin/env python3

import socket  # [Sockets, Message Handling]

HOST = '127.0.0.1'  # [Protocol/Workflow: where to listen]
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # [Sockets]
    s.bind((HOST, PORT))    	# [Listener: binds to address/port]
    s.listen(1)             	# [Listener: ready for 1 connection]
    print("Server listening on", (HOST, PORT))
    conn, addr = s.accept() # [Listener: accept a client]
    with conn:
        print("Client connected:", addr)  # [Testing/Interaction]
        data = conn.recv(1024)            # [Message Handling: receive bytes]
        print("Received:", data.decode())  # [Message Handling: decode text]
        conn.sendall(data)                 # [Protocol: echo back]
        # [Shutdown: 'with' auto-closes sockets]
