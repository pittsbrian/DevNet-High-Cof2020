"""DevNet High - Class of 2020 - Challenge 1"""

import random
import ipaddress

# TODO: Write a print statement that displays both the type and value of 'ip'
ip = ("10.1.1.200")

#bpitts code
print (ip)
print(type(ip))


# TODO: Write a conditional to print out if `iosversion` is less than or greater than 14
i = random.randint(12, 17)
print('i is {}'.format(i))

#bpitts code
if i != 14:
    print ('iosversion is less than or greater than 14')

# TODO: Write a conditional that prints the serial number of the device
devices = ({'CAT9300':'XVNM1245ERGC'}, {'ISR4331':'VNMM8742THBX'}, {'NGFW2120':'EAQP4900RTJO'})
device = random.sample(devices, 1) [0]
device = list(device.values())[0]

#bpitts code
print (device)


# Function for converting CIDR notation into 32-bit netmask (nothing to do here)
def cidr_to_netmask(ip_str):
    ip = ipaddress.IPv4Network(ip_str)
    return ip.with_netmask

'''
TODO: Call the function above few times to so that the input of IP network with CIDR displays the IP network with 32-bit netmask
Example:
Input would be '10.1.1.0/24' and when printed out the output would be '10.1.1.0/255.255.255.0'
'''

ip_address1 = cidr_to_netmask("10.0.0.0/24")
ip_address2 = cidr_to_netmask("10.100.100.100/30")
ip_address3 = cidr_to_netmask("192.168.0.0/18")

print(ip_address1)

print(ip_address2)

print(ip_address3)
