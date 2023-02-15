#!/usr/bin/env python3

from teacher import Teacher
from student import Student
from user import User

teacher1 = Teacher('Tuva', 'tuva@gmail.com', 'tuva001', 443)

teacher1.introduce()

print(dir(teacher1))


#student1 = Student('Cynthia', 'cyn@gmail.com', 'cyn020', 110)

#student1.introduce

#user1 = User('Tuva', 'tuva@gmail.com', 'tuva001')
#user1.introduce()
