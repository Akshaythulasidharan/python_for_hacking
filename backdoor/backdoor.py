#!/usr/bin/python3
import socket

connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("192.168.1.7",4444))