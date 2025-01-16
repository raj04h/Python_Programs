try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print(e)
else:
    print(f"You are {age} years old")
finally:
    print("End of program")
