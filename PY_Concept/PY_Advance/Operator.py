# Without walrus operator
if (n := len([1, 2, 3])) > 2:
    print(f"List has {n} elements")

# Output: List has 3 elements

from typing import List

def greet_all(names: List[str]) -> None:
    for name in names:
        print(f"Hello, {name}")

greet_all(["Alice", "Bob", "Charlie"])

from typing import Union

def square_root(number: Union[int, float]) -> float:
    return number ** 0.5

print(square_root(25))    # Output: 5.0
print(square_root(16.0))  # Output: 4.0

x = 10

def func():
    global x
    x += 5
    print(x)

func()  # Output: 15

for index, value in enumerate(["a", "b", "c"]):
    print(index, value)

# Output:
# 0 a
# 1 b
# 2 c




