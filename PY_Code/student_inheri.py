class student:
    def __init__(self):
        self.roll=None
        self.marks=None
        self.name=None
    
    def inp(self):
        print("Enter roll: ")

class Himanshu(student):
    def dis(self):
        self.roll=1
        self.name="HRaj"
        self.marks=90

        print(f"{self.roll} {self.name} {self.marks}")

class student_inheri:
    if __name__=="__main__":
        h=Himanshu()
        h.inp()
        h.dis()