
'''
number = int(input("Enter a number: "))
factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print("Factorial:", factorial)
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
