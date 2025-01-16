dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = dict1 | dict2
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}

dict1 |= dict2
print(dict1)   # Output: {'a': 1, 'b': 3, 'c': 4}

squares = [x ** 2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]