# SecOps_toolkit
A kit of tools I have written myself to accomplish certain tasks I find annoying or tedious during I.T. operations and tasks.
These tools were written in Python and designed for Debain based Linux distros only. I may expand usage in the future but as this is my personal kit I'll be prioritizing my needs.

## Toolbelt Overview
1. MAC_RANDOMIZER
   A tool I wrote for randomizing your MAC address in Debian-based Linux distros. The main purpose I use this tool is for occasional security auditing on wireless networks with clients to explain what MAC addresses are, how they can't always be a reliable piece of data when identifying an attacker, and how easy it is to change them. This tool has also proven useful on penetration tests since it specifically randomizes MAC addresses with a "02" prefix, making it look like a local unicast address which allows us to evade vendor fingerprinting and bypass basic MAC filtering while still having our packets be valid over the network.  

2. 
