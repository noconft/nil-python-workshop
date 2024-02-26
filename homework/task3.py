# ## Task 3.1
# _Use the `ipaddress` module_

# Create variable for a subnet and a subnet mask:

# ```
# import ipaddress
# ip_subnet = ipaddress.ip_network('192.168.0.0/24')
# ```

# Use a loop to print the first 10 ip address and a hostname

# Example:

# ```
# IP address: 192.168.0.1, Hostname: host01
# IP address: 192.168.0.2, Hostname: host02
# [...]
# IP address: 192.168.0.10, Hostname: host10
# ```

import ipaddress

ip_subnet = ipaddress.ip_network('192.168.0.0/24')

# Print the first 10 hosts with customized hostnames
for i, host in enumerate(ip_subnet.hosts()):
    hostname = f"host{i+1:02}"  # Customize the hostname format
    print(f"IP address: {host}, Hostname: {hostname}")
    # Stop after printing 10 hosts
    if i == 9:
        break