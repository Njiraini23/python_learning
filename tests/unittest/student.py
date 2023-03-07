#!usr/bin/env python3

class Student:
    school = "Alx Africa"

    def __init__(self, name, course):
        self.name = name
        self.course = course

Student1 = Student("Jane", "JavaScript")
Student2 = Student("John", "Python")

print(Student1.name)
print(Student2.name)
print(Student1.course)
print(Student2.course)
