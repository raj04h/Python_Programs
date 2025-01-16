# Different data types in Python
integer_var = 10
float_var = 20.5
string_var = "Hello, World!"
list_var = [1, 2, 3, 4, 5]
tuple_var = (1, 2, 3)
dict_var = {"name": "Alice", "age": 25}


# Arithmetic operators
print(2 + 3)  # Addition
print(10 - 4)  # Subtraction
print(4 * 5)  # Multiplication
print(20 / 4)  # Division
print(10 % 3)  # Modulus

# Comparison operators
print(2 > 3)  # Greater than
print(10 == 10)  # Equal to

# Logical operators
print(True and False)  # AND
print(True or False)  # OR
print(not True)  # NOT

x = 10
print(type(x))  # <class 'int'>

# Typecasting
x = str(x)
print(type(x))  # <class 'str'>

my_string = "Hello, World!"
print(my_string[0:5])  # Output: Hello
print(my_string[7:12])  # Output: World

my_string = "Hello, World!"
print(my_string[0:12:2])  # Output: Hlo ol

my_string = "Hello, World!"

# len() function returns the length of the string
print(len(my_string))  # Output: 13

# lower() function converts all characters to lowercase
print(my_string.lower())  # Output: hello, world!

# upper() function converts all characters to uppercase
print(my_string.upper())  # Output: HELLO, WORLD!

# replace() function replaces a substring with another substring
print(my_string.replace("World", "Python"))  # Output: Hello, Python!

# find() function finds the first occurrence of a substring
print(my_string.find("World"))  # Output: 7


# Newline character
print("Hello\nWorld!")

# Tab character
print("Hello\tWorld!")

# Backslash character
print("This is a backslash: \\")

# Single quote
print('It\'s a beautiful day!')

# Double quote
print("He said, \"Hello, World!\"")


x = 10
y = 20

print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)   # Output: False
print(x < y)   # Output: True
print(x >= y)  # Output: False
print(x <= y)  # Output: True


x = 5
y = 10
z = 15

# and operator
print(x < y and y < z)  # Output: True

# or operator
print(x < y or y > z)  # Output: True

# not operator
print(not (x < y))  # Output: False