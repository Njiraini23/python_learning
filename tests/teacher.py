#!/usr/bin/env python3

from user import User

class Teacher(User):

    def __init__(self, name, email, username, work_id):
        super().__init__(name, email, username)
        self.__work_id = work_id

    def introduce(self):
        print(f"Hi there! My name is {self.__name} and I am a teacher")




