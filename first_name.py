class User:
    """A member of FriendFace. For now we are only storing their name and birthday. But soon we will store an uncomfortable amount of user information."""

def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday

        #extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

help(User)


