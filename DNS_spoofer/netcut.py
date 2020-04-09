#!/usr/bin/python3

# iptables -I FORWARD -j NFQUEUE --queue-num 0
import netfilterqueue
import subprocess

def create_queue():
    subprocess.call(["sudo","iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"])
    print("[+] Creating queue")


def delete_queue():
    subprocess.call(["sudo","iptables","--flush"])
    print("[-] Deleting queue")


def process_packet(packet):
    print(packet)
    #packet.accept()

create_queue()
try:
    while(True):
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0,process_packet)
        queue.run()
except(KeyboardInterrupt):
    print("\n")
    delete_queue()


