#EJ24_P2    Classes 2

# NOTES:
#       - names of a class always starts with capital letter
#       - the name of the class is the name of the file
#       - when you define a class, you need at lest one line
#       - you should not capitalize the name of a field and should sepera words by "_"
#       - Always use description comments for functions and Classes

class User:
    """This class is just for learning how a class works"""
    def __init__(self, full_name, birthday):
        """This is a constructor for class User"""
        self.name = full_name
        self.birthday = birthday

user = User("Ivan", "09/02/1996")
print user.name
print user.birthday
help(User)
