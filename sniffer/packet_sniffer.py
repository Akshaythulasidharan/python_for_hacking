#!/usr/bin/python3
#python3   -m pip install SomePackage 
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if(packet.haslayer(http.HTTPRequest)):
        if(packet.haslayer(scapy.Raw)):
            #print(packet.show())
            print(packet[scapy.Raw].load)

sniff("eth0")   # your interface