#!/bin/python3

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1,verbose = False)[0] # srp - send recieve packets ,used[0] because srp usually returns ans and unans
    
    print("IP\t\t\tMAC Address\n------------------------------------------")
    
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc) #psrc ip of client hwsrc mac of destination
        

scan("10.0.3.15/24")