class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I am studying {self.course}.")

student1 = Student("Rod Jette", 21, "Computer Science")
student2 = Student("Kian", 22, "Information Technology")
student3 = Student("Irish", 19, "Business Administration")

student1.introduce()
student2.introduce()
student3.introduce()
