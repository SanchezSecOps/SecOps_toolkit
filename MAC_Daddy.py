import subprocess
import optparse
import random
import re

#MAC randomization functionality
def generateMAC():
    mac = [0x02, 0x00,0x00,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(f"{octet:02x}" for octet in mac)

#MAC address change verification
def get_current_mac(interface):
    try:
        output = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    except subprocess.CalledProcessError:
        print("Could not get mac address for interface {interface}.")
        return None

    mac_address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
    if mac_address_search:
            return mac_address_search.group(0)
    else:
        print("[-] Interface MAC address not found")
        return None


#adding options for faster use on CLI
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to use")
(options, arguments) = parser.parse_args()

#user defines network interface
interface = options.interface

#checking for missing arguments
if not interface:
    parser.error("[-] specify an interface to change:-i <eth0>")

# random MAC
new_mac = generateMAC()

#module call and list of commands running
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

#user notification of MAC change result
current_mac = get_current_mac(interface)
if current_mac == new_mac:
    print("[+] MAC Address of " + interface + " changed to " + new_mac)
else:
    print("[-] MAC Address failed current MAC is " + current_mac)