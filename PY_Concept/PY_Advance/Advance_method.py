# Regular function
def square(x):
    return x ** 2

print(square(5))  # Output: 25

# Equivalent lambda function
square_lambda = lambda x: x ** 2

print(square_lambda(5))  # Output: 25

my_list = ["Hello", "World", "Python"]
joined_string = " ".join(my_list)
print(joined_string)  # Output: Hello World Python

name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: My name is Alice and I am 30 years old.

numbers = [1, 2, 3, 4, 5]

# Double each number
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5]

# Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum of all numbers
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # Output: 15
