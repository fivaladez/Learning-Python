#EJ24_P2    Classes 2

# NOTES:
#       - names of a class always starts with capital letter
#       - the name of the class is the name of the file
#       - when you define a class, you need at lest one line
#       - you should not capitalize the name of a field and should sepera words by "_"
#       - Always use description comments for functions and Classes

class User:
    """This class is just for learning how a class works"""
    __secret_count = 0
    def __init__(self, full_name, birthday):
        """This is a constructor for class User"""
        self.name = full_name
        self.birthday = birthday
        self.__secret_count += 1
    def __del__(self):
        """This is a destructor for class User"""
        class_name = self.__class__.__name__
        print class_name, "destroyed"

user = User("Ivan", "09/02/1996")
print user.name
print user.birthday
help(User)
#Below comment not allowed
#print user.__secret_count
#To see hide data use:
print user._User__secret_count
del user
#Below comment not allowed because it doesn't exist any more
print user.name
