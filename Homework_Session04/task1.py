# ## Task 1.1
# _Use dictionaries_

# Given the set `names` below create a dictionary that contains the set objects (i.e. name) as keys, and frequency (i.e. frequency of name) as value.
# To check print the dictionary.

# ```
# names_1 = ["Michele", "Robin", "Sara"]
# names_2 = ["Michele", "Robbyn", "Sarah"]
# names_3 = ["Michelelele", "Robin", "Sarah"]
# names = names_1 + names_2 + names_3
# ```

names_1 = ["Michele", "Robin", "Sara"]
names_2 = ["Michele", "Robbyn", "Sarah"]
names_3 = ["Michelelele", "Robin", "Sarah"]
names = names_1 + names_2 + names_3

print(names)


names_dict = {}
for name in names:
    names_dict[name] = names.count(name)

print(names_dict)

while True:
    name_input = input('Enter a name to search for (or "q" to quit): ')
    if name_input == 'q':
        break
    elif name_input in names_dict:
        print(f'{name_input} appears {names.count(name_input)} times.')
