def count_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

uppercase, lowercase = count_case("Hello World!")
print(f"Uppercase letters: {uppercase}, Lowercase letters: {lowercase}")
# Output: Uppercase letters: 2, Lowercase letters: 8
