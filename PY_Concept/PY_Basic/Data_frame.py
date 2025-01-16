
# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1

# Modifying elements
my_list[2] = 10
print(my_list)  # Output: [1, 2, 10, 4, 5]

# Adding elements
my_list.append(6)
print(my_list)  # Output: [1, 2, 10, 4, 5, 6]

# Removing elements
my_list.remove(10)
print(my_list)  # Output: [1, 2, 4, 5, 6]

# Positive indexing
print(my_list[1])  # Output: 2

# Negative indexing
print(my_list[-1])  # Output: 6

# Creating a list
my_list = [1, 2, 3, 4, 5]

# append() method adds an element at the end of the list
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# insert() method inserts an element at a specified position
my_list.insert(2, 10)
print(my_list)  # Output: [1, 2, 10, 3, 4, 5, 6]

# pop() method removes an element from a specified position
my_list.pop(2)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# sort() method sorts the list
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]


# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print(my_tuple[0])  # Output: 1

# Tuples are immutable, so you cannot modify elements
# my_tuple[2] = 10  # This will raise a TypeError

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# count() method returns the number of times a specified value occurs in a tuple
print(my_tuple.count(3))  # Output: 1

# index() method returns the position of a specified value
print(my_tuple.index(4))  # Output: 3


# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values
print(my_dict["name"])  # Output: Alice

# Modifying values
my_dict["age"] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# Adding new key-value pairs
my_dict["email"] = "alice@example.com"
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

# Removing key-value pairs
my_dict.pop("city")
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# keys() method returns a list of all the keys
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])

# values() method returns a list of all the values
print(my_dict.values())  # Output: dict_values(['Alice', 25, 'New York'])

# items() method returns a list of all key-value pairs
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# get() method returns the value for the specified key
print(my_dict.get("name"))  # Output: Alice

# update() method updates the dictionary with the specified key-value pairs
my_dict.update({"age": 26, "email": "alice@example.com"})
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union: combines elements from both sets
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6}

# Intersection: gets elements common to both sets
print(set1.intersection(set2))  # Output: {3, 4}

# Difference: gets elements in set1 but not in set2
print(set1.difference(set2))  # Output: {1, 2}

# Symmetric difference: gets elements in either set1 or set2 but not both
print(set1.symmetric_difference(set2))  # Output: {1, 2, 5, 6}
