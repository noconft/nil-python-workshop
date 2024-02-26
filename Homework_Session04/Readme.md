# Tasks

---

## Task 1.1
_Use dictionaries_

Given the set `names` below create a dictionary that contains the set objects (i.e. name) as keys, and frequency (i.e. frequency of name) as value.
To check print the dictionary.

```
names_1 = ["Michele", "Robin", "Sara"]
names_2 = ["Michele", "Robbyn", "Sarah"]
names_3 = ["Michelelele", "Robin", "Sarah"]
names = names_1 + names_2 + names_3
```

## Task 1.2
_(continuation from above)_

Now utilize the dictionary.
Let the user input a name (i.e. `Michele`) and return the frequency of the name.
Put the user input in a loop so the user can ask multiple times.

Example:

```
Enter a name to search for: Sara
Sara appears 1 times.
Enter a name to search for: Sarah
Sarah appears 2 times.
Enter a name to search for: ^C
KeyboardInterrupt
```

Hint: use control+C to stop the program if it gets stuck in a loop.

## Task 1.3
_(continuation from above)_

Same as above but now also give the user the option of escaping the loop.

Example:

```
Enter a name to search for (or 'q' to quit): Sara
Sara appears 1 times.
Enter a name to search for (or 'q' to quit): Sarah
Sarah appears 2 times.
Enter a name to search for (or 'q' to quit): q
Exiting...
```

## Task 2
_Use the `ipaddress` module_

Create variable for a subnet and a subnet mask:

```
import ipaddress
ip_subnet = ipaddress.ip_network('192.168.0.0/24')
```

Find and print the subnet mask using functions that comes with the `ipaddress` module.

Example:

```
The subnet mask is: 255.255.255.0
```

## Task 3.1
_Use the `ipaddress` module_

Create variable for a subnet and a subnet mask:

```
import ipaddress
ip_subnet = ipaddress.ip_network('192.168.0.0/24')
```

Use a loop to print the first 10 ip address and a hostname

Example:

```
IP address: 192.168.0.1, Hostname: host01
IP address: 192.168.0.2, Hostname: host02
[...]
IP address: 192.168.0.10, Hostname: host10
```

## Task 3.2
_Use the `ipaddress` module (advanced)_
_(continuation from above)_

Import the `csv` module:

```
import csv
```

Use a loop to write the first 10 ip address and a hostname into a csv file `hosts.csv`

Example:

```
cat hosts.csv
192.168.0.1,host01
192.168.0.2,host02
[...]
192.168.0.10,host10
```
