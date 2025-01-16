class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most birds can fly but some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Penguin(Bird):
    def flight(self):
        print("Penguins cannot fly.")

# Create objects
bird = Bird()
sparrow = Sparrow()
penguin = Penguin()

# Access methods
bird.flight()     # Output: Most birds can fly but some cannot.
sparrow.flight()  # Output: Sparrows can fly.
penguin.flight()  # Output: Penguins cannot fly.
