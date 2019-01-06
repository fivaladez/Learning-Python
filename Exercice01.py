#Exercice00 - For practicing basic topics from python language
class DadClass:
    #Docstring
    """ This is a message for getting knoledge about the class"""
    __name = ""
    __age  = 30
    height = 1.80
    weight = 80.0
    def __init__(self,name, age, height, weight):
        """This is a constructor"""
        self.__name = name
        self.__age = age
        self.height = height
        self.weight = weight
    def GetAge(self):
        return self.__age
    def GetHeight(self):
        return self.height
    #NOTE: You shall always let the parameter self in a function inside of a class
    #      without it, it won't work. The function will create another variable
    #      instead of make reference to an existent one

class sonClass(DadClass):
    __activity = "Soccer"
    def getVar(self):
        return self.__activity

class daughterClass(DadClass):
    __vacationsDays = 10
    def getVar(self):
        return self.__vacationsDays

if __name__ == "__main__":
    #For getting info about the class
    help(DadClass)
    MyObjectParent = DadClass("Erick", 45, 1.75, 90)
    print MyObjectParent.height
    #print MyObjectParent.__age
    #Last line is impossible to get because variable "__age" is private and you only can have
    #access by an internal function of the class
    print MyObjectParent.GetAge()

    MyObjectSon = sonClass("Carlos", 22, 1.74, 80)
    print MyObjectSon.height
    print MyObjectSon.GetAge()
    print MyObjectSon.getVar()

    MyObjectDaughter = daughterClass("Monica", 17, 1.65, 55)
    print MyObjectDaughter.height
    print MyObjectDaughter.GetAge()
    print MyObjectDaughter.getVar()
