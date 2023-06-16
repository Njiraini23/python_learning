class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Not a name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]: 
            Raise ValueError("Inavlid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def main():
        student = get_student()
        print(student)

    def get_student():
        name = input("What's your name? ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return
