#!/bin/python3

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    print(answered.summary())
    
    
    #arp_request_broadcast.show()
    #print(broadcast.summary())
    #scapy.ls(scapy.Ether())
    #arp_request.pdst=ip
    #print(arp_request.summary())
    #scapy.ls(scapy.ARP()) //to list options avwailable  

scan("10.0.2.2/24")