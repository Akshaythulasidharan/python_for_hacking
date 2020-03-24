#!/usr/bin/python3
#08:00:27:1f:30:76
#08:00:27:1f:30:76
import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface use --help for info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new_mac use --help for info")
    else:
        return options



def change_mac(interface,new_mac):
    print("[+] Changing mac address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface,"hw", "ether",new_mac])
    subprocess.call(["ifconfig", interface,"up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    #print(ifconfig_result)
    mac_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig_result))
    if(mac_search_result):
        return mac_search_result.group(0)
    else:
        print("no mac address for this interface")

options =  get_arguments()
#change_mac(options.interface,options.new_mac)
current = get_current_mac(options.interface)
print("[+] The current mac address is:",current)
change_mac(options.interface,options.new_mac)
new = get_current_mac(options.interface)
if(new == current):
    print("[+] The mac address is successfully changed to:" + new)
else:
    print("[-] The mac address did not get changed")