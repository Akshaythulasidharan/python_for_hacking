#!/bin/python3

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1,verbose = False)[0] # srp - send recieve packets ,used[0] because srp usually returns ans and unans
    
    
    clients_list = []
    for element in answered_list:
        client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc }
        clients_list.append(client_dict) 
        #print(element[1].psrc + "\t\t" + element[1].hwsrc) #psrc ip of client hwsrc mac of destination
    return clients_list

def print_results(results_list):
    print("IP\t\t\tMAC Address\n------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

print_results(scan("10.0.3.15/24"))