# ## Task 2
# _Use the `ipaddress` module_

# Create variable for a subnet and a subnet mask:

# ```
# import ipaddress
# ip_subnet = ipaddress.ip_network('192.168.0.0/24')
# ```

# Find and print the subnet mask using functions that comes with the `ipaddress` module.

# Example:

# ```
# The subnet mask is: 255.255.255.0
# ```

import ipaddress

ip_subnet = ipaddress.ip_network('192.168.0.0/24')

print(f'The subnet mask is: {ip_subnet.netmask}.')