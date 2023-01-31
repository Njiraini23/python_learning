class User:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday
user = User("Dave Bowman", "19910426")
print(user.name)
print(user.birthday)
