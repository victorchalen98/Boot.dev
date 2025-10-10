names = ["jack bronson", "jill mcarty", "john denver"]

names_dict = {}
for name in names:
    # .split() returns a list of strings
    # where each string is a single word from the original
    name_list = name.split()

    # here we update the dictionary
    names_dict[name_list[0]] = name_list[1]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty', 'john': 'denver'}

'''
Which is the correct syntax to create a new key/value pair in an existing dictionary?
dict[key] = value
'''