# Generator function to generate squares of numbers
def square_generator(n):
    for i in range(1, n+1):
        yield i ** 2  #int' object is not iterable, so we not use here return method

# Using the generator to print squares of numbers from 1 to 5
for num in square_generator(5):
    print(num)

# Output:
# 1
# 4
# 9
# 16
# 25

def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(3, 5)
print(sum_result)  # Output: 8
