class Student:
    print("Hi Student")

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.percentage = self.perc(self.marks)
        
        if self.percentage >= 75:
            print(f"Eligible. Adding {self.name} as Student in Database.")
        else:
            print(f"{self.name} your are not eligible.")

    def perc(self, marks):
        self.marks = (marks/200) * 100
        return self.marks

if __name__ == "__main__":
    name = input("Enter your Name: ")
    marks = int(input("Enter the total marks you got out of 200: "))
    s1 = Student(name, marks)