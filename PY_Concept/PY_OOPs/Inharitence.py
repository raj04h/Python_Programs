class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def bark(self):
        return "Dog barks"

# Creating instances
dog = Dog()
print(dog.speak())  # Output: Animal speaks
print(dog.bark())   # Output: Dog barks
