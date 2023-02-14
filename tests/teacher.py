#!/usr/bin/env python3

class Teacher:

    def __init__(self, name, email, username, workid):
        self.__name = name
        self.__email = email
        self.__username = username
        self.__workid = workid

    def introduce(self):
        print(f"Hi there! My name is {self.__name} and I am a teacher")




