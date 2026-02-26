# this asks the user to type an ip address and stores it in the variable "ip"
ip = input("Enter IP address: ")
# this asks the user to type a subnet mask and stores it in the variable "subnet"
subnet = input("Enter subnet mask: ")

# splits the ip address on every "." and returns a list
split_ip = ip.split(".")
print(split_ip)  # prints the ip after it's been split by "."

octets = []  # "[]" converts "octets" to numbers
for part in split_ip:  # loops through each element inside split_ip, assigning each value to the variable "part"
    # converts variable "part" into integer and adds it to the octets list
    octets.append(int(part))
    # prints the octets, which is the split ip converted into whole numbers
    print(octets)

if subnet == "":
    print("you need to insert a subnet mask")
    exit()

if subnet[0] == "/":  # if the user types "/" in the subnet
    subnet = subnet[1:]  # it gets ignored and uses only what comes after it
subnet = int(subnet)  # converts subnet string into whole numbers

host_bits = 32 - subnet  # host bits gets calculated
print(host_bits)  # temporary debug

host_amount = 2 ** host_bits - 2  # calculates amount of usable hosts in the subnet
print(host_amount)  # temporary debug

network_octets = octets.copy()  # copies the octets list
host_octets = host_bits // 8
print(host_octets)  # temporary debug
