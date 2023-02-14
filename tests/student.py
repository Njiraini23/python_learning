#!bin/usr/bin/env python3

class Student:

    def __init__(self, name, email, username, adm_no):
        self.__name = name
        self.__email = email
        self.__username = username
        self.__adm_no = adm_no

    def introduce(self):
        print("Hi there! My name is {self.__name} and I am a student")
