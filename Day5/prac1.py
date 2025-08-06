class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

        print(f"Hi, {self.name}.")
        self.avgMarks()
        
    def avgMarks(self):
        print(f"Your avg marks is: ", sum(self.marks)/3)

if __name__ == "__main__":
    name = input("Enter your Name: ")
    n = int(input("Enter number of subjects: "))
    marks = []
    for i in range (n):
        marks.append(int(input(f"Enter your marks for subject {i + 1}: ")))

    s = Student(name, marks)