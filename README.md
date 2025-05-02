# SecOpsToolkit
**in progress**

A kit of tools I have written myself to accomplish certain tasks I find tedious during Security & I.T. operations.
These tools were written in Python and designed for Debain based Linux distros only. I may expand usage in the future.

## Toolbelt Overview
1. [MAC_Daddy](MAC_Daddy.py)
   A tool I wrote for randomizing your network interface's MAC address in Debian-based Linux distros. The main purpose I use this tool is for occasional security auditing on wireless networks with clients to explain what MAC addresses are, how they can't always be a reliable piece of data when identifying an attacker, and how easy it is to change them. This tool has also proven useful on penetration tests since it specifically randomizes MAC addresses with a "02" prefix, making it look like a local unicast address which allows us to evade vendor fingerprinting and bypass basic MAC filtering while still having our packets be valid over the network.  

   ### HOW TO USE
   -Download MAC_Daddy.py
   
   -Place in an accessible directory
   
   -Run Terminal and navigate to the designated directory where script is placed

   -type: *sudo python MAC_Daddy.py -i <network interface>*

   -You should receive confirmation on what your new MAC address is

   -type: *ip a* to see new MAC/ether
