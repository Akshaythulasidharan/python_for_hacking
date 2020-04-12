#!/usr/bin/python3
import socket

connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("192.168.1.7",4444))

msg = "\n[+]connection established\n"
connection.send(msg.encode('ascii'))
recieved_data = connection.recv(1024)
print(recieved_data.decode('ascii'))


connection.close()