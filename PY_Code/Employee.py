class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_employee(self):
        return f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}"

# Creating instances
person = Person("Alice", 30)
employee = Employee("Bob", 25, "EMP123")

print(person.display_person())    # Output: Name: Alice, Age: 30
print(employee.display_employee())    # Output: Name: Bob, Age: 25, Employee ID: EMP123
