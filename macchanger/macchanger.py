#!/usr/bin/python3
#08:00:27:1f:30:76
#08:00:27:1f:30:76
import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")
#parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC address")

(options,arguments) = parser.parse_args()

#interface = input("enter the interface:")
#new_mac = input("enter the mac address:")

interface = options.interface
new_mac = options.new_mac

print("[+] Changing mac address for " + interface + " to " + new_mac)

#subprocess.call("ifconfig " + interface + " down", shell=True)
#subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
#subprocess.call("ifconfig " + interface + " up", shell=True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface,"hw", "ether",new_mac])
subprocess.call(["ifconfig", interface,"up"])