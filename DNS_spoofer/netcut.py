#!/usr/bin/python3

# iptables -I FORWARD -j NFQUEUE --queue-num 0
import netfilterqueue
import subprocess

def create_queue():
    subprocess.call(["sudo","iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"])

def process_packet(packet):
    print(packet)
    #packet.accept()

create_queue()
queue = netfilterqueue.NetfilterQueue()
queue.bind(0,process_packet)
queue.run()


