# Read entire file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Read one line at a time
with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()

# Read all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line, end="")

with open("example.txt", "r") as file:
    content = file.read(10)  # Read first 10 bytes
    print(content)


# Write a single string
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Write multiple lines
lines = ["I am python developer and I am currently working on the project based on the AI.\n", "Second line\n", "Third line\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)

with open("example.txt", "r") as file:
    content = file.read()
    print(content)



