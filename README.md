## Subnet Calculator (WIP)
A lightweight Python script designed to calculate network parameters such as available host bits and usable host amounts based on an IP address and a subnet mask (CIDR notation).

Note: This project is currently a Work In Progress (WIP) and is not yet feature-complete.


### Current Features
**Accepts IP address input and splits it into standard integer octets.

* Accepts CIDR subnet input (supports input with or without a leading /, e.g., /24 or 24).

* Handles basic validation for empty subnet inputs.

* calculates total host bits (32 - subnet).

* calculates total usable hosts (2^host_bits - 2).


