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

import csv
import ipaddress

ip_subnet = ipaddress.ip_network('192.168.0.0/24')

# Open a CSV file in write mode
with open('hosts.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)
    
    # Write header row
    csv_writer.writerow(['IP address', 'Hostname'])
    
    # Write the first 10 hosts with customized hostnames
    for i, host in enumerate(ip_subnet.hosts()):
        hostname = f"host{i+1:02}"  # Customize the hostname format
        csv_writer.writerow([str(host), hostname])
        # Stop after writing 10 hosts
        if i == 9:
            break
