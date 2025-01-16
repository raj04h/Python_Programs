class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    @staticmethod
    def bark():
        return "Woof Woof"

# Instantiate the Dog class as object
mikey = Dog("Mikey", 6)

# Access the instance attributes
print(mikey.description())  # Output: Mikey is 6 years old.
print(mikey.speak("Woof Woof"))  # Output: Mikey says Woof Woof
