#!usr/bin/env python3
class Person:

    def __init__(self, name, age, height, sex):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__sex = sex

    def talk(self):
        print(f"Hi there you told me to talk")

    def walk(self):
        print(f"Hi! {self.__name} here. Just imagine I'm walking")

    def __str__(self):
        return f"This person is called {self.__name} and is {self.__age} years \
and is {self.__height}cm tall"

        
def main():

    person1 = Person("Tuva", 23, 178, "male")

    person1.walk()

    print(dir(person1))

    
main()
